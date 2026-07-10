init python:
    def exhib_stat_changes():
        if perk_exhibitionist.dict["exhib_event_trigger"] <= 3:
            player.add_mood(-3)
        if perk_exhibitionist.dict["exhib_event_trigger"] <= 5:
            player.add_desire_random(5)
        if perk_exhibitionist.dict["exhib_event_trigger"] <= 6:
            player.add_desire_random(5)
        if perk_exhibitionist.dict["exhib_event_trigger"] <= 7:
            player.add_desire_random(10)

label random_event_generic_exhib_cover:
    $ exhib_stat_changes()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_sad", If(perk_exhibitionist.dict["exhib_counter"] < 100, 100, 0)),
    ("random_event_generic_exhib_neutral", If(100 <= perk_exhibitionist.dict["exhib_counter"] <= 200, 100, 0)),
    ("random_event_generic_exhib_happy", If(perk_exhibitionist.dict["exhib_counter"] > 200, 100, 0)),
    ("random_event_generic_exhib_empty", 300),

    ])






label random_event_chain_exhib_0:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    pcm "How is it I always end up walking around showing my ass off?"
    jump travel

label random_event_chain_exhib_1:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    pcm "Again and again I am walking around with everything hanging out."
    jump travel

label random_event_chain_exhib_2:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    pcm "..."
    $ player.uncover()
    $ player.face_happy()
    pcm "Hehe"
    pcm "..."
    $ player.cover()
    jump travel

label random_event_chain_exhib_3:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "I suppose it's not so bad walking around like this..."
    pcm "Was super scary at first. But been showing off so much I sometimes forget that I am..."
    $ player.cover()
    jump travel

label random_event_chain_exhib_4:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "Am I doing this on purpose or something? Showing myself off to all these damn perverts."
    $ player.cover()
    jump travel

label random_event_chain_exhib_5:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "Showing off again...?"
    pcm "Whatever. I don't mind. Look at me you damn perverts."
    $ player.cover()
    jump travel

label random_event_chain_exhib_6:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    if c.cansee_ass_clothes_check() <= 2:
        pcm "You perverts like looking at my ass when you think I can't see you?"
    elif c.cansee_breasts_clothes_check() <= 2:
        pcm "You perverts like looking at my tit's when you think I am not looking?"
    elif c.cansee_vag_clothes_check() <= 2:
        pcm "You dirty men like seeing what I have down there? Sneaking a look when you think I won't notice."
    else:
        pcm "You dirty perverts like looking at me? You think I don't notice you looking?"
    $ player.cover()
    jump travel

label random_event_chain_exhib_7:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "Take a good look you perverts."
    jump travel

label random_event_chain_exhib_8:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "You like seeing what I have to show?"
    jump travel

label random_event_chain_exhib_9:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "Walking around like this makes me kind of excited..."
    pcm "Maybe I should do something more extreme?"
    jump travel

label random_event_chain_exhib_10:
    $ perk_exhibitionist.dict["exhib_event_trigger"] += 1
    $ player.uncover()
    pcm "Yeah, something much more extreme would be fun."
    pcm "Maybe run around naked at night or something?"
    pcm "..."
    pcm "Hehe."

    jump travel





label random_event_generic_exhib_sad:
    jump expression WeightedChoice([
    ("random_event_generic_exhib_sad_1", 100),
    ("random_event_generic_exhib_sad_2", If(player.cover_breasts, 100, 0)),
    ("random_event_generic_exhib_sad_3", If(player.cover_vagina, 100, 0)),
    ("random_event_generic_exhib_sad_4", If(player.cover_ass, 100, 0)),
    ])

label random_event_generic_exhib_sad_1:
    $ player.face_worried()
    pcm "People are looking at me. I need to cover up some more."
    jump travel

label random_event_generic_exhib_sad_2:
    $ player.face_worried()
    pcm "People can see my boobs. I really need to wear something better."
    jump travel

label random_event_generic_exhib_sad_3:
    $ player.face_worried()
    pcm "I need to cover up better. People can basically see me exposing myself."
    jump travel

label random_event_generic_exhib_sad_4:
    $ player.face_worried()
    if c.skirt:
        pcm "This skirt doesn't hide much and I'm showing my ass off. I need to wear something better."
    elif c.thong:
        pcm "These pants do nothing to hide my arse. I need to wear something better."
    else:
        pcm "Everyone can see my ass. I should cover up more."
    jump travel

label random_event_generic_exhib_neutral:
    jump expression WeightedChoice([
    ("random_event_generic_exhib_neutral_1", 100),
    ("random_event_generic_exhib_neutral_2", If(player.cover_breasts, 100, 0)),
    ("random_event_generic_exhib_neutral_3", If(player.cover_vagina, 100, 0)),
    ("random_event_generic_exhib_neutral_4", If(player.cover_ass, 100, 0)),
    ])

label random_event_generic_exhib_neutral_1:
    $ player.face_worried()
    pcm "People are looking at me as usual..."
    jump travel

label random_event_generic_exhib_neutral_2:
    $ player.face_worried()
    pcm "Cant keep your eyes of my chest can you?"
    jump travel

label random_event_generic_exhib_neutral_3:
    $ player.face_worried()
    pcm "Don't drool too much you perverts."
    jump travel

label random_event_generic_exhib_neutral_4:
    $ player.face_worried()
    pcm "They barely make a secret of trying to get a look at my arse."
    jump travel

label random_event_generic_exhib_happy:
    jump expression WeightedChoice([
    ("random_event_generic_exhib_happy_1", 100),
    ("random_event_generic_exhib_happy_2", If(player.cover_breasts, 100, 0)),
    ("random_event_generic_exhib_happy_3", If(player.cover_vagina, 100, 0)),
    ("random_event_generic_exhib_happy_4", If(player.cover_ass, 100, 0)),
    ])

label random_event_generic_exhib_happy_1:
    $ player.face_happy()
    pcm "Have a good look you dirty perverts."
    jump travel

label random_event_generic_exhib_happy_2:
    $ player.face_happy()
    pcm "Like looking at my tits do you?"
    jump travel

label random_event_generic_exhib_happy_3:
    $ player.face_happy()
    pcm "Yup, have a look at where you wish your cock was going."
    jump travel

label random_event_generic_exhib_happy_4:
    $ player.face_happy()
    pcm "Don't even need to bend over to give you boys a good look."
    jump travel

label random_event_generic_exhib_empty:
    jump travel
    jump random_event_picker_tombola
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
