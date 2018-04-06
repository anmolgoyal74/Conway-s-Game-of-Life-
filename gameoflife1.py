#!/usr/bin/env python

from visual import *
import random
import time
def two(sp,a):
    move_count=0;
    #right
    if ((a+1)%10 != 0) and stickers[a+1].color == (0,1,0):
        move_count=move_count+1;
    #left
    if ((a-1)%10 != 9) and stickers[a-1].color == (0,1,0):
        move_count=move_count+1;
        #bottom
    if a+10<100 and stickers[a+10].color == (0,1,0):
        move_count=move_count+1;    
        #top
    if a-10>=0 and stickers[a-10].color == (0,1,0):
        move_count=move_count+1;
	    
        #left top
    if a-11 >= 0:
        if a-10>=0 and ((a-1)%10 != 9) and stickers[a-11].color == (0,1,0):
            move_count=move_count+1;
	    
        #right bottom
    if a+11 < 100:
        if ((a+1)%10 != 0) and a+10<100 and stickers[a+11].color == (0,1,0):
            move_count=move_count+1;
	    
        #left bottom
    if a+9 <100 and a-1 >= 0:
        if ((a-1)%10 != 9) and ((a-1)%10 != 9) and  stickers[a+9].color == (0,1,0):
            move_count=move_count+1;
	    
        #right top
    if a-10 >= 0 and a+1<100:
        if ((a+1)%10 != 0) and a-10>=0 and stickers[a-9].color == (0,1,0):
            move_count=move_count+1;
            
    return move_count;
        

def brain():

    t1=[];
    t2=[];
    for sticker in stickers:
            if sticker.color==(1,0,0) and (two(sticker,stickers.index(sticker)) == 3):
                t1.append(sticker.pos);
            if sticker.color==(0,1,0) and (two(sticker,stickers.index(sticker))==2 or two(sticker,stickers.index(sticker))==3):
                t2.append(sticker.pos);
                                 
    print(t1);
    for sticker in stickers:
        for p in t1:
            if sticker.pos == p:
                sticker.color=(1,1,0);
        for t in t2:
            if sticker.pos == t:
                sticker.color=(1,1,0);
                
                       
def zero():
    for sticker in stickers:
        if sticker.color == (1,1,0):
            sticker.color=(0,1,0);
        else:
            sticker.color=(1,0,0);


stickers = []
g=10;
h=0;
for x in range(0, 10):
   h=0;
   for y in range(0, 10):
       sticker =box(pos=(h,g,0), size=(1,1,0.1), color=color.red)
       h=h+1.1;
       stickers.append(sticker);
   g=g-1.1;

stickers[13].color=(0,1,0)
stickers[16].color=(0,1,0)
stickers[27].color=(0,1,0)
stickers[33].color=(0,1,0)
stickers[37].color=(0,1,0)
stickers[45].color=(0,1,0)
stickers[44].color=(0,1,0)
stickers[46].color=(0,1,0)
stickers[47].color=(0,1,0)
   
#print(stickers.pos);           

for i in range(0,20):
     brain();
     zero();                                          
     time.sleep(0.1);                                          
                                               
                        
   

