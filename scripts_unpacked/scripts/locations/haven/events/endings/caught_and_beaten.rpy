label haven_caught_and_beaten:
    $ add_to_list(main_quest_05.list, "beaten")
    pc "Wait wai..."
    $ player.punch()
    pause 0.3
    $ player.punch()
    show screen blackout(100) with Dissolve(0.2)
    $ renpy.scene()
    $ walk(loc_haven_office, time_amount=45)
    pause 1
    $ player.eye = 4
    show haven_alex at right1
    show haven_guard3 at right3
    show screen blackout(50) with dissolve
    pc "Ugghhhhh..."
    $ player.eye = 2
    alex.nname "...trouble in here. Who do you think?"
    havguard "You think it's them?"
    alex.nname "No one else would try something so stupid. So who else?"
    havguard "So what should we do?"
    pc "Uhhhhhh..."
    hide screen blackout with dissolve
    havguard "Looks like she is coming round."
    $ player.eye = 1
    $ player.face_worried()
    alex.nname "Good."
    pc "Huh, wait what?"
    pc "What's going on?"

    if "flooded" in main_quest_05.list:
        alex.nname "You tell me. Why the fuck would you do something as stupid as to try to wreck my place?"
        pc "Wait no! I wasn't trying to wreck the place."
        alex.nname "No? You just fell on the pipes with a crowbar and they broke did they?"
    elif "set_fire" in main_quest_05.list:
        alex.nname "You tell me. Why the fuck would you do something as stupid as to try to wreck my place?"
        pc "Wait no! I wasn't trying to wreck the place."
        alex.nname "No? You just happened to set a fire downstairs because you were bored or what?"
    else:
        alex.nname "You tell me. What the fuck are you doing sneaking around this place? Come to kill me?"
        pc "Wait no! I it's nothing like that!"
        alex.nname "No? You got lost and wound up walking past a locked gate?"

    pc "No, look sorry. But it was the only way I would be able to see you."
    alex.nname "The fuck do you want with me?"
    pc "You know about [ant.fname] [ant.sname]. I came here..."
    with vpunch
    alex.nname "HIM!?"
    if "flooded" in main_quest_05.list or "set_fire" in main_quest_05.list:
        alex.nname "You wreck my place because of that shit?"
    else:
        alex.nname "You're sneaking about my place because of that shit?"


    pc "I need to..."
    alex.nname "That FUCKER! Still causing me trouble. What do you want with him?"
    pc "Err... To find out where he is..."
    alex.nname "Any why did you come here to find that out?"
    pc "Because of your connection with him?"
    alex.nname "There is no connection between us! I am here trying to clean up the dregs while shits like him want to abuse them."
    pc "But he was here..."
    alex.nname "And then I kicked him out! I have no use for someone looking to push an addiction on the dregs instead of helping them up."
    alex.nname "So don't you fucking dare try to lump me together with scum like him!"
    show haven_guard3 with dissolve:
        xzoom -1
    havguard "*Whisper* ...not part of... ...somewhere to deal with..."
    alex.nname "Mmmm."
    pc "So where is he?"
    alex.nname "You would need to ask the twins that. Doubt you will get the chance though."
    alex.nname "Take her to the pen."
    show haven_guard3 with dissolve:
        xzoom 1
    pc "Wait, twins?"
    alex.nname "Your [ant.name] is playing with them to create something new."
    pc "Huh?"
    show haven_guard3 at right6 with dissolve
    pcm "Fuck! Too late, got to get out of here now!"
    hide haven_alex
    hide haven_guard3
    with hpunch
    pcm "Fuck fuck fuck! Window?!"
    jump haven_caught_and_beaten_windowbreak
    call screen haven_office_screen



label haven_caught_and_beaten_bag:
    "I rush over and grab the bag."
    pcm "The hell am I supposed to do with this?"
    jump haven_sold_ending

label haven_caught_and_beaten_books:
    "I rush over and grab one of the books and try to hit the guard with it."
    with hpunch
    pc "Ahhgg!"
    jump haven_sold_ending

label haven_caught_and_beaten_desk:
    "I rush to the desk and jump up on it trying to kick anyone coming close. But it's not long until my foot is grabbed and I am dragged off of it."
    with vpunch
    pc "Ah shit!"
    jump haven_sold_ending

label haven_caught_and_beaten_folder:
    "I rush over and grab one of the folders and try to hit the guard with it."
    with hpunch
    pc "Ahhgg!"
    jump haven_sold_ending

label haven_caught_and_beaten_grain:
    "I rush over to the bags and try to lift it to use as a weapon but they are far too heavy to lift."
    pc "UNG!"
    jump haven_sold_ending

label haven_caught_and_beaten_lamp:
    "I rush over and grab the lamp and attempt to use it as a bludgeon. But after a few swings I am tackled by one of the guards."
    with hpunch
    pc "Ung!"
    jump haven_sold_ending

label haven_caught_and_beaten_map:
    "I rush over to the desk and grab some of the junk that is on the table to throw at the guards to give myself space. But it isn't long until I am grabbed."
    with hpunch
    pc "Ung!"
    jump haven_sold_ending

label haven_caught_and_beaten_sofa:
    "I rush to the sofa and start grabbing the pillows to throw at the guards. This of course does nothing to slow them so I am quickly tackled."
    with hpunch
    pc "Ung!"
    jump haven_sold_ending

label haven_caught_and_beaten_windowboard:
    "I try to rush to the boarded up window but the desk is in the way and I am grabbed before I can even reach it."
    with hpunch
    pc "Ung!"
    jump haven_sold_ending

label haven_caught_and_beaten_windowbreak:
    $ renpy.stop_predict("images/locations/haven/screen_office/*.webp")
    if "survive_fall" in main_quest_05.list:
        "I rush to the window and, without hesitation, I jump right through."
        jump haven_window_escape
    else:
        "I rush to the window preparing to jump, but as I reach the window I hesitate realising I have no idea if I can even survive a fall like that."
        pcm "Fuck fuck!"
        show haven_guard3 at right6 with hpunch
        "One of the guards comes up and starts to try and grab me."
        pcm "No choice. Got to get out of here!"
        if player.check_fight(3):
            show haven_guard3 at right4 with hpunch
            "I manage to slip out of the guard's grasp and turn to the window."
            jump haven_window_escape
        else:
            "I try to free myself from the guards grasp but he is too strong and I cannot get free."
            jump haven_sold_ending



screen haven_office_screen():
    zorder 1

    for i in ("bag", "books", "folder", "grain", "desk", "map", "sofa", "windowboard", "windowbreak", "lamp"):
        imagebutton auto ("bg_haven_office_" + i + "_layer_%s") focus_mask True action Jump ("haven_caught_and_beaten_" + i)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
