### Names, maybe do OOP later (self, name, various sprites, respect, attraction)? ###

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define lun = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define g = Character("Gurges", color="4F4F4F")
define lup = Character("Lupa")
define a = Character("Attendant")
define f = Character("Felix")
define b = Character("Bishop")

### Screens / Image Buttons  (ill move into screens.rpy laterrrrrr) ###

init:
    transform flip:
        xzoom -1
    transform thirdzoom:
        zoom 0.33

screen gui:
    frame:
        xpos 80 # offset on the x axis
        ypos 950 # offset on the y axis
        xsize 200 # Width of your frame
        ysize 120 # Height of your frame
        #background "my_image.png" #Assuming it is located in the images folder.
        vbox:
            align(0.5, 0.5)
            text "{b}[weekday]{/b}"
            text "{b}DEN: [money]{/b}"
            #textbutton "Return" action Hide("my_black_box") # Hides the box you've created, but this part may vary on how you handle screens.

screen cubi_nav():
    imagebutton auto "door_%s": #ignore the magic door
        xpos 1520
        ypos 180
        focus_mask True
        action [Hide ("cubi_nav"), Jump ("insula_ext")]
    imagebutton auto "bed_%s":
        focus_mask True
        if totalday == 1 and time == 0:
            action [Jump ("cant_sleep")]
        action [Jump ("cubi_wake")]

screen ins_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ins_nav"), Jump ("street_n1")]
    imagebutton auto "insula_entry_%s":
        focus_mask True
        action [Hide ("ins_nav"), Jump ("cubi")]

screen sn1_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("sn1_nav"), Jump ("forum")]
        tooltip "To the forum"
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 400
        at flip
        focus_mask None
        action [Hide ("sn1_nav"), Jump ("insula_ext")]
        tooltip "Back home"
    imagebutton auto "thermasign_%s":
        xpos 498
        ypos 648
        focus_mask True
        action [Hide ("sn1_nav"), Jump ("therma_int")]

screen therma_int_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("therma_int_nav"), Jump ("street_n1")]

screen therma_ext_nav():
    imagebutton auto "therma_entrance_%s":
        focus_mask True
        action [Hide ("therma_ext_nav"), Jump ("therma_int")]

screen forum_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_s1")]
        tooltip "South"
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 400
        at flip
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_n1")]

screen ss1_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("port")]
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 400
        at flip
        focus_mask None
        action [Hide ("ss1_nav"), Jump ("forum")]

screen port_nav():
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 300
        at flip
        focus_mask None
        action [Hide ("port_nav"), Jump ("street_s1")]
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 500
        at flip
        focus_mask None
        action [Hide ("port_nav"), Jump ("schola")]

screen schola_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("schola_nav"), Jump ("port")]
    imagebutton auto "garden_ent_%s":
        focus_mask True
        action [Hide ("schola_nav"), Jump ("schola_garden")]

screen schola_garden_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("schola_garden_nav"), Jump ("schola")]
    if leaves == False and mud == False and statue < 2:
        imagebutton idle "pr statue basic":
            xpos .479
            ypos 570
            focus_mask True
            action [Hide ("schola_garden_nav"), Jump ("pedestal")]
            at thirdzoom
    elif statue == 2:
        imagebutton idle "pr statue fixed":
            xpos .479
            ypos 570
            focus_mask True
            action [Hide ("schola_garden_nav"), Jump ("pedestal")]
            at thirdzoom
    else:
        imagebutton idle "pr statue basic":
            xpos .479
            ypos 570
            focus_mask True
            at thirdzoom
    if leaves == True:
        imagebutton idle "leaves":
            xpos .65
            ypos .6
            # action Play("sound", "leaves.ogg")
            action [SetVariable("leaves", False), SetVariable("time", time + 1)]
    if mud == True:
        imagebutton idle "mud":
            ypos .3
            # action Play("sound", "mud.ogg")
            action [SetVariable("mud", False), SetVariable("time", time + 1)]
        

screen pedestal_nav(): #maybe add dialog when clicking statue
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("pedestal_nav"), Jump ("schola_garden")]
    if statue == 0:
        imagebutton idle "pr statue basic":
            xpos .52
            ypos 310
            focus_mask True
            action [Hide ("schola_garden_nav")]
    if statue == 1:
        imagebutton idle "pr statue broken":
            xpos .52
            ypos 310
            focus_mask True
            action [Hide ("schola_garden_nav")]
    if statue == 2:
        imagebutton idle "pr statue fixed":
            xpos .52
            ypos 310
            focus_mask True
            action [Hide ("schola_garden_nav")]

