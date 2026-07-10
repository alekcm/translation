
label action_wolfpack_grabbed_resist_sex_prepare_pressed:
    $ renpy.scene()
    show sb_pressed
    with vpunch
    "The guy behind me shoves me against the wall."
    if numgen():
        show sb_pressed hand
    pc "[rlist.sex_exclaim_negative]"
    $ dialogue = WeightedChoice([
    ("I am stark naked with my face pressed into the wall. There is no chance I am getting out of this now.", 1),
    ("I am forced into the wall with the guys cock pressed against my ass, ready to take his prize.", 1),
    ("The guy stands behind me chuckling, knowing he has me as he wants.", 1),
    ("I am pressed against the wall with a cock against my ass. It's only a matter of time until he gets what he wants.", 1),
    ])
    "[dialogue]"
    show sb_pressed poke with dissolve
    if not numgen(0,10):
        jump action_wolfpack_sex_resist_pressed_anal
    else:
        jump action_wolfpack_sex_resist_pressed_vag








label action_wolfpack_sex_resist_pressed_vag:
    $ dialogue = WeightedChoice([
    ("Struggle all you want.", 1),
    ("I like it when they try to get away.", 1),
    ("Come here you sneaky bitch.", 1),
    ("I'm gonna enjoy taking you like a bitch.", 1),
    ])
    wolf.name "[dialogue]"
    pc "[rlist.sex_exclaim_negative]"
    show sb_pressed sex with dissolve
    $ player.sex_vag(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_vag_forced]"
    "[rlist.having_sex_action]"
    "[rlist.having_sex_action_struggle_pretend]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_resist_pressed_vag_cum

label action_wolfpack_sex_resist_pressed_vag_cum:
    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_action_struggle_pretend]"
    $ player.sex_cum(wolf, "inside", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_vag_notwant_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_pressed poke with dissolve
    show sb_pressed noman with dissolve
    jump action_wolfpack_sex_resist_pressed_end



label action_wolfpack_sex_resist_pressed_anal:
    $ dialogue = WeightedChoice([
    ("Struggle all you want.", 1),
    ("I like it when they try to get away.", 1),
    ("Come here you sneaky bitch.", 1),
    ("I'm gonna enjoy taking you like a bitch.", 1),
    ])
    wolf.name "[dialogue]"
    pc "[rlist.sex_exclaim_negative]"
    show sb_pressed anal with dissolve
    $ player.sex_anal(wolf, quest_wolfgang)
    "[rlist.having_sex_penetrate_ass_forced]"
    pc "[rlist.having_sex_nng]"
    "[rlist.having_sex_action_ass]"
    "[rlist.having_sex_action_struggle_pretend]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    jump action_wolfpack_sex_resist_pressed_anal_cum

label action_wolfpack_sex_resist_pressed_anal_cum:
    "[rlist.having_sex_man_close]"
    "[rlist.having_sex_action_struggle_pretend]"
    $ player.sex_cum(wolf, "anal", quest_wolfgang)
    "[rlist.having_sex_cumming_inside_ass_notwant_action]"
    wolf.name "[rlist.sex_exclaim_wolfman]"
    wolf.name "[rlist.foreplay_goodbitch_comment]"
    show sb_pressed poke with dissolve
    jump action_wolfpack_sex_resist_pressed_end

label action_wolfpack_sex_resist_pressed_end:
    $ player.grope_end()
    hide sb_pressed
    show sb_doggy1 ah
    with dissolve
    "With him done, I fall to my knees to catch my breath."
    if not numgen(0,8):
        $ npc_race_picker()
        "With the stray having got what he wanted and lost interest in me, I try to get up and get away."
        $ renpy.scene()
        show sb_onbelly back worried oh assjob
        with hpunch
        "But I am too slow and am pounced on by some other horny mutt."
        show sb_onbelly poke with dissolve
        if not numgen(0,10):
            jump action_wolfpack_sex_resist_onbelly_anal
        else:
            jump action_wolfpack_sex_resist_onbelly_vag
    else:
        "With the stray having got what he wanted and lost interest in me, I get up and get away from him."
        hide sb_pressed with dissolve
        jump action_wolfpack_sex_end

label action_wolfpack_sex_pressed_end:
    $ player.grope_end()
    hide sb_pressed
    show sb_doggy1 ah
    with dissolve
    "With him done, I fall to my knees to catch my breath."
    if not numgen(0,8):
        "With the stray having got what he wanted and lost interest in me, I hang around a little to see if any others want a turn."
        $ renpy.scene()
        show sb_onbelly back worried oh
        with hpunch
        "And it seems one horny dog does want."
        $ npc_race_picker()
        jump action_wolfpack_grabbed_sex_prepare_onbelly
    else:
        "With the stray having got what he wanted and lost interest in me, I hang around a bit to see if anyone else wants some fun."
        "But no one comes up to me, so I get back up."
        hide sb_pressed with dissolve
        jump action_wolfpack_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
