# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:19:08 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hi = Minecraft.create()
x,y,z = Hi.player.getTilePos()
Hi.setSign(x,y,z,63,0,"","重生地點","","")