image sb_assup_bg_layer:
    "sb_assup_bg_" + loc_cur.loc_type


image sb_assup_pc_body_base_layer:
    "sb_assup_pc_body_base"
    skin_base_colour_transform()
image sb_assup_pc_body_shad_layer:
    "sb_assup_pc_body_shad"
    skin_shad_colour_transform()



image sb_assup_pc_body_nails_layer:
    "sb_assup_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image sb_assup_pc_body_spank_layer:
    "sb_assup_pc_body_spank"
    opacity_transform(bruise.ass)


image sb_assup_pc_face_freckles_layer:
    "sb_assup_pc_face_freckles"
    skin_shad_colour_transform()
image sb_assup_pc_face_blush_layer:
    "sb_assup_pc_face_blush"
    blush_opacity_transform()

image sb_assup_pc_face_mouth_ag_lipstick_layer:
    "sb_assup_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_assup_pc_face_mouth_grit_lipstick_layer:
    "sb_assup_pc_face_mouth_grit_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_assup_pc_face_mouth_neutral_lipstick_layer:
    "sb_assup_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_assup_pc_face_mouth_laugh_lipstick_layer:
    "sb_assup_pc_face_mouth_laugh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_assup_pc_face_mouth_ah_lipstick_layer:
    "sb_assup_pc_face_mouth_ah_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_assup_pc_face_mouth_frown_lipstick_layer:
    "sb_assup_pc_face_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_assup_pc_face_eyeshadow_layer:
    "sb_assup_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image sb_assup_pc_face_eyeliner_closed_layer:
    "sb_assup_pc_face_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_assup_pc_face_eyeliner_up_layer:
    "sb_assup_pc_face_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_assup_pc_face_eyeliner_wink_layer:
    "sb_assup_pc_face_eyeliner_wink_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_assup_pc_face_eyeliner_squint_layer:
    "sb_assup_pc_face_eyeliner_squint_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_assup_pc_face_eyeliner_back_layer:
    "sb_assup_pc_face_eyeliner_back_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_assup_pc_face_eye_iris_up_layer:
    "sb_assup_pc_face_eye_iris_up"
    eye_colour_transform()
image sb_assup_pc_face_eye_iris_wink_layer:
    "sb_assup_pc_face_eye_iris_wink"
    eye_colour_transform()
image sb_assup_pc_face_eye_iris_squint_layer:
    "sb_assup_pc_face_eye_iris_squint"
    eye_colour_transform()
image sb_assup_pc_face_eye_iris_back_layer:
    "sb_assup_pc_face_eye_iris_back"
    eye_colour_transform()

image sb_assup_pc_face_brow_straight_layer:
    "sb_assup_pc_face_brow_straight"
    hair_colour_transform()
image sb_assup_pc_face_brow_worried_layer:
    "sb_assup_pc_face_brow_worried"
    hair_colour_transform()
image sb_assup_pc_face_brow_angry_layer:
    "sb_assup_pc_face_brow_angry"
    hair_colour_transform()
image sb_assup_pc_face_brow_happy_layer:
    "sb_assup_pc_face_brow_happy"
    hair_colour_transform()


image sb_assup_man_sex_base_layer:
    "sb_assup_man_sex_base"
    npc_skin_base_colour_transform()
image sb_assup_man_sex_shad_layer:
    "sb_assup_man_sex_shad"
    npc_skin_shad_colour_transform()

image sb_assup_man_hold_base_layer:
    "sb_assup_man_hold_base"
    npc_skin_base_colour_transform()
image sb_assup_man_hold_shad_layer:
    "sb_assup_man_hold_shad"
    npc_skin_shad_colour_transform()

image sb_assup_man_mast_base_layer:
    "sb_assup_man_mast_base"
    npc_skin_base_colour_transform()
image sb_assup_man_mast_shad_layer:
    "sb_assup_man_mast_shad"
    npc_skin_shad_colour_transform()


image sb_assup_pc_hair_back_bun_2 = "sb_assup_pc_hair_back_bun"
image sb_assup_pc_hair_back_bun_3 = "sb_assup_pc_hair_back_bun"
image sb_assup_pc_hair_back_bun_4 = "sb_assup_pc_hair_back_bun"
image sb_assup_pc_hair_back_pony_2 = "sb_assup_pc_hair_back_bun"
image sb_assup_pc_hair_back_pony_3 = "sb_assup_pc_hair_back_bun"
image sb_assup_pc_hair_back_pony_4 = "sb_assup_pc_hair_back_bun"

