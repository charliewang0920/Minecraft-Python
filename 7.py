# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 13:53:38 2018

@author: NTPU
"""

import random
import time
from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
Hi.setBlocks(x,y+5,z,)




