
label action_wolfpack_grabbed_resist_sex_prepare_onbelly:
    $ renpy.scene()
    show sb_onbelly oh worried back
    with vpunch
    "The guy behind me presses his knee into the back of mine, making me fall over."
    pc "[rlist.sex_exclaim_negative]"
    $ dialogue = WeightedChoice([
    ("I am stark naked and forced onto the ground. There is no chance I am getting out of this now.", 1),
    ("I am forced on the grass and the guy stands over me, ready to take his prize.", 1),
    ("The guy stands over me with a grin, knowing he has me as he wants.", 1),
    ("I am face down in the grass, with my ass in the air and the guy standing over me. It's only a matter of time until he gets what he wants.", 1),
    ])
    "[dialogue]"
    show sb_onbelly poke with dissolve
    if not numgen(0,10):
        jump action_wolfpack_sex_resist_onbelly_anal
    else:
        jump action_wolfpack_sex_resist_onbelly_vag

label action_wolfpack_grabbed_sex_prepare_onbelly:
    $ renpy.scene()
    show sb_onbelly oh back
    with dissolve
    "[rlist.having_sex_present_onbelly]"
    show sb_onbelly poke with dissolve
    pc "[rlist.having_sex_suprise]"
    if not numgen(0,10):
        jump action_wolfpack_sex_onbelly_anal
    else:
        jump action_wolfpack_sex_onbelly_vag







label action_wolfpack_sex_resist_onbelly_vag:
    $ dialogue = WeightedChoice([
    ("Struggle all you want.", 1),
    ("I like it when they try to get away.", 1),
    ("Come here you sneaky bitch.", 1),
    ("I'm gonna enjoy taking you like a bitch.", 1),
    ])
    wolf.name "[dialogue]"
    pc "[rlist.sex_exclaim_negative]"
    show sb_onbelly sex ag up with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_vag_forced]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action_struggle_pretend]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_resist_onbelly_vag_cum

label action_wolfpack_sex_resist_onbelly_vag_cum:
    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_action_struggle_pretend]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_onbelly poke back neutral with dissolve
    show sb_onbelly noman with dissolve
    jump action_wolfpack_sex_resist_onbelly_end

label action_wolfpack_sex_onbelly_vag:
    "[rlist.having_sex_tease_vag]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_onbelly vag with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_vag_slow_pull]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_onbelly_vag_cum

label action_wolfpack_sex_onbelly_vag_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_vag_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_onbelly poke with dissolve
    show sb_onbelly noman with dissolve
    jump action_wolfpack_sex_resist_onbelly_end



label action_wolfpack_sex_resist_onbelly_anal:
    $ dialogue = WeightedChoice([
    ("Struggle all you want.", 1),
    ("I like it when they try to get away.", 1),
    ("Come here you sneaky bitch.", 1),
    ("I'm gonna enjoy taking you like a bitch.", 1),
    ])
    wolf.name "[dialogue]"
    pc "[rlist.sex_exclaim_negative]"
    show sb_onbelly sex with dissolve
    $ player.sex_anal(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_ass_forced]"
    pc "[rlist.having_sex_nng]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_action_struggle_pretend]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_resist_onbelly_anal_cum

label action_wolfpack_sex_resist_onbelly_anal_cum:
    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_action_struggle_pretend]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_ass_notwant_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_onbelly poke with dissolve
    show sb_onbelly noman with dissolve
    jump action_wolfpack_sex_resist_onbelly_end

label action_wolfpack_sex_onbelly_anal:
    "[rlist.having_sex_ass_poke]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    pc "[rlist.sex_exclaim_like]"
    show sb_onbelly sex with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_ass_slow_pull]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_enjoy]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_onbelly_anal_cum

label action_wolfpack_sex_onbelly_anal_cum:
    "[rlist.having_sex_man_close]"
    $ player.sex_cum(wolf, "anal", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_ass_want_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_onbelly poke with dissolve
    show sb_onbelly noman with dissolve
    jump action_wolfpack_sex_resist_onbelly_end

label action_wolfpack_sex_resist_onbelly_end:
    $ player.grope_end()
    "With the stray having got what he wanted and lost interest in me, I get up and get away from him."
    hide sb_onbelly with dissolve
    jump action_wolfpack_sex_end

label action_wolfpack_sex_onbelly_end:
    $ player.grope_end()
    "With the stray having got what he wanted and lost interest in me, I hang around a bit to see if anyone else wants some fun."
    "But no one comes up to me, so I get back up."
    hide sb_onbelly with dissolve
    jump action_wolfpack_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