screen port_g():
    imagebutton idle "g basic.png":
        xpos 1200
        ypos 400
        focus_mask True
        action [Hide ("port_g"), Jump ("port_work")]
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 300
        at flip
        focus_mask None
        action [Hide ("port_nav"), Jump ("street_s1")]
    imagebutton auto "arrow_%s":
        xpos 1850
        ypos 500
        at flip
        focus_mask None
        action [Hide ("port_nav"), Jump ("schola")]

label day_change:
    $ time = 0
    $ therma = 0
    #$ totalday += 1 wasnt working here,
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

### Variables ###

default weekday_number = 1
default weekday = "SOL"
default totalday = 0
    #rent in cub costs ~350 every 30?
default time = 0
    # 0 - 12, Roman hour system. 1-6 for work, 7-8 for bathing/excersie/recreation, 9 - 12 for dinner/nightlife. 
default money = 15
default therma = 0
default leaves = True
default mud = True
default statue = 0

### More Efficient Day System? (guy was mean so i gave up) ###
    #default weekday = 0
    #label day_change
    #$ weekday = (weekday+1) % 7
    #return
    #define day_names = [ "SOL", "LUN", "MAR", "MER", "IOV", "VEN", "SAT" ]
    #$ today = day_names(weekday)

### Daily Flags? (Like a variable class that can wipe all at sleep?) ###
    #default dailyFlags = []
    #dailyFlags[worked] = 0
    #later, use: dailyFlags[event_ID] = value


# The game starts here.

label start:
    with fade
    "It was a moonless night."
    scene bg found with fade
    "I was left in a basket, outside a brothel."
    scene bg baby with fade
    "Lupa, the matron, brought me in. I had only an amulet, inscribed with my name..."
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
    "After saving up some money, I was able to afford a small apartment. And thanks to Lupa's connections I secured a job at the port. My first day of work is tomorrow."

label cubi_wake:
    scene bg cubi int with fade
    show screen gui
    show screen cubi_nav
    call day_change()
    show p basic 
    with dissolve
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
        p "{i}yawn{/i}"
        p "Another day another denarius..."
        hide p basic
    call screen cubi_nav

label cant_sleep:
    show screen cubi_nav
    show p shocked
    p "I can't go back to sleep! I need to pay rent!"
    jump cubi

label cubi:
    scene bg cubi int
    call screen cubi_nav

label insula_ext:
    scene bg insula
    if totalday == 1 and time == 0:
        show p basic with dissolve
        p "The port is directly South, past the Forum."
        show p basic:
            xzoom -1
        p "If I hit the sea I've gone too far."
        hide p basic with dissolve
    call screen ins_nav

label street_n1:
    scene bg street n1
    call screen sn1_nav

# label therma_ext:
#     scene bg therma ext
#     call screen therma_ext_nav

label therma_int:
    if time > 10:
        scene bg therma int night
        $ renpy.pause(hard=True)
    else:
        if therma < 1:
            scene bg therma int
            show a basic at right with dissolve
            show p basic at left with dissolve
            a "Welcome to the Baths of Luna."
            menu baths:
                "What is this place?":
                    a "Our baths are famous across the Empire for rejuvenating the body, mind, and soul."
                    a "Please feel free to enjoy our various pools, gym, and library."
                    jump baths
                "Pay to Enter":
                    a "That will be 2 denarii, please."                   
                    $ money -= 2
                    p "Here you go."
                    a "Thank you! Enjoy the baths."
                    hide a basic with dissolve
                    hide p basic with dissolve
                    $ therma += 1
                    jump therma_int
                "Leave":
                    show a annoyed at right
                    jump street_n1 #change to therma_ext when done
        else: #bath times coming soon
            $ renpy.pause(hard=True)
    call screen therma_int_nav

