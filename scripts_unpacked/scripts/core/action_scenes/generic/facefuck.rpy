image sb_facefuck_man_sit_base_layer:
    "sb_facefuck_man_sit_base"
    npc_skin_base_colour_transform()
image sb_facefuck_man_sit_shad_layer:
    "sb_facefuck_man_sit_shad"
    npc_skin_shad_colour_transform()
image sb_facefuck_man_sit_hair_layer:
    "sb_facefuck_man_sit_hair"
    hair_colour_transform()

image sb_facefuck_man_sit_blow_base_layer:
    "sb_facefuck_man_sit_blow_base"
    npc_skin_base_colour_transform()
image sb_facefuck_man_sit_blow_shad_layer:
    "sb_facefuck_man_sit_blow_shad"
    npc_skin_shad_colour_transform()
image sb_facefuck_man_sit_blow_hair_layer:
    "sb_facefuck_man_sit_blow_hair"
    hair_colour_transform()

image sb_facefuck_man_sit_mast_base_layer:
    "sb_facefuck_man_sit_mast_base"
    npc_skin_base_colour_transform()
image sb_facefuck_man_sit_mast_shad_layer:
    "sb_facefuck_man_sit_mast_shad"
    npc_skin_shad_colour_transform()

image sb_facefuck_man_deep_base_layer:
    "sb_facefuck_man_deep_base"
    npc_skin_base_colour_transform()
image sb_facefuck_man_deep_shad_layer:
    "sb_facefuck_man_deep_shad"
    npc_skin_shad_colour_transform()
image sb_facefuck_man_deep_hair_layer:
    "sb_facefuck_man_deep_hair"
    hair_colour_transform()


image sb_facefuck_pc_body_base_layer:
    "sb_facefuck_pc_body_base"
    skin_base_colour_transform()
image sb_facefuck_pc_body_shad_layer:
    "sb_facefuck_pc_body_shad"
    skin_shad_colour_transform()


image sb_facefuck_pc_face_blush_layer:
    "sb_facefuck_pc_face_blush"
    blush_opacity_transform()
image sb_facefuck_pc_face_freckles_layer:
    "sb_facefuck_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_facefuck_pc_face_eyeshad_layer:
    "sb_facefuck_pc_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))


image sb_facefuck_pc_writing_face_layer:
    "sb_facefuck_pc_writing_face"
    writing_transform("face")
image sb_facefuck_pc_writing_forehead_layer:
    "sb_facefuck_pc_writing_forehead"
    writing_transform("forehead")


image sb_facefuck_pc_face_eye_iris_up_layer:
    "sb_facefuck_pc_face_eye_iris_up"
    eye_colour_transform()
image sb_facefuck_pc_face_eye_eyeliner_up_layer:
    "sb_facefuck_pc_face_eye_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_facefuck_pc_face_eye_iris_down_layer:
    "sb_facefuck_pc_face_eye_iris_down"
    eye_colour_transform()
image sb_facefuck_pc_face_eye_eyeliner_down_layer:
    "sb_facefuck_pc_face_eye_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_facefuck_pc_face_eye_eyeliner_closed_layer:
    "sb_facefuck_pc_face_eye_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_facefuck_pc_face_eye_iris_squint_layer:
    "sb_facefuck_pc_face_eye_iris_squint"
    eye_colour_transform()
image sb_facefuck_pc_face_eye_eyeliner_squint_layer:
    "sb_facefuck_pc_face_eye_eyeliner_squint_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image sb_facefuck_pc_face_brow_slant_layer:
    "sb_facefuck_pc_face_brow_slant"
    hair_colour_transform()
image sb_facefuck_pc_face_brow_straight_layer:
    "sb_facefuck_pc_face_brow_straight"
    hair_colour_transform()

image sb_facefuck_pc_hair_back_layer:
    "sb_facefuck_pc_hair_back"
    hair_colour_transform()

image sb_facefuck_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_facefuck_pc_hair_front")
    hair_colour_transform()

image sb_facefuck = LayeredImageProxy("sb_facefuck_layer", Transform(xalign = (0.85)))

layeredimage sb_facefuck_layer:  
    if loc_cur == loc_motel_pinkroom:
        "sb_facefuck_bg_pink"
    else:
        "sb_facefuck_bg"

    always "sb_facefuck_pc_body_base_layer"
    always "sb_facefuck_pc_body_shad_layer"

    always "sb_facefuck_pc_face_freckles_layer"
    always "sb_facefuck_pc_face_blush_layer"
    always "sb_facefuck_pc_face_eyeshad_layer"

    if writing.face:
        "sb_facefuck_pc_writing_face_layer"
    if writing.forehead:
        "sb_facefuck_pc_writing_forehead_layer"

    if player.cum_locations["cum_mouth"]:
        "sb_facefuck_pc_cum_mouth"
    if player.cum_locations["cum_face"]:
        "sb_facefuck_pc_cum_face"

    group eyes:
        attribute up default "sb_facefuck_pc_face_eye_iris_up_layer"
        attribute up default "sb_facefuck_pc_face_eye_eye_up"
        attribute up default "sb_facefuck_pc_face_eye_eyeliner_up_layer"
        attribute up default "sb_facefuck_pc_face_brow_straight_layer"

        attribute down "sb_facefuck_pc_face_eye_iris_down_layer"
        attribute down "sb_facefuck_pc_face_eye_eye_down"
        attribute down "sb_facefuck_pc_face_eye_eyeliner_down_layer"
        attribute down "sb_facefuck_pc_face_brow_straight_layer"

        attribute squint "sb_facefuck_pc_face_eye_iris_squint_layer"
        attribute squint "sb_facefuck_pc_face_eye_eye_squint"
        attribute squint "sb_facefuck_pc_face_eye_eyeliner_squint_layer"
        attribute squint "sb_facefuck_pc_face_brow_slant_layer"

        attribute closed "sb_facefuck_pc_face_eye_eyeliner_closed_layer"
        attribute closed "sb_facefuck_pc_face_brow_straight_layer"

    always "sb_facefuck_pc_hair_back_layer"
    always "sb_facefuck_pc_hair_front_layer"

    group man:

        attribute mast default "sb_facefuck_man_sit_hair_layer"
        attribute mast default "sb_facefuck_man_sit_base_layer"
        attribute mast default "sb_facefuck_man_sit_shad_layer"
        attribute mast default "sb_facefuck_man_sit_mast_base_layer"
        attribute mast default "sb_facefuck_man_sit_mast_shad_layer"

        attribute blow "sb_facefuck_man_sit_hair_layer"
        attribute blow "sb_facefuck_man_sit_base_layer"
        attribute blow "sb_facefuck_man_sit_shad_layer"
        attribute blow "sb_facefuck_man_sit_blow_hair_layer"
        attribute blow "sb_facefuck_man_sit_blow_base_layer"
        attribute blow "sb_facefuck_man_sit_blow_shad_layer"

        attribute deep "sb_facefuck_man_deep_hair_layer"
        attribute deep "sb_facefuck_man_deep_base_layer"
        attribute deep "sb_facefuck_man_deep_shad_layer"

    always "sb_facefuck_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
