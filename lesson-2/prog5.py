from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x = 5
z = -23
while True:
	x1, y1, z1 = mc.player.getTilePos()
      if (x == x1 and z == z1):
      	mc.postToChat('It is magic!')