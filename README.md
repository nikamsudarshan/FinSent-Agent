# FinSent-Agent: Algorithmic Sentiment Analysis & Market Intelligence

**A modular financial intelligence agent that integrates real-time market data with VADER-based sentiment heuristics to quantify the impact of news cycles on asset volatility.**

---

## 🚀 Core Features

* **Real-Time Market Telemetry:** Automated retrieval of high-frequency stock data including OHLC (Open, High, Low, Close) metrics and trading volume.
* **Automated News Aggregation:** Dynamic polling of global financial news via API, filtering for temporal relevance within a 7-day window.
* **Quantitative Sentiment Analysis:** Implementation of the **VADER (Valence Aware Dictionary and sEntiment Reasoner)** algorithm to assign polarity scores to market headlines.
* **Corporate Metadata Extraction:** Systematic gathering of sector-specific info, industry classification, and market capitalization to provide contextual depth.

## 🛠 Technical Stack

The agent is built using a robust Python-based data science stack:

* **Data Acquisition:** `yfinance` for market data and `NewsApiClient` for global headlines.
* **Linguistic Analysis:** `vaderSentiment` for rule-based sentiment intensity scoring.
* **Data Processing:** `pandas` for time-series handling and data normalization.
* **Temporal Logic:** `datetime` for managing rolling look-back windows.

## 🏗 System Architecture (How it Works)

The agent follows a deterministic logic flow to ensure reproducible results:

1. **Ticker Initialization:** The user provides a standardized exchange symbol (e.g., AAPL, GOOGL).
2. **Market Data Polling:** The system executes a fetch request to Yahoo Finance for current-day price action and fundamental company metadata.
3. **News Retrieval:** A query is sent to the News API to pull the most recent 20 articles associated with the company’s legal name.
4. **Sentiment Scoring:** Each headline undergoes polarity analysis. A **Compound Score** is calculated; scores $\geq 0.05$ are classified as Positive, while scores $\leq -0.05$ are classified as Negative.
5. **Report Generation:** The agent synthesizes these disparate data streams into a unified terminal report for rapid decision-making.

---

## 🔬 Scientific & Research Relevance

In a research-centric environment like **IISc Bangalore**, this architecture serves as a foundation for several academic applications:

* **Behavioral Finance Studies:** Quantifying "market noise" and its correlation with short-term price deviations.
* **NLP Benchmark Testing:** Using the modular sentiment class as a baseline for testing more complex Transformer-based models (like FinBERT).
* **Automated Data Logging:** Providing a template for scheduled, autonomous data collection from web-based APIs for long-term longitudinal studies.

---

## 💻 Installation & Usage

### Prerequisites

* Python 3.8+
* A valid API Key from [NewsAPI.org](https://newsapi.org/)

### Setup

1. **Clone the Repository:**
```bash
git clone https://github.com/nikamsudarshan/FinSent-Agent.git
cd FinSent-Agent

```


2. **Install Dependencies:**
```bash
pip install yfinance newsapi-python vaderSentiment pandas

```


3. **Configure API Key:**
Open `AgnoFinancialAgent.py` and replace `'NEWS_API_KEY'` with your actual key.
4. **Run the Agent:**
```bash
python AgnoFinancialAgent.py

```



---

## 👨‍🔬 About the Author

I am a **Mechatronics Engineering student** at **New Horizon Institute of Technology** (affiliated with the **University of Mumbai**), currently in my second year. With a **Minor in Information Technology**, my work focuses on the intersection of hardware-software co-design and intelligent automation.

As the founding member of the **ARMORY Robotics Club**, I have led projects involving complex kinematics and gesture-controlled systems. I am deeply interested in applying my technical background in Python, C++, and Linux environments to rigorous Research & Development challenges at the intersection of AI and physical systems.
