import pygame
import my_start_end
from my_node import Node 
import my_button
# from math import sqrt
# from random import randint, choice


pygame.init() # initialiser


sz = [1100, 700]
scr = pygame.display.set_mode(sz)   # frame width=1100, height=700
pygame.display.set_caption('MV A Star Visual') # yeah name


ps = my_start_end.Node(20, 20, 0)
pe = my_start_end.Node(660, 660, 1)

grid = []
graphgrid = []

for i in range(0, 700, 20):
    for j in range(0, 700, 20):
        grid.append(Node(j, i, 'hide', ps, pe))
        graphgrid.append(pygame.Rect(j, i, 20, 20))

#list for algorithm
open_list=[]
closed_list=[]


# find starting grid
for x in grid:
    if x.g == 0:
        start_node = grid.index(x)

# curr_node =start_node
# final_node
done = True



font = pygame.font.SysFont('ariel',25)

button_start = my_button.Button([51,51,51], [70,70,70], 800, 20, 200, 50, font, 'Start')
button_inc = my_button.Button([51,51,51], [70,70,70], 800, 300, 200, 50, font, '+')
button_dec = my_button.Button([51,51,51], [70,70,70], 800, 400, 200, 50, font, '-')



##############best feature i like delay
# delay var
value=0
step=0


once = 0



def startgui(scr):
    scr.fill((204,242,238))

    pygame.draw.rect(scr,[39,119,111],(2,2,695,695),3)
    pygame.draw.line(scr,[0,0,0],(710,200),(1100,200),3)

    button_start.show(scr)
    button_inc.show(scr)
    button_dec.show(scr)
                        
    scr.blit(font.render('Delay {}'.format(value),1,[0,0,0]),(800,500))
    
    ps.show(scr)
    pe.show(scr)


start = False

walls = []

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:        #if any one press red cross buttom it will close
            # done=False
            pygame.quit()
        
             
    if not start:
              # starting scene
        
        # condition
         
        mouse_pos = pygame.mouse.get_pos()     #(x,y)
        ispressed = pygame.mouse.get_pressed()   #(button1,button2,button3)
        iskeypressed = pygame.key.get_pressed()    # bool
        
        startgui(scr)
        # since three button inc,dec,start a/c to change situation

        # if only touch not push --colour change of button

        button_start.touch(mouse_pos)
        
        if button_start.pressed(mouse_pos, ispressed):
            start = True
       
        button_inc.touch(mouse_pos)
        
        
        if button_inc.pressed(mouse_pos, ispressed):
            value+=1
       
        
        
        button_dec.touch(mouse_pos)

        if button_dec.pressed(mouse_pos,ispressed):
            value-=1


       #edit start node, end node, make wall

    #    if wall

        if ps.update_pos(mouse_pos, ispressed, graphgrid) == False and pe.update_pos(mouse_pos, ispressed, graphgrid) == False:
            if ispressed == (1,0,0):
                ix=pygame.Rect(mouse_pos[0],mouse_pos[1],1,1).collidelist(graphgrid)
                if ix != -1:
                    if graphgrid[ix][0] != ps.x and graphgrid[ix][1] != ps.y or graphgrid[ix][0] != pe.x and graphgrid[ix][1] != pe.y:
                        walls.append(graphgrid[ix])

        

        #  asigning grid as wall  and draw
        for w in walls:
            pygame.draw.rect(scr,[38,119,111],w,0)

        for x in grid:
            x.show(scr)

        
        
        # ending all statics part and assigning wall in grid

    if start and once == 0:
        for node in grid:
            node.heuristic(ps,pe)

               #assigning wall in grid
            for w in walls:
                if node.x == w[0] and node.y == w[1]:
                    node.mode ='wall'

            if node.g==0:
                start_node = grid.index(node) 

            #if value is negative
        if value < 0:
            value=0        

            #basic step of algo
        open_list.append(grid[start_node])
        grid[start_node].mode='open_list'
        curr_node=grid[start_node]

        once+=1  # we want setup only one time


        # now the time has come for writing algo
        # for understanding algo see any youtube video
       
    if start:
        if step == value:

            if len(open_list) == 0:
                break

            for c in grid:
                c.show(scr)

            pygame.draw.circle(scr,[255,255,255],(ps.x+10,ps.y+10),10)
            pygame.draw.circle(scr,[255,0,255],(pe.x+10,pe.y+10),10)

                # a/c to algo
                
            minif=10**10
            minih=10**10
            for node in open_list:
                if node.f < minif:
                        minif=node.f
                        minih=node.h
                        curr_node=node
                    
                elif node.f==minif:
                        if node.h<minih:
                            minif=node.f
                            minih=node.h
                            curr_node= node

                
            open_list.remove(curr_node)
            closed_list.append(curr_node)
            curr_node.mode='closed_list'

            neighbour=[]

            for node in grid:
                if node.x == curr_node.x + 20 and node.y == curr_node.y:  
                    neighbour.append(node)

                if node.x == curr_node.x - 20 and node.y == curr_node.y:
                    neighbour.append(node)

                if node.x == curr_node.x and node.y == curr_node.y + 20:
                    neighbour.append(node)

                if node.x == curr_node.x and node.y == curr_node.y - 20:
                    neighbour.append(node)


            for node in neighbour:
                if closed_list.count(node)== 0 and node.mode !='wall':
                    if open_list.count(node)==0:
                        open_list.append(node)
                        node.mode='open_list'
                        
                    node.parent=curr_node

            if curr_node.x==pe.x and curr_node.y==pe.y:
                    done = False 
                    # final_node=curr_node    

            step=0
        else:
            step+=1       

    pygame.display.update()

# aadding some fancy path

A_star_path=[]
temp_node=curr_node
while True:
    
    A_star_path.append(( int(temp_node.x)+10 ,int(temp_node.y)+10))
    temp_node=temp_node.parent

    if temp_node.x == ps.x and temp_node.y == ps.y:
        break
A_star_path.append((ps.x+10,ps.y+10))
A_star_path.reverse()
# A_star_path = []
# x, y = curr_node.x, curr_node.y
# while True:
#     A_star_path.append((x + 10, y + 10))
#     x, y = curr_node.parent.x, curr_node.parent.y

#     curr_node = curr_node.parent

#     if x == a.x and y == a.y:
#         break
# A_star_path.append((a.x + 10, a.y + 10))
# A_star_path.reverse()
    
step=0
    # this is for just annimation on line path
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
        

    for g in grid:
        g.show(scr)


    for i in range(0,len(A_star_path)-1):
        pygame.draw.line(scr,[0,0,0],A_star_path[i],A_star_path[i+1],4)

        
    pygame.draw.circle(scr,[255,255,255],(ps.x+10,ps.y+10),10)
    pygame.draw.circle(scr,[255,0,255],(pe.x+10,pe.y+10),10)
 
         
    pygame.draw.circle(scr,[255,0,0],(A_star_path[step][0],A_star_path[step][1]),10)

        #infinite time
    if step != len(A_star_path)-1:
        step+=1
    else:
        step=0

    pygame.display.update()