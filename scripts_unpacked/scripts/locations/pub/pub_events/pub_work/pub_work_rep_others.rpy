label pub_waitress_work_dani_first_talk:
    show dani happy at right1 with dissolve
    $ add_to_list(dani.list, "pub_first_talk")
    dani.name "Hey [name]!"
    if dani.dict["pub_started_working"] == t.day:
        pc "Oh hey [dani.nname]. Your first day?"
        dani.name "Yeah."
    else:
        pc "Oh hey [dani.nname]. Good to see you are still here after your first day."
        dani.name "Yeah, it's not so bad and need the money."
    pc "Well, good luck out there. Don't kick too many drunks."
    dani.name "Ha! I will try not to."
    hide dani with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_others_picker:
    $ rand_choice = WeightedChoice([
    
    
    ("pub_waitress_work_dani_first_talk", If (dani_here(loc_pub) and not "pub_first_talk" in dani.list, 10000,0)),
    ("pub_waitress_work_dani_1", If (dani_here(loc_pub) and (dani.dict["pub_started_working"] + 10) < t.day, 100,0)),
    ("pub_waitress_work_dani_2", If (dani_here(loc_pub), 100,0)),
    ("pub_waitress_work_dani_3", If (dani_here(loc_pub), 100,0)),
    ("pub_waitress_work_dani_4", If (dani_here(loc_pub), 100,0)),
    ("pub_waitress_work_dani_5", If (dani_here(loc_pub), 100,0)),
    ("pub_waitress_work_dani_6", If (dani_here(loc_pub) and (dani.iswhore or (dani.dict["pub_started_working"] + 10) > t.day), 100,0)),

    
    ("pub_waitress_work_trixie_1", 100),
    ("pub_waitress_work_trixie_2", 100),
    ("pub_waitress_work_trixie_3", If (loc_pub_toilet_girls.has_gloryhole, 100,0)),
    ("pub_waitress_work_trixie_4", 100),
    ("pub_waitress_work_trixie_5", 100),
    ("pub_waitress_work_trixie_6", 100),
    ("pub_waitress_work_trixie_7", 100),
    ("pub_waitress_work_trixie_8", 100),

    
    ("pub_waitress_work_robin_meet", If (robin_here(loc_pub) and not "met_pub" in robin.list, 10000,0)),

    ("pub_waitress_work_robin_1", If (robin_here(loc_pub) and "met_pub" in robin.list, 100, 0)),
    ("pub_waitress_work_robin_2", If (robin_here(loc_pub) and "met_pub" in robin.list and not c.pants, 100, 0)),
    ("pub_waitress_work_robin_3", If (robin_here(loc_pub) and "met_pub" in robin.list and player.cum_locations["cum_face"], 100, 0)),
    ("pub_waitress_work_robin_4", If (robin_here(loc_pub) and "met_pub" in robin.list and (player.cum_locations["cum_vagin"] or player.cum_locations["cum_assin"]), 100, 0)),
    ("pub_waitress_work_robin_5", If (robin_here(loc_pub) and "met_pub" in robin.list and player.cum_locations["cum_mouth"], 100, 0)),
    ("pub_waitress_work_robin_6", If (robin_here(loc_pub) and "met_pub" in robin.list and player.has_perk(perk_inseminated), 100, 0)),


    ])
    jump expression rand_choice

label pub_waitress_work_dani_1:
    show dani_pub_talk at right2 with dissolve
    if not dani.hate:
        pcm "Hmm, looks like [dani.name] is getting along okay with the patrons."
        pcm "Maybe she will stick around working here."
    else:
        pcm "Look at the cunt whore..."
    jump pub_waitress_work_others_end

label pub_waitress_work_dani_2:
    show dani_pub_talk at right2 with dissolve
    if not dani.hate:
        pcm "[dani.name] seems to be popular."
        pcm "Good for her, earn some money without going home all depressed wondering how to pay [oskar.name]."
    else:
        pcm "Bitch, chatting away with these guys. Choke on a dick!"
    jump pub_waitress_work_others_end

label pub_waitress_work_dani_3:
    show dani_pub_talk at right2 with dissolve
    if not dani.hate:
        pcm "Heh. She's enjoying the flirting?"
    else:
        pcm "Ugh, fucking lunatic."
    jump pub_waitress_work_others_end

label pub_waitress_work_dani_4:
    show dani_pub_walk at right2 with dissolve
    if not dani.hate:
        pcm "Heh. She is teasing the men like this."
        pcm "Well, more tips so why not?"
    else:
        pcm "They better be careful with that lunatic."
    jump pub_waitress_work_others_end

