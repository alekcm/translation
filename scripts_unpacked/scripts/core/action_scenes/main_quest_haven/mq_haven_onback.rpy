image haven_onback_pc_writing_milk_layer:
    "haven_onback_pc_writing_milk"
    writing_transform("chest")
image haven_onback_pc_writing_belly_layer:
    "haven_onback_pc_writing_belly"
    writing_transform("belly")
image haven_onback_pc_writing_pubic_layer:
    "haven_onback_pc_writing_pubic"
    writing_transform("pubic")
image haven_onback_pc_writing_lleg_up_layer:
    "haven_onback_pc_writing_lleg_up"
    writing_transform("lleg")
image haven_onback_pc_writing_lleg_down_layer:
    "haven_onback_pc_writing_lleg_down"
    writing_transform("lleg")

layeredimage haven_onback:

    always:
        "haven_onback_base"

    group man_low auto:
        attribute noman default:
            null


    group pc_leg auto:
        attribute down default

    if player.cum_locations["cum_vagin"]:
        "haven_onback_pc_cum"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_belly"]: 
        "haven_onback_pc_cumb"

    if writing.chest:
        "haven_onback_pc_writing_milk_layer"
    if writing.belly:
        "haven_onback_pc_writing_belly_layer"
    if writing.pubic:
        "haven_onback_pc_writing_pubic_layer"
    if writing.lleg:
        if_any "up" "haven_onback_pc_writing_lleg_up_layer"
    if writing.lleg:
        if_any "down" "haven_onback_pc_writing_lleg_down_layer"

    group man_high auto:
        attribute noman default:
            null



    group rarm if_not "up":
        attribute pcmast :
            "haven_onback_pc_rarm_mast"
        attribute rest default:
            "haven_onback_pc_rarm_rest"

    group larm if_not "up":
        attribute breast :
            "haven_onback_pc_larm_breast"
        attribute thigh default:
            "haven_onback_pc_larm_thigh"



    group pc_face auto:
        attribute norm default
    always:
        "haven_onback_pc_hair"
    always:
        "haven_onback_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
