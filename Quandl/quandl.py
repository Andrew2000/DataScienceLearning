import pandas as pd
import quandl

"""
# When we need to get new data from quandl
df = quandl.get('WIKI/GOOGL')

# pickle it
df.to_pickle('quandlData.pkl')
"""
def getQuandlForGOOGL():
    df = pd.read_pickle('quandlData.pkl')

    # write data frame to csv
    # df.to_csv('quandlData.csv', encoding='utf-8')

    # write data frame to json
    # df.to_json('quandlData.json', orient='records', index=True)

    print(df.head)

if __name__=="__main__":
    getQuandlForGOOGL()