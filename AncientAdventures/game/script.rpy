# Names

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")


# Image Buttons

# The game starts here.

label start:
    with fade

    "It was a moonless night."

    scene bg found with fade

    "I was left outside a brothel."

    scene bg baby with fade

    "Julia, the Matron, brought me in. A swaddled babe, carrying only an amulet, inscribed with my name..."

    python:
        pname = renpy.input("Name?", length=32)
        pname = pname.strip()

        if not pname:
             pname = "Amator"

    scene black with fade

    "I did not receive the most... traditional... education."

    scene bg younglife with fade

    "But I was treated with care, and learned much of business and finance along the way."

    scene black with fade

    "Thanks to Julia's connections, I was able to secure a job at the port. My first day of work is tomorrow."


    scene bg cubi int with fade
    show screen cubi_nav

    screen cubi_nav():
        imagebutton auto "door_%s":
            xpos 1900
            ypos 500
            focus_mask True
            action Jump ("insula_ext")


    show p basic


    p "A dignified career and a new apartment..."
    p "No longer am I the orphaned whore-son. Today, I enter the noble city of Luna as a respectable citizen!"

    window hide
    pause
    show p shocked

    p "Damn, I was supposed to be at the port before sunrise!"

    window hide

label insula_ext:

    scene bg insula


    p "The port is directly South, past the Forum. If I hit the Sea I've gone too far."

    return
