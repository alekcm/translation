

image pub_lapsit_talk_pc_body_base_layer:
    "pub_lapsit_talk_pc_body_base"
    skin_base_colour_transform()
image pub_lapsit_talk_pc_body_shad_layer:
    "pub_lapsit_talk_pc_body_shad"
    skin_shad_colour_transform()

image pub_lapsit_talk_pc_larm_hold_base_layer:
    "pub_lapsit_talk_pc_larm_hold_base"
    skin_base_colour_transform()
image pub_lapsit_talk_pc_larm_hold_shad_layer:
    "pub_lapsit_talk_pc_larm_hold_shad"
    skin_shad_colour_transform()
image pub_lapsit_talk_pc_larm_mast_base_layer:
    "pub_lapsit_talk_pc_larm_mast_base"
    skin_base_colour_transform()
image pub_lapsit_talk_pc_larm_mast_shad_layer:
    "pub_lapsit_talk_pc_larm_mast_shad"
    skin_shad_colour_transform()

image pub_lapsit_talk_pc_breasts_base_layer:
    get_skin_filename("pub_lapsit_talk_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image pub_lapsit_talk_pc_breasts_shad_layer:
    get_skin_filename("pub_lapsit_talk_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image pub_lapsit_talk_pc_breasts_col_layer:
    get_skin_filename("pub_lapsit_talk_pc_breasts_col", breasts=True)
image pub_lapsit_talk_pc_breasts_tattoo_layer:
    get_skin_filename("pub_lapsit_talk_pc_breasts_tattoo", breasts=True)
image pub_lapsit_talk_pc_writing_chest_layer:
    "pub_lapsit_talk_pc_writing_chest"
    writing_transform("chest")

image pub_lapsit_talk_man_base_layer:
    "pub_lapsit_talk_man_base"
    npc_skin_base_colour_transform()
image pub_lapsit_talk_man_shad_layer:
    "pub_lapsit_talk_man_shad"
    npc_skin_shad_colour_transform()

image pub_lapsit_talk_man_larm_mast_base_layer:
    "pub_lapsit_talk_man_larm_mast_base"
    npc_skin_base_colour_transform()

image pub_lapsit_talk_man_larm_hold_base_layer:
    "pub_lapsit_talk_man_larm_hold_base"
    npc_skin_base_colour_transform()
image pub_lapsit_talk_man_larm_hold_shad_layer:
    "pub_lapsit_talk_man_larm_hold_shad"
    npc_skin_shad_colour_transform()

image pub_lapsit_talk_man_penis_base_layer:
    "pub_lapsit_talk_man_penis_base"
    npc_skin_base_colour_transform()
image pub_lapsit_talk_man_penis_shad_layer:
    "pub_lapsit_talk_man_penis_shad"
    npc_skin_shad_colour_transform()

image pub_serve_lap talk = LayeredImageProxy("pub_serve_lap_talk", Transform(align=(0.8, 0.0)))

layeredimage pub_serve_lap_talk:

    always:
        "pub_lapsit_bg"



    group pc_larm:
        attribute hold default:
            "pub_lapsit_talk_pc_larm_hold_base_layer"
        attribute hold default:
            "pub_lapsit_talk_pc_larm_hold_shad_layer"

    always:
        "pub_lapsit_talk_man_rarm_hold"
    always:
        "pub_lapsit_talk_man_base_layer"
    always:
        "pub_lapsit_talk_man_shad_layer"
    always:
        "pub_lapsit_talk_man_col"
    always:
        "pub_lapsit_talk_pc_body_base_layer"
    always:
        "pub_lapsit_talk_pc_body_shad_layer"
    always:
        "pub_lapsit_talk_pc_dress"

    group sit_penis_group:
        attribute no_penis default:
            null
        attribute penis:
            "pub_lapsit_talk_man_penis_base_layer"
        attribute penis:
            "pub_lapsit_talk_man_penis_shad_layer"

    group man_talk_rarm:

        attribute man_mast:
            "pub_lapsit_talk_man_larm_mast_base_layer"
        attribute man_mast:
            "pub_lapsit_talk_man_larm_mast_col"

    group pc_larm:
        attribute mast:
            "pub_lapsit_talk_pc_larm_mast_base_layer"
        attribute mast:
            "pub_lapsit_talk_pc_larm_mast_shad_layer"

    if player.pregnancy >= 2:
        "pub_lapsit_talk_pc_belly"
    always:
        "pub_lapsit_talk_pc_breasts_base_layer"
    always:
        "pub_lapsit_talk_pc_breasts_shad_layer"
    always:
        "pub_lapsit_talk_pc_breasts_col_layer"
    if tattoo.chest:
        "pub_lapsit_talk_pc_breasts_tattoo_layer"
    if writing.chest:
        "pub_lapsit_talk_pc_writing_chest_layer"
    if c.socks:
        "pub_lapsit_talk_pc_socks"

    group man_talk_rarm:
        attribute rest default:
            "pub_lapsit_talk_man_larm_hold_base_layer"
        attribute rest default:
            "pub_lapsit_talk_man_larm_hold_shad_layer"
        attribute rest default:
            "pub_lapsit_talk_man_larm_hold_col"

    always:
        "pub_lapsit_frame"



image pub_lapsit_hump_pc_body_base_layer:
    "pub_lapsit_hump_pc_body_base"
    skin_base_colour_transform()
image pub_lapsit_hump_pc_body_shad_layer:
    "pub_lapsit_hump_pc_body_shad"
    skin_shad_colour_transform()

image pub_lapsit_hump_pc_breasts_layer:
    get_skin_filename("pub_lapsit_hump_pc_breasts", breasts=True)

image pub_lapsit_hump_man_arm_base_layer:
    "pub_lapsit_hump_man_arm_base"
    npc_skin_base_colour_transform()
image pub_lapsit_hump_man_arm_shad_layer:
    "pub_lapsit_hump_man_arm_shad"
    npc_skin_shad_colour_transform()

image pub_lapsit_hump_man_penis_base_layer:
    "pub_lapsit_hump_man_penis_base"
    npc_skin_base_colour_transform()
image pub_lapsit_hump_man_penis_shad_layer:
    "pub_lapsit_hump_man_penis_shad"
    npc_skin_shad_colour_transform()


image pub_serve_lap hump = LayeredImageProxy("pub_serve_lap_hump", Transform(align=(0.8, 0.0)))

layeredimage pub_serve_lap_hump:

    always:
        "pub_lapsit_bg"

    always:
        "pub_lapsit_talk_man_base_layer"
    always:
        "pub_lapsit_talk_man_shad_layer"
    always:
        "pub_lapsit_hump_man_col"

    group penis:
        attribute rub:
            "pub_lapsit_hump_man_penis_base_layer"
        attribute rub:
            "pub_lapsit_hump_man_penis_shad_layer"

        attribute no_penis default:
            null

        attribute penis_in:
            null

    always:
        "pub_lapsit_hump_pc_body_base_layer"
    always:
        "pub_lapsit_hump_pc_body_shad_layer"
    always:
        "pub_lapsit_hump_man_arm_base_layer"
    always:
        "pub_lapsit_hump_man_arm_shad_layer"
    always:
        "pub_lapsit_hump_man_arm_col"
    if c.socks:
        "pub_lapsit_hump_pc_socks"
    always:
        "pub_lapsit_hump_pc_dress"
    if player.pregnancy >= 2:
        "pub_lapsit_hump_pc_belly"
    always:
        "pub_lapsit_hump_pc_breasts_layer"

    always:
        "pub_lapsit_frame"



image pub_lapsit_prep_pc_body_base_layer:
    "pub_lapsit_prep_pc_body_base"
    skin_base_colour_transform()
image pub_lapsit_prep_pc_body_shad_layer:
    "pub_lapsit_prep_pc_body_shad"
    skin_shad_colour_transform()

image pub_lapsit_prep_pc_breasts_layer:
    get_skin_filename("pub_lapsit_prep_pc_breasts", breasts=True)

image pub_lapsit_prep_man_arm_base_layer:
    "pub_lapsit_prep_man_arm_base"
    npc_skin_base_colour_transform()
image pub_lapsit_prep_man_arm_shad_layer:
    "pub_lapsit_prep_man_arm_shad"
    npc_skin_shad_colour_transform()

image pub_lapsit_prep_man_penis_layer:
    "pub_lapsit_prep_man_penis"
    npc_skin_shad_colour_transform()

image pub_serve_lap prep = LayeredImageProxy("pub_serve_lap_prep", Transform(align=(0.8, 0.0)))

layeredimage pub_serve_lap_prep:
    always:
        "pub_lapsit_bg"

    always:
        "pub_lapsit_talk_man_base_layer"
    always:
        "pub_lapsit_talk_man_shad_layer"
    always:
        "pub_lapsit_prep_man_col"

    always:
        "pub_lapsit_prep_man_penis_layer"

    always:
        "pub_lapsit_prep_pc_body_base_layer"
    always:
        "pub_lapsit_prep_pc_body_shad_layer"
    always:
        "pub_lapsit_prep_man_arm_base_layer"
    always:
        "pub_lapsit_prep_man_arm_shad_layer"
    always:
        "pub_lapsit_prep_man_arm_col"
    if c.socks:
        "pub_lapsit_prep_pc_socks"
    always:
        "pub_lapsit_prep_pc_dress"
    if player.pregnancy >= 2:
        "pub_lapsit_prep_pc_belly"
    always:
        "pub_lapsit_prep_pc_breasts_layer"

    always:
        "pub_lapsit_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
