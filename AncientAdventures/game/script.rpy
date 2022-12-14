### Names, maybe do OOP later (self, name, various sprites, respect, attraction)? ###

define p = Character("[pname]", color="9C0000")
define pr = Character("Priapus", color="354A36")
define lun = Character("Luna", color="EBF5F5")
define v = Character("Venus", color="FF0082")
define c = Character("Cupid", color="FF93CA")
define g = Character("Gurges", color="4F4F4F")
define lup = Character("Lupa")
define a = Character("Therma Attendant")
define f = Character("Felix")
define b = Character("Bishop")
define s = Character("Serving Woman")

### Screens / Image Buttons  (ill move into screens.rpy laterrrrrr) ###

init:
    transform flip: #to make arrows point right
        xzoom -1
    transform thirdzoom:
        zoom 0.33

screen gui:
    zorder 10
    frame:
        xpos 80 # offset on the x axis
        ypos 950 # offset on the y axis
        xsize 200 # Width of your frame
        ysize 120 # Height of your frame
        #background "my_image.png"
        vbox:
            align(0.5, 0.5)
            text "{b}[weekday]{/b}"
            text "{b}DEN: [money]{/b}"
            #textbutton "Return" action Hide("") # Hides the box you've created, but this part may vary on how you handle screens.

# screen questtracker:
    
# screen inventory:

screen cubi_nav():
    # modal True (problems with showing screens)
    imagebutton auto "door_%s":
        xpos 1520
        ypos 180
        focus_mask True
        action [Hide ("cubi_nav"), Jump ("insula_ext")]
    imagebutton auto "bed_%s":
        focus_mask True
        if totalday == 1 and time <= 3:
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
    imagebutton auto "thermasign_%s":
        xpos 498
        ypos 648
        focus_mask True
        if totalday == 1 and time <= 3:
            action [Hide ("sn1_nav"), Jump ("cant_bathe")]
        else:
            action [Hide ("sn1_nav"), Jump ("therma_apo")]

screen therma_apo_nav():
    # imagebutton auto "therma_apo_ent_%s":
    #     focus_mask True
    #     if clothes == False:
    #         action Jump ("cant_leave")
    #     else:
    #         action [Hide ("therma_apo_nav"), Jump ("street_n1")]
    # imagebutton auto "therma_apo_tep_%s":
    #     focus_mask True
    #     action [Hide ("therma_apo_nav"), Jump ("therma_tep")]
    # imagebutton auto "therma_apo_pae_%s":
    #     focus_mask True
    #     action [Hide ("therma_apo_nav"), Jump ("therma_pae")]
    # if clothes == True:
    #     imagebutton auto "clothes_spot_%s":
    #         focus_mask True
    #         # action Play("sound", "clothes.ogg")
    #         action SetVariable("clothes", False)
    imagemap auto "bg_therma_apo_%s":
        alpha True
        hotspot (20, 440, 317, 622):
            if clothes == True:
                action [Hide ("therma_apo_nav"), Jump ("street_n1")]
            else:
                action [Hide ("therma_apo_nav"), Jump ("cant_leave")]
        hotspot (825, 441, 255, 384) action [Hide ("therma_apo_nav"), Jump ("therma_tep")]
        hotspot (1651, 534, 261, 146) action [Hide ("therma_apo_nav"), Jump ("therma_pae")]
        hotspot (365, 468, 338, 446) action [Hide ("therma_apo_nav"), Jump ("therma_attendant")]
        if clothes == True:
            hotspot (1218, 756, 420, 306) action SetVariable("clothes", False)
    if clothes == False:
        imagebutton auto "clothes_%s":
            xpos 1350
            ypos 885
            action SetVariable("clothes", True)
            # action Play("sound", "clothes.ogg")

        
screen therma_tep_nav():
    # imagebutton auto "therma_tep_apo_%s":
    #     focus_mask True
    #     action [Hide ("therma_tep_nav"), Jump ("therma_apo")]
    # imagebutton auto "therma_tep_cal_%s":
    #     focus_mask True
    #     action [Hide ("therma_tep_nav"), Jump ("therma_cal")]
    # imagebutton auto "therma_tep_fri_%s":
    #     focus_mask True
    #     action [Hide ("therma_tep_nav"), Jump ("therma_fri")]
    # imagebutton auto "strigil_%s":
    #     focus_mask None
    #     action []
    imagemap auto "bg_therma_tep_%s":
        alpha True
        hotspot (1056, 178, 259, 444) action [Hide ("therma_tep_nav"), Jump ("therma_apo")]
        hotspot (60, 455, 158, 536) action [Hide ("therma_tep_nav"), Jump ("therma_fri")]
        hotspot (1701, 434, 188, 587) action [Hide ("therma_tep_nav"), Jump ("therma_cal")]
        hotspot (363, 881, 182, 191) action [Hide ("therma_tep_nav"), Jump ("therma_tep")]
            # strigil


