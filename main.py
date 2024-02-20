import time
import board
import busio
from adafruit_htu21d import HTU21D

i2c = busio.I2C(board.GP27_A1, board.GP26_A0)
sensor = HTU21D(i2c)

#TODO: do scan to find device, if not port changes each time code runs
# take sample every 5 minutes or on request
temp = sensor.temperature
temp_f = temp * (9/5) + 32
humidity = sensor.relative_humidity
print("Temperature: %0.1f F" % temp_f)
print("Relative humidity: %0.1f%%" % humidity)