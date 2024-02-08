import RPi.GPIO as GPIO

# Define the GPIO pin for your button
SWITCH_PIN = 16
LED_PIN = 18

# Define debounce time in milliseconds
DEBOUNCE_TIME_MS = 200  # 200 milliseconds

# Set the initial state and pull-up resistor for the button
GPIO.setmode(GPIO.BCM) # Set the GPIO mode to BCM
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize the button state and previous state
switch_state = GPIO.input(SWITCH_PIN)
prev_switch_state = switch_state

# Define a function to handle button presses
def button_callback(channel):
    global switch_state
    switch_state = GPIO.input(SWITCH_PIN)

# Add an event listener for the button press
GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=button_callback, bouncetime=DEBOUNCE_TIME_MS)

try:
    # Main loop
    while True:
        # Check if the button state has changed
        if switch_state != prev_switch_state:
            if switch_state == GPIO.HIGH:
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
            
            prev_switch_state = switch_state


except KeyboardInterrupt:
    # Clean up GPIO on exit
    GPIO.cleanup()