

image gh_blow_behind_man_hole_base_layer:
    "gh_blow_behind_man_hole_base"
    npc_skin_base_colour_transform()
image gh_blow_behind_man_hole_shad_layer:
    "gh_blow_behind_man_hole_shad"
    npc_skin_shad_colour_transform()



image gh_blow_behind_pc_breasts_base_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_pc_breasts_shad_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image gh_blow_behind_pc_breasts_nips_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image gh_blow_behind_pc_breasts_nipring_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image gh_blow_behind_pc_body_base_layer:
    "gh_blow_behind_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_pc_body_shad_layer:
    "gh_blow_behind_pc_body_shad"
    skin_shad_colour_transform()
image gh_blow_behind_pc_body_vag_layer:
    "gh_blow_behind_pc_body_vag"
    vagina_colour_transform()

image gh_blow_behind_pc_writing_ass_layer:
    "gh_blow_behind_pc_writing_ass"
    writing_transform("ass")
image gh_blow_behind_pc_writing_anus_layer:
    "gh_blow_behind_pc_writing_anus"
    writing_transform("anus")

image gh_blow_behind_pc_spank_layer:
    "gh_blow_behind_pc_spank"
    opacity_transform(bruise.ass)

image gh_blow_behind_pc_phair_layer:
    "gh_blow_behind_pc_phair"
    phair_colour_transform()

image gh_blow_behind_pc_hair_back_bun_2 = "gh_blow_behind_pc_hair_back_bun"
image gh_blow_behind_pc_hair_back_bun_3 = "gh_blow_behind_pc_hair_back_bun"
image gh_blow_behind_pc_hair_back_bun_4 = "gh_blow_behind_pc_hair_back_bun"
image gh_blow_behind_pc_hair_back_pony_4 = "gh_blow_behind_pc_hair_back_pony_3"

image gh_blow_behind_pc_hair_back_layer:
    get_hair_back_cg_filename("gh_blow_behind_pc_hair_back")
    hair_colour_transform()



image gh_blow_behind_pc_breasts_pub_col_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_pub_col", breasts=True)
image gh_blow_behind_pc_breasts_pub_base_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_pub_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_pc_breasts_pub_shad_layer:
    get_skin_filename("gh_blow_behind_pc_breasts_pub_shad", breasts=True)
    skin_shad_colour_transform()



image gh_blow_behind_man_sex_dani_poke_base_layer:
    "gh_blow_behind_man_sex_dani_poke_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_dani_poke_shad_layer:
    "gh_blow_behind_man_sex_dani_poke_shad"
    npc2_skin_shad_colour_transform()

image gh_blow_behind_man_sex_dani_sex_base_layer:
    "gh_blow_behind_man_sex_dani_sex_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_dani_sex_shad_layer:
    "gh_blow_behind_man_sex_dani_sex_shad"
    npc2_skin_shad_colour_transform()

image gh_blow_behind_man_sex_pc_asspoke_base_layer:
    "gh_blow_behind_man_sex_pc_asspoke_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_pc_asspoke_shad_layer:
    "gh_blow_behind_man_sex_pc_asspoke_shad"
    npc2_skin_shad_colour_transform()

image gh_blow_behind_man_sex_pc_asssex_base_layer:
    "gh_blow_behind_man_sex_pc_asssex_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_pc_asssex_shad_layer:
    "gh_blow_behind_man_sex_pc_asssex_shad"
    npc2_skin_shad_colour_transform()

image gh_blow_behind_man_sex_pc_vagpoke_base_layer:
    "gh_blow_behind_man_sex_pc_vagpoke_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_pc_vagpoke_shad_layer:
    "gh_blow_behind_man_sex_pc_vagpoke_shad"
    npc2_skin_shad_colour_transform()

