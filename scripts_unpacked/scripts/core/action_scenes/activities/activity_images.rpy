image activity_bg_plaster = "activity_bg_room"
image activity_bg_tile = "activity_bg_room"

image activity_bg_layer:
    "activity_bg_" + loc_cur.loc_type
    skin_base_colour_transform()





image activity_dance_pc_base_layer:
    get_cg_filename("activity_dance_pc_base")
    skin_base_colour_transform()
image activity_dance_pc_shad_layer:
    get_cg_filename("activity_dance_pc_shad")
    skin_shad_colour_transform()

image activity_dance = LayeredImageProxy("activity_dance_layeredimage", Transform(align=(0.8, 0.2)))

layeredimage activity_dance_layeredimage:

    always:
        "activity_bg_layer"

    always:
        "activity_dance_main"

    always:
        "activity_dance_pc_base_layer"
    always:
        "activity_dance_pc_shad_layer"

    always:
        "activity_frame"





image activity_run_pc_base_layer:
    get_cg_filename("activity_run_pc_base")
    skin_base_colour_transform()
image activity_run_pc_shad_layer:
    get_cg_filename("activity_run_pc_shad")
    skin_shad_colour_transform()

image activity_run = LayeredImageProxy("activity_run_layeredimage", Transform(align=(0.8, 0.2)))

layeredimage activity_run_layeredimage:

    always:
        "activity_bg_layer"

    always:
        "activity_run_main"
    always:
        "activity_run_pc_base_layer"
    always:
        "activity_run_pc_shad_layer"

    always:
        "activity_frame"





image activity_soccer_pc_base_layer:
    get_cg_filename("activity_soccer_pc_base")
    skin_base_colour_transform()
image activity_soccer_pc_shad_layer:
    get_cg_filename("activity_soccer_pc_shad")
    skin_shad_colour_transform()


image activity_soccer = LayeredImageProxy("activity_soccer_layeredimage", Transform(align=(0.8, 0.2)))


layeredimage activity_soccer_layeredimage:

    always:
        "activity_bg_layer"

    always:
        "activity_soccer_main"
    always:
        "activity_soccer_pc_base_layer"
    always:
        "activity_soccer_pc_shad_layer"

    always:
        "activity_frame"





image activity_walk_pc_base_layer:
    get_cg_filename("activity_walk_pc_base")
    skin_base_colour_transform()
image activity_walk_pc_shad_layer:
    get_cg_filename("activity_walk_pc_shad")
    skin_shad_colour_transform()


image activity_walk = LayeredImageProxy("activity_walk_layeredimage", Transform(align=(0.8, 0.2)))


layeredimage activity_walk_layeredimage:

    always:
        "activity_bg_layer"

    always:
        "activity_walk_pc_base_layer"
    always:
        "activity_walk_pc_shad_layer"
    always:
        "activity_walk_main"

    always:
        "activity_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
