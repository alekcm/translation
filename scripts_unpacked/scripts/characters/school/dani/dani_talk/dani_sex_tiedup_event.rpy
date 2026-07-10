init python:
    def yan_dani_sleeping():
        if t.hour in (23,0,1,2,3,4,5) and dani_here():
            return True
        return False

    def yan_dani_can_event():
        if dani_here() and not yan_dani_sleeping():
            return True
        return False

    def yan_dani_set_from_location():
        if dani_here(dis_school):
            dani.dict["yan_tied_from_location"] = "academy"
        elif dani_here(dis_pub):
            dani.dict["yan_tied_from_location"] = "pub"
        elif dani_here(dis_partyhouse):
            dani.dict["yan_tied_from_location"] = "party"
        elif dani_here(loc_stairwell):
            dani.dict["yan_tied_from_location"] = "outside"
        elif dani_here(loc_bedroom_dani):
            dani.dict["yan_tied_from_location"] = "home"

    def yan_dani_update_image():
        if dani_here() and yan_dani_sleeping():
            renpy.show(random(["sb_onback look_right dani_lay_closed dani_sleep", "sb_onback look_down dani_lay_closed dani_sleep", "sb_onback look_up dani_lay_closed dani_sleep" ]))
        else:
            renpy.show(random(["sb_onback look_right no_dani", "sb_onback look_down no_dani", "sb_onback look_up no_dani" ]))
        
        renpy.with_statement(dissolve)

    def yan_dani_can_escape():
        if sum(["yan_tied_gangbang" in dani.list, "yan_tied_oskar_sex" in dani.list, "yan_tied_strapon_sex" in dani.list]) >= 2 and t.day >= dani.dict["yan_tied_up_start_day"] + 2 and not (dani_here() or dani_here(loc_stairwell)):
            return True
        return False

label dani_bedroom_tiedup_start:
    show sb_onback tied worried look_up
    $ pc_strip(temp=True)
    $ dani.dict["yan_tied_up_start_day"] = t.day
    $ dani.dict["yan_tied_from_location"] = ""
    $ add_to_list(dani.list, "pc_is_tied_up")
    $ player.add_perk(perk_gagged)
    $ dani.hate = True
    $ dani.hate_message = "Fucking crazy bitch tied me up in her flat and did all manner to things to me. I never want to see her face again."
    hide screen blackout with hpunch

    pc "something"
    if dani_here():
        dani.name "Ah, you are awake?"
        pc "Something"
        dani.name "I'm just making sure you can't go around being a little whore like you tend to do."
        dani.name "Safer here with me."
        pc "something"
        dani.name "Don't worry, I'll look after you."
    else:
        pc "something"
        show sb_onback look_right with dissolve
        show sb_onback look_down with dissolve
        show sb_onback look_up with dissolve
        pc "something"
        pcm "What the fuck, why am I tied up?"
        pcm "Did [dani.nname] do this?"
        pcm "Where is she?"
    "I struggle with my bindings for some time."
    "They are pretty tight and it doesn't look like I will be getting out of them any time soon."
    if dani_here():
        dani.name "Don't worry. I will treat you well."
        pc "something"
    else:
        pc "something."
        pcm "I wonder if someone can hear me."
        pcm "Fuck, even if they could, they would probably just come and rape me."
    pcm "I need to get out of these things and try and get away."
    jump dani_bedroom_tiedup_loop_picker