image gh_blow_behind_man_sex_pc_vagsex_base_layer:
    "gh_blow_behind_man_sex_pc_vagsex_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_sex_pc_vagsex_shad_layer:
    "gh_blow_behind_man_sex_pc_vagsex_shad"
    npc2_skin_shad_colour_transform()
image gh_blow_behind_man_sex_pc_vagsex_vag_layer:
    "gh_blow_behind_man_sex_pc_vagsex_vag"
    vagina_colour_transform()



image gh_blow_behind_idle_pc_belly_base_layer:
    "gh_blow_behind_idle_pc_belly_base"
    skin_base_colour_transform()
image gh_blow_behind_idle_pc_belly_shad_layer:
    "gh_blow_behind_idle_pc_belly_shad"
    skin_shad_colour_transform()

image gh_blow_behind_idle_pc_body_base_layer:
    "gh_blow_behind_idle_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_idle_pc_body_shad_layer:
    "gh_blow_behind_idle_pc_body_shad"
    skin_shad_colour_transform()

image gh_blow_behind_idle_pc_nails_layer:
    "gh_blow_behind_idle_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))
image gh_blow_behind_idle_pc_spank_layer:
    "gh_blow_behind_idle_pc_spank"
    opacity_transform(bruise.ass)

image gh_blow_behind_idle_pc_writing_ass_layer:
    "gh_blow_behind_idle_pc_writing_ass"
    writing_transform("ass")
image gh_blow_behind_idle_pc_writing_anus_layer:
    "gh_blow_behind_idle_pc_writing_anus"
    writing_transform("anus")



image gh_blow_behind_mast_pc_belly_base_layer:
    "gh_blow_behind_mast_pc_belly_base"
    skin_base_colour_transform()
image gh_blow_behind_mast_pc_belly_shad_layer:
    "gh_blow_behind_mast_pc_belly_shad"
    skin_shad_colour_transform()

image gh_blow_behind_mast_pc_body_base_layer:
    "gh_blow_behind_mast_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_mast_pc_body_shad_layer:
    "gh_blow_behind_mast_pc_body_shad"
    skin_shad_colour_transform()

image gh_blow_behind_mast_pc_phair_layer:
    "gh_blow_behind_mast_pc_phair"
    hair_colour_transform()

image gh_blow_behind_mast_pc_nails_layer:
    "gh_blow_behind_mast_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image gh_blow_behind_mast_pc_writing_belly_layer:
    "gh_blow_behind_mast_pc_writing_belly"
    writing_transform("belly")
image gh_blow_behind_mast_pc_writing_pubic_layer:
    "gh_blow_behind_mast_pc_writing_pubic"
    writing_transform("pubic")



image gh_blow_behind_sex_stand_pc_belly_base_layer:
    "gh_blow_behind_sex_stand_pc_belly_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_stand_pc_belly_shad_layer:
    "gh_blow_behind_sex_stand_pc_belly_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_stand_pc_body_base_layer:
    "gh_blow_behind_sex_stand_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_stand_pc_body_shad_layer:
    "gh_blow_behind_sex_stand_pc_body_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_stand_pc_phair_layer:
    "gh_blow_behind_sex_stand_pc_phair"
    hair_colour_transform()

image gh_blow_behind_sex_stand_pc_writing_belly_layer:
    "gh_blow_behind_sex_stand_pc_writing_belly"
    writing_transform("belly")
image gh_blow_behind_sex_stand_pc_writing_belly_2_layer:
    "gh_blow_behind_sex_stand_pc_writing_belly_2"
    writing_transform("belly")
image gh_blow_behind_sex_stand_pc_writing_belly_3_layer:
    "gh_blow_behind_sex_stand_pc_writing_belly_3"
    writing_transform("belly")
image gh_blow_behind_sex_stand_pc_writing_pubic_layer:
    "gh_blow_behind_sex_stand_pc_writing_pubic"
    writing_transform("pubic")
image gh_blow_behind_sex_stand_pc_writing_lleg_layer:
    "gh_blow_behind_sex_stand_pc_writing_lleg"
    writing_transform("lleg")



