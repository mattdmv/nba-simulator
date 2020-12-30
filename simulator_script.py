# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:21:25 2018

@author: matt.dmv
"""

from input_teams import *
from nba_simulator import *
import numpy as np

home = Team(home_team['full_name'], points_home=home_points, 
            opp_points_home=away_team_away_games_opp_points)
away = Team(away_team['full_name'], points_away=away_points, 
            opp_points_away=home_team_home_games_opp_points)

msim = MatchupSimulator(home, away)

n=int(input('Enter number of simulations: '))

msim.gamesSim(n)