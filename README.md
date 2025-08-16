Please see this in code type to see it properly
So here is how I did the tasks
Task 1
I saw tutorials of github and set it up
I tried using panda lib to directly take it from google sheets but it showed error 401:Unauthorized
So I downloaded it as excel sheet and directly operated in it using pd.read_excel instead of converting it into csv
Then i tried making it look better but there was a problem everytime i printed it it would go like ths
1 P1
2 P2
3 P3
.
.
.
83 P83
84 P84
which means it was not showing the whole data
But then i did hit and trial and came ton know that till 25 coloumns it shows full data
SO what I did I made it into a loop of 21 by using for loop on interval of 21 bcz 21X4=84 ie given number of columns and it worked in first try!!!
now it showed the whole data
Now the next task was to get altitide from the pressure data 
I learnt basic division and subtraction in excel and directly applied division by 12.3 in excel and subtracted initial altitude from all



