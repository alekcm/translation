

image gh_blow_close_man_base_layer:
    "gh_blow_close_man_base"
    npc_skin_base_colour_transform()
image gh_blow_close_man_shad_layer:
    "gh_blow_close_man_shad"
    npc_skin_shad_colour_transform()



image gh_blow_close_pc_suck_head_base_layer:
    "gh_blow_close_pc_suck_head_base"
    skin_base_colour_transform()
image gh_blow_close_pc_suck_head_shad_layer:
    "gh_blow_close_pc_suck_head_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_suck_head_freckles_layer:
    "gh_blow_close_pc_suck_head_freckles"
    skin_shad_colour_transform()
image gh_blow_close_pc_suck_head_lipstick_layer:
    "gh_blow_close_pc_suck_head_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image gh_blow_close_pc_suck_hair_back_bun_2 = "gh_blow_close_pc_suck_hair_back_pony"
image gh_blow_close_pc_suck_hair_back_bun_3 = "gh_blow_close_pc_suck_hair_back_pony"
image gh_blow_close_pc_suck_hair_back_bun_4 = "gh_blow_close_pc_suck_hair_back_pony"

image gh_blow_close_pc_suck_hair_back_pony_2 = "gh_blow_close_pc_suck_hair_back_pony"
image gh_blow_close_pc_suck_hair_back_pony_3 = "gh_blow_close_pc_suck_hair_back_pony"
image gh_blow_close_pc_suck_hair_back_pony_4 = "gh_blow_close_pc_suck_hair_back_pony"

image gh_blow_close_pc_suck_hair_back_layer:
    get_hair_back_cg_filename("gh_blow_close_pc_suck_hair_back")
    hair_colour_transform()

image gh_blow_close_pc_suck_hair_front_layer:
    get_hair_front_cg_filename("gh_blow_close_pc_suck_hair_front")
    hair_colour_transform()



image gh_blow_close_pc_lick_face_base_layer:
    "gh_blow_close_pc_lick_face_base"
    skin_base_colour_transform()
image gh_blow_close_pc_lick_face_shad_layer:
    "gh_blow_close_pc_lick_face_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_lick_face_freckles_layer:
    "gh_blow_close_pc_lick_face_freckles"
    skin_shad_colour_transform()
image gh_blow_close_pc_lick_face_lipstick_layer:
    "gh_blow_close_pc_lick_face_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image gh_blow_close_pc_lick_face_eyeshad_layer:
    "gh_blow_close_pc_lick_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image gh_blow_close_pc_lick_eye_iris_layer:
    "gh_blow_close_pc_lick_eye_iris"
    eye_colour_transform()
image gh_blow_close_pc_lick_eye_eyeliner_layer:
    "gh_blow_close_pc_lick_eye_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image gh_blow_close_pc_lick_brow_layer:
    "gh_blow_close_pc_lick_brow"
    hair_colour_transform()

image gh_blow_close_pc_lick_writing_chest_layer:
    "gh_blow_close_pc_lick_writing_chest"
    writing_transform("chest")
image gh_blow_close_pc_lick_writing_forehead_layer:
    "gh_blow_close_pc_lick_writing_forehead"
    writing_transform("forehead")

image gh_blow_close_pc_lick_hair_back_bun_2 = "gh_blow_close_pc_lick_hair_back_bun"
image gh_blow_close_pc_lick_hair_back_bun_3 = "gh_blow_close_pc_lick_hair_back_bun"
image gh_blow_close_pc_lick_hair_back_bun_4 = "gh_blow_close_pc_lick_hair_back_bun"

image gh_blow_close_pc_lick_hair_back_layer:
    get_hair_back_cg_filename("gh_blow_close_pc_lick_hair_back")
    hair_colour_transform()

image gh_blow_close_pc_lick_hair_front_layer:
    get_hair_front_cg_filename("gh_blow_close_pc_lick_hair_front")
    hair_colour_transform()



image gh_blow_close_pc_cum_head_base_layer:
    "gh_blow_close_pc_cum_head_base"
    skin_base_colour_transform()
image gh_blow_close_pc_cum_head_shad_layer:
    "gh_blow_close_pc_cum_head_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_cum_head_freckles_layer:
    "gh_blow_close_pc_cum_head_freckles"
    skin_shad_colour_transform()




