# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:20:21 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
while True:
    Hi.executeCommand("time add 20")
    time.sleep(0.01)






