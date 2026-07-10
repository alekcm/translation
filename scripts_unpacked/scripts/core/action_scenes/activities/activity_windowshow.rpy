image activity_pinkroom_ass_body_base_layer:
    "activity_pinkroom_ass_body_base"
    skin_base_colour_transform()
image activity_pinkroom_ass_body_shad_layer:
    "activity_pinkroom_ass_body_shad"
    skin_shad_colour_transform()

image activity_pinkroom_ass_breasts_base_layer:
    get_skin_filename("activity_pinkroom_ass_breasts_base", breasts=True)
    skin_base_colour_transform()
image activity_pinkroom_ass_breasts_shad_layer:
    get_skin_filename("activity_pinkroom_ass_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image activity_pinkroom_ass_belly_base_layer:
    "activity_pinkroom_ass_belly_base"
    skin_base_colour_transform()
image activity_pinkroom_ass_belly_shad_layer:
    "activity_pinkroom_ass_belly_shad"
    skin_shad_colour_transform()

image activity_pinkroom_ass_spank_layer:
    "activity_pinkroom_ass_spank"
    opacity_transform(bruise.ass)

image activity_pinkroom_ass_writing_ass_layer:
    "activity_pinkroom_ass_writing_ass"
    writing_transform("ass")
image activity_pinkroom_ass_writing_anus_layer:
    "activity_pinkroom_ass_writing_anus"
    writing_transform("anus")


image activity_windowshow_ass = LayeredImageProxy("activity_windowshow_ass_layeredimage", Transform(align=(0.8, 0.0)))

layeredimage activity_windowshow_ass_layeredimage:
    always "activity_pinkroom_bg"

    always "activity_pinkroom_ass_breasts_base_layer"
    always "activity_pinkroom_ass_breasts_shad_layer"
    always "activity_pinkroom_ass_body_base_layer"
    always "activity_pinkroom_ass_body_shad_layer"
    if player.pregnancy >= 2:
        "activity_pinkroom_ass_belly_base_layer"
    if player.pregnancy >= 2:
        "activity_pinkroom_ass_belly_shad_layer"

    always "activity_pinkroom_ass_spank_layer"

    if writing.ass:
        "activity_pinkroom_ass_writing_ass_layer"
    if writing.anus:
        "activity_pinkroom_ass_writing_anus_layer"
    if tattoo.ass:
        "activity_pinkroom_ass_tattoo_tramp"

    always "activity_pinkroom_frame"

    group sale:
        attribute sale "activity_pinkroom_forsale" default
        attribute nosale null





image activity_pinkroom_front_body_base_layer:
    "activity_pinkroom_front_body_base"
    skin_base_colour_transform()
image activity_pinkroom_front_body_shad_layer:
    "activity_pinkroom_front_body_shad"
    skin_shad_colour_transform()

image activity_pinkroom_front_belly_base_2 = "activity_pinkroom_front_belly_base_3"
image activity_pinkroom_front_belly_shad_2 = "activity_pinkroom_front_belly_shad_3"
image activity_pinkroom_front_belly_base_layer:
    get_skin_filename("activity_pinkroom_front_belly_base", preg=True)
    skin_base_colour_transform()
image activity_pinkroom_front_belly_shad_layer:
    get_skin_filename("activity_pinkroom_front_belly_shad", preg=True)
    skin_shad_colour_transform()

image activity_pinkroom_front_breasts_base_layer:
    get_skin_filename("activity_pinkroom_front_breasts_base", breasts=True)
    skin_base_colour_transform()
image activity_pinkroom_front_breasts_shad_layer:
    get_skin_filename("activity_pinkroom_front_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image activity_pinkroom_front_breasts_nips_layer:
    get_skin_filename("activity_pinkroom_front_breasts_nips", breasts=True)
    nipple_colour_transform()
image activity_pinkroom_front_breasts_nipring_layer:
    get_skin_filename("activity_pinkroom_front_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image activity_pinkroom_front_breasts_tattoo_layer:
    get_skin_filename("activity_pinkroom_front_breasts_tattoo", breasts=True)

image activity_pinkroom_front_writing_ass_layer:
    "activity_pinkroom_front_writing_ass"
    writing_transform("ass")
image activity_pinkroom_front_writing_chest_layer:
    "activity_pinkroom_front_writing_chest"
    writing_transform("chest")
image activity_pinkroom_front_writing_pubic_layer:
    "activity_pinkroom_front_writing_pubic"
    writing_transform("pubic")
image activity_pinkroom_front_writing_lleg_layer:
    "activity_pinkroom_front_writing_lleg"
    writing_transform("lleg")
image activity_pinkroom_front_writing_belly_2 = "activity_pinkroom_front_writing_belly_3"
image activity_pinkroom_front_writing_belly_layer:
    get_skin_filename("activity_pinkroom_front_writing_belly", preg=True)
    writing_transform("belly")

image activity_pinkroom_front_phair_layer:
    "activity_pinkroom_front_phair"
    phair_colour_transform()

image activity_pinkroom_front_navring_2 = "activity_pinkroom_front_navring_3"
image activity_pinkroom_front_navring_layer:
    get_skin_filename("activity_pinkroom_front_navring", True)
    accessories_secondary_colour_transform("navelring")

image activity_windowshow_front = LayeredImageProxy("activity_windowshow_front_layeredimage", Transform(align=(0.8, 0.0)))

layeredimage activity_windowshow_front_layeredimage:
    always "activity_pinkroom_bg"

    always "activity_pinkroom_front_body_base_layer"
    always "activity_pinkroom_front_body_shad_layer"

    if player.pregnancy:
        "activity_pinkroom_front_belly_base_layer"
    if player.pregnancy:
        "activity_pinkroom_front_belly_shad_layer"

    always "activity_pinkroom_front_breasts_base_layer"
    always "activity_pinkroom_front_breasts_shad_layer"
    always "activity_pinkroom_front_breasts_nips_layer"
    if tattoo.chest:
        "activity_pinkroom_front_breasts_tattoo_layer"
    if acc.nipring:
        "activity_pinkroom_front_breasts_nipring_layer"

    if writing.ass:
        "activity_pinkroom_front_writing_ass_layer"
    if writing.belly:
        "activity_pinkroom_front_writing_belly_layer"
    if writing.chest:
        "activity_pinkroom_front_writing_chest_layer"
    if writing.lleg:
        "activity_pinkroom_front_writing_lleg_layer"
    if writing.pubic:
        "activity_pinkroom_front_writing_pubic_layer"

    if player.phair:
        "activity_pinkroom_front_phair_layer"

    if acc.navelring:
        "activity_pinkroom_front_navring_layer"

    always "activity_pinkroom_frame"

    group sale:
        attribute sale "activity_pinkroom_forsale" default
        attribute nosale null
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
