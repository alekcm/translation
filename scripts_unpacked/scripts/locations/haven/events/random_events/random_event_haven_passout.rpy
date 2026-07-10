label haven_drunk_trigger:
    show screen blackout(100)
    $ rand_choice = WeightedChoice([
    ("haven_drunk_event_1", 10),
    ("haven_drunk_event_2", 10),
    ("haven_drunk_event_3", 10),
    ("haven_drunk_event_4", 10),
    ("haven_drunk_event_5", 8),
    ("haven_drunk_event_6", 5),
    ("haven_drunk_event_7", 3),
    ("haven_drunk_event_8", 3),
    ])
    jump expression rand_choice

label haven_drunk_event_1:
    $ walk(loc_haven_bed)
    $ time_sleep(120)
    $ time_sleep(120)
    show haven_sleep at right2
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    show haven_sleep conf
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    pcm "Ugh, where am I?"
    pcm "..."
    pcm "Oh, right..."
    hide haven_sleep with dissolve
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8
    pc "..."
    pcm "What happened? I don't remember much..."
    pcm "Splitting headache though. Must have drunk way too much."
    pcm "Oh well, still have all my fingers and toes so isn't too bad."
    $ player.face_normal()
    jump travel

label haven_drunk_event_2:
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ walk(loc_haven_room1)
    elif randomnum == 2:
        $ walk(loc_haven_room2)
    else:
        $ walk(loc_haven_room3)
    $ time_sleep(120)
    $ time_sleep(120)
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    pcm "Ugh, where am I?"
    pcm "The hell am I doing in here?"
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8
    pc "..."
    pcm "What happened? I don't remember much..."
    pcm "Splitting headache though. Must have drunk way too much."
    pcm "Oh well, still have all my fingers and toes so isn't too bad."
    $ player.face_normal()
    jump travel

label haven_drunk_event_3:

    $ walk(loc_haven_utilities)
    $ pc_strip()
    $ time_sleep(120)
    $ time_sleep(120)
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    pcm "Ugh, where am I?"
    pcm "The hell am I doing in here? And why am I naked?"
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8
    pc "..."
    pcm "What happened? I don't remember much..."
    pcm "Splitting headache though. Must have drunk way too much."
    pcm "Oh well, still have all my fingers and toes so isn't too bad."
    $ player.face_normal()
    jump travel

label haven_drunk_event_4:
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ walk(loc_haven_room1)
    elif randomnum == 2:
        $ walk(loc_haven_room2)
    else:
        $ walk(loc_haven_room3)
    $ pc_strip()
    $ time_sleep(120)
    $ time_sleep(120)
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    pcm "Ugh, where am I? And why am I naked?"
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8

    pcm "Fuck..."
    "I look around for my clothes and find them nearby on the floor."
    pcm "Thankfully these didn't go missing. Can't imagine having to walk through here stark naked."
    $ pc_dress()
    pcm "Doesn't feel like anything happened to me while I was passed out. No idea how I ended up naked though."
    pc "..."
    if player.mood <= 20:
        $ player.face_cry()
        pc "*SOB*"
        if player.mood <= 0:
            pc "I want out of this place..."
    $ player.face_normal()
    jump travel

label haven_drunk_event_5:

    $ walk(loc_haven_utilities)
    $ pc_strip()
    $ time_sleep(120)
    $ haven_sleep_sex_loop()
    $ time_sleep(120)
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    pcm "Ugh, where am I?"
    pcm "The hell am I doing in here? And why am I naked?"
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8
    pc "..."
    pcm "What happened? I don't remember much..."
    pcm "Splitting headache though. Must have drunk way too much."
    pcm "Body is aching... Feels like some people took advantage of me being shit drunk..."
    if player.mood <= 20:
        $ player.face_cry()
        pc "*SOB*"
        if player.mood <= 0:
            pc "I want out of this place..."
    $ player.face_normal()
    jump travel

label haven_drunk_event_6:
    $ walk(loc_haven_room3)
    $ time_sleep(120)
    $ c.bottom = 0
    $ c.pants = 0
    $ haven_sleep_sex_loop()
    $ time_sleep(120)
    show haven_bentover nomanfull sleep at right
    $ player.inhib_sleep()
    $ player.face_normal()
    $ player.eye = 3
    show screen blackout(50) with Dissolve(2)
    pc "Uuuuuuuu..."
    show haven_bentover plead
    hide screen blackout with dissolve
    $ player.face_worried()
    $ player.eye = 2
    hide haven_bentover with dissolve
    pcm "Ugh, what the fuck?"
    pcm "..."
    pcm "Fuck..."
    "I look around for my shorts and find them nearby on the floor."
    pcm "Thankfully they didn't run off with these as well or I would be traipsing through this shithole with my bare arse hanging out."
    $ player.face_puke()
    pc "Ubbbbb!"
    $ player.mouth = 8
    $ pc_dress()
    pc "..."
    if player.mood <= 20:
        $ player.face_cry()
        pc "*SOB*"
        if player.mood <= 0:
            pc "I want out of this place..."
    $ player.face_normal()
    jump travel

label haven_drunk_event_7:
    $ walk(loc_haven_bed)
    $ time_sleep(120)
    show haven_sleep at right2
    jump haven_bed_sleep_join_blackout

label haven_drunk_event_8:
    $ travel_isolate()
    jump random_event_haven_ko
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
