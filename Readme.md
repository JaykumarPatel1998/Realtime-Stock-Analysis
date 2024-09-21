# Real-Time Trade Analytics Dashboard

---

## Q1. Introduction and Background
The motivation for choosing the topic of real-time trade analytics comes from the increasing importance of data-driven decision-making in the financial industry. The advent of high-frequency trading and algorithmic trading has made real-time trade data more valuable than ever. Inspiration for this project came from financial news outlets, fintech forums, and the growing trend of democratizing financial data through APIs like Finnhub.

This project is highly relevant in today's data-driven world. Financial markets are dynamic and volatile, with prices changing rapidly based on numerous factors. By analyzing real-time trade data, we aim to gain insights into market trends, detect anomalies, and make informed trading decisions. The goal is not only to understand financial markets better but also to leverage technology to respond to market changes effectively.

---

## Q2. Objectives and Goals
The primary objective of this project is to learn how to handle, analyze, and visualize real-time trade data. Some of the key questions we aim to answer include:
- What are the current market trends for a particular stock?
- How does trade volume fluctuate throughout the day?
- Are there any anomalies or unusual trading activities occurring?

### Benefits
- **For individual traders and investors:** Provides valuable insights for trading decisions.
- **For financial institutions:** Acts as a tool to monitor market trends and detect anomalies.

---

## Q3. Datasets
- **Source:** The dataset is available via the WebSocket Trades API provided by [Finnhub](https://finnhub.io/docs/api/websocket-trades).
- **Data Provider:** Finnhub, a global financial data provider offering APIs for real-time and historical stock prices, forex, and cryptocurrency.
- **Publications:** No specific publications are associated with this dataset, but it is widely used in financial analysis, algorithmic trading, and other fintech applications.
- **Dataset Size:** The dataset is dynamic and depends on the number of trades happening in real-time. Each trade record contains:
  - Type
  - Data
  - `s` (symbol)
  - `p` (last price)
  - `t` (UNIX timestamp in milliseconds)
  - `v` (volume)
  - `c` (list of trade conditions)
- **Geographic Locations:** Not applicable for this project.
- **Dataset Usefulness and Limitations:**
  - **Usefulness:** The dataset is invaluable for financial analysis and algorithmic trading. By analyzing trade volume and price data in real-time, we can detect patterns and make informed trading decisions.
  - **Limitations:** The dataset is highly volatile, requiring efficient handling of a large amount of changing data. Additionally, the lack of geographic data limits its use in location-based analyses.

---

## Q4. Visualization Plan
1. **Line Chart (Price Trend):** 
   - **X-axis:** Timestamp (`t`)
   - **Y-axis:** Last price (`p`)
   - Visualizes the price trend of a particular stock over time.

2. **Bar Chart (Trade Volume):**
   - **X-axis:** Timestamp (`t`)
   - **Y-axis:** Volume (`v`)
   - Illustrates the trade volume of a particular stock over time.

3. **Table (Trade Details):**
   - Columns: Symbol (`s`), last price (`p`), timestamp (`t`), volume (`v`), and trade conditions (`c`).
   - Provides a detailed view of each trade.

4. **Pie Chart (Trade Conditions Distribution):**
   - Visualizes the distribution of different trade conditions (`c`), offering an overview of the types of trades happening.

5. **Histogram (Price Distribution):**
   - Displays the distribution of trade prices using the last price (`p`), offering insight into common trade prices.

6. **Time Series Chart (Volume Over Time):**
   - **X-axis:** Timestamp (`t`)
   - **Y-axis:** Cumulative volume (`v`)
   - Shows how the total trade volume evolves over time.

## Data Collection Architecture
![image](https://github.com/user-attachments/assets/03020c7f-7cc2-4aa9-b8ae-dee440f170c2)

## Dashboard
![image](https://github.com/user-attachments/assets/0b68d7bc-e14b-4507-b24f-1521096742e0)

