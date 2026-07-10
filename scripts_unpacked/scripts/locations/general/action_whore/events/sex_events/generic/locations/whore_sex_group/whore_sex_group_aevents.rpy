






init python:
    def whore_street_sex_group_can_watch_robin():
        if robin_here() and player.sex_holes != [] and not any("robin" in holes for holes in player.sex_holes):
            return True
        else:
            return False
label whore_street_sex_group_start:
    menu:
        "Are you being forced?":
            $ player.sex_forced(tempname, quest_temp)
        "Not forced":
            $ NullAction()

    if player.beingraped:
        $ tempname = guy_gangbang_r
    else:
        $ tempname = guy_gangbang
    "This is the start where sex hasnt happened yet."
    $ player.sex_holes = []
    if not player.sex_man_amount:
        $ player.sex_man_amount = numgen(3,50)
    $ npc_race_picker()
    "Debug. there are [player.sex_man_amount] men wanting to fuck. this can be really high for testing."
    jump whore_street_sex_group_start_picker

label whore_street_sex_group_start_picker:
    $ player.sex_holes = []
    if not player.sex_man_amount:

        $ player.sex_man_amount = numgen(3,50)

    if not c.nude:
        call whore_street_sex_strip_call from _call_whore_street_sex_strip_call_5
    $ npc_race_picker()
    jump expression WeightedChoice([
    ("whore_street_sex_group_cowgirl_start_picker", If(loc_cur.loc_type == "room", 100, 0)),
    ("whore_street_sex_group_onback_start_picker", If(loc_cur.loc_type == "room", 100, 0)),
    ("whore_street_sex_group_bukkake_start_picker", 100),
    ("whore_street_sex_group_dpstand_start_picker", 50),
    ("whore_street_sex_group_spitroast_doggy_start_picker", 75),
    ("whore_street_sex_group_onfours_start_picker", If(not loc_cur.loc_type in ("conc","tile"), 75, 0)),
    ("whore_street_sex_group_matingpress_start_picker", If(not loc_cur.loc_type in ("conc","tile"), 75, 0)),
    ("whore_street_sex_group_standassup_start_picker", 75),
    ])

label whore_street_sex_group_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_cowgirl_picker", If(renpy.showing("sb_ontop"), 100, 0)),
    ("whore_street_sex_group_onback_picker", If(renpy.showing("sb_onback"), 100, 0)),
    ("whore_street_sex_group_bukkake_picker", If(renpy.showing("sb_blowjob"), 100, 0)),
    ("whore_street_sex_group_spitroast_doggy_picker", If(renpy.showing("sb_doggy1"), 100, 0)),
    ("whore_street_sex_group_spitroast_assup_picker", If(renpy.showing("sb_layblow"), 100, 0)),
    ("whore_street_sex_group_onbelly_picker", If(renpy.showing("sb_onbelly"), 100, 0)),
    ("whore_street_sex_group_dpstand_picker", If(renpy.showing("sb_dpstand"), 100, 0)),
    ("whore_street_sex_group_onfours_picker", If(renpy.showing("sb_onfours"), 100, 0)),
    ("whore_street_sex_group_standbehind_picker", If(renpy.showing("sb_standbehind"), 100, 0)),

    ("whore_street_sex_group_matingpress_picker", If(renpy.showing("sb_matingpress"), 100, 0)),
    ("whore_street_sex_group_standassup_picker", If(renpy.showing("sb_standassup"), 100, 0)),

    ("whore_street_sex_end", If(player.sex_man_amount <= 0 and player.sex_holes == [], 1000000, 0)), 
    ])





label whore_street_sex_group_reset:
    if not player.beingraped:
        "The guys are taking a break so I reposition myself."
    $ renpy.scene()
    with dissolve
    if player.beingraped:
        "I try to run away but someone catches me."
    jump whore_street_sex_group_start_picker

label whore_street_sex_group_spank:
    $ player.spank()
    pc "[rlist.sex_exclaim_like]"
    $ player.spank()
    tempname.name "[rlist.sex_exclaim_like_reply]"
    pc "[rlist.sex_exclaim_more]"
    $ player.spank()
    jump whore_street_sex_group_picker

label whore_street_sex_group_sexytalk:
    tempname.name "[rlist.having_sex_man_dirtytalk]"
    pc "[rlist.having_sex_yes]"
    pc "[rlist.having_sex_yes]"
    jump whore_street_sex_group_picker

label whore_street_sex_group_beat:
    $ player.punch()
    pc "Ahhh!"
    $ player.punch()
    pc "Stop! It hurts!"
    jump whore_street_sex_group_picker

label whore_street_sex_group_plug_remove:
    tempname.name "So many people waiting their turn and you have a hole plugged up?"
    "He reaches round and tugs at the plug in my ass."
    show screen sex_action_flash("anal")
    $ acc.anus = 0
    $ player.face_shock()
    with grope_trans
    pc "Ai! More gentle next time."
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
