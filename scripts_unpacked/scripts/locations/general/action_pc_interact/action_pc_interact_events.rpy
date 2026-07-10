label action_pc_interact_eye_tombola:
    jump expression WeightedChoice([

    ("action_pc_interact_eye_flies", 100),

    ])

label action_pc_interact_eye_flies:
    pcm "Ugh!"
    $ player.face_annoyed()
    pcm "Damn flies getting in my face or something."
    jump travel

label action_pc_interact_breasts_tombola:
    jump expression WeightedChoice([

    ("action_pc_interact_breasts_shoo", If(not player.check_horny(), 100, 0)),
    ("action_pc_interact_breasts_strip", If(not player.check_horny(extreme=True), 100, 0)),

    ("travel", 1), 

    ])

label action_pc_interact_breasts_shoo:
    pcm "Ugh!"
    $ player.face_annoyed()
    $ player.eye = 5
    pc "Shoo!"
    jump travel

label action_pc_interact_breasts_strip:
    $ player.eye = 5
    pcm "Right... Okay."
    $ pc_strip_upper(True, True)
    pcm "There we go."
    jump travel

label action_pc_interact_vag_tombola:
    jump expression WeightedChoice([

    ("action_pc_interact_vag_mast", If(not player.check_horny(extreme=True), 100, 0)),

    ("travel", 1), 

    ])

label action_pc_interact_vag_mast:
    $ player.eye = 5
    pause 0.3
    $ player.eye = 6
    pause 0.3
    $ player.eye = 1
    jump random_event_generic_desirenocontrol
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