image gh_blow_behind_man_mast_base_layer:
    "gh_blow_behind_man_mast_base"
    npc2_skin_base_colour_transform()
image gh_blow_behind_man_mast_shad_layer:
    "gh_blow_behind_man_mast_shad"
    npc2_skin_shad_colour_transform()



image gh_blow_behind_sex_down_pc_belly_base_layer:
    "gh_blow_behind_sex_down_pc_belly_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_down_pc_belly_shad_layer:
    "gh_blow_behind_sex_down_pc_belly_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_down_pc_body_base_layer:
    "gh_blow_behind_sex_down_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_down_pc_body_shad_layer:
    "gh_blow_behind_sex_down_pc_body_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_down_pc_breasts_base_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_sex_down_pc_breasts_shad_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image gh_blow_behind_sex_down_pc_breasts_nips_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image gh_blow_behind_sex_down_pc_breasts_tattoo_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_tattoo", breasts=True)
image gh_blow_behind_sex_down_pc_breasts_nipring_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image gh_blow_behind_sex_down_pc_breasts_pub_base_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_pub_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_sex_down_pc_breasts_pub_shad_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_pub_shad", breasts=True)
    skin_shad_colour_transform()
image gh_blow_behind_sex_down_pc_breasts_pub_col_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_pub_col", breasts=True)
image gh_blow_behind_sex_down_pc_breasts_pub_tattoo_layer:
    get_skin_filename("gh_blow_behind_sex_down_pc_breasts_pub_tattoo", breasts=True)

image gh_blow_behind_sex_down_pc_hair_back_3 = "gh_blow_behind_sex_down_pc_hair_back_2"
image gh_blow_behind_sex_down_pc_hair_back_4 = "gh_blow_behind_sex_down_pc_hair_back_2"
image gh_blow_behind_sex_down_pc_hair_back_bun_4 = "gh_blow_behind_sex_down_pc_hair_back_bun_3"
image gh_blow_behind_sex_down_pc_hair_back_pony_4 = "gh_blow_behind_sex_down_pc_hair_back_pony_3"
image gh_blow_behind_sex_down_pc_hair_layer:
    get_hair_back_cg_filename("gh_blow_behind_sex_down_pc_hair_back")
    hair_colour_transform()



image gh_blow_behind_sex_up_pc_belly_base_layer:
    "gh_blow_behind_sex_up_pc_belly_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_up_pc_belly_shad_layer:
    "gh_blow_behind_sex_up_pc_belly_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_up_pc_body_base_layer:
    "gh_blow_behind_sex_up_pc_body_base"
    skin_base_colour_transform()
image gh_blow_behind_sex_up_pc_body_shad_layer:
    "gh_blow_behind_sex_up_pc_body_shad"
    skin_shad_colour_transform()

image gh_blow_behind_sex_up_pc_phair_layer:
    "gh_blow_behind_sex_up_pc_phair"
    hair_colour_transform()

image gh_blow_behind_sex_up_pc_writing_belly_layer:
    "gh_blow_behind_sex_up_pc_writing_belly"
    writing_transform("belly")
image gh_blow_behind_sex_up_pc_writing_pubic_layer:
    "gh_blow_behind_sex_up_pc_writing_pubic"
    writing_transform("pubic")
image gh_blow_behind_sex_up_pc_writing_lleg_layer:
    "gh_blow_behind_sex_up_pc_writing_lleg"
    writing_transform("lleg")

image gh_blow_behind_sex_up_pc_breasts_base_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_sex_up_pc_breasts_shad_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image gh_blow_behind_sex_up_pc_breasts_nips_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image gh_blow_behind_sex_up_pc_breasts_tattoo_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_tattoo", breasts=True)
image gh_blow_behind_sex_up_pc_breasts_nipring_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image gh_blow_behind_sex_up_pc_breasts_pub_base_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_pub_base", breasts=True)
    skin_base_colour_transform()
