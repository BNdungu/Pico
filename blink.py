import machine
import time

# Define the onboard LED pin
led_pin = machine.Pin(25, machine.Pin.OUT)

# Main loop
while True:
    led_pin.on()      # Turn the LED on
    time.sleep(0.5)   # Wait for 0.5 seconds
    led_pin.off()     # Turn the LED off
    time.sleep(0.5)   # Wait for 0.5 seconds
t