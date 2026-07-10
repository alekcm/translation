image haven_lament_open_writing_face_layer:
    "haven_lament_open_writing_face"
    writing_transform("face")
image haven_lament_open_writing_forehead_layer:
    "haven_lament_open_writing_forehead"
    writing_transform("forehead")
image haven_lament_open_writing_chest_layer:
    "haven_lament_open_writing_chest"
    writing_transform("chest")
image haven_lament_open_writing_belly_layer:
    "haven_lament_open_writing_belly"
    writing_transform("belly")
image haven_lament_open_writing_pubic_layer:
    "haven_lament_open_writing_pubic"
    writing_transform("pubic")

image haven_lament_sleep_writing_ass_layer:
    "haven_lament_sleep_writing_ass"
    writing_transform("ass")
image haven_lament_sleep_writing_anus_layer:
    "haven_lament_sleep_writing_anus"
    writing_transform("anus")

image haven_lament_writing_ass_layer:
    "haven_lament_writing_ass"
    writing_transform("ass")
image haven_lament_writing_face_layer:
    "haven_lament_writing_face"
    writing_transform("face")
image haven_lament_writing_forehead_layer:
    "haven_lament_writing_forehead"
    writing_transform("forehead")
image haven_lament_writing_chest_layer:
    "haven_lament_writing_chest"
    writing_transform("chest")


layeredimage haven_lament:

    always:
        "haven_lament_base"
    if bruise.face > 1:
        "haven_lament_bruise"
    if writing.forehead:
        "haven_lament_writing_forehead_layer"
    if writing.face:
        "haven_lament_writing_face_layer"
    if writing.forehead:
        "haven_lament_writing_forehead_layer"
    if writing.chest:
        "haven_lament_writing_chest_layer"

layeredimage haven_lament_open:

    always:
        "haven_lament_open_base"
    if player.pregnancy == 1:
        "haven_lament_open_belly_1"
    if player.pregnancy == 2:
        "haven_lament_open_belly_2"
    if player.pregnancy == 3:
        "haven_lament_open_belly_3"

    if bruise.face:
        "haven_lament_open_bruise"
    if writing.forehead:
        "haven_lament_open_writing_forehead_layer"
    if writing.face:
        "haven_lament_open_writing_face_layer"
    if writing.chest:
        "haven_lament_open_writing_chest_layer"
    if writing.belly and not player.pregnancy:
        "haven_lament_open_writing_belly_layer"
    if writing.pubic:
        "haven_lament_open_writing_pubic_layer"

layeredimage haven_lament_sleep:

    always:
        "haven_lament_sleep_base"
    if bruise.chest and bruise.belly:
        "haven_lament_sleep_bruise"
    if writing.ass:
        "haven_lament_sleep_writing_ass_layer"
    if writing.anus:
        "haven_lament_sleep_writing_anus_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
