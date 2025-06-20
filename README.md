#  Hyperlocal Sentiment Dashboard

A Streamlit-based web app to collect, analyze, and visualize sentiment from Twitter, news sources, and surveys. This tool is designed to help political strategy and social research teams make informed, hyperlocal decisions.

##  Features
- 🐦 Live Twitter scraping using snscrape
- 📰 News sentiment from NewsAPI
- 📊 Sentiment analysis of uploaded surveys
- 🗺️ Interactive sentiment map (via Folium + GeoPandas)
- 📈 Time series visualization of sentiment trends
- 📄 Exportable admin summary PDF & CSV

##  Folder Structure
```
hyperlocal-sentiment-dashboard/
├── dashboard.py
├── requirements.txt
├── README.md
├── .streamlit/
│   └── config.toml
│   └── secrets.toml (only locally)
└── utils/
    ├── __init__.py
    ├── twitter_scraper.py
    ├── sentiment.py
    ├── news_fetcher.py
    ├── geo_utils.py
    └── pdf_report.py
```

## 🧑‍💻 Setup Instructions
```bash
git clone https://github.com/YOUR_USERNAME/hyperlocal-sentiment-dashboard.git
cd hyperlocal-sentiment-dashboard
pip install -r requirements.txt
streamlit run dashboard.py
```

##  Streamlit Cloud Deployment
1. Push this code to GitHub
2. Go to https://streamlit.io/cloud and sign in
3. Click "New App", select this repo and main file = `dashboard.py`
4. Add your secret API key:
```
# On Streamlit Cloud > Settings > Secrets
news_api_key = "YOUR_NEWSAPI_KEY"
```

##  Survey File Format
CSV file with at least this column:
```
content
"Modi government is doing great work in infrastructure."
"There is anger about electricity prices."
