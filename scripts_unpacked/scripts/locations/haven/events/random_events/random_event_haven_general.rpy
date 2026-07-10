label random_event_haven_desire_1:
    pause 0.1
    $ player.face_surprised()
    with grope_trans
    pc "Ugn!"
    pcm "Damn this plug..."
    jump travel

label random_event_haven_desire_2:
    $ player.face_shy()
    pc "*Huuu*"
    pcm "At his rate, I might have to go peep in the showers..."
    jump travel

label random_event_haven_desire_3:
    $ player.face_shy()
    pcm "Did they really have to put a plug the size of my fist up my arse? This thing is driving me wild."
    jump travel

label random_event_haven_desire_4:
    $ player.face_shy()
    pcm "Wonder if I should keep this plug when I get out of this place?"
    jump travel

label random_event_haven_desire_5:
    $ player.face_shy()
    pcm "Maybe I should go and get caught by that pervert from the peephole."
    jump travel

label random_event_haven_hygiene_1:
    pcm "I am starting to really smell..."
    jump travel

label random_event_haven_hygiene_2:
    pcm "I know this is a homeless community. But I should at least try not to stink like the homeless."
    jump travel

label random_event_haven_hygiene_3:
    pcm "Ugh, I really need to shower."
    jump travel

label random_event_haven_harass_1:
    hav "Hey."
    $ player.spank()
    if player.check_sex_agree(4,notif=False):
        $ player.face_shy()
    else:
        pcm "Idiot."
    jump travel

label random_event_haven_harass_2:
    $ player.grope()
    pc "AH!"
    $ player.grope_end()
    with vpunch
    if player.check_sex_agree(4,notif=False):
        $ player.face_shy()
    else:
        pcm "Idiot."
    jump travel

label random_event_haven_harass_3:
    $ grope_mastleft = True
    $ player.sex_cum(havenman, "ass", main_quest_05)
    $ player.face_worried()
    hav "Ahhhh!"
    $ player.face_angry()
    pc "Ugh, fuck off!"
    $ grope_mastleft = False
    with hpunch
    $ player.face_annoyed()
    pcm "Ugh, dirty fuck!"
    jump travel

label random_event_haven_harass_4:
    $ player.face_worried()
    $ player.sex_forced(havenman)
    $ player.grope_hips()
    pc "Ugh!"
    pc "Piss off..."
    $ player.grope_poke()
    hav "Nnng!"
    $ player.sex_cum(havenman, "pullout", main_quest_05)
    $ player.face_annoyed()
    hav "Ahhhh!"
    $ player.face_angry()
    pc "Ugh, fuck off!"
    $ player.grope_end()
    with hpunch
    $ player.face_annoyed()
    pcm "Ugh, dirty fuck!"
    jump travel

label random_event_haven_ko:
    if not renpy.get_screen("blackout"):
        show screen blackout(100)
        with hpunch
    $ renpy.scene()
    $ pc_strip()
    $ haven_sleep_sex_loop(amount=20)
    hide screen cum_action
    $ bruise.belly = 4
    $ bruise.chest = 4
    $ bruise.face = 4
    $ blood.face = 5
    $ player.eye = 4
    show screen blackout(50) with dissolve
    pc "... Uhhhhhh ..."
    hide screen blackout with dissolve
    $ player.face_meek()
    pc "Uhggghhhh..."
    pcm "What the hell..."
    pcm "Ouch! Fuck! Ahhhh I am sore all over..."
    pcm "That..."
    $ player.face_cry()
    $ player.eye = 3
    pc "*SOB*"
    pc "..."
    pc "*SOB*"
    $ player.eye = 2
    pcm "*Sniff*"
    if loc_cur in (loc_haven_utilities, loc_haven_shower_stall):
        pause 0.5
        $ walk(loc_haven_shower)
        pause 0.5
    $ player.face_cry()
    pc "Ahh so sore."
    $ player.face_puke()
    pc "Ubbb!"
    $ player.face_cry()
    pcm "..."
    if loc_cur in (loc_haven_utilities, loc_haven_shower_stall, loc_haven_shower):
        call haven_shower_dress_call from _call_haven_shower_dress_call_2
    else:
        $ pc_dress_slow()
    pc "Ughhhh I need to lay down. Or a beer might numb this pain."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
