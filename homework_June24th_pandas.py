import pandas as pd

df_sample=\
pd.DataFrame([[1, '英語', 25],
[1, '国語', 63],
[1, '数学', 42],
[2, '地歴', 90],
[2, '英語', 44],
[3, '数学', 94]])

df_sample.columns = ["number","subject","score"]
#print(df_sample[[1,2]])
print(df_sample.groupby("subject").mean())

print(df_sample.groupby("subject").max())

print(df_sample.groupby("subject").min())
