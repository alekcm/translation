label whore_street_sex_group_dpstand_start_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_standing_dp_vag_start", 100),
    ("whore_street_sex_group_standing_dp_anal_start", If(player.check_anal_agree(), 50, 0)),
    ])

label whore_street_sex_group_standing_dp_vag_start:
    "One of the guys comes up in front of me, grabs me by the arse and lifts my leg up."
    jump whore_street_sex_group_standing_dp_vag

label whore_street_sex_group_standing_dp_anal_start:
    "One of the guys comes up behind me and pulls me towards him while lifting my leg up."
    jump whore_street_sex_group_standing_dp_anal

label whore_street_sex_group_dpstand_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_standing_dp_vag", If(not "vag" in player.sex_holes and player.sex_man_amount, 100, 0)),
    ("whore_street_sex_group_standing_dp_vag_cont", If("vag" in player.sex_holes and not "ass" in player.sex_holes, 100, 0)),
    ("whore_street_sex_group_standing_dp_vag_cum_picker", If("vag" in player.sex_holes, 50, 0)),
    
    ("whore_street_sex_group_standing_dp_anal", If(not "ass" in player.sex_holes and player.sex_man_amount and player.check_anal_agree(), 100, 0)),
    ("whore_street_sex_group_standing_dp_anal_cont", If("ass" in player.sex_holes and not "vag" in player.sex_holes, 100, 0)),
    ("whore_street_sex_group_standing_dp_anal_cum_picker", If("ass" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_standing_dp_cont", If(If(all(x in ["ass", "vag"] for x in player.sex_holes)), 100, 0)),

    ("whore_street_sex_group_dp_onback_switch", If("vag" in player.sex_holes and not "ass" in player.sex_holes, 50, 0)),
    ("whore_street_sex_group_dp_doggy_switch", If("ass" in player.sex_holes and not "vag" in player.sex_holes, 50, 0)),

    ("whore_street_sex_group_plug_remove", If(acc.anus and player.sex_man_amount > 3, 25, 0)),

    ("whore_street_sex_group_watch_robin_picker", If(whore_street_sex_group_can_watch_robin(), 15, 0)),

    ("whore_street_sex_group_reset", If(player.sex_holes == [] and player.sex_man_amount, 1000, 0)),
    ])

label whore_street_sex_group_standing_dp_vag:
    $ add_to_list(player.sex_holes, "vag")
    show sb_dpstand poke forward oh with dissolve
    if "ass" in player.sex_holes:
        "With my leg already in the air from the guy ass fucking me, there is perfect access for another guy to come at me from the front."
    else:
        "One of the guys walk up to me, puts his arm around me with his hand on my arse and pulls me close."
    "I can already feel his hard cock pressing against me, and it takes no time until..."
    show sb_dpstand vag happy with dissolve
    $ player.sex_vag(tempname, quest_temp)
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_vag_cont:
    "[rlist.having_sex_action]"
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_anal:
    $ add_to_list(player.sex_holes, "ass")
    show sb_dpstand bpoke back oh with dissolve
    "[rlist.having_sex_ass_poke]"
    show sb_dpstand banal ahh with dissolve
    $ player.sex_anal(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_penetrate_ass_slow]"
    tempname.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_anal_cont:
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_cont:
    "Having a cock in both my holes gives me a sense of fullness I never feel with normal sex. I feel stretched open and complexly full up as they fuck me."
    "I am not even sure I could tell how long they fucked me like this. With my mind lost in such raw sexual lust, I was mostly a ragdoll being held upright only because I was impaled in both holes."
    "They kept a good rhythm, sometimes both entering me and sliding out at the same time, so there was a moment of total, blissful fullness followed by total emptiness and a desire to be filled again."
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_vag_cum_picker:
    $ player.sex_cum_location_offer(
    difficulty=5, choice_inside="Keep going!", choice_pullout="Not inside.",
    cum_want="whore_street_sex_group_standing_dp_vag_cum_want", 
    cum_notwant="whore_street_sex_group_standing_dp_vag_cum_notwant", 
    cum_pullout="whore_street_sex_group_standing_dp_vag_cum_pullout", 
    )

label whore_street_sex_group_standing_dp_vag_cum_want:
    $ remove_from_list(player.sex_holes, "vag")
    show sb_dpstand forward
    pc "[rlist.having_sex_pc_cum_inside_vag_want_dialogue]"
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)
    show sb_dpstand forward happy
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    "[rlist.having_sex_came_take_cock_out_vag]"
    show sb_dpstand poke with dissolve
    show sb_dpstand noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_vag_cum_notwant:
    $ remove_from_list(player.sex_holes, "vag")
    show sb_dpstand forward
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"
    $ player.sex_cum(tempname, "inside", quest_temp)

    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    show sb_dpstand oh
    tempname.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_vag_notwant_reaction]"
    pc "*Sigh*"
    "[rlist.having_sex_came_take_cock_out_vag]"
    show sb_dpstand poke with dissolve
    show sb_dpstand noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_vag_cum_pullout:
    $ remove_from_list(player.sex_holes, "vag")
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    show sb_dpstand poke back with dissolve
    $ player.sex_cum(tempname, "pullout", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_dpstand noman with dissolve
    $ npc_race_picker_1()
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_anal_cum_picker:

    jump expression WeightedChoice([
    ("whore_street_sex_group_standing_dp_ass_cum", 100),
    ("whore_street_sex_group_standing_dp_ass_cum_pullout", 75),
    ])

label whore_street_sex_group_standing_dp_ass_cum:
    $ remove_from_list(player.sex_holes, "ass")
    pc "[rlist.having_sex_yes]"
    tempname.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname, "anal", quest_temp)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    pc "[rlist.having_sex_came_inside_ass_want]"
    "[rlist.having_sex_came_take_cock_out_vag]"
    show sb_dpstand bnoman with dissolve
    $ npc_race_picker_2()
    jump whore_street_sex_group_picker

label whore_street_sex_group_standing_dp_ass_cum_pullout:
    $ remove_from_list(player.sex_holes, "ass")
    tempname.name "[rlist.having_sex_cumming_pullout_man_dialogue]"
    show sb_dpstand bpoke back with dissolve
    $ player.sex_cum(tempname, "ass", quest_temp)
    "[rlist.having_sex_cumming_pullout_action]"
    tempname.name "Ahh yes!"
    pc "[rlist.having_sex_cumming_pullout_reaction]"
    show sb_dpstand bnoman with dissolve
    $ npc_race_picker_2()
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