label dani_bedroom_tiedup_loop_picker:
    jump expression WeightedChoice([

    
    ("dani_bedroom_tiedup_struggle_general", If(not dani_here(), 100, 0)),
    ("dani_bedroom_tiedup_struggle_comment", If(not dani_here(), 30, 0)),
    ("dani_bedroom_tiedup_struggle_shout", If(not dani_here(), 50, 0)),

    
    ("dani_bedroom_tiedup_dani_noevent", If(dani_here() and not yan_dani_sleeping(), 50, 0)),
    ("dani_bedroom_tiedup_dani_talk", If(dani_here() and not yan_dani_sleeping(), 100, 0)),
    ("dani_bedroom_tiedup_dani_sleep_loop_picker", If(dani_here() and yan_dani_sleeping(), 100, 0)),
    ("dani_bedroom_tiedup_dani_strapon", If(dani_here() and not yan_dani_sleeping() and dani.lust > 60, 100, 0)),

    
    ("dani_bedroom_tiedup_sleep", If(not dani_here() and player.tired <= 40, 500, 0)),
    ("dani_bedroom_tiedup_sleep_dani", If(dani_here() and player.tired <= 10, 500, 0)),

    
    ("dani_bedroom_tiedup_invite_oskar", If(not oskar.dead and dani_here(loc_stairwell) and not "yan_tied_oskar_sex" in dani.list and t.timeofday == "day", If(t.wkday == "Sunday", 1000, 100), 0)),
    
    ("dani_bedroom_tiedup_invite_pub_arrive", If(dani_here() and dani.dict["yan_tied_from_location"] == "pub" and not "yan_tied_gangbang" in dani.list, 500, 0)),
    ("dani_bedroom_tiedup_invite_academy_arrive", If(dani_here() and dani.dict["yan_tied_from_location"] == "academy" and not "yan_tied_gangbang" in dani.list, 100, 0)),
    ("dani_bedroom_tiedup_invite_courtyard_arrive", If(dani_here(loc_stairwell) and not "yan_tied_gangbang" in dani.list, 20, 0)),

    
    ("dani_bedroom_tiedup_escape", If(yan_dani_can_escape(), 50, 0)),

    ])




label dani_bedroom_tiedup_struggle_general:
    $ yan_dani_set_from_location()
    $ renpy.show(random(["sb_onback look_right", "sb_onback look_down", "sb_onback look_up"]))
    with dissolve
    if dani_here(dis_school):
        "The crazy bitch should be at the academy, so I should have time to get these free."
    elif dani_here(loc_pub):
        "She is working the pub. I had better try and get out of here before she comes home."
    elif dani_here(loc_stairwell):
        "Pretty sure she is just outside, so I had better be careful."
    elif dani_here(dis_partyhouse):
        "The lunatic went to that party, I should have some time before she gets back."
    else:
        "Not sure where that crazy bitch is, she might come home at any moment."
    if numgen():
        show sb_onback angry look_closed
        with hpunch
        "I try to get my bindings loose, pulling at them or trying to twist, but I don't really manage to get much leverage."
        with vpunch
        $ exercise(numgen(20,50))
        show sb_onback worried look_down
        pc "something"
        "After struggling for a bit, I start to feel sore so rest for a bit."
    else:
        "I am tired and not wanting to risk getting caught, so I relax for a bit."
        $ relax(numgen(10,40))
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_struggle_comment:
    $ yan_dani_set_from_location()
    pcm "I must be making some progress with these straps."
    pcm "They can't be that strong..."
    $ relax(numgen(5,30))
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_struggle_shout:
    $ yan_dani_set_from_location()
    pc "somethin"
    pc "something"
    pcm "Come on, someone hear me!"
    pc "somf"
    $ relax(numgen(5,30))
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_sleep:
    $ yan_dani_set_from_location()
    show sb_onback look_closed with dissolve
    "I am exhausted, so I close my eyes for a bit and try and get some sleep."
    jump bed_sleep_loop

label dani_bedroom_tiedup_sleep_dani:
    $ yan_dani_set_from_location()
    "I don't really want to fall asleep with this lunatic around, but I can't keep my eyes open."
    show sb_onback look_closed with dissolve
    jump bed_sleep_loop


