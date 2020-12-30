# nba_simulator
![](https://upload.wikimedia.org/wikipedia/en/0/03/National_Basketball_Association_logo.svg)

## Intro
This simple script makes use of nba_api to predict NBA games outcome considering which team is playing on home court and which team is away.
Original script was developed by Ken Jee and can be found on his github repo NBA_Simulator (https://github.com/PlayingNumbers/NBASimulator). I tried to improve the script with taking into consideration which team is playing at home and which team is playing away. 

It is well known that some teams perform better on their homecourt becase of fans impact. Since the 2021 NBA season just started we can't expect accurate results at first, but as season goes along accuracy of the predictions should improve because there will be more data to calculate teams performances.   
Also, this season's games are played without crowds, so impact of homecourt could be taken away (in this case original script should be fine).

**used libraries:** random, pandas, numpy, nba_api

## How to use script
**1.** Open Command Prompt or Anaconda Prompt.

**2.** Navigate to directory containing simulator_script.py (in my case C:\Users\Korisnik\git_workspace\nba_simulator).
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/2.JPG)

**3.** Type command "python simulator_script.py" and press **Enter** to run the script.
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/3.JPG)

**4.** Input home team name abbreviation ('LAL' in the example stands for Los Angeles Lakers) and press **Enter**.
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/4.JPG)

**5.** Input away team name abbreviation ('NYK' in the example stands for New York Knicks) and press **Enter**.
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/5.JPG)

**6.** Input number of simulations you wish to run and press **Enter**.
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/6.JPG)

**7.** The script will do the rest and calculate winning percentages for both teams.
![](https://raw.githubusercontent.com/mattdmv/nba_simulator/main/guidebook/7.JPG)
