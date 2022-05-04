## price-scrapper

A simple yet useful tool to scrape cryptocurrency data.

The script access data by utilizing binance API, tranforms the incoming data and

exports a `.csv` file in the project directory named `scrapped_data.csv`.


## Instructions

In the project directory, install our libraries with the following command:

```
pip install -r requirements.txt
```

Next, configure binance at `config.py` file by adding your API_KEY and API_SECRET.

On lines 16-22 ouf our code `price_scrapper.py` provide your desired **PAIR** (e.g ETHUSDT),

time **INTERVAL** (e.g '3m' --> 3 minute data) and **LOOKBACK** period (e.g '1d' --> 1 day ago).


## Deploy

In the project directory, run the command:

```
python price_scrapper.py
```
