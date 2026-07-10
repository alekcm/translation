
image sb_dpstand_bg_beach = "sb_dpstand_bg_grass"
image sb_dpstand_bg_layer:
    "sb_dpstand_bg_" + loc_cur.loc_type



image sb_dpstand_pc_body_base_layer:
    get_skin_filename("sb_dpstand_pc_body_base")
    skin_base_colour_transform()
image sb_dpstand_pc_body_shad_layer:
    get_skin_filename("sb_dpstand_pc_body_shad")
    skin_shad_colour_transform()
image sb_dpstand_pc_body_vag_layer:
    get_skin_filename("sb_dpstand_pc_body_vag")
    vagina_colour_transform()
image sb_dpstand_pc_body_nails_layer:
    "sb_dpstand_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))



image sb_dpstand_pc_det_blush_layer:
    "sb_dpstand_pc_det_blush"
    blush_opacity_transform()
image sb_dpstand_pc_det_spank_layer:
    "sb_dpstand_pc_det_spank"
    opacity_transform(bruise.ass)
image sb_dpstand_pc_det_freckles_layer:
    "sb_dpstand_pc_det_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_dpstand_pc_det_phair_layer:
    "sb_dpstand_pc_det_phair"
    phair_colour_transform()
image sb_dpstand_pc_det_eyeshadow_layer:
    "sb_dpstand_pc_det_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))



image sb_dpstand_pc_face_happy_lipstick_layer:
    "sb_dpstand_pc_face_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_dpstand_pc_face_happy_brow_layer:
    "sb_dpstand_pc_face_happy_brow"
    hair_colour_transform()

image sb_dpstand_pc_face_ag_lipstick_layer:
    "sb_dpstand_pc_face_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_dpstand_pc_face_ag_brow_layer:
    "sb_dpstand_pc_face_ag_brow"
    hair_colour_transform()

image sb_dpstand_pc_face_oh_lipstick_layer:
    "sb_dpstand_pc_face_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_dpstand_pc_face_oh_brow_layer:
    "sb_dpstand_pc_face_oh_brow"
    hair_colour_transform()

image sb_dpstand_pc_face_ahh_lipstick_layer:
    "sb_dpstand_pc_face_ahh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_dpstand_pc_face_ahh_brow_layer:
    "sb_dpstand_pc_face_ahh_brow"
    hair_colour_transform()

image sb_dpstand_pc_face_neutral_lipstick_layer:
    "sb_dpstand_pc_face_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_dpstand_pc_face_neutral_brow_layer:
    "sb_dpstand_pc_face_neutral_brow"
    hair_colour_transform()



image sb_dpstand_pc_eye_forward_eyeliner_layer:
    "sb_dpstand_pc_eye_forward_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_dpstand_pc_eye_back_eyeliner_layer:
    "sb_dpstand_pc_eye_back_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_dpstand_pc_eye_forward_iris_layer:
    "sb_dpstand_pc_eye_forward_iris"
    eye_colour_transform()
image sb_dpstand_pc_eye_back_iris_layer:
    "sb_dpstand_pc_eye_back_iris"
    eye_colour_transform()



image sb_dpstand_pc_writing_ass_layer:
    "sb_dpstand_pc_writing_ass"
    writing_transform("ass")
image sb_dpstand_pc_writing_anus_layer:
    "sb_dpstand_pc_writing_anus"
    writing_transform("anus")
image sb_dpstand_pc_writing_face_layer:
    "sb_dpstand_pc_writing_face"
    writing_transform("face")
image sb_dpstand_pc_writing_forehead_layer:
    "sb_dpstand_pc_writing_forehead"
    writing_transform("forehead")



image sb_dpstand_pc_gag_metal_layer:
    "sb_dpstand_pc_gag_metal"
    gag_metal_transform()
image sb_dpstand_pc_gag_base_layer:
    "sb_dpstand_pc_gag_base"
    gag_colour_transform()
image sb_dpstand_pc_gag_lipstick_layer:
    "sb_dpstand_pc_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))



image sb_dpstand_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_dpstand_pc_hair_front")
    hair_colour_transform()

