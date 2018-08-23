# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:17:35 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
#Hi.player.setPos(x+0.5,y,z+0.5)
Hi.setBlocks(x+1,y-1,z+1,x-1,y-1,z-1,11)