image gh_blow_close_pc_cum_eye_iris_look_layer:
    "gh_blow_close_pc_cum_eye_iris_look"
    eye_colour_transform()
image gh_blow_close_pc_cum_eye_eyeliner_look_layer:
    "gh_blow_close_pc_cum_eye_eyeliner_look_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image gh_blow_close_pc_cum_eye_eyeliner_closed_layer:
    "gh_blow_close_pc_cum_eye_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image gh_blow_close_pc_cum_brow_layer:
    "gh_blow_close_pc_cum_brow"
    hair_colour_transform()

image gh_blow_close_pc_cum_hair_back_layer:
    "gh_blow_close_pc_cum_hair_back"
    hair_colour_transform()

image gh_blow_close_pc_cum_hair_front_layer:
    get_hair_front_cg_filename("gh_blow_close_pc_cum_hair_front")
    hair_colour_transform()



image gh_blow_close_pc_asspoke_body_base_layer:
    "gh_blow_close_pc_asspoke_body_base"
    skin_base_colour_transform()
image gh_blow_close_pc_asspoke_body_shad_layer:
    "gh_blow_close_pc_asspoke_body_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_asspoke_body_pubshad_layer:
    "gh_blow_close_pc_asspoke_body_pubshad"
    skin_shad_colour_transform()

image gh_blow_close_pc_asspoke_spank_layer:
    "gh_blow_close_pc_asspoke_spank"
    opacity_transform(bruise.ass)

image gh_blow_close_pc_asspoke_nails_layer:
    "gh_blow_close_pc_asspoke_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image gh_blow_close_pc_asspoke_writing_ass_layer:
    "gh_blow_close_pc_asspoke_writing_ass"
    writing_transform("ass")
image gh_blow_close_pc_asspoke_writing_anus_layer:
    "gh_blow_close_pc_asspoke_writing_anus"
    writing_transform("anus")



image gh_blow_close_pc_asssex_body_base_layer:
    "gh_blow_close_pc_asssex_body_base"
    skin_base_colour_transform()
image gh_blow_close_pc_asssex_body_shad_layer:
    "gh_blow_close_pc_asssex_body_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_asssex_body_pubshad_layer:
    "gh_blow_close_pc_asssex_body_pubshad"
    skin_shad_colour_transform()

image gh_blow_close_pc_asssex_spank_layer:
    "gh_blow_close_pc_asssex_spank"
    opacity_transform(bruise.ass)

image gh_blow_close_pc_asssex_nails_layer:
    "gh_blow_close_pc_asssex_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image gh_blow_close_pc_asssex_writing_ass_layer:
    "gh_blow_close_pc_asssex_writing_ass"
    writing_transform("ass")
image gh_blow_close_pc_asssex_writing_anus_layer:
    "gh_blow_close_pc_asssex_writing_anus"
    writing_transform("anus")



image gh_blow_close_pc_vagsex_body_base_layer:
    "gh_blow_close_pc_vagsex_body_base"
    skin_base_colour_transform()
image gh_blow_close_pc_vagsex_body_shad_layer:
    "gh_blow_close_pc_vagsex_body_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_vagsex_body_pubshad_layer:
    "gh_blow_close_pc_vagsex_body_pubshad"
    skin_shad_colour_transform()
image gh_blow_close_pc_vagsex_body_vag_layer:
    "gh_blow_close_pc_vagsex_body_vag"
    vagina_colour_transform()

image gh_blow_close_pc_vagsex_spank_layer:
    "gh_blow_close_pc_vagsex_spank"
    opacity_transform(bruise.ass)

image gh_blow_close_pc_vagsex_nails_layer:
    "gh_blow_close_pc_vagsex_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image gh_blow_close_pc_vagsex_writing_ass_layer:
    "gh_blow_close_pc_vagsex_writing_ass"
    writing_transform("ass")
image gh_blow_close_pc_vagsex_writing_anus_layer:
    "gh_blow_close_pc_vagsex_writing_anus"
    writing_transform("anus")



image gh_blow_close_pc_vagpoke_body_base_layer:
    "gh_blow_close_pc_vagpoke_body_base"
    skin_base_colour_transform()