image gh_blow_behind_sex_up_pc_breasts_pub_shad_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_pub_shad", breasts=True)
    skin_shad_colour_transform()
image gh_blow_behind_sex_up_pc_breasts_pub_col_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_pub_col", breasts=True)
image gh_blow_behind_sex_up_pc_breasts_pub_tattoo_layer:
    get_skin_filename("gh_blow_behind_sex_up_pc_breasts_pub_tattoo", breasts=True)

image gh_blow_behind = LayeredImageProxy("gh_blow_behind_layer", Transform(align=(0.8, 0.0)))

layeredimage gh_blow_behind_layer:

    always "gh_blow_behind_bg"

    group hole:
        attribute man_hole default "gh_blow_behind_man_hole_base_layer"
        attribute man_hole default "gh_blow_behind_man_hole_shad_layer"

        attribute no_man_hole null

    group pc_suck:
        attribute suck "gh_blow_behind_pc_layer"
        attribute mast "gh_blow_behind_pc_mast_layered"
        attribute sex_stand "gh_blow_behind_pc_sex_stand_layered"
        attribute sex_up "gh_blow_behind_pc_sex_up_layered"
        attribute no_pc default null

    group danig:

        attribute dani_hump "gh_blow_behind_dani"
        attribute dani_stand "gh_blow_behind_dani_stand"
        attribute dani_lick "gh_blow_behind_dani_lick"
        attribute dani_suck "gh_blow_behind_dani_suck"
        attribute no_dani default null

    group dani_cumg:
        attribute dani_cum "gh_blow_behind_dani_cum"
        attribute no_dani_cum default null


    group dani_peeg:
        attribute dani_pee "gh_blow_behind_dani_pee"
        attribute no_dani_pee default null

    group man_behind:
        attribute dani_poke "gh_blow_behind_man_sex_danipoke"
        attribute dani_sex "gh_blow_behind_man_sex_danisex"

        attribute vagpoke "gh_blow_behind_man_sex_pc_vagpoke"
        attribute vagsex "gh_blow_behind_man_sex_pc_vagsex"
        attribute asspoke "gh_blow_behind_man_sex_pc_asspoke"
        attribute asssex "gh_blow_behind_man_sex_pc_asssex"

        attribute man_mast "gh_blow_behind_man_mast_layered"

        attribute no_man default null

    group trixieg:
        attribute trixie "gh_blow_behind_trixie"

        attribute trixie_rub "gh_blow_behind_trixie"
        attribute trixie_rub if_any "dani_poke" "gh_blow_behind_trixie_hand_danipoke"
        attribute trixie_rub if_any "dani_sex" "gh_blow_behind_trixie_hand_danisex"
        attribute trixie_rub if_any "vagpoke" "gh_blow_behind_trixie_hand_pcvagpoke"
        attribute trixie_rub if_any "vagsex" "gh_blow_behind_trixie_hand_pcvagsex"
        attribute trixie_rub if_any "asspoke" "gh_blow_behind_trixie_hand_pcasspoke"
        attribute trixie_rub if_any "asssex" "gh_blow_behind_trixie_hand_pcasssex"

        attribute trixie_dani "gh_blow_behind_trixie"
        attribute trixie_dani "gh_blow_behind_trixie_hand_dani"

        attribute trixie_pc "gh_blow_behind_trixie"
        attribute trixie_pc "gh_blow_behind_trixie_hand_pc"

        attribute trixie_both "gh_blow_behind_trixie"
        attribute trixie_both "gh_blow_behind_trixie_hand_dani"
        attribute trixie_both "gh_blow_behind_trixie_hand_pc"

    group pc_suck:
        attribute idle "gh_blow_behind_pc_idle_layered"
        attribute sex_down "gh_blow_behind_pc_sex_down_layered"

    always "gh_blow_behind_frame"

