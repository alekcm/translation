image mastside_main_base_layer:
    "mastside_main_base"
    skin_base_colour_transform()
image mastside_main_shad_layer:
    "mastside_main_shad"
    skin_shad_colour_transform()

image mastside_body_base_layer:
    get_skin_filename("mastside_body_base", preg=True)
    skin_base_colour_transform()
image mastside_body_shad_layer:
    get_skin_filename("mastside_body_shad", preg=True)
    skin_shad_colour_transform()

image mastside_main_nails_layered:
    "mastside_body_nails_" + str(player.pregnancy)
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image mastside_body_nip_layer:
    get_skin_filename("mastside_body_nip", breasts=True)
    nipple_colour_transform()
image mastside_body_navring_layer:
    get_skin_filename("mastside_body_navring", True)
    accessories_secondary_colour_transform("navelring")

layeredimage mastside:

    always:
        "mastside_bg"

    always "mastside_main_base_layer"
    always "mastside_main_shad_layer"

    always "mastside_body_base_layer"
    always "mastside_body_shad_layer"
    if player.pregnancy in (0,1):
        "mastside_body_nip_layer"
    if acc.navelring == 1:
        "mastside_body_navring_layer"

    if acc.nails == 1:
        "mastside_main_nails_layered"
    if acc.nails == 1:
        "mastside_body_nails_layered"

    always:
        "mastside_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
