
image sb_standassup_bg_layer:
    "sb_standassup_bg_" + loc_cur.loc_type


image sb_standassup_pc_body_base_layer:
    "sb_standassup_pc_body_base"
    skin_base_colour_transform()
image sb_standassup_pc_body_shad_layer:
    "sb_standassup_pc_body_shad"
    skin_shad_colour_transform()
image sb_standassup_pc_body_vag_layer:
    "sb_standassup_pc_body_vag"
    vagina_colour_transform()
image sb_standassup_pc_body_hair_layer:
    "sb_standassup_pc_body_hair"
    hair_colour_transform()

image sb_standassup_pc_belly_base_layer:
    "sb_standassup_pc_belly_base"
    skin_base_colour_transform()
image sb_standassup_pc_belly_shad_layer:
    "sb_standassup_pc_belly_shad"
    skin_shad_colour_transform()

image sb_standassup_pc_breasts_base_layer:
    get_skin_filename("sb_standassup_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_standassup_pc_breasts_shad_layer:
    get_skin_filename("sb_standassup_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_standassup_pc_breasts_nips_layer:
    get_skin_filename("sb_standassup_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_standassup_pc_breasts_nipring_layer:
    get_skin_filename("sb_standassup_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")


image sb_standassup_pc_face_eye_forward_iris_layer:
    "sb_standassup_pc_face_eye_forward_iris"
    eye_colour_transform()
image sb_standassup_pc_face_eye_forward_eyeliner_layer:
    "sb_standassup_pc_face_eye_forward_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_standassup_pc_face_eye_down_iris_layer:
    "sb_standassup_pc_face_eye_down_iris"
    eye_colour_transform()
image sb_standassup_pc_face_eye_down_eyeliner_layer:
    "sb_standassup_pc_face_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_standassup_pc_face_brow_neutral_layer:
    "sb_standassup_pc_face_brow_neutral"
    hair_colour_transform()


image sb_standassup_pc_face_mouth_oh_lipstick_layer:
    "sb_standassup_pc_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_standassup_pc_face_mouth_happy_lipstick_layer:
    "sb_standassup_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_standassup_pc_face_mouth_neutral_lipstick_layer:
    "sb_standassup_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_standassup_pc_face_mouth_gagged_lipstick_layer:
    "sb_standassup_pc_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_standassup_pc_face_mouth_gagged_base_layer:
    "sb_standassup_pc_face_mouth_gag_base"
    gag_colour_transform()
image sb_standassup_pc_face_mouth_gagged_metal_layer:
    "sb_standassup_pc_face_mouth_gag_metal"
    gag_metal_transform()


image sb_standassup_pc_face_blush_layer:
    "sb_standassup_pc_face_blush"
    blush_opacity_transform()
image sb_standassup_pc_face_freckles_layer:
    "sb_standassup_pc_face_freckles"
    skin_shad_colour_transform()
image sb_standassup_pc_face_eyeshadow_layer:
    "sb_standassup_pc_face_eyeshadow"
    eyeshadow_colour_transform()


image sb_standassup_pc_writing_ass_layer:
    "sb_standassup_pc_writing_ass"
    writing_transform("ass")
image sb_standassup_pc_writing_anus_layer:
    "sb_standassup_pc_writing_anus"
    writing_transform("anus")
image sb_standassup_pc_writing_lleg_layer:
    "sb_standassup_pc_writing_lleg"
    writing_transform("lleg")
image sb_standassup_pc_writing_forehead_layer:
    "sb_standassup_pc_writing_forehead"
    writing_transform("forehead")
image sb_standassup_pc_writing_face_layer:
    "sb_standassup_pc_writing_face"
    writing_transform("face")
image sb_standassup_pc_writing_belly_layer:
    "sb_standassup_pc_writing_belly_" + str(player.pregnancy)
    writing_transform("belly")
image sb_onfours_pc_body_spank_layer:
    "sb_onfours_pc_spank"
    opacity_transform(bruise.ass)



image sb_standassup_man_vag_base_layer:
    "sb_standassup_man_vag_base"
    npc_skin_base_colour_transform()
image sb_standassup_man_vag_shad_layer:
    "sb_standassup_man_vag_shad"
    npc_skin_shad_colour_transform()

image sb_standassup_man_vag_pc_base_layer:
    "sb_standassup_man_vag_pc_base"
    skin_base_colour_transform()
image sb_standassup_man_vag_pc_shad_layer:
    "sb_standassup_man_vag_pc_shad"
    skin_shad_colour_transform()
image sb_standassup_man_vag_pc_vag_layer:
    "sb_standassup_man_vag_pc_vag"
    vagina_colour_transform()


image sb_standassup_man_anal_base_layer:
    "sb_standassup_man_anal_base"
    npc_skin_base_colour_transform()
image sb_standassup_man_anal_shad_layer:
    "sb_standassup_man_anal_shad"
    npc_skin_shad_colour_transform()

image sb_standassup_man_anal_pc_shad_layer:
    "sb_standassup_man_anal_pc_shad"
    skin_shad_colour_transform()


image sb_standassup_man_poke_base_layer:
    "sb_standassup_man_poke_base"
    npc_skin_base_colour_transform()
image sb_standassup_man_poke_shad_layer:
    "sb_standassup_man_poke_shad"
    npc_skin_shad_colour_transform()

image sb_standassup = LayeredImageProxy("sb_standassup_layered", Transform(xalign = (0.7)))

layeredimage sb_standassup_layered:

    always "sb_standassup_bg_layer"

    always "sb_standassup_pc_body_base_layer"
    always "sb_standassup_pc_body_shad_layer"
    always "sb_standassup_pc_body_vag_layer"
    always "sb_standassup_pc_body_hair_layer"

    if player.showing:
        "sb_standassup_pc_belly_base_layer"
    if player.showing:
        "sb_standassup_pc_belly_shad_layer"

    if writing.ass:
        "sb_standassup_pc_writing_ass_layer"
    if writing.anus:
        "sb_standassup_pc_writing_anus_layer"
    if writing.face:
        "sb_standassup_pc_writing_face_layer"
    if writing.forehead:
        "sb_standassup_pc_writing_forehead_layer"
    if writing.lleg:
        "sb_standassup_pc_writing_lleg_layer"
    if writing.belly:
        "sb_standassup_pc_writing_belly_layer"

    if player.cum_locations["cum_assin"]:
        "sb_standassup_pc_cum_anus"
    if player.cum_locations["cum_vagin"]:
        "sb_standassup_pc_cum_vag"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_assout"]:
        "sb_standassup_pc_cum_ass"

    if acc.anus:
        "sb_standassup_pc_plug"
    group sex:
        attribute noman null default

        attribute vag "sb_standassup_man_vag_pc_vag_layer"
        attribute vag "sb_standassup_man_vag_pc_base_layer"
        attribute vag "sb_standassup_man_vag_pc_shad_layer"

        attribute anal "sb_standassup_man_anal_pc_shad_layer"

    always "sb_standassup_pc_breasts_base_layer"
    always "sb_standassup_pc_breasts_shad_layer"
    always "sb_standassup_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_standassup_pc_breasts_nipring_layer"

    if skin_effect.face:
        "sb_standassup_pc_face_freckles_layer"
    always "sb_standassup_pc_face_blush_layer"
    always "sb_standassup_pc_face_eyeshadow_layer"
    group eyes:
        attribute forward "sb_standassup_pc_face_eye_forward_iris_layer" default
        attribute forward "sb_standassup_pc_face_eye_forward_eye" default
        attribute forward "sb_standassup_pc_face_eye_forward_eyeliner_layer" default

        attribute down "sb_standassup_pc_face_eye_down_iris_layer"
        attribute down "sb_standassup_pc_face_eye_down_eye"
        attribute down "sb_standassup_pc_face_eye_down_eyeliner_layer"


    always "sb_standassup_pc_face_brow_neutral_layer"

    group mouth:
        attribute neutral "sb_standassup_pc_face_mouth_neutral_lipstick_layer" default
        attribute neutral "sb_standassup_pc_face_mouth_neutral" default

        attribute happy "sb_standassup_pc_face_mouth_happy_lipstick_layer"
        attribute happy "sb_standassup_pc_face_mouth_happy"

        attribute oh "sb_standassup_pc_face_mouth_oh_lipstick_layer"
        attribute oh "sb_standassup_pc_face_mouth_oh"

    if player.gagged:
        "sb_standassup_gagged_layered"

    group sex:
        attribute noman null default

        attribute vag "sb_standassup_man_vag_base_layer"
        attribute vag "sb_standassup_man_vag_shad_layer"

        attribute anal "sb_standassup_man_anal_base_layer"
        attribute anal "sb_standassup_man_anal_shad_layer"

        attribute poke "sb_standassup_man_poke_base_layer"
        attribute poke "sb_standassup_man_poke_shad_layer"

    always "sb_standassup_frame"


layeredimage sb_standassup_gagged_layered:
    always "sb_standassup_pc_face_mouth_gagged_lipstick_layer"
    always "sb_standassup_pc_face_mouth_gagged_base_layer"
    always "sb_standassup_pc_face_mouth_gagged_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
