# Names

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")


# Image Buttons/Screens

screen cubi_nav():
    imagebutton auto "door_%s":
        xpos 1520
        ypos 180
        focus_mask True
        action [Hide ("cubi_nav"), Jump ("insula_ext")]

screen ins_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ins_nav"), Jump ("streetn1")]

screen sn1_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("sn1_nav"), Jump ("forum")]
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("sn1_nav"), Jump ("insula_ext")]

screen forum_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("streets1")]
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("streetn1")]

screen ss1_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("port")]
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("forum")]

screen port_nav():
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("port_nav"), Jump ("streets1")]

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

    "I did not receive the most {i}traditional{/i} education."

    scene bg younglife with fade

    "But I was treated with care, and learned much of business and finance along the way."

    scene black with fade

    "Thanks to Julia's connections, I was able to secure a job at the port. My first day of work is tomorrow."

label cubi:
    scene bg cubi int with fade
    show screen cubi_nav

    show p basic with dissolve

    p "A dignified career and a new apartment..."
    p "No longer am I the orphaned whore-son. Today, I enter the noble city of Luna as a respectable citizen!"

    window hide
    pause
    show p shocked

    p "Damn, I was supposed to be at the port before sunrise!"

    window hide

    hide p shocked with dissolve

    $ renpy.pause(hard=True)

label insula_ext:
    scene bg insula
    show screen ins_nav

    show p basic with dissolve

    p "The port is directly South, past the Forum. If I hit the Sea I've gone too far."

    hide p basic with dissolve

    $ renpy.pause(hard=True)

label streetn1:
    scene bg street n1
    show screen sn1_nav

    $ renpy.pause(hard=True)

label forum:
    scene bg forum
    show screen forum_nav

    $ renpy.pause(hard=True)

label streets1:
    scene bg street s1
    show screen ss1_nav

    $ renpy.pause(hard=True)

label port:
    scene bg port
    show screen port_nav

    $ renpy.pause(hard=True)

    return
