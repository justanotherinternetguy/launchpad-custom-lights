import mido

# Define the SysEx message format
sysex_message = [0xF0, 0x00, 0x20, 0x29, 0x02, 0x18, 0x0B, 36, 100, 0, 0, 0xF7]
port_name = "Launchpad MK2:Launchpad MK2 MIDI 1 24:0"

# Define the MIDI output port
output_port = mido.open_output(port_name)

# Function to send the SysEx message
def send_sysex_message(message):
    output_port.send(mido.Message('sysex', data=message))

# Function to set the RGB values of an LED
def set_led_rgb(led, red, green, blue):
    sysex_message[7] = led
    sysex_message[8] = red
    sysex_message[9] = green
    sysex_message[10] = blue
    send_sysex_message(sysex_message)

# Example usage
set_led_rgb(1, 63, 0, 0)  # Set LED 1 to red
