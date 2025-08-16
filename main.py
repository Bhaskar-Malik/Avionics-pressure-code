import pandas as pd

'''sheet_id='1mJ23Fru44nqmm3Yn9CakJ3FT_Sp6XUITiH3_Ksy8nd0'   #sheet id
df=pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
print(df)'''

P_A=pd.read_excel(r"C:\Users\hp\Desktop\Raw_flight _data.xlsx")#raw pressure data
for i in range(0,84,21):
        print(P_A.iloc[i:i+21])
