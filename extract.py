import json
import pandas as pd



file = open('result.json')



contact = json.load(file)['contacts']['list']
df = pd.DataFrame(contact)
df['Name'] = df['first_name'].str.strip() + df['last_name'].str.strip()
df  = df.rename(columns={'phone_number':'Phone'})
df = df[['Name','Phone']].copy()
# print(df.columns)
# print(df.head(10))
df.to_csv('contacts.csv')