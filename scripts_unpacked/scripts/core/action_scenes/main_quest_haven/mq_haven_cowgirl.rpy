image haven_cowgirl_writing_chest_layer:
    "haven_cowgirl_writing_chest"
    writing_transform("chest")
image haven_cowgirl_writing_belly_layer:
    "haven_cowgirl_writing_belly"
    writing_transform("belly")
image haven_cowgirl_writing_pubic_layer:
    "haven_cowgirl_writing_pubic"
    writing_transform("pubic")

image haven_cowgirl = LayeredImageProxy("haven_cowgirl_layer", Transform(xalign = (0.75)))

layeredimage haven_cowgirl_layer:  

    if loc_cur == loc_haven_bed:
        "haven_cowgirl_bg_bunk"
    else:
        "haven_cowgirl_bg_room"

    always:
        "haven_cowgirl_base"
    if player.pregnancy == 1:
        "haven_cowgirl_belly_1"
    elif player.pregnancy == 2:
        "haven_cowgirl_belly_2"
    elif player.pregnancy == 3:
        "haven_cowgirl_belly_3"

    always:
        "haven_cowgirl_phair"
    if writing.chest:
        "haven_cowgirl_writing_chest_layer"
    if not player.pregnancy and writing.belly:
        "haven_cowgirl_writing_belly_layer"
    if not player.pregnancy and writing.pubic:
        "haven_cowgirl_writing_pubic_layer"



    if bruise.face:
        "haven_cowgirl_bruise"
    if c.socks > 0:
        "haven_cowgirl_clothes"



    group face:
        attribute happy default:
            "haven_cowgirl_happy"
        attribute stern:
            "haven_cowgirl_stern"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
