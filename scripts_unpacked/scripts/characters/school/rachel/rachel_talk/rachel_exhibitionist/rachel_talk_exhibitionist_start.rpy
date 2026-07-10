label rachel_talk_exhib_cheat:
    if not rachel.has_met:
        "You have not met rachel. Meeting her now."
        jump rachel_talk_meet_academy
    if not "rachel_exhib_talk" in rachel.dict:
        $ rachel.dict["rachel_exhib_talk"] = 0
    elif loc_school_secret_entrance.locked:
        "You havent discovered the secret entrace. Unlocking it now."
        $ loc_school_secret_entrance.locked = False
        jump travel
    elif not loc_school_secret_entrance.visited:
        "You havent visited the secret entrance. putting you there now."
        $ walk(loc_school_secret_entrance)
        jump loc_school_secret_entrance_visit
    elif not rachel.love >= 60:
        "You dont have enough affection with her. Boosting it now."
        $ rachel.talk_love_add(1000)
        jump travel
    elif rachel.dict["rachel_exhib_talk"] == 0:
        "Starting the rachel chain"
        jump rachel_talk_exhib_0
    else:
        "You have unlocked all the requirements. Go and talk to rachel."
        jump travel


label rachel_talk_exhib_0:
    $ rachel.dict["rachel_exhib_talk"] += 1
    rachel.name "You know a way to sneak in at night don't you?"
    pc "Err, sneak in here? Yeah I do."
    rachel.name "Can you show me?"
    pc "Err... Depends."
    rachel.name "Huh?"
    pc "If you trash the place or have a party, they will lock it up."
    rachel.name "Noo. Not like that."
    jump rachel_talk_end

label rachel_talk_exhib_1:
    $ rachel.dict["rachel_exhib_talk"] += 1
    $ add_to_list(rachel.list, "exhib_wait_outside")
    rachel.name "Soooo. Can you show me how to get inside?"
    pc "Only if you keep it secret and don't bring people here."
    rachel.name "Nooo. I can party in other places. I want somewhere alone and private."
    pc "Alone? No men?"
    rachel.name "Just me!"
    pc "Right... Meet me at night then when the place closes."
    rachel.name "Thanks!"
    $ log.assign("A place to be alone")
    jump rachel_talk_end

label rachel_talk_exhib_show:
    $ remove_from_list(rachel.list, "exhib_wait_outside")
    $ add_to_list(rachel.list, "exhib_inside_academy")
    $ rachel.dict["rachel_exhib_try"] = t.day
    rachel.name "Ah you came!"
    pc "Yeah."
    rachel.name "Show me show me!"
    pc "Right. Remember no messing this up for us."
    rachel.name "Nope. My lips are sealed."
    pc "Okay, along the fence here..."
    $ walk(loc_school_secret_entrance)
    pc "There is a hole here."
    rachel.name "Ahh."
    hide rachel
    show rachel_climbhole at right1
    with dissolve
    rachel.name "Nnng!"
    rachel.name "You do this every time?"
    pc "It gets easier with practice. Give everyone a show if you wear a skirt though."
    rachel.name "Huh?"
    pc "Nice pinkies."
    rachel.name "Ah. Like them?"
    pc "Sure."
    hide rachel_climbhole with hpunch
    pc "There you go."
    if c.skirt:
        pcm "Now to flash my arse getting though..."
    show rachel at right1
    $ walk(loc_school_field)
    pc "And we are in."
    rachel.name "What about inside the school?"
    pc "They dont lock the back doors so you can just walk in."
    rachel.name "Ahhh. Let's see..."
    $ walk(loc_school_hallway)
    rachel.name "Whooo!"
    pc "What do you want in here for anyway?"
    rachel.name "I want somewhere alone and private I can relax."
    rachel.name "I want to be alone."
    pc "Okay then."
    rachel.name "Thanks [name]!"
    hide rachel with dissolve
    pc "You're welcome..."
    pcm "She better not cause any trouble."
    $ log.markdone("quest_exhib_01")
    $ loc_school_hallway.opening_hours = []
    $ loc_school_gym.opening_hours = []
    $ loc_school_hallway_2f.opening_hours = []
    $ loc_school_toilet_girls.opening_hours = []
    $ loc_school_toilet_boys.opening_hours = []
    $ loc_school_toilet_girls_stall.opening_hours = []
    $ loc_school_toilet_boys_stall.opening_hours = []
    $ loc_school_locker_girls.opening_hours = []
    $ loc_school_locker_boys.opening_hours = []
    $ loc_school_library.opening_hours = []
    $ loc_school_cafe.opening_hours = []

    jump travel

