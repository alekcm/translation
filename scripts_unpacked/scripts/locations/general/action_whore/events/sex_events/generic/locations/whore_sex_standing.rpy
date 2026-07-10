


label whore_street_sex_standing:
    $ renpy.scene()
    if loc_cur.loc_type == "room":
        $ renpy.show(renpy.random.choice(["sb_againstwall2", "sb_againstwall3", "sb_table bentover happy"]))
    else:
        $ renpy.show(renpy.random.choice(["sb_againstwall2", "sb_againstwall3"]))
    with dissolve
    "[rlist.foreplay_preparesex_wall]"
    if player.soldrequest == "anal":
        $ if_showing("sb_againstwall2", "pokeasshand wink worried", "sb_againstwall3", "poke wink", "sb_table", "mast")
    else:
        $ if_showing("sb_againstwall2", "pokevaghand wink worried", "sb_againstwall3", "poke wink")
    jump whore_street_sex_standing_vag_picker

label whore_street_sex_standing_vag_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_standing_vag_rough", 1),
    ("whore_street_sex_standing_vag_normal", 5),
    ("whore_street_sex_standing_anal", 1),
    ("whore_street_sex_standing_anal", If(player.want_sexlocation == 2, 1, 0)),
    ("whore_street_sex_standing_anal", If(player.soldrequest == "anal", 50, 0)),
    ])

label whore_street_sex_standing_vag_normal:

    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast", "sb_table", "sex")
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")




    if player.soldrequest == "anal":
        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_ask]"
        tempname.name "[rlist.having_sex_asked_anal_ask_respond]"

    "[rlist.having_sex_penetrate_vag_slow_pull]"
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_againstwall2", "insidevag ag wink", "sb_againstwall3", "sex wink ag", "sb_table", "ag")
    if player.soldrequest == "anal":
        pc "[rlist.having_sex_thats_not_anal_happy]"
    "[rlist.having_sex_action]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call

    "[rlist.having_sex_enjoy]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"



    pc "[rlist.having_sex_yes]"
    if not numgen(0,30):
        jump whore_street_sex_standing_vag_normal_cum_confused
    if not numgen(0,10):
        jump whore_street_sex_standing_vag_anal_switch

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_street_sex_standing_vag_normal_cum_picker

label whore_street_sex_standing_vag_rough:
    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast", "sb_table", "sex")
    "[rlist.having_sex_tease_vag_rough]"
    $ player.spank()
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    if player.soldrequest == "anal":
        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_ask]"
        $ player.spank()
        tempname.name "[rlist.having_sex_asked_anal_ask_respond]"

    $ player.sex_vag(tempname, quest_temp)
    $ player.face_shock()
    $ if_showing("sb_againstwall2", "insidevag shock wink", "sb_againstwall3", "sex wink grit", "sb_table", "pain", trans=hpunch)
    "[rlist.having_sex_penetrate_vag_forced]"
    "[rlist.having_sex_action]"
    pc "[rlist.having_sex_nng]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_nng]"
    "[rlist.having_sex_enjoy_rough]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_nng]"

    if numgen():
        jump whore_street_sex_standing_vag_rough_behind

    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_street_sex_standing_vag_normal_cum_picker

label whore_street_sex_standing_vag_anal_switch:
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    $ if_showing("sb_againstwall2", "pokeass")
    "[rlist.having_sex_vag_to_ass_switch]"

    if player.want_sexlocation == 2:
        pc "Finally aiming for the hole I asked for? ♥"
    else:
        pc "[rlist.having_sex_tease_ass_suprise]"

    "[rlist.having_sex_vag_to_ass]"
    $ if_showing("sb_againstwall2", "insideass", "sb_againstwall3", "sex")
    $ player.sex_anal(tempname, quest_temp)
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_standing_anal_jump

