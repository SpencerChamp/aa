# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define p = Character("[pname]", color="9C0000")

python:
    pname = renpy.input("On the back was inscribed...", length=32)
    pname = povname.strip()

    if not povname:
         povname = "Amator"

# The game starts here.

label start:

    with fade

    "It was a moonless night."

    scene bg found
    with fade

    python:
        pname = renpy.input("What is your name?", length=32)
        pname = pname.strip()

        if not pname:
             pname = "Amator"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy


    v "Test."

    l "Test."

    return
