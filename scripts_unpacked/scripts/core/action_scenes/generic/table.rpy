image sb_table_bg_layer:
    "sb_table_bg_" + loc_cur.loc_type

image sb_table_man_hand_base_layer:
    "sb_table_man_hand_base"
    npc_skin_base_colour_transform()
image sb_table_man_hand_shad_layer:
    "sb_table_man_hand_shad"
    npc_skin_shad_colour_transform()
image sb_table_man_sex_base_layer:
    "sb_table_man_sex_base"
    npc_skin_base_colour_transform()
image sb_table_man_sex_shad_layer:
    "sb_table_man_sex_shad"
    npc_skin_shad_colour_transform()
image sb_table_man_mast_base_layer:
    "sb_table_man_mast_base"
    npc_skin_base_colour_transform()
image sb_table_man_mast_shad_layer:
    "sb_table_man_mast_shad"
    npc_skin_shad_colour_transform()





image sb_table_pc_stand_body_base_layer:
    "sb_table_pc_stand_body_base"
    skin_base_colour_transform()
image sb_table_pc_stand_body_shad_layer:
    "sb_table_pc_stand_body_shad"
    skin_shad_colour_transform()

image sb_table_pc_stand_body_preg_base_layer:
    get_skin_filename("sb_table_pc_stand_body_base_preg", True)
    skin_base_colour_transform()
image sb_table_pc_stand_body_preg_shad_layer:
    get_skin_filename("sb_table_pc_stand_body_shad_preg", True)
    skin_shad_colour_transform()