label whore_street_sex_standing_vag_notwant:
    $ if_showing("sb_againstwall2", "pokevaghand", "sb_againstwall3", "mast", "sb_table", "sex")
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    if player.want_sexlocation == 2:
        pc "[rlist.having_sex_asked_anal_comment]"

        if player.check_speech(2):
            tempname.name "[rlist.having_sex_asked_anal_respond]"
            jump whore_street_sex_standing_anal_switch
        else:
            if player.check_sex_agree(4):
                jump whore_street_sex_standing_vag_picker
            else:
                tempname.name "[rlist.having_sex_asked_anal_respond]"
    $ player.sex_forced(tempname, quest_temp)
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_angry()
    $ if_showing("sb_againstwall2", "insidevag shock wink", "sb_againstwall3", "sex wink grit", "sb_table", "shock", trans=hpunch)
    "[rlist.having_sex_penetrate_vag_forced]"
    pc "[rlist.having_sex_thats_not_anal_angry]"
    $ dialouge = WeightedChoice([
    ("Don't worry, I'll pull out.", 1),
    ("It's ok. I'll try not to cum inside.", 1),
    ("Don't worry. Just relax and enjoy.", 1),
    ("It's ok. I just want to make you feel good.", 1),
    ])
    tempname.name "[dialouge]"
    pc "[rlist.having_sex_take_it_out]"
    jump whore_street_sex_forced_attack_position

label whore_street_sex_standing_vag_rough_behind:
    $ renpy.scene()
    show sb_standbehind ah
    with hpunch
    tempname.name "C'mere!"
    "He grabs onto me pulling me away from the wall and wraps his arms around me while hump fucking me."
    "[rlist.having_sex_action]"
    tempname.name "[rlist.foreplay_badgirl_comment]"
    if numgen():
        $ renpy.scene()
        show sb_doggy1 shock
        with hpunch
        "He pulls me about while groping me for a while, then shoves me onto the floor."
        pc "[rlist.sex_exclaim_negative]"
        tempname.name "[rlist.foreplay_badgirl_comment]"
        jump whore_street_sex_floor_vag_rough
    jump whore_street_sex_standing_vag_normal_cum_confused

label whore_street_sex_standing_vag_normal_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="whore_street_sex_standing_vag_normal_cum_want", 
    cum_notwant="whore_street_sex_standing_vag_normal_cum_notwant", 
    cum_pullout="whore_street_sex_standing_vag_normal_cum_pullout",
    cum_pullout_anal="whore_street_sex_standing_vag_normal_cum_pullout_anal", 
    cum_pullout_bj="whore_street_sex_standing_vag_normal_cum_pullout_blowjob",  
    cum_pullout_poke="whore_street_sex_standing_vag_normal_cum_pullout_poke",
    cum_bj="whore_street_sex_standing_vag_normal_cum_pullout_blowjob_init",    
    )

label whore_street_sex_standing_anal:
    $ if_showing("sb_againstwall2", "pokeasshand", "sb_againstwall3", "mast", "sb_table", "mast")
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke", "sb_table", "sex")

    "[rlist.having_sex_vag_to_ass_switch]"

    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_againstwall2", "insideass ag wink", "sb_againstwall3", "sex wink ag", "sb_table", "ag")

    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_standing_anal_jump

label whore_street_sex_standing_anal_jump:
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_pc_close_anal]"
    $ player.face_orgasm()

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_cum_dialogue]"

    $ player.sex_cum_anal_location_offer(
        
        cum_want="whore_street_sex_standing_anal_cum_want", 
        cum_notwant="whore_street_sex_standing_anal_cum_notwant", 
        cum_pullout="whore_street_sex_standing_anal_cum_pullout"
    )












label whore_street_sex_standing_anal_switch:
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke", "sb_table", "mast")
    $ if_showing("sb_againstwall2", "pokeasshand", "sb_table", "sex")
    $ if_showing("sb_againstwall2", "pokevaghand")
    $ if_showing("sb_againstwall2", "pokevag")
    "[rlist.having_sex_vag_to_ass_switch]"

    if player.want_sexlocation == 2:
        pc "Finally aiming for the hole I asked for? ♥"
    elif player.soldrequest == "anal":
        pc "Finally putting it where you wanted to in the first place? ♥"
    else:
        pc "[rlist.having_sex_tease_ass_suprise]"

    "[rlist.having_sex_vag_to_ass]"
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_againstwall2", "insideass ag wink", "sb_againstwall3", "sex wink ag", "sb_table", "ag")
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_standing_anal_jump

