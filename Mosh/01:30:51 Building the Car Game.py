command = ""
started = False
while True:
    command = input("Enter command: ").lower()
    if command == "start":
        if started:
            print ("Car already started!")
        else:
            started = True
            print ("Car started!")
    elif command == "stop":
        if not started:
            print ("Car already stopped!")
        else:
            started = False
            print ("Car stopped!")
    elif command == "help":
        print ("""
Start - Start the car
Stop - Stop the car
Exit - Exit the program
""")
    elif command == "exit":
        break
    else: 
         print ("Invalid command!")