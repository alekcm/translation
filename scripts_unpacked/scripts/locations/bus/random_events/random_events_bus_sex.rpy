label random_event_bus_sex_stumble:
    with hpunch
    "I pretend to stumble on the bus and press my ass right against his groin."
    $ player.grope_hips(steal=True)
    pcm "That's better."
    jump random_event_bus_sex_hump_want

label random_event_bus_sex_drunk:
    with hpunch
    "I stumble onto some guy and he doesn't seem to mind much."
    $ player.grope_hips(steal=True)
    pcm "Ugh..."
    jump random_event_bus_sex_hump_want

label random_event_bus_sex_choice:
    pcm "Huh?"
    pcm "Is that his cock poking between my legs??"
    pcm "Errrr..."
    if player.check_sex_agree_choice(3, "Having fun?", "Sorry mate"):
        jump random_event_bus_sex_want
    else:
        jump random_event_bus_sex_evade

label random_event_bus_sex_hump_want:
    $ player.grope_poke(steal=True)
    pcm "That what I think it is?"
    $ player.grope_poke()
    pcm "Errrr..."
    $ player.grope()
    pcm "Mmmmm..."
    "I gently fall into his rhythm and press back against him as he is rubbing his cock against me."
    $ player.grope(steal=True)
    pcm "Mmm, kinda fun."
    $ player.grope(steal=True)
    if c.can_access_vag():
        jump random_event_bus_sex_choice
    if not numgen(0,3):
        if numgen():
            $ grope_mastright = True
        else:
            $ grope_mastleft = True
        $ player.grope(steal=True)
        pcm "Oh? Some other perverts noticed."
        if player.has_perk(perk_exhibitionist, notif=True):
            pcm "Fucking hell. They are watching and wanking over me. This is exciting."
        pcm "Mmmmmmm..."
        pcm "Watch this pervert do what he wants!"
    pc "Oooh."
    pcm "Shit, need to be quiet."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Oooh?"
    $ player.sex_cum(busgroper, "ass")
    pervert "Ahhhh!"
    pcm "..."
    if any([grope_mastright, grope_mastleft]):
        $ player.sex_cum(busgroper, "belly")
        pcm "Oh, you wanker decided to cum as well?"
        pcm "Dirty man."
        $ grope_mastleft = False
        $ grope_mastright = False
    pc "*Phew*"
    pcm "Well that was fun..."
    $ player.grope_end()
    "The guy let's go of me and I don't even look back to see who it was."
    jump bus_travel_end


label random_event_bus_sex_want:
    if not c.can_access_vag():
        pcm "Mmmm..."
        $ c.bottom = 0
        $ c.outfit = 0
        pcm "Oh? Taking it off are you?"
        if not c.can_access_vag():
            $ c.pants = 0
    pcm "..."
    $ player.sex_vag(busgroper)
    $ player.grope_insert(steal=True)
    pc "Haaaa... ♥"
    pcm "Ah, didn't think I would be getting fucked on the bus..."
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "In front of so many people. So fucking HOT!"
        pcm "Mmmmmm..."
    $ player.grope(steal=True)
    pcm "Mmmmmm. Keep going you pervert!"
    "I gently fall into his rhythm and press back against him as he is thrusting into me."
    $ player.grope(steal=True)
    "We don't have much room so we need to be somewhat discreet. Thought the bus is always full of deviants so probably not the first time they have seen this."
    if not numgen(0,3):
        if numgen():
            $ grope_mastright = True
        else:
            $ grope_mastleft = True
        $ player.grope(steal=True)
        pcm "Oh? Some other perverts noticed."
        if player.has_perk(perk_exhibitionist, notif=True):
            pcm "Fucking hell. They are watching and wanking over me. I think I'm gonna explode."
        pcm "Mmmmmmm..."
        pcm "Watch me get fucked!"
    pc "Oooh."
    pcm "Shit, need to be quiet."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Oooh?"
    $ player.sex_cum_location_offer( 
    difficulty=3, 
    cum_want="random_event_bus_sex_cum_inside_want", 
    cum_notwant="random_event_bus_sex_cum_inside_notwant", 
    cum_pullout="random_event_bus_sex_cum_pullout",
    )

label random_event_bus_sex_notwant:
    $ player.sex_forced(busgroper)
    if not c.can_access_vag():
        pcm "Ah!"
        $ c.bottom = 0
        $ c.outfit = 0
        pcm "Fuck fuck fuck!!"
        if not c.can_access_vag():
            $ c.pants = 0
    pcm "..."
    $ player.sex_vag(busgroper)
    $ player.grope_insert(steal=True)
    pc "Nnng!"
    pcm "No! Not on the bus like this..."
    $ player.grope(steal=True)
    $ player.face_cry()
    pc "*Sob*"
    "I stand there limp as he rocks me back and forth. I just try to pretend nothing is happening and hope no one has noticed."
    $ player.grope(steal=True)
    "Since there is not much room, he is being mostly discreet and not drawing attention to us."
    if not numgen(0,3):
        if numgen():
            $ grope_mastright = True
        else:
            $ grope_mastleft = True
        $ player.grope(steal=True)
        pcm "SHIT! Someone noticed."
        pcm "Fuck..."
    pc "Nnng!"
    pcm "Shit, need to be quiet."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Noooooo..."
    jump random_event_bus_sex_cum_inside_notwant