label whore_street_sex_standing_vag_normal_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_againstwall2", "happy", "sb_againstwall3", "happy", "sb_table", "happy")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke", "sb_table", "noman")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_vag_normal_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    $ if_showing("sb_againstwall2", "open shock worried", "sb_againstwall3", "squint pout worried", "sb_table", "shock back")
    tempname.name "Ahh yes."
    pc "Ah what are you doing?"

    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    $ if_showing("sb_againstwall2", "frown")
    pc "*Sigh*"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke", "sb_table", "noman")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_vag_normal_cum_confused:
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    pcm "Huh?"
    $ player.spank()
    tempname.name "[rlist.having_sex_man_yes]"
    $ if_showing("sb_againstwall2", "pokevag", "sb_againstwall3", "poke")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman", "sb_table", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_vag_normal_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_againstwall2", "pokevaghand ag wink", "sb_againstwall3", "mast", "sb_table", "mast")
    $ if_showing("sb_againstwall2", "cum", "sb_againstwall3", "cum")
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    jump whore_street_sex_end

label whore_street_sex_standing_vag_normal_cum_pullout_anal:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_pc_cum_pullout_ask_anal_reply]"
    jump whore_street_sex_standing_anal_switch

label whore_street_sex_standing_vag_normal_cum_pullout_poke:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_againstwall2", "pokevaghand ag wink", "sb_againstwall3", "mast")
    $ player.sex_cum(tempname, "pullout", quest_temp)
    "[rlist.having_sex_cumming_pullout_poke_action]"
    if player.want_pullout:
        $ if_showing("sb_againstwall2", "open shock worried", "sb_againstwall3", "squint pout worried", "sb_table", "shock")
        pc "[rlist.having_sex_cumming_pullout_poke_reaction]"
        $ if_showing("sb_againstwall2", "cum", "sb_againstwall3", "cum", "sb_table", "mast")
        "[rlist.having_sex_cumming_pullout_poke_reaction_followup]"
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:

        pc "[rlist.having_sex_came_inside_vag_want]"
        tempname.name "[rlist.sex_end_man_tired]"
        $ if_showing("sb_againstwall2", "poke", "sb_againstwall3", "poke")
        "[rlist.having_sex_came_take_cock_out_vag]"
        $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman", "sb_table", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_anal_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ if_showing("sb_againstwall2", "happy", "sb_againstwall3", "happy", "sb_table", "happy")
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke", "sb_table", "noman")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_anal_cum_notwant:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    $ if_showing("sb_againstwall2", "frown", "sb_againstwall3", "pout", "sb_table", "shock")
    pc "[rlist.having_sex_came_inside_ass_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_ass_notwant_excuse]"
    pc "*Sigh*"
    pc "Whatever..."
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_againstwall2", "pokeass", "sb_againstwall3", "poke", "sb_table", "noman")
    "[rlist.having_sex_came_take_cock_out_vag]"
    $ if_showing("sb_againstwall2", "noman", "sb_againstwall3", "noman")
    jump whore_street_sex_end

label whore_street_sex_standing_anal_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_againstwall2", "pokevaghand ag wink", "sb_againstwall3", "mast", "sb_table", "mast")
    $ if_showing("sb_againstwall2", "cum", "sb_againstwall3", "cum")
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    jump whore_street_sex_end

label whore_street_sex_standing_spank_call:
    $ player.spank()
    $ if_showing("sb_againstwall2", "closed shock", "sb_againstwall3", "closed grit", "sb_table", "shock")
    pc "[rlist.sex_exclaim_like]"
    $ if_showing("sb_againstwall2", "wink happy", "sb_againstwall3", "wink happy", "sb_table", "happy")
    $ player.spank()
    tempname.name "[rlist.sex_exclaim_like_reply]"
    $ if_showing("sb_againstwall2", "open vhappy", "sb_againstwall3", "up", "sb_table", "back")
    pc "[rlist.sex_exclaim_more]"
    $ player.spank()
    $ if_showing("sb_againstwall2", "wink ag", "sb_againstwall3", "wink ag", "sb_table", "ag up")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
