label home_drunk_sleep:
    $ temp_var_1 = False
    $ temp_var_2 = False
    $ temp_var_3 = False
    $ temp_var_4 = False
    $ temp_var_5 = False


    $ rand_choice = WeightedChoice([
    ("home_drunk_sleep_vcommon", 5),
    ("home_drunk_sleep_common", 5),
    ("home_drunk_sleep_rare", 5),
    ("home_drunk_sleep_vrare", 5),
    ("home_drunk_sleep_xrare", 5)
    ])
    jump expression rand_choice

label home_drunk_sleep_vcommon:
    jump expression renpy.random.choice([
    "home_drunk_sleep_event_vcommon_1"
    ])
label home_drunk_sleep_common:
    jump expression renpy.random.choice([
    "home_drunk_sleep_event_common_1"
    ])
label home_drunk_sleep_rare:
    jump expression renpy.random.choice([
    "home_drunk_sleep_event_rare_1",
    "home_drunk_sleep_event_rare_2",
    "home_drunk_sleep_event_rare_3"
    ])
label home_drunk_sleep_vrare:
    jump expression renpy.random.choice([
    "home_drunk_sleep_event_vrare_1",
    "home_drunk_sleep_event_vrare_2",
    "home_drunk_sleep_event_vrare_3"
    ])
label home_drunk_sleep_xrare:
    jump expression renpy.random.choice([
    "home_drunk_sleep_event_xrare_1",
    "home_drunk_sleep_event_xrare_2",
    "home_drunk_sleep_event_xrare_3"

    ])





label home_drunk_sleep_event_vcommon_1:
    scene bg_bedroom
    "You stagger in through the door and just about manage to change into your pijamas before passing out face first on the bed."
    "Sleep and switch to morning"
    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 4)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
    else:
        pc "Please... Never again..."
    jump bedroom_screen





label home_drunk_sleep_event_common_1:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve
    $ top = 0
    $ bottom = 0
    $ outfit = 0
    "You stagger in through the door and just about manage to change into your pijamas but dont quite make it to your bedroom. Instead you pass out in your underwear on the sofa."
    scene bg_common with dissolve
    show screen pc_avatar with dissolve

    $ face = 2
    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
    else:
        pc "Please... Never again..."
    jump common_screen





label home_drunk_sleep_event_rare_1:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked on the sofa."
    scene bg_common with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
    else:
        pc "Please... Never again..."
    jump common_screen

label home_drunk_sleep_event_rare_2:

    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked on the bed."
    scene bg_bedroom with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
    else:
        pc "Please... Never again..."
    jump bedroom_screen

label home_drunk_sleep_event_rare_3:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked while hugging the toilet bowl."
    scene bg_bathroom with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
    else:
        pc "Please... Never again..."
    jump bathroom_screen





label home_drunk_sleep_event_vrare_1:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass naked on the sofa."
    scene bg_common with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
        pc "And is that... Cum on my tits? What the hell did I do last night?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
        pc "And is that... Cum on my face? What the hell did I do last night?"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
        pc "And is that... Cum on my stomach? What the hell did I do last night?"
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
        pc "And is that... Cum on my lips? What the hell did I do last night?"
    else:
        pc "Please... Never again..."
        pc "And is that... Cum on my legs? What the hell did I do last night?"
    jump common_screen
label home_drunk_sleep_event_vrare_2:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked on the bed."
    scene bg_bedroom with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
        pc "And is that... Cum on my tits? What the hell did I do last night?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
        pc "And is that... Cum on my face? What the hell did I do last night?"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
        pc "And is that... Cum on my stomach? What the hell did I do last night?"
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
        pc "And is that... Cum on my lips? What the hell did I do last night?"
    else:
        pc "Please... Never again..."
        pc "And is that... Cum on my legs? What the hell did I do last night?"
    jump bedroom_screen