layeredimage gh_blow_behind_pc_breasts_nude_layer:
    always "gh_blow_behind_pc_breasts_base_layer"
    always "gh_blow_behind_pc_breasts_shad_layer"
    always "gh_blow_behind_pc_breasts_nips_layer"
    if acc.nipring:
        "gh_blow_behind_pc_breasts_nipring_layer"

layeredimage gh_blow_behind_pc_breasts_pub_layer:
    always "gh_blow_behind_pc_breasts_pub_base_layer"
    always "gh_blow_behind_pc_breasts_pub_shad_layer"
    always "gh_blow_behind_pc_breasts_pub_col_layer"

layeredimage gh_blow_behind_pc_layer:
    if c.outfit == 6:
        "gh_blow_behind_pc_breasts_pub_layer"
    else:
        "gh_blow_behind_pc_breasts_nude_layer"
    always "gh_blow_behind_pc_body_base_layer"
    always "gh_blow_behind_pc_body_shad_layer"
    always "gh_blow_behind_pc_body_vag_layer"

    if acc.anus:
        "gh_blow_behind_pc_plug"
    if writing.ass:
        "gh_blow_behind_pc_writing_ass_layer"
    if writing.anus:
        "gh_blow_behind_pc_writing_anus_layer"
    always "gh_blow_behind_pc_spank_layer"

    if c.pants == 6:
        "gh_blow_behind_pc_pub_pants"
    if c.outfit == 6:
        "gh_blow_behind_pc_pub_dress" 
    always "gh_blow_behind_pc_hair_back_layer"
    if c.outfit == 6:
        "gh_blow_behind_pc_pub_dress_hair"
    if player.phair and not c.pants:
        "gh_blow_behind_pc_phair_layer"

    if player.cum_locations["cum_vagin"]:
        "gh_blow_behind_pc_cum_vagin"
    if player.cum_locations["cum_assin"]:
        "gh_blow_behind_pc_cum_assin"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "gh_blow_behind_pc_cum_assout"



layeredimage gh_blow_behind_man_sex_danipoke:
    always "gh_blow_behind_man_sex_dani_poke_base_layer"
    always "gh_blow_behind_man_sex_dani_poke_shad_layer"

layeredimage gh_blow_behind_man_sex_danisex:
    always "gh_blow_behind_man_sex_dani_sex_col"
    always "gh_blow_behind_man_sex_dani_sex_base_layer"
    always "gh_blow_behind_man_sex_dani_sex_shad_layer"

layeredimage gh_blow_behind_man_sex_pc_asspoke:
    always "gh_blow_behind_man_sex_pc_asspoke_base_layer"
    always "gh_blow_behind_man_sex_pc_asspoke_shad_layer"
    always "gh_blow_behind_man_sex_pc_asspoke_col"

layeredimage gh_blow_behind_man_sex_pc_asssex:
    always "gh_blow_behind_man_sex_pc_asssex_base_layer"
    always "gh_blow_behind_man_sex_pc_asssex_shad_layer"
    always "gh_blow_behind_man_sex_pc_asssex_col"

layeredimage gh_blow_behind_man_sex_pc_vagpoke:
    always "gh_blow_behind_man_sex_pc_vagpoke_base_layer"
    always "gh_blow_behind_man_sex_pc_vagpoke_shad_layer"
    always "gh_blow_behind_man_sex_pc_vagpoke_col"

layeredimage gh_blow_behind_man_sex_pc_vagsex:
    always "gh_blow_behind_man_sex_pc_vagsex_base_layer"
    always "gh_blow_behind_man_sex_pc_vagsex_shad_layer"
    always "gh_blow_behind_man_sex_pc_vagsex_vag_layer"
    always "gh_blow_behind_man_sex_pc_vagsex_col"

layeredimage gh_blow_behind_man_mast_layered:
    always "gh_blow_behind_man_mast_base_layer"
    always "gh_blow_behind_man_mast_shad_layer"
    always "gh_blow_behind_man_mast_col"



