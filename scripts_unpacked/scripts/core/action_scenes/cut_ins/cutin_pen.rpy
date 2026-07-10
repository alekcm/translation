



image cutin_pen_1_pc_base_layer:
    "cutin_pen_1_pc_base"
    skin_base_colour_transform()
image cutin_pen_1_pc_shad_layer:
    "cutin_pen_1_pc_shad"
    skin_shad_colour_transform()
image cutin_pen_1_pc_vag_layer:
    "cutin_pen_1_pc_vag"
    vagina_colour_transform()
image cutin_pen_1_pc_phair_layer:
    "cutin_pen_1_pc_phair"
    phair_colour_transform()


image cutin_pen_1_penis_vag_base_layer:
    "cutin_pen_1_penis_vag_base"
    npc_skin_base_colour_transform()
image cutin_pen_1_penis_vag_shad_layer:
    "cutin_pen_1_penis_vag_shad"
    npc_skin_shad_colour_transform()
image cutin_pen_1_penis_vag_vag_layer:
    "cutin_pen_1_penis_vag_vag"
    vagina_colour_transform()


image cutin_pen_1_penis_anal_base_layer:
    "cutin_pen_1_penis_anal_base"
    npc_skin_base_colour_transform()
image cutin_pen_1_penis_anal_shad_layer:
    "cutin_pen_1_penis_anal_shad"
    npc_skin_shad_colour_transform()
image cutin_pen_1_penis_anal_vag_layer:
    "cutin_pen_1_penis_anal_vag"
    vagina_colour_transform()


image cutin_pen_1_penis_poke_base_layer:
    "cutin_pen_1_penis_poke_base"
    npc_skin_base_colour_transform()
image cutin_pen_1_penis_poke_shad_layer:
    "cutin_pen_1_penis_poke_shad"
    npc_skin_shad_colour_transform()

image cutin_pen_1 = LayeredImageProxy("cutin_pen_1_layerd", Transform(xalign = (1.00)))

layeredimage cutin_pen_1_layerd:
    always "cutin_pen_1_bg"

    always "cutin_pen_1_pc_base_layer"
    always "cutin_pen_1_pc_shad_layer"
    always "cutin_pen_1_pc_vag_layer"

    if player.phair:
        "cutin_pen_1_pc_phair_layer"

    group penis:
        attribute vag "cutin_pen_1_penis_vag_vag_layer"
        attribute vag "cutin_pen_1_penis_vag_base_layer"
        attribute vag "cutin_pen_1_penis_vag_shad_layer"

        attribute anal "cutin_pen_1_penis_anal_vag_layer"
        attribute anal "cutin_pen_1_penis_anal_base_layer"
        attribute anal "cutin_pen_1_penis_anal_shad_layer"

        attribute poke "cutin_pen_1_penis_poke_base_layer"
        attribute poke "cutin_pen_1_penis_poke_shad_layer"

    if player.cum_locations["cum_vagin"]:
        if_any "vag" "cutin_pen_1_penis_vag_cum"
    if player.cum_locations["cum_assin"]:
        if_any "anal" "cutin_pen_1_penis_anal_cum"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_belly"]:
        if_any "poke" "cutin_pen_1_penis_vag_cum"
    always "cutin_pen_1_frame"





image cutin_pen_2_pc_base_layer:
    "cutin_pen_2_pc_base"
    skin_base_colour_transform()
image cutin_pen_2_pc_shad_layer:
    "cutin_pen_2_pc_shad"
    skin_shad_colour_transform()
image cutin_pen_2_pc_vag_layer:
    "cutin_pen_2_pc_vag"
    vagina_colour_transform()
image cutin_pen_2_pc_phair_layer:
    "cutin_pen_2_pc_phair"
    phair_colour_transform()


image cutin_pen_2_penis_vag_base_layer:
    "cutin_pen_2_penis_vag_base"
    npc_skin_base_colour_transform()
image cutin_pen_2_penis_vag_shad_layer:
    "cutin_pen_2_penis_vag_shad"
    npc_skin_shad_colour_transform()
image cutin_pen_2_penis_vag_vag_layer:
    "cutin_pen_2_penis_vag_vag"
    vagina_colour_transform()


image cutin_pen_2_penis_anal_base_layer:
    "cutin_pen_2_penis_anal_base"
    npc_skin_base_colour_transform()
image cutin_pen_2_penis_anal_shad_layer:
    "cutin_pen_2_penis_anal_shad"
    npc_skin_shad_colour_transform()