label dani_bedroom_tiedup_dani_noevent:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    "With [dani.nname] here, there isn't much I can do to escape, so I just lay here hoping she doesn't do anything weird."
    $ relax(numgen(15,45))
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_dani_talk:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    "With not much I can do since [dani.nname] is here, I am forced to listen to her crazy talk."
    dani.name "[rlist.dani_tied_talk_nonesense]"
    $ relax(numgen(5,30))
    $ renpy.show(random(["sb_onback look_right", "sb_onback look_down", "sb_onback look_up"]))
    "She drones on and I try to block it out."
    dani.name "[rlist.dani_tied_talk_nonesense]"
    $ relax(numgen(5,30))
    pc "oaofa"
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_dani_sleep:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    "With [dani.nname] sleeping next to me, there isn't much I can do to escape so I just lay there bored stiff."
    $ relax(numgen(15,60))
    jump dani_bedroom_tiedup_loop_picker


label dani_bedroom_tiedup_invite_oskar:
    $ add_to_list(dani.list, "yan_tied_oskar_sex")
    show sb_onback look_up with dissolve
    pcm "Fuck, I hear her coming to the window."
    "I watch as [dani.nname] climbs through the window, shortly followed by [oskar.name]."
    pcm "Fuck!!"
    dani.name "I thought I would make use of my dirty little slut."
    pc "smsm"
    dani.name "No need to pay the rent myself when I have a little toy here to do it for me."
    pc "some"
    dani.name "Have fun."
    "I watch as she climbs back out the window and leaves me alone with [oskar.name]."
    pc "soms"
    oskar.name "I knew you girls were into some nasty stuff, but I didn't think this much."
    pc "soso"
    "It's no use, he thinks we are up to some kinky games. I lay here helpless as I watch him undress."
    pc "soms"
    $ npc_race_picker(oskar)
    show sb_onback hump look_down with dissolve
    pc "sooo"
    $ temp_var_1 = oskar.sex
    $ player.sex_vag(oskar)
    show sb_onback look_up
    pc "fpian"
    if temp_var_1:
        oskar.name "If I knew you girls were this dirty, I would have come around and fucked you both a lot more."
        oskar.name "Both of you paying the rent with your body, but I didn't know you enjoyed it this much."
    else:
        oskar.name "Mmm, watching a little slut lik you walking around, I knew it was only a matter of time before I fucked you."
        oskar.name "All you sexy whores eventually offer your arse to pay the rent."
    "I lay there unable to do anything as [oskar.name] fucks me."
    "He is getting off to my helplessness and thinks this is a fun game me and [dani.nname] are playing."
    pc "ododo"
    oskar.name "Don't worry you little whore, I'll make sure to fill you up."
    pc "sosoos"
    oskar.name "Fuck this is nice!"
    oskar.name "Ahhhh fuck!"
    $ player.sex_cum(oskar, "inside")
    oskar.name "Ahhh fuck yes!"
    pc "ofof"
    oskar.name "Mmm, maybe have to come around some more."
    show sb_onback no_sex look_up with dissolve
    "I lay there helpless, with cum leaking out of me and watch [oskar.name] dress up with a smirk on his face."
    "He gives me one last look then heads out the window, leaving me alone."
    pcm "Fucking lunatic [dani.nname]!"
    "With nothing I can do, I just lay here helplessly hoping nothing else crazy happens."
    $ relax(numgen(5,20))
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_invite_pub_arrive:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    pc "foof"
    "I can hear something going on outside the window. It's about time [dani.nname] came home from working the pub."
    "But it sounds like a bunch of men."
    "I see [dani.nname] climb into the window, but followed by a few guys."
    jump dani_bedroom_tiedup_invite_pub

label dani_bedroom_tiedup_invite_academy_arrive:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    pc "foof"
    "I can hear something going on outside the window. It's about time [dani.nname] came home from the academy."
    "But it sounds like a bunch of men."
    "I see [dani.nname] climb into the window, but followed by a few guys."
    jump dani_bedroom_tiedup_invite_pub

label dani_bedroom_tiedup_invite_courtyard_arrive:
    $ yan_dani_set_from_location()
    $ yan_dani_update_image()
    "I know [dani.nname] is outside in the courtyard, but it sounds like she is no longer alone."
    "It's unusual, she usually runs at the first sign of someone trying to talk to her, but she seems to be staying out there."
    "I can't work out what they are saying, so just listen to the distant voices."
    $ relax(10)

    "Eventually the voices get louder. It sounds like they are getting closer, until I see [dani.name] climb into the window."
    "And she isnt alone..."
    jump dani_bedroom_tiedup_invite_courtyard


