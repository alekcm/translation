image pub_tablesex_main_phair_layer:
    "pub_tablesex_main_phair"
    phair_colour_transform()

image pub_tablesex_enjoy_base_layer:
    get_skin_filename("pub_tablesex_enjoy_base", False)
    skin_base_colour_transform()
image pub_tablesex_enjoy_shad_layer:
    get_skin_filename("pub_tablesex_enjoy_shad", False)
    skin_shad_colour_transform()

image pub_tablesex_forward_base_layer:
    get_skin_filename("pub_tablesex_forward_base", False)
    skin_base_colour_transform()
image pub_tablesex_forward_shad_layer:
    get_skin_filename("pub_tablesex_forward_shad", False)
    skin_shad_colour_transform()

image pub_tablesex_forward_arm_hjob_base_layer:
    get_skin_filename("pub_tablesex_forward_arm_hjob_base", False)
    skin_base_colour_transform()
image pub_tablesex_forward_arm_hjob_shad_layer:
    get_skin_filename("pub_tablesex_forward_arm_hjob_shad", False)
    skin_shad_colour_transform()

image pub_tablesex_forward_arm_rel_base_layer:
    get_skin_filename("pub_tablesex_forward_arm_rel_base", False)
    skin_base_colour_transform()
image pub_tablesex_forward_arm_rel_shad_layer:
    get_skin_filename("pub_tablesex_forward_arm_rel_shad", False)
    skin_shad_colour_transform()

image pub_tablesex_main_pc_base_layer:
    get_skin_filename("pub_tablesex_main_pc_base", False)
    skin_base_colour_transform()
image pub_tablesex_main_pc_shad_layer:
    get_skin_filename("pub_tablesex_main_pc_shad", False)
    skin_shad_colour_transform()



image pub_tablesex_main_man_base_layer:
    "pub_tablesex_main_man_base"
    npc_skin_base_colour_transform()
image pub_tablesex_main_man_shad_layer:
    "pub_tablesex_main_man_shad"
    npc_skin_shad_colour_transform()

image pub_tablesex_main_penis_in_base_layer:
    "pub_tablesex_main_penis_in_base"
    npc_skin_base_colour_transform()
image pub_tablesex_main_penis_in_shad_layer:
    "pub_tablesex_main_penis_in_shad"
    npc_skin_shad_colour_transform()

image pub_tablesex_main_penis_out_base_layer:
    "pub_tablesex_main_penis_out_base"
    npc_skin_base_colour_transform()
image pub_tablesex_main_penis_out_shad_layer:
    "pub_tablesex_main_penis_out_shad"
    npc_skin_shad_colour_transform()


image pub_serve_tablesex = LayeredImageProxy("pub_serve_tablesex_layered", Transform(align=(1.0, 0.0)))

layeredimage pub_serve_tablesex_layered:

    always:
        "pub_tablesex_bg"

    always:
        "pub_tablesex_main_man_base_layer"
    always:
        "pub_tablesex_main_man_shad_layer"

    group penis:
        attribute trousers default:
            "pub_tablesex_main_man_trousers"

    always:
        "pub_tablesex_main_pc_base_layer"
    always:
        "pub_tablesex_main_pc_shad_layer"
    always:
        "pub_tablesex_main_dress"
    if player.phair == 1:
        "pub_tablesex_main_phair_layer"
    if c.socks > 0:
        "pub_tablesex_main_socks"
    if c.pants > 0:
        "pub_tablesex_main_pants"


    group penis:
        attribute inside:
            "pub_tablesex_main_penis_in_base_layer"
        attribute inside:
            "pub_tablesex_main_penis_in_shad_layer"

        attribute outside:
            "pub_tablesex_main_penis_out_base_layer"
        attribute outside:
            "pub_tablesex_main_penis_out_shad_layer"


    group girl:
        attribute relax default:
            "pub_tablesex_forward_base_layer"
        attribute relax default:
            "pub_tablesex_forward_shad_layer"
        attribute relax default:
            "pub_tablesex_forward_dress"
        attribute relax default:
            "pub_tablesex_forward_arm_rel_base_layer"
        attribute relax default:
            "pub_tablesex_forward_arm_rel_shad_layer"

        attribute hjob:
            "pub_tablesex_forward_base_layer"
        attribute hjob:
            "pub_tablesex_forward_shad_layer"
        attribute hjob:
            "pub_tablesex_forward_dress"
        attribute hjob:
            "pub_tablesex_forward_arm_hjob_base_layer"
        attribute hjob:
            "pub_tablesex_forward_arm_hjob_shad_layer"



        attribute enjoy:
            "pub_tablesex_enjoy_base_layer"
        attribute enjoy:
            "pub_tablesex_enjoy_shad_layer"
        attribute enjoy:
            "pub_tablesex_enjoy_dress"

    always:
        "pub_tablesex_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
