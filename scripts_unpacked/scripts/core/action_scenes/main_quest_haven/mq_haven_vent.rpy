layeredimage haven_vent:

    always:
        "haven_vent_bg"

    group man:
        attribute man:
            "haven_vent_man"
        attribute noman default:
            null

    always:
        "haven_vent_pc_body"

    group shorts:
        attribute shortson default:
            "haven_vent_pc_shorts"
        attribute shortsoff:
            null

    group face:
        attribute neutral default:
            "haven_vent_pc_face_neutral"
        attribute conf :
            "haven_vent_pc_face_conf"
        attribute shock:
            "haven_vent_pc_face_shock"
        attribute giveup:
            "haven_vent_pc_face_giveup"

    group tears:
        attribute tears:
            "haven_vent_pc_tears"
        attribute notears default:
            null

    always:
        "haven_vent_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
