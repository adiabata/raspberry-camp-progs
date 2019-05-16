from mcpi.minecraft import Minecraft
mc = Minecraft.create()

block = 42
x, y, z = mc.player.getPos()

for j in range(3):
    for i in range(5):
        mc.setBlocks(x - 5, y - 1, z - 5, x + 5, y, z + 5, 42)
        mc.setBlocks(x - 5, y, z - 5, x + 5, y + 4, z + 5, 20)
        mc.setBlocks(x - 4, y, z - 4, x + 4, y + 4, z + 4, 20)
        y = y + 4
    x = x + 10
    y = y - 20
