image pub_talking_table_pc_body_base_layer:
    "pub_talking_table_pc_body_base"
    skin_base_colour_transform()
image pub_talking_table_pc_body_shad_layer:
    "pub_talking_table_pc_body_shad"
    skin_shad_colour_transform()

image pub_talking_table_pc_breasts_col_layer:
    get_skin_filename("pub_talking_table_pc_breasts_col", breasts=True)
image pub_talking_table_pc_breasts_tattoo_layer:
    get_skin_filename("pub_talking_table_pc_breasts_tattoo", breasts=True)
image pub_talking_table_pc_breasts_base_layer:
    get_skin_filename("pub_talking_table_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image pub_talking_table_pc_breasts_shad_layer:
    get_skin_filename("pub_talking_table_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image pub_talking_table_man_rarm_grope_base_layer:
    "pub_talking_table_man_rarm_grope_base"
    npc_skin_base_colour_transform()
image pub_talking_table_man_rarm_grope_shad_layer:
    "pub_talking_table_man_rarm_grope_shad"
    npc_skin_shad_colour_transform()

image pub_talking_table_man_rarm_down_base_layer:
    "pub_talking_table_man_rarm_down_base"
    npc_skin_base_colour_transform()
image pub_talking_table_man_rarm_down_shad_layer:
    "pub_talking_table_man_rarm_down_shad"
    npc_skin_shad_colour_transform()

image pub_talking_table_man_larm_mast_base_layer:
    "pub_talking_table_man_larm_mast_base"
    npc_skin_base_colour_transform()
image pub_talking_table_man_larm_mast_shad_layer:
    "pub_talking_table_man_larm_mast_shad"
    npc_skin_shad_colour_transform()

image pub_talking_table_man_rarm_down_base_layer:
    "pub_talking_table_man_rarm_down_base"
    npc_skin_base_colour_transform()
image pub_talking_table_man_rarm_down_shad_layer:
    "pub_talking_table_man_rarm_down_shad"
    npc_skin_shad_colour_transform()



image pub_serve_talking = LayeredImageProxy("pub_serve_talking_layered", Transform(align=(0.8, 0.0)))

layeredimage pub_serve_talking_layered:

    always:
        "pub_talking_table_bg"
    always:
        "pub_talking_table_pc_body_base_layer"
    always:
        "pub_talking_table_pc_body_shad_layer"

    if c.pants:
        "pub_talking_table_pc_pants"
    always:
        "pub_talking_table_pc_dress"
    if player.pregnancy >= 2:
        "pub_talking_table_pc_dress_belly"

    group rarm:

        attribute touch:
            "pub_talking_table_man_rarm_grope_base_layer"
        attribute touch:
            "pub_talking_table_man_rarm_grope_shad_layer"
        attribute touch:
            "pub_talking_table_man_rarm_grope_col"

    if c.socks:
        "pub_talking_table_pc_socks"

    always:
        "pub_talking_table_pc_breasts_base_layer"
    always:
        "pub_talking_table_pc_breasts_shad_layer"




    always:
        "pub_talking_table_pc_breasts_col_layer"


    group rarm:
        attribute rest default:
            "pub_talking_table_man_rarm_down_base_layer"
        attribute rest default:
            "pub_talking_table_man_rarm_down_shad_layer"
        attribute rest default:
            "pub_talking_table_man_rarm_down_col"

    always:
        "pub_talking_table_man_base"

    group larm:
        attribute down default:
            "pub_talking_table_man_larm_down"

        attribute mast:
            "pub_talking_table_man_larm_mast_base_layer"
        attribute mast:
            "pub_talking_table_man_larm_mast_shad_layer"
        attribute mast:
            "pub_talking_table_man_larm_mast_col"


    always:
        "pub_talking_table_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
