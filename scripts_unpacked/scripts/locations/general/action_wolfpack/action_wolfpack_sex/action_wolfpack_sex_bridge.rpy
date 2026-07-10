label action_wolfpack_grabbed_sex_prepare_bridge:
    $ renpy.scene()
    show sb_standassup happy
    with dissolve
    "[rlist.having_sex_present_standassup]"
    show sb_standassup poke down with dissolve
    pc "[rlist.having_sex_suprise]"
    if not numgen(0,10):
        jump action_wolfpack_sex_bridge_anal
    else:
        jump action_wolfpack_sex_bridge_vag








label action_wolfpack_sex_bridge_vag:
    "[rlist.having_sex_tease_vag]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_standassup vag with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_vag_slow]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_bridge_vag_cum

label action_wolfpack_sex_bridge_vag_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_standassup poke with dissolve
    show sb_standassup noman with dissolve
    jump action_wolfpack_sex_bridge_end



label action_wolfpack_sex_bridge_anal:
    "[rlist.having_sex_ass_poke]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_standassup anal with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_ass_slow_pull]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_bridge_anal_cum

label action_wolfpack_sex_bridge_anal_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "anal", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_standassup poke with dissolve
    show sb_standassup noman with dissolve
    jump action_wolfpack_sex_bridge_end

label action_wolfpack_sex_bridge_end:
    $ player.grope_end()
    hide sb_standassup
    show sb_doggy1 ah
    with dissolve
    "With him done, I fall to my knees to catch my breath."
    if not numgen(0,8):
        "With the stray having got what he wanted and lost interest in me, I hang around a little to see if any others want a turn."
        "And it seems one horny dog does want."
        show sb_doggy1 poke with dissolve
        pc "[rlist.having_sex_suprise]"
        if not numgen(0,10):
            jump action_wolfpack_sex_doggy_anal
        else:
            jump action_wolfpack_sex_doggy_vag
    else:
        "With the stray having got what he wanted and lost interest in me, I hang around a bit to see if anyone else wants some fun."
        "But no one comes up to me, so I get back up."
        hide sb_standassup with dissolve
        jump action_wolfpack_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
