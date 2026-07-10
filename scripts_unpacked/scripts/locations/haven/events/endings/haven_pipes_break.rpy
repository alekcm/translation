label haven_pipes_break_ending:
    $ loc_haven_landing.dict["gate_open"] = True
    $ add_to_list(main_quest_05.list, "flooded")
    if not haven_time_empty():
        "Just as I am about to leave the room, the door is opened by someone."
        show havman at right1 with dissolve
        hav "Tha fuck is goin' on in ere?"
        $ player.face_worried()
        hav "You in 'ere wrecking shit? Fucking bitch! What you go and do that to our home for?"
        $ player.face_shock()
        "He lunges forward to try and grab me, but my wet and naked body makes it hard for him to find somewhere to grab hold of."
        "I try to worm my way around him and out the door, but he does a good job of blocking my escape."
        pcm "Fuck, I need to get out of here."
        "I try to make another attempt to get out of the door when..."
        show haven_guard3 at right2
        show haven_guard2 at right4
        with dissolve
        havguard "The fuck is going on in here?"
        hav "This little bitch gone an wrecked the place."
        "The guard looks at me, notices the broken pipes and the crowbar near my feet."
        havguard "Whatcha go an do somethin like that for?"
        "The guards approach me and before I can react..."
        jump haven_caught_and_beaten
    else:

        "I rush out the room and thankfully the showers are totally empty."
        $ walk(loc_haven_shower_stall)
        pcm "Gotta be quick, the guards will be heading here soon. Fuck! I can hear them."
        $ walk(loc_haven_shower)
        pcm "Shit! No time to dress or they will catch me here and ask me what happened."
        $ walk(loc_haven_hallway_1f)
        pause 0.3
        $ walk(loc_haven_room1)
        pcm "..."
        "I hear some booted steps rush past the room then a whole lot of shouting and orders being barked."
        pcm "Guess they have seen the mess. Now, what the fuck do I do? I can't just stroll back into the showers butt naked and grab my clothes..."
        pcm "..."
        pcm "No choice, maybe I can find something to wrap around me upstairs. I have to get past that gate."
        pcm "Ok, go..."
        $ walk(loc_haven_hallway_1f)
        pcm "Quick quick..."
        $ walk(loc_haven_lobby)
        pause 0.5
        $ walk(loc_haven_landing)
        pcm "Yes! They left the gate open."
        jump haven_access_top_floor
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
