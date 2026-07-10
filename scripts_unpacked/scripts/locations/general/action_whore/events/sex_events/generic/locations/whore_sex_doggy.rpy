





label whore_street_sex_floor:
    $ npc_race3 = npc_race
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_onfours", "sb_ontop", "sb_doggy1", "sb_doggy2"]))
    with dissolve
    "[rlist.foreplay_preparesex_fours]"
    if player.soldrequest == "anal":
        $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    else:
        $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    jump whore_street_sex_floor_vag_picker

label whore_street_sex_floor_vag_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_floor_vag_rough", 1),
    ("whore_street_sex_floor_vag_rough", If(player.soldrequest == "rough", 100, 0)),
    ("whore_street_sex_floor_vag_normal", 5),
    ("whore_street_sex_floor_anal", 1),
    ("whore_street_sex_floor_anal", If(player.want_sexlocation == 2, 1, 0)),
    ("whore_street_sex_floor_anal", If(player.soldrequest == "anal", 100, 0)),
    ])

label whore_street_sex_floor_vag_normal:
    $ npc_race3 = npc_race
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "up vag", "sb_ontop", "back ag", "sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag", "sb_assup", "sex")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    if player.want_sexlocation == 2:
        pc "[rlist.having_sex_thats_not_anal_happy]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    if not numgen(0,10):
        jump whore_street_sex_floor_anal_switch

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_floor_vag_cum_picker

label whore_street_sex_floor_vag_rough:
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag_rough]"
    $ player.spank()
    if player.soldrequest == "anal":
        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_ask]"
        $ player.spank()
        tempname.name "[rlist.having_sex_asked_anal_ask_respond]"

    $ player.sex_vag(tempname, quest_temp)
    $ player.face_shock()
    $ if_showing("sb_onfours", "up vag", "sb_ontop", "back ag", "sb_doggy1", "ag vag head_down", "sb_doggy2", "head_back happy wink insidevag", "sb_assup", "sex", trans=hpunch)
    "[rlist.having_sex_penetrate_vag_forced]"
    "[rlist.having_sex_action]"
    pc "[rlist.having_sex_nng]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_nng]"
    "[rlist.having_sex_enjoy_rough]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_nng]"

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_street_sex_floor_vag_cum_picker

label whore_street_sex_floor_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_floor_vag_cum_want", 
    cum_notwant="whore_street_sex_floor_vag_cum_notwant", 
    cum_pullout="whore_street_sex_floor_cum_pullout",
    cum_pullout_poke="whore_street_sex_floor_cum_pullout_poke",
    cum_pullout_anal="whore_street_sex_floor_cum_pullout_anal",    
    )

label whore_street_sex_floor_vag_notwant:
    $ c.pants = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    if player.want_sexlocation == 2:

        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_comment]"

        if player.check_speech(2):
            tempname.name "[rlist.having_sex_asked_anal_respond]"
            jump whore_street_sex_floor_anal
        else:
            if player.check_sex_agree(4):
                jump whore_street_sex_floor_vag_want
            else:
                tempname.name "[rlist.having_sex_asked_anal_respond]"
    $ player.sex_forced(tempname, quest_temp)
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_angry()
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onfours", "vag up", "sb_doggy1", "grit vag", "sb_doggy2", "head_back shock squint angry insidevag")
    pc "[rlist.having_sex_thats_not_anal_angry]"
    $ dialouge = WeightedChoice([
    ("Don't worry, I'll pull out.", 1),
    ("It's ok. I'll try not to cum inside.", 1),
    ("Don't worry. Just relax and enjoy.", 1),
    ("It's ok. I just want to make you feel good.", 1),
    ])
    tempname.name "[dialouge]"
    pc "[rlist.having_sex_take_it_out]"
    "He doesn't listen and carries on fucking me. There isn't much point in kicking up a fuss "
    jump pub_waitress_work_forcesex

label whore_street_sex_floor_anal:
    $ c.pants = 0
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_doggy2", "pokeasshold")
    $ if_showing("sb_doggy2", "pokeass")

    "[rlist.having_sex_vag_to_ass_switch]"

    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_onfours", "ass", "sb_ontop", "doggy", "sb_doggy1", "anal", "sb_doggy2", "insideass")

    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_floor_anal_jump

label whore_street_sex_floor_anal_jump:
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_pc_close_anal]"
    $ player.face_orgasm()

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_cum_dialogue]"

    $ player.sex_cum_anal_location_offer(
        
        cum_want="whore_street_sex_floor_ass_cum_want", 
        cum_notwant="whore_street_sex_floor_ass_cum_notwant", 
        cum_pullout="whore_street_sex_floor_cum_pullout"
    )












