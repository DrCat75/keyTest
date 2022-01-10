import keyboard

while True:
    if keyboard.read_key() == "p":
        print("You pressed p")
        break

while True:
    if keyboard.is_pressed("q"):
        print("You pressed q")
        break
        