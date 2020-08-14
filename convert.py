import pandas as pd
df = pd.read_json (r'C:/Users/nmwamlima/Desktop/completeOut.json')
df.to_csv (r'C:/Users/nmwamlima/Desktop/rahisi_v3.csv', index = None)