label pub_waitress_work_dani_5:
    show dani_pub_walk at right2 with dissolve
    if not dani.hate:
        pcm "Is she lifting the back of her skirt on purpose?"
    else:
        pcm "Bitch, showing her ass off like that."
    jump pub_waitress_work_others_end

label pub_waitress_work_dani_6:
    show dani_pub_grope at right2 with dissolve
    if not dani.hate:
        pcm "Oooh? Making new friends are you?"
        pcm "Make sure to get paid."
    else:
        pcm "Hope they rape you in an alleyway."
    jump pub_waitress_work_others_end




label pub_waitress_work_trixie_1:
    show trixie_pub_finger at right2 with dissolve
    pcm "She really does know how to wrap these guys around her finger."
    pcm "How does she manage to look like she does but also come across as all sweet?"
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_2:
    show trixie_pub_finger at right2 with dissolve
    pcm "She's got them all drooling."
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_3:
    show trixie_pub_finger at right2 with dissolve
    patron "So is it your lips on the other side of that hole?"
    trixie.name "Hole? Haven't a clue what you mean hon."
    patron "Yeah right."
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_4:
    show trixie_pub_pose at right2 with dissolve
    trixie.name "Hey guys. Was it beers or some company you wanted?"
    pcm "Wow. So forward..."
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_5:
    show trixie_pub_pose at right2 with dissolve
    trixie.name "Phew. This is getting tiring. Anyone want to help me take a break and relax?"
    pcm "Oh wow!"
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_6:
    show trixie_pub_mast at right2 with dissolve
    pcm "Err. I think I shouldn't be seeing this..."
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_7:
    show trixie_pub_mast at right2 with dissolve
    trixie.name "...in your wallet and we can go somewhere alone."
    patron "Ahh. Yeah! Haaa!"
    trixie.name "C'mon."
    jump pub_waitress_work_others_end

label pub_waitress_work_trixie_8:
    show trixie_pub_lapsit at right2 with dissolve
    pcm "Oooh, someone is getting a good service."
    jump pub_waitress_work_others_end




label pub_waitress_work_robin_meet:
    show robin at right1 with dissolve
    $ add_to_list(robin.list, "met_pub")
    pc "Ah, hey [robin.name]. Finally came?"
    robin.name "Yeah. Thought I would pop by and see how things go."
    pc "Well, don't get your hopes up. I still have to work here."
    robin.name "Sure. Whatever."
    pc "Heh, better be careful yourself. I can see the people looking at you."
    robin.name "Yeah. They aren't even being discreet."
    if "robin_talk_sexobject_last_outing" in robin.dict and robin.dict["robin_talk_sexobject_last_outing"] > 0:
        pc "Don't even need to dress you up like a whore for people to want to drag you in an alleyway."
        robin.name "More fun if I am though."
        pc "Why aren't you all dressed up?"
        robin.name "Alone? Too scary. I'll wait until you want some fun as well."
    pc "Ok, well have fun watching. I'll get back to it."
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_1:
    show robin at right1 with dissolve
    pc "Having fun with the perverts?"
    robin.name "Ha, sure. Get back to showing your ass off."
    pc "Don't look at it too hard."
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_2:
    show robin at right1 with dissolve
    pc "I'm not wearing any underwear."
    robin.name "Oh? You dirty pervert."
    if player.has_perk(perk_buttplug):
        pc "Also have a plug in my ass."
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_3:
    show robin at right1 with dissolve
    pc "Hey."
    robin.name "Oh wow, you have..."
    pc "Cum on my face."
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_4:
    show robin at right1 with dissolve
    pc "Hey, wanna know something?"
    robin.name "Sure."
    pc "I have cum leaking out of me."
    robin.name "Slut!"
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_5:
    show robin at right1 with dissolve
    pc "Hey, wanna know something?"
    robin.name "Sure."
    pc "I can still taste the guy who came in my mouth."
    robin.name "Slut!"
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_robin_6:
    show robin at right1 with dissolve
    pc "So, right now I have cum in me."
    robin.name "Good."
    pc "And it's a bad time of the month. It might be getting me pregnant as we speak."
    robin.name "Slut! I can't wait to see you growing fat."
    hide robin with dissolve
    jump pub_waitress_work_others_end

label pub_waitress_work_others_end:
    $ renpy.scene()
    with dissolve
    if player.left_hand:
        jump pub_waitress_work_ogleend
    else:
        jump pub_waitress_work_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
