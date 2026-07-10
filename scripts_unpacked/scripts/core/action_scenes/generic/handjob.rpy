image sb_handjob_bg_layer:
    "sb_handjob_bg_" + loc_cur.loc_type

image sb_handjob_body_base_layer:
    "sb_handjob_body_base"
    skin_base_colour_transform()
image sb_handjob_body_shad_layer:
    "sb_handjob_body_shad"
    skin_shad_colour_transform()
image sb_handjob_body_hairshad_layer:
    "sb_handjob_body_hairshad_" + str(player.hair_fringe)
    skin_shad_colour_transform()
image sb_handjob_freckles_layer:
    "sb_handjob_freckles"
    skin_shad_colour_transform()

image sb_handjob_hand_base_layer:
    "sb_handjob_hand_base"
    skin_base_colour_transform()
image sb_handjob_hand_shad_layer:
    "sb_handjob_hand_shad"
    skin_shad_colour_transform()
image sb_handjob_hand_nails_layer:
    "sb_handjob_hand_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_handjob_handballs_base_layer:
    "sb_handjob_handballs_base"
    skin_base_colour_transform()
image sb_handjob_handballs_shad_layer:
    "sb_handjob_handballs_shad"
    skin_shad_colour_transform()
image sb_handjob_handballs_nails_layer:
    "sb_handjob_handballs_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_handjob_hair_back_4 = "sb_handjob_hair_back_3"
image sb_handjob_hair_back_bun_2 = "sb_handjob_hair_back_tied"
image sb_handjob_hair_back_bun_3 = "sb_handjob_hair_back_tied"
image sb_handjob_hair_back_bun_4 = "sb_handjob_hair_back_tied"
image sb_handjob_hair_back_pony_2 = "sb_handjob_hair_back_tied"
image sb_handjob_hair_back_pony_3 = "sb_handjob_hair_back_tied"
image sb_handjob_hair_back_pony_4 = "sb_handjob_hair_back_tied"

image sb_handjob_hair_back_layer:
    get_hair_back_cg_filename("sb_handjob_hair_back")
    hair_colour_transform()


image sb_handjob_mouth_neutral_lipstick_layer:
    "sb_handjob_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_handjob_mouth_shock_lipstick_layer:
    "sb_handjob_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_handjob_mouth_frown_lipstick_layer:
    "sb_handjob_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))


image sb_handjob_man_base_layer:
    "sb_handjob_man_base"
    npc_skin_base_colour_transform()
image sb_handjob_man_shad_layer:
    "sb_handjob_man_shad"
    npc_skin_shad_colour_transform()
image sb_handjob_man_top_shad_layer:
    "sb_handjob_man_top_shad"
    npc_skin_shad_colour_transform()

image sb_handjob_base_layer:
    "sb_handjob_base"
    skin_base_colour_transform()
image sb_handjob_shad_layer:
    "sb_handjob_shad"
    skin_shad_colour_transform()








image sb_handjob_makeup_eyeshadow_layer:
    "sb_handjob_makeup_eyeshadow"
    eyeshadow_colour_transform()
image sb_handjob_blush_layer:
    "sb_handjob_blush"
    blush_opacity_transform()


image sb_handjob_eye_iris_up_layer:
    "sb_handjob_eye_iris_up"
    eye_colour_transform()
image sb_handjob_eye_iris_down_layer:
    "sb_handjob_eye_iris_down"
    eye_colour_transform()

image sb_handjob_eyeliner_up_layer:
    "sb_handjob_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_handjob_eyeliner_down_layer:
    "sb_handjob_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")




image sb_handjob_brow_straight_layer:
    "sb_handjob_brow_straight"
    hair_colour_transform()
image sb_handjob_brow_worried_layer:
    "sb_handjob_brow_worried"
    hair_colour_transform()
image sb_handjob_brow_happy_layer:
    "sb_handjob_brow_happy"
    hair_colour_transform()

image sb_handjob_hair_front_layer:
    get_hair_front_cg_filename("sb_handjob_hair_front")
    hair_colour_transform()

image sb_handjob_effect_rain_loop:
    "sb_handjob_effect_rain1"
    .03
    "sb_handjob_effect_rain2"
    .03
    "sb_handjob_effect_rain3"
    .03
    repeat

layeredimage sb_handjob:

    always:
        "sb_handjob_bg_layer"

    always:
        "sb_handjob_body_base_layer"
    if player.hair_fringe > 0:
        "sb_handjob_body_hairshad_layer"
    always:
        "sb_handjob_body_shad_layer"
    if skin_effect.face:
        "sb_handjob_freckles_layer"
    always "sb_handjob_blush_layer"

    always:
        "sb_handjob_hair_back_layer"

    if writing.face:
        "sb_handjob_writing_face"
    if writing.forehead:
        "sb_handjob_writing_forehead"
    if writing.special == "glasses":
        "sb_handjob_writing_glasses"

    group mouth:
        attribute neutral default:
            "sb_handjob_mouth_neutral_lipstick_layer"
        attribute neutral default:
            "sb_handjob_mouth_neutral"

        attribute frown:
            "sb_handjob_mouth_frown_lipstick_layer"
        attribute frown:
            "sb_handjob_mouth_frown"

        attribute shock:
            "sb_handjob_mouth_shock_lipstick_layer"
        attribute shock:
            "sb_handjob_mouth_shock"





    if acc.eyeshadow and acc.makeup_on:
        "sb_handjob_makeup_eyeshadow_layer"
    group brow:
        attribute straight default:
            "sb_handjob_brow_straight_layer"
        attribute worried:
            "sb_handjob_brow_worried_layer"
        attribute angry:
            "sb_handjob_brow_angry_layer"

    group eyes:
        attribute up default:
            "sb_handjob_eye_iris_up_layer"
        attribute up default:
            "sb_handjob_eye_eye_up"
        attribute up default:
            "sb_handjob_eyeliner_up_layer"


        attribute down:
            "sb_handjob_eye_iris_down_layer"
        attribute down:
            "sb_handjob_eye_eye_down"
        attribute down:
            "sb_handjob_eyeliner_down_layer"


    always:
        "sb_handjob_hair_front_layer"

    always:
        "sb_handjob_man_base_layer"
    always:
        "sb_handjob_man_shad_layer"
    group man_top:
        attribute topon default:
            "sb_handjob_man_top_shad_layer"
        attribute topon default:
            "sb_handjob_man_top"
        attribute notop:
            null

    group hand:
        attribute nohand:
            null
        attribute mast default:
            "sb_handjob_hand_base_layer"
        attribute mast default:
            "sb_handjob_hand_shad_layer"
        attribute mast default:
            "sb_handjob_hand_nails_layer"

        attribute ballrub :
            "sb_handjob_handballs_base_layer"
        attribute ballrub :
            "sb_handjob_handballs_shad_layer"
        attribute ballrub :
            "sb_handjob_handballs_nails_layer"

    if player.cum_locations["cum_hand"]:
        "sb_handjob_cum_penis"
    if player.cum_locations["cum_hand"]:
        if_any "mast" "sb_handjob_cum_hand"

    group showerg:
        attribute no_shower default:
            null
        attribute shower:
            "sb_handjob_effect_rain_loop"
        attribute shower:
            "sb_handjob_effect_steam"
    always:
        "sb_handjob_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
