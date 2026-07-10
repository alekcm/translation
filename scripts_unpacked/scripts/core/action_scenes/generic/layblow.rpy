
image sb_layblow_manlay_base_layer:
    "sb_layblow_manlay_base"
    npc_skin_base_colour_transform()
image sb_layblow_manlay_shad_layer:
    "sb_layblow_manlay_shad"
    npc_skin_shad_colour_transform()


image sb_layblow_mansex_base_layer:
    "sb_layblow_mansex_base"
    npc_skin_base_colour_transform()
image sb_layblow_mansex_shad_layer:
    "sb_layblow_mansex_shad"
    npc_skin_shad_colour_transform()


image sb_layblow_pc_mast_base_layer:
    "sb_layblow_pc_mast_base"
    skin_base_colour_transform()
image sb_layblow_pc_mast_shad_layer:
    "sb_layblow_pc_mast_shad"
    skin_shad_colour_transform()
image sb_layblow_pc_mast_m_base_layer:
    "sb_layblow_pc_mast_m_base"
    npc_skin_base_colour_transform()
image sb_layblow_pc_mast_m_shad_layer:
    "sb_layblow_pc_mast_m_shad"
    npc_skin_shad_colour_transform()
image sb_layblow_pc_mast_nails_layer:
    "sb_layblow_pc_mast_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))


image sb_layblow_pc_blow_base_layer:
    "sb_layblow_pc_blow_base"
    skin_base_colour_transform()
image sb_layblow_pc_blow_shad_layer:
    "sb_layblow_pc_blow_shad"
    skin_shad_colour_transform()
image sb_layblow_pc_blow_m_base_layer:
    "sb_layblow_pc_blow_m_base"
    npc_skin_base_colour_transform()
image sb_layblow_pc_blow_m_shad_layer:
    "sb_layblow_pc_blow_m_shad"
    npc_skin_shad_colour_transform()
image sb_layblow_pc_blow_nails_layer:
    "sb_layblow_pc_blow_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))
image sb_layblow_pc_blow_lipstick_layer:
    "sb_layblow_pc_blow_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))


image sb_layblow_pc_body_base_layer:
    "sb_layblow_pc_body_base"
    skin_base_colour_transform()
image sb_layblow_pc_body_shad_layer:
    "sb_layblow_pc_body_shad"
    skin_shad_colour_transform()
image sb_layblow_pc_body_nails_layer:
    "sb_layblow_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))


image sb_layblow_pc_face_blush_layer:
    "sb_layblow_pc_face_blush"
    blush_opacity_transform()
image sb_layblow_pc_face_freckles_layer:
    "sb_layblow_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_layblow_pc_face_spank_layer:
    "sb_layblow_pc_face_spank"
    opacity_transform(bruise.ass)


image sb_layblow_pc_writing_face_layer:
    "sb_layblow_pc_writing_face"
    writing_transform("face")
image sb_layblow_pc_writing_forehead_layer:
    "sb_layblow_pc_writing_forehead"
    writing_transform("forehead")


image sb_layblow_pc_eye_eyeliner_forward_layer:
    "sb_layblow_pc_eye_eyeliner_forward_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_layblow_pc_eye_eyeliner_down_layer:
    "sb_layblow_pc_eye_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_layblow_pc_eye_iris_forward_layer:
    "sb_layblow_pc_eye_iris_forward"
    eye_colour_transform()
image sb_layblow_pc_eye_iris_down_layer:
    "sb_layblow_pc_eye_iris_down"
    eye_colour_transform()


image sb_layblow_pc_brow_straight_layer:
    "sb_layblow_pc_brow_straight"
    hair_colour_transform()
image sb_layblow_pc_brow_slant_layer:
    "sb_layblow_pc_brow_slant"
    hair_colour_transform()
image sb_layblow_pc_brow_worried_layer:
    "sb_layblow_pc_brow_worried"
    hair_colour_transform()

image sb_layblow_pc_mouth_laugh_lipstick_layer:
    "sb_layblow_pc_mouth_laugh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_layblow_pc_hair_back_pony_2 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_pony_3 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_pony_4 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_bun_2 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_bun_3 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_bun_4 = "sb_layblow_pc_hair_back_pony"
image sb_layblow_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_layblow_pc_hair_back")
    hair_colour_transform()

image sb_layblow_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_layblow_pc_hair_front")
    hair_colour_transform()

image sb_layblow = LayeredImageProxy("sb_layblow_layer", Transform(xalign = (0.85)))

layeredimage sb_layblow_layer:  
    always "sb_layblow_bg"

    always "sb_layblow_manlay_base_layer"
    always "sb_layblow_manlay_shad_layer"

    always "sb_layblow_pc_body_base_layer"
    always "sb_layblow_pc_body_shad_layer"
    always "sb_layblow_pc_body_nails_layer"
    if tattoo.ass:
        "sb_layblow_pc_tattoo_tramp"

    always "sb_layblow_pc_face_freckles_layer"
    always "sb_layblow_pc_face_blush_layer"
    always "sb_layblow_pc_face_spank_layer"

    if writing.face:
        "sb_layblow_pc_writing_face_layer"
    if writing.forehead:
        "sb_layblow_pc_writing_forehead_layer"

    group eye:
        attribute forward default "sb_layblow_pc_eye_iris_forward_layer"
        attribute forward default "sb_layblow_pc_eye_eye_forward"
        attribute forward default "sb_layblow_pc_eye_eyeliner_forward_layer"

        attribute down "sb_layblow_pc_eye_iris_down_layer"
        attribute down "sb_layblow_pc_eye_eye_down"
        attribute down "sb_layblow_pc_eye_eyeliner_down_layer"

    group brow:
        attribute happy default "sb_layblow_pc_brow_straight_layer"
        attribute slant "sb_layblow_pc_brow_slant_layer"
        attribute worried "sb_layblow_pc_brow_worried_layer"

    always if_any "mast" "sb_layblow_pc_mouth_laugh_lipstick_layer"  
    always if_any "mast" "sb_layblow_pc_mouth_laugh"


    if player.has_perk(perk_blind):
        "sb_layblow_pc_face_blindfold"

    group man_behind:
        attribute nosex default null

        attribute sex "sb_layblow_mansex_base_layer"
        attribute sex "sb_layblow_mansex_shad_layer"

    always "sb_layblow_pc_hair_back_layer"
    always "sb_layblow_pc_hair_front_layer"

    group hand:
        attribute mast default "sb_layblow_pc_mast_m_base_layer"
        attribute mast default "sb_layblow_pc_mast_m_shad_layer"
        attribute mast default "sb_layblow_pc_mast_base_layer"
        attribute mast default "sb_layblow_pc_mast_shad_layer"
        attribute mast default "sb_layblow_pc_mast_nails_layer"

        attribute blow "sb_layblow_pc_blow_lipstick_layer"
        attribute blow "sb_layblow_pc_blow_m_base_layer"
        attribute blow "sb_layblow_pc_blow_m_shad_layer"
        attribute blow "sb_layblow_pc_blow_base_layer"
        attribute blow "sb_layblow_pc_blow_shad_layer"
        attribute blow "sb_layblow_pc_blow_nails_layer"





    always "sb_layblow_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
