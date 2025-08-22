Bhaiya/Di I hv worked really hard on this project and u will be able to see the dedication in mycode and the main point is I HARDLY USED CHATGPT OR ANY OTHER AI FOR THIS,I made my own logics and used them 
Thank you

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

It was time to make animation for graphs but that absolutely maddend me I tried every way for 2 days but the graph showed blank every time,I even tries usong chatgpt for this after frustration but sma eproblem.I came to know accidently that it works on normal output window and not on interactive Jupyter one but due to this I saw the given video multiple times to see what I was doing wrong and i noticed the first part of video where he was giving example by taking two lists for x and y,I thought about it deeply and thought to make a loop intead of writing another code to run a live csv file and then take dta a from that bla bla bla...After that I noticed animation(i)'s i and searched on google what it was so i came to know that it was frame and it goes like time??? 1,2,3 like that,here i knew what I had to do ,take two empty lists , altitude data as a  list but there was a prob,lists have commas in between but I wasnt going to put comma on everydata so I learnt how to add comma in excel sheet by addding it to one value and now I had data_alt ready,I used the i from animation(i) to append it in time list and 
alti[i] so alti[i] gave me data one by one and time 1,2,3 all using the frame rate i,no chatgpt no complex codes just pure brain and logic,I m proud of myself and I dont think anybody used this logic to plot the graphs!!!,anyway,after this I added color to graphs and put them in functions and then presented them in if else statements
I saw that the code looked really neat and i like it:} so I implemented it on graph plotting too.Then I added the comments I thought were required.

With this I ended the given task and Bhaiya/di I hv worked reaaly hard for this
THANK YOU ;>


