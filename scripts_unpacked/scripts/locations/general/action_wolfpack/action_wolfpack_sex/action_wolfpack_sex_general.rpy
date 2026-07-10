init python:
    def action_wolfpack_grabbed_strip_function():
        if not c.nude:
            player.grope(strip=True)
            if not c.nude:
                renpy.pause(0.5)
                action_wolfpack_grabbed_strip_function()
        else:
            return

label action_wolfpack_grabbed:
    $ npc_race_picker()
    $ player.face_shock()
    show sb_standbehind ah with hpunch
    wolf.name "Gotcha!"
    if player.check_nowill() or player.has_perk([perk_bambi, perk_meek, perk_broken], notif=True) or player.check_victim():
        jump action_wolfpack_grabbed_submit
    else:
        menu:
            "Feign resistance":
                jump action_wolfpack_grabbed_resist
            "Submit":
                jump action_wolfpack_grabbed_submit

label action_wolfpack_grabbed_strip_call:
    wolf.name "Get this stuff off you!"
    $ action_wolfpack_grabbed_strip_function()
    $ player.face_shock()
    return

label action_wolfpack_grabbed_resist:
    $ dialogue = WeightedChoice([
    ("I try to worm my way out of the guys grasp.", 1),
    ("I struggle against the guy and try to get away.", 1),
    ("I try to squeeze my way out of the guys grasp.", 1),
    ("I wiggle and try to get away from the guy grabbing me.", 1),
    ])
    "[dialogue]"
    if player.check_fight(4, can_spray=False):
        $ player.grope_end()
        $ renpy.scene()
        with hpunch
        $ dialogue = WeightedChoice([
        ("I manage to shake the guy off and slip out of his grasp. Realising I got away, the guy slinks back into the bushes.", 1),
        ("I manage to escape the guys grasp. Instead of chasing me though, he runs off back into the bushes.", 1),
        ("I manage to worm my way out of his grasp and looking back as I run, I realise he is not following and instead backing up into the bushes.", 1),
        ("I escape the guys grasp and run away, creating some distance between us. When I look back the guy is no where to be seen.", 1),
        ])
        "[dialogue]"
        $ dialogue = WeightedChoice([
        ("Phew!", 1),
        ("Ha, can't catch me!", 1),
        ("Woof!", 1),
        ("Shoo doggy!.", 1),
        ])
        pc "[dialogue]"
        jump travel
    else:

        with hpunch
        $ dialogue = WeightedChoice([
        ("But I don't manage to get away.", 1),
        ("But I don't manage to escape the guy, who keeps holding onto me.", 1),
        ("The guy managed to keep hold of me as I struggle and I am unable to get away from him.", 1),
        ("The guy keeps a firm grip on me and I am not able to escape.", 1),
        ])
        "[dialogue]"
        jump action_wolfpack_grabbed_resist_sex_prepare_picker

label action_wolfpack_grabbed_resist_sex_prepare_picker:
    if not c.nude:
        $ pc_strip()
    $ player.grope_end()
    jump expression WeightedChoice([
    ("action_wolfpack_grabbed_resist_sex_prepare_doggy", 100),
    ("action_wolfpack_grabbed_resist_sex_prepare_onbelly", 100),
    ("action_wolfpack_grabbed_resist_sex_prepare_pressed", 100),
    ])

label action_wolfpack_grabbed_submit:
    show sb_standbehind happy
    $ dialogue = WeightedChoice([
    ("Having been caught, I show I am happy to go along with whatever this stray hound wants.", 1),
    ("Since I am in the guys arms, I wiggle my ass to show I am willing to submit to him.", 1),
    ("Caught in the guys arms, I press my ass against him, showing my eagerness for him to take me as his bitch.", 1),
    ("I have been caught, so now it's time to show what a bitch I am.", 1),
    ])
    "[dialogue]"
    $ player.grope_end()
    jump action_wolfpack_grabbed_submit_sex_prepare_picker

label action_wolfpack_grabbed_submit_sex_prepare_picker:
    if not c.nude:
        call action_wolfpack_grabbed_strip_call from _call_action_wolfpack_grabbed_strip_call
    jump expression WeightedChoice([
    ("action_wolfpack_grabbed_sex_prepare_doggy", 100),
    ("action_wolfpack_grabbed_sex_prepare_bridge", 100),
    ("action_wolfpack_grabbed_sex_prepare_mating", 100),
    
    
    ])

label action_wolfpack_sex_end:
    pc "*Phew*"
    $ player.face_neutral()
    if event_end_interrupt_label:
        jump expression event_end_interrupt_label

    if dis(dis_misc):
        if not loc_from in dis_misc.locs:
            $ walk(loc_from)
        else:
            $ walk(dis_cur.hub)

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
