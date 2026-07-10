image sb_bentover_bg_layer:

    "sb_bentover_bg_room"

image sb_bentover_pc_bottom_base_layer:
    "sb_bentover_pc_bottom_base"
    skin_base_colour_transform()
image sb_bentover_pc_bottom_shad_layer:
    "sb_bentover_pc_bottom_shad"
    skin_shad_colour_transform()

image sb_bentover_pc_bottom_hair_layer:
    "sb_bentover_pc_bottom_hair"
    hair_colour_transform()


image sb_bentover_pc_top_base_layer:
    "sb_bentover_pc_top_base"
    skin_base_colour_transform()
image sb_bentover_pc_top_shad_layer:
    "sb_bentover_pc_top_shad"
    skin_shad_colour_transform()

image sb_bentover_pc_top_breasts_base_layer:
    get_skin_filename("sb_bentover_pc_top_breasts_base", breasts=True)
    skin_shad_colour_transform()
image sb_bentover_pc_top_breasts_shad_layer:
    get_skin_filename("sb_bentover_pc_top_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_bentover_pc_top_breasts_nips_layer:
    get_skin_filename("sb_bentover_pc_top_breasts_nips", breasts=True)
    nipple_colour_transform()


image sb_bentover_pc_face_eyeshadow_layer:
    "sb_bentover_pc_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))
image sb_bentover_pc_face_freckles_layer:
    "sb_bentover_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_bentover_pc_face_blush_layer:
    "sb_bentover_pc_face_blush"
    blush_opacity_transform()
image sb_bentover_pc_bottom_spank_layer:
    "sb_bentover_pc_bottom_spank"
    opacity_transform(bruise.ass)


image sb_bentover_pc_face_eye_forward_eyeliner_layer:
    "sb_bentover_pc_face_eye_forward_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_bentover_pc_face_eye_forward_iris_layer:
    "sb_bentover_pc_face_eye_forward_iris"
    eye_colour_transform()

image sb_bentover_pc_face_eye_back_eyeliner_layer:
    "sb_bentover_pc_face_eye_back_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_bentover_pc_face_eye_back_iris_layer:
    "sb_bentover_pc_face_eye_back_iris"
    eye_colour_transform()

image sb_bentover_pc_face_eye_closed_eyeliner_layer:
    "sb_bentover_pc_face_eye_closed_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image sb_bentover_pc_face_mouth_smile_layer:
    "sb_bentover_pc_face_mouth_smile"
    matrixcolor OpacityMatrix(If(not player.gagged, 1,0))
image sb_bentover_pc_face_mouth_smile_lipstick_layer:
    "sb_bentover_pc_face_mouth_smile_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_bentover_pc_face_mouth_ooh_layer:
    "sb_bentover_pc_face_mouth_ooh"
    matrixcolor OpacityMatrix(If(not player.gagged, 1,0))
image sb_bentover_pc_face_mouth_ooh_lipstick_layer:
    "sb_bentover_pc_face_mouth_ooh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_bentover_pc_face_mouth_oh_layer:
    "sb_bentover_pc_face_mouth_oh"
    matrixcolor OpacityMatrix(If(not player.gagged, 1,0))
image sb_bentover_pc_face_mouth_oh_lipstick_layer:
    "sb_bentover_pc_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_bentover_pc_face_mouth_ag_layer:
    "sb_bentover_pc_face_mouth_ag"
    matrixcolor OpacityMatrix(If(not player.gagged, 1,0))
image sb_bentover_pc_face_mouth_ag_lipstick_layer:
    "sb_bentover_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_bentover_pc_face_mouth_gag_lipstick_layer:
    "sb_bentover_pc_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_bentover_pc_face_mouth_gag_base_layer:
    "sb_bentover_pc_face_mouth_gag_base"
    gag_colour_transform()
image sb_bentover_pc_face_mouth_gag_metal_layer:
    "sb_bentover_pc_face_mouth_gag_metal"
    gag_metal_transform()



image sb_bentover_pc_face_brow_straight_layer:
    "sb_bentover_pc_face_brow_straight"
    hair_colour_transform()
image sb_bentover_pc_face_brow_worried_layer:
    "sb_bentover_pc_face_brow_worried"
    hair_colour_transform()


image sb_bentover_pc_hair_back_bun_2 = "sb_bentover_pc_hair_back_bun"
image sb_bentover_pc_hair_back_bun_3 = "sb_bentover_pc_hair_back_bun"
image sb_bentover_pc_hair_back_bun_4 = "sb_bentover_pc_hair_back_bun"
image sb_bentover_pc_hair_back_pony_2 = "sb_bentover_pc_hair_back_bun"
image sb_bentover_pc_hair_back_pony_3 = "sb_bentover_pc_hair_back_bun"
image sb_bentover_pc_hair_back_pony_4 = "sb_bentover_pc_hair_back_bun"

image sb_bentover_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_bentover_pc_hair_back")
    hair_colour_transform()

image sb_bentover_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_bentover_pc_hair_front")
    hair_colour_transform()


image sb_bentover_pc_face_writing_chest_layer:
    "sb_bentover_pc_face_writing_chest"
    writing_transform("chest")
image sb_bentover_pc_face_writing_face_layer:
    "sb_bentover_pc_face_writing_face"
    writing_transform("face")
image sb_bentover_pc_face_writing_forehead_layer:
    "sb_bentover_pc_face_writing_forehead"
    writing_transform("forehead")

image sb_bentover = LayeredImageProxy("sb_bentover_layered", Transform(xalign = (0.80)))

layeredimage sb_bentover_layered:
    always "sb_bentover_bg_layer"

    always "sb_bentover_pc_bottom_base_layer"
    always "sb_bentover_pc_bottom_shad_layer"
    always "sb_bentover_pc_bottom_hair_layer"
    if tattoo.ass:
        "sb_bentover_pc_bottom_tattoo_tramp"
    always "sb_bentover_pc_bottom_spank_layer"

    group sex:
        attribute no_dani default null
        attribute dani_lick "sb_bentover_dani_lick"
        attribute dani_cum "sb_bentover_dani_cum"
        attribute dani_poke "sb_bentover_dani_poke"
        attribute dani_sex "sb_bentover_dani_sex"

    group head:
        attribute head_up default null
        attribute head_down null

    always if_any "head_up" "sb_bentover_pc_top_base_layer"
    always if_any "head_up" "sb_bentover_pc_top_shad_layer"

    always if_any "head_up" "sb_bentover_pc_top_breasts_base_layer"
    always if_any "head_up" "sb_bentover_pc_top_breasts_shad_layer"
    always if_any "head_up" "sb_bentover_pc_top_breasts_nips_layer"

    always if_any "head_up" "sb_bentover_pc_face_eyeshadow_layer"
    always if_any "head_up" "sb_bentover_pc_face_freckles_layer"
    always if_any "head_up" "sb_bentover_pc_face_blush_layer"

    group eyes if_any "head_up":
        attribute forward "sb_bentover_pc_face_eye_forward_iris_layer"
        attribute forward "sb_bentover_pc_face_eye_forward_eye"
        attribute forward "sb_bentover_pc_face_eye_forward_eyeliner_layer"

        attribute back default "sb_bentover_pc_face_eye_back_iris_layer"
        attribute back default "sb_bentover_pc_face_eye_back_eye"
        attribute back default "sb_bentover_pc_face_eye_back_eyeliner_layer"

        attribute closed "sb_bentover_pc_face_eye_closed_eyeliner_layer"

    group brow if_any "head_up":
        attribute straight default "sb_bentover_pc_face_brow_straight_layer"
        attribute worried "sb_bentover_pc_face_brow_worried_layer"

    group mouth if_any "head_up":
        attribute smile default "sb_bentover_pc_face_mouth_smile_lipstick_layer"
        attribute smile default "sb_bentover_pc_face_mouth_smile_layer" 

        attribute ooh "sb_bentover_pc_face_mouth_ooh_lipstick_layer"
        attribute ooh "sb_bentover_pc_face_mouth_ooh_layer" 

        attribute oh "sb_bentover_pc_face_mouth_oh_lipstick_layer"
        attribute oh "sb_bentover_pc_face_mouth_oh_layer" 

        attribute ag "sb_bentover_pc_face_mouth_ag_lipstick_layer"
        attribute ag "sb_bentover_pc_face_mouth_ag_layer" 

    if writing.chest:
        if_any "head_up" "sb_bentover_pc_face_writing_chest_layer"
    if writing.forehead:
        if_any "head_up" "sb_bentover_pc_face_writing_forehead_layer"
    if writing.face:
        if_any "head_up" "sb_bentover_pc_face_writing_face_layer"

    if player.gagged:
        if_any "head_up" "sb_bentover_gag"
    if player.blind:
        if_any "head_up" "sb_bentover_pc_face_blind"

    always if_any "head_up" "sb_bentover_pc_hair_back_layer"
    always if_any "head_up" "sb_bentover_pc_hair_front_layer"

    always "sb_bentover_frame"
layeredimage sb_bentover_gag:
    always "sb_bentover_pc_face_mouth_gag_lipstick_layer"
    always "sb_bentover_pc_face_mouth_gag_base_layer"
    always "sb_bentover_pc_face_mouth_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
