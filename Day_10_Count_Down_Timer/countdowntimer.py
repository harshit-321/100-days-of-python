import time

# Take input in seconds
seconds = int(input("Enter time in seconds: "))

while seconds > 0:
    mins, secs = divmod(seconds, 60)
    timer = f"{mins:02d}:{secs:02d}"
    print(timer, end="\r")  # overwrite line
    time.sleep(1)
    seconds -= 1

print("⏰ Time's up!")