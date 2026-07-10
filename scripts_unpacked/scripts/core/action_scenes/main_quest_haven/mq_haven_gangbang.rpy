image haven_gangbang_spank_layer:
    "haven_gangbang_spank"
    opacity_transform(bruise.ass)

image haven_gangbang_writing_anal_layer:
    "haven_gangbang_writing_anal"
    writing_transform("anus")
image haven_gangbang_writing_counter_layer:
    "haven_gangbang_writing_counter"
    writing_transform("ass")



layeredimage haven_gangbang_plug:  
    always:
        "haven_gangbang_bgnoman"
    if bruise.chest:
        "haven_gangbang_bruise"
    always:
        "haven_gangbang_spank_layer"

    if writing.ass:
        "haven_gangbang_writing_counter_layer"
    if writing.anus:
        "haven_gangbang_writing_anal_layer"

    group plug:
        attribute plugin default:
            "haven_gangbang_pc_plug"
        attribute plugpull:
            "haven_gangbang_pc_plug"
        attribute plugpull:
            "haven_gangbang_pc_plughand"
        attribute noplug:
            null

    always:
        "haven_gangbang_frame"

layeredimage haven_gangbang:

    if loc_cur == loc_haven_bed:
        "haven_gangbang_bg_bunk"
    else:
        "haven_gangbang_bg_bed"

    always:
        "haven_gangbang_main"
    group anal:
        attribute anal:
            "haven_gangbang_anal_shad"

    if bruise.chest:
        "haven_gangbang_bruise"
    always:
        "haven_gangbang_spank_layer"

    if writing.ass:
        "haven_gangbang_writing_counter_layer"
    if writing.anus:
        "haven_gangbang_writing_anal_layer"

    if c.socks:
        "haven_gangbang_pc_clothes"

    group plug:
        attribute plugin default:
            "haven_gangbang_pc_plug"
        attribute plugpull:
            "haven_gangbang_pc_plug"
        attribute plugpull:
            "haven_gangbang_pc_plughand"
        attribute noplug:
            null

    group manblow:
        attribute noblow default:
            null
        attribute manblow if_any "down":
            "haven_gangbang_blow_penisdown"
        attribute manblow if_any "blow":
            null
        attribute manblow:
            "haven_gangbang_blow_man"


    group head:
        attribute down default:
            "haven_gangbang_pc_headdown"
        attribute blow:
            "haven_gangbang_pc_headblow"

    group anal:
        attribute noanal default:
            null
        attribute anal:
            "haven_gangbang_anal_man"

    group penis:
        attribute penisup :  
            "haven_gangbang_lay_up"
        attribute penisvag default:
            "haven_gangbang_lay_vag"
        attribute penisanal:
            "haven_gangbang_lay_anal"

    group plug:
        attribute plugpull:
            "haven_gangbang_pc_plughand"


    always:
        "haven_gangbang_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
