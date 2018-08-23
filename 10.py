# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:36:12 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
while a<21:
    Hi.setBlock(x+30,y-1,z,x-30,y-30,z,57)
    z=z+1