image sb_scissoring_pc_base_layer:
    "sb_scissoring_pc_base"
    skin_base_colour_transform()
image sb_scissoring_pc_shad_layer:
    "sb_scissoring_pc_shad"
    skin_shad_colour_transform()



image sb_scissoring_pc_breasts_base_layer:
    get_skin_filename("sb_scissoring_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_scissoring_pc_breasts_shad_layer:
    get_skin_filename("sb_scissoring_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_scissoring_pc_breasts_nips_layer:
    get_skin_filename("sb_scissoring_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_scissoring_pc_breasts_nipring_layer:
    get_skin_filename("sb_scissoring_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_scissoring_pc_hair_layer:
    "sb_scissoring_pc_hair"
    hair_colour_transform()

image sb_scissoring = LayeredImageProxy("sb_scissoring_layered", Transform(align=(0.8, 0.0)))

layeredimage sb_scissoring_layered:
    always "sb_scissoring_bg"

    group girl:
        attribute dani default "sb_scissoring_dani"

    always "sb_scissoring_pc_base_layer"
    always "sb_scissoring_pc_shad_layer"

    always "sb_scissoring_pc_breasts_base_layer"
    always "sb_scissoring_pc_breasts_shad_layer"
    always "sb_scissoring_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_scissoring_pc_breasts_nipring_layer"

    always "sb_scissoring_pc_hair_layer"

    always "sb_scissoring_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
