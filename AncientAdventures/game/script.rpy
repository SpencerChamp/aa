# Names

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define l = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define b = Character("Boss", color="4F4F4F")
define i =

# Image Buttons/Screens

#screen day_dis:
    #text "{b}[weekday]{/b}" ypos .90 xpos .05

screen cubi_nav():
    imagebutton auto "door_%s":
        xpos 1520
        ypos 180
        focus_mask True
        action [Hide ("cubi_nav"), Jump ("insula_ext")]
    imagebutton auto "bed_%s":
        focus_mask True
        action [Jump ("cubi")]

screen ins_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ins_nav"), Jump ("street_n1")]

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
        action [Hide ("forum_nav"), Jump ("street_s1")]
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_n1")]

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
        action [Hide ("port_nav"), Jump ("street_s1")]

label day_change:
    if weekday_number == 7:
        $ weekday_number = 1
    else:
        $ weekday_number += 1

    if weekday_number == 1:
        $ weekday = "SOL"
    elif weekday_number == 2:
        $ weekday = "LUN"
    elif weekday_number == 3:
        $ weekday = "MAR"
    elif weekday_number == 4:
        $ weekday = "MER"
    elif weekday_number == 5:
        $ weekday = "IOV"
    elif weekday_number == 6:
        $ weekday = "VEN"
    elif weekday_number == 7:
        $ weekday = "SAT"
    else:
        $ weekday = ":/"
    return

default weekday_number = 1
default weekday = "SOL"

## NEW DAY SYS (guy was mean so i gave up) ##

#default weekday = 0

#label day_change
    #$ weekday = (weekday+1) % 7
    #return

#define day_names = [ "SOL", "LUN", "MAR", "MER", "IOV", "VEN", "SAT" ]
    #$ today = day_names(weekday)

# The game starts here.

label start:
    with fade

    "It was a moonless night."

    scene bg found with fade

    "I was left outside a brothel."

    scene bg baby with fade

    "Iulia, the Matron, brought me in. A swaddled babe, carrying only an amulet, inscribed with my name..."

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

    "Thanks to Iulia's connections, I was able to secure a job at the port. My first day of work is tomorrow."

label cubi:
    scene bg cubi int with fade
    show screen cubi_nav
    show screen day_dis
    call day_change()

    show p basic with dissolve

    p "A dignified career and a new apartment..."
    p "No longer will I be the poor, orphaned whore-son."
    p "Today, I enter the noble city of Luna as a respectable citizen!"

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

    p "The port is directly South, past the Forum."

    show p basic:
        xzoom -1

    p "If I hit the sea I've gone too far."

    hide p basic with dissolve

    $ renpy.pause(hard=True)

label street_n1:
    scene bg street n1
    show screen sn1_nav

    $ renpy.pause(hard=True)

label forum:
    scene bg forum
    show screen forum_nav

    $ renpy.pause(hard=True)

label street_s1:
    scene bg street s1
    show screen ss1_nav

    $ renpy.pause(hard=True)

label port:
    scene bg port
    show screen port_nav

    show p basic at left with dissolve:
        xzoom -1

    p "Hm... Iulia told me to talk to the "

    pause .5

    show p basic at left:
        xzoom 1

    $ renpy.pause(hard=True)

    return
