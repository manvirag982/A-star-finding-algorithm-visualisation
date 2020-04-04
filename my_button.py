import pygame

class Button:
    def __init__(self,col_without,colwith_mse,x,y,w,h,font,text):
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.font=font
        self.text=text
        self.maincolour=col_without
        self.colortouch=colwith_mse
        self.col=col_without
    
    def show(self,scr):
        pygame.draw.rect(scr,self.maincolour,(self.x,self.y,self.w,self.h),0)
        scr.blit(self.font.render(self.text,1,[255,255,255]),(self.x+70,self.y+20))
    
    def touch(self, check):
        if pygame.Rect(self.x,self.y,self.w,self.h).collidepoint(check)==True:
            self.maincolour=self.colortouch
        else:
            self.maincolour=self.col   
    # if pressed key is left mouse button and collide position is in button range then return true        
    def pressed(self,mouse_pos,pressed):
        if pressed==(1,0,0):
            return pygame.Rect(self.x,self.y,self.w,self.h).collidepoint(mouse_pos)