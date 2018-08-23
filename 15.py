# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:09:16 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()


while True:
    hits = Hi.events.pollProjectileHits()
    if len(hits)>0:
        h = hits[0]
        x,y,z = h.pos.x, h.pos.y, h.pos.z
        Hi.createExplosion(x,y,z,150)