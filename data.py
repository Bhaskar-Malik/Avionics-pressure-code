import pandas as pd
import matplotlib.pyplot as plt
#I made two ways two get data
def loop():
         P_A=pd.read_excel(r"C:\Users\hp\Desktop\PvsA.xlsx")
         for i in range(0,54,21):
                   print(P_A.iloc[i:i+25])

def subplot():
        df=pd.read_excel("C:\\Users\\hp\\Desktop\\PvsA.xlsx",'Sheet1')
        print(df)

print("1.Loop statement(press 1)")
print("2.Subplot(press 2)")
ch=int(input("which one do you want to use"))
if ch==1:
         loop()
elif ch==2:
         subplot()
else:
         print("Please enter a valid choice")
