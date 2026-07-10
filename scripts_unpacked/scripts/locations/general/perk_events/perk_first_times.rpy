default sex_first_time_dict = []

label first_time_return_catcher:
    return

label first_time_hsex:
    if any([player.beingraped, player.osex]):
        return
    jump expression WeightedChoice([
    ("former_male_first_handjob", If (player.has_perk(perk_male), 100, 0)),
    ("gamine_first_handjob", If (player.has_perk(perk_gamine), 100, 0)),
    ("bimbo_first_handjob", If (player.has_perk(perk_bimbo), 100, 0)),
    ("bambi_first_handjob", If (player.has_perk(perk_bambi), 100, 0)),
    ("oldbody_first_handjob", If (player.has_perk(perk_survivor), 100, 0)),
    ("girl_first_handjob", 1),
    ])

label first_time_osex:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("former_male_first_blowjob", If (player.has_perk(perk_male), 100, 0)),
    ("gamine_first_blowjob", If (player.has_perk(perk_gamine), 100, 0)),
    ("bimbo_first_blowjob", If (player.has_perk(perk_bimbo), 100, 0)),
    ("bambi_first_blowjob", If (player.has_perk(perk_bambi), 100, 0)),
    ("oldbody_first_blowjob", If (player.has_perk(perk_survivor), 100, 0)),
    ("girl_first_blowjob", 1),
    ])

label first_time_vsex:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("former_male_first_vagsex", If (player.has_perk(perk_male), 100, 0)),
    ("exhibitionist_first_vagsex", If (player.has_perk(perk_exhibitionist), 100, 0)),
    ("bimbo_first_vagsex", If (player.has_perk(perk_bimbo), 100, 0)),
    ("bambi_first_vagsex", If (player.has_perk(perk_bambi), 100, 0)),
    ("broodmother_first_vagsex", If (player.has_perk(perk_broodmother), 100, 0)),
    ("girl_first_vagsex", 1),
    ])

label first_time_asex:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("former_male_first_asssex", If (player.has_perk(perk_male), 100, 0)),
    ("girl_first_asssex", 1),
    ])

label first_time_swallow:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("perk_male_first_swallow", If (player.has_perk(perk_male), 100, 0)),
    ("bimbo_first_swallow", If (player.has_perk(perk_bimbo), 100, 0)),
    ("bambi_first_swallow", If (player.has_perk(perk_bambi), 100, 0)),
    ("broodmother_first_swallow", If (player.has_perk(perk_broodmother), 100, 0)),
    ("girl_first_swallow", 1),
    ])

