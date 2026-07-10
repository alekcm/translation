image pen_anal_2_base_layer:
    get_skin_filename("pen_anal_2_base", False)
    skin_base_colour_transform()
image pen_anal_2_shad_layer:
    get_skin_filename("pen_anal_2_shad", False)
    skin_shad_colour_transform()
image pen_anal_2_vag_layer:
    get_skin_filename("pen_anal_2_vag", False)
    vagina_colour_transform()
image pen_anal_2_phair_layer:
    "pen_anal_2_phair"
    phair_colour_transform()

image pen_anal_2 = LayeredImageProxy("pen_anal_2_layer", Transform(align=(0.3, 0.67)))
image pen_vag_1_impact:
    "pen_impact_loop"
    xalign 0.08
    yalign 1.15

layeredimage pen_anal_2_layer:

    if player.beingraped:
        "pen_anal_2_bgred"
    else:
        "pen_anal_2_bgpink"
    always:
        "pen_anal_2_base_layer"
    always:
        "pen_anal_2_shad_layer"
    always:
        "pen_anal_2_vag_layer"
    always:
        "pen_anal_2_frame"
    if player.cum_locations["cum_assin"]:
        "pen_anal_2_cum"
    if player.phair:
        "pen_anal_2_phair_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
