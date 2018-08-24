# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 14:08:54 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z =Hi.player.getTilePos
Hi.setBlocks(x+100,y+5,z,20)