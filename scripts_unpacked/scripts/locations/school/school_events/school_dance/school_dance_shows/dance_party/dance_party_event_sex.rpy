label random_event_picker_dance_party_sexy_picker:
    jump expression WeightedChoice([
    
    ("random_event_picker_dance_party_general_gropesex", 100),
    ("random_event_picker_dance_party_general_gropeblow", 100),
    ("random_event_picker_dance_party_general_sex_invite", 100),
    ("random_event_picker_dance_party_general_gangbang_invite", 100),
    ("random_event_picker_dance_party_grope_1", 100),
    ("random_event_picker_dance_party_grope_2", 100),
    ("random_event_picker_dance_party_takeclothes_1", If(c.top, 100, 0)),
    ("random_event_picker_dance_party_takeclothes_2", If(c.bottom, 100, 0)),
    ])

label random_event_picker_dance_party_general_gropesex:
    $ player.grope()
    pc "Ah!"
    partyman.name "Nice one baby."
    $ player.grope()
    pc "Oi, calm down."
    partyman.name "Don't worry, we are all here to have fun."
    pc "Huh?"
    $ player.grope_poke()
    pc "Oh?"
    partyman.name "How about it?"
    if player.check_whore_agree_choice(option1="Sure, why not" ,option2="Noo, I have things to do"):
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_mainroom_end")
        jump whore_street_sex_standing
    else:
        pc "Sorry mate, not out here."
        $ player.grope_end()
        if numgen():
            partyman.name "How about we go somewhere quiet then?"
            pc "Err..."
            if player.check_whore_agree_choice(option1="Sure, why not" ,option2="No thanks mate"):
                $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
                jump whore_street_customer_pick_location_partyhouse_bedroom
            else:
                partyman.name "No worries love. I'll check if one of the other girls want some fun."
                pc "Sure, enjoy yourself."
                jump travel

label random_event_picker_dance_party_general_gropeblow:
    $ player.grope()
    pc "Ah!"
    partyman.name "Nice one baby."
    $ player.grope()
    pc "Oi, calm down."
    partyman.name "Don't worry, we are all here to have fun."
    $ grope_mastleft = True
    pc "Oh?"
    partyman.name "How about it? Wanna suck me off?"
    if player.check_whore_agree_choice(option1="Sure, why not" ,option2="Noo, I have things to do", request="oral"):
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_mainroom_end")
        jump whore_street_sex_nosex_picker
    else:
        pc "Sorry mate, not out here."
        $ player.grope_end()
        if numgen():
            partyman.name "How about we go somewhere quiet then?"
            pc "Err..."
            if player.check_whore_agree_choice(option1="Sure, why not" ,option2="No thanks mate", request="oral"):
                $ dance_party_sex_init("random_event_picker_dance_party_general_sex_mainroom_end")
                jump whore_street_customer_pick_location_partyhouse_bedroom
            else:
                partyman.name "No worries love. I'll check if one of the other girls want some fun."
                pc "Sure, enjoy yourself."
                jump travel

label random_event_picker_dance_party_general_sex_invite:
    partyman.name "Hey darling, how about we go somewhere for a little fun?"
    pc "Err..."
    if player.check_whore_agree_choice(option1="Sure, why not" ,option2="Noo, I have things to do"):
        pc "Let's go "
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
        jump whore_street_customer_pick_location_partyhouse_bedroom
    else:
        pc "Sorry mate, another time."
        $ player.spank()
        partyman.name "No problem."
        jump travel

label random_event_picker_dance_party_general_gangbang_invite:
    $ player.grope()
    partyman.name "Hey darling, how about we go somewhere for a little fun?"
    pc "Err..."
    $ grope_mastleft = True
    pc "Wait, all of you?"
    partyman.name "Yeah, we can all have some fun."
    if player.check_whore_agree_choice(option1="Sure, why not" ,option2="Noo, I have things to do"):
        pc "Let's go "
        $ player.grope_end()
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
        $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
        $ player.sex_man_amount = numgen(3,8)
        jump whore_street_sex_group_start_picker
    else:
        pc "Sorry lads, don't think I can deal with that."
        $ player.grope_end()
        $ player.spank()
        partyman.name "No problem."
        jump travel

