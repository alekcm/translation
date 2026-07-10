
image sb_mast_stand_bg_beach = "sb_mast_stand_bg_grass"
image sb_mast_stand_bg_layer:
    "sb_mast_stand_bg_" + loc_cur.loc_type


image sb_mast_stand_pc_body_base_layer:
    "sb_mast_stand_pc_body_base"
    skin_base_colour_transform()
image sb_mast_stand_pc_body_shad_layer:
    "sb_mast_stand_pc_body_shad"
    skin_shad_colour_transform()
image sb_mast_stand_pc_body_nails_layer:
    "sb_mast_stand_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image sb_mast_stand_pc_phair_layer:
    "sb_mast_stand_pc_phair"
    phair_colour_transform()

image sb_mast_stand_pc_belly_base_layer:
    get_skin_filename("sb_mast_stand_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_mast_stand_pc_belly_shad_layer:
    get_skin_filename("sb_mast_stand_pc_belly_shad", preg=True)
    skin_shad_colour_transform()

image sb_mast_stand_pc_breasts_base_layer:
    get_skin_filename("sb_mast_stand_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_mast_stand_pc_breasts_shad_layer:
    get_skin_filename("sb_mast_stand_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image sb_mast_stand_pc_breats_nips_layer:
    get_skin_filename("sb_mast_stand_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_mast_stand_pc_breasts_nipring_layer:
    get_skin_filename("sb_mast_stand_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_mast_stand_pc_breasts_tattoo_layer:
    get_skin_filename("sb_mast_stand_pc_breasts_tattoo", breasts=True)


image sb_mast_stand_pc_writing_belly_layer:
    get_skin_filename("sb_mast_stand_pc_writing_belly", preg=True)
    writing_transform("belly")
image sb_mast_stand_pc_writing_pubic_layer:
    "sb_mast_stand_pc_writing_pubic"
    writing_transform("pubic")

image sb_mast_stand_pc_navring_layer:
    get_skin_filename("sb_mast_stand_pc_navring", True)
    accessories_secondary_colour_transform("navelring")

image sb_mast_stand_effect_rain_loop:
    "sb_mast_stand_effect_rain1"
    .03
    "sb_mast_stand_effect_rain2"
    .03
    "sb_mast_stand_effect_rain3"
    .03
    repeat

image sb_mast_stand = LayeredImageProxy("sb_mast_stand_layerd", Transform(xalign = (0.8)))

layeredimage sb_mast_stand_layerd:
    always "sb_mast_stand_bg_layer"

    always "sb_mast_stand_pc_body_base_layer"
    always "sb_mast_stand_pc_body_shad_layer"
    always "sb_mast_stand_pc_body_nails_layer"

    always "sb_mast_stand_pc_breasts_base_layer"
    always "sb_mast_stand_pc_breasts_shad_layer"
    always "sb_mast_stand_pc_breats_nips_layer"
    if tattoo.chest:
        "sb_mast_stand_pc_breasts_tattoo_layer"
    if acc.nipring:
        "sb_mast_stand_pc_breasts_nipring_layer"

    if writing.pubic:
        "sb_mast_stand_pc_writing_pubic_layer"
    if player.phair:
        "sb_mast_stand_pc_phair_layer"
    if player.pregnancy:
        "sb_mast_stand_pc_belly_base_layer"
    if player.pregnancy:
        "sb_mast_stand_pc_belly_shad_layer"
    if writing.belly:
        "sb_mast_stand_pc_writing_belly_layer"
    if acc.navelring:
        "sb_mast_stand_pc_navring_layer"

    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_mast_stand_effect_rain_loop"
    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_mast_stand_effect_steam"

    always "sb_mast_stand_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
