
image diary_stats_body_base_layer:
    "diary_stats_body_base"
    skin_base_colour_transform()
image diary_stats_body_shad_layer:
    "diary_stats_body_shad"
    skin_shad_colour_transform()

image diary_stats_belly_base_layer:
    get_skin_filename("diary_stats_belly_base", preg=True)
    skin_base_colour_transform()
image diary_stats_belly_shad_layer:
    get_skin_filename("diary_stats_belly_shad", preg=True)
    skin_shad_colour_transform()

image diary_stats_breasts_base_layer:
    get_skin_filename("diary_stats_breasts_base", breasts=True)
    skin_base_colour_transform()
image diary_stats_breasts_shad_layer:
    get_skin_filename("diary_stats_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image diary_stats_breasts_nips_layer:
    get_skin_filename("diary_stats_breasts_nips", breasts=True)
    nipple_colour_transform()
image diary_stats_breasts_nipring_layer:
    get_skin_filename("diary_stats_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image diary_stats_body_spank_layer:
    "diary_stats_body_spank"
    opacity_transform(bruise.ass)

image diary_stats_body_writing_anal_layer:
    "diary_stats_body_writing_anal"
    writing_transform("anus")
image diary_stats_body_writing_counter_layer:
    "diary_stats_body_writing_counter"
    writing_transform("ass")

layeredimage diary_stats_layered:

    always "diary_stats_belly_base_layer"
    always "diary_stats_belly_shad_layer"

    always "diary_stats_breasts_base_layer"
    always "diary_stats_breasts_shad_layer"
    always "diary_stats_breasts_nips_layer"
    if acc.nipring:
        "diary_stats_breasts_nipring_layer"
    always "diary_stats_body_base_layer"
    always "diary_stats_body_shad_layer"

    if tattoo.ass:
        "diary_stats_body_tattoo_tramp"
    always "diary_stats_body_spank_layer"
    if writing.anus:
        "diary_stats_body_writing_anal_layer"
    if writing.ass:
        "diary_stats_body_writing_counter_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
