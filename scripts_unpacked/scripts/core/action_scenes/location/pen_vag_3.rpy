image pen_vag_3_base_layer:
    get_skin_filename("pen_vag_3_base", False)
    skin_base_colour_transform()
image pen_vag_3_shad_layer:
    get_skin_filename("pen_vag_3_shad", False)
    skin_shad_colour_transform()
image pen_vag_3_vag_layer:
    get_skin_filename("pen_vag_3_vag", False)
    vagina_colour_transform()
image pen_vag_3_phair_layer:
    "pen_vag_3_phair"
    phair_colour_transform()

image pen_vag_3 = LayeredImageProxy("pen_vag_3_layer", Transform(align=(0.3, 0.67)))
image pen_vag_3_impact:
    "pen_impact_loop"
    xalign 0.08
    yalign 1.15

layeredimage pen_vag_3_layer:

    always:
        "pen_vag_3_bg"
    always:
        "pen_vag_3_base_layer"
    always:
        "pen_vag_3_shad_layer"
    always:
        "pen_vag_3_vag_layer"
    always:
        "pen_vag_3_frame"
    if player.cum_locations["cum_vagin"]:
        "pen_vag_3_cum"
    if player.phair:
        "pen_vag_3_phair_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
