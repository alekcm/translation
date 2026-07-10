image mq01_aw_pregstate:
    "mq01_aw_preg" + str(player.pregnancy)





layeredimage mq01_aw:

    always:
        "mq01_aw_bg"
    always:
        "mq01_aw_pregstate"

    group head:
        attribute sup default:
            "mq01_aw_girl_face"
        attribute sup default:
            "mq01_aw_girl_eye_sup"
        attribute sup default:
            "mq01_aw_girl_mouth_sup"

        attribute happy:
            "mq01_aw_girl_face"
        attribute happy:
            "mq01_aw_girl_eye_happy"
        attribute happy:
            "mq01_aw_girl_mouth_happy"

        attribute cheer:
            "mq01_aw_girl_face"
        attribute cheer:
            "mq01_aw_girl_eye_cheer"
        attribute cheer:
            "mq01_aw_girl_mouth_cheer"

        attribute angry:
            "mq01_aw_girl_face"
        attribute angry:
            "mq01_aw_girl_eye_angry"
        attribute angry:
            "mq01_aw_girl_mouth_angry"

        attribute headup:
            "mq01_aw_girl_headup"

    group man:
        attribute noman:
            "mq01_aw_frame" 

        attribute grope:
            "mq01_aw_man_grope"

        attribute mast:
            "mq01_aw_man_mast"

        attribute poke:
            "mq01_aw_man_poke"

        attribute pokegrab:
            "mq01_aw_man_pokegrab"

        attribute inside:
            "mq01_aw_man_inside"


    always:
        "mq01_aw_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
