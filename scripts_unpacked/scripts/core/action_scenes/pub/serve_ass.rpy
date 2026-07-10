image pub_serving_ass_pc_base_layer:
    "pub_serving_ass_pc_base"
    skin_base_colour_transform()
image pub_serving_ass_pc_shad_layer:
    "pub_serving_ass_pc_shad"
    skin_shad_colour_transform()
image pub_serving_ass_pc_vag_layer:
    "pub_serving_ass_pc_vag"
    vagina_colour_transform()

image pub_serving_ass_pc_dress_breasts_layer:
    get_skin_filename("pub_serving_ass_pc_dress_breasts", breasts=True)

image pub_serving_ass_pc_spank_layer:
    "pub_serving_ass_pc_spank"
    opacity_transform(bruise.ass)

image pub_serving_ass_pc_writing_ass_layer:
    "pub_serving_ass_pc_writing_ass"
    writing_transform("ass")
image pub_serving_ass_pc_writing_anus_layer:
    "pub_serving_ass_pc_writing_anus_layer"
    writing_transform("anus")



image pub_serving_ass_man_idle_base_layer:
    "pub_serving_ass_man_idle_base"
    npc_skin_base_colour_transform()

image pub_serving_ass_man_grope_base_layer:
    "pub_serving_ass_man_grope_base"
    npc_skin_base_colour_transform()
image pub_serving_ass_man_grope_shad_layer:
    "pub_serving_ass_man_grope_shad"
    npc_skin_shad_colour_transform()

image pub_serve_ass = LayeredImageProxy("pub_serve_ass_layered", Transform(align=(0.9, 0.0)))

layeredimage pub_serve_ass_layered:

    always:
        "pub_serving_ass_bg"

    always:
        "pub_serving_ass_pc_base_layer"
    always:
        "pub_serving_ass_pc_shad_layer"
    always:
        "pub_serving_ass_pc_vag_layer"

    if acc.anus:
        "pub_serving_ass_pc_plug"
    always:
        "pub_serving_ass_pc_spank_layer"
    if writing.ass:
        "pub_serving_ass_pc_writing_ass"
    if writing.anus:
        "pub_serving_ass_pc_writing_anus"

    if c.socks:
        "pub_serving_ass_pc_socks"
    if c.pants:
        "pub_serving_ass_pc_pants"

    always:
        "pub_serving_ass_pc_dress_main"
    always:
        "pub_serving_ass_pc_dress_breasts_layer"
    if player.pregnancy >= 2:
        "pub_serving_ass_pc_dress_belly"

    group groper:

        attribute grope:
            "pub_serving_ass_man_grope_base_layer"
        attribute grope:
            "pub_serving_ass_man_grope_shad_layer"
        attribute grope:
            "pub_serving_ass_man_grope_lines"

        attribute nogrope default:
            "pub_serving_ass_man_idle_base_layer"
        attribute nogrope default:
            "pub_serving_ass_man_idle_lines"

    always:
        "pub_serving_ass_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
