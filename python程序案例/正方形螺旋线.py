from turtle import *
n=1

for i in range(1,50):
    for j in[90,180,-90,0]:
        for t in["red","green","blue","purple","gold","violet"]:
            seth(j)
            pencolor(t)
            fd(n)
            n+=0.05
        
    

    
