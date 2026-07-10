label action_wolfpack_grabbed_sex_prepare_mating:
    $ renpy.scene()
    show sb_matingpress happy
    with dissolve
    "[rlist.having_sex_present_onback]"
    show sb_matingpress poke down oh with dissolve
    pc "[rlist.having_sex_suprise]"
    if not numgen(0,10):
        jump action_wolfpack_sex_mating_anal
    else:
        jump action_wolfpack_sex_mating_vag








label action_wolfpack_sex_mating_vag:
    "[rlist.having_sex_tease_vag]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_matingpress vag happy with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_vag_slow]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_mating_vag_cum

label action_wolfpack_sex_mating_vag_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_matingpress up poke with dissolve
    show sb_matingpress noman neutral with dissolve
    jump action_wolfpack_sex_mating_end



label action_wolfpack_sex_mating_anal:
    "[rlist.having_sex_ass_poke]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_matingpress anal happy with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_ass_slow_pull]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_mating_anal_cum

label action_wolfpack_sex_mating_anal_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "anal", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_matingpress poke with dissolve
    show sb_matingpress noman neutral with dissolve
    jump action_wolfpack_sex_mating_end

label action_wolfpack_sex_mating_end:
    $ player.grope_end()
    "With him done, I lay there presenting myself for any one else to have their way with me."
    if not numgen(0,8):
        "And it seems one horny dog does want."
        show sb_doggy1 poke with dissolve
        pc "[rlist.having_sex_suprise]"
        if not numgen(0,10):
            jump action_wolfpack_sex_mating_anal
        else:
            jump action_wolfpack_sex_mating_vag
    else:
        "But no one comes up to me, so I get back up."
        hide sb_matingpress with dissolve
        jump action_wolfpack_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
