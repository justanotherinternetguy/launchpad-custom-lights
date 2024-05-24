import mido
import random
import time

port_name = "Launchpad MK2:Launchpad MK2 MIDI 1 24:0"

all_leds = range(0, 120)  # All LED indices

def write_led(led_id, color_vel):
    midi_out.send(mido.Message('note_on', channel=0, note=led_id, velocity=color_vel))

def set_board_color(color):
    for led in all_leds:
        write_led(led, color)

def random_color():
    red_or_green = bool(random.randint(0, 1))  # Making sure the number is always >0 for one component
    return random.randint(int(red_or_green), 3) + \
           random.randint(int(not red_or_green), 3) * 16

if __name__ == "__main__":
    try:
        midi_out = mido.open_output(port_name)  # Launchkey InControl port
        midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x7F]))  # Switch to "InControl" mode
        
        while True:
            color = random_color()
            set_board_color(color)
            time.sleep(200)
    except KeyboardInterrupt:
        pass

    set_board_color(0)  # Turn off all LEDs
    midi_out.send(mido.Message.from_bytes([0x90, 0x0C, 0x00]))  # Disable "InControl" mode
    midi_out.close()