label dani_bedroom_tiedup_dani_strapon:
    $ dani.dict["strapon_sex"] += 1
    $ add_to_list(dani.list, "yan_tied_strapon_sex")
    dani.name "I think your little whore self needs some fun."
    "[dani.name] gets up and starts putting on her strapon."
    pc "ifif"
    show sb_onback dani_kiss strapon
    with dissolve
    "Without warning, she gets on top of me and starts kissing over my gag."
    dani.name "Mmmm."
    dani.name "You are so sexy."
    dani.name "I think I know what a dirty girl like you needs."
    pc "Oh?"
    dani.name "I'm going to fuck you like the dirty whore you are."
    show sb_onback dani_sex with dissolve
    dani.name "And give you this giant cock you love."
    pc "aaa"
    $ player.sex_vag(dani)
    show sb_onback ah angry
    "Without much warning, she presses it against me and starts sliding it inside me."
    pc "aa"
    dani.name "You dirty fucking whore!"
    "[dani.nname] starts to fuck me, and not at all gentle or pleasurable."
    "She just grabs hold of my thigh and rams the dam thing in and out of me."
    with hpunch
    dani.name "You dirty bitch, you like a big cock like this?"
    "I try to ignore her taunts and hope she get's this over with."
    dani.name "I know a slut like you would enjoy something like this."
    with hpunch
    dani.name "Take it you dirty bitch!"
    "She keeps hammering away until it looks like she is getting tired, and slows her pace."
    dani.name "So much fun fucking you like this."
    show sb_onback look_up
    pc "fafa"
    show sb_onback dani_kiss strapon with dissolve
    dani.name "You dirty girl."
    show sb_onback no_dani with dissolve
    pcm "Thank fuck thats over..."
    "I just lay there for a bit, recovering from what just happened."
    $ relax(numgen(10,30))
    jump dani_bedroom_tiedup_loop_picker


label dani_bedroom_tiedup_escape:
    $ renpy.show(random(["sb_onback look_right", "sb_onback look_down", "sb_onback look_up"]))
    with dissolve
    if dani_here(dis_school):
        "The crazy bitch should be at the academy, so I should have time to get these free."
    elif dani_here(loc_pub):
        "She is working the pub. I had better try and get out of here before she comes home."
    elif dani_here(loc_stairwell):
        "Pretty sure she is just outside, so I had better be careful."
    elif dani_here(dis_partyhouse):
        "The lunatic went to that party, I should have some time before she gets back."
    else:
        "Not sure where that crazy bitch is, she might come home at any moment."

    show sb_onback angry look_closed
    with hpunch
    "I try to get my bindings loose, pulling at them or trying to twist, and to my suprise, one of them just snaps off."
    with vpunch
    pcm "Ah I got it!"
    show sb_onback relaxed look_up with vpunch
    pcm "Fuck finally free!"
    hide sb_onback with hpunch
    "I jump to my feet and get ready to get the fuck out of here."
    $ walk(loc_stairwell)
    pcm "Thank fuck!"
    pc "gngn"
    pcm "Ah, still gagged."
    $ player.remove_perk(perk_gagged)
    $ player.face_angry()
    "I rip the gag off and throw it on the floor."
    if "yan_dani_plugged" in dani.list and "yan_dani_nipped" in dani.list:
        pcm "Still here arse naked with a plug up my arse and these nipple rings..."
    elif "yan_dani_plugged" in dani.list:
        pcm "Still here arse naked with a plug up my arse..."
    elif "yan_dani_nipped" in dani.list:
        pcm "Still here arse naked with these new nipple rings..."
    else:
        pcm "Still standing here arse naked..."
    pcm "Fucking lunatic bitch."
    pcm "I'd better get some clothes."
    $ remove_from_list(dani.list, "pc_is_tied_up")
    $ diary_dani_tiedup = Diary_Class("Lunatic friend", "I knew she was having issues, kinda why I hung around with her a lot. Plus it was fun.\nBut fucking hell the lunatic tied me up while I was asleep. Not even the fun type of tied up but the type where you need to escape alive before you are dead.\nUgh, I am going to have to avoid her from now on I think.\nYeah, best to just stay far, far away.")
    jump travel





