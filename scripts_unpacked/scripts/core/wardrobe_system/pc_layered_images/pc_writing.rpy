image writing_belly_layer:
    get_skin_filename("writing_belly", True)
    writing_transform("belly")
image writing_pubic_layer:
    get_skin_filename("writing_pubic", True)
    writing_transform("pubic")

image writing_chest_layer:
    "writing_chest"
    writing_transform("chest")
image writing_forehead_layer:
    "writing_forehead"
    writing_transform("forehead")
image writing_face_layer:
    "writing_face"
    writing_transform("face")
image writing_lleg_layer:
    "writing_lleg"
    writing_transform("lleg")
image writing_glasses_layer:
    "writing_glasses"
    writing_transform("special")

layeredimage pc_writing_face:
    if writing.forehead:
        "writing_forehead_layer"
    if writing.face:
        "writing_face_layer"
    if writing.special == "glasses":
        "writing_glasses_layer"

layeredimage pc_writing_body:

    if writing.pubic:
        "writing_pubic_layer"
    if writing.lleg:
        "writing_lleg_layer"
    if writing.chest:
        "writing_chest_layer"
    if writing.belly:
        "writing_belly_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