label forum:
    scene bg forum
    if totalday == 1 and time == 0:
        show p happy at right with dissolve
        p "Ah, the forum. Bustling as usual."
        "{i}Exile them!{/i}"
        show p basic at right:
            xzoom -1
        p "Maybe a bit more than usual..."
        hide p basic with dissolve
        scene bg forum crowd
        show b basic 
        with dissolve
        b "We must be lenient, brothers and sister."
        b "For our archaic, earthly laws do not allow us to dispense justice as our Lord, the Most High God wills."
        b "Yet."
        b "We must, regretfully, continue to toil in this age of sin."
        "{i}Boo!{/i}" 
        "{i}Out with the wicked!{/i}"
        b "But with only a small donation to the Church, we can strengthen our resolve and..."
        hide b basic
        show bg forum
        with dissolve
        show p basic
        p "Yikes."
        hide p basic with dissolve
    call screen forum_nav

label street_s1:
    scene bg street s1
    call screen ss1_nav

label port:
    scene bg port
    if totalday == 1 and time == 0:
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
        # if [pname[0]] == "B" and [pname[1]] == "i":
        #     g "Fired."
        #     g "You're fired."  
        #     p "I deserve it..."
        #     return
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
        p "I should head to the schola."
        hide p basic with dissolve
    if totalday == 1 and time == 3:
        show g basic at right
        show p basic at left with dissolve
        p "nfiefwnkefjnef.wjenfwkjefnwkjefnwejf"
    else:
        if time == 0:
                call screen port_g
    call screen port_nav
    
label port_work:
    scene bg port with fade
    show p basic at left with dissolve
    show g basic at right with dissolve
    g "Well, at least you made it on time."
    menu:
        "Work":
            g "Good. Let's get started. First..."
            scene work with fade 
            "Work was tiring. The shipments seemed to never stop coming."
            $ time == 6
            scene bg port
            show g basic at right 
            show p basic at left
            g "Alright, decent work today. Enjoy your evening."
            $ money += 25
            show p happy with dissolve
            jump port
    $ renpy.pause(hard=True)

label schola:
    scene bg schola
    if totalday == 1 and time == 0:
        show f basic at right:
            xzoom -1
        show p basic at left with dissolve
        p "Hm, this place doesn't seem so dirty."
        show f basic at right:
            xzoom 1
        f "That's because we've already cleaned most of it, sleepy head."
        p "Ah..."
        f "Don't worry, we left you the old garden to take care of."
        p "Very thoughtful of you."
        f "Better hurry up, the boss usually does inspections before lunch."
        p "Copy that."
        hide f basic with dissolve
        hide p basic with dissolve
    call screen schola_nav

label schola_garden:
    scene bg schola garden
    show screen schola_garden_nav
    if totalday == 1 and time == 0:
        show p basic at right with dissolve:
            xzoom -1
        p "Such a quiet and peaceful spot. Despite being so close to the port."
        p "I wonder why it hasn't been maintained."
        show p basic at right:
            xzoom 1
        p "Well, I should probably clean like my job depends on it."
        hide p basic with dissolve
        #if inventory implemented: click tool then:
        #minigame ideas: click + hold and drag to clean mud, click + drag leaves to basket
    call screen schola_garden_nav

label pedestal:
    scene bg pedestal
    show screen pedestal_nav
    if totalday == 1:
        show p basic at left with dissolve
        if statue == 2:
            p "Better wait until later to get my bulla back."
            call screen pedestal_nav
        if time >= 2:
            p "Lastly, the ever-ready protector of the gardens, noble Priapus."
            show p basic at center
            #zorder here or pedestal_nav ?
            p "Let's just clean you up..."
            "{i} crack {/i}"
            $ statue += 1
            show p shocked at left
            pause
            g "...you know we have a collegium meeting tomorrow night. Everything needs to be perfect."
            show p shocked at left with dissolve:
                #possible to update without dissolve?
                xzoom -1
            show p shocked at left with dissolve:
                xzoom 1
            p "I'll definitely lose my job now. It's over. I'll have to move back to-"
            show p basic
            p "Unless..."
            p "Oh gods, please work."
            #if inventory implemented: drag amulet from inv to statue
            show p basic at center
            "{i} click {/i}"
            $ statue += 1
            show p basic at right:
                xzoom -1
            pause
            g "Whats this?"
            show p happy at right
            show g basic at left with dissolve:
                xzoom -1
            p "Just finishing up, sir!"
            g "..."
            pause
            g "I think you've cleaned {i}that{/i} part enough, [pname]."
            show g basic:
                xzoom 1
            g "But the grounds look clean enough."
            g "Meet me back at the port for your pay."
            p "Will do, thank you, sir."
            $ time += 1
            hide g basic with dissolve
            pause

    call screen pedestal_nav

    return
