from pixycamev3.pixy2 import Pixy2

# set port and i2c address
pixy2 = Pixy2(port=1, i2c_address=0x54)

# get version
version = pixy2.get_version()
print('Hardware: ', version.hardware)
print('Firmware: ', version.firmware)

# get frame resolution
resolution = pixy2.get_resolution()
print('Frame width: ', resolution.width)
print('Frame height: ', resolution.height)

# Turn upper leds on for 2s, then turn off
pixy2.set_lamp(1, 0)
sleep(2)
pixy2.set_lamp(0, 0)

# Track blocks with signature 1, request just 1 block wile true:
nr_blocks, blocks = pixy2.get_blocks(1, 1)
# extrack data of first (and only) block
if nr_blocks >= 1:
    sig = blocks[0].sig
    x = blocks[0].x_center
    y = blocks[0].y_center
    w = blocks[0].width
    h = blocks[0].height
    print('The x-axis of the block is: ', x)
    print('The y-axis of the block is: ', y)
    print('The width of the block is: ', w)
    print('The height of the block is: ', h)