label dani_bedroom_tiedup_dani_sleep_loop_picker:

    jump expression WeightedChoice([

    
    ("dani_bedroom_tiedup_dani_sleep_join", If(yan_dani_sleeping() and not renpy.showing("sb_onback dani_lay_closed"), 5000, 0)),
    ("dani_bedroom_tiedup_dani_sleep_loop", If(yan_dani_sleeping() and renpy.showing("sb_onback dani_lay_closed"), 100, 0)),
    ("dani_bedroom_tiedup_dani_sleep_pc_sleep", If(yan_dani_sleeping() and player.tired < 20 and renpy.showing("sb_onback dani_lay_closed"), 100, 0)),
    ("dani_bedroom_tiedup_dani_sleep_wake", If(not yan_dani_sleeping(), 5000, 0)),
    ])

label dani_bedroom_tiedup_dani_sleep_join:
    dani.name "I am sleepy..."
    dani.name "I get to lay next to my little pet."
    show sb_onback dani_lay_closed dani_neutral look_right with dissolve
    "[dani.nname] climbs into bed and tried to snuggle up to me. Made a bit difficult by the straps tying me up."
    dani.name "Goodnight my princess."
    pc "dodo"
    show sb_onback dani_lay_closed dani_sleep with dissolve
    "I lay there for a while making sure she is asleep. But looks like she passed out pretty quickly."
    jump dani_bedroom_tiedup_dani_sleep_loop_picker

label dani_bedroom_tiedup_dani_sleep_loop:
    $ yan_dani_update_image()
    show sb_onback dani_lay_closed
    $ relax(numgen(15,40))
    jump dani_bedroom_tiedup_dani_sleep_loop_picker

label dani_bedroom_tiedup_dani_sleep_pc_sleep:
    "Despite [dani.nname] being right next to me, I risk getting some sleep myself."
    show sb_onback look_closed dani_lay_closed with dissolve
    jump dani_bedroom_tiedup_sleep_loop_picker

label dani_bedroom_tiedup_dani_sleep_wake:
    show sb_onback dani_neutral look_right with dissolve
    dani.name "*YAAAWN*"
    dani.name "Good morning sweetheart."
    pc "fmmf"
    dani.name "So nice I can wake to you evey morning."
    pc "ofof"
    show sb_onback no_dani with dissolve
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_sleep_loop_picker:

    jump expression WeightedChoice([

    
    ("dani_bedroom_tiedup_sleep_cont", If(not dani_here() and player.tired <= 30, 100, 0)),
    
    
    ("dani_bedroom_tiedup_sleep_wake", If(not dani_here() and player.tired > 50, 100, 0)),
    ("dani_bedroom_tiedup_sleep_daniwake", If(yan_dani_can_event(), 100, 0)),
    ("dani_bedroom_tiedup_sleep_daniwake_pub", If(dani_here() and dani.dict["yan_tied_from_location"] == "pub" and not "yan_tied_gangbang" in dani.list, 900, 0)),
    ("dani_bedroom_tiedup_sleep_daniwake_academy", If(dani_here() and dani.dict["yan_tied_from_location"] == "academy" and not "yan_tied_gangbang" in dani.list, 300, 0)),
    ("dani_bedroom_tiedup_sleep_daniwake_courtyard", If(dani_here(loc_stairwell)  and not "yan_tied_gangbang" in dani.list, 20, 0)),

    
    ("dani_bedroom_tiedup_sleep_plug", If(yan_dani_can_event() and not acc.anus, 20, 0)),
    ("dani_bedroom_tiedup_sleep_nips", If(yan_dani_can_event() and not acc.nipring, 20, 0)),

    ])

