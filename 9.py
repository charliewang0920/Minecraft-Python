# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:48:30 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
a=Hi.getBlock(x+1,y-1,z)
b=Hi.getBlock(x-1,y-1,z)
c=Hi.getBlock(x,y-1,z+1)
d=Hi.getBlock(x,y-1,z-1)
while True:
    if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
        Hi.setBlock(x+1,y-1,z+1,x-1,y-1,z-1,103)