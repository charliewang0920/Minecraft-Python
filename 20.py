# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:13:47 2018

@author: NTPU
"""

import random
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()

for j in range(30):
    x,y,z=Hi.player.getTilePos()
    x=x+j
    for i in range(30):
        r = random.randrange(0,16)
        Hi.setBlock(x,y,z,35,r)
        z=z+1

Hi.postToChat("請用你的劍找出隱藏的鑽石方塊")
r = random.randrange(0,16)

while True:
    hits = Hi.events.pollBlockHits()
    if len(hits)>0:
        h = hits[0]
        
        block = Hi.getBlockWithData(h.pos)
        data = block.data
        
        if data==r:
            Hi.postToChat("You succeed")
            break
        elif data<r:
            Hi.postToChat("請找id大一點的顏色")
        elif data>r:
            Hi.postToChat("請找id小一點的顏色")