command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Hey! The Car is already started!")
        else:
            started = True
            print("The Car is started...")
    elif command == "stop":
        if not started:
            print("Hey! The Car is already stopped!")
        else:
            started = False
            print("The car is stopped...")
    elif command == "help":
        print("""
    start - to start the car
    stop - to stop the car
    quit - to exit the game
        """)
    elif command == "quit":
        print("Thank you for playing, and come again!")
        break
    else:
        print("Sorry, I don't understand that.")