label random_event_picker_dance_party_general_sex_mainroom_end:
    $ player.spank()
    partyman.name "Cheers love. You girls really liven this place up."
    pc "We sure do."
    $ renpy.scene()
    with dissolve
    $ player.face_normal()
    pcm "Better get some more wine I guess..."
    jump travel

label random_event_picker_dance_party_general_sex_bedroom_end:
    partyman.name "Hope you girls keep coming here."
    if not numgen(0,3):
        partyman2.name "Oh, you finished? Can I have a turn?"
        $ player.sex_man_amount = numgen(1,3)
        $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
        jump whore_street_sex_group_picker
    $ renpy.scene()
    with dissolve
    pcm "Should head back I guess."
    if not numgen(0,5):
        partyman2.name "Still looking to have some fun darling?"
        if player.check_sex_agree_choice(diff=2,option1="Sure, why not" ,option2="Noo, I have things to do"):
            $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
            jump whore_sex_start
        else:
            pc "Sorry mate, I need to clean up a bit."
            partyman2.name "No problem luv. I'll ask around."
    if player.cum_visible:
        pcm "I had better clean up before heading back out there."
        "I head to the sink and clean up any cum from my body."
        $ player.cum_clean_outside()
    $ walk(loc_party_main)
    jump travel

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_svet_threesome:
    show sb_tripplesex svet rachel dani with dissolve
    pc "Oh... Errr, I'll find another room..."
    hide sb_tripplesex
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_anabel_threesome:
    show sb_tripplesex anabel rachel dani with dissolve
    pc "Oh... Errr, I'll find another room..."
    hide sb_tripplesex
    $ walk(loc_party_main)
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_danielle:
    show dance_dani_group lookup with dissolve
    pc "Ah, sorry..."
    dani.name "Mmmmfff!"
    pc "Let's find another room."
    hide dance_dani_group
    $ walk(loc_party_main)
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_rachel:
    show dance_rachel_dp with dissolve
    pc "Ah, sorry..."
    rachel.name "Ah fuck yes!"
    pc "Let's find another room."
    hide dance_rachel_dp
    $ walk(loc_party_main)
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_svetlana:
    show dance_svet_buk with dissolve
    pc "Ah, sorry..."
    "Man" "Take it you dirty whore!"
    pc "Let's find another room."
    hide dance_svet_buk
    $ walk(loc_party_main)
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_anabel:
    show dance_anabel_behind with dissolve
    pc "Ah, sorry..."
    anabel.name "Oh fuck fuck fuck..."
    pc "Let's find another room."
    hide dance_anabel_behind
    $ walk(loc_party_main)
    $ walk(random([loc_party_bedroom1, loc_party_bedroom2, loc_party_bedroom3, loc_party_bedroom4]))
    jump whore_sex_start

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel:
    if numgen():
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_sex
    else:
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_blow

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_blow:
    $ temp_var_1 = []
    $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
    $ add_to_list(quest_whore.list, "should_pay")
    if all(["party_sex" in dani.list, "party_sex" in rachel.list]):
        show sb_trippleblow dani mid_man rachel close_man with dissolve
        $ temp_var_1 = ["rachel", "dani"]
    elif "party_sex" in dani.list:
        show sb_trippleblow dani mid_man with dissolve
        $ temp_var_1 = ["dani"]
    else:
        show sb_trippleblow rachel close_man with dissolve
        $ temp_var_1 = ["rachel"]

    pc "Err, sorry. Wrong room."
    partyman.name "No, looks right to me. We can stay here."
    pc "Ah... Okay."
    if "party_sex" in rachel.list:
        rachel.name "Mmmmfff!"

    show sb_trippleblow far_man with dissolve
    partyman.name "C'mon darlin'."
    pc "Right..."
    "I hear over, get on my knees and take the guy in my mouth."
    show sb_trippleblow pc with dissolve
    $ player.sex_oral(partyman, quest_dancevip)
    "[rlist.blowjob_start_suck]"
    pc "[rlist.blowjob_muffle]"
    partyman.name "[rlist.having_sex_man_yes]"
    "[rlist.blowjob_start_suck_reaction]"
    pc "[rlist.blowjob_muffle]"

    if not numgen(0,2):
        if "rachel" in temp_var_1:
            show sb_trippleblow no_close close_noman with dissolve
            rachel.name "Where ya going?"
            "Man" "I'm gonna fuck your friend while she is busy."
            rachel.name "Oh? Okay, have fun [name]."
        else:

            show sb_trippleblow no_mid mid_noman with dissolve
            dani.name "Err, you didn't finish."
            "Man" "I know. I'm gonna fuck your friend while she is busy."
            dani.name "Oh, okay then."
        pcm "Huh?"

        "While I am sucking this guy's cock, I feel something going on behind me and have a pretty good idea what."
        $ renpy.scene()
        show sb_doggy1 poke blow
        with dissolve
        "He starts touching my ass and rubbing his cock against me."
        $ add_to_list(player.sex_holes, "mouth")
        $ player.sex_man_amount = 1
        jump expression WeightedChoice([
        ("whore_street_sex_group_spitroast_doggy_vag", 100),
        ("whore_street_sex_group_spitroast_doggy_anal", If(player.check_anal_agree(), 50, 0)),
        ])

    elif numgen(0,2):
        $ renpy.scene()
        $ renpy.show(random(["sb_blowjob up suck", "sb_spitroast up blow"]))
        with dissolve
        jump whore_street_sex_blowjob_jump_cum
    else:

        partyman.name "How about we get this party really started?"
        if "rachel" in temp_var_1:
            rachel.name "oooh, wanna fuck us? About time!"
        else:

            dani.name "Err, you want to do something more?"
            partyman.name "Yeah, come here."
        $ renpy.scene()
        jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_sex_jumper

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_sex:
    $ temp_var_1 = []
    $ dance_party_sex_init("random_event_picker_dance_party_general_sex_bedroom_end")
    $ add_to_list(quest_whore.list, "should_pay")
    if all(["party_sex" in dani.list, "party_sex" in rachel.list]):
        show sb_tripplesex dani rachel with dissolve
        $ temp_var_1 = ["rachel", "dani"]
    elif "party_sex" in dani.list:
        show sb_tripplesex dani with dissolve
        $ temp_var_1 = ["dani"]
    else:
        show sb_tripplesex rachel with dissolve
        $ temp_var_1 = ["rachel"]

    pc "Err, sorry. Wrong room."
    partyman.name "No, looks right to me. We can stay here."
    pc "Ah... Okay."
    if "party_sex" in rachel.list:
        rachel.name "Lotsa room [name]!"

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_sex_jumper:
    if "party_sex" in dani.list:
        show sb_tripplesex pc with dissolve
    else:
        show sb_tripplesex pc right
    with dissolve
    partyman.name "Good girl."
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow_pull]"
    $ player.sex_vag(partyman, quest_dancevip)
    show sb_tripplesex happy
    $ player.face_excited()
    pc "Haa fuck yes!"
    if "rachel" in temp_var_1:
        rachel.name "Haha, go [name]!"
    else:
        dani.name "Ah, getting fucked?"
        pc "Haaa yeah..."
    "[rlist.having_sex_action]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_6

    "[rlist.having_sex_enjoy]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"

    if not "rachel" in temp_var_1:
        rachel.name "Ah, here you guys are."
        pc "Ah fuck!"
        $ add_to_list(rachel.list, "party_sex")
        $ add_to_list(temp_var_1, "rachel")
        show sb_tripplesex right rachel with dissolve
        rachel.name "I'll have fun with you guys!"
        dani.name "The more the merrier."
    elif not "dani" in temp_var_1 and dani.iswhore:
        dani.name "Oh... Err..."
        rachel.name "[dani.name]! Youcan bring your friend and join."
        $ add_to_list(dani.list, "party_sex")
        $ add_to_list(temp_var_1, "dani")
        show sb_tripplesex left dani with dissolve
        dani.name "Okay. We can have fun together."

    pc "[rlist.having_sex_yes]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_7

    "[rlist.having_sex_enjoy]"
    if "rachel" in temp_var_1 and "dani" in temp_var_1:
        "Slapping sounds fill the room as the three of us are fucked side by side by these men."
        rachel.name "Yes fuck go harder!"
        dani.name "Oh fuck!"
        pc "Haaaa yes!"
    elif "rachel" in temp_var_1:
        show sb_tripplesex right
        "I look [rachel.name] in the eye as I am being fucked and I can see the pleasure on her face."
        rachel.name "Yes fuck go harder!"
        pc "Haaaa yes!"
    else:
        show sb_tripplesex left
        "I look over at [dani.name] as she is being fucked an she shares a look with me. Both of us being fucked side by side."
        dani.name "Oh fuck!"
        pc "Haaaa yes!"

    "[rlist.having_sex_enjoy]"
    if "rachel" in temp_var_1:
        "Guy" "Oh fuck you dirty whore. I am close."
        rachel.name "Ah yes keep fucking me!"
        pc "Gonna get sticky."
        rachel.name "Yes make me sticky!"
        "Guy" "Ah fuck yes!"
        "Guy" "Haaaaa."
        $ rachel.have_sex(partyman, anal_reduce=True)
        rachel.name "Ohhh I feel it."
        if "dani" in temp_var_1:
            dani.name "Slut!"
        "Guy" "Haa yeah..."
        show sb_tripplesex no_right with dissolve
    if "dani" in temp_var_1:
        if "rachel" in temp_var_1:
            "Man" "Your turn now!"
        else:
            "Man" "Oh fuck you dirty whore. I am close."
        dani.name "Oh? Gonna cum?"
        "Man" "Ah fuck yes!"
        "Man" "Haaaaa."
        pc "Ohh, [dani.name] is going to get messy."
        dani.name "Ahhh fuck!"
        $ dani.have_sex(partyman, anal_reduce=True)
        "Man" "Fuck yes! Fuuuuuuccck!"
        "Man" "Haaa that was good."
        show sb_tripplesex no_left with dissolve

    partyman.name "Your turn now!"

    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Cum inside!", choice_pullout="Not inside.",  
    cum_want="random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_cum_want", 
    cum_notwant="random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_cum_notwant", 
    cum_pullout="whore_street_sex_standing_vag_normal_cum_pullout",    
    )

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    partyman.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(partyman, "inside", quest_dancevip)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    partyman.name "[rlist.sex_end_man_tired]"
    "[rlist.having_sex_came_take_cock_out_vag]"
    jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_end

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    partyman.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(partyman, "inside", quest_dancevip)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    partyman.name "Ahh yes."
    pc "Ah what are you doing?"
    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    partyman.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    pc "*Sigh*"
    "[rlist.having_sex_came_take_cock_out_vag]"
    jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_end

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    partyman.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ player.sex_cum(partyman, "ass", quest_dancevip)
    "[rlist.having_sex_cumming_pullout_action]"
    partyman.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    jump random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_end

label random_event_picker_dance_party_general_sex_bedroom_inturrupt_dani_rachel_end:
    hide sb_tripplesex
    if "rachel" in temp_var_1:
        show rachel at right5
    if "dani" in temp_var_1:
        show dani at right6
    with dissolve
    if "rachel" in temp_var_1:
        rachel.name "Ha, that was fun!"
        hide rachel with dissolve
    if "dani" in temp_var_1:
        dani.name "Thanks for the company [name]."
        hide dani with dissolve
    $ walk(loc_party_main)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
