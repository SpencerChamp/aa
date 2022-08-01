# Names

define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define p = Character("[pname]", color="9C0000")

# The game starts here.

label start:
    with fade

    "It was a moonless night"

    scene bg found
    with fade

    "I was left in a outside a brothel"

    scene bg baby
    with fade

    "Julia, the Matron, brought me in. A swaddled babe, carrying only an amulet, inscribed with my name..."

    python:
        pname = renpy.input("Name?", length=32)
        pname = pname.strip()

        if not pname:
             pname = "Amator"

    scene black
    with fade

    "I did not receive the most... traditional... education."

    scene bg younglife
    with fade

    "But I was treated with care, and learned much of business and finance along the way."

    scene black
    with fade

    "Thanks to Julia's connections, I was able to secure a job at the port. My first day of work is tomorrow."


    scene bg cubi int
    with fade

    show p basic

    p "A dignified career and a new apartment..."
    p "No longer am I the orphaned whore-son. Today, I enter the noble city of Luna as a respectable citizen!"

    pause

    show p shocked
    p "Damn, I was supposed to be at the port before sunrise!"

    hide p shocked

    scene bg cubi ext

    p "The port is directly South, past the Forum. If I hit the Sea I've gone too far."

    return
