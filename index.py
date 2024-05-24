import mido
import time

# staring index: 11
# 11-90 is index range

# List available output ports
output_ports = mido.get_output_names()
print(f"Available output ports: {output_ports}")

# Open the desired output port
port_name = "Launchpad MK2:Launchpad MK2 MIDI 1 24:0"

outport = mido.open_output(port_name)

# Function to send a note on message
def send_note_on(note, velocity):
    msg = mido.Message('note_on', note=note, velocity=velocity)
    outport.send(msg)


v = 119
# Iterate through all note numbers and send note on
for note in range(11, 90):
    send_note_on(note, v)
    print(f"Sent note on for note number {note} for v number {v}")
    time.sleep(0.05)
    # v += 1  
    # Add a delay if needed to see the LEDs light up

# Close the output port
outport.close()
