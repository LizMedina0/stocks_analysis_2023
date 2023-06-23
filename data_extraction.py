import numpy as np
import pandas as pd
import yfinance

sp_wiki_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
sp_list = pd.read_html(sp_wiki_url)
