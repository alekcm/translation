label whore_street_sex_group_standbehind_picker:
    jump expression WeightedChoice([
    ("whore_street_sex_group_standing_cont", 100),
    ("whore_street_sex_group_standing_dp_switch", If("ass" in player.sex_holes, 100, 0)),
    ("whore_street_sex_group_stand_doggy_switch", If("vag" in player.sex_holes, 100, 0)),
    ])

label whore_street_sex_group_standing_cont:
    "He wraps his arms around me, still fucking me while groping my tits."
    "I have no idea what he is doing, but just go along with it. He seems to like my body being close to him."
    jump whore_street_sex_group_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
