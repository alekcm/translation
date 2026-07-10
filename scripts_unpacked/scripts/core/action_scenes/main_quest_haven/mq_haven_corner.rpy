image corner_pc_bodyfront_spank_layer:
    "corner_pc_bodyfront_spank"
    opacity_transform(bruise.ass)
image corner_pc_bodyback_spank_layer:
    "corner_pc_bodyback_spank"
    opacity_transform(bruise.ass)

image corner_pc_writing_counter_layer:
    "corner_pc_writing_counter"
    writing_transform("ass")
image corner_pc_writing_anal_layer:
    "corner_pc_writing_anal"
    writing_transform("anus")
image corner_pc_writing_pubic_layer:
    "corner_pc_writing_pubic"
    writing_transform("pubic")
image corner_pc_writing_belly_layer:
    "corner_pc_writing_belly"
    writing_transform("belly")
image corner_pc_writing_chest_layer:
    "corner_pc_writing_chest"
    writing_transform("chest")

layeredimage haven_corner man_mast: 

    always:
        "corner_bg_shower"
    always:
        "corner_man_stand_larm"
    always:
        "corner_man_stand_penis"
    always:
        "corner_man_stand_body"
    group standarm:
        attribute mast:
            "corner_man_stand_rarm_mast"
        attribute down default:
            "corner_man_stand_rarm_down"
    always:
        "corner_frame"

layeredimage haven_corner stand_facing_alone: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"

    always:
        "corner_bg_shad_faceforward"



    group pc_rarm:
        attribute up default:
            "corner_pc_rarm_up"
        attribute gropeself:
            "corner_pc_rarm_gropeself"
        attribute push:
            "corner_pc_rarm_push"
    group head:
        attribute forward default:
            "corner_pc_head_forward"
        attribute avoid:
            "corner_pc_head_avoid"
    group face:
        attribute neutral default if_all "forward":
            "corner_pc_head_forward_neutral"
        attribute neutral default if_all "avoid":
            "corner_pc_head_avoid_neutral"

        attribute happy if_all "forward":
            "corner_pc_head_forward_happy"
        attribute happy if_all "avoid":
            "corner_pc_head_avoid_happy"

        attribute ah if_all "forward":
            "corner_pc_head_forward_ah"
        attribute ah if_all "avoid":
            "corner_pc_head_avoid_ah"
    always:
        "corner_pc_bodyfront"
    always:
        "corner_pc_bodyfront_spank_layer"
    if writing.pubic:
        "corner_pc_writing_pubic_layer"
    if writing.belly:
        "corner_pc_writing_belly_layer"
    if writing.chest:
        "corner_pc_writing_chest_layer"



    group pc_larm:
        attribute down default:
            "corner_pc_larm_down"



    always:
        "corner_frame"


layeredimage haven_corner stand_facing: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"

    always:
        "corner_bg_shad_faceforward"

    always:
        "corner_man_stand_larm"

    group standpenis:
        attribute penisup:
            "corner_man_stand_penis"
        attribute penisnone:
            null
    group pc_rarm:
        attribute up default:
            "corner_pc_rarm_up"
        attribute gropeself:
            "corner_pc_rarm_gropeself"
        attribute push:
            "corner_pc_rarm_push"
    group head:
        attribute forward default:
            "corner_pc_head_forward"
        attribute avoid:
            "corner_pc_head_avoid"
    group face:
        attribute neutral default if_all "forward":
            "corner_pc_head_forward_neutral"
        attribute neutral default if_all "avoid":
            "corner_pc_head_avoid_neutral"

        attribute happy if_all "forward":
            "corner_pc_head_forward_happy"
        attribute happy if_all "avoid":
            "corner_pc_head_avoid_happy"

        attribute ah if_all "forward":
            "corner_pc_head_forward_ah"
        attribute ah if_all "avoid":
            "corner_pc_head_avoid_ah"
    always:
        "corner_pc_bodyfront"
    always:
        "corner_pc_bodyfront_spank_layer"
    if writing.pubic:
        "corner_pc_writing_pubic_layer"
    if writing.belly:
        "corner_pc_writing_belly_layer"
    if writing.chest:
        "corner_pc_writing_chest_layer"

    always:
        "corner_man_stand_body"

    group pc_larm:
        attribute down default:
            "corner_pc_larm_down"
        attribute mastman:
            "corner_pc_larm_mast"


    group standarm:
        attribute grope:
            "corner_man_stand_rarm_grope"
        attribute finger:
            "corner_man_stand_rarm_finger"
        attribute mast:
            "corner_man_stand_rarm_mast"
        attribute mandown default:
            "corner_man_stand_rarm_down"


    always:
        "corner_frame"

layeredimage haven_corner stand_facingaway_alone: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"
    always:
        "corner_bg_shad_faceback"

    always:
        "corner_pc_bodyback"
    always:
        "corner_pc_bodyback_spank_layer"
    if writing.anus:
        "corner_pc_writing_anal_layer"
    if writing.ass:
        "corner_pc_writing_counter_layer"

    group head:
        attribute back default:
            "corner_pc_head_back"
        attribute facewall:
            "corner_pc_head_wall"
    group face:
        attribute neutral default if_all "back":
            "corner_pc_head_back_neutral"
        attribute neutral default if_all "facewall":
            null

        attribute happy if_all "back":
            "corner_pc_head_back_happy"
        attribute happy if_all "facewall":
            null

        attribute ah if_all "back":
            "corner_pc_head_back_ah"
        attribute ah if_all "facewall":
            null

    always:
        "corner_frame"

