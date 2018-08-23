# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 16:04:08 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create ()
while True:
    x,y,z= Hi.player.getTilePos()
    Hi.setBlock(x,y,z,103)
