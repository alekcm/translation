image pub_undress_bg_layer:
    "pub_undress_bg_" + loc_cur.loc_type

image pub_undress_pc_legs_straight_base_layer:
    "pub_undress_pc_legs_straight_base"
    skin_base_colour_transform()
image pub_undress_pc_legs_straight_shad_layer:
    "pub_undress_pc_legs_straight_shad"
    skin_shad_colour_transform()

image pub_undress_pc_legs_straight_pants_takeoff_base_layer:
    "pub_undress_pc_legs_straight_pants_takeoff_base"
    skin_base_colour_transform()
image pub_undress_pc_legs_straight_pants_takeoff_shad_layer:
    "pub_undress_pc_legs_straight_pants_takeoff_shad"
    skin_shad_colour_transform()

image pub_undress_pc_legs_up_base_layer:
    "pub_undress_pc_legs_up_base"
    skin_base_colour_transform()
image pub_undress_pc_legs_up_shad_layer:
    "pub_undress_pc_legs_up_shad"
    skin_shad_colour_transform()

image pub_undress_pc_legs_up_arms_base_layer:
    "pub_undress_pc_legs_up_arms_base"
    skin_base_colour_transform()
image pub_undress_pc_legs_up_arms_shad_layer:
    "pub_undress_pc_legs_up_arms_shad"
    skin_shad_colour_transform()


image pub_undress_man_base_layer:
    "pub_undress_man_base"
    npc_skin_base_colour_transform()
image pub_undress_man_shad_layer:
    "pub_undress_man_shad"
    npc_skin_shad_colour_transform()
image pub_undress_man_pc_shad_layer:
    "pub_undress_man_pc_shad"
    skin_shad_colour_transform()

image pub_undress_pc_spank_layer:
    "pub_undress_pc_spank"
    opacity_transform(bruise.ass)

image pub_undress = LayeredImageProxy("pub_undress_layered", Transform(align=(0.8, 0.0)))

layeredimage pub_undress_layered:

    always:
        "pub_undress_bg_layer"

    group activity:
        attribute stand default:
            "pub_undress_pc_legs_straight_base_layer"
        attribute stand default:
            "pub_undress_pc_legs_straight_shad_layer"


        attribute pants_off:
            "pub_undress_pc_legs_straight_base_layer"
        attribute pants_off:
            "pub_undress_pc_legs_straight_shad_layer"

        attribute socks_off:
            "pub_undress_pc_legs_up_base_layer"
        attribute socks_off:
            "pub_undress_pc_legs_up_shad_layer"
        attribute socks_off:
            "pub_undress_pc_legs_up_socks"
        attribute socks_off:
            "pub_undress_pc_legs_up_arms_base_layer"
        attribute socks_off:
            "pub_undress_pc_legs_up_arms_shad_layer"

    if acc.anus:
        "pub_undress_pc_plug"

    if c.socks:
        if_any ["stand", "pants_off"] "pub_undress_pc_legs_straight_socks"

    if c.pants:
        if_any ["stand"] "pub_undress_pc_legs_straight_pants"
    if c.pants:
        if_any ["socks_off"] "pub_undress_pc_legs_up_pants"

    always:
        "pub_undress_pc_spank_layer"

    always:
        "pub_undress_pc_dress"

    group activity:
        attribute pants_off:
            "pub_undress_pc_legs_straight_pants_takeoff_base_layer"
        attribute pants_off:
            "pub_undress_pc_legs_straight_pants_takeoff_shad_layer"
        attribute pants_off:
            "pub_undress_pc_legs_straight_pants_takeoff_pants"


    group man_group:
        attribute man:
            "pub_undress_man_pc_shad_layer"
        attribute man:
            "pub_undress_man_base_layer"
        attribute man:
            "pub_undress_man_shad_layer"

        attribute no_man default:
            null

    always:
        "pub_undress_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
