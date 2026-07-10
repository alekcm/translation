image sb_pose_lookback_bg_layer:
    "sb_pose_lookback_bg_" + loc_cur.loc_type


image sb_pose_lookback_belly_base_layer:
    get_skin_filename("sb_pose_lookback_belly_base", preg=True)
    skin_base_colour_transform()
image sb_pose_lookback_belly_shad_layer:
    get_skin_filename("sb_pose_lookback_belly_shad", preg=True)
    skin_shad_colour_transform()
image sb_pose_lookback_nip_layer:
    get_skin_filename("sb_pose_lookback_nip", breasts=True)
    nipple_colour_transform()
image sb_pose_lookback_nipring_layer:
    get_skin_filename("sb_pose_lookback_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_pose_lookback_breasts_base_layer:
    get_skin_filename("sb_pose_lookback_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_pose_lookback_breasts_shad_layer:
    get_skin_filename("sb_pose_lookback_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image sb_pose_lookback_body_base_layer:
    get_skin_filename("sb_pose_lookback_body_base")
    skin_base_colour_transform()
image sb_pose_lookback_body_shad_layer:
    get_skin_filename("sb_pose_lookback_body_shad")
    skin_shad_colour_transform()

image sb_pose_lookback_shorts_base_layer:
    get_cg_clothing_filename("sb_pose_lookback_shorts_base", preg=True)
    pants_primary_colour_transform()
image sb_pose_lookback_shorts_trim_layer:
    get_cg_clothing_filename("sb_pose_lookback_shorts_trim", preg=True)
    pants_secondary_colour_transform()

image sb_pose_lookback_briefs_base_layer:
    get_cg_clothing_filename("sb_pose_lookback_briefs_base")
    pants_primary_colour_transform()
image sb_pose_lookback_briefs_trim_layer:
    get_cg_clothing_filename("sb_pose_lookback_briefs_trim")
    pants_secondary_colour_transform()

image sb_pose_lookback_thong_layer:
    get_cg_clothing_filename("sb_pose_lookback_thong")
    pants_primary_colour_transform()


image sb_pose_lookback_eye_iris_layer:
    "sb_pose_lookback_eye_iris"
    eye_colour_transform()
image sb_pose_lookback_eye_eyeliner_layer:
    "sb_pose_lookback_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_pose_lookback_eyeshadow_layer:
    "sb_pose_lookback_eyeshadow"
    eyeshadow_colour_transform()
image sb_pose_lookback_freckles_layer:
    "sb_pose_lookback_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_pose_lookback_blush_layer:
    "sb_pose_lookback_blush"
    blush_opacity_transform()
image sb_pose_lookback_spank_layer:
    "sb_pose_lookback_spank"
    opacity_transform(bruise.ass)

image sb_pose_lookback_brow_neutral_layer:
    "sb_pose_lookback_brow_neutral"
    hair_colour_transform()
image sb_pose_lookback_brow_happy_layer:
    "sb_pose_lookback_brow_happy"
    hair_colour_transform()
image sb_pose_lookback_brow_worried_layer:
    "sb_pose_lookback_brow_worried"
    hair_colour_transform()

image sb_pose_lookback_mouth_normal_lipstick_layer:
    "sb_pose_lookback_mouth_normal_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_lookback_mouth_frown_lipstick_layer:
    "sb_pose_lookback_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_lookback_mouth_tounge_lipstick_layer:
    "sb_pose_lookback_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))
image sb_pose_lookback_mouth_happy_lipstick_layer:
    "sb_pose_lookback_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If(acc.lipstick and acc.makeup_on, 1, 0))

image sb_pose_lookback_hair_back_bun_2 = "sb_pose_lookback_hair_back_bun"
image sb_pose_lookback_hair_back_bun_3 = "sb_pose_lookback_hair_back_bun"
image sb_pose_lookback_hair_back_bun_4 = "sb_pose_lookback_hair_back_bun"
image sb_pose_lookback_hair_back_pony_4 = "sb_pose_lookback_hair_back_pony_3"

image sb_pose_lookback_hair_back_layer:
    get_hair_back_cg_filename("sb_pose_lookback_hair_back")
    hair_colour_transform()
image sb_pose_lookback_hair_front_layer:
    get_hair_front_cg_filename("sb_pose_lookback_hair_front")
    hair_colour_transform()

image sb_pose_lookback_effect_rain:
    "sb_pose_lookback_effect_rain1"
    .03
    "sb_pose_lookback_effect_rain2"
    .03
    "sb_pose_lookback_effect_rain3"
    .03
    repeat

layeredimage sb_pose_lookback:

    always "sb_pose_lookback_bg_layer"

    always "sb_pose_lookback_belly_base_layer"
    always "sb_pose_lookback_belly_shad_layer"

    always "sb_pose_lookback_breasts_base_layer"
    always "sb_pose_lookback_breasts_shad_layer"

    always "sb_pose_lookback_nip_layer"
    if acc.nipring:
        "sb_pose_lookback_nipring_layer"

    always "sb_pose_lookback_body_base_layer"
    always "sb_pose_lookback_body_shad_layer"
    if c.pants and not c.thong:
        "sb_pose_lookback_briefs_base_layer"
    if c.pants and not c.thong:
        "sb_pose_lookback_briefs_trim_layer"

    if writing.face:
        "sb_pose_lookback_writing_face"
    if writing.forehead:
        "sb_pose_lookback_writing_forehead"
    if writing.ass:
        "sb_pose_lookback_writing_ass"
    if writing.anus:
        "sb_pose_lookback_writing_anus"
    if tattoo.ass:
        "sb_pose_lookback_tat_tramp"

    always "sb_pose_lookback_spank_layer"

    if c.pants and c.thong:
        "sb_pose_lookback_thong_layer"

    if acc.eyeshadow and acc.makeup_on:
        "sb_pose_lookback_eyeshadow_layer"
    always "sb_pose_lookback_eye_iris_layer"
    always "sb_pose_lookback_eye_eye"
    always "sb_pose_lookback_eye_eyeliner_layer"

    always "sb_pose_lookback_freckles_layer"
    always "sb_pose_lookback_blush_layer"

    group brows:
        attribute neutral default:
            "sb_pose_lookback_brow_neutral_layer"
        attribute worried:
            "sb_pose_lookback_brow_worried_layer"
        attribute happy:
            "sb_pose_lookback_brow_happy_layer"

    group mouth:
        attribute normal default:
            "sb_pose_lookback_mouth_normal_lipstick_layer"
        attribute normal default:
            "sb_pose_lookback_mouth_normal"

        attribute frown:
            "sb_pose_lookback_mouth_frown_lipstick_layer"
        attribute frown:
            "sb_pose_lookback_mouth_frown"

        attribute smile:
            "sb_pose_lookback_mouth_happy_lipstick_layer"
        attribute smile:
            "sb_pose_lookback_mouth_happy"

        attribute tounge:
            "sb_pose_lookback_mouth_tounge_lipstick_layer"
        attribute tounge:
            "sb_pose_lookback_mouth_tounge"

    always:
        "sb_pose_lookback_hair_back_layer"
    always:
        "sb_pose_lookback_hair_front_layer"

    group showerg:
        attribute noshower default null
        attribute shower null

    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_pose_lookback_effect_rain"
    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_pose_lookback_effect_steam"
    always:
        "sb_pose_lookback_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