layeredimage haven_corner stand_facingaway: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"
    always:
        "corner_bg_shad_faceback"

    always:
        "corner_man_stand_larm"

    always:
        "corner_pc_bodyback"
    always:
        "corner_pc_bodyback_spank_layer"
    if writing.anus:
        "corner_pc_writing_anal_layer"
    if writing.ass:
        "corner_pc_writing_counter_layer"

    group head:
        attribute back default:
            "corner_pc_head_back"
        attribute facewall:
            "corner_pc_head_wall"
    group face:
        attribute neutral default if_all "back":
            "corner_pc_head_back_neutral"
        attribute neutral default if_all "facewall":
            null

        attribute happy if_all "back":
            "corner_pc_head_back_happy"
        attribute happy if_all "facewall":
            null

        attribute ah if_all "back":
            "corner_pc_head_back_ah"
        attribute ah if_all "facewall":
            null


    group standpenis:
        attribute penisup:
            "corner_man_stand_penis"
        attribute penisnone:
            null

    always:
        "corner_man_stand_body"



    group standarm:
        attribute holdarm:
            "corner_man_stand_rarm_holdarm"
        attribute mast:
            "corner_man_stand_rarm_mast"
        attribute mandown default:
            "corner_man_stand_rarm_down"


    always:
        "corner_frame"


layeredimage haven_corner man_poke: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"
    always:
        "corner_bg_shad_faceback"

    always:
        "corner_man_poke_larm"

    always:
        "corner_pc_bodyback"
    always:
        "corner_pc_bodyback_spank_layer"
    if writing.anus:
        "corner_pc_writing_anal_layer"
    if writing.ass:
        "corner_pc_writing_counter_layer"

    group head:
        attribute back default:
            "corner_pc_head_back"
        attribute facewall:
            "corner_pc_head_wall"
    group face:
        attribute neutral default if_all "back":
            "corner_pc_head_back_neutral"
        attribute neutral default if_all "facewall":
            null

        attribute happy if_all "back":
            "corner_pc_head_back_happy"
        attribute happy if_all "facewall":
            null

        attribute ah if_all "back":
            "corner_pc_head_back_ah"
        attribute ah if_all "facewall":
            null


    group standpenis:
        attribute penisrub default:
            "corner_man_poke_penis_rub"
        attribute penisnone:
            null
        attribute penispoke:
            "corner_man_poke_penis_poke"

    always:
        "corner_man_poke_body"



    group standarm:
        attribute ass default:
            "corner_man_poke_rarmass"

        attribute tit:
            "corner_man_poke_rarmtit"


    always:
        "corner_frame"




layeredimage haven_corner man_grind: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"
    always:
        "corner_bg_shad_faceback"


    always:
        "corner_pc_bodyback"
    always:
        "corner_pc_bodyback_spank_layer"
    if writing.anus:
        "corner_pc_writing_anal_layer"
    if writing.ass:
        "corner_pc_writing_counter_layer"

    group head:
        attribute back default:
            "corner_pc_head_back"
        attribute facewall:
            "corner_pc_head_wall"
    group face:
        attribute neutral default if_all "back":
            "corner_pc_head_back_neutral"
        attribute neutral default if_all "facewall":
            null

        attribute happy if_all "back":
            "corner_pc_head_back_happy"
        attribute happy if_all "facewall":
            null

        attribute ah if_all "back":
            "corner_pc_head_back_ah"
        attribute ah if_all "facewall":
            null


    group standpenis:
        attribute penisrub default:
            "corner_man_grind_penisass"
        attribute penisnone:
            null
        attribute penispoke:
            "corner_man_grind_penisin"

    always:
        "corner_man_grind_body"



    group standarm:
        attribute ass default:
            "corner_man_grind_armhips"

        attribute tit:
            "corner_man_grind_armtits"


    always:
        "corner_frame"


layeredimage haven_corner man_sex: 

    group bg:
        attribute shower default:
            "corner_bg_shower"
        attribute wall:
            "corner_bg_wall"
    always:
        "corner_bg_shad_faceback"


    always:
        "corner_pc_bodyback"
    always:
        "corner_pc_bodyback_spank_layer"
    if writing.anus:
        "corner_pc_writing_anal_layer"
    if writing.ass:
        "corner_pc_writing_counter_layer"

    group head:
        attribute back default:
            "corner_pc_head_back"
        attribute facewall:
            "corner_pc_head_wall"
    group face:
        attribute neutral default if_all "back":
            "corner_pc_head_back_neutral"
        attribute neutral default if_all "facewall":
            null

        attribute happy if_all "back":
            "corner_pc_head_back_happy"
        attribute happy if_all "facewall":
            null

        attribute ah if_all "back":
            "corner_pc_head_back_ah"
        attribute ah if_all "facewall":
            null


    always:
        "corner_man_sex_body"



    group standarm:
        attribute reach default:
            "corner_man_sex_reachfront"

        attribute tit:
            "corner_man_sex_gropetits"


    always:
        "corner_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
