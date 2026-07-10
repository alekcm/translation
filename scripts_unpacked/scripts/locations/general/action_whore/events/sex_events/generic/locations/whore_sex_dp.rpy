label whore_street_sex_dp_bed_start:
    "I lay the guy on the bed and get on top of him."
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["sb_ontop lay down happy", "sb_dpbed poke"]))
    with dissolve
    "I rub my his cock against my pussy. Since his friend is better positioned for my ass, I get ready to slip him in my pussy."
    $ if_showing("sb_dpbed", "vag")
    $ player.sex_vag(tempname, quest_temp)
    $ player.face_excited()
    "[rlist.having_sex_action_cowgirl]"

    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_4

    "[rlist.having_sex_enjoy_cowgirl]"
    $ if_showing("sb_ontop", "doggy back", "sb_dpbed", "bpoke")
    pc "Oh, decided to join us?"
    tempname2.name "Sexy ass."

    $ player.sex_anal(tempname, quest_temp)
    $ if_showing("sb_dpbed", "banal")
    $ player.face_excited()

    "[rlist.having_sex_penetrate_ass_slow]"
    tempname2.name "Ahhhhhh so warm."
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_action_ass]"
    "Having a cock in both my holes gives me a sense of fullness I never feel with normal sex. I feel stretched open and complexly full up as they fuck me."
    "I am not even sure I could tell how long they fucked me like this. With my mind lost in such raw sexual lust, I was mostly a ragdoll being held upright only because I was impaled in both holes."
    "They kept a good rhythm, sometimes both entering me and sliding out at the same time, so there was a moment of total, blissful fullness followed by total emptiness and a desire to be filled again."
    pc "[rlist.having_sex_yes]"
    if not numgen(0,10):
        call whore_street_sex_standing_spank_call from _call_whore_street_sex_standing_spank_call_5
    pc "I can't believe how much you are both filling me up!"
    $ player.spank()
    pc "[rlist.having_sex_yes]"
    jump expression WeightedChoice([
    ("whore_street_sex_dp_bed_cum_vag_first", 1),
    ("whore_street_sex_dp_bed_cum_ass_first", 1),
    ])

label whore_street_sex_dp_bed_cum_vag_first:
    tempname.name "[rlist.having_sex_man_cum_inside_vag_dialogue]"

    $ player.sex_cum(tempname, "inside", quest_temp)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_came_inside_vag_want]"
    tempname.name "[rlist.sex_end_man_tired]"
    $ if_showing("sb_dpbed", "poke")
    "[rlist.having_sex_came_take_cock_out_vag]"
    pc "You still going at it in my arse?"
    pc "[rlist.having_sex_yes]"
    $ player.spank()
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname2.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname2, "anal", quest_cleaner)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname2.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    $ if_showing("sb_dpbed", "bpoke")
    $ renpy.show(renpy.random.choice(["sb_ontop no_doggy", "sb_dpbed b_noman"]))
    jump whore_street_sex_dp_bed_end

label whore_street_sex_dp_bed_cum_ass_first:
    pc "[rlist.having_sex_pc_cum_inside_ass_want_dialogue]"
    pc "[rlist.having_sex_yes]"
    tempname2.name "[rlist.having_sex_man_cum_inside_ass_dialogue]"
    $ player.sex_cum(tempname2, "anal", quest_cleaner)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    tempname2.name "Ahh yes."
    pc "[rlist.having_sex_came_inside_ass_want]"
    $ if_showing("sb_dpbed", "bpoke")
    $ renpy.show(renpy.random.choice(["sb_ontop no_doggy", "sb_dpbed b_noman"]))
    "With the cock in my arse gone, I keep riding the guy below me."
    "[rlist.having_sex_action_cowgirl_continue]"
    "[rlist.having_sex_enjoy]"
    $ player.face_orgasm()
    pc "[rlist.having_sex_yes]"
    "[rlist.having_sex_man_close]"
    tempname.name "[rlist.having_sex_man_close_dialogue]"
    jump whore_bed_sex_cowgirl_vag_cum_picker

label whore_street_sex_dp_bed_end:
    pc "Haaaa..."
    $ renpy.scene()
    with dissolve
    "I lift myself off the guy and try to catch my breath. It's not easy with both holes sore and leaking cum."
    pc "*Phew*"
    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
