default school_toilet_boy_prompt = False

label loc_school_visit:
    $ player.face_worried()
    if t.day in (1,2):
        pcm "This is the school I am supposed to attend. Ugh..."
        pcm "Looks locked though. Should come back on Monday."
    elif t.hour in irange(8,10):
        pcm "Okay. First day of school is it?"
        pcm "Not looking forward to this..."
    elif t.hour in irange(11,14):
        pcm "Probably not the best idea to turn up so late for my first day of school. But whatever."
    else:
        pcm "This is the academy I am supposed to attend. Ugh..."
        pcm "Looks open so I can walk around if I want to. But is too late for classes."
    jump travel

label loc_school_hallway_visit:
    $ player.face_worried()
    if t.day == 3 and t.hour in irange(7,11):
        pcm "First day of school then..."
        if "school" in tab_top:
            pcm "Got my uniform on so I shouldn't stand out. Just go about it like it's normal."
            if player.has_perk(perk_male) and c.skirt:
                pcm "Gonna take some time getting used to this skirt though. Not looking forward to having the boys try to look up it."
                pcm "Fuck..."
    pcm "Place looks..."
    pcm "Old."
    pcm "It's all run down but also looks like people try to maintain it."
    pcm "Ah well, not like I can expect much better considering everything that's been going on."
    jump travel

label loc_school_hallway_2f_visit:
    pcm "Looks even worse up here than down there. Do they not look after things up here."
    pcm "Doesn't look like there are classrooms here so maybe not."
    pcm "Library... Did they really just paint the sign? Some other rooms... What are they? Club type places?"
    pcm "Whatever, I can just look inside and see."
    jump travel

label loc_school_library_visit:
    pcm "Hmm, is actually stocked with books. Thought this stuff would have been used as firewood a long time ago."
    pcm "Pretty quiet here. Doubt anyone is interested in reading with all the shit going on around us."
    pcm "Can probably relax here without issues."
    jump travel

label loc_school_hallway_closed:
label loc_school_gym_closed:
    if t.hour == 7:
        pc "School isn't open yet. I will have to wait around for a bit."
        if t.minute >= 40 and t.wkday in weekdays:
            pcm "Think I'll go over and chat to the other girls waiting for the school to open."
            $ walk(loc_school)
            pc "Hey."
            girl "Hey, waiting for it to open as well?"
            pc "Yeah."
            "I hang around and chat for a bit as more people arrive and wait around."
            $ time_round_to_hour()
            girl "Looks like they are opening. I am gonna go inside. See you round."
            pc "See you round."
            pcm "I should head inside as well."
            $ walk (loc_school_hallway)
            jump travel
    elif loc(loc_school) and loc_school_secret_entrance.visited:
        jump loc_school_use_back
    elif t.hour < 7:
        pc "School doesn't open for some time yet. I should go and do something else."
    else:
        pc "School is closed. I will have to wait until tomorrow."
    if not loc(loc_school):
        $ walk(loc_school)
    jump travel

label school_hallway_locked_start:
    pcm "The school doesn't open until Monday."
    jump travel

label school_toilet_boy_arrival:
    if (player.confidence >= 50 or player.check_sex_agree(4, notif=False)) and school_toilet_boy_prompt == False:
        $ player.face_shy()
        pcm "This is the men's toilet. I probably shouldn't be going inside..."
        menu:
            "Enter anyway":
                $ school_toilet_boy_prompt = True
                $ player.face_normal()
            "Yeah, I shouldn't go inside":
                $ player.face_normal()
                jump travel

    elif school_toilet_boy_prompt == False:
        $ player.face_worried()
        pcm "It's the men's toilet. I shouldn't be going in there."
        $ player.face_normal()
        jump travel

    elif str(t.day) + str(t.hour) in random_event_school_boys_toilet_var:
        call random_event_school_boys_toilet_return from _call_random_event_school_boys_toilet_return

    $ walk(loc_school_toilet_boys)

label school_locker_boy_arrival:
    pcm "I shouldn't be going in there."
    jump travel

label loc_school_chem_visit:
    "New location where you can make drugs from ingredients found while scavenging."
    "Can also buy knock off beer from the boys here."
    jump travel

label school_darkroom_arrival:

    jump school_photo_quest_picker

label loc_school_darkroom_closed:
    pcm "Closed. He should be here in the afternoon when the school is empty."
    if loc(loc_school_darkroom):
        $ walk(loc_school_hallway_2f)
    jump travel

label school_field_secret_entrance:
    if not school_soccer_quest_backentrance["used"]:
        $ school_soccer_quest_backentrance["used"] = True
        $ loc_school_field.opening_hours = []
        $ loc_school_field_back.opening_hours = []
        $ loc_school_locker_old.opening_hours = []
        pcm "Hmm, near the bushes there is a hole..."
        $ walk(loc_bushes)
        pcm "Let's see..."
        $ player.face_happy()
        pcm "Ah, yes! There we go."
        $ player.face_worried()
        pcm "Err..."
        pcm "That's a pretty small hole."
        if havenvent.vsex > 0:
            show haven_vent shortsoff giveup tears man at right2 with dissolve
            pcm "..."
            $ player.face_angry()
            hide haven_vent with dissolve
            pcm "I swear, if something like that happens again I am going to make it my life's work to chop off and collect as many penises as possible!"
            pc "*Sigh*"
        $ player.face_neutral()
        pcm "Well, might as well give it a go."
        pc "Hup!"
        with vpunch
        $ player.face_pain()
        pc "Ung!"
        with vpunch
        $ walk(loc_school_field, trans=hpunch)
        if c.skirt and c.bottom:
            $ c.bottom = 0
            $ player.face_confused()
            pcm "There we..."
            $ player.face_annoyed()
            pc "Ah fuck!"
            pcm "Snagged on the fence."
            $ pc_dress()
            pc "*Sigh*"
            $ player.face_neutral()
        else:
            pc "There we go."
        jump travel
    else:

        $ walk(loc_school_field)
        jump travel

label loc_school_sewroom_locked:
    pcm "The door is locked."
    if any([frida.has_met, saskia.has_met]):
        if t.wkday in weekend:
            pcm "The girls are usually at their stall in the market on weekends."
    jump travel

label school_cafe_eat:
    if not player.cash >= 5:
        pcm "I'm hungry but no money to buy anything..."
        jump travel
    else:
        jump random_event_school_hungry_2

label loc_school_use_back:
    pcm "It's locked. I need to use the back way."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
