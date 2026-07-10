







label whore_bed_sex_onback:
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_onback pout look_up knee", "sb_onbed"]))
    with dissolve
    "[rlist.foreplay_preparesex_layback]"
    $ if_showing("sb_onback", random(["missionary oh", "hump oh"]), "sb_onbed", "poke")
    jump whore_bed_sex_onback_vag_picker

label whore_bed_sex_onback_vag_picker:
    jump expression WeightedChoice([
    
    ("whore_bed_sex_onback_vag_normal", 5),
    ("whore_bed_sex_onback_anal", 1),
    ("whore_bed_sex_onback_anal", If(player.want_sexlocation == 2, 1, 0)),
    ("whore_bed_sex_onback_anal", If(player.soldrequest == "anal", 50, 0)),
    ])

label whore_bed_sex_onback_vag_normal:
    "[rlist.having_sex_tease_vag]"
    "[rlist.having_sex_penetrate_vag_slow]"
    $ if_showing("sb_onback", "happy", "sb_onbed", "sex")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    if player.want_sexlocation == 2:
        pc "[rlist.having_sex_thats_not_anal_happy]"
label whore_bed_sex_onback_vag_normal_inturrupt:
    "[rlist.having_sex_action_onback]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    if not numgen(0,10):
        jump whore_bed_sex_onback_anal_switch

    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"

    if not numgen(0,3):
        jump whore_bed_sex_onback_vag_position_switch

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_onback_vag_normal_cum_picker

label whore_bed_sex_onback_vag_rough:
    "[rlist.having_sex_tease_vag_rough]"
    $ player.spank()
    if player.soldrequest == "anal":
        pcm "[rlist.having_sex_asked_anal_wonder]"
        pc "[rlist.having_sex_asked_anal_ask]"
        $ player.spank()
        tempname.name "[rlist.having_sex_asked_anal_ask_respond]"


    $ player.sex_vag(tempname, quest_temp)
    $ player.face_shock()
    $ if_showing("sb_onback", "ooh", "sb_onbed", "sex", trans=hpunch)
    "[rlist.having_sex_penetrate_vag_forced]"
    "[rlist.having_sex_action]"
    pc "[rlist.having_sex_nng]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_nng]"
    "[rlist.having_sex_enjoy_rough]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_nng]"

    if not numgen(0,3):
        jump whore_bed_sex_onback_vag_position_switch

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_onback_vag_normal_cum_picker





label whore_bed_sex_onback_vag_position_switch:
    "[rlist.having_sex_switch_position]"
    jump expression WeightedChoice([
    ("whore_bed_sex_onback_vag_position_switch_doggy", 100),
    ])

label whore_bed_sex_onback_vag_position_switch_doggy:
    tempname.name "[rlist.having_sex_told_behind]"
    pc "Oh?"
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_onfours", "sb_ontop", "sb_doggy1", "sb_doggy2"]))
    with dissolve
    "I flip my body over and while I am trying to get in position to give him access, he grabs hold of my hips and pulls me towards him."
    jump whore_street_sex_floor_vag_normal





label whore_bed_sex_onback_vag_normal_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_bed_sex_onback_vag_cum_want", 
    cum_notwant="whore_bed_sex_onback_vag_cum_notwant", 
    cum_pullout="whore_bed_sex_onback_cum_pullout",
    cum_pullout_poke="whore_bed_sex_onback_cum_pullout_poke",
    cum_pullout_anal="whore_bed_sex_onback_cum_pullout_anal",    
    )

label whore_bed_sex_onback_vag_cum_want:
    if renpy.showing("sb_onback missionary") and (player.has_perk(perk_preg_want) and not numgen(0,3)) or not numgen(0, 10):

        jump whore_bed_sex_onback_vag_cum_want_preg

    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    $ if_showing("sb_onback", "happy look_down")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_onback", "happy look_up")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"

    jump whore_street_sex_end

