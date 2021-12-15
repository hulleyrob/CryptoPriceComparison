# CryptoPriceComparison

Inspired by what i saw at https://itnext.io/create-beautiful-cryptocurrency-graphs-in-python-bec7b9cbc21a

I created this to do a relative comparison between coins that im interested in.

Maybe this can be useful for someone else looking to do the same.

To use you will need to:

    pip install pandas pandas_datareader plotly sklearn

Edit the CRYPTOS list for the coins your interested in (use https://finance.yahoo.com/cryptocurrencies/ for the correct names less the currency)

Once its finished getting the data it will open your default browser with an interactive graph.

Enjoy.

(The difference to the one in the link is this script normalises the data using max closing price within a 0-100% scale)
