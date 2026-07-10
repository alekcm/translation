





label random_event_generic_desirenocontrol:
    jump expression WeightedChoice([
    ("random_event_generic_desirenocontrol_1", If(inv.qty(item_bdsm), 100, 0)),
    ("random_event_generic_desirenocontrol_2", 100),
    ("random_event_generic_desirenocontrol_3", If(player.has_perk(perk_lebo), 200, 0)),
    ("random_event_generic_desirenocontrol_4", 100),
    ])

label random_event_generic_desirenocontrol_1:
    pc "..."
    pcm "Right, that's enough! I'm going to have some fun."
    $ travel_sleep_location()
    pcm "Hmm, over there..."
    $ travel_isolate()
    pcm "This should do."
    $ pc_striptease()
    $ pc_set_temp_outfit()
    pc "..."
    pcm "I'll make use of these I think."
    "I take some of the bindings I have out and start attaching them to myself."
    show sb_doggy1 body_tied with dissolve
    pcm "And now I wait..."
    jump random_event_generic_freeuse_tied_start

label random_event_generic_desirenocontrol_2:
    $ tempname = streetguy
    $ male_npc_create()
    pc "..."
    pcm "Right, that's enough! I'm going to have some fun."
    $ travel_sleep_location()
    pcm "Hmm, over there..."
    $ travel_isolate()
    pcm "This should do."
    "I stand around looking at the odd man that passes by. Most just look at me strangely, until eventually..."
    show male_generic at right1 with dissolve
    man "What you up to 'ere love?"
    pc "Waiting for someone to come and entertain me."
    man "Oh? You one 'o dem girls?"
    pc "If you mean the type to let a stranger take her somewhere and fuck her silly, then yes. I am one 'o dem girls."
    man "Right... Okay then."
    pc "Interested?"
    man "Sure I am!"
    jump whore_street_sex_start_picker

label random_event_generic_desirenocontrol_3:
    pcm "Fuck, this lebo is making me so hot!"
    pcm "Right, that's enough! I'm going to have some fun."
    $ travel_whore_location()
    jump flirt_street_start

label random_event_generic_desirenocontrol_4:
    pcm "Fuck, I am so, so fucking hot!"
    pcm "..."
    $ travel_whore_location()
    pcm "Hmmm... There is a group over there..."
    $ male_npc_create_all()
    show male_generic at right1
    show male2_generic at right2
    show male3_generic at right3
    with dissolve
    $ tempname = streetguy
    $ tempname2 = streetman
    $ tempname2 = streetpervert
    $ quest_temp = None
    pc "Hey guys."
    tempname.name "What we got 'ere?"
    pc "Someone looking to let off a bit of steam."
    tempname2.name "Oh? Want us to help with that?"
    pc "That's why I am here. ♥"
    $ player.sex_man_amount = numgen(3,8)
    $ renpy.scene()
    $ walk(loc_cur.isolate_loc)
    "I walk away, looking back at them to make sure they are following."
    call whore_street_sex_strip_full_call from _call_whore_street_sex_strip_full_call
    pc "Maybe we should do something a bit more?"
    pc "But you guys are looking a bit over dressed ♥"
    jump whore_street_sex_group_start_picker

label random_event_generic_freeuse_tied_start:
    $ tempname = guy_tiedtrain
    $ quest_temp = None
    $ relax(5)
    if renpy.showing("sb_doggy1"):
        "I spend some time laying here with my ass in the air until finally I hear people talking. Seems someone has noticed me."

    if renpy.showing("sb_doggy1"):
        "He seems a bit confused about what is going on, but a little wiggle of my bum seems to set him at ease."


    if player.gagged:
        pc "Something."
        tempname.name "What we got 'ere then?"
        pc "Something."
        tempname.name "Don't mind if I do."
        jump random_event_generic_freeuse_tied_sex_first
    else:
        pc "Oh no... I seem to have gotten myself all tied up, whatever will I do?"
        tempname.name "Oh?"
        pc "Please don't do terrible things to my naked body."
        if not numgen(0,10):

            if renpy.showing("sb_doggy1"):
                pc "I hope you aren't one of those types of guys who would take advantage of a naked girl all tied up with her ass out in the open ready to be taken."

            if renpy.showing("sb_upsidedown") or renpy.showing("sb_doggy1"):
                pc "I'm sure you won't give me a spanking until my arse is purple."

            pc "Or stick your hard, throbbing cock inside me and fuck the shit out of me until you fill me with cum."
            pc "Or..."
            tempname.name "Yeah yeah, I get it."
        else:
            tempname.name "Who me? Noooo. I'll untie you. But my clothes will get in the way so gimme a sec to undress."
            pc "Ah good."
        jump random_event_generic_freeuse_tied_sex_first

