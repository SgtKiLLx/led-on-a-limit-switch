import RPi.GPIO as GPIO

SWITCH_PIN = 16
LED_PIN = 18

DEBOUNCE_TIME_MS = 200

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

switch_state = GPIO.input(SWITCH_PIN)
prev_switch_state = switch_state

def button_callback(channel):
    global switch_state
    switch_state = GPIO.input(SWITCH_PIN)

GPIO.add_event_detect(SWITCH_PIN, GPIO.BOTH, callback=button_callback, bouncetime=DEBOUNCE_TIME_MS)

try:
    
    while True:
       
        if switch_state != prev_switch_state:
            if switch_state == GPIO.HIGH:
                GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
            else:
                GPIO.output(LED_PIN, GPIO.LOW)  # Turn off LED
            
            prev_switch_state = switch_state


except KeyboardInterrupt:
    
    GPIO.cleanup()
