import websocket
import psycopg2
import json
from datetime import datetime

def on_message(ws, message):
    # Load the message as a JSON object
    message_json = json.loads(message)

    # Connect to your postgres DB
    conn = psycopg2.connect(dbname="postgres", user="jay", password="postgres", host="localhost")
    cur = conn.cursor()

    # Iterate over each item in the data array
    for item in message_json["data"]:
        # Extract the values
        message_type = message_json["type"]
        symbol = item["s"]
        last_price = item["p"]
        timestamp = datetime.fromtimestamp(item["t"]/1000.0)
        volume = item["v"]
        trade_conditions = item["c"]

        # Insert the data into the DB
        for condition in trade_conditions:
            cur.execute("INSERT INTO trades (message_type, symbol, last_price, timestamp, volume, trade_condition) VALUES (%s, %s, %s, %s, %s, %s)", (message_type, symbol, last_price, timestamp, volume, condition))

    # Commit the transaction
    conn.commit()
    print("Committed")

    # Close the cursor and the connection
    cur.close()
    conn.close()


def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### closed ###")

def on_open(ws):
    symbols = ["AMZN", "AAPL", "GOOG"]
    for symbol in symbols:
        ws.send(f'{{"type":"subscribe","symbol":"{symbol}"}}')

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("wss://ws.finnhub.io?token=<YOUR_FINNHUB_TOKEN_HERE>",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