label dani_bedroom_tiedup_sleep_cont:
    jump bed_sleep_loop

label dani_bedroom_tiedup_sleep_wake:
    $ yan_dani_set_from_location()
    hide screen blackout with hpunch
    show sb_onback look_right with dissolve
    show sb_onback look_down with dissolve
    show sb_onback look_up with dissolve
    pcm "Fuck, still here..."
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_sleep_daniwake:
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    dani.name "Wake up you dirty bitch!"
    pc "fgiig"
    jump dani_bedroom_tiedup_loop_picker


label dani_bedroom_tiedup_sleep_plug:
    $ yan_dani_set_from_location()
    $ add_to_list(dani.list, "yan_dani_plugged")
    $ acc.anus = 1
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    pc "something"
    pcm "Something in my ass!?"
    dani.name "I thought I would give you something to have fun with."
    pc "something."
    pcm "Crazy bitch!"
    jump dani_bedroom_tiedup_loop_picker

label dani_bedroom_tiedup_sleep_nips:
    $ yan_dani_set_from_location()
    $ add_to_list(dani.list, "yan_dani_nipped")
    $ acc.nipring = 1
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    pc "something"
    show sb_onback look_down with dissolve
    "What did she do to my nipples??"
    dani.name "I thought I would give you something to have fun with."
    pc "something."
    pcm "Crazy bitch!"
    jump dani_bedroom_tiedup_loop_picker


label dani_bedroom_tiedup_sleep_daniwake_pub:
    $ yan_dani_set_from_location()
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    dani.name "Wake up you dirty slut!"
    pc "soemthing"
    "I look around and [dani.nname] is not alone, It looks like she brought back some drunks from the pub."
    pc "ododfo"
    pcm "Fuck..."
    jump dani_bedroom_tiedup_invite_pub

label dani_bedroom_tiedup_sleep_daniwake_academy:
    $ yan_dani_set_from_location()
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    dani.name "Wake up you dirty slut!"
    pc "soemthing"
    "I look around and [dani.nname] is not alone, It looks like she brought back some guys from the academy."
    pc "ododfo"
    pcm "Fuck..."
    jump dani_bedroom_tiedup_invite_academy

label dani_bedroom_tiedup_sleep_daniwake_courtyard:
    $ yan_dani_set_from_location()
    hide screen blackout with hpunch
    show sb_onback look_up with dissolve
    dani.name "Wake up you dirty slut!"
    pc "soemthing"
    "I look around and [dani.nname] is not alone, It looks like she brought back some random guys."
    pc "ododfo"
    pcm "Fuck..."
    jump dani_bedroom_tiedup_invite_courtyard



label dani_bedroom_tiedup_invite_pub:
    dani.name "See, I have a little pet you can have fun with."
    pubpatron.name "Oh looks like you do."
    dani.name "She has been naughty so I am teaching her to behave."
    pubpatron.name "Nothing wrong with being a little naughty."
    dani.name "Well, this one is too much. But have fun."
    "I watch as [dani.nname] goes into the corner to sit down, leaving me at the mercy of these drunk perverts."
    pc "jhfjjf"
    pubpatron.name "Don't worry darling, we will give you a good time."
    "One of the guys starts stripping his clothes and comes over to me."
    $ npc_race_picker()
    $ tiedman_dani._fname = "Drunk from the pub"
    $ tiedman2_dani._fname = "Drunkard"
    $ tiedman3_dani._fname = "Pub guy"
    $ tempname = tiedman_dani
    $ tempname2 = tiedman2_dani
    $ tempname3 = tiedman3_dani
    $ quest_temp = None
    $ player.sex_forced(dani)
    jump dani_bedroom_tiedup_invite_gangback_start


