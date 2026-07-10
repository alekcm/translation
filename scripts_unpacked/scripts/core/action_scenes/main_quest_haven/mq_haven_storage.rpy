image haven_storage_pc_spank_layer:
    "haven_storage_pc_spank"
    opacity_transform(bruise.ass)

image haven_storage_pc_writing_ass_layer:
    "haven_storage_pc_writing_ass"
    writing_transform("ass")
image haven_storage_pc_writing_anus_layer:
    "haven_storage_pc_writing_anus"
    writing_transform("anus")

layeredimage haven_storage:

    always:
        "haven_storage_bg"

    group larm:
        attribute hold if_any "man":
            "haven_storage_man_larm_hold"
        attribute noarm default:
            null
        attribute mast if_any "man":
            "haven_storage_man_larm_mast"

    group man:
        attribute man:
            "haven_storage_man_body"
        attribute noman default:
            null

    always:
        "haven_storage_pc_body"
    always:
        "haven_storage_pc_spank_layer"
    if writing.ass:
        "haven_storage_pc_writing_ass_layer"
    if writing.anus:
        "haven_storage_pc_writing_anus_layer"

    group shorts:
        attribute shortsup default:
            "haven_storage_pc_shortsup"
        attribute shortsdown:
            "haven_storage_pc_shortsdown"
        attribute noshorts:
            null

    group head:
        attribute headup default:
            "haven_storage_pc_headup"
        attribute headdown:
            "haven_storage_pc_headdown"

    group rarm:
        attribute ass default if_any "man":
            "haven_storage_man_rarm_ass"
        attribute thigh if_any "man":
            "haven_storage_man_rarm_thigh"
        attribute finger if_any "man":
            "haven_storage_man_rarm_finger"
    always:
        "haven_storage_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