label whore_street_sex_floor_anal_switch:
    $ if_showing("sb_onfours", "poke", "sb_ontop", "doggy", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ if_showing("sb_doggy2", "pokeasshold")
    $ if_showing("sb_doggy2", "pokeass")
    "[rlist.having_sex_vag_to_ass_switch]"

    if player.want_sexlocation == 2:
        pc "Finally aiming for the hole I asked for? ♥"
    else:
        pc "[rlist.having_sex_tease_ass_suprise]"

    "[rlist.having_sex_vag_to_ass]"
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_onfours", "ass", "sb_ontop", "doggy", "sb_doggy1", "anal", "sb_doggy2", "insideass")
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_floor_anal_jump

label whore_street_sex_floor_vag_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"

    jump whore_street_sex_floor_end

label whore_street_sex_floor_vag_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    $ if_showing("sb_ontop", "back shock", "sb_doggy1", "shock", "sb_doggy2", "shock squint angry")
    tempname.name "Ahh yes."
    pc "Ah what are you doing?"

    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    $ if_showing("sb_ontop", "surprise", "sb_doggy1", "neutral", "sb_doggy2", "frown worried")
    pc "*Sigh*"
    jump whore_street_sex_floor_end

label whore_street_sex_floor_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"

    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"

    jump whore_street_sex_floor_end

label whore_street_sex_floor_cum_pullout_anal:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_pc_cum_pullout_ask_anal_reply]"
    jump whore_street_sex_floor_anal_switch

label whore_street_sex_floor_cum_pullout_poke:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "pokevaghold")
    $ player.sex_cum(tempname, "pullout", quest_temp)
    "[rlist.having_sex_cumming_pullout_poke_action]"
    if player.want_pullout:
        $ if_showing("sb_ontop", "back shock", "sb_doggy1", "shock", "sb_doggy2", "shock squint angry")
        pc "[rlist.having_sex_cumming_pullout_poke_reaction]"
        $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")

        "[rlist.having_sex_cumming_pullout_poke_reaction_followup]"
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:

        pc "[rlist.having_sex_came_inside_vag_want]"
    jump whore_street_sex_floor_end

label whore_street_sex_floor_ass_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    jump whore_street_sex_floor_end

label whore_street_sex_floor_ass_cum_notwant:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    $ if_showing("sb_ontop", "surprise", "sb_doggy1", "neutral", "sb_doggy2", "frown worried")
    pc "[rlist.having_sex_came_inside_ass_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_ass_notwant_excuse]"
    pc "*Sigh*"
    pc "Whatever..."
    jump whore_street_sex_floor_end

label whore_street_sex_floor_end:
    $ if_showing("sb_onfours", "poke", "sb_doggy1", "poke", "sb_doggy2", "cum")
    tempname.name "That was fun."
    $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
    jump whore_street_sex_end
    if loc(loc_motel_pinkroom):
        jump whore_street_sex_end
    "The guy pulls his trousers up and walks away without another word."
    $ renpy.scene()
    with dissolve
    $ pc_dress()
    pcm "Right... Well, better get back to it."
    jump whore_street_sex_end

label whore_street_sex_floor_forcesex:
    if player.has_perk(perk_freeuse):
        $ player.face_angry()
        with hpunch
        pc "Ugh! Not so rough!"
        $ player.face_cry()
        if player.selling:
            tempname.name "Stop struggling, I paid to fuck you!"
        else:
            tempname.name "This will go a lot easier if you stop struggling!"
        pc "I'm not struggling you idiot!"
        "He continues to pin me down as he thrusts inside me. Fucking me with increased vigour."
        tempname.name "Mmmmm, such a lovely young slut."
        pc "..."
        tempname.name "Ahhhhhh!"
        $ player.sex_cum(rapist, "inside", quest_temp)
        tempname.name "Ahhh yes!"
        pc "Had your fun?"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me alone."
        $ renpy.scene()
        with dissolve
        pc "Idiot."
    elif player.check_fight(2):
        $ player.sex_end()
        $ player.face_angry()
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=vpunch)
        "I jump away as he tried so grab hold of me, but he doesn't manage to keep a grip on me. Realising his predicament, he quickly pulls his trousers up and runs away."
        $ renpy.scene()
        with dissolve
        pc "What the fuck! What a cunt!"
        $ player.face_cry()
        if player.has_perk([perk_whore, perk_numb]):
            $ player.sex_end()
            pcm "Fuck that was a close one. Just trying to clean and these fuckers do that?"
            pc "*Phew*"
            jump whore_street_sex_end
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        pc "I can't believe that just happened..."
        pc "..."
    else:

        $ player.face_angry()
        with hpunch
        "I try to worm my way out of his grasp, but I am not strong enough and he pulls me closer while fucking me."
        $ player.face_cry()
        pc "Fuck!"
        if player.selling:
            tempname.name "Stop struggling, I paid to fuck you!"
        else:
            tempname.name "This will go a lot easier if you stop struggling!"
        pc "Fuck you!"
        "He continues to pin me down as he thrusts inside me. Fucking me with increased vigour knowing that I can't push him off."
        if player.virgin_pregcheck:
            tempname.name "Mmmmm, such a lovely young slut. And is that blood? Were you a virgin?"
            tempname.name "Oh man having popped the cherry of some little teenage slut. I will have to tell everyone."
            pc "*SOB*"
        else:
            tempname.name "Mmmmm, such a lovely young slut."
            pc "*SOB*"
        tempname.name "Ahhhhhh!"
        pc "*SOB*"
        $ player.sex_cum(rapist, "inside", quest_temp)
        tempname.name "Ahhh yes!"
        pc "*SOB*"
        $ if_showing("sb_onfours", "noman", "sb_ontop", "no_doggy", "sb_doggy1", "noman", "sb_doggy2", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me alone."
        $ renpy.scene()
        with dissolve
        pcm "Bastard!"
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        pc "I can't believe that just happened..."
        pc "..."
    jump whore_street_sex_force_end

label whore_street_sex_floor_cumrun:
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
