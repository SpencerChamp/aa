# Names

define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define p = Character("[pname]", color="9C0000")

# The game starts here.

label start:
    with fade

    "It was a moonless night."

    scene bg found
    with fade

    "I was left outside a brothel."

    scene bg baby
    with fade

    "Julia, the Matron, says I had only an amulet, inscribed with my name..."

    python:
        pname = renpy.input("Name?", length=32)
        pname = pname.strip()

        if not pname:
             pname = "Amator"

    scene
    with fade

    "I did not receive the most... respectable... education."

    scene bg younglife
    with fade

    "But I learned much of business and finance."

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    # show eileen happy


    v "Test."

    l "Test."
    p "test."

    return
