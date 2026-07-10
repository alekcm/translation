
image diary_bio_body_base_base_layer:
    "diary_bio_body_base_base"
    skin_base_colour_transform()
image diary_bio_body_base_shad_layer:
    "diary_bio_body_base_shad"
    skin_shad_colour_transform()
image diary_bio_body_base_nails_layer:
    "diary_bio_body_base_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image diary_bio_body_base_phair_layer:
    "diary_bio_body_base_phair"
    phair_colour_transform()

image diary_bio_body_belly_base_layer:
    get_skin_filename("diary_bio_body_belly_base", preg=True)
    skin_base_colour_transform()
image diary_bio_body_belly_shad_layer:
    get_skin_filename("diary_bio_body_belly_shad", preg=True)
    skin_shad_colour_transform()
image diary_bio_body_navring_layer:
    get_skin_filename("diary_bio_body_navring", True)
    accessories_secondary_colour_transform("navelring")

image diary_bio_body_breasts_base_layer:
    get_skin_filename("diary_bio_body_breasts_base", breasts=True)
    skin_base_colour_transform()
image diary_bio_body_breasts_shad_layer:
    get_skin_filename("diary_bio_body_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image diary_bio_body_breasts_nips_layer:
    get_skin_filename("diary_bio_body_breasts_nips", breasts=True)
    nipple_colour_transform()
image diary_bio_body_breasts_nipring_layer:
    get_skin_filename("diary_bio_body_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image diary_bio_body_breasts_tattoo_layer:
    get_skin_filename("diary_bio_body_breasts_tattoo", breasts=True)


image diary_bio_face_freckles_layer:
    "diary_bio_face_freckles"
    skin_shad_colour_transform()

image diary_bio_face_mouth_lipstick_layer:
    "diary_bio_face_mouth_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image diary_bio_face_eyeshadow_layer:
    "diary_bio_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image diary_bio_face_eye_eyeliner_layer:
    "diary_bio_face_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image diary_bio_face_eye_iris_layer:
    "diary_bio_face_eye_iris"
    eye_colour_transform()

image diary_bio_face_brow_layer:
    "diary_bio_face_brow"
    hair_colour_transform()

image diary_bio_face_blush_layer:
    "diary_bio_face_blush"
    blush_opacity_transform()

image diary_bio_body_writing_forehead_layer:
    "diary_bio_body_writing_forehead"
    writing_transform("forehead")
image diary_bio_body_writing_face_layer:
    "diary_bio_body_writing_face"
    writing_transform("face")
image diary_bio_body_writing_chest_layer:
    "diary_bio_body_writing_chest"
    writing_transform("chest")
image diary_bio_body_writing_pubic_layer:
    "diary_bio_body_writing_pubic"
    writing_transform("pubic")
image diary_bio_body_writing_belly_layer:
    "diary_bio_body_writing_belly_" + str(player.pregnancy)
    writing_transform("belly")

image diary_bio_body_spank_layer:
    "diary_bio_body_spank"
    opacity_transform(bruise.ass)


image diary_bio_hair_back_bun_2 = "diary_bio_hair_back_bun"
image diary_bio_hair_back_bun_3 = "diary_bio_hair_back_bun"
image diary_bio_hair_back_bun_4 = "diary_bio_hair_back_bun"
image diary_bio_hair_back_pony_2 = "diary_bio_hair_back_bun"
image diary_bio_hair_back_pony_3 = "diary_bio_hair_back_pony_4"


image diary_bio_hair_back_layer:
    get_hair_back_cg_filename("diary_bio_hair_back")
    hair_colour_transform()

image diary_bio_hair_front_layer:
    get_hair_front_cg_filename("diary_bio_hair_front")
    hair_colour_transform()

layeredimage diary_bio_layered:

    always  "diary_bio_body_base_base_layer"
    always "diary_bio_body_base_shad_layer"
    always "diary_bio_body_spank_layer"
    always "diary_bio_body_base_nails_layer"

    if writing.pubic:
        "diary_bio_body_writing_pubic_layer"
    if player.phair:
        "diary_bio_body_base_phair_layer"

    if player.pregnancy:
        "diary_bio_body_belly_base_layer"
    if player.pregnancy:
        "diary_bio_body_belly_shad_layer"
    if acc.navelring:
        "diary_bio_body_navring_layer"

    always "diary_bio_body_breasts_base_layer"
    always "diary_bio_body_breasts_shad_layer"
    always "diary_bio_body_breasts_nips_layer"
    if acc.nipring:
        "diary_bio_body_breasts_nipring_layer"
    if tattoo.chest:
        "diary_bio_body_breasts_tattoo_layer"

    if skin_effect.face:
        "diary_bio_face_freckles_layer"
    if player.shy:
        "diary_bio_face_blush_layer"
    always "diary_bio_face_mouth_lipstick_layer"
    always "diary_bio_face_mouth"
    always "diary_bio_face_eyeshadow_layer"
    always "diary_bio_face_eye_iris_layer"
    always "diary_bio_face_eye_eye"
    always "diary_bio_face_eye_eyeliner_layer"
    always "diary_bio_face_brow_layer"

    if writing.forehead:
        "diary_bio_body_writing_forehead_layer"
    if writing.face:
        "diary_bio_body_writing_face_layer"
    if writing.chest:
        "diary_bio_body_writing_chest_layer"
    if writing.belly:
        "diary_bio_body_writing_belly_layer"

    always "diary_bio_hair_back_layer"
    always "diary_bio_hair_front_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
