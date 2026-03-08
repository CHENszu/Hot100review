import random
import time
import shutil
import sys
import os

def matrix_rain():
    # Setup terminal
    try:
        columns, rows = shutil.get_terminal_size(fallback=(80, 24))
    except:
        columns, rows = 80, 24
    
    # Characters to display (Katakana-like or just ASCII)
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&*()_+"
    
    # Track the remaining length of the stream for each column
    # 0 means no stream currently
    drops = [0] * columns
    
    try:
        # Clear screen
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')
            
        print("\033[32m") # Set color to green once
        
        while True:
            line = ""
            for i in range(columns):
                if drops[i] > 0:
                    # Print a random character
                    char = random.choice(chars)
                    # Occasionally make a character white (head of stream effect)
                    if random.random() > 0.95:
                         line += f"\033[37m{char}\033[32m"
                    else:
                         line += char
                    drops[i] -= 1
                else:
                    line += " "
                    # Random chance to start a new stream
                    # Lower probability to prevent screen filling up too much
                    if random.random() > 0.98:
                        drops[i] = random.randint(5, rows // 2)
            
            print(line)
            
            # Sleep to control speed
            time.sleep(0.05)
            
    except KeyboardInterrupt:
        print("\033[0m") # Reset color
        print("\nMatrix Rain stopped.")
        sys.exit()

if __name__ == "__main__":
    matrix_rain()
