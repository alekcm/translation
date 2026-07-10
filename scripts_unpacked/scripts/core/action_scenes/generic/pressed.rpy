image sbpressed_bg_layer:
    "sb_pressed_bg_" + loc_cur.loc_type

image sb_pressed_pc_body_base_layer:
    "sb_pressed_pc_body_base"
    skin_base_colour_transform()
image sb_pressed_pc_body_shad_layer:
    "sb_pressed_pc_body_shad"
    skin_shad_colour_transform()

image sb_pressed_pc_belly_base_layer:
    "sb_pressed_pc_belly_base"
    skin_base_colour_transform()
image sb_pressed_pc_belly_shad_layer:
    "sb_pressed_pc_belly_shad"
    skin_shad_colour_transform()

image sb_pressed_pc_face_lipstick_layer:
    "sb_pressed_pc_face_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_pressed_pc_face_eyeshadow_layer:
    "sb_pressed_pc_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image sb_pressed_pc_face_freckles_layer:
    "sb_pressed_pc_face_freckles"
    skin_shad_colour_transform()
image sb_pressed_pc_face_nails_layer:
    "sb_pressed_pc_face_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_pressed_pc_face_gag_base_layer:
    "sb_pressed_pc_face_gag_base"
    gag_colour_transform()
image sb_pressed_pc_face_gag_metal_layer:
    "sb_pressed_pc_face_gag_metal"
    gag_metal_transform()
image sb_pressed_pc_face_gag_lipstick_layer:
    "sb_pressed_pc_face_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_pressed_pc_face_gag_skin_layer:
    "sb_pressed_pc_face_gag_skin"
    skin_base_colour_transform()

image sb_pressed_pc_face_brow_layer:
    "sb_pressed_pc_face_brow"
    hair_colour_transform()
image sb_pressed_pc_face_eye_iris_layer:
    "sb_pressed_pc_face_eye_iris"
    eye_colour_transform()

image sb_pressed_pc_face_eye_eyeliner_layer:
    "sb_pressed_pc_face_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image sb_pressed_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_pressed_pc_hair_back")
    hair_colour_transform()
image sb_pressed_pc_hair_front_layer:
    "sb_pressed_pc_hair_front"
    hair_colour_transform()


image sb_pressed_pc_breasts_base_layer:
    get_skin_filename("sb_pressed_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_pressed_pc_breasts_shad_layer:
    get_skin_filename("sb_pressed_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_pressed_pc_breasts_nips_layer:
    get_skin_filename("sb_pressed_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_pressed_pc_breasts_nipring_layer:
    get_skin_filename("sb_pressed_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_pressed_pc_writing_anus_layer:
    "sb_pressed_pc_writing_anal"
    writing_transform("anus")



image sb_pressed_man_handgag_base_layer:
    "sb_pressed_man_handgag_base"
    npc_skin_base_colour_transform()
image sb_pressed_man_handgag_shad_layer:
    "sb_pressed_man_handgag_shad"
    npc_skin_shad_colour_transform()

image sb_pressed_man_top_base_layer:
    "sb_pressed_man_top_base"
    npc_skin_base_colour_transform()
image sb_pressed_man_top_shad_layer:
    "sb_pressed_man_top_shad"
    npc_skin_shad_colour_transform()

image sb_pressed_man_bottom_ass_base_layer:
    "sb_pressed_man_bottom_ass_base"
    npc_skin_base_colour_transform()
image sb_pressed_man_bottom_ass_shad_layer:
    "sb_pressed_man_bottom_ass_shad"
    npc_skin_shad_colour_transform()

image sb_pressed_man_bottom_poke_base_layer:
    "sb_pressed_man_bottom_poke_base"
    npc_skin_base_colour_transform()
image sb_pressed_man_bottom_poke_shad_layer:
    "sb_pressed_man_bottom_poke_shad"
    npc_skin_shad_colour_transform()

image sb_pressed_man_bottom_sex_base_layer:
    "sb_pressed_man_bottom_sex_base"
    npc_skin_base_colour_transform()
image sb_pressed_man_bottom_sex_shad_layer:
    "sb_pressed_man_bottom_sex_shad"
    npc_skin_shad_colour_transform()

image sb_pressed = LayeredImageProxy("sb_pressed_layered", Transform(xalign = (0.7)))

layeredimage sb_pressed_layered:
    always "sbpressed_bg_layer"

    always "sb_pressed_pc_body_base_layer"
    always "sb_pressed_pc_body_shad_layer"

    if tattoo.ass:
        "sb_pressed_pc_tattoo_tramp"
    if writing.anus:
        "sb_pressed_pc_writing_anus_layer"

    if player.showing:
        "sb_pressed_pc_belly_base_layer"
    if player.showing:
        "sb_pressed_pc_belly_shad_layer"

    always "sb_pressed_pc_face_lipstick_layer"
    always "sb_pressed_pc_face_eyeshadow_layer"
    if skin_effect.face:
        "sb_pressed_pc_face_freckles_layer"
    always "sb_pressed_pc_face_nails_layer"

    always "sb_pressed_breasts_layered"

    always "sb_pressed_pc_face_brow_layer"

    if player.beingraped:
        "sb_pressed_pc_face_cry"

    always "sb_pressed_pc_face_eye_iris_layer"
    always "sb_pressed_pc_face_eye_eye"
    always "sb_pressed_pc_face_eye_eyeliner_layer"

    if player.beingraped:
        "sb_pressed_pc_face_tear"
    if player.gagged:
        "sb_pressed_gag_layered"
    if player.blind:
        "sb_pressed_pc_blindfold"

    group hand:
        attribute no_hand null default

        attribute hand "sb_pressed_man_handgag_base_layer"
        attribute hand "sb_pressed_man_handgag_shad_layer"

    group man:
        attribute poke "sb_pressed_man_bottom_poke_base_layer" 
        attribute poke "sb_pressed_man_bottom_poke_shad_layer"

        attribute ass "sb_pressed_man_bottom_ass_base_layer" default
        attribute ass "sb_pressed_man_bottom_ass_shad_layer" default

        attribute sex "sb_pressed_man_bottom_sex_base_layer"
        attribute sex "sb_pressed_man_bottom_sex_shad_layer"

    always "sb_pressed_man_top_base_layer"
    always "sb_pressed_man_top_shad_layer"

    always "sb_pressed_pc_hair_front_layer"
    always "sb_pressed_pc_hair_back_layer"

    always "sb_pressed_frame"

layeredimage sb_pressed_breasts_layered:

    always "sb_pressed_pc_breasts_base_layer"
    if player.breasts > 1:
        "sb_pressed_pc_breasts_shad_layer"
    if player.breasts < 3:
        "sb_pressed_pc_breasts_nips_layer"
    if player.breasts < 3 and acc.nipring:
        "sb_pressed_pc_breasts_nipring_layer"

layeredimage sb_pressed_gag_layered:
    always "sb_pressed_pc_face_gag_skin_layer"
    always "sb_pressed_pc_face_gag_lipstick_layer"
    always "sb_pressed_pc_face_gag_base_layer"
    always "sb_pressed_pc_face_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
