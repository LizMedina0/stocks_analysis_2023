import pandas as pd
import yfinance

sp_wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp_wiki_list = pd.read_html(sp_wiki_url)

sp_dataframe = sp_wiki_list[0]
company_list = sp_dataframe["Symbol"].values.tolist()

df = yfinance.download(company_list)

adj_close_df = df["Adj Close"]
close_df = df["Close"]
high_df = df["High"]
low_df = df["Low"]
open_df = df["Open"]
volume_df = df["Volume"]
range_df = high_df - low_df