label dani_bedroom_tiedup_invite_academy:
    dani.name "See, [name] is my little pet."
    "Guy in uniform" "Oh shit, she is."
    dani.name "She has been naughty so I am teaching her to behave."
    "Guy in uniform" "Nothing wrong with being a little naughty."
    dani.name "Well, this one is too much. But have fun."
    "I watch as [dani.nname] goes into the corner to sit down, leaving me at the mercy of the guys from the academy."
    pc "jhfjjf"
    "Guy in uniform" "Don't worry [name], we will give you a good time."
    "One of the guys starts stripping his clothes and comes over to me."
    $ npc_race_picker()
    $ tiedman_dani._fname = "Academy guy"
    $ tiedman2_dani._fname = "Guy in unifrom"
    $ tiedman3_dani._fname = "School guy"
    $ tempname = tiedman_dani
    $ tempname2 = tiedman2_dani
    $ tempname3 = tiedman3_dani
    $ quest_temp = None
    $ player.sex_forced(dani)
    jump dani_bedroom_tiedup_invite_gangback_start

label dani_bedroom_tiedup_invite_courtyard:
    dani.name "See, told you I have a little pet."
    "Scruffy guy" "Oh, looks like you do."
    dani.name "She has been naughty so I am teaching her to behave."
    "Scruffy guy" "Nothing wrong with being a little naughty."
    dani.name "Well, this one is too much. But have fun."
    "I watch as [dani.nname] goes into the corner to sit down, leaving me at the mercy of the guys she just met."
    pc "jhfjjf"
    "Scruffy guy" "Don't worry you little whore, we will give you a good time."
    "One of the guys starts stripping his clothes and comes over to me."
    $ npc_race_picker()
    $ tiedman_dani._fname = "Academy guy"
    $ tiedman2_dani._fname = "Guy in unifrom"
    $ tiedman3_dani._fname = "School guy"
    $ tempname = tiedman_dani
    $ tempname2 = tiedman2_dani
    $ tempname3 = tiedman3_dani
    $ quest_temp = None
    $ player.sex_forced(dani)
    jump dani_bedroom_tiedup_invite_gangback_start





label dani_bedroom_tiedup_invite_gangback_start:
    $ add_to_list(dani.list, "yan_tied_gangbang")
    show sb_onback missionary with dissolve
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ player.sex_vag(tempname, quest_temp)
    "[rlist.having_sex_action_onback]"
    "[rlist.having_sex_action_onback]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "daad"
    show sb_onback man_right look_right with dissolve
    "One of the guys comes up to me while wanking."
    pcm "Fuck."
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    show sb_onback look_down
    $ player.sex_cum(tempname, "belly", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_onback no_sex with dissolve
    dani.name "Hey, why did you do that? Fill my little pet up."
    dani.name "She should be leaking half of [town] once you are all finished."
    tempname2.name "Don't worry, thats what I plan to do."
    $ npc_race_picker_1()
    "Another one of the drunks comes over and gets between my legs."
    pc "ifif"
    show sb_onback missionary look_up with dissolve
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    $ player.sex_vag(tempname, quest_temp)
    pc "ofofo"
    show sb_onback look_right
    "The guy wanking over me suddenly starts to groan, and it's not long before..."
    $ player.sex_cum(tempname, "face", quest_temp)
    show sb_onback look_closed
    tempname2.name "[rlist.handjob_man_cum_yes_dialogue]"
    pc "aaa"
    show sb_onback no_man_right look_right with dissolve
    with hpunch
    pc "ofof"
    show sb_onback look_up
    "With not much I can do, I just lay there getting fucked by the last guy."
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pc "ogfogfo"
    tempname.name "Ahh yes."
    show sb_onback no_sex with dissolve
    pc "foog"
    "With the guys finished, they hang around drinking the rest of the ber they brought with them and chatting away to [dani.nname]."
    "With no choice but to lay there, thats what I do."
    $ relax(numgen(15,40))
    "Eventually they finish up their beers, and head out the window."
    dani.name "Buy guys, hope you had fun."
    dani.name "..."
    dani.name "There, now you can't say I dont do anything nice for you."
    jump dani_bedroom_tiedup_loop_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