label rachel_talk_exhib_inside_talk_0:
    $ rachel.dict["rachel_exhib_try"] = t.day
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    pc "So having fun in here?"
    rachel.name "Fun?"
    pc "Yeah. Whatever you do here."
    rachel.name "Err, sure am! No one to disturb be here."
    pc "Except me."
    rachel.name "Ah yeah. Shoo!"
    pc "Ha!"
    jump rachel_talk_end

label rachel_talk_exhib_inside_talk_1:
    $ rachel.dict["rachel_exhib_try"] = t.day
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    $ add_to_list(rachel.list, "stripping_trigger")
    rachel.name "Ah, sneaking in here."
    pc "Yeah."
    rachel.name "What you doing here?"
    pc "Err, just came to chat."
    rachel.name "You are messing with my alone time."
    pc "Right..."
    jump rachel_talk_end

label rachel_talk_exhib_inside_talk_2:
    $ add_to_list(rachel.list, "is_stripping")
    $ rachel.dict["rachel_exhib_try"] = t.day
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    pc "Hmm, no [rachel.name] today?"
    jump travel

label rachel_talk_exhib_inside_talk_3:
    $ rachel.dict["rachel_exhib_try"] = t.day
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    pc "Still no [rachel.name]? Did she stop coming here?"
    jump travel




label rachel_talk_exhib_inside_notalk_0:
    $ rachel.dict["rachel_exhib_try"] = (t.day - 1)
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    pcm "I should probably check on [rachel.name] at some point and make sure she isn't doing something weird at night in the gym."
    jump travel

label rachel_talk_exhib_inside_notalk_1:
    $ rachel.dict["rachel_exhib_try"] = (t.day - 1)
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    $ add_to_list(rachel.list, "stripping_trigger")
    jump travel

label rachel_talk_exhib_inside_notalk_2:
    $ add_to_list(rachel.list, "is_stripping")
    $ rachel.dict["rachel_exhib_try"] = (t.day - 1)
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    jump travel

label rachel_talk_exhib_inside_notalk_3:
    $ rachel.dict["rachel_exhib_try"] = (t.day - 1)
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    pcm "I should see what [rachel.name] is up to in the gym at night."
    jump travel



label rachel_talk_exhib_inside_talk_4:
    $ add_to_list(rachel.list, "show_stripping")
    $ remove_from_list(rachel.list, "stripping_trigger")

    $ rachel.dict["rachel_exhib_try"] = t.day
    $ rachel.dict["rachel_exhib_inside_talk"] += 1
    $ player.face_shock()
    pc "Ah!"
    show rachel nude angry at right1 with dissolve
    rachel.name "What the fuck [name]? Why do you keep showing up?"
    pc "Err... To say hello?"
    $ player.eye = 6
    pc "..."
    pc "You're... Naked?"
    $ player.eye = 1
    $ player.mouth = 8
    rachel.name "Duh!"
    pc "..."
    pc "Why?"
    show rachel neutral
    rachel.name "Trying things out."
    pc "Trying what out?"
    rachel.name "Being naked."
    pc "Okay... Why?"
    rachel.name "Why not? Seemed like it could be fun so I tried it."
    rachel.name "So I wanted somewhere private."
    show rachel angry
    rachel.name "But you keep showing up!"
    pc "Sorry?"
    rachel.name "Are you?"
    pc "Err, yes?"
    rachel.name "Get naked!"
    pc "Whaa?"
    rachel.name "Undress."
    pc "Why?"
    rachel.name "So we are equal."
    pc "Errr..."
    if player.check_sex_agree(5, exhibitionist=True):
        menu:
            "Okay":
                pc "Right then..."
                $ pc_striptease(temp=True)
                pc "Happy?"
                rachel.name "Yup!"
                hide rachel with dissolve
                pc "Okay then..."
            "Err, no thanks":
                rachel.name "Then shoo and leave me be!"
                pc "Okay..."
                hide rachel
                $ walk(loc_school_field)
                pcm "That was weird..."
    else:
        rachel.name "Then shoo and leave me be!"
        pc "Okay..."
        hide rachel
        $ walk(loc_school_field)
        pcm "That was weird..."

    $ log.markdone("quest_exhib_02")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
