image sb_onbed_bg_layer:
    "sb_onbed_bg_" + loc_cur.loc_type

image sb_onbed_pc_phair_layer:
    "sb_onbed_pc_phair"
    hair_colour_transform()


image sb_onbed_pc_body_hair_layer:
    "sb_onbed_pc_body_hair"
    hair_colour_transform()
image sb_onbed_pc_body_base_layer:
    "sb_onbed_pc_body_base"
    skin_base_colour_transform()
image sb_onbed_pc_body_shad_layer:
    "sb_onbed_pc_body_shad"
    skin_shad_colour_transform()


image sb_onbed_pc_legs_relax_base_layer:
    "sb_onbed_pc_legs_relax_base"
    skin_base_colour_transform()
image sb_onbed_pc_legs_relax_shad_layer:
    "sb_onbed_pc_legs_relax_shad"
    skin_shad_colour_transform()

image sb_onbed_pc_legs_up_base_layer:
    "sb_onbed_pc_legs_up_base"
    skin_base_colour_transform()
image sb_onbed_pc_legs_up_shad_layer:
    "sb_onbed_pc_legs_up_shad"
    skin_shad_colour_transform()


image sb_onbed_pc_belly_base_2 = "sb_onbed_pc_belly_base_3"
image sb_onbed_pc_belly_shad_2 = "sb_onbed_pc_belly_shad_3"
image sb_onbed_pc_belly_base_layer:
    get_skin_filename("sb_onbed_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_onbed_pc_belly_shad_layer:
    get_skin_filename("sb_onbed_pc_belly_shad", preg=True)
    skin_shad_colour_transform()



image sb_onbed_pc_mast_base_layer:
    "sb_onbed_pc_mast_base"
    skin_base_colour_transform()
image sb_onbed_pc_mast_shad_layer:
    "sb_onbed_pc_mast_shad"
    skin_shad_colour_transform()


image sb_onbed_pc_breasts_pc_base_layer:
    get_skin_filename("sb_onbed_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_onbed_pc_breasts_pc_shad_layer:
    get_skin_filename("sb_onbed_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_onbed_pc_breasts_nips_layer:
    get_skin_filename("sb_onbed_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_onbed_pc_breasts_nipring_layer:
    get_skin_filename("sb_onbed_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_onbed_pc_breasts_tattoo_layer:
    get_skin_filename("sb_onbed_pc_breasts_tattoo", breasts=True)


image sb_onbed_pc_writing_chest_layer:
    "sb_onbed_pc_writing_chest"
    writing_transform("chest")
image sb_onbed_pc_writing_belly_layer:
    "sb_onbed_pc_writing_belly"
    writing_transform("belly")
image sb_onbed_pc_writing_pubic_layer:
    "sb_onbed_pc_writing_pubic"
    writing_transform("pubic")


image sb_onbed_man_poke_base_layer:
    "sb_onbed_man_poke_base"
    npc_skin_base_colour_transform()
image sb_onbed_man_poke_shad_layer:
    "sb_onbed_man_poke_shad"
    npc_skin_shad_colour_transform()

image sb_onbed_man_cum_base_layer:
    "sb_onbed_man_cum_base"
    npc_skin_base_colour_transform()
image sb_onbed_man_cum_shad_layer:
    "sb_onbed_man_cum_shad"
    npc_skin_shad_colour_transform()

image sb_onbed_man_sex_base_layer:
    "sb_onbed_man_sex_base"
    npc_skin_base_colour_transform()
image sb_onbed_man_sex_shad_layer:
    "sb_onbed_man_sex_shad"
    npc_skin_shad_colour_transform()

image sb_onbed = LayeredImageProxy("sb_onbed_layered", Transform(xalign = (0.8)))

layeredimage sb_onbed_layered:
    always "sb_onbed_bg_layer"

    always "sb_onbed_pc_body_base_layer"
    always "sb_onbed_pc_body_shad_layer"
    always "sb_onbed_pc_body_hair_layer"

    if writing.belly:
        "sb_onbed_pc_writing_belly_layer"

    group legs:
        attribute noman "sb_onbed_pc_legs_relax_base_layer"
        attribute noman "sb_onbed_pc_legs_relax_shad_layer"

        attribute relax default "sb_onbed_pc_legs_relax_base_layer"
        attribute relax default "sb_onbed_pc_legs_relax_shad_layer"

        attribute mast "sb_onbed_pc_legs_relax_base_layer"
        attribute mast "sb_onbed_pc_legs_relax_shad_layer"

        attribute poke "sb_onbed_pc_legs_up_base_layer"
        attribute poke "sb_onbed_pc_legs_up_shad_layer"

        attribute cum "sb_onbed_pc_legs_up_base_layer"
        attribute cum "sb_onbed_pc_legs_up_shad_layer"

        attribute sex "sb_onbed_pc_legs_up_base_layer"
        attribute sex "sb_onbed_pc_legs_up_shad_layer"

    if writing.pubic:
        "sb_onbed_pc_writing_pubic_layer"
    if player.phair:
        "sb_onbed_pc_phair_layer"

    group legs:
        attribute noman null

        attribute mast "sb_onbed_pc_mast_base_layer"
        attribute mast "sb_onbed_pc_mast_shad_layer"

        attribute poke "sb_onbed_man_poke_base_layer"
        attribute poke "sb_onbed_man_poke_shad_layer"

        attribute cum "sb_onbed_man_cum_base_layer"
        attribute cum "sb_onbed_man_cum_shad_layer"

        attribute sex "sb_onbed_man_sex_base_layer"
        attribute sex "sb_onbed_man_sex_shad_layer"

    if player.pregnancy:
        "sb_onbed_pc_belly_base_layer"
    if player.pregnancy:
        "sb_onbed_pc_belly_shad_layer"

    always "sb_onbed_pc_breasts_pc_base_layer"
    always "sb_onbed_pc_breasts_pc_shad_layer"
    always "sb_onbed_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_onbed_pc_breasts_nipring_layer"
    if tattoo.chest:
        "sb_onbed_pc_breasts_tattoo_layer"
    if writing.chest:
        "sb_onbed_pc_writing_chest_layer"

    always "sb_onbed_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
