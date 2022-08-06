# Names

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define lun = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define g = Character("Gurges", color="4F4F4F")
define lup = Character("Lupa")

# Image Buttons/Screens

screen day_dis:
    text "{b}[weekday]{/b}" ypos .90 xpos .05

screen cubi_nav():
    imagebutton auto "door_%s":
        xpos 1520
        ypos 180
        focus_mask True
        action [Hide ("cubi_nav"), Jump ("insula_ext")]
    imagebutton auto "bed_%s":
        focus_mask True
        action [Jump ("cubi_wake")]

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
        tooltip "To the forum"
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("sn1_nav"), Jump ("insula_ext")]
        tooltip "Back home"

screen forum_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_s1")]
        tooltip "South"
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_n1")]
        tooltip "North"

screen ss1_nav():
    imagebutton auto "larrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("port")]
        tooltip "To the port"
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 400
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("forum")]
        tooltip "To the forum"

screen port_nav():
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 300
        focus_mask None
        action [Hide ("port_nav"), Jump ("street_s1")]
        tooltip "North"
    imagebutton auto "rarrow_%s":
        xpos 1850
        ypos 500
        focus_mask None
        action [Hide ("port_nav"), Jump ("schola")]
        tooltip "To the merchant schola"

label day_change:
    if weekday_number == 7:
        $ weekday_number = 1
        $ totalday += 1
    else:
        $ weekday_number += 1
        $ totalday += 1

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
default totalday = 0

######## NEW DAY SYS (guy was mean so i gave up) ##########

#default weekday = 0

#label day_change
    #$ weekday = (weekday+1) % 7
    #return

#define day_names = [ "SOL", "LUN", "MAR", "MER", "IOV", "VEN", "SAT" ]
    #$ today = day_names(weekday)

##### DAILY FLAGS #####

default dailyFlags = []

#later, use: dailyFlags[event_ID] = value


# The game starts here.

label start:
    with fade

    "It was a moonless night."

    scene bg found with fade

    "I was left outside a brothel."

    scene bg baby with fade

    "Lupa, the matron, brought me in. A swaddled babe, carrying only an amulet, inscribed with my name..."

    python:
        pname = renpy.input("Name?", length=32)
        pname = pname.strip()

        if not pname:
            pname = "Remus"

    scene black with fade

    "I did not receive the most {i}traditional{/i} education."

    scene bg younglife with fade

    "But I was treated with care, and learned much of business and accounting along the way."

    scene black with fade

    "After saving up some money, I was able to afford a small apartment. And thanks to Lupa's connections, I secured a job at the port. My first day of work is tomorrow."

label cubi_wake:
    scene bg cubi int with fade
    show screen cubi_nav
    show screen day_dis
    call day_change()

    show p basic with dissolve

    if totalday == 1:
        p "A dignified career and a new apartment..."
        p "No longer will I be the poor, orphaned whore-son."
        p "Today, I enter the noble city of Luna as a respectable citizen!"

        window hide
        pause
        show p shocked

        p "Damn, I was supposed to be at the port before sunrise!"

        window hide

        hide p shocked with dissolve
   
    else:
        p "{i}yawn{/i} Another day another denari..."

        hide p basic

    $ renpy.pause(hard=True)

label insula_ext:
    scene bg insula
    show screen ins_nav

    if totalday == 1:
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

    if totalday == 1:
        show p basic with dissolve

        p "The forum. The lively beating heart of any Roman city."
        p "No time to enjoy it this morning."

        hide p basic with dissolve

    $ renpy.pause(hard=True)

label street_s1:
    scene bg street s1
    show screen ss1_nav

    $ renpy.pause(hard=True)

label port:
    scene bg port
    show screen port_nav

    if totalday == 1:
        show p basic at left with dissolve:
            xzoom -1

        p "Hm... Lupa told me to talk to the man in charge..."

        window hide
        pause

        g "So! The wolf's cub decided to join us."

        show g basic at right with dissolve

        pause .5

        show p shocked at left:
            xzoom 1

        p "Ah! You must be-"

        g "Your employer. Gurges."

        g "And you are..."

        show p basic at left

        p "I'm [pname[0]][pname[1]]-"

        show g angry at right

        g "Late! On your first day."

        p "Sorry, sir, I-"

        show g basic at right

        g "I don't want to hear it. I've already taught a slave enough numbers to do your job for today."

        g "So now you'll be cleaning the merchant collegium's headquarters."

        g "Maybe there you'll learn to have respect for our great guild."

        p "Yes sir. Right away."

        show g basic at right:
            xzoom -1

        g "{i}grumbles{/i}"

        hide g basic with dissolve

        p "Well, at least I still have a job."

        pause

        p "I should head to the schola."

        hide p basic with dissolve

    $ renpy.pause(hard=True)

label schola:
    scene bg schola

    $ renpy.pause(hard=True)

    return
