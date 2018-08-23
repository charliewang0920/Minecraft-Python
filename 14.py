# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:04 2018

@author: NTPU
"""
import random, time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()

Pos = Hi.getTilePos

while True:
    x = Pos.x+random.uniform(-50,50)
    y = Pos.y+50
    z = Pos.z+random.uniform(-50,50)
    Hi.spawnEntity(x,y,z,93)