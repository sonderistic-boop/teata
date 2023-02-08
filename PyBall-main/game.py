#make game class, with a run method, and a main method
#game should be 810x770
import pygame as pg
import math
import sys

from entities.pawn import Pawn
from entities.ball import Ball
import entities.stadium.stadiums as stadiums
class Game():
    def __init__(self,parentScreen,players,stadium,colours):
        self.size = (810,770)
        self.parentScreen = parentScreen
        self.stadium = stadium
        self.leftTeam = {}
        self.rightTeam = {}
        
        
        
        #load game surface, load players, load ball, load stadium
        

        self.screen = pg.Surface((self.size),pg.SRCALPHA)
        
        self.stadium = getattr(stadiums,stadium)
        self.stadium = self.stadium(self.screen,200,200)
        
        self.ball = Ball(screen,(self.stadium.bounds["middle"][0],self.stadium.bounds["middle"][0]),(30,30))
        
        
        for i in players["team1"]:
            self.leftTeam.append{i : Pawn(i,colours["team1"],False,self.screen,(400,400),(70.3,70.3))           
        
        for i in players["team2"]:
            self.rightTeam.append{i : Pawn(i,colours["team2"],False,self.screen,(400,400),(70.3,70.3))     

        
        
        
        #add collision groupis
        
        for 
        




        self.ballgroup = pg.sprite.GroupSingle(self.ball)
        self.guygroup = pg.sprite.Group()

        for player in players:
            self.guygroup.add(Pawn(player[0],player[1],player[2],screen,(400,400),(70.3,70.3)))
        self.arc = Arc(screen,(600,400),30,(0,math.pi/2),(255,255,255,128))
        self.arcgroup = pg.sprite.GroupSingle(self.arc)
    