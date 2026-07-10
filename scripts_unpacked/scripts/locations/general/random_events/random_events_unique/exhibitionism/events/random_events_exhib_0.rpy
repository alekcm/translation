label random_event_generic_exhib_0_1:
    pcm "Fuck! I can't be out here looking like this..."
    $ travel_isolate()
    pcm "Maybe I can look around here for something to cover up with."
    jump travel

label random_event_generic_exhib_0_2:
    pcm "Not so busy out here, but people can still see me. I really need to find something to wear."
    jump travel

label random_event_generic_exhib_0_3:
    $ player.face_shy()
    pcm "I can't believe I am out here like this."
    pcm "Someone is bound to see me."
    jump travel

label random_event_generic_exhib_0_4:
    $ player.face_shy()
    pcm "Maybe I can go hide somewhere until it's dark?"
    $ travel_isolate()
    pcm "If I wait here, I might be able to sneak home late at night."
    jump travel

label random_event_generic_exhib_0_5:
    $ player.face_shy()
    pc "Ahhh!"
    $ travel_isolate()
    pcm "Shit! Someone saw me!"
    pcm "..."
    pcm "Fuck. Do I just wait here or something?"
    if not numgen(0,10):
        $ male_npc_create_all()
        show male_generic
        man "Hey darling."
        pc "Ah!"
        man "Having fun here?"
        pc "What? No! Go away!"
        if not numgen(0,10):
            man "Really? Okay then."
            pc "..."
            pcm "Wow. He actually left."
        else:
            man "Looks like you need some clothes."
            pc "..."
            pc "Yeah, I do."
            man "I got some you can have for a price."
            jump random_event_generic_exhib_general_sex_for_clothes

    jump travel

label random_event_generic_exhib_0_6:
    if c.cansee_breasts:
        pcm "Dammit, everyone can see my tits."
    elif c.cansee_ass:
        pcm "Dammit. I am walking with ym ass out."
    else:
        pcm "Dammit, people can see me like this."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