layeredimage gh_blow_behind_pc_sex_test_layered:
    always "gh_blow_behind_pc_sex_test_base_layer"
    always "gh_blow_behind_pc_sex_test_shad_layer"
    always "gh_blow_behind_pc_sex_test_nips_layer"

layeredimage gh_blow_behind_pc_idle_layered:
    if player.pregnancy >= 2:
        "gh_blow_behind_idle_pc_belly_base_layer"
    if player.pregnancy >= 2:
        "gh_blow_behind_idle_pc_belly_shad_layer"
    if player.pregnancy >= 2 and c.outfit == 6:
        "gh_blow_behind_idle_pc_belly_pub"

    always "gh_blow_behind_idle_pc_body_base_layer"
    always "gh_blow_behind_idle_pc_body_shad_layer"
    always "gh_blow_behind_idle_pc_nails_layer"
    always "gh_blow_behind_idle_pc_spank_layer"

    if writing.ass:
        "gh_blow_behind_idle_pc_writing_ass_layer"
    if writing.anus:
        "gh_blow_behind_idle_pc_writing_anus_layer"

    if c.socks == 7:
        "gh_blow_behind_idle_pc_socks"
    if c.pants == 6:
        "gh_blow_behind_idle_pc_pants"
    if c.outfit == 6:
        "gh_blow_behind_idle_pc_pubdress"

layeredimage gh_blow_behind_pc_mast_layered:
    if player.pregnancy >= 2:
        "gh_blow_behind_mast_pc_belly_base_layer"
    if player.pregnancy >= 2:
        "gh_blow_behind_mast_pc_belly_shad_layer"
    if player.pregnancy >= 2 and c.outfit == 6:
        "gh_blow_behind_mast_pc_belly_pub"

    always "gh_blow_behind_mast_pc_body_base_layer"
    always "gh_blow_behind_mast_pc_body_shad_layer"
    if player.phair:
        "gh_blow_behind_mast_pc_phair_layer"
    always "gh_blow_behind_mast_pc_nails_layer"

    if writing.belly:
        "gh_blow_behind_mast_pc_writing_belly_layer"
    if writing.pubic:
        "gh_blow_behind_mast_pc_writing_pubic_layer"

    if c.socks == 7:
        "gh_blow_behind_mast_pc_socks"
    if c.pants == 6:
        "gh_blow_behind_mast_pc_pants"
    if c.outfit == 6:
        "gh_blow_behind_mast_pc_pubdress"

layeredimage gh_blow_behind_pc_sex_stand_layered:
    always "gh_blow_behind_sex_stand_pc_body_base_layer"
    always "gh_blow_behind_sex_stand_pc_body_shad_layer"
    if player.phair:
        "gh_blow_behind_sex_stand_pc_phair_layer"

    if writing.belly:
        "gh_blow_behind_sex_stand_pc_writing_belly_layer"
    if writing.pubic:
        "gh_blow_behind_sex_stand_pc_writing_pubic_layer"
    if writing.lleg:
        "gh_blow_behind_sex_stand_pc_writing_lleg_layer"

    if player.pregnancy >= 2:
        "gh_blow_behind_sex_stand_pc_belly_base_layer"
    if player.pregnancy >= 2:
        "gh_blow_behind_sex_stand_pc_belly_shad_layer"

    if writing.belly and player.pregnancy == 2:
        "gh_blow_behind_sex_stand_pc_writing_belly_2_layer"
    if writing.belly and player.pregnancy == 3:
        "gh_blow_behind_sex_stand_pc_writing_belly_3_layer"

    if c.socks == 7:
        "gh_blow_behind_sex_stand_pc_socks"
    if c.outfit == 6:
        "gh_blow_behind_sex_stand_pc_pubdress"
    if player.pregnancy >= 2 and c.outfit == 6:
        "gh_blow_behind_sex_stand_pc_belly_pub"

