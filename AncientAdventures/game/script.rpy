# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pr = Character("Priapus")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid")
define p = Character("[pname]")

python:
    pname = renpy.input("What is your name?", length=32)
    pname = povname.strip()

    if not povname:
         povname = "Amator"

# The game starts here.

label start:

    with fade

    "It was a moonless night."

    scene bg found
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    v "Test."

    l "Test."

    return
