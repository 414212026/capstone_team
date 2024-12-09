from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/portfolio_overview')
def portfolio_overview():
    return render_template('portfolio.html')

@app.route('/historic_stock_performance')
def historic_stock_performance():
    return render_template('historic_performance.html')

@app.route('/economic_data_&_news_sentiment')
def economic_news_indicators():
    return render_template('economic_news_indicators.html')

if __name__ == '__main__':
    app.run(debug=True)