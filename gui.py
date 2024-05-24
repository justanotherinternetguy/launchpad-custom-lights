import mido
import pygame

numbers = list(range(11, 90))

# Use list comprehension to filter out numbers ending in 0
notes = [num for num in numbers]

print(notes)


pygame.init()

# Set up the display
display_width = 900
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Launchpad MK2 Simulator")

# Initialize the Launchpad
outport = mido.open_output('Launchpad MK2:Launchpad MK2 MIDI 1 24:0')


button_width = 50
button_height = 50
button_spacing = 1

# Define colors
button_off_color = (64, 64, 64)
button_on_color = (255, 0, 0)

buttons = []
for row in range(8):
    row_buttons = []
    for col in range(10):  # Change to 10 columns
        x = col * (button_width + button_spacing)
        y = row * (button_height + button_spacing)
        rect = pygame.Rect(x, y, button_width, button_height)
        row_buttons.append((rect, False))  # (rect, is_on)
    buttons.append(row_buttons)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle mouse click events
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for row in range(8):
                for col in range(10):  # Change to 10 columns
                    button_rect, is_on = buttons[row][col]
                    if button_rect.collidepoint(mouse_pos):
                        # Toggle button state
                        buttons[row][col] = (button_rect, not is_on)

                        # Send MIDI message to Launchpad
                        note = ((7 - row) * 10 + col)  # Change to 10 columns
                        note = notes[note]
                        if is_on:
                            outport.send(mido.Message('note_off', note=note))
                            print(note)
                        else:
                            outport.send(mido.Message('note_on', note=note, velocity=119))
                            print(note)

    # Clear the display
    display.fill((0, 0, 0))

    # Draw buttons
    for row in range(8):
        for col in range(10):  # Change to 10 columns
            button_rect, is_on = buttons[row][col]
            color = button_on_color if is_on else button_off_color
            pygame.draw.rect(display, color, button_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