label whore_bed_sex_onback_vag_cum_want_preg:
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    $ if_showing("sb_onback", "lock")
    "I wrap my legs around him, making sure he cannot escape and gives me what I want."
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    $ if_showing("sb_ontop", "up happy", "sb_doggy1", "oh", "sb_doggy2", "happy straight")
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"

    jump whore_street_sex_end

label whore_bed_sex_onback_vag_cum_notwant:
    pc "[rlist.having_sex_pc_cum_pullout_ask_front]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    $ if_showing("sb_onback", "pout angry look_up")
    tempname.name "Ahh yes."
    pc "Ah what are you doing?"

    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_vag_notwant_excuse]"
    pc "*Sigh*"
    $ if_showing("sb_onback", "no_sex knee", "sb_onbed", "relax")
    jump whore_street_sex_end





label whore_bed_sex_onback_anal:
    "[rlist.having_sex_tease_vag]"
    $ if_showing("sb_onback", "ah", "sb_onbed", "sex")

    "[rlist.having_sex_vag_to_ass_switch]"

    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    $ if_showing("sb_onback", "ag", "sb_onbed", "sex")

    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_bed_sex_onback_anal_jump

label whore_bed_sex_onback_anal_jump:
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"

    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_pc_close_anal]"
    $ player.face_orgasm()

    tempname.name "[rlist.having_sex_man_close_dialogue]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_cum_dialogue]"
    $ player.sex_cum_anal_location_offer(
        
        cum_want="whore_bed_sex_onback_ass_cum_want", 
        cum_notwant="whore_bed_sex_onback_ass_cum_notwant", 
        cum_pullout="whore_bed_sex_onback_cum_pullout"
    )


label whore_bed_sex_onback_anal_switch:
    $ if_showing("sb_onback", "oh hump", "sb_onbed", "poke")
    "[rlist.having_sex_vag_to_ass_switch]"

    if player.want_sexlocation == 2:
        pc "Finally aiming for the hole I asked for? ♥"
    else:
        pc "[rlist.having_sex_tease_ass_suprise]"

    "[rlist.having_sex_vag_to_ass]"
    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_onback", "happy missionary", "sb_onbed", "sex")
    "[rlist.having_sex_penetrate_ass_slow]"
    pc "[rlist.having_sex_yes]"
    jump whore_bed_sex_onback_anal_jump

label whore_bed_sex_onback_cum_pullout:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"

    $ if_showing("sb_onback", "happy hump", "sb_onbed", "poke")
    $ if_showing("sb_onbed", "cum")
    $ player.sex_cum(tempname, "belly", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    jump whore_street_sex_end

label whore_bed_sex_onback_cum_pullout_anal:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_pc_cum_pullout_ask_anal_reply]"
    jump whore_bed_sex_onback_anal_switch

label whore_bed_sex_onback_cum_pullout_poke:
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    $ if_showing("sb_onback", "happy hump", "sb_onbed", "poke")
    $ player.sex_cum(tempname, "pullout", quest_temp)
    "[rlist.having_sex_cumming_pullout_poke_action]"
    if player.want_pullout:
        $ player.face_angry()
        $ if_showing("sb_onback", "worried look_down pout")
        pc "[rlist.having_sex_cumming_pullout_poke_reaction]"
        $ if_showing("sb_onback", "worried look_up pout")

        "[rlist.having_sex_cumming_pullout_poke_reaction_followup]"
        pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    else:

        pc "[rlist.having_sex_came_inside_vag_want]"
    jump whore_street_sex_end

