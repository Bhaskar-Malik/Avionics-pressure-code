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
While learning plotting data from excel,I found a better way to represent the data other than loop so I made both of them into different functions with a choice to choose any one using if else bcz I didnt want to change what I made using my own logic
I found out that I was obtaining pressure vs Altitude data but Alti vs time vas required
Now I had used pandas to plot the graph for velocity vs time as well

Hello Bhaiya/Di,I tried to explain this part my best but god knows how clear it is to you:

Now I had to deal with **** data so q=what I did I found difference between consecutive velocitires like if data is
v    t
4    1
6    2
8    3

I found difference between 4 and 6 and then 6 and 8 like that and then divivded them by 1 ie time difference,
it meant i got acceleration for each now I plotted data for acceleration and time wrt to the altitude vs time and
it came out to be almost constant and the values themselves were moving with diff of 0.X so considering this
I took the accleration of previous one of *** and the next one of *** which had in themselves diff of 0.3
only and took their avg,now I had accln and time,I got velocity from there and then altitude which came out to 
be 333.52m

After that i came to know about linear interpolation,I applied it using previous and next value of **** and got altitude of 322.3728m,the diff was of 11m between my method and linear interpolation and that for velocity was only 0.2 m/s although I feel that both methods were similar,I used the linear interpolation data for my work.
