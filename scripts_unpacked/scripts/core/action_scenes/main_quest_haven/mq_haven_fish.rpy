image haven_fish_writing_forehead_layer:
    "haven_fish_writing_forehead"
    writing_transform("forehead")
image haven_fish_writing_face_layer:
    "haven_fish_writing_face"
    writing_transform("face")
image haven_fish_writing_chest_layer:
    "haven_fish_writing_chest"
    writing_transform("chest")
image haven_fish_writing_belly_layer:
    "haven_fish_writing_belly"
    writing_transform("belly")
image haven_fish_writing_pubic_layer:
    "haven_fish_writing_pubic"
    writing_transform("pubic")
image haven_fish_writing_lleg_layer:
    "haven_fish_writing_lleg"
    writing_transform("lleg")



layeredimage haven_fish:

    always:
        "haven_fish_base"
    if player.beingraped:
        "haven_fish_tears"
    if player.cum_locations["cum_vagin"] or player.cum_locations["cum_vagout"]:
        "haven_fish_cum"
    if writing.forehead:
        "haven_fish_writing_forehead_layer"
    if writing.face:
        "haven_fish_writing_face_layer"
    if writing.chest:
        "haven_fish_writing_chest_layer"
    if writing.belly:
        "haven_fish_writing_belly_layer"
    if writing.pubic:
        "haven_fish_writing_pubic_layer"
    if writing.lleg:
        "haven_fish_writing_lleg_layer"

    group man:
        attribute sex:
            "haven_fish_man"
        attribute nosex default:
            null
    if bruise.face > 1:
        "haven_fish_bruise"
    always:
        "haven_fish_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
