label haven_lounge_fire_hangout:
    "I decide to hang out by the fire to kill some time."
    if haven_time_empty():
        pcm "Kind of peaceful round here while it is so quiet."
    else:
        jump expression WeightedChoice([
        ("haven_lounge_fire_hangout_1", 100),
        ("haven_lounge_fire_hangout_2", 100),
        ("haven_lounge_fire_hangout_3", 100),
        ("haven_lounge_fire_hangout_4", 100),
        ("haven_lounge_fire_hangout_meetvik", If(not havenvik.has_met and haven_time_danger(), 100, 0)),
        ("haven_lounge_fire_hangout_intel_1", If (haven_time_danger(), 30, 0)),
        ("haven_lounge_fire_hangout_intel_2", If (haven_time_danger(), 30, 0)),
        ])
    $ relax(20)
    $ player.add_mood(10)
    jump travel_arrival

label haven_lounge_fire_hangout_1:
    " temp event"
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_2:
    " temp event"
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_3:
    " temp event"
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_4:
    " temp event"
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_meetvik:
    show haven_viktor at right1 with dissolve
    $ havenvik.dict["brew_stage"] = 1
    havenvik.name "Hey little thing. Looking fa some brew?"
    pc "Huh?"
    havenvik.name "Some booze. Interested?"
    pc "Err, sure."
    havenvik.name "'Ere. Free sample since ya new roun' these parts."
    $ inv.take(item_brew)
    havenvik.name "Gotta pay next time though ya hear?"
    pc "Thanks. Pay how much?"
    havenvik.name "50 a jar. But new little bird like you, we can arrange something else."
    if player.check_sex_agree(2, notif=False):
        pc "Will something else wind up with me naked."
        havenvik.name "Yup. Else you have somethin' else ta barter with."
    else:
        pc "Err. Like what?"
        havenvik.name "Pretty girl like you. What do you think?"
        pc "Oh."
    pc "We'll see."
    havenvik.name "That we will. Have fun."
    hide haven_viktor with dissolve
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_intel_1:
    hav "...least he knew how to do that. It's how we got so much brew here. That Doctor couldn't fix a person but knew how to get a still going."
    pcm "They talking about [ant.name]?"
    hav "...why he went over to those lot. Not just booze you can learn when going to doctor school. Load of other tricks as well so they wanted him over there to cook something up."
    hav "Think so? Didn't seem like he would be interested in that. Came here all noble but is just shit like all the rest."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_1")
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_intel_2:
    hav "...like he had been in a fire. Come in 'ere like he owns the place claiming he would know better 'cos he is a Doctor or summit."
    pcm "Doctor. What about him?"
    hav "...probably running away 'cos he has some disease and they wanna lock him up 'fore he spreads it."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_2")
    jump haven_lounge_fire_hangout_end

label haven_lounge_fire_hangout_end:
    $ relax(20)
    $ player.add_mood(10)
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