label random_event_generic_freeuse_tied_start_unknown:
    $ tempname = guy_tiedtrain
    $ quest_temp = None
    $ relax(5)
    "I'm not quite sure how long I end up laying here, but eventually I hear voices and it seems someone has noticed me."
    if player.blind:
        "I can't see what they are doing or who they are, but I can hear them walking close to me."
    else:
        if renpy.showing("sb_doggy1"):
            "I can't really see the guy since my face is in the floor and he is behind me, but I hear him come close to me."
    if player.gagged:
        pc "Something."
        tempname.name "What we got 'ere then?"
        pc "Something."
        tempname.name "Don't mind if I do."
        jump random_event_generic_freeuse_tied_sex_first
    else:
        pc "Err, I am kinda stuck. Can you untie me?"
        tempname.name "Yeah right. Probably did it to yourself."
        pc "Why would I do that?"
        tempname.name "Dunno, you girls round 'eye are up to some freaky shit."
        pc "No, I ended up like this. Wasn't me who did it."
        tempname.name "..."
        pc "So... gonna untie me?"
        tempname.name "Hmm, No. I think I will have some fun with you."
        pc "Ugh..."
        jump random_event_generic_freeuse_tied_sex_first

label random_event_generic_freeuse_tied_sex_first:


    if player.blind:
        "I hear the guy doing something, sounds like he might be undressing."
    else:
        "The guy looks around a bit before starting to take his clothes off."
    tempname.name "Nice to have a little fun now an' then."
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut], notif=True):
        pc "Planning to do something naughty are you?"
    else:
        pc "Please, untie me."
        tempname.name "Maybe after I have had some fun."
        pc "What?"
        tempname.name "You dirty sluts like to play a naughty game."
    $ if_showing("sb_doggy1", "poke")
    tempname.name "Mmmm. Dirty little whore."
    $ if_showing("sb_doggy1", "vag")
    $ player.sex_vag(tempname, quest_temp)
    pc "Nnng!"
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        if renpy.showing("sb_doggy1"):
            "I end up with my face on the floor as the guy takes me from behind."
        "I should probably pretend to put up a fight, but in reality I don't really care and try to enjoy myself."
    else:
        "The guy ignores my pleading to untie me. My only hope is that once he is done he might take pity on me."
        "So in the end I just save my energy and let him do as he wants."
    $ player.sex_cum(tempname, "inside", quest_temp)
    tempname.name "Ahhh fuck yes!"
    pc "..."
    tempname.name "Haaa... Lovely little slut."
    $ if_showing("sb_doggy1", "poke")
    $ if_showing("sb_doggy1", "noman")

    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        pc "..."
        "The guy dresses up and quickly leaves, leaving the door open as he does."
        pcm "Wonder how many guys it's going to take before someone actually let's me go?"
        pcm "A lot probably..."
    else:
        pc "Gonna untie me now you have had your fun?"
        tempname.name "What? Of course not. I'm sure you can fit more cum inside you and there are plenty of men who will put it there."
        pc "Arse!"
        "The guy just dresses up and walks away. But I overhear him telling some other people that I am here."
        pcm "Fuck, most of these cunts are going to be like this..."
        "Resigned to my fate, I just close my eyes and hope that one of the people who enter will take pity on me."

    $ temp_var_1 = 0
    $ temp_var_2 = False
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_loop:
    $ temp_var_1 += 1
    $ relax(numgen(5,20))
    if player.tired <= 15:
        jump random_event_generic_freeuse_tied_sex_sleep
    elif temp_var_1 >= 15:
        "At some point I lose count of how many men have fucked me. I am tired and it is all becoming a blur..."
        show screen blackout(50) with dissolve
        pcm "How many more will it be?"
        show screen blackout(100) with dissolve
        jump random_event_generic_freeuse_tied_sex_instant
    elif temp_var_1 >= 7:
        if not temp_var_2:
            $ temp_var_2 = True
            if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
                "I start to really relax back and let the guys fuck me without even pretending to want to be released."
                "No doubt eventually someone will take pity on me, until then though I will just enjoy myself."
            else:
                "At this point I don't even bother to beg to be released. I just lay back and prepare to take it."
                "I have no idea how many cocks will fuck me until I am released. But at some point someone will surely help me out."
                "So I just tune out all the fucking and wait for that moment."
            jump random_event_generic_freeuse_tied_sex_quickloop
    if player.has_perk([perk_freeuse, perk_sucu, perk_slut]):
        "Another guy enters after some time. I make a token effort to pretend I want to be released and as expected he ignores me."
        "So again I end up taking another cock in me..."
    else:
        "Another guy enters and I try and plead with him to let me go. But of course he ignores me."
        "After he gets naked I no longer even bother to beg him."

    if not player.gagged and numgen():
        pcm "Huh, what is he doing?"
        if numgen():
            $ inv.take(item_ballgag)
            $ player.add_perk(perk_gagged)
        else:
            $ inv.take(item_ballgag_locked)
            $ player.add_perk(perk_gagged_locked)
        pc "Something"
    elif not player.blind and numgen():
        pc "No, don't put that on!"
        $ inv.take(item_blindfold)
        $ player.add_perk(perk_blind)
        pcm "Ugh..."

    jump expression WeightedChoice([
    ("random_event_generic_freeuse_tied_sex_loop_vag", 100),
    ("random_event_generic_freeuse_tied_sex_loop_anal", If(not acc.anus, 50, 0)), 
    ("random_event_generic_freeuse_tied_sex_loop_blow", If(not (player.gagged or renpy.showing("sb_doggy1")), 50, 0)),
    ("random_event_generic_freeuse_tied_sex_loop_wank", If(renpy.showing("sb_onback"), 50, 0)), 
    ("random_event_generic_freeuse_tied_sex_loop_buk", If(renpy.showing("sb_onback"), 50, 0)),
    ])

