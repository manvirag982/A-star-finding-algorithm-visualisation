import pygame
from math import sqrt

def distance(x1,y1,x2,y2):
    return sqrt((x1-x2)**2 + (y1-y2)**2)

class Node:
    def __init__(self, x, y, mode, str_node, end_node):
        self.x=x
        self.y=y

        self.h=int(distance(self.x,self.y,end_node.x , end_node.y))
        self.g=int(distance(self.x,self.y,str_node.x , str_node.y))
        self.f=self.g+self.h

        self.mode=mode
        self.parent=None
        self.size=0
        self.sizeMax=10
        # that's the magic 
    def show(self,scr):
        if self.mode=='wall':
            pygame.draw.rect(scr,[38,119,111],(self.x,self.y,20,20),0) # screen, color,rect contain x,y,height,weight  , thick
        if self.mode=='hide':
            pygame.draw.rect(scr,[38,119,111],(self.x,self.y,20,20),1) # screen, color,rect contain x,y,height,weight  , thick
        if self.mode=='open_list':
            pygame.draw.circle(scr,[0,0,138],(self.x+10,self.y+10),self.size) # screen, x,y , radius
        if self.mode=='closed_list':
            pygame.draw.circle(scr,[0,191,255],(self.x+10,self.y+10),self.size) # screen, color,x,y , radis  .... add + 10 otherwise it will come at top left corner of cell
        

        # for creating annimation in circle inrease its gradually
        if self.mode != 'hide' and self.mode != 'wall':
            if self.size < self.sizeMax:
                self.size += 1
    
    
    def heuristic(self , start_node , end_node):
        self.g=int(distance(self.x, self.y, start_node.x,start_node.y))
        self.h=int(distance(self.x,self.y, end_node.x,end_node.y))
        self.f=self.g + self.h
        