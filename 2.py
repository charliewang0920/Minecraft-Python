# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 15:32:01 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create ()
while True:
    x,y,z = Hi.player.getTilePos()
    Hi.postToChat("I'm watching you"+" x"+str(x)+" ,y"+str(y)+" ,z"+str(z))
    time.sleep(3)