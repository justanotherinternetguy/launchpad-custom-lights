from launchpad_rgb import Message
import mido

# Create a new Message object
msg = Message()

# Set LED 11 to red (RGB value 63, 0, 0)
msg.note(1, 1, 0, 1, 0)

# Get the sysex data as bytes
sysex_data = msg()

# Print the sysex data
print(sysex_data)


# Create an output port for your MIDI device
out_port = mido.open_output('Launchpad MK2:Launchpad MK2 MIDI 1 24:0')

# Convert sysex data to a mido SysexMessage
sysex_msg = mido.Message('sysex', data=sysex_data)

# Send the sysex message
out_port.send(sysex_msg)