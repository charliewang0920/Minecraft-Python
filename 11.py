# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:06:44 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()

block=int(input("Block ID"))
Hi.setBlock(x,y,z,block)