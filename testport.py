import sys

print(len(sys.argv))

if len(sys.argv) > 2:
    port = sys.argv[1]
    state = sys.argv[2]
    print("Port : " + port)

    import gpiozero
    control = gpiozero.DigitalOutputDevice(port, active_high=False, initial_value=False)

    if state:
        control.on()
        print("Switching on")
    else:
        control.off()
        print("Switching off")
else:
    print("python testport.py [port] [state]")