label random_event_generic_freeuse_tied_sex_loop_vag:
    $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
    "The guy climbs on me and I feel him lining his cock up with my pussy."
    $ player.sex_vag(tempname, quest_temp)
    $ if_showing("sb_upsidedown", "vag", "sb_doggy1", "vag")
    "Nothing I can do about it but take it in me."
    "He keeps fucking me while saying some stuff. But I just tune it out. He isn't going to untie me so I don't much care what he has to say."
    "I just have to accept his cock pushing in and out of me and the guy taking what fun he wants."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pc "..."
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    "He dismounts and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_loop_anal:
    $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
    "The guy climbs on me and I feel him lining his cock up with my arsehole."
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_upsidedown", "ass", "sb_doggy1", "anal")
    "His cock invades my arse and I can do nothing but accept it inside me."
    "He fucks and spanks me while saying some dirty words. But I mostly tune it all out"
    "I just have to accept his cock fucking my arsehole and hope he finished somewhat soon."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "anal", quest_temp)
    pc "..."
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    "He dismounts and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_loop_blow:
    "The guy aims his cock closer to my face. I guess this time round I will be getting fucked in the face."
    $ if_showing("sb_upsidedown", "blow closed", "sb_onback", "facefuck")
    $ player.sex_oral(tempname, quest_temp)
    "He rides my face, using my mouth as just a hole to fuck."
    $ if_showing("sb_upsidedown", "blowdeep", "sb_onback", "facefuck_deep")
    "But that of course it not enough. He has to fuck my throat as well. Making it tough for me to breathe."
    "I just manage to suck in some air through my nose when he pulls out a bit and hope he hurries up."
    tempname.name "Ahhhyes!"
    $ player.sex_cum(tempname, "mouth", quest_temp)
    "I feel him coming down my throat and try my best not to choke on it."
    $ if_showing("sb_upsidedown", "blow closed", "sb_onback", "facefuck")
    $ if_showing("sb_upsidedown", "no_sex", "sb_onback", "no_sex")
    "Eventually he leaves, leaving the door open for someone else."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_loop_wank:
    $ if_showing("sb_onback", If(numgen(), "man_left", "man_right"))
    "The guy climbs onto the bed and starts wanking off."
    "One of the few guys who cont actually try and put anything inside me, but his furious wanking and hands roving over my body let me know he's enjoying himself."
    "It's not long before his cock sounds a lot wetter and I can feel the odd drip from his cock."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "face", quest_temp)
    pc "..."
    $ if_showing("sb_onback", "no_man_left no_man_right")
    "He gets off the bed and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_loop_buk:
    $ if_showing("sb_onback", If(numgen(), "man_left", "man_right"))
    "The guy climbs onto the bed and starts wanking off. But it sounds like someone else is also in the room."
    "I realise I am right when I feel some weight on the other side of the bed."
    $ if_showing("sb_onback", "man_left man_right")
    "I hear them both wanking from each ear, neither say anything but both their hands are groping everywhere they can while the other hand works their cock."
    tempname.name "Ahhhhh!"
    $ player.sex_cum(tempname, "face", quest_temp)
    tempname2.name "Yes dirty bitch!"
    $ player.sex_cum(tempname2, "chest", quest_temp)
    "Cum from both sides hit my body and once they are done, they head off to leave."
    $ if_showing("sb_onback", "no_man_left no_man_right")
    "He gets off the bed and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_quickloop:
    if not numgen(0,10):
        jump random_event_generic_freeuse_tied_rescue
    elif numgen(0,4) and not acc.anus:
        $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
        pcm "My arse this time is it?"
        $ player.sex_anal(tempname, quest_temp)
        $ if_showing("sb_upsidedown", "ass", "sb_doggy1", "anal")
        "I lay back and get my ass fucked, waiting for him to cum..."
        tempname.name "Ahhhhh!"
        $ player.sex_cum(tempname, "anal", quest_temp)
        $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
        $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
        "He dismounts and heads out the door, of course leaving it open for someone else to join."
    else:
        $ if_showing("sb_upsidedown", "poke closed pout", "sb_onback", If(numgen(), "look_closed pout hump", "look_closed pout missionary"), "sb_doggy1", "poke")
        "He lines up his cock with my pussy."
        $ player.sex_vag(tempname, quest_temp)
        $ if_showing("sb_upsidedown", "vag", "sb_doggy1", "vag")
        "And I just lay there and take it."
        tempname.name "Ahhhhh!"
        $ player.sex_cum(tempname, "inside", quest_temp)
        $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
        $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
        "He dismounts and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop

