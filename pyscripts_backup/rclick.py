from pynput import mouse

# Counter for clicks
click_counter = 0

def on_click(x, y, button, pressed):
    global click_counter
    if button == mouse.Button.right and pressed:
        click_counter += 1
        print('Right button pressed at ({}, {})'.format(x, y))
        if click_counter >= 2:
            # Stop the listener once we've recorded two clicks
            return False

# Collect events until released
with mouse.Listener(on_click=on_click) as listener:
    listener.join()