image gh_blow_close_pc_vagpoke_body_shad_layer:
    "gh_blow_close_pc_vagpoke_body_shad"
    skin_shad_colour_transform()
image gh_blow_close_pc_vagpoke_body_pubshad_layer:
    "gh_blow_close_pc_vagpoke_body_pubshad"
    skin_shad_colour_transform()
image gh_blow_close_pc_vagpoke_body_vag_layer:
    "gh_blow_close_pc_vagpoke_body_vag"
    vagina_colour_transform()

image gh_blow_close_pc_vagpoke_spank_layer:
    "gh_blow_close_pc_vagpoke_spank"
    opacity_transform(bruise.ass)

image gh_blow_close_pc_vagpoke_nails_layer:
    "gh_blow_close_pc_vagpoke_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image gh_blow_close_pc_vagpoke_writing_ass_layer:
    "gh_blow_close_pc_vagpoke_writing_ass"
    writing_transform("ass")
image gh_blow_close_pc_vagpoke_writing_anus_layer:
    "gh_blow_close_pc_vagpoke_writing_anus"
    writing_transform("anus")

image gh_blow_close = LayeredImageProxy("gh_blow_close_layer", Transform(align=(0.8, 0.0)))

layeredimage gh_blow_close_layer:  

    always "gh_blow_close_bg"

    group man:
        attribute man_hole default:
            "gh_blow_close_man_base_layer"
        attribute man_hole default:
            "gh_blow_close_man_shad_layer"
        attribute man_hole default:
            "gh_blow_close_man_col"

        attribute no_man_hole:
            null

    group pc:
        attribute suck:
            "gh_blow_close_suck_layer"
        attribute lick:
            "gh_blow_close_lick_layer"
        attribute cum:
            "gh_blow_close_cum_layer"

        attribute vagsex:
            "gh_blow_close_vagsex_layer"
        attribute vagpoke:
            "gh_blow_close_vagpoke_layer"
        attribute asssex:
            "gh_blow_close_asssex_layer"
        attribute asspoke:
            "gh_blow_close_asspoke_layer"

        attribute no_pc default:
            null

    always "gh_blow_close_frame"

layeredimage gh_blow_close_suck_layer:
    always "gh_blow_close_pc_suck_head_base_layer"
    always "gh_blow_close_pc_suck_head_shad_layer"
    if skin_effect.face:
        "gh_blow_close_pc_suck_head_freckles_layer"
    always "gh_blow_close_pc_suck_head_lipstick_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_suck_pub"
    always "gh_blow_close_pc_suck_drool"
    if player.cum_locations["cum_mouth"]:
        "gh_blow_close_pc_suck_cum"
    always "gh_blow_close_pc_suck_hair_back_layer"
    always "gh_blow_close_pc_suck_hair_front_layer"

layeredimage gh_blow_close_lick_layer:
    always "gh_blow_close_pc_lick_face_base_layer"
    always "gh_blow_close_pc_lick_face_shad_layer"
    if skin_effect.face:
        "gh_blow_close_pc_lick_face_freckles_layer"
    always "gh_blow_close_pc_lick_face_lipstick_layer"
    always "gh_blow_close_pc_lick_face_eyeshad_layer"
    always "gh_blow_close_pc_lick_face_mouth"
    always "gh_blow_close_pc_lick_eye_iris_layer"
    always "gh_blow_close_pc_lick_eye_eye"
    always "gh_blow_close_pc_lick_eye_eyeliner_layer"
    always "gh_blow_close_pc_lick_brow_layer"
    if writing.forehead:
        "gh_blow_close_pc_lick_writing_forehead_layer"
    if writing.chest:
        "gh_blow_close_pc_lick_writing_chest_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_lick_pub"
    always "gh_blow_close_pc_lick_hair_back_layer"
    always "gh_blow_close_pc_lick_hair_front_layer"

