def displayMessage():
    print("Add message?")
    message = input()
    print("This is message {message}?".format(message = message))
    input()
    return message