screen therma_cal_nav():
    imagebutton auto "therma_cal_tep_%s":
        focus_mask True
        action [Hide ("therma_cal_nav"), Jump ("therma_tep")]

screen therma_fri_nav():
    imagebutton auto "therma_fri_tep_%s":
        focus_mask True
        action [Hide ("therma_fri_nav"), Jump ("therma_tep")]

screen therma_pae_nav():
    imagebutton auto "therma_pae_apo_%s":
        focus_mask True
        action [Hide ("therma_pae_nav"), Jump ("therma_apo")]
    imagebutton auto "therma_pae_lib_%s":
        focus_mask True
        action [Hide ("therma_pae_nav"), Jump ("therma_lib")]
    imagebutton auto "natatio_%s":
        focus_mask True
        action [Hide ("therma_pae_nav"), Jump ("pae_swim")]
    # imagebutton auto "weights_%s":
    #     focus_mask True
    #     action []
    imagemap auto "bg_therma_pae_%s":
        alpha True
        hotspot (1236, 76, 172, 439) action [Hide ("therma_tep_nav"), Jump ("therma_apo")]
        hotspot (684, 190, 325, 334) action [Hide ("therma_tep_nav"), Jump ("pae_snack")]
        hotspot (234, 235, 172, 399) action [Hide ("therma_tep_nav"), Jump ("therma_lib")]
        hotspot (400, 882, 476, 178) action [Hide ("therma_tep_nav"), Jump ("pae_weights")]
        hotspot (1552, 708, 366, 372) action [Hide ("therma_tep_nav"), Jump ("pae_nat")]

screen pae_nat_nav():
        imagebutton auto "arrow_%s":
            xpos 20
            ypos 400
            focus_mask None
            action [Hide ("pae_swim_nav"), Jump ("therma_pae")]

screen pae_weights_nav():
        imagebutton auto "arrow_%s":
            xpos 20
            ypos 400
            focus_mask None
            action [Hide ("pae_weights_nav"), Jump ("therma_pae")]

screen pae_snack_nav():
        imagebutton auto "arrow_%s":
            xpos 20
            ypos 400
            focus_mask None
            action [Hide ("pae_snack_nav"), Jump ("therma_pae")]

screen therma_lib_nav():
    imagebutton auto "therma_lib_pae_%s":
        focus_mask True
        action [Hide ("therma_lib_nav"), Jump ("therma_pae")]  

screen forum_nav():
    imagebutton auto "arrow_%s":
        xpos 20
        ypos 400
        focus_mask None
        action [Hide ("forum_nav"), Jump ("street_s1")]
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
    imagebutton idle "g basic":
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

### More Efficient Day System? (guy was mean so i gave up) ###
    #default weekday = 0
    #label day_change
    #$ weekday = (weekday+1) % 7
    #return
    #define day_names = [ "SOL", "LUN", "MAR", "MER", "IOV", "VEN", "SAT" ]
    #$ today = day_names(weekday)


### Environmental Variables ###

default weekday_number = 1
default weekday = "SOL"
default totalday = 0
    #rent in cub costs ~350 every 30?
default time = 0
    # 0 - 24, 12 day hours (starting at 6am) and 12 night. 1-6/7 for work, 6-8 light lunch,siesta, 7-13 for bathing/excersie/recreation/afternoon business, 13 - 17 for dinner/nightlife. 
default leaves = True
default mud = True
default statue = 0

### Personal Variables ###

default money = 15
default therma_pass = False
default clothes = True
default skill_swim = 0
default skill_str = 0
default skill_lib = 0

# The game starts here.

label start:
    with fade
    "It was a moonless night."
    scene bg_found with fade
    "I was left in a basket, outside a brothel."
    scene bg_baby with fade
    "Lupa, the matron, brought me in. I had only an amulet, inscribed with my name..."
    python:
        pname = renpy.input("Name?", length=32)
        pname = pname.strip()
        if not pname:
            pname = "Remus"
    scene black with fade
    "I did not receive the most {i}traditional{/i} education."
    scene bg_younglife with fade
    "But I was treated with care, and learned much of business and accounting along the way."
    scene black with fade
    "After saving up some money, I was able to afford a small apartment. And thanks to Lupa's connections I secured a job at the port. My first day of work is tomorrow."

