label action_beaten_start:
    show screen blackout(50)
    pause 0.5
    show screen blackout(100) with dissolve
    $ renpy.scene()
    $ travel_isolate()
    pause 0.5
    jump action_beaten_events_picker

label action_beaten_events_picker:
    jump expression WeightedChoice([
    
    
    ("action_beaten_event_general_1", 50), 

    ("action_beaten_event_nude_1", 200),
    ("action_beaten_event_nude_2", 200),  

    ("sleep_rough_wake_drunk", If(danger_weight(), 200, 0)), 
    ("sleep_rough_wake_vrare", If(danger_weight(), 100, 0)),

    ])

label action_beaten_event_general_1:
    $ player.grope_end()
    show screen blackout(50) with dissolve
    pc "Ugh..."
    pc "Fuck..."
    pcm "Damn. Did I get knocked out?"
    pcm "Fuck! My head is killing me."
    hide screen blackout with dissolve
    pcm "I need to be more careful."
    jump travel

label action_beaten_event_nude_1:
    $ player.grope_end()
    $ pc_strip()
    show screen blackout(50) with dissolve
    pc "Ugh..."
    pc "Fuck..."
    pcm "Damn. Did I get knocked out?"
    pcm "Fuck! My head is killing me."
    hide screen blackout with dissolve
    pcm "Shit! Where did my clothes go?"
    pcm "Fuck!"
    jump travel

label action_beaten_event_nude_2:
    $ player.grope_end()
    $ pc_loose_clothes_random()
    show screen blackout(50) with dissolve
    pc "Ugh..."
    pc "Fuck..."
    pcm "Damn. Did I get knocked out?"
    pcm "Fuck! My head is killing me."
    hide screen blackout with dissolve
    if pc_lost_clothes():
        pcm "Fuck, I had more than this on before..."
        pcm "Someone steal my clothes?"
        pc "Ugh!"
    else:
        pcm "I need to be more careful."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