label home_drunk_sleep_event_vrare_3:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked while hugging the toilet bowl."
    scene bg_bathroom with dissolve
    show screen pc_avatar with dissolve

    "Uuuugggg"
    $ randomnum = renpy.random.randint(1, 5)
    if randomnum==1:
        pc "Ugh, my head is killing me... Why did I drink so much...?"
        pc "And is that... Cum on my tits? What the hell did I do last night?"
    elif randomnum==2:
        pc "Uuuuuu. Please room stop spinning"
        pc "And is that... Cum on my face? What the hell did I do last night?"
    elif randomnum==3:
        pc "Noooo stop thumping head..."
        pc "And is that... Cum on my stomach? What the hell did I do last night?"
    elif randomnum==4:
        pc "Ugh, did I really have that much to drink?"
        pc "And is that... Cum on my lips? What the hell did I do last night?"
    else:
        pc "Please... Never again..."
        pc "And is that... Cum on my legs? What the hell did I do last night?"
    jump bathroom_screen





label home_drunk_sleep_event_xrare_1:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass naked on the sofa."
    $ temp_var_2 = True
    scene bg_common with dissolve
    show screen pc_avatar with dissolve
    jump home_drunk_sleep_event_xrare_random


label home_drunk_sleep_event_xrare_2:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked on the bed."
    $ temp_var_1 = True
    scene bg_bedroom with dissolve
    show screen pc_avatar with dissolve
    jump home_drunk_sleep_event_xrare_random

label home_drunk_sleep_event_xrare_3:
    scene bg_black with dissolve
    hide screen pc_avatar with dissolve

    $ top = 0
    $ bottom = 0
    $ outfit = 0
    $ pants = 0
    $ bra = 0
    "You stagger in through the door and dont quite make it into your pijamas. You pass out naked while hugging the toilet bowl."
    scene bg_bathroom with dissolve
    show screen pc_avatar with dissolve
    jump home_drunk_sleep_event_xrare_random

label home_drunk_sleep_event_xrare_random:

    $ randomnum = renpy.random.randint(1, 4)


    if randomnum==1:
        pc "Ugh, did I really have that much to drink?"
        pc "Ahhh no! My ass is so fucking sore. And is that cum all over my ass?"
        pc "Did I let someone fuck me in the ass last night while I was drunk?"
        if avirgin == True:
            $ avirgin = False
            pc "Damn... First time fucked in the ass and I was too drunk to even remember it. Maybe thats a good thing."

    elif randomnum==2:
        pc "Please... Never again..."
        pc "Ahhh no! My ass is so fucking sore. And is that cum leaking out if it?"
        pc "Did I let someone fuck me in the ass last night while I was drunk?"
        if avirgin == True:
            $ avirgin = False
            pc "Damn... First time fucked in the ass and I was too drunk to even remember it. Maybe thats a good thing."

    elif randomnum==3:
        pc "Ugh, did I really have that much to drink?"
        pc "Ahhh no! My pussy is so fucking sore. And is that cum leaking out if it?"
        if vvirgin == True:
            $ vvirgin = False
            pc "Damn... Virginity taken and I'll never know by who. What a let down."
            if preg_pills == True:
                pc "Good job I am on the pill since whoever fucked me clearly didnt use a condom."
            else:
                pc "Takes my virginity and tries to leave a baby in my belly... Not really a good deal there."
        else:
            if preg_pills == True:
                pc "Good job I am on the pill since whoever fucked me clearly didnt use a condom."
            else:
                pc "Fuck, this could have got me pregnant. Whoever fucked me clearly didnt use a condom."
    else:

        pc "Please... Never again..."
        pc "Ahhh no! My pussy is so fucking sore. And is that cum all over my stomach?"
        pc "Did I let someone fuck me last night while I was drunk?"
        if vvirgin == True:
            $ vvirgin = False
            pc "Damn... Virginity taken and I'll never know by who. What a let down."
            if preg_pills == True:
                pc "Damn, looks like whoever fucked me pulled out at least."
            else:
                pc "Looks like he pulled out so at least he didn't try and put a baby in me. But there is always the risk..."
        else:
            if preg_pills == True:
                pc "Damn, looks like whoever fucked me pulled out at least."
            else:
                pc "Fuck, this could have got me pregnant. Although it seems like he pulled out I might still end up with his baby."

    if temp_var_1 == True:
        jump bedroom_screen

    elif temp_var_2 == True:
        jump common_screen
    else:

        jump bathroom_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