label first_time_facial:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("perk_male_first_facial", If (player.has_perk(perk_male), 100, 0)),
    ("exhibitionist_first_facial", If (player.has_perk(perk_exhibitionist), 100, 0)),
    ("gamine_first_facial", If (player.has_perk(perk_gamine), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_creamvag:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("perk_male_first_creampie", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_creamanal:
    if player.beingraped:
        return
    jump expression WeightedChoice([
    ("perk_male_first_analcreampie", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_assault:
    jump expression WeightedChoice([
    ("perk_male_first_assault", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_rape:
    jump expression WeightedChoice([
    ("perk_male_first_rape", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_soldprice:
    jump expression WeightedChoice([
    ("perk_male_first_selloffer", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])

label first_time_soldpricetotal:
    jump expression WeightedChoice([
    ("perk_male_first_selltake", If (player.has_perk(perk_male), 100, 0)),
    ("first_time_return_catcher", 1),
    ])








label bambi_first_handjob:

    pcm "Ahh it so warm!"
    pcm "What do I do with it? Back and fourth? Probably..."
    return

label bimbo_first_handjob:

    pcm "Oooh who's a little cutie?"
    pcm "Err, not so little actually. Kinda big."
    pcm "Who's a giant weird looking mushroom? Yes, you are!"
    return

label gamine_first_handjob:

    pcm "First cock in my hand in this new body. No doubt won't be the last though."
    pcm "Feels different than than before though. Smaller hands maybe?"
    pcm "Whatever, still nice I guess."
    return

label girl_first_handjob:

    pcm "Hmm, bigger than I expected to see. This new body see things differently or is this guy particularly huge?"
    pcm "This guy is hard as a rock as well. So warm and kinda nice in my hand."
    pcm "Well, let's have some fun and see what he's got..."
    return

label oldbody_first_handjob:

    pcm "Hmm, bigger than I expected to see. Is this normal? Never actually had one in my hand before."
    pcm "This guy is hard as a rock as well. So warm and kinda nice in my hand."
    pcm "Well, let's have some fun and see what he's got..."
    return



label bambi_first_blowjob:
    $ player.face_confused()
    pcm "Oh shit. I' really doing this!"
    pcm "Hope he likes it..."
    return

label bimbo_first_blowjob:
    $ player.face_confused()
    pcm "Mmm, come here my sperm making friend."
    pcm "You look like a mushroom but you don't taste like one."
    pcm "Although mushrooms are tasty as well..."
    pcm "Come here my mushroom monster!"
    return

label gamine_first_blowjob:
    $ player.face_confused()
    pcm "Did this plenty before. No need to get all shy because of the new body."
    pcm "Mmm, not bad though..."
    pcm "Let's see if I can make him blow as quickly as I used to be able to."
    return

label girl_first_blowjob:
    $ player.face_confused()
    pcm "Okay. Here we go. Sucking a cock. It's normal. New body doesn't change that."
    pcm "I think I did this before... Probably did."
    pcm "Tongue under or around, no teeth, don't bite and use my hands."
    return

label oldbody_first_blowjob:
    $ player.face_confused()
    pcm "Okay. Here we go. Sucking a cock. It's normal."
    pcm "Might have never done this before coming here, but it's normal and lots of people do it."
    pcm "Tongue under or around, no teeth, don't bite and use my hands."
    return



label bambi_first_vagsex:
    pcm "Haa... Shit shit!"
    pcm "Nnng! He's inside me! First time. Haaaaa..."
    pcm "I need to relax. C'mon, relax... Let him in me."
    pcm "Haaaaa..."
    return

label bimbo_first_vagsex:
    pcm "Oh yeah! First time. C'mon, show me what you have."
    pcm "You got a dirty virgin on the end of your cock, so make her feel good."
    pcm "Fuck me and make me scream for my first time."
    pcm "Haaaaa..."
    return

label exhibitionist_first_vagsex:
    if loc_cur.outside:
        pcm "Oh fucking hell. Outside in the open taking a dick in me for the first time. So fucking hot!"
        pcm "Let everyone that sees us know you are taking my first time!"
    elif dis(dis_bus_interior):
        pcm "Oh fucking hell. On the bus in front of everyone taking a dick in me for the first time. So fucking hot!"
        pcm "Show me off to these other perverts how you are fucking a virgin!"
    elif dis(dis_pub):
        pcm "Oh fucking hell. Hopefully all the customers in the pub know you took me here to fuck my brains out!"
        pcm "Let all these pub perverts I am giving you my first time here like a dirty slut!"
    else:
        pcm "Haaaa fuck yes! Fuck me and I'll scream loud enough for others to hear."
        pcm "Maybe they will come to watch. Watch you fuck the virgin on the end of your cock."
    pcm "Well, no more a virgin. Your cock in me saw to that."
    pcm "Haaaa fuck!"
    return

label broodmother_first_vagsex:
    pcm "Oh fuck yes! Raw cock inside me just ready to give me it's cum."
    pcm "You going to take my virginity and leave a little baby in my belly to remember my first time by?"
    pcm "You fucking better or I'll have to fuck you again and again until you do."
    pcm "Ooooh fuck!"
    return

label girl_first_vagsex:
    pcm "Nnnnnggg. Haaa first time a cock is in me. He is stretching me open..."
    pcm "Relax. Let him inside me..."
    return


label girl_first_asssex:
    $ player.face_grit()
    pcm "Oooohhh! Christ a cock up the arse hurts."
    pcm "Relax relax..."
    pcm "Breathe in, breathe out. Relax around the cock breaking me in half."
    pcm "Whoa my legs are all jelly. All tingly everywhere."
    return



label gamine_first_swallow:
    $ player.face_shock()
    pcm "Oh, he's all in my mouth."
    pcm "Tastes... Better than I remember actually..."
    pcm "Maybe the shitty diet that everyone eats these days makes this stuff better."
    return

label bimbo_first_swallow:
    $ player.face_shock()
    pcm "Ohh, I feel him putting it all in my mouth. Mmmmm."
    pcm "Be a waste to spit it out after I went through all this effort to get it out."
    pcm "Plus it's kinda naughty to drink it up."
    return

label bambi_first_swallow:
    $ player.face_shock()
    pcm "Aiii, he squirting it in my mouth?!"
    pcm "What do I do? What do I do??"
    pcm "Too much and his cock is still in my mouth. Swallow it?"
    return

label broodmother_first_swallow:
    $ player.face_shock()
    pcm "Ah, he's putting it in my mouth?"
    pcm "Should I bend over so it can go somewhere better?"
    pcm "Ugh, too late for that now..."
    pcm "Well, at least it's inside me if I drink it. Can't knock me up but better than putting it to waste by spitting it out."
    return

label girl_first_swallow:
    $ player.face_shock()
    pcm "Oooh, in my mouth!?"
    pcm "Err... swallow it down right?"
    pcm "Well his cock is still in my mouth so no other choice anyway."
    return



label gamine_first_facial:
    $ player.face_shock()
    pcm "Ah shit. Not in the eye, not in the eye!"
    pcm "No matter where they point their thing, it always gets in the eye."
    return

label exhibitionist_first_facial:
    $ player.face_shock()
    pcm "Oooh, all over my face?"
    pcm "Going to let everyone else see that you just been having fun with me by showing off your work all over my face?"
    return

label girl_first_facial:
    $ player.face_shock()
    pcm "Ah, all over my face. It's quite warm actually."
    pcm "Kinda degrading but also kinda fun."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
