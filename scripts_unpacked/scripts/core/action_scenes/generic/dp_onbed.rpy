
image sb_dpbed_bg_plaster = "sb_dpbed_bg_room"
image sb_dpbed_bg_conc = "sb_dpbed_bg_room"
image sb_dpbed_bg_layer:
    "sb_dpbed_bg_" + loc_cur.loc_type



image sb_dpbed_pc_body_base_layer:
    get_skin_filename("sb_dpbed_pc_body_base")
    skin_base_colour_transform()
image sb_dpbed_pc_body_shad_layer:
    get_skin_filename("sb_dpbed_pc_body_shad")
    skin_shad_colour_transform()
image sb_dpbed_pc_body_vag_layer:
    get_skin_filename("sb_dpbed_pc_body_vag")
    vagina_colour_transform()
image sb_dpbed_pc_body_nails_layer:
    "sb_dpbed_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))



image sb_dpbed_pc_det_spank_layer:
    "sb_dpbed_pc_det_spank"
    opacity_transform(bruise.ass)
image sb_dpbed_pc_det_phair_layer:
    "sb_dpbed_pc_det_phair"
    phair_colour_transform()

image sb_dpbed_pc_writing_ass_layer:
    "sb_dpbed_pc_writing_ass"
    writing_transform("ass")
image sb_dpbed_pc_writing_anus_layer:
    "sb_dpbed_pc_writing_anus"
    writing_transform("anus")



image sb_dpbed_manlay_poke_base_layer:
    "sb_dpbed_manlay_poke_base"
    npc_skin_base_colour_transform()
image sb_dpbed_manlay_poke_shad_layer:
    "sb_dpbed_manlay_poke_shad"
    npc_skin_shad_colour_transform()

image sb_dpbed_manlay_vag_base_layer:
    "sb_dpbed_manlay_vag_base"
    npc_skin_base_colour_transform()
image sb_dpbed_manlay_vag_shad_layer:
    "sb_dpbed_manlay_vag_shad"
    npc_skin_shad_colour_transform()

image sb_dpbed_manlay_anal_base_layer:
    "sb_dpbed_manlay_anal_base"
    npc_skin_base_colour_transform()
image sb_dpbed_manlay_anal_shad_layer:
    "sb_dpbed_manlay_anal_shad"
    npc_skin_shad_colour_transform()

image sb_dpbed_manlay_grope_base_layer:
    "sb_dpbed_manlay_grope_base"
    npc_skin_base_colour_transform()
image sb_dpbed_manlay_grope_shad_layer:
    "sb_dpbed_manlay_grope_shad"
    npc_skin_shad_colour_transform()



image sb_dpbed_manbehind_poke_base_layer:
    "sb_dpbed_manbehind_poke_base"
    npc2_skin_base_colour_transform()
image sb_dpbed_manbehind_poke_shad_layer:
    "sb_dpbed_manbehind_poke_shad"
    npc2_skin_shad_colour_transform()

image sb_dpbed_manbehind_anal_base_layer:
    "sb_dpbed_manbehind_anal_base"
    npc2_skin_base_colour_transform()
image sb_dpbed_manbehind_anal_shad_layer:
    "sb_dpbed_manbehind_anal_shad"
    npc2_skin_shad_colour_transform()

image sb_dpbed = LayeredImageProxy("sb_dpbed_layered", Transform(xalign = (0.80)))

layeredimage sb_dpbed_layered:

    always "sb_dpbed_bg_layer"

    always "sb_dpbed_pc_body_base_layer"
    always "sb_dpbed_pc_body_shad_layer"
    always "sb_dpbed_pc_body_vag_layer"

    always "sb_dpbed_pc_det_spank_layer"
    if player.phair:
        "sb_dpbed_pc_det_phair_layer"
    if writing.ass:
        "sb_dpbed_pc_writing_ass_layer"
    if writing.anus:
        "sb_dpbed_pc_writing_anus_layer"

    if player.cum_locations["cum_vagin"]:
        "sb_dpbed_pc_cum_vagin"
    if player.cum_locations["cum_assin"]:
        "sb_dpbed_pc_cum_assin"
    if player.cum_locations["cum_assout"]:
        "sb_dpbed_pc_cum_assout"
    if player.cum_locations["cum_vagout"]:
        "sb_dpbed_pc_cum_vagout"

    if acc.anus:
        "sb_dpbed_pc_det_plug"

    group manlay:
        attribute poke default "sb_dpbed_manlay_poke_base_layer"
        attribute poke default "sb_dpbed_manlay_poke_shad_layer"

        attribute vag "sb_dpbed_manlay_vag_base_layer"
        attribute vag "sb_dpbed_manlay_vag_shad_layer"

        attribute anal "sb_dpbed_manlay_anal_base_layer"
        attribute anal "sb_dpbed_manlay_anal_shad_layer"

    if (t.minute % 2) == 0:
        "sb_dpbed_manlay_grope_base_layer"
    if (t.minute % 2) == 0:
        "sb_dpbed_manlay_grope_shad_layer"

    group manbehind:
        attribute b_noman default null

        attribute bpoke "sb_dpbed_manbehind_poke_base_layer"
        attribute bpoke "sb_dpbed_manbehind_poke_shad_layer"

        attribute banal "sb_dpbed_manbehind_anal_base_layer"
        attribute banal "sb_dpbed_manbehind_anal_shad_layer"

    always "sb_dpbed_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
