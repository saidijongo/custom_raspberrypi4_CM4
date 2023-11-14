import RPi.GPIO as GPIO
import time

# Set GPIO mode to BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = [6,17, 13, 16, 18, 19, 12, 20, 21, 22, 23, 24]

for pin in led_pins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)


try:
    while True:
        # Turn on all LEDs
        for pin in led_pins:
            GPIO.output(pin, GPIO.HIGH)

        time.sleep(1)

        # Turn off all LEDs
        for pin in led_pins:
            GPIO.output(pin, GPIO.LOW)

        time.sleep(1)  

except KeyboardInterrupt:
    GPIO.output(led_pins, GPIO.LOW)
    GPIO.cleanup()
