label dani_stairwell_talk_0:
    $ dani.dict["stairwell_talk"] += 1
    pc "Ah hey [dani.nname]. What you doing out here?"
    dani.name "Hey [name], just relaxing and killing time."
    pc "You live round here?"
    dani.name "Yeah just over there. You too?"
    pc "Yeah, that one there."
    dani.name "Ah so we are basically neighbours."
    pc "Yup!"
    jump dani_talk_end

label dani_stairwell_talk_1:
    $ dani.dict["stairwell_talk"] += 1
    pc "Why aren't you hanging out at the park just over there?"
    show dani worried
    dani.name "I do sometimes. But last time some weird naked guy rushed over to me barking and tried to bite my leg."
    if quest_wolfgang.isactive():
        pc "Ah, the dog weirdos."
        dani.name "Huh?"
        pc "People run around the park pretending to be dogs."
        dani.name "Right..."
    else:
        $ player.face_shock()
        pc "What?"
        dani.name "Yeah... Weird."
        $ player.face_worried()
        pc "Right..."
    jump dani_talk_end

label dani_stairwell_talk_2:
    $ dani.dict["stairwell_talk"] += 1
    dani.name "So hang out here now so I can rush home if any crazies come alone."
    pc "Nothing to do here, but at least you can see the lunatics coming."
    dani.name "Yup."
    pc "Why don't you hang out at home?"
    dani.name "At home? My place is a shithole."
    pc "That bad?"
    dani.name "I have a mattress on a chest of drawers because there wasn't enough room for both."
    pc "Wow..."
    jump dani_talk_end

label dani_stairwell_talk_3:
    $ dani.dict["stairwell_talk"] += 1
    pc "Still though, your shitty room is your own space."
    dani.name "I guess. Though unless it's really hot outside, my room is freezing."
    dani.name "Have to be fully clothed or wrap up in a blanket inside the place."
    pc "It at least have a lock on the door?"
    show dani worried
    dani.name "Err, I don't have a door."
    $ player.face_shock()
    pc "What?"
    dani.name "I have to climb in the window to get into my room."
    pc "Seriously?"
    $ player.face_neutral()
    show dani neutral
    jump dani_talk_end

label dani_stairwell_talk_4:
    $ dani.dict["stairwell_talk"] += 1
    pc "What's your flatmates like?"
    dani.name "Dunno. Barely see them and never talk to them."
    dani.name "None of them have tried to get in my room though so that's great."
    pc "Get in your room? Guys?"
    dani.name "Yeah. Think I am the only girl."
    pc "..."
    jump dani_talk_end

label dani_stairwell_talk_5:
    $ dani.dict["stairwell_talk"] += 1
    dani.name "What about your flatmates? How are they?"
    pc "Think you have met them. Or at least seen them around the academy."
    dani.name "Ah. I've seen you talk to the girl with short hair. She lives with you?"
    pc "Yeah."
    jump dani_talk_end

label dani_stairwell_talk_6:
    $ dani.dict["stairwell_talk"] += 1
    dani.name "How's your room? It as bad as mine?"
    pc "Not seen yours so not sure. But the way you describe it, no."
    pc "I at least have an actual bed frame with a mattress on it."
    dani.name "How do you afford that?"
    if t.day < 14:
        pc "Not sure yet. I just moved in. Maybe I can't afford it."
    elif oskar.sex:
        pc "Err... I help the landlord around a bit."
    else:
        pc "Umm, working?"
    jump dani_talk_end

label dani_stairwell_talk_7:
    $ dani.dict["stairwell_talk"] += 1
    dani.name "[oskar.name] your landlord as well?"
    pc "Yeah..."
    dani.name "Ugh."
    pc "Think he owns or runs or whatever all the buildings in this block."
    dani.name "Yeah? Ugh. How did someone like him manage that?"
    pc "No idea."
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
