from mcpi.minecraft import Minecraft
from time import sleep
from mcpi.effect import *
mc = Minecraft.create()


mc.postToChat("Hello")
x, y, z = mc.player.getPos()

look = mc.player.getEyeLocation()
print(look)

mc.player.effect("NIGHT_VISION", 10000, 1)

sleep(15)
blockHits = mc.events.pollBlockHits()
print(blockHits)
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
