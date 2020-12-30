# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 13:43:52 2020

@author: matt.dmv

This script will try to simulate selected NBA games for 2020-2021 season. At first we don't
expect great accuracy of predictions but as season goes along there will be more games from which
this script could calculate stats and predict games outcomes. Therefore, script should be more
accurate towards the end of the season.
"""

import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.library.parameters import Season, SeasonType, LeagueID

season='22020'

#all games in 2020-2021 season 
all_games_2021=leaguegamefinder.LeagueGameFinder(season_nullable=Season.default, 
                                                 season_type_nullable=SeasonType.regular,
                                                 league_id_nullable=LeagueID.default).get_data_frames()[0]

home_team=input('Home team (abbreviation): ')
away_team=input('Away team (abbreviation): ')

home_team=teams.find_team_by_abbreviation(home_team)
home_team_id=home_team['id']

away_team=teams.find_team_by_abbreviation(away_team)
away_team_id=away_team['id']

#home team games 
home_team_games=leaguegamefinder.LeagueGameFinder(team_id_nullable=home_team_id, 
                                                  season_nullable=Season.default, 
                                                  season_type_nullable=SeasonType.regular).get_data_frames()[0]
home_team_home_games=home_team_games[home_team_games['MATCHUP'].str.contains('vs.')]

#list of home team home games
home_team_home_games_list=home_team_home_games['GAME_ID'].to_list()

#home team home games points list
home_points=home_team_home_games['PTS'].to_list()

#home team home games opponents stats & points
home_team_home_games_opp_stats=all_games_2021[(all_games_2021['GAME_ID'].isin(home_team_home_games_list))&
                                              (all_games_2021['TEAM_ID']!=home_team_id)]

home_team_home_games_opp_points=home_team_home_games_opp_stats['PTS'].to_list()


#away team games
away_team_games=leaguegamefinder.LeagueGameFinder(team_id_nullable=away_team_id, 
                                                  season_nullable=Season.default, 
                                                  season_type_nullable=SeasonType.regular).get_data_frames()[0]
away_team_away_games=away_team_games[away_team_games['MATCHUP'].str.contains('@')]

#list of away team away games
away_team_away_games_list=away_team_away_games['GAME_ID'].to_list()

#away team away games points list
away_points=away_team_away_games['PTS'].to_list()

#away team away games opponents stats & points
away_team_away_games_opp_stats=all_games_2021[(all_games_2021['GAME_ID'].isin(away_team_away_games_list))&
                                              (all_games_2021['TEAM_ID']!=away_team_id)]

away_team_away_games_opp_points=away_team_away_games_opp_stats['PTS'].to_list()