label whore_bed_sex_onback_cum_pullout_wank:
    $ npc_race3 = npc_race
    pc "[rlist.having_sex_pc_cum_pullout_ask]"
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    if renpy.showing("sb_onback") and not numgen(0,2):
        $ if_showing("sb_onback", "knee look_up ooh")
        "He pulls out, then rushes over to me to help him finish the job."
        $ if_showing("sb_onback", "man_right r_penis look_right ooh")
        "I grab hold of his cock which has already started to leak and wank him off until..."
    else:
        $ renpy.scene()
        show sb_facefuck
        with dissolve
        "He pulls out, straddles my face and starts furiously wanking."
        "I just lay there watching him wank himself off."
        show sb_facefuck squint

        if not numgen(0,2):

            show sb_facefuck blow with hpunch
            "Without warning, he shoves his cock in my mouth and immediately starts to cum."
            tempname.name "[rlist.blowjob_cum_mouth_man_dialogue]"
            show sb_facefuck deep closed with dissolve
            $ player.sex_cum(tempname, "mouth", quest_temp)
            "[rlist.blowjob_cum_mouth]"
            tempname.name "[rlist.having_sex_man_yes]"
            pc "[rlist.blowjob_muffle]"
            show sb_facefuck blow down with dissolve
            show sb_facefuck mast up with dissolve
            pc "[rlist.blowjob_cum_mouth_swallow_reaction]"
            tempname.name "[rlist.blowjob_cum_mouth_swallow_reaction_man]"
            jump whore_street_sex_end


    "[rlist.handjob_man_cum_action_face_man]"
    $ player.sex_cum(tempname, "face", quest_temp)
    tempname.name "[rlist.having_sex_man_yes]"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    tempname.name "*Phew*"
    jump whore_street_sex_end

label whore_bed_sex_onback_ass_cum_want:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ if_showing("sb_onback", "happy")
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    jump whore_street_sex_end

label whore_bed_sex_onback_ass_cum_notwant:
    pc "[rlist.having_sex_pc_cum_ass_pullout_ask]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"

    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname.name "Ahh yes."
    $ if_showing("sb_onback", "straight pout")
    pc "[rlist.having_sex_came_inside_ass_notwant_reaction]"
    tempname.name "[rlist.having_sex_came_inside_ass_notwant_excuse]"
    pc "*Sigh*"
    pc "Whatever..."
    jump whore_street_sex_end

label whore_bed_sex_onback_forcesex:
    $ player.sex_forced(tempname, quest_temp)
    if player.has_perk(perk_freeuse):
        $ player.face_angry()
        with hpunch
        pc "Ugh! Not so rough!"
        $ if_showing("sb_onback", "angry pout")
        tempname.name "This will go a lot easier if you stop struggling!"
        pc "I'm not struggling you idiot!"
        "He continues to pin me down as he thrusts inside me. Fucking me with increased vigour."
        tempname.name "Mmmmm, such a lovely young slut."
        pc "..."
        tempname.name "Ahhhhhh!"
        $ player.sex_cum(tempname, "inside", quest_temp)
        tempname.name "Ahhh yes!"
        $ if_showing("sb_onback", "hump look_down", "sb_onbed", "poke")
        pc "Had your fun?"
        $ if_showing("sb_onback", "no_sex", "sb_onbed", "noman")
        "Once he is finished inside me, he quickly pulls out, puts his trousers on and leaves. Leaving me alone."
        $ renpy.scene()
        with dissolve
        pc "Idiot."
    elif player.check_fight(2):
        $ player.sex_end()
        $ player.face_angry()
        $ if_showing("sb_onback", "angry ah look_up", trans=vpunch)
        "I jump away as he tried so grab hold of me, but he doesn't manage to keep a grip on me. Realising his predicament, he quickly pulls his trousers up and runs away."
        $ renpy.scene()
        with dissolve
        pc "What the fuck! What a cunt!"
        $ player.face_cry()
        if player.has_perk([perk_whore, perk_numb]):
            $ player.sex_end()
            pcm "Fuck that was a close one. What the hell is it with these fuckers?"
            pc "*Phew*"
            jump whore_street_sex_end
        pc "*SOB*"
        if player.virgin_pregcheck:
            pc "My first time comes to this..."
        pc "I can't believe that just happened..."
        pc "..."
    else:

        $ player.face_angry()
        $ if_showing("sb_onback", "angry ah look_up", trans=vpunch)
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
        $ player.sex_cum(tempname, "inside", quest_temp)
        tempname.name "Ahhh yes!"
        pc "*SOB*"
        $ if_showing("sb_onback", "hump look_down", "sb_onbed", "poke")
        $ if_showing("sb_onback", "no_sex", "sb_onbed", "noman")
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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
