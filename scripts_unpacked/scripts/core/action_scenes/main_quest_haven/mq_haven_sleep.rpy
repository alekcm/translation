image haven_sleep_pc_body_spank_layer:
    "haven_sleep_pc_body_spank"
    opacity_transform(bruise.ass)

image haven_sleep_pc_writing_whore_layer:
    "haven_sleep_pc_writing_whore"
    writing_transform("forehead")
image haven_sleep_pc_writing_slut_layer:
    "haven_sleep_pc_writing_slut"
    writing_transform("face")
image haven_sleep_pc_writing_milk_layer:
    "haven_sleep_pc_writing_milk"
    writing_transform("chest")

layeredimage haven_sleep: 

    always:
        "haven_sleep_bg"


    group man:
        attribute penisout:
            "haven_sleep_man_nude"
        attribute penisin:
            "haven_sleep_man_nude"
        attribute clothed:
            "haven_sleep_man_sleep"
        attribute noman default:
            null


    group pc_head:
        attribute headdown default:
            "haven_sleep_pc_headdown"
        attribute gag:
            "haven_sleep_pc_headup"

    group pc_face if_any "headdown":
        attribute sleep default:
            "haven_sleep_pc_face_sleep"
        attribute conf:
            "haven_sleep_pc_face_conf"
        attribute pain:
            "haven_sleep_pc_face_pain"
        attribute peek:
            "haven_sleep_pc_face_peek"
        attribute ag:
            "haven_sleep_pc_face_ag"
        attribute happy:
            "haven_sleep_pc_face_happy"

    if writing.face:
        if_any "headdown" "haven_sleep_pc_writing_slut_layer"
    if writing.forehead:
        if_any "headdown" "haven_sleep_pc_writing_whore_layer"

    group pc_head:
        attribute headdown default:
            "haven_sleep_pc_hairdown"

    always:
        "haven_sleep_pc_body"
    always:
        "haven_sleep_pc_body_spank_layer"

    if writing.chest:
        "haven_sleep_pc_writing_milk_layer"



    if player.cum_locations["cum_vagin"]:
        "haven_sleep_pc_cum_leak"
    if player.cum_locations["cum_vagout"]:
        "haven_sleep_pc_cum_out"

    if c.bottom:
        "haven_sleep_pc_shortsup"
    else:
        "haven_sleep_pc_shortsdown"
    if c.top:
        "haven_sleep_pc_top"

    always:
        if_not ["noman", "gag"] "haven_sleep_man_grope"




    group man:
        attribute penisout:
            "haven_sleep_man_penisout"
        attribute penisin:
            "haven_sleep_man_penisin"
        attribute clothed:
            null
        attribute noman default:
            null




    always:
        "haven_sleep_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
