import pygame

class Node:
    def __init__(self,x,y,mode):
        self.x=x
        self.y=y

        self.pos=pygame.math.Vector2(self.x,self.y)
        self.mode=mode                   # mode=0 start,,mode=1,end
    
    def show(self,scr):
        if self.mode==0:
            pygame.draw.circle(scr,[0,0,0],(self.x+10,self.y+10),10)    # screen,color,coordinate,radius
        if self.mode==1:
            pygame.draw.circle(scr,[255,255,51],(self.x+10,self.y+10),10)    # screen,color,coordinate,radius
    
    # user changed position
    
    def update_pos(self,mouse_pos,pressed,matrix):
        # if user want to change the position of start or end node
        if pygame.Rect(self.x,self.y,20,20).collidepoint(mouse_pos) and pressed==(1, 0, 0):
            self.x=mouse_pos[0]-10 # change little position so jusk know
            self.y=mouse_pos[1]-10
            return True
        else:   #  either want to make a wall or nothing
            ix=pygame.Rect(self.x,self.y,20,20).collidelist(matrix)   #return index if found else -1
            if ix != -1:
                self.x=matrix[ix][0]
                self.y=matrix[ix][1]
            return False




