import random
import sys

while True:
    sys.stdout.buffer.write(b"Type in two numbers :\n")
    sys.stdout.flush()

    min = int(sys.stdin.buffer.readline())
    max = int(sys.stdin.buffer.readline())

    if min == max:
        sys.stdout.buffer.write(b"Type in different numbers")
        sys.stdout.flush()
        continue

    if min > max:
        sys.stdout.buffer.write(b"Type in numbers in ascending order")
        sys.stdout.flush()
        continue  
    break

guess = random.randint(min, max)
count = min 

sys.stdout.buffer.write(f"Type in a number betweern {min} and {max} ({count} Chances):\n".encode())
sys.stdout.flush()
for i in range(min):
    ans = int(input())
    if ans == guess:
        sys.stdout.buffer.write(b"Correct!\nCongulatulation\n")
        sys.stdout.flush()
        sys.exit(0)
    else:
        sys.stdout.buffer.write(b"Incorrect!\n")
        sys.stdout.flush()
        

sys.stdout.buffer.write(b"Game Over!\nThank you for playing\n")
sys.stdout.flush()


