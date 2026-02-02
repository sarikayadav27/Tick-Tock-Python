import time
import os  # For clearing the screen

while True:
    current_time = time.strftime("%H:%M:%S %p")  # 12-hour: %H, 24-hour: %I
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🕒 Digital Clock")
    print("----------------")
    print(current_time)
    time.sleep(1)


