import pandas as pd
import math

#E
df = pd.read_csv("sample_products.csv")



#T
df["unit_price"] = df["unit_price"].apply(math.ceil)


#L
df.to_csv("output/clean_products.csv",index=False)