layeredimage gh_blow_behind_pc_sex_down_layered:

    always "gh_blow_behind_sex_down_pc_body_base_layer"
    always "gh_blow_behind_sex_down_pc_body_shad_layer"
    if tattoo.ass:
        "gh_blow_behind_sex_down_pc_tattoo_tramp"
    if c.socks == 7:
        "gh_blow_behind_sex_down_pc_socks"
    if player.pregnancy >= 2 and not c.outfit:
        "gh_blow_behind_sex_down_pc_belly_base_layer"
    if player.pregnancy >= 2 and not c.outfit:
        "gh_blow_behind_sex_down_pc_belly_shad_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_down_pc_dress"
    if player.pregnancy >= 2 and c.outfit == 6:
        "gh_blow_behind_sex_down_pc_belly_pub"

    if not c.outfit:
        "gh_blow_behind_sex_down_pc_breasts_base_layer"
    if not c.outfit:
        "gh_blow_behind_sex_down_pc_breasts_shad_layer"
    if not c.outfit:
        "gh_blow_behind_sex_down_pc_breasts_nips_layer"
    if not c.outfit and tattoo.chest:
        "gh_blow_behind_sex_down_pc_breasts_tattoo_layer"
    if not c.outfit and acc.nipring:
        "gh_blow_behind_sex_down_pc_breasts_nipring_layer"

    if c.outfit == 6:
        "gh_blow_behind_sex_down_pc_breasts_pub_base_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_down_pc_breasts_pub_shad_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_down_pc_breasts_pub_col_layer"
    if c.outfit == 6 and tattoo.chest:
        "gh_blow_behind_sex_down_pc_breasts_pub_tattoo_layer"

    always "gh_blow_behind_sex_down_pc_hair_layer"

layeredimage gh_blow_behind_pc_sex_up_layered:
    always "gh_blow_behind_sex_up_pc_body_base_layer"
    always "gh_blow_behind_sex_up_pc_body_shad_layer"
    if player.cum_locations["cum_vagin"]:
        "gh_blow_behind_sex_up_pc_cum"
    if player.phair:
        "gh_blow_behind_sex_up_pc_phair_layer"
    if writing.belly:
        "gh_blow_behind_sex_up_pc_writing_belly_layer"
    if writing.pubic:
        "gh_blow_behind_sex_up_pc_writing_pubic_layer"
    if writing.lleg:
        "gh_blow_behind_sex_up_pc_writing_lleg_layer"

    if c.socks:
        "gh_blow_behind_sex_up_pc_socks"
    if player.pregnancy >= 2:
        "gh_blow_behind_sex_up_pc_belly_base_layer"
    if player.pregnancy >= 2:
        "gh_blow_behind_sex_up_pc_belly_shad_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_up_pc_dress"
    if player.pregnancy >= 2 and c.outfit == 6:
        "gh_blow_behind_sex_up_pc_belly_dress"

    if not c.outfit:
        "gh_blow_behind_sex_up_pc_breasts_base_layer"
    if not c.outfit:
        "gh_blow_behind_sex_up_pc_breasts_shad_layer"
    if not c.outfit:
        "gh_blow_behind_sex_up_pc_breasts_nips_layer"
    if not c.outfit and tattoo.chest:
        "gh_blow_behind_sex_up_pc_breasts_tattoo_layer"
    if not c.outfit and acc.nipring:
        "gh_blow_behind_sex_up_pc_breasts_nipring_layer"

    if c.outfit == 6:
        "gh_blow_behind_sex_up_pc_breasts_pub_base_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_up_pc_breasts_pub_shad_layer"
    if c.outfit == 6:
        "gh_blow_behind_sex_up_pc_breasts_pub_col_layer"
    if c.outfit == 6 and tattoo.chest:
        "gh_blow_behind_sex_up_pc_breasts_pub_tattoo_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
