label whore_bed_sex_vag_position_switch:
    jump expression WeightedChoice([
    ("whore_bed_sex_cowgirl_switch", If(renpy.showing(["sb_cowgirl", "sb_sb_ontop lay"]))),
    ("whore_bed_sex_onback_switch", 50),
    ])

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