label cubi_wake:
    scene bg_cubi_int with fade
    show screen gui
    show screen cubi_nav
    call day_change()
    show p basic 
    with dissolve
    if totalday == 1:
        $ time = 2
        p "A dignified career and a new apartment..."
        p "No longer will I be the poor, orphaned whore-son."
        p "Today, I enter the noble city of Luna as a respectable citizen!"
        window hide
        pause
        show p shocked
        p "Damn, I was supposed to be at the port at sunrise!"
        window hide
        hide p shocked with dissolve
    else:
        p "{i}yawn{/i}"
        p "Another day another denarius..."
        hide p basic
    call screen cubi_nav

###call in these three preventative labels doesnt return correctly, sticking with Jump and Jump back

label cant_leave:
    show screen therma_apo_nav
    p "I should probably put my clothes back on..."
    jump therma_apo

label cant_sleep:
    show screen cubi_nav
    show p shocked
    p "I can't go back to sleep! I need to pay rent!"
    jump cubi

label cant_bathe:
    scene bg_street_n1
    p "As nice as a hot bath sounds... No time!"
    call screen sn1_nav

label cubi:
    scene bg_cubi_int
    call screen cubi_nav

label insula_ext:
    scene bg_insula
    if totalday == 1 and time <= 3:
        show p basic with dissolve
        p "The port is directly South, past the forum."
        show p basic:
            xzoom -1
        p "If I hit the sea I've gone too far."
        hide p basic with dissolve
    call screen ins_nav

label street_n1:
    scene bg_street_n1
    call screen sn1_nav

# label therma_ext:
#     scene bg_therma_ext
#     call screen therma_ext_nav

label therma_apo:
    if time > 15:
        scene bg_therma_int_night
        call screen therma_apo_nav
    else:
        if therma_pass == False:
            jump therma_attendant
        else:
            scene bg_therma_apo
            call screen therma_apo_nav
    call screen therma_apo_nav
    $ renpy.pause(hard=True) ###activating exit twice is jumping to next inline label, maybe this helps :)

label therma_attendant:
    scene bg_therma_apo_att
    show p basic at right with dissolve:
        xzoom -1
    a "Welcome to the Baths of Luna."
    menu apo_menu:
        "What is this place?":
            a "Our baths are famous across the Empire for rejuvenating the body, mind, and soul."
            a "Please feel free to enjoy our various pools, gym, and library."
            a "Also, keep in mind our baths are mixed."
            show p happy
            pause
            show p basic
            jump apo_menu
        "What should I do?":
            a "First, you should deposit your belongings in one of the available spaces here."
            a "Men usually prefer to then oil themselves and work out in the Paelestra, afterwards relaxing in the Tepidarium while they clean themselves with the supplied strigils."
            a "From that point you can freely cycle the bath rooms, or enjoy a more cereberal activity in the library."
            jump apo_menu
        "Pay to Enter" if therma_pass == False:
            a "That will be 2 denarii, please."                   
            $ money -= 2
            p "Here you go."
            a "Thank you! Enjoy the baths."
            hide a basic with dissolve
            hide p basic with dissolve
            $ therma_pass = True
            jump therma_apo
        "Leave":
            if therma_pass == False:
                show a_annoyed at right
                jump street_n1 #change to therma_ext when done
            else:
                jump therma_apo

label therma_pae:
    scene bg_therma_pae
    call screen therma_pae_nav

label pae_nat:
    scene bg_therma_pae_blur
    call screen pae_nat_nav
    show p basic at left with dissolve
    menu nat:
        "Go for a swim":
            p "A cool swim sounds perfect right now."
            hide p basic with dissolve
            scene bg_pae_swim 
            "Nothing like a few laps under the Sun."
            $ time += 1
            # $ skill_swim += 1

label pae_weights:
    scene bg_therma_pae_blur
    call screen pae_weights_nav

label pae_snack:
    scene bg_therma_pae_blur
    call screen pae_snack_nav

label therma_lib:
    scene bg_therma_lib
    call screen therma_lib_nav

label lib_read:
    scene bg_therma_lib_read
    call screen lib_read_nav


label therma_tep:
    scene bg_therma_tep
    call screen therma_tep_nav

label therma_cal:
    scene bg_therma_cal
    call screen therma_cal_nav

label therma_fri:
    scene bg_therma_fri
    call screen therma_fri_nav

