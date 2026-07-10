

image sb_trippleblow_far_pc_base_base_layer:
    "sb_trippleblow_far_pc_base_base"
    skin_base_colour_transform()
image sb_trippleblow_far_pc_base_shad_layer:
    "sb_trippleblow_far_pc_base_shad"
    skin_shad_colour_transform()

image sb_trippleblow_far_pc_breasts_base_layer:
    get_skin_filename("sb_trippleblow_far_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_trippleblow_far_pc_breasts_shad_layer:
    get_skin_filename("sb_trippleblow_far_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image sb_trippleblow_far_pc_face_brow_layer:
    "sb_trippleblow_far_pc_face_brow"
    hair_colour_transform()


image sb_trippleblow_far_pc_hair_back_bun_3 = "sb_trippleblow_far_pc_hair_back_bun_2"
image sb_trippleblow_far_pc_hair_back_pig_4 = "sb_trippleblow_far_pc_hair_back_pig_3"
image sb_trippleblow_far_pc_hair_back_pony_2 = "sb_trippleblow_far_pc_hair_back_pony"
image sb_trippleblow_far_pc_hair_back_pony_3 = "sb_trippleblow_far_pc_hair_back_pony"
image sb_trippleblow_far_pc_hair_back_pony_4 = "sb_trippleblow_far_pc_hair_back_pony"

image sb_trippleblow_far_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_trippleblow_far_pc_hair_back")
    hair_colour_transform()
image sb_trippleblow_far_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_trippleblow_far_pc_hair_front")
    hair_colour_transform()

image sb_trippleblow_far_pc_face_eye_iris_layer:
    "sb_trippleblow_far_pc_face_eye_iris"
    eye_colour_transform()
image sb_trippleblow_far_pc_face_eye_eyeliner_layer:
    "sb_trippleblow_far_pc_face_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_trippleblow_far_pc_writing_face_layer:
    "sb_trippleblow_far_pc_writing_face"
    writing_transform("face")
image sb_trippleblow_far_pc_writing_forehead_layer:
    "sb_trippleblow_far_pc_writing_forehead"
    writing_transform("forehead")
image sb_trippleblow_far_pc_writing_chest_layer:
    "sb_trippleblow_far_pc_writing_chest"
    writing_transform("chest")

image sb_trippleblow_far_pc_face_lipstick_layer:
    "sb_trippleblow_far_pc_face_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_trippleblow_far_pc_face_freckles_layer:
    "sb_trippleblow_far_pc_face_freckles"
    skin_shad_colour_transform()
image sb_trippleblow_far_pc_face_blush_layer:
    "sb_trippleblow_far_pc_face_blush"
    blush_opacity_transform()
image sb_trippleblow_far_pc_face_eyeshad_layer:
    "sb_trippleblow_far_pc_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))



image sb_trippleblow_front_man_base_layer:
    "sb_trippleblow_front_man_base"
    npc_skin_base_colour_transform()
image sb_trippleblow_front_man_shad_layer:
    "sb_trippleblow_front_man_shad"
    npc_skin_shad_colour_transform()

image sb_trippleblow_mid_man_base_layer:
    "sb_trippleblow_mid_man_base"
    npc2_skin_base_colour_transform()
image sb_trippleblow_mid_man_shad_layer:
    "sb_trippleblow_mid_man_shad"
    npc2_skin_shad_colour_transform()

image sb_trippleblow_far_man_base_layer:
    "sb_trippleblow_far_man_base"
    npc3_skin_base_colour_transform()
image sb_trippleblow_far_man_shad_layer:
    "sb_trippleblow_far_man_shad"
    npc3_skin_shad_colour_transform()


image sb_trippleblow = LayeredImageProxy("sb_trippleblow_layered", Transform(xalign = (0.8)))

layeredimage sb_trippleblow_layered:
    always "sb_trippleblow_bg"

    group far_man:
        attribute far_man "sb_trippleblow_far_man_base_layer"
        attribute far_man "sb_trippleblow_far_man_shad_layer"

        attribute far_noman null

    group far:
        attribute pc "sb_trippleblow_pc_layered" 
        attribute anabel "sb_trippleblow_far_anabel"
        attribute svet "sb_trippleblow_far_svet"

        attribute no_far null

    group mid_man:

        attribute mid_man "sb_trippleblow_mid_man_base_layer"
        attribute mid_man "sb_trippleblow_mid_man_shad_layer"

        attribute mid_noman null

    group mid:
        attribute dani "sb_trippleblow_mid_dani"
        attribute robin "sb_trippleblow_mid_robin"
        attribute no_mid null

    group close_man:

        attribute close_man "sb_trippleblow_front_man_base_layer"
        attribute close_man "sb_trippleblow_front_man_shad_layer"

        attribute close_noman null

    group front:
        attribute rachel "sb_trippleblow_front_rachel"
        attribute trixie "sb_trippleblow_front_trixie"

        attribute no_close null

    always "sb_trippleblow_frame"

layeredimage sb_trippleblow_pc_layered:
    always "sb_trippleblow_far_pc_base_base_layer"
    always "sb_trippleblow_far_pc_base_shad_layer"
    always "sb_trippleblow_far_pc_breasts_base_layer"
    always "sb_trippleblow_far_pc_breasts_shad_layer"

    always "sb_trippleblow_far_pc_face_eyeshad_layer"

    always "sb_trippleblow_far_pc_face_brow_layer"
    always "sb_trippleblow_far_pc_face_eye_iris_layer"
    always "sb_trippleblow_far_pc_face_eye_eye"
    always "sb_trippleblow_far_pc_face_eye_eyeliner_layer"


    always "sb_trippleblow_far_pc_face_lipstick_layer"
    if writing.chest:
        "sb_trippleblow_far_pc_writing_chest_layer"
    if writing.face:
        "sb_trippleblow_far_pc_writing_face_layer"
    if writing.forehead:
        "sb_trippleblow_far_pc_writing_forehead_layer"
    if skin_effect.face:
        "sb_trippleblow_far_pc_face_freckles_layer"
    always "sb_trippleblow_far_pc_face_blush_layer"


    always "sb_trippleblow_far_pc_hair_back_layer"
    always "sb_trippleblow_far_pc_hair_front_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
