import pandas as pd

df = pd.read_csv (
    r"C:\Coding\Netflix Review\CONTENT_INTERACTION\ViewingActivity.csv",
    index_col="Title",
    usecols=['Title', 'Profile Name', 'Start Time', 'Duration'],
    parse_dates=['Start Time'],

)
df['Duration'] = pd.to_timedelta(df['Duration'])
mdf = df[df.index.str.contains('Supernatural')]

pd.set_option('display.width', None)

print(mdf.groupby('Profile Name')[['Duration']].sum())
