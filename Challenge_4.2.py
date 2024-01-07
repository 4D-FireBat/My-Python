# Challenge 4.2
# Creaet a program that gets a message from the user and then prints it out backwards

# Have the user enter a message.

message = input("Please enter a message: ")

print("\nI will now reverse your message.")

high = len(message)
low = -len(message)

newmessage = message[high,low]

print(message[high:0])

input("\n\nPress the enter key to exit.")
