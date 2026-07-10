image sb_cowgirl_pc_sit_base_layer:
    "sb_cowgirl_pc_sit_base"
    skin_base_colour_transform()
image sb_cowgirl_pc_sit_shad_layer:
    "sb_cowgirl_pc_sit_shad"
    skin_shad_colour_transform()

image sb_cowgirl_pc_up_base_layer:
    "sb_cowgirl_pc_up_base"
    skin_base_colour_transform()
image sb_cowgirl_pc_up_shad_layer:
    "sb_cowgirl_pc_up_shad"
    skin_shad_colour_transform()
image sb_cowgirl_pc_up_vag_layer:
    "sb_cowgirl_pc_up_vag"
    vagina_colour_transform()

image sb_cowgirl_man_base_layer:
    "sb_cowgirl_man_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_shad_layer:
    "sb_cowgirl_man_shad"
    npc_skin_shad_colour_transform()

image sb_cowgirl_man_penis_cheeks_base_layer:
    "sb_cowgirl_man_penis_cheeks_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_penis_cheeks_shad_layer:
    "sb_cowgirl_man_penis_cheeks_shad"
    npc_skin_shad_colour_transform()

image sb_cowgirl_man_penis_poke_base_layer:
    "sb_cowgirl_man_penis_poke_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_penis_poke_shad_layer:
    "sb_cowgirl_man_penis_poke_shad"
    npc_skin_shad_colour_transform()

image sb_cowgirl_man_penis_vag_base_layer:
    "sb_cowgirl_man_penis_vag_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_penis_vag_shad_layer:
    "sb_cowgirl_man_penis_vag_shad"
    npc_skin_shad_colour_transform()

image sb_cowgirl_man_penis_ass_base_layer:
    "sb_cowgirl_man_penis_ass_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_penis_ass_shad_layer:
    "sb_cowgirl_man_penis_ass_shad"
    npc_skin_shad_colour_transform()

image sb_cowgirl_man_penis_cheeks_base_layer:
    "sb_cowgirl_man_penis_cheeks_base"
    npc_skin_base_colour_transform()
image sb_cowgirl_man_penis_cheeks_shad_layer:
    "sb_cowgirl_man_penis_cheeks_shad"
    npc_skin_shad_colour_transform()
image sb_cowgirl = LayeredImageProxy("sb_cowgirl_layered", Transform(xalign = (0.80)))

layeredimage sb_cowgirl_layered:
    always "sb_cowgirl_bg"

    always "sb_cowgirl_man_base_layer"
    always "sb_cowgirl_man_shad_layer"

    group pc:

        attribute pose default if_any ["vag", "ass", "out"] "sb_cowgirl_pc_sit_base_layer"
        attribute pose default if_any ["vag", "ass", "out"] "sb_cowgirl_pc_sit_shad_layer"

        attribute pose default if_any "poke" "sb_cowgirl_pc_up_base_layer"
        attribute pose default if_any "poke" "sb_cowgirl_pc_up_shad_layer"
        attribute pose default if_any "poke" "sb_cowgirl_pc_up_vag_layer"

    if tattoo.ass:
        if_any "sit" "sb_cowgirl_pc_sit_tattoo"


    group penis:
        attribute out default "sb_cowgirl_man_penis_cheeks_base_layer"
        attribute out default "sb_cowgirl_man_penis_cheeks_shad_layer"

        attribute poke "sb_cowgirl_man_penis_poke_base_layer"
        attribute poke "sb_cowgirl_man_penis_poke_shad_layer"

        attribute vag "sb_cowgirl_man_penis_vag_base_layer"
        attribute vag "sb_cowgirl_man_penis_vag_shad_layer"

        attribute ass "sb_cowgirl_man_penis_ass_base_layer"
        attribute ass "sb_cowgirl_man_penis_ass_shad_layer"


    always "sb_cowgirl_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
