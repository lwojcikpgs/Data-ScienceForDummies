# Import the necessary packages
from consolemenu import *
from consolemenu.items import *
from titanic.script import displayMessage

# Create the menu
menu = ConsoleMenu("PGS Upskill", "Data science for Dummies")

menu.append_item(FunctionItem("Titanic", displayMessage))

# Finally, we call show to show the menu and allow the user to interact
menu.show()