layeredimage gh_blow_close_cum_layer:
    always "gh_blow_close_pc_cum_head_base_layer"
    always "gh_blow_close_pc_cum_head_shad_layer"
    if skin_effect.face:
        "gh_blow_close_pc_cum_head_freckles_layer"

    always "gh_blow_close_pc_cum_head_mouth"

    if player.cum_locations["cum_mouth"]:
        "gh_blow_close_pc_cum_eye_eyeliner_closed_layer"
    if not player.cum_locations["cum_mouth"]:
        "gh_blow_close_pc_cum_eye_iris_look_layer"
    if not player.cum_locations["cum_mouth"]:
        "gh_blow_close_pc_cum_eye_eye_look"
    if not player.cum_locations["cum_mouth"]:
        "gh_blow_close_pc_cum_eye_eyeliner_look_layer"

    always "gh_blow_close_pc_cum_brow_layer"

    if player.cum_locations["cum_mouth"] or player.cum_locations["cum_face"]:
        "gh_blow_close_pc_cum_cum"

    always "gh_blow_close_pc_cum_hair_back_layer"
    always "gh_blow_close_pc_cum_hair_front_layer"

layeredimage gh_blow_close_asspoke_layer:
    always "gh_blow_close_pc_asspoke_body_base_layer"
    always "gh_blow_close_pc_asspoke_body_shad_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_asspoke_body_pubshad_layer"
    always "gh_blow_close_pc_asspoke_spank_layer"
    always "gh_blow_close_pc_asspoke_nails_layer"
    if tattoo.ass:
        "gh_blow_close_pc_asspoke_tattoo"
    if writing.ass:
        "gh_blow_close_pc_asspoke_writing_ass_layer"
    if writing.anus:
        "gh_blow_close_pc_asspoke_writing_anus_layer"
    if player.cum_locations["cum_assin"]:
        "gh_blow_close_pc_asspoke_cum"
    if c.outfit == 6:
        "gh_blow_close_pc_asspoke_pubdress"

layeredimage gh_blow_close_asssex_layer:
    always "gh_blow_close_pc_asssex_body_base_layer"
    always "gh_blow_close_pc_asssex_body_shad_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_asssex_body_pubshad_layer"
    always "gh_blow_close_pc_asssex_spank_layer"
    always "gh_blow_close_pc_asssex_nails_layer"
    if writing.ass:
        "gh_blow_close_pc_asssex_writing_ass_layer"
    if writing.anus:
        "gh_blow_close_pc_asssex_writing_anus_layer"
    if player.cum_locations["cum_assin"]:
        "gh_blow_close_pc_asssex_cum"
    if c.outfit == 6:
        "gh_blow_close_pc_asssex_pubdress"

layeredimage gh_blow_close_vagsex_layer:
    always "gh_blow_close_pc_vagsex_body_base_layer"
    always "gh_blow_close_pc_vagsex_body_shad_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_vagsex_body_pubshad_layer"
    always "gh_blow_close_pc_vagsex_body_vag_layer"
    always "gh_blow_close_pc_vagsex_spank_layer"
    always "gh_blow_close_pc_vagsex_nails_layer"
    if writing.ass:
        "gh_blow_close_pc_vagsex_writing_ass_layer"
    if writing.anus:
        "gh_blow_close_pc_vagsex_writing_anus_layer"
    if player.cum_locations["cum_vagin"]:
        "gh_blow_close_pc_vagsex_cum"
    if c.outfit == 6:
        "gh_blow_close_pc_vagsex_pubdress"

layeredimage gh_blow_close_vagpoke_layer:
    always "gh_blow_close_pc_vagpoke_body_base_layer"
    always "gh_blow_close_pc_vagpoke_body_shad_layer"
    if c.outfit == 6:
        "gh_blow_close_pc_vagpoke_body_pubshad_layer"
    always "gh_blow_close_pc_vagpoke_body_vag_layer"
    always "gh_blow_close_pc_vagpoke_spank_layer"
    always "gh_blow_close_pc_vagpoke_nails_layer"
    if tattoo.ass:
        "gh_blow_close_pc_vagpoke_tattoo"
    if writing.ass:
        "gh_blow_close_pc_vagpoke_writing_ass_layer"
    if writing.anus:
        "gh_blow_close_pc_vagpoke_writing_anus_layer"
    if player.cum_locations["cum_vagin"]:
        "gh_blow_close_pc_vagpoke_cum"
    if c.outfit == 6:
        "gh_blow_close_pc_vagpoke_pubdress"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
