from launchpad_rgb import Message
import mido


# Create a new Message object
msg = Message()


# zero indexed (row, col) values
msg.note(0, 0, 63, 0, 0) # r = 63, g = 0, b = 0


# Get the sysex data as bytes
sysex_data = msg()

# Print the sysex data
print(sysex_data)
print(type(sysex_data))


# Create an output port for your MIDI device
out_port = mido.open_output('Launchpad MK2:Launchpad MK2 MIDI 1 24:0')

# Convert sysex data to a mido SysexMessage
sysex_msg = mido.Message('sysex', data=sysex_data)

# Send the sysex message
out_port.send(sysex_msg)