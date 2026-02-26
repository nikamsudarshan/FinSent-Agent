import yfinance as yf
from newsapi import NewsApiClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
from datetime import date, timedelta

# --- CONFIGURATION ---
# Replace with your own News API key
NEWS_API_KEY = 'NEWS_API_KEY'

class FinancialAgent:
    """
    A simple financial agent that provides stock data, news, and sentiment analysis.
    """

    def __init__(self, ticker):
        """
        Initializes the FinancialAgent with a stock ticker.

        Args:
            ticker (str): The stock ticker symbol (e.g., 'AAPL' for Apple).
        """
        self.ticker = ticker
        self.stock = yf.Ticker(self.ticker)
        self.newsapi = NewsApiClient(api_key=NEWS_API_KEY)
        self.analyzer = SentimentIntensityAnalyzer()

    def get_stock_data(self):
        """
        Retrieves and displays the latest stock data.
        """
        print(f"--- Stock Data for {self.ticker.upper()} ---")
        try:
            # Get today's data
            hist = self.stock.history(period="1d")
            if not hist.empty:
                print(f"Open:    ${hist['Open'].iloc[0]:.2f}")
                print(f"High:    ${hist['High'].iloc[0]:.2f}")
                print(f"Low:     ${hist['Low'].iloc[0]:.2f}")
                print(f"Close:   ${hist['Close'].iloc[0]:.2f}")
                print(f"Volume:  {hist['Volume'].iloc[0]:,}")
            else:
                print("No data available for the current day.")

            # Get company info
            info = self.stock.info
            print("\n--- Company Information ---")
            print(f"Company Name: {info.get('longName', 'N/A')}")
            print(f"Sector: {info.get('sector', 'N/A')}")
            print(f"Industry: {info.get('industry', 'N/A')}")
            print(f"Website: {info.get('website', 'N/A')}")
            print(f"Market Cap: ${info.get('marketCap', 0):,}")

        except Exception as e:
            print(f"An error occurred while fetching stock data: {e}")

    def get_financial_news(self):
        """
        Retrieves and displays the latest financial news for the company.
        """
        print(f"\n--- Recent News for {self.ticker.upper()} ---")
        try:
            # Calculate dates for the last 7 days
            to_date = date.today()
            from_date = to_date - timedelta(days=7)

            # Fetch news articles
            all_articles = self.newsapi.get_everything(
                q=self.stock.info.get('longName', self.ticker),
                from_param=from_date.strftime('%Y-%m-%d'),
                to=to_date.strftime('%Y-%m-%d'),
                language='en',
                sort_by='publishedAt',
                page_size=5
            )

            if all_articles['articles']:
                for i, article in enumerate(all_articles['articles']):
                    print(f"{i+1}. {article['title']}")
                    print(f"   Source: {article['source']['name']}")
                    print(f"   Published: {pd.to_datetime(article['publishedAt']).strftime('%Y-%m-%d %H:%M')}")
                    print(f"   URL: {article['url']}")
            else:
                print("No recent news found.")
        except Exception as e:
            print(f"An error occurred while fetching news: {e}")
            if "apiKeyInvalid" in str(e):
                print("Please check if your News API key is correct in the configuration.")


    def analyze_sentiment(self):
        """
        Analyzes the sentiment of recent news headlines.
        """
        print(f"\n--- Sentiment Analysis for {self.ticker.upper()} ---")
        try:
            to_date = date.today()
            from_date = to_date - timedelta(days=7)

            all_articles = self.newsapi.get_everything(
                q=self.stock.info.get('longName', self.ticker),
                from_param=from_date.strftime('%Y-%m-%d'),
                to=to_date.strftime('%Y-%m-%d'),
                language='en',
                sort_by='publishedAt',
                page_size=20 # Get more articles for better analysis
            )

            if not all_articles['articles']:
                print("No news available to analyze sentiment.")
                return

            compound_scores = []
            for article in all_articles['articles']:
                sentiment = self.analyzer.polarity_scores(article['title'])
                compound_scores.append(sentiment['compound'])

            if compound_scores:
                average_sentiment = sum(compound_scores) / len(compound_scores)
                print(f"Average Sentiment Score: {average_sentiment:.2f}")

                if average_sentiment >= 0.05:
                    print("Overall Sentiment: Positive")
                elif average_sentiment <= -0.05:
                    print("Overall Sentiment: Negative")
                else:
                    print("Overall Sentiment: Neutral")
            else:
                print("Could not analyze sentiment.")

        except Exception as e:
            print(f"An error occurred during sentiment analysis: {e}")

def main():
    """
    Main function to run the financial agent.
    """
    print("--- Simple AGNO Financial Agent ---")
    ticker_symbol = input("Please enter a stock ticker symbol (e.g., AAPL, GOOGL): ").strip().upper()

    if not ticker_symbol:
        print("No ticker symbol entered. Exiting.")
        return

    agent = FinancialAgent(ticker_symbol)
    agent.get_stock_data()
    agent.get_financial_news()
    agent.analyze_sentiment()
    print("\n--- End of Report ---")


if __name__ == "__main__":
    main()
