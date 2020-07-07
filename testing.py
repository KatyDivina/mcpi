from mcpi.minecraft import Minecraft
from time import sleep
from mcpi.effect import *
mc = Minecraft.create("178.140.2.146")


mc.postToChat("Hello")
x, y, z = mc.player.getPos()

mc.dropItem(x, y, z+5, 369)
mc.player.give(354)



# data = look.replace("'", '').split(',')
# xraw = data[1].split("=")
# yraw = data[2].split("=")
# zraw = data[3].split("=")
#
# x = float(xraw[1])
# y = float(yraw[1])
# z = float(zraw[1])
# pos = map(float,)
#
# while True:
#     x, y, z = mc.player.getTargetBlock()
#     bID, bDATA = mc.getBlockWithData(x, y, z)
#     mc.setBlock(x, y, z, 41)
#     sleep(1)
#     mc.setBlock(x, y, z, bID, bDATA)
#
# mc.player.effect("NIGHT_VISION", 10000, 1)
#
# sleep(15)
# blockHits = mc.events.pollBlockHits()
# print(blockHits)
# while True:
#
#     look = mc.player.getEyeLocation()
#     #print(look)
#     block = look.split(' ')
#     print(*block, sep = '\n')

    # bb = mc.events.pollBlockHits()
    # print(*bb, sep="\n" )

    # cc = mc.events.pollBlockSwordHits()
    # print(*cc, sep="\n" )
