from mcpi.minecraft import Minecraft
mc = Minecraft.create()

air = 0
gold = 41

while True:
	x, y, z = mc.player.getPos()
	block = mc.getBlock(x, y - 1, z)
	if block != air:
		mc.setBlock(x, y - 1, z, gold)