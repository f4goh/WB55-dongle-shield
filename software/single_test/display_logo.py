from machine import I2C, Pin
# display SSD1306 is connected on I2C1 of arduino connector
import framebuf
import ssd1306
import time

# ----------------------------------------
# screen parameters
SCREEN_WIDTH = 128
SCREEN_HEIGHT = 64

# ----------------------------------------
# READ Picture from file
def load_image(filename):
    with open(filename, 'rb') as f:
        f.readline()
        width, height = [int(v) for v in f.readline().split()]
        data = bytearray(f.read())
    return framebuf.FrameBuffer(data, width, height, framebuf.MONO_HLSB)


# ----------------------------------------
# search if i2c id are present on i2c bus
def isPresentOnI2C(i2c, i2c2_list, id_tofound):
    if i2c2_list is None:
        local_i2clist = self.i2c.scan()
    else:
        local_i2clist = i2c2_list
    for i in local_i2clist:
        if i == id_tofound:
            return 1
    return 0

# -------------------------------------------
# display ST logo
def display_logo(screen):
    if screen is not None:
        screen.fill(0)

        logo_pbm = load_image("logo_st.pbm")
        screen.blit(logo_pbm, 0, 0)

        screen.show()


# -------------------------------------------
# display temperature and humidity

# ---------------------------------------------
#                  main
# ---------------------------------------------
i2c1 = I2C(1)
display = None
if __name__ == '__main__':
    # scan i2c bus to see which ip components are present
    print(i2c1.scan())
    # wait to be sure all the component are present
    time.sleep_ms(1000)
    # init display
    #if isPresentOnI2C(i2c1, None, 60):
    display = ssd1306.SSD1306_I2C(SCREEN_WIDTH, SCREEN_HEIGHT, 60)

    # display log during 5 seconds
    display_logo(display)
    time.sleep_ms(5000)