image cutin_pen_2_penis_anal_vag_layer:
    "cutin_pen_2_penis_anal_vag"
    vagina_colour_transform()


image cutin_pen_2_penis_poke_base_layer:
    "cutin_pen_2_penis_poke_base"
    npc_skin_base_colour_transform()
image cutin_pen_2_penis_poke_shad_layer:
    "cutin_pen_2_penis_poke_shad"
    npc_skin_shad_colour_transform()

image cutin_pen_2 = LayeredImageProxy("cutin_pen_2_layerd", Transform(xalign = (1.00)))

layeredimage cutin_pen_2_layerd:
    always "cutin_pen_2_bg"

    always "cutin_pen_2_pc_base_layer"
    always "cutin_pen_2_pc_shad_layer"
    always "cutin_pen_2_pc_vag_layer"

    if player.phair:
        "cutin_pen_2_pc_phair_layer"

    group penis:
        attribute vag "cutin_pen_2_penis_vag_vag_layer"
        attribute vag "cutin_pen_2_penis_vag_base_layer"
        attribute vag "cutin_pen_2_penis_vag_shad_layer"

        attribute anal "cutin_pen_2_penis_anal_vag_layer"
        attribute anal "cutin_pen_2_penis_anal_base_layer"
        attribute anal "cutin_pen_2_penis_anal_shad_layer"

        attribute poke "cutin_pen_2_penis_poke_base_layer"
        attribute poke "cutin_pen_2_penis_poke_shad_layer"

    if player.cum_locations["cum_vagin"]:
        if_any "vag" "cutin_pen_2_penis_vag_cum"
    if player.cum_locations["cum_assin"]:
        if_any "anal" "cutin_pen_2_penis_anal_cum"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_belly"]:
        if_any "poke" "cutin_pen_2_penis_vag_cum"
    always "cutin_pen_2_frame"





image cutin_pen_3_pc_base_layer:
    "cutin_pen_3_pc_base"
    skin_base_colour_transform()
image cutin_pen_3_pc_shad_layer:
    "cutin_pen_3_pc_shad"
    skin_shad_colour_transform()
image cutin_pen_3_pc_vag_layer:
    "cutin_pen_3_pc_vag"
    vagina_colour_transform()


image cutin_pen_3_penis_vag_base_layer:
    "cutin_pen_3_penis_vag_base"
    npc_skin_base_colour_transform()
image cutin_pen_3_penis_vag_shad_layer:
    "cutin_pen_3_penis_vag_shad"
    npc_skin_shad_colour_transform()
image cutin_pen_3_penis_vag_vag_layer:
    "cutin_pen_3_penis_vag_vag"
    vagina_colour_transform()


image cutin_pen_3_penis_anal_base_layer:
    "cutin_pen_3_penis_anal_base"
    npc_skin_base_colour_transform()
image cutin_pen_3_penis_anal_shad_layer:
    "cutin_pen_3_penis_anal_shad"
    npc_skin_shad_colour_transform()


image cutin_pen_3_penis_poke_base_layer:
    "cutin_pen_3_penis_poke_base"
    npc_skin_base_colour_transform()
image cutin_pen_3_penis_poke_shad_layer:
    "cutin_pen_3_penis_poke_shad"
    npc_skin_shad_colour_transform()

image cutin_pen_3 = LayeredImageProxy("cutin_pen_3_layerd", Transform(xalign = (1.00)))

layeredimage cutin_pen_3_layerd:
    always "cutin_pen_3_bg"

    always "cutin_pen_3_pc_base_layer"
    always "cutin_pen_3_pc_shad_layer"
    always "cutin_pen_3_pc_vag_layer"

    group penis:
        attribute vag "cutin_pen_3_penis_vag_vag_layer"
        attribute vag "cutin_pen_3_penis_vag_base_layer"
        attribute vag "cutin_pen_3_penis_vag_shad_layer"

        attribute anal "cutin_pen_3_penis_anal_base_layer"
        attribute anal "cutin_pen_3_penis_anal_shad_layer"

        attribute poke "cutin_pen_3_penis_poke_base_layer"
        attribute poke "cutin_pen_3_penis_poke_shad_layer"

    if player.cum_locations["cum_vagin"]:
        if_any "vag" "cutin_pen_3_penis_vag_cum"
    if player.cum_locations["cum_assin"]:
        if_any "anal" "cutin_pen_3_penis_anal_cum"
    if player.cum_locations["cum_vagout"] or player.cum_locations["cum_belly"]:
        if_any "poke" "cutin_pen_3_penis_vag_cum"
    always "cutin_pen_3_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
