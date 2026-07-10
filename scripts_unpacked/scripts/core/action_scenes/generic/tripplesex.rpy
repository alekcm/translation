

image sb_tripplesex_pc_body_base_layer:
    "sb_tripplesex_pc_body_base"
    skin_base_colour_transform()
image sb_tripplesex_pc_body_shad_layer:
    "sb_tripplesex_pc_body_shad"
    skin_shad_colour_transform()

image sb_tripplesex_pc_belly_base_layer:
    get_skin_filename("sb_tripplesex_pc_belly_base", True)
    skin_base_colour_transform()
image sb_tripplesex_pc_belly_shad_layer:
    get_skin_filename("sb_tripplesex_pc_belly_shad", True)
    skin_shad_colour_transform()

image sb_tripplesex_pc_breasts_base_layer:
    get_skin_filename("sb_tripplesex_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_tripplesex_pc_breasts_shad_layer:
    get_skin_filename("sb_tripplesex_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_tripplesex_pc_breasts_nips_layer:
    get_skin_filename("sb_tripplesex_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_tripplesex_pc_breasts_tattoo_layer:
    get_skin_filename("sb_tripplesex_pc_breasts_tattoo", breasts=True)


image sb_tripplesex_pc_face_blush_layer:
    "sb_tripplesex_pc_face_blush"
    blush_opacity_transform()
image sb_tripplesex_pc_face_freckles_layer:
    "sb_tripplesex_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_tripplesex_pc_face_eyeshadow_layer:
    "sb_tripplesex_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))


image sb_tripplesex_pc_writing_chest_layer:
    "sb_tripplesex_pc_writing_chest"
    writing_transform("chest")
image sb_tripplesex_pc_writing_face_layer:
    "sb_tripplesex_pc_writing_face"
    writing_transform("face")
image sb_tripplesex_pc_writing_forehead_layer:
    "sb_tripplesex_pc_writing_forehead"
    writing_transform("forehead")


image sb_tripplesex_pc_hair_back_bun_2 = "sb_tripplesex_pc_hair_back_tied"
image sb_tripplesex_pc_hair_back_bun_3 = "sb_tripplesex_pc_hair_back_tied"
image sb_tripplesex_pc_hair_back_bun_4 = "sb_tripplesex_pc_hair_back_tied"
image sb_tripplesex_pc_hair_back_bun_2 = "sb_tripplesex_pc_hair_back_tied"
image sb_tripplesex_pc_hair_back_bun_3 = "sb_tripplesex_pc_hair_back_tied"
image sb_tripplesex_pc_hair_back_bun_4 = "sb_tripplesex_pc_hair_back_tied"

image sb_tripplesex_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_tripplesex_pc_hair_back")
    hair_colour_transform()

image sb_tripplesex_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_tripplesex_pc_hair_front")
    hair_colour_transform()


image sb_tripplesex_pc_face_eye_left_eyeliner_layer:
    "sb_tripplesex_pc_face_eye_left_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_tripplesex_pc_face_eye_right_eyeliner_layer:
    "sb_tripplesex_pc_face_eye_right_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_tripplesex_pc_face_eye_left_iris_layer:
    "sb_tripplesex_pc_face_eye_left_iris"
    eye_colour_transform()
image sb_tripplesex_pc_face_eye_right_iris_layer:
    "sb_tripplesex_pc_face_eye_right_iris"
    eye_colour_transform()

image sb_tripplesex_pc_face_brow_straight_layer:
    "sb_tripplesex_pc_face_brow_straight"
    hair_colour_transform()
image sb_tripplesex_pc_face_brow_slant_layer:
    "sb_tripplesex_pc_face_brow_slant"
    hair_colour_transform()
image sb_tripplesex_pc_face_brow_worried_layer:
    "sb_tripplesex_pc_face_brow_worried"
    hair_colour_transform()

image sb_tripplesex_pc_face_mouth_happy_lipstick_layer:
    "sb_tripplesex_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_tripplesex_pc_face_mouth_oh_lipstick_layer:
    "sb_tripplesex_pc_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_tripplesex_pc_face_mouth_pout_lipstick_layer:
    "sb_tripplesex_pc_face_mouth_pout_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))
image sb_tripplesex_pc_face_mouth_smile_lipstick_layer:
    "sb_tripplesex_pc_face_mouth_smile_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not player.gagged and acc.lipstick,1,0))


image sb_tripplesex_man_mid_base_layer:
    "sb_tripplesex_man_mid_base"
    npc_skin_base_colour_transform()
image sb_tripplesex_man_mid_shad_layer:
    "sb_tripplesex_man_mid_shad"
    npc_skin_shad_colour_transform()

image sb_tripplesex_man_right_base_layer:
    "sb_tripplesex_man_right_base"
    npc2_skin_base_colour_transform()
image sb_tripplesex_man_right_shad_layer:
    "sb_tripplesex_man_right_shad"
    npc2_skin_shad_colour_transform()

image sb_tripplesex_man_left_base_layer:
    "sb_tripplesex_man_left_base"
    npc3_skin_base_colour_transform()
image sb_tripplesex_man_left_shad_layer:
    "sb_tripplesex_man_left_shad"
    npc3_skin_shad_colour_transform()

image sb_tripplesex = LayeredImageProxy("sb_tripplesex_layered", Transform(xalign = (0.8)))

layeredimage sb_tripplesex_layered:
    always "sb_tripplesex_bg"

    always if_any ["pc", "anabel", "svet"] "sb_tripplesex_man_mid_base_layer"
    always if_any ["pc", "anabel", "svet"] "sb_tripplesex_man_mid_shad_layer"

    always if_any ["robin", "dani"] "sb_tripplesex_man_left_base_layer"
    always if_any ["robin", "dani"] "sb_tripplesex_man_left_shad_layer"

    always if_any ["trixie", "rachel"] "sb_tripplesex_man_right_base_layer"
    always if_any ["trixie", "rachel"] "sb_tripplesex_man_right_shad_layer"

    group left:
        attribute dani "sb_tripplesex_dani_layered"
        attribute robin "sb_tripplesex_robin_layered"
        attribute no_left null

    group right:
        attribute trixie "sb_tripplesex_trixie_layered"
        attribute rachel "sb_tripplesex_rachel_layered"
        attribute no_right null

    group mid:
        attribute svet "sb_tripplesex_svet"
        attribute anabel "sb_tripplesex_anabel_layered"
        attribute pc "sb_tripplesex_pc_layered"
        attribute no_mid null

    group eyes:
        attribute left default if_any "pc" "sb_tripplesex_pc_face_eye_left_iris_layer"
        attribute left default if_any "pc" "sb_tripplesex_pc_face_eye_left_eye"
        attribute left default if_any "pc" "sb_tripplesex_pc_face_eye_left_eyeliner_layer"

        attribute right if_any "pc" "sb_tripplesex_pc_face_eye_right_iris_layer"
        attribute right if_any "pc" "sb_tripplesex_pc_face_eye_right_eye"
        attribute right if_any "pc" "sb_tripplesex_pc_face_eye_right_eyeliner_layer"

    group brow:
        attribute slant default if_any "pc" "sb_tripplesex_pc_face_brow_slant_layer"
        attribute straight if_any "pc" "sb_tripplesex_pc_face_brow_straight_layer"
        attribute worried if_any "pc" "sb_tripplesex_pc_face_brow_worried_layer"

    group mouth:
        attribute happy if_any "pc" "sb_tripplesex_pc_face_mouth_happy_lipstick_layer"
        attribute happy if_any "pc" "sb_tripplesex_pc_face_mouth_happy"

        attribute oh if_any "pc" "sb_tripplesex_pc_face_mouth_oh_lipstick_layer"
        attribute oh if_any "pc" "sb_tripplesex_pc_face_mouth_oh"

        attribute pout if_any "pc" "sb_tripplesex_pc_face_mouth_pout_lipstick_layer"
        attribute pout if_any "pc" "sb_tripplesex_pc_face_mouth_pout"

        attribute smile default if_any "pc" "sb_tripplesex_pc_face_mouth_smile_lipstick_layer"
        attribute smile default if_any "pc" "sb_tripplesex_pc_face_mouth_smile"

    always if_any "pc" "sb_tripplesex_pc_hair_back_layer"
    always if_any "pc" "sb_tripplesex_pc_hair_front_layer"


    group right:
        attribute trixie if_any "pc" "sb_tripplesex_trixie_above_pc"

        attribute rachel if_any "svet" "sb_tripplesex_rachel_above_svet"
        attribute rachel if_any "anabel" "sb_tripplesex_rachel_above_anabel"
        attribute rachel if_any "pc" "sb_tripplesex_rachel_above_pc"
    group left:
        attribute robin if_any "pc" "sb_tripplesex_robin_above_pc"

        attribute dani if_any "pc" "sb_tripplesex_dani_above_pc"
        attribute dani if_any "anabel" "sb_tripplesex_dani_above_anabel"


    always "sb_tripplesex_frame"

layeredimage sb_tripplesex_pc_layered:
    always "sb_tripplesex_pc_body_base_layer"
    always "sb_tripplesex_pc_body_shad_layer"

    if player.showing:
        "sb_tripplesex_pc_belly_base_layer"
    if player.showing:
        "sb_tripplesex_pc_belly_shad_layer"

    always "sb_tripplesex_pc_breasts_base_layer"
    always "sb_tripplesex_pc_breasts_shad_layer"
    always "sb_tripplesex_pc_breasts_nips_layer"
    if tattoo.chest:
        "sb_tripplesex_pc_breasts_tattoo_layer"

    always "sb_tripplesex_pc_face_blush_layer"
    always "sb_tripplesex_pc_face_freckles_layer"
    always "sb_tripplesex_pc_face_eyeshadow_layer"

    if writing.chest:
        "sb_tripplesex_pc_writing_chest_layer"
    if writing.forehead:
        "sb_tripplesex_pc_writing_forehead_layer"
    if writing.face:
        "sb_tripplesex_pc_writing_face_layer"


layeredimage sb_tripplesex_dani_layered:
    always "sb_tripplesex_dani_main"
    if dani.showing:
        "sb_tripplesex_dani_belly"

layeredimage sb_tripplesex_robin_layered:
    always "sb_tripplesex_robin_main"
    if robin.showing:
        "sb_tripplesex_robin_belly"

layeredimage sb_tripplesex_trixie_layered:
    always "sb_tripplesex_trixie_main"
    if trixie.showing:
        "sb_tripplesex_trixie_belly"

layeredimage sb_tripplesex_rachel_layered:
    always "sb_tripplesex_rachel_main"
    if rachel.showing:
        "sb_tripplesex_rachel_belly"

layeredimage sb_tripplesex_anabel_layered:
    always "sb_tripplesex_anabel_main"
    if anabel.showing:
        "sb_tripplesex_anabel_belly"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