label random_event_bus_sex_passive:
    if not c.can_access_vag():
        pcm "Err..."
        $ c.bottom = 0
        $ c.outfit = 0
        pcm "Oh no..."
        if not c.can_access_vag():
            $ c.pants = 0
    pcm "..."
    $ player.sex_vag(busgroper)
    $ player.grope_insert(steal=True)
    pc "Nnng!"
    pcm "No! Not on the bus like this..."
    $ player.grope(steal=True)
    $ player.face_cry()
    pc "..."
    "I stand there limp as he rocks me back and forth. I just try to pretend nothing is happening and hope no one has noticed."
    $ player.grope(steal=True)
    "Since there is not much room, he is being mostly discreet and not drawing attention to us."
    if not numgen(0,3):
        if numgen():
            $ grope_mastright = True
        else:
            $ grope_mastleft = True
        $ player.grope(steal=True)
        pcm "Huh? Fuck. Someone else..."
        pcm "..."
    pc "Nnng!"
    pcm "Ah, I should be quiet so no one notices."
    $ player.grope(steal=True)
    pcm "Nnng. Not easy..."
    $ player.grope(steal=True)
    $ player.grope(steal=True)
    pcm "Noooooo..."
    jump random_event_bus_sex_cum_inside_notwant

label random_event_bus_sex_cum_inside_want:
    pcm "Mmmmmm..."
    $ player.grope(steal=True)
    pcm "Keep... Going... ♥"
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    if any([grope_mastright, grope_mastleft]):
        $ player.sex_cum(busgroper, "belly")
        pcm "Oh, you wanker decided to cum as well?"
        pcm "Dirty man."
        $ grope_mastleft = False
        $ grope_mastright = False
    $ player.grope()
    pc "*Huff*"
    pcm "Mmmmmm..."
    pcm "Well that was fun..."
    $ player.grope_end()
    "I let the guy slip out of me and pretend like nothing happened."
    jump bus_travel_end

label random_event_bus_sex_cum_inside_notwant:
    pcm "No no. Not inside..."
    $ player.grope(steal=True)
    "I press against the guy and try to push him away hoping he gets the message."
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Fuuuuuck!!!"
    $ player.grope()
    pcm "Outside! Outside!"
    pervert "Haaaaa..."
    $ player.grope()
    if any([grope_mastright, grope_mastleft]):
        $ player.sex_cum(busgroper, "belly")
        pcm "Ah shit. You as well?"
        pcm "Dammit."
        $ grope_mastleft = False
        $ grope_mastright = False
    $ player.grope()
    pc "*Huff*"
    pcm "..."
    $ player.grope_end()
    "The guy slips out of me and I try to pretend like nothing happened."
    jump bus_travel_end

label random_event_bus_sex_cum_inside_force:
    pcm "No no. Not inside..."
    $ player.grope(steal=True)
    "I struggle against the guy, trying to get him out from inside me."
    pervert "Nnnnnngggg..."
    $ player.sex_cum(busgroper, "inside")
    pcm "Fuuuuuck!!!"
    $ player.grope()
    pcm "Outside! Outside!"
    with hpunch
    pervert "Haaaaa..."
    $ player.grope()
    if any([grope_mastright, grope_mastleft]):
        $ player.sex_cum(busgroper, "belly")
        pcm "Ah shit. You as well?"
        pcm "Dammit."
        $ grope_mastleft = False
        $ grope_mastright = False
    $ player.grope()
    $ player.face_cry()
    pc "*SOB*"
    pcm "..."
    $ player.grope_end()
    "The guy slips out of me and I sob to myself while trying to pretend nothing happened."
    jump bus_travel_end

label random_event_bus_sex_cum_pullout:
    pcm "No no. Not inside..."
    $ player.grope(steal=True)
    "I press against the guy and try to push him away hoping he gets the message."
    pervert "Nnnnnngggg..."
    $ player.grope_poke()
    $ player.sex_cum(busgroper, "pullout")
    pcm "Mmmmmmm..."
    $ player.grope()
    pervert "Haaaaa..."
    $ player.grope()
    if any([grope_mastright, grope_mastleft]):
        $ player.sex_cum(busgroper, "belly")
        pcm "Oh, you wanker decided to cum as well?"
        pcm "Dirty man."
        $ grope_mastleft = False
        $ grope_mastright = False
    $ player.grope()
    pc "*Huff*"
    pcm "Mmmmmm..."
    pcm "Well that was fun..."
    $ player.grope_end()
    "The guy pulls his cock from between my legs and I just pretend like nothing happened."
    jump bus_travel_end

label random_event_bus_sex_evade:
    with hpunch
    if player.check_fight(2):
        $ player.grope_end()
        "I disentangle myself from the groper and head towards the entrance of the bus."
        pc "*Phew*"
        jump bus_travel_end
    else:
        "I try to get out of the gropers arms but he doesn't let up and keeps me where I am."
        if player.has_perk([perk_sucu, perk_slut, perk_bimbo], notif=True) or player.check_sex_agree(5):
            jump random_event_bus_sex_want
        else:
            jump random_event_bus_sex_notwant
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