image sb_dpstand_pc_hair_back_pony_4 = "sb_dpstand_pc_hair_back_pony_3"
image sb_dpstand_pc_hair_back_bun_2 = "sb_dpstand_pc_hair_back_bun"
image sb_dpstand_pc_hair_back_bun_3 = "sb_dpstand_pc_hair_back_bun"
image sb_dpstand_pc_hair_back_bun_4 = "sb_dpstand_pc_hair_back_bun"
image sb_dpstand_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_dpstand_pc_hair_back")
    hair_colour_transform()





image sb_dpstand_manf_top_base_layer:
    "sb_dpstand_manf_top_base"
    npc_skin_base_colour_transform()
image sb_dpstand_manf_top_shad_layer:
    "sb_dpstand_manf_top_shad"
    npc_skin_shad_colour_transform()

image sb_dpstand_manf_vag_base_layer:
    "sb_dpstand_manf_vag_base"
    npc_skin_base_colour_transform()
image sb_dpstand_manf_vag_shad_layer:
    "sb_dpstand_manf_vag_shad"
    npc_skin_shad_colour_transform()
image sb_dpstand_manf_vag_vag_layer:
    "sb_dpstand_manf_vag_vag"
    vagina_colour_transform()

image sb_dpstand_manf_anal_base_layer:
    "sb_dpstand_manf_anal_base"
    npc_skin_base_colour_transform()
image sb_dpstand_manf_anal_shad_layer:
    "sb_dpstand_manf_anal_shad"
    npc_skin_shad_colour_transform()

image sb_dpstand_manf_poke_base_layer:
    "sb_dpstand_manf_poke_base"
    npc_skin_base_colour_transform()
image sb_dpstand_manf_poke_shad_layer:
    "sb_dpstand_manf_poke_shad"
    npc_skin_shad_colour_transform()



image sb_dpstand_manb_top_base_layer:
    "sb_dpstand_manb_top_base"
    npc2_skin_base_colour_transform()
image sb_dpstand_manb_top_shad_layer:
    "sb_dpstand_manb_top_shad"
    npc2_skin_shad_colour_transform()

image sb_dpstand_manb_vag_base_layer:
    "sb_dpstand_manb_vag_base"
    npc2_skin_base_colour_transform()
image sb_dpstand_manb_vag_shad_layer:
    "sb_dpstand_manb_vag_shad"
    npc2_skin_shad_colour_transform()
image sb_dpstand_manb_vag_vag_layer:
    "sb_dpstand_manb_vag_vag"
    vagina_colour_transform()

image sb_dpstand_manb_anal_base_layer:
    "sb_dpstand_manb_anal_base"
    npc2_skin_base_colour_transform()
image sb_dpstand_manb_anal_shad_layer:
    "sb_dpstand_manb_anal_shad"
    npc2_skin_shad_colour_transform()

image sb_dpstand_manb_poke_base_layer:
    "sb_dpstand_manb_poke_base"
    npc2_skin_base_colour_transform()
image sb_dpstand_manb_poke_shad_layer:
    "sb_dpstand_manb_poke_shad"
    npc2_skin_shad_colour_transform()


image sb_dpstand = LayeredImageProxy("sb_dpstand_layered", Transform(xalign = (0.80)))

image sb_dpstand_effect_rain_loop:
    "sb_dpstand_effect_rain1"
    .03
    "sb_dpstand_effect_rain2"
    .03
    "sb_dpstand_effect_rain3"
    .03
    repeat

layeredimage sb_dpstand_shower_layered:
    always "sb_dpstand_effect_rain_loop"
    always "sb_dpstand_effect_steam"

layeredimage sb_dpstand_pc_gag:
    always "sb_dpstand_pc_gag_lipstick_layer"
    always "sb_dpstand_pc_gag_base_layer"
    always "sb_dpstand_pc_gag_metal_layer"

