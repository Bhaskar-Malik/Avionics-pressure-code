import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_excel("C:\\Users\\hp\\Desktop\\RFD_LI.xlsx",'Sheet1')
        
def plot_Altitude():    #Altitude VS Time
       plt.xlabel("Time(s)")
       plt.ylabel("Altitude(m)")    
       plt.plot(df['Time(s)'],df['Altitude(m)'])
def plot_Velocity():    #Velocity VS Time
       plt.xlabel("Time(s)")
       plt.ylabel("Velocity(m/s)")
       plt.plot(df['Time(s)'],df['Velocity(m/s)'])
def plot_Velfake():                                       #I made these two func without labels
                                                        # so that their labels are not shown 
         plt.plot(df['Time(s)'],df['Velocity(m/s)'])       #when used  together
def plot_Altfake():
        plt.plot(df['Time(s)'],df['Altitude(m)'])
#some choice based if-else statemnts

print("Altitude vs Time(Press 1)")
print("Velocity vs Time(Press 2)")
print("Both(Press 3)")
ch2=int(input("Which graph do you want to see:"))


if ch2==1:
        plot_Altitude()
elif ch2==2:
        plot_Velocity()
elif ch2==3:
        print("Orange graph for velocity vs time")
        print("Blue for Altitude vs Time")
        plot_Altfake()
        plot_Velfake()
else:
        print("Please enter a valid number")
plt.show()
