# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:02:06 2018

@author: matt.dmv
"""

import pandas as pd 
import random as rnd
import numpy as np 
import matplotlib.pyplot as plt


class Team:
    """Team creates an object that can be passed into the simulation. Takes a Team Name (string)
    points_home(list), points_away (list), opp_points_home(list) and opp_points_away (list) """
    
    def __init__(self, TeamName, points_home=None, points_away=None, opp_points_home=None, opp_points_away=None):
        self.TeamName = TeamName
        self.points_home = points_home
        self.points_away = points_away
        self.opp_points_home = opp_points_home
        self.opp_points_away = opp_points_away
    
    #Returns avg of points in home games
    def pointsavg_home(self):
        return np.mean(self.points_home)
    
    #Returns avg of points in away games
    def pointsavg_away(self):
        return np.mean(self.points_away)
    
    #Returns standard deviation of points in home games
    def pointsstd_home(self):
        return np.std(self.points_home)
    
    #Returns standard deviation of points in away games
    def pointsstd_away(self):
        return np.std(self.points_away)
    
    #returns avg of opponent points in home games
    def opp_pointsavg_home(self):
        return np.mean(self.opp_points_home)
    
        #returns avg of opponent points in away games
    def opp_pointsavg_away(self):
        return np.mean(self.opp_points_away)
    
    #returns standard deviation of opponent points home games
    def opp_pointsstd_home(self):
        return np.std(self.opp_points_home)
    
    #returns standard deviation of opponent points in away games
    def opp_pointsstd_away(self):
        return np.std(self.opp_points_away)

class MatchupSimulator:
    """ Simulates single game outcomes as well as multiple outcomes;
        Team 1 is home team, Team 2 is away team
    """
    def __init__(self, Team1,Team2):
        self.Team1 = Team1 #home team
        self.Team2 = Team2 #away team
        self.results = []
    
    #Simulates a single game returns 1 if team 1 wins, returns -1 if Team 2 wins, 
    #and returns 0 if the game is tied
    def gameSim(self):
        #Averages the random sample of a teams points with a random sample of the number of
        #points the opponent allows (taking into consideration which team plays on home court)
        #Randomly samples from the two gaussian distributions to produce a probabilistic outcome
        T1 = (rnd.gauss(self.Team1.pointsavg_home(),self.Team1.pointsstd_home())+ rnd.gauss(self.Team2.opp_pointsavg_away(),self.Team2.opp_pointsstd_away()))/2
        T2 = (rnd.gauss(self.Team2.pointsavg_away(),self.Team2.pointsstd_away())+ rnd.gauss(self.Team1.opp_pointsavg_home(),self.Team1.opp_pointsstd_home()))/2
        if int(round(T1)) > int(round(T2)):
            return 1
        elif int(round(T1)) < int(round(T2)):
            return -1
        else: return 0
        
    def gamesSim(self,number_simulations):
        gamesout = []
        team1win = 0
        team2win = 0
        tie = 0
        for i in range(number_simulations):
            #calls the pervious game simulator and aggregates results
            gm = self.gameSim()
            gamesout.append(gm)
            if gm == 1:
                team1win +=1 
            elif gm == -1:
                team2win +=1
            else: tie +=1 
        print(self.Team1.TeamName + ' Win ', round((team1win/(team1win+team2win+tie)*100),2),'%')
        print(self.Team2.TeamName + ' Win ', round((team2win/(team1win+team2win+tie)*100),2),'%')
        print('Tie ', round((tie/(team1win+team2win+tie)*100),2), '%')
        print('Number of Simulations: ',number_simulations)
        #can see all results using self.results
        self.results = gamesout

    
