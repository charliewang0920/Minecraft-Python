# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:59:10 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()

while True:
    hits = Hi.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        x,y,z = h.pos.x, h.pos.y, h.pos.z
        Hi.setBlock(x,y,z,41)