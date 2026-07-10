image pc_bruise_belly_1 = im.Alpha("characters/pc/bruise/bruise_belly_0.webp", 0.2)
image pc_bruise_belly_2 = im.Alpha("characters/pc/bruise/bruise_belly_0.webp", 0.4)
image pc_bruise_belly_3 = im.Alpha("characters/pc/bruise/bruise_belly_0.webp", 0.6)
image pc_bruise_belly_4 = im.Alpha("characters/pc/bruise/bruise_belly_0.webp", 0.8)

image pc_bruise_face_1 = im.Alpha("characters/pc/bruise/bruise_face.webp", 0.2)
image pc_bruise_face_2 = im.Alpha("characters/pc/bruise/bruise_face.webp", 0.4)
image pc_bruise_face_3 = im.Alpha("characters/pc/bruise/bruise_face.webp", 0.6)
image pc_bruise_face_4 = im.Alpha("characters/pc/bruise/bruise_face.webp", 0.8)

image pc_bruise_chest_1 = im.Alpha("characters/pc/bruise/bruise_chest.webp", 0.2)
image pc_bruise_chest_2 = im.Alpha("characters/pc/bruise/bruise_chest.webp", 0.4)
image pc_bruise_chest_3 = im.Alpha("characters/pc/bruise/bruise_chest.webp", 0.6)
image pc_bruise_chest_4 = im.Alpha("characters/pc/bruise/bruise_chest.webp", 0.8)

image pc_bruise_spank:
    "characters/pc/bruise/bruise_ass.webp"
    opacity_transform(bruise.ass)

layeredimage pc_bruise_belly:

    if bruise.belly == 1:
        "pc_bruise_belly_1"
    elif bruise.belly == 2:
        "pc_bruise_belly_2"
    elif bruise.belly == 3:
        "pc_bruise_belly_3"
    elif bruise.belly >= 4:
        "pc_bruise_belly_4"

layeredimage pc_bruise_face:

    if bruise.face == 1:
        "pc_bruise_face_1"
    elif bruise.face == 2:
        "pc_bruise_face_2"
    elif bruise.face == 3:
        "pc_bruise_face_3"
    elif bruise.face >= 4:
        "pc_bruise_face_4"

layeredimage pc_bruise_chest:

    if bruise.chest == 1:
        "pc_bruise_chest_1"
    elif bruise.chest == 2:
        "pc_bruise_chest_2"
    elif bruise.chest == 3:
        "pc_bruise_chest_3"
    elif bruise.chest >= 4:
        "pc_bruise_chest_4"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
