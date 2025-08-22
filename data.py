import pandas as pd
import matplotlib.pyplot as plt
#I made two ways two get data
def loop():#In this I made a loop which takes in i has input for loop 
         P_A=pd.read_excel(r"C:\Users\hp\Desktop\PvsA.xlsx")#I read excel
         for i in range(0,54,21):#A gap of 21 is done so i=1,22..
                   print(P_A.iloc[i:i+25])#iloc in integer location which is used tot ake data from the excel

def subplot():
        df=pd.read_excel("C:\\Users\\hp\\Desktop\\PvsA.xlsx",'Sheet1')#Reads the given sheet
        print(df)
#Made some choice based if-else
print("1.Loop statement(press 1)")
print("2.Subplot(press 2)")
ch=int(input("which one do you want to use"))
if ch==1:
         loop()
elif ch==2:
         subplot()
else:
         print("Please enter a valid choice")
