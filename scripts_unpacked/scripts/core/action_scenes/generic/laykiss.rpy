
image sb_laykiss_pc_base_layer:
    "sb_laykiss_pc_base"
    skin_base_colour_transform()
image sb_laykiss_pc_shad_layer:
    "sb_laykiss_pc_shad"
    skin_shad_colour_transform()


image sb_laykiss_pc_breasts_base_layer:
    get_skin_filename("sb_laykiss_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_laykiss_pc_breasts_nips_layer:
    get_skin_filename("sb_laykiss_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_laykiss_pc_breasts_nipring_layer:
    get_skin_filename("sb_laykiss_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")


image sb_laykiss_pc_hair_back_bun_2 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_bun_3 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_bun_4 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_pony_2 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_pony_3 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_pony_4 = "sb_laykiss_pc_hair_back_bun"
image sb_laykiss_pc_hair_back_pig_2 = "sb_laykiss_pc_hair_back_pig"
image sb_laykiss_pc_hair_back_pig_3 = "sb_laykiss_pc_hair_back_pig"
image sb_laykiss_pc_hair_back_pig_4 = "sb_laykiss_pc_hair_back_pig"

image sb_laykiss_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_laykiss_pc_hair_front")
    hair_colour_transform()
image sb_laykiss_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_laykiss_pc_hair_back")
    hair_colour_transform()


image sb_laykiss_pc_face_eye_open_iris_layer:
    "sb_laykiss_pc_face_eye_open_iris"
    eye_colour_transform()
image sb_laykiss_pc_face_eye_open_eyeliner_layer:
    "sb_laykiss_pc_face_eye_open_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_laykiss_pc_face_eye_closed_eyeliner_layer:
    "sb_laykiss_pc_face_eye_closed_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_laykiss_pc_face_brow_layer:
    "sb_laykiss_pc_face_brow"
    hair_colour_transform()

image sb_laykiss = LayeredImageProxy("sb_laykiss_layered", Transform(xalign = (0.9)))

layeredimage sb_laykiss_layered:
    always "sb_laykiss_bg"

    always "sb_laykiss_pc_base_layer"
    always "sb_laykiss_pc_shad_layer"

    always "sb_laykiss_pc_breasts_base_layer"
    always "sb_laykiss_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_laykiss_pc_breasts_nipring_layer"

    group eye:
        attribute open default "sb_laykiss_pc_face_eye_open_iris_layer"
        attribute open default "sb_laykiss_pc_face_eye_open_eye"
        attribute open default "sb_laykiss_pc_face_eye_open_eyeliner_layer"

        attribute closed "sb_laykiss_pc_face_eye_closed_eyeliner_layer"

    always "sb_laykiss_pc_face_brow_layer"

    always "sb_laykiss_pc_hair_back_layer"
    always "sb_laykiss_pc_hair_front_layer"

    always "sb_laykiss_dani"

    group clothes:
        attribute naked default null

        attribute strapon "sb_laykiss_dani_strapon"

        attribute underwear "sb_laykiss_dani_sleepwear"

    always "sb_laykiss_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