label random_event_generic_freeuse_tied_sex_instant:
    $ relax(numgen(5,20))
    if not numgen(0,20):
        pause 0.5
        $ player.cheat_bukake()
        $ player.cheat_bukake()
        $ player.sex_hideaction()
        hide screen blackout with dissolve
        jump random_event_generic_freeuse_tied_rescue
    elif not numgen(0,4) and not acc.anus:
        $ player.sex_anal(tempname, quest_temp)
        $ player.sex_cum(tempname, "anal", quest_temp)
    else:
        $ player.sex_vag(tempname, quest_temp)
        if numgen(0, 4):
            $ player.sex_cum(tempname, "inside", quest_temp)
        else:
            $ player.sex_cum(tempname, "pullout", quest_temp)
    jump random_event_generic_freeuse_tied_sex_instant





label random_event_generic_freeuse_tied_sex_sleep:
    "I am totally exhausted and can barely even keep my eyes open despite the position I am in."
    show screen blackout(50) with dissolve
    "I start to fade out, despite knowing how much of a bad idea it is."
    show screen blackout(100) with dissolve
    jump random_event_generic_freeuse_tied_sex_sleep_loop

label random_event_generic_freeuse_tied_sex_sleep_loop:
    $ pinkroom_customer_event_train_sex_sleep_loop_function()
    $ time_sleep_hour()
    if player.tired >= 20 and not numgen(0, 4):
        jump random_event_generic_freeuse_tied_sex_sleep_wake
    else:
        jump random_event_generic_freeuse_tied_sex_sleep_loop

label random_event_generic_freeuse_tied_sex_sleep_wake:
    $ player.sex_hideaction()
    $ if_showing("sb_upsidedown", "vag up shock", "sb_doggy1", "vag", "sb_onback", "hump worried look_up ah", trans=None)
    hide screen blackout with hpunch
    "I wake with a start and look around to see where I am..."
    pcm "Ah, yeah... I am tied up..."
    "It's not the least shocking to be woke up to a guy fucking me."
    pcm "Haven't been rescued yet, so I guess more waiting..."
    $ if_showing("sb_upsidedown", "closed", "sb_onback", "look_closed")
    $ player.sex_cum(tempname, "inside", quest_temp)
    $ if_showing("sb_upsidedown", "poke", "sb_doggy1", "poke", "sb_onback", "no_sex")
    $ if_showing("sb_upsidedown", "noman", "sb_doggy1", "noman")
    "He dismounts and heads out the door, of course leaving it open for someone else to join."
    jump random_event_generic_freeuse_tied_sex_loop





label random_event_generic_freeuse_tied_rescue:
    "I notice that my hands feel a bit looser than they were before."
    pcm "Did someone loosen them for me or did they just come loose after time?"
    pcm "Doesn't matter I guess."
    "I manage to fumble with the straps and get the rest of them off, then get myself upright."
    $ renpy.scene()
    with dissolve
    if player.has_perk(perk_sucu, notif=True):
        pcm "Not gonna sleep for a week now though."
        pcm "Worth it..."
    elif player.has_perk(perk_broken, notif=True):
        pcm "..."
        pcm "Was nice to be used again..."
    elif player.has_perk(perk_freeuse, notif=True):
        pcm "Since I am not dead though, that was well worth it."
        pcm "Can't get any more free use than tied up and fucked by so many strangers."
    else:
        pcm "Fucking hell. That was terrible!"
    pc "..."


    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