image sb_table_pc_stand_breasts_base_layer:
    get_skin_filename("sb_table_pc_stand_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_table_pc_stand_breasts_shad_layer:
    get_skin_filename("sb_table_pc_stand_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_table_pc_stand_breasts_nips_layer:
    get_skin_filename("sb_table_pc_stand_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_table_pc_stand_breasts_nipring_layer:
    get_skin_filename("sb_table_pc_stand_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_table_pc_stand_breasts_tattoo_layer:
    get_skin_filename("sb_table_pc_stand_breasts_tattoo", breasts=True)

image sb_table_pc_stand_breasts_c_base_layer:
    get_skin_filename("sb_table_pc_stand_breasts_c_base", breasts=True)
    skin_base_colour_transform()
image sb_table_pc_stand_breasts_c_shad_layer:
    get_skin_filename("sb_table_pc_stand_breasts_c_shad", breasts=True)
    skin_shad_colour_transform()
image sb_table_pc_stand_breasts_c_nips_layer:
    get_skin_filename("sb_table_pc_stand_breasts_c_nips", breasts=True)
    nipple_colour_transform()
image sb_table_pc_stand_breasts_c_tattoo_layer:
    get_skin_filename("sb_table_pc_stand_breasts_c_tattoo", breasts=True)

image sb_table_pc_stand_nails_layer:
    "sb_table_pc_stand_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_table_pc_stand_outfit_pub_breasts_layer:
    get_skin_filename("sb_table_pc_stand_outfit_pub_breasts", breasts=True)
image sb_table_pc_stand_outfit_pub_preg_layer:
    get_skin_filename("sb_table_pc_stand_outfit_pub_preg", preg=True)
image sb_table_pc_stand_outfit_dungarees_breasts_layer:
    get_skin_filename("sb_table_pc_stand_outfit_dungarees_breasts", breasts=True)
image sb_table_pc_stand_outfit_dungarees_preg_layer:
    get_skin_filename("sb_table_pc_stand_outfit_dungarees_preg", preg=True)
image sb_table_pc_stand_outfit_maid_breasts_layer:
    get_skin_filename("sb_table_pc_stand_outfit_maid_breasts", breasts=True)
image sb_table_pc_stand_outfit_maid_preg_layer:
    get_skin_filename("sb_table_pc_stand_outfit_maid_preg", preg=True)






image sb_table_pc_bentover_body_base_layer:
    "sb_table_pc_bentover_body_base"
    skin_base_colour_transform()
image sb_table_pc_bentover_body_shad_layer:
    "sb_table_pc_bentover_body_shad"
    skin_shad_colour_transform()

image sb_table_pc_bentover_body_preg_base_layer:
    get_skin_filename("sb_table_pc_bentover_body_base_preg", True)
    skin_base_colour_transform()
image sb_table_pc_bentover_body_preg_shad_layer:
    get_skin_filename("sb_table_pc_bentover_body_shad_preg", True)
    skin_shad_colour_transform()

image sb_table_pc_bentover_breasts_base_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_table_pc_bentover_breasts_shad_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_table_pc_bentover_breasts_nips_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_table_pc_bentover_breasts_nipring_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_table_pc_bentover_breasts_tattoo_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_tattoo", breasts=True)

image sb_table_pc_bentover_breasts_c_base_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_c_base", breasts=True)
    skin_base_colour_transform()
image sb_table_pc_bentover_breasts_c_shad_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_c_shad", breasts=True)
    skin_shad_colour_transform()
image sb_table_pc_bentover_breasts_c_nips_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_c_nips", breasts=True)
    nipple_colour_transform()
image sb_table_pc_bentover_breasts_c_tattoo_layer:
    get_skin_filename("sb_table_pc_bentover_breasts_c_tattoo", breasts=True)

image sb_table_pc_bentover_nails_layer:
    "sb_table_pc_bentover_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_table_pc_bentover_outfit_pub_breasts_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_pub_breasts", breasts=True)
image sb_table_pc_bentover_outfit_pub_preg_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_pub_preg", preg=True)
image sb_table_pc_bentover_outfit_dungarees_breasts_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_dungarees_breasts", breasts=True)
image sb_table_pc_bentover_outfit_dungarees_preg_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_dungarees_preg", preg=True)
image sb_table_pc_bentover_outfit_maid_breasts_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_maid_breasts", breasts=True)
image sb_table_pc_bentover_outfit_maid_preg_layer:
    get_skin_filename("sb_table_pc_bentover_outfit_maid_preg", preg=True)



image sb_table_pc_bentover_face_eyeshadow_layer:
    "sb_table_pc_bentover_face_eyeshadow"
    eyeshadow_colour_transform()
image sb_table_pc_bentover_face_freckles_layer:
    "sb_table_pc_bentover_face_freckles"
    skin_shad_colour_transform()
image sb_table_pc_bentover_face_blush_layer:
    "sb_table_pc_bentover_face_blush"
    blush_opacity_transform()

image sb_table_pc_bentover_face_eye_eyeliner_up_layer:
    "sb_table_pc_bentover_face_eye_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_table_pc_bentover_face_eye_iris_up_layer:
    "sb_table_pc_bentover_face_eye_iris_up"
    eye_colour_transform()
image sb_table_pc_bentover_face_eye_eyeliner_back_layer:
    "sb_table_pc_bentover_face_eye_eyeliner_back_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_table_pc_bentover_face_eye_iris_back_layer:
    "sb_table_pc_bentover_face_eye_iris_back"
    eye_colour_transform()

image sb_table_pc_bentover_face_mouth_happy_lipstick_layer:
    "sb_table_pc_bentover_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_table_pc_bentover_face_mouth_happy_layer:
    "sb_table_pc_bentover_face_mouth_happy"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_table_pc_bentover_face_mouth_shock_lipstick_layer:
    "sb_table_pc_bentover_face_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_table_pc_bentover_face_mouth_shock_layer:
    "sb_table_pc_bentover_face_mouth_shock"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_table_pc_bentover_face_mouth_ag_lipstick_layer:
    "sb_table_pc_bentover_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_table_pc_bentover_face_mouth_ag_layer:
    "sb_table_pc_bentover_face_mouth_ag"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_table_pc_bentover_face_mouth_pain_lipstick_layer:
    "sb_table_pc_bentover_face_mouth_pain_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_table_pc_bentover_face_mouth_pain_layer:
    "sb_table_pc_bentover_face_mouth_pain"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_table_pc_bentover_face_mouth_gag_lipstick_layer:
    "sb_table_pc_bentover_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_table_pc_bentover_face_mouth_gag_base_layer:
    "sb_table_pc_bentover_face_mouth_gag_base"
    gag_colour_transform()
image sb_table_pc_bentover_face_mouth_gag_metal_layer:
    "sb_table_pc_bentover_face_mouth_gag_metal"
    gag_metal_transform()

image sb_table_pc_bentover_face_brow_happy_layer:
    "sb_table_pc_bentover_face_brow_happy"
    hair_colour_transform()
image sb_table_pc_bentover_face_brow_worried_layer:
    "sb_table_pc_bentover_face_brow_worried"
    hair_colour_transform()
image sb_table_pc_bentover_face_brow_angry_layer:
    "sb_table_pc_bentover_face_brow_angry"
    hair_colour_transform()

image sb_table_pc_bentover_hair_front_layer:
    get_hair_front_cg_filename("sb_table_pc_bentover_hair_front")
    hair_colour_transform()
image sb_table_pc_bentover_hair_back_1 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_pig_1 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_pig_2 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_pony_1 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_pony_2 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_pony_3 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_bun_1 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_bun_2 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_bun_3 = "sb_table_pc_bentover_hair_back_base"
image sb_table_pc_bentover_hair_back_bun_4 = "sb_table_pc_bentover_hair_back_base"

image sb_table_pc_bentover_hair_back_layer:
    get_hair_back_cg_filename("sb_table_pc_bentover_hair_back")
    hair_colour_transform()

image sb_table = LayeredImageProxy("sb_table_layered", Transform(xalign = (0.8)))

layeredimage sb_table_layered:

    if dis(dis_pub):
        "sb_table_bg_pub"
    else:
        "sb_table_bg_office"

    group man:
        attribute noman default null

        attribute grope "sb_table_man_grope"

        attribute sex "sb_table_man_sex_base_layer"
        attribute sex "sb_table_man_sex_shad_layer"
        attribute sex "sb_table_man_sex_clothes"

        attribute mast "sb_table_man_mast_base_layer"
        attribute mast "sb_table_man_mast_shad_layer"
        attribute mast "sb_table_man_mast_clothes"

    always if_any "bentover" "sb_table_pc_bentover_hair_back_layer"

    group pc:
        attribute stand default "sb_table_stand_layered"
        attribute bentover "sb_table_bentover_layered"

    group man:
        attribute noman default null

        attribute sex "sb_table_man_hand_base_layer"
        attribute sex "sb_table_man_hand_shad_layer"

        attribute mast "sb_table_man_hand_base_layer"
        attribute mast "sb_table_man_hand_shad_layer"

    if skin_effect.face: 
        if_any "bentover" "sb_table_pc_bentover_face_freckles_layer"
    always if_any "bentover" "sb_table_pc_bentover_face_eyeshadow_layer"
    always if_any "bentover" "sb_table_pc_bentover_face_blush_layer"

    group mouth if_any "bentover":
        attribute shock default "sb_table_pc_bentover_face_mouth_shock_lipstick_layer" 
        attribute shock default "sb_table_pc_bentover_face_mouth_shock_layer" 

        attribute happy "sb_table_pc_bentover_face_mouth_happy_lipstick_layer"
        attribute happy "sb_table_pc_bentover_face_mouth_happy_layer"

        attribute pain "sb_table_pc_bentover_face_mouth_pain_lipstick_layer"
        attribute pain "sb_table_pc_bentover_face_mouth_pain_layer"

        attribute ag "sb_table_pc_bentover_face_mouth_ag_lipstick_layer"
        attribute ag "sb_table_pc_bentover_face_mouth_ag_layer"

    if player.gagged:
        if_any "bentover" "sb_table_bentover_gag_layered"

    group brow if_any "bentover":
        attribute shock default "sb_table_pc_bentover_face_brow_worried_layer" 
        attribute happy "sb_table_pc_bentover_face_brow_happy_layer"
        attribute pain "sb_table_pc_bentover_face_brow_angry_layer"
        attribute ag "sb_table_pc_bentover_face_brow_worried_layer"

    group eyes if_any "bentover":
        attribute back default "sb_table_pc_bentover_face_eye_iris_back_layer"
        attribute back default "sb_table_pc_bentover_face_eye_eye_back"
        attribute back default "sb_table_pc_bentover_face_eye_eyeliner_back_layer"

        attribute up "sb_table_pc_bentover_face_eye_iris_up_layer"
        attribute up "sb_table_pc_bentover_face_eye_eye_up"
        attribute up "sb_table_pc_bentover_face_eye_eyeliner_up_layer"

    always if_any "bentover" "sb_table_pc_bentover_hair_front_layer"

    always "sb_table_frame"

layeredimage sb_table_stand_layered:
    always "sb_table_pc_stand_washcloth"
    always "sb_table_pc_stand_body_base_layer"
    always "sb_table_pc_stand_body_shad_layer"
    if player.pregnancy >= 2:
        "sb_table_pc_stand_body_preg_base_layer"
    if player.pregnancy >= 2:
        "sb_table_pc_stand_body_preg_shad_layer"
    always "sb_table_pc_stand_nails_layer"

    if c.outfit == 6:
        "sb_table_pc_stand_outfit_pub_body"
    if c.outfit == 6 and player.pregnancy >= 2:
        "sb_table_pc_stand_outfit_pub_preg_layer"

    if c.outfit == 19:
        "sb_table_pc_stand_outfit_dungarees_body"
    if c.outfit == 19 and player.pregnancy >= 2:
        "sb_table_pc_stand_outfit_dungarees_preg_layer"

    if c.outfit == 20:
        "sb_table_pc_stand_outfit_maid_body"
    if c.outfit == 20 and player.pregnancy >= 2:
        "sb_table_pc_stand_outfit_maid_preg_layer"

    if c.outfit:
        "sb_table_stand_breasts_c_layered"
    else:
        "sb_table_stand_breasts_layered"

    if c.outfit == 6:
        "sb_table_pc_stand_outfit_pub_breasts_layer"
    if c.outfit == 19:
        "sb_table_pc_stand_outfit_dungarees_breasts_layer"
    if c.outfit == 20:
        "sb_table_pc_stand_outfit_maid_breasts_layer"

layeredimage sb_table_bentover_layered:

    always "sb_table_pc_bentover_body_base_layer"
    always "sb_table_pc_bentover_body_shad_layer"
    if player.pregnancy >= 2:
        "sb_table_pc_bentover_body_preg_base_layer"
    if player.pregnancy >= 2:
        "sb_table_pc_bentover_body_preg_shad_layer"

    if c.outfit == 6:
        "sb_table_pc_bentover_outfit_pub_body"
    if c.outfit == 6 and player.pregnancy >= 2:
        "sb_table_pc_bentover_outfit_pub_preg_layer"

    if c.outfit == 19:
        "sb_table_pc_bentover_outfit_dungarees_body"
    if c.outfit == 19 and player.pregnancy >= 2:
        "sb_table_pc_bentover_outfit_dungarees_preg_layer"

    if c.outfit == 20:
        "sb_table_pc_bentover_outfit_maid_body"
    if c.outfit == 20 and player.pregnancy >= 2:
        "sb_table_pc_bentover_outfit_maid_preg_layer"

    if c.outfit:
        "sb_table_bentover_breasts_c_layered"
    else:
        "sb_table_bentover_breasts_layered"

    if c.outfit == 6:
        "sb_table_pc_bentover_outfit_pub_breasts_layer"
    if c.outfit == 19:
        "sb_table_pc_bentover_outfit_dungarees_breasts_layer"
    if c.outfit == 20:
        "sb_table_pc_bentover_outfit_maid_breasts_layer"

layeredimage sb_table_stand_outfit_body_layered:
    always "sb_table_pc_stand_outfit_pub_body"
    if player.pregnancy >= 2:
        "sb_table_pc_stand_outfit_pub_preg_layer"
    always "sb_table_pc_stand_outfit_pub_breasts_layer"

layeredimage sb_table_stand_breasts_layered:
    always "sb_table_pc_stand_breasts_base_layer"
    always "sb_table_pc_stand_breasts_shad_layer"
    always "sb_table_pc_stand_breasts_nips_layer"
    if tattoo.chest:
        "sb_table_pc_stand_breasts_tattoo_layer"
    if acc.nipring:
        "sb_table_pc_stand_breasts_nipring_layer"
layeredimage sb_table_stand_breasts_c_layered:
    always "sb_table_pc_stand_breasts_c_base_layer"
    always "sb_table_pc_stand_breasts_c_shad_layer"
    always "sb_table_pc_stand_breasts_c_nips_layer"
    if tattoo.chest:
        "sb_table_pc_stand_breasts_c_tattoo_layer"

layeredimage sb_table_bentover_breasts_layered:
    always "sb_table_pc_bentover_breasts_base_layer"
    always "sb_table_pc_bentover_breasts_shad_layer"
    always "sb_table_pc_bentover_breasts_nips_layer"
    if tattoo.chest:
        "sb_table_pc_bentover_breasts_tattoo_layer"
    if acc.nipring:
        "sb_table_pc_bentover_breasts_nipring_layer"
layeredimage sb_table_bentover_breasts_c_layered:
    always "sb_table_pc_bentover_breasts_c_base_layer"
    always "sb_table_pc_bentover_breasts_c_shad_layer"
    always "sb_table_pc_bentover_breasts_c_nips_layer"
    if tattoo.chest:
        "sb_table_pc_bentover_breasts_c_tattoo_layer"
layeredimage sb_table_bentover_gag_layered:
    always "sb_table_pc_bentover_face_mouth_gag_lipstick_layer"
    always "sb_table_pc_bentover_face_mouth_gag_base_layer"
    always "sb_table_pc_bentover_face_mouth_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