layeredimage sb_dpstand_layered:

    always "sb_dpstand_bg_layer"

    always "sb_dpstand_pc_body_base_layer"
    always "sb_dpstand_pc_body_shad_layer"
    always "sb_dpstand_pc_body_vag_layer"
    always "sb_dpstand_pc_body_nails_layer"

    always "sb_dpstand_pc_det_blush_layer"
    always "sb_dpstand_pc_det_spank_layer"
    always "sb_dpstand_pc_det_freckles_layer"
    always "sb_dpstand_pc_det_eyeshadow_layer"
    if player.phair:
        "sb_dpstand_pc_det_phair_layer"

    group face:

        attribute neutral default "sb_dpstand_pc_face_neutral_lipstick_layer"
        attribute neutral default "sb_dpstand_pc_face_neutral_brow_layer"

        attribute happy "sb_dpstand_pc_face_happy_brow_layer"
        attribute happy "sb_dpstand_pc_face_happy_lipstick_layer"
        attribute happy "sb_dpstand_pc_face_happy_col"

        attribute ag "sb_dpstand_pc_face_ag_brow_layer"
        attribute ag "sb_dpstand_pc_face_ag_lipstick_layer"
        attribute ag "sb_dpstand_pc_face_ag_col"

        attribute ahh "sb_dpstand_pc_face_ahh_brow_layer"
        attribute ahh "sb_dpstand_pc_face_ahh_lipstick_layer"
        attribute ahh "sb_dpstand_pc_face_ahh_col"

        attribute oh "sb_dpstand_pc_face_oh_brow_layer"
        attribute oh "sb_dpstand_pc_face_oh_lipstick_layer"
        attribute oh "sb_dpstand_pc_face_oh_col"

    group eye:
        attribute forward default "sb_dpstand_pc_eye_forward_iris_layer"
        attribute forward default "sb_dpstand_pc_eye_forward_eye"
        attribute forward default "sb_dpstand_pc_eye_forward_eyeliner_layer"

        attribute back "sb_dpstand_pc_eye_back_iris_layer"
        attribute back "sb_dpstand_pc_eye_back_eye"
        attribute back "sb_dpstand_pc_eye_back_eyeliner_layer"

    if writing.ass:
        "sb_dpstand_pc_writing_ass_layer"
    if writing.anus:
        "sb_dpstand_pc_writing_anus_layer"
    if writing.face:
        "sb_dpstand_pc_writing_face_layer"
    if writing.forehead:
        "sb_dpstand_pc_writing_forehead_layer"

    if player.has_perk([perk_gagged, perk_gagged_locked]):
        "sb_dpstand_pc_gag"
    if acc.anus:
        "sb_dpstand_pc_plug"
    if player.has_perk(perk_blind):
        "sb_dpstand_pc_blind"

    always "sb_dpstand_pc_hair_back_layer"
    always "sb_dpstand_pc_hair_front_layer"


    group man_front:

        attribute noman default null

        attribute poke "sb_dpstand_manf_poke_base_layer"
        attribute poke "sb_dpstand_manf_poke_shad_layer"

        attribute vag "sb_dpstand_manf_vag_vag_layer"
        attribute vag "sb_dpstand_manf_vag_base_layer"
        attribute vag "sb_dpstand_manf_vag_shad_layer"

        attribute anal "sb_dpstand_manf_anal_base_layer"
        attribute anal "sb_dpstand_manf_anal_shad_layer"

    always if_any ["vag", "poke", "anal"] "sb_dpstand_manf_top_base_layer"
    always if_any ["vag", "poke", "anal"] "sb_dpstand_manf_top_shad_layer"

    group man_behind:

        attribute bnoman default null

        attribute bpoke "sb_dpstand_manb_poke_base_layer"
        attribute bpoke "sb_dpstand_manb_poke_shad_layer"

        attribute bvag "sb_dpstand_manb_vag_vag_layer"
        attribute bvag "sb_dpstand_manb_vag_base_layer"
        attribute bvag "sb_dpstand_manb_vag_shad_layer"

        attribute banal "sb_dpstand_manb_anal_base_layer"
        attribute banal "sb_dpstand_manb_anal_shad_layer"

    always if_any ["bvag", "bpoke", "banal"] "sb_dpstand_manb_top_base_layer"
    always if_any ["bvag", "bpoke", "banal"] "sb_dpstand_manb_top_shad_layer"

    if "shower" in loc_cur.name:
        "sb_dpstand_shower_layered"

    always "sb_dpstand_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