image sb_assup_pc_hair_back_pig_3 = "sb_assup_pc_hair_back_pig_2"

image sb_assup_pc_hair_back_4 = "sb_assup_pc_hair_back_3"

image sb_assup_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_assup_pc_hair_back")
    hair_colour_transform()

image sb_assup_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_assup_pc_hair_front")
    hair_colour_transform()

image sb_assup = LayeredImageProxy("sb_assup_layer", Transform(xalign = (0.85)))

layeredimage sb_assup_layer:  

    always:
        "sb_assup_bg_layer" 

    always:
        "sb_assup_pc_body_base_layer"  
    always:
        "sb_assup_pc_body_shad_layer"
    always:
        "sb_assup_pc_body_nails_layer"
    if skin_effect.face:
        "sb_assup_pc_face_freckles_layer"
    always "sb_assup_pc_face_blush_layer"
    always:
        "sb_assup_pc_body_spank_layer"

    if tattoo.ass:
        "sb_assup_pc_tattoo_tramp"
    if writing.face:
        "sb_assup_pc_writing_face"
    if writing.forehead:
        "sb_assup_pc_writing_forehead"
    if writing.special == "glasses":
        "sb_assup_pc_writing_glasses"

    group brow auto:
        attribute straight default:
            "sb_assup_pc_face_brow_straight_layer"
        attribute worried:
            "sb_assup_pc_face_brow_worried_layer"
        attribute angry:
            "sb_assup_pc_face_brow_angry_layer"
        attribute happy:
            "sb_assup_pc_face_brow_happy_layer"

    always:
        "sb_assup_pc_face_eyeshadow_layer"

    group eye:
        attribute up default:
            "sb_assup_pc_face_eye_iris_up_layer"
        attribute up default:
            "sb_assup_pc_face_eye_eye_up"
        attribute up default:
            "sb_assup_pc_face_eyeliner_up_layer"

        attribute closed :
            "sb_assup_pc_face_eyeliner_closed_layer"

        attribute wink:
            "sb_assup_pc_face_eye_iris_wink_layer"
        attribute wink:
            "sb_assup_pc_face_eye_eye_wink"
        attribute wink:
            "sb_assup_pc_face_eyeliner_wink_layer"

        attribute squint:
            "sb_assup_pc_face_eye_iris_squint_layer"
        attribute squint:
            "sb_assup_pc_face_eye_eye_squint"
        attribute squint:
            "sb_assup_pc_face_eyeliner_squint_layer"

        attribute back:
            "sb_assup_pc_face_eye_iris_back_layer"
        attribute back:
            "sb_assup_pc_face_eye_eye_back"
        attribute back:
            "sb_assup_pc_face_eyeliner_back_layer"

    group pc_face_mouth:
        attribute ag:
            "sb_assup_pc_face_mouth_ag_lipstick_layer"
        attribute ag:
            "sb_assup_pc_face_mouth_ag"

        attribute laugh:
            "sb_assup_pc_face_mouth_laugh_lipstick_layer"
        attribute laugh:
            "sb_assup_pc_face_mouth_laugh"

        attribute frown:
            "sb_assup_pc_face_mouth_frown_lipstick_layer"
        attribute frown:
            "sb_assup_pc_face_mouth_frown"

        attribute neutral default:
            "sb_assup_pc_face_mouth_neutral_lipstick_layer"
        attribute neutral default:
            "sb_assup_pc_face_mouth_neutral"

        attribute ah:
            "sb_assup_pc_face_mouth_ah_lipstick_layer"
        attribute ah:
            "sb_assup_pc_face_mouth_ah"

        attribute grit:
            "sb_assup_pc_face_mouth_grit_lipstick_layer"
        attribute grit:
            "sb_assup_pc_face_mouth_grit"

    if player.beingraped:
        "sb_assup_pc_face_tears"

    group man:
        attribute noman default:
            null

        attribute poke:
            "sb_assup_man_hold_base_layer"
        attribute poke:
            "sb_assup_man_hold_shad_layer"

        attribute sex:
            "sb_assup_man_sex_base_layer"
        attribute sex:
            "sb_assup_man_sex_shad_layer"

        attribute mast:
            "sb_assup_man_mast_base_layer"
        attribute mast:
            "sb_assup_man_mast_shad_layer"


    always:
        "sb_assup_pc_hair_back_layer"
    always:
        "sb_assup_pc_hair_front_layer"


    always:
        "sb_assup_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