label forum:
    scene bg_forum
    if totalday == 1 and time == 2:
        show p basic with dissolve
        p "The forum. The heart of the city."
        p "Seems like half of the people are as late as I am."
        hide p basic
        call screen forum_nav
    if totalday == 2 and time >= 3:
        show p happy at right with dissolve
        p "The forum. Bustling as usual."
        "{i}Exile them!{/i}"
        show p basic at right:
            xzoom -1
        p "Maybe a bit more than usual..."
        hide p basic with dissolve
        scene bg_forum crowd
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
        show bg_forum
        with dissolve
        show p basic
        p "Yikes."
        hide p basic with dissolve
    call screen forum_nav

label street_s1:
    scene bg_street_s1
    call screen ss1_nav

label port:
    scene bg_port
    if totalday == 1 and time == 2:
        show p basic at left with dissolve:
            xzoom -1
        p "Hm... Lupa told me to talk to the man in charge..."
        window hide
        pause
        g "So! The wolf's pup decided to join us."
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
        hide p basic with dissolve
    else:
        if time < 6:
                call screen port_g
    call screen port_nav
    
label port_work:
    scene bg_port
    show p basic at left
    show g basic at right
    with dissolve
    if totalday == 1 and time == 0:
        g "Need me to hold your hand, pup? Get to the schola!"
        call screen port_nav
    if totalday == 1 and statue == 2:
        g "All done?"
        p "Yep! Clean as a whistle!"
        g "Good. Here's half a days pay, and you're lucky to get that."
        $ money += 15
        g "Our collegium works as a unit. From the slaves hauling amphorae to yours truly."
        g "Every member is vital. Any weak links and the chain breaks."
        g "Know what happens when the chain breaks?"
        p "Bad things. Probably."
        g "You're young. You don't remember a time when bread wasn't on the table."
        g "But that time is closer than you think."
        g "See you tomorrow, pup."
        hide g basic with dissolve
        $ time = 6
        p "Hm."
        show p basic at center with dissolve
        p "Well, an eventful first day."
        show p basic:
            xzoom -1 
        p "I should head to the baths, the perfect place to wash off the sweat and stress."
        hide p basic with dissolve
        jump port
    else:
        g "Well, at least you made it on time."
        menu:
            "Work":
                g "Good. Let's get started. First..."
                scene work with fade 
                $ quote = renpy.random.choice([1,2,3])
                if quote == 1:
                    p "Work was tiring. The shipments seemed to never stop coming."
                if quote == 2:
                    p "So much cargo... I feel like my fingers are going to fall off."
                if quote == 3:
                    p "Another long day. I need a snack. And a bath."
                $ time == 6
                scene bg_port
                show g basic at right 
                show p basic at left
                g "Alright, decent work today. Enjoy your evening."
                $ money += 30
                show p happy with dissolve
                jump port

label schola:
    if totalday == 2 and time == 8:
        scene bg_schola_dinner
        show g_fancy at right
        with dissolve

    scene bg_schola
    if totalday == 1 and time == 2:
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
        f "Better hurry up, the boss wants these areas spotless before the day ends."
        p "Copy that."
        hide f basic with dissolve
        hide p basic with dissolve
    call screen schola_nav

label schola_garden:
    scene bg_schola_garden
    show screen schola_garden_nav
    if totalday == 1 and time == 2:
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
    scene bg_pedestal
    show screen pedestal_nav
    if totalday == 1:
        show p basic at left with dissolve
        if statue == 2:
            p "Can't get my bulla back now."
            p "Better wait until later tonight, when no ones around."
            call screen pedestal_nav
        if statue == 0:
            p "Lastly, the ever-ready protector of the gardens, noble Priapus."
            show p basic at center
            #zorder here or pedestal_nav ?
            p "Let's just clean you up..."
            $ statue += 1
            "{i} crack {/i}" with hpunch
            show p shocked at left
            pause
            g "...you know we have a collegium meeting tomorrow night. Everything needs to be perfect."
            show p shocked at left with dissolve:
                #possible to update without dissolve?
                xzoom -1
            show p shocked at left with dissolve:
                xzoom 1
            p "I'll definitely lose my job now. It's over. I'll have to change my name, I can stow away on-"
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
            g "Meet me back at the port for your pay when you're finished."
            p "Will do, thank you, sir."
            $ time += 1
            hide g basic with dissolve
            pause
            show p basic 
            p "That was close."
            show p basic at center:
                xzoom -1
            p "I can't take my bulla back now... Too many people around."
            hide p basic with dissolve
    call screen pedestal_nav

    return
