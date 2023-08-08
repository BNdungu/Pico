import machine
import time

# Define GPIO pins for trigger and echo
trigger_pin = machine.Pin(2, machine.Pin.OUT)  # GPIO2 (Pin 4) for trigger
echo_pin = machine.Pin(3, machine.Pin.IN)      # GPIO3 (Pin 5) for echo

def get_distance():
    # Set trigger pin to LOW for a short time to ensure a clean pulse
    trigger_pin.off()
    time.sleep_us(2)

    # Generate a 10us pulse on trigger pin to trigger the sensor
    trigger_pin.on()
    time.sleep_us(10)
    trigger_pin.off()

    # Measure the pulse duration on the echo pin
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    # Calculate the pulse duration in microseconds
    pulse_duration = time.ticks_diff(pulse_end, pulse_start)

    # Calculate distance using the speed of sound (343 m/s)
    distance = (pulse_duration * 0.0343) / 2

    return distance

# Main loop
while True:
    distance = get_distance()
    print("Distance: {:.2f} cm".format(distance))
    time.sleep(1)  # Delay for 1 second before next measurement
