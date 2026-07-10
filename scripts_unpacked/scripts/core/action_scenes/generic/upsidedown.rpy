

image sb_upsidedown_pc_body_base_layer:
    "sb_upsidedown_pc_body_base"
    skin_base_colour_transform()
image sb_upsidedown_pc_body_shad_layer:
    "sb_upsidedown_pc_body_shad"
    skin_shad_colour_transform()
image sb_upsidedown_pc_body_vag_layer:
    "sb_upsidedown_pc_body_vag"
    vagina_colour_transform()
image sb_upsidedown_pc_body_hair_layer:
    "sb_upsidedown_pc_body_hair"
    hair_colour_transform()
image sb_upsidedown_pc_body_phair_layer:
    "sb_upsidedown_pc_body_phair"
    phair_colour_transform()
image sb_upsidedown_pc_body_spank_layer:
    "sb_upsidedown_pc_body_spank"
    opacity_transform(bruise.ass)



image sb_upsidedown_pc_breasts_base_layer:
    get_skin_filename("sb_upsidedown_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_upsidedown_pc_breasts_shad_layer:
    get_skin_filename("sb_upsidedown_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_upsidedown_pc_breasts_nips_layer:
    get_skin_filename("sb_upsidedown_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_upsidedown_pc_breasts_nipring_layer:
    get_skin_filename("sb_upsidedown_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_upsidedown_pc_breasts_tattoo_layer:
    get_skin_filename("sb_upsidedown_pc_breasts_tattoo", breasts=True)



image sb_upsidedown_pc_face_freckles_layer:
    "sb_upsidedown_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_upsidedown_pc_face_blush_layer:
    "sb_upsidedown_pc_face_blush"
    blush_opacity_transform()
image sb_upsidedown_pc_face_eyeshad_layer:
    "sb_upsidedown_pc_face_eyeshad"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image sb_upsidedown_pc_face_eye_up_eyeliner_layer:
    "sb_upsidedown_pc_face_eye_up_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_upsidedown_pc_face_eye_down_eyeliner_layer:
    "sb_upsidedown_pc_face_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_upsidedown_pc_face_eye_closed_eyeliner_layer:
    "sb_upsidedown_pc_face_eye_closed_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_upsidedown_pc_face_eye_up_iris_layer:
    "sb_upsidedown_pc_face_eye_up_iris"
    eye_colour_transform()
image sb_upsidedown_pc_face_eye_down_iris_layer:
    "sb_upsidedown_pc_face_eye_down_iris"
    eye_colour_transform()

image sb_upsidedown_pc_face_mouth_ag_lipstick_layer:
    "sb_upsidedown_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_upsidedown_pc_face_mouth_ah_lipstick_layer:
    "sb_upsidedown_pc_face_mouth_ah_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_upsidedown_pc_face_mouth_happy_lipstick_layer:
    "sb_upsidedown_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_upsidedown_pc_face_mouth_smile_lipstick_layer:
    "sb_upsidedown_pc_face_mouth_smile_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_upsidedown_pc_face_mouth_pout_lipstick_layer:
    "sb_upsidedown_pc_face_mouth_pout_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_upsidedown_pc_face_brow_worried_layer:
    "sb_upsidedown_pc_face_brow_worried"
    hair_colour_transform()
image sb_upsidedown_pc_face_brow_angry_layer:
    "sb_upsidedown_pc_face_brow_angry"
    hair_colour_transform()
image sb_upsidedown_pc_face_brow_neutral_layer:
    "sb_upsidedown_pc_face_brow_neutral"
    hair_colour_transform()

image sb_upsidedown_pc_face_gag_base_layer:
    "sb_upsidedown_pc_face_gag_base"
    gag_colour_transform()
image sb_upsidedown_pc_face_gag_metal_layer:
    "sb_upsidedown_pc_face_gag_metal"
    gag_metal_transform()
image sb_upsidedown_pc_face_gag_lipstick_layer:
    "sb_upsidedown_pc_face_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))



image sb_upsidedown_pc_writing_chest_layer:
    "sb_upsidedown_pc_writing_chest"
    writing_transform("chest")
image sb_upsidedown_pc_writing_ass_layer:
    "sb_upsidedown_pc_writing_ass"
    writing_transform("ass")
image sb_upsidedown_pc_writing_anus_layer:
    "sb_upsidedown_pc_writing_anus"
    writing_transform("anus")
image sb_upsidedown_pc_writing_face_layer:
    "sb_upsidedown_pc_writing_face"
    writing_transform("face")
image sb_upsidedown_pc_writing_forehead_layer:
    "sb_upsidedown_pc_writing_forehead"
    writing_transform("forehead")



image sb_upsidedown_man_poke_base_layer:
    "sb_upsidedown_man_poke_base"
    npc_skin_base_colour_transform()
image sb_upsidedown_man_poke_shad_layer:
    "sb_upsidedown_man_poke_shad"
    npc_skin_shad_colour_transform()

image sb_upsidedown_man_blow_base_layer:
    "sb_upsidedown_man_blow_base"
    npc_skin_base_colour_transform()
image sb_upsidedown_man_blow_shad_layer:
    "sb_upsidedown_man_blow_shad"
    npc_skin_shad_colour_transform()
image sb_upsidedown_man_blow_lipstick_layer:
    "sb_upsidedown_man_blow_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_upsidedown_man_blowdeep_base_layer:
    "sb_upsidedown_man_blowdeep_base"
    npc_skin_base_colour_transform()
image sb_upsidedown_man_blowdeep_shad_layer:
    "sb_upsidedown_man_blowdeep_shad"
    npc_skin_shad_colour_transform()

image sb_upsidedown_man_vag_base_layer:
    "sb_upsidedown_man_vag_base"
    npc_skin_base_colour_transform()
image sb_upsidedown_man_vag_shad_layer:
    "sb_upsidedown_man_vag_shad"
    npc_skin_shad_colour_transform()
image sb_upsidedown_man_vag_vag_layer:
    "sb_upsidedown_man_vag_vag"
    vagina_colour_transform()

image sb_upsidedown_man_ass_base_layer:
    "sb_upsidedown_man_ass_base"
    npc_skin_base_colour_transform()
image sb_upsidedown_man_ass_shad_layer:
    "sb_upsidedown_man_ass_shad"
    npc_skin_shad_colour_transform()
image sb_upsidedown_man_ass_vag_layer:
    "sb_upsidedown_man_ass_vag"
    vagina_colour_transform()

image sb_upsidedown = LayeredImageProxy("sb_upsidedown_layered", Transform(xalign = (0.7)))

layeredimage sb_upsidedown_layered:
    always "sb_upsidedown_bg"

    always "sb_upsidedown_pc_body_base_layer"
    always "sb_upsidedown_pc_body_shad_layer"
    always "sb_upsidedown_pc_body_vag_layer"
    always "sb_upsidedown_pc_body_hair_layer"
    always "sb_upsidedown_pc_body_lines"
    always "sb_upsidedown_pc_body_spank_layer"
    if player.phair:
        "sb_upsidedown_pc_body_phair_layer"

    if player.cum_locations["cum_vagin"]:
        "sb_upsidedown_pc_cum_vag"
    if player.cum_locations["cum_assin"]:
        "sb_upsidedown_pc_body_anus"
    if player.cum_locations["cum_assin"]:
        "sb_upsidedown_pc_cum_anus"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "sb_upsidedown_pc_cum_ass"
    if player.cum_locations["cum_mouth"]:
        "sb_upsidedown_pc_cum_mouth"
    if player.cum_locations["cum_face"]:
        "sb_upsidedown_pc_cum_face"

    if acc.anus:
        "sb_upsidedown_pc_plug"


    if writing.chest:
        "sb_upsidedown_pc_writing_chest_layer"
    if writing.ass:
        "sb_upsidedown_pc_writing_ass_layer"
    if writing.anus:
        "sb_upsidedown_pc_writing_anus_layer"
    if writing.face:
        "sb_upsidedown_pc_writing_face_layer"
    if writing.forehead:
        "sb_upsidedown_pc_writing_forehead_layer"

    always "sb_upsidedown_pc_breasts_base_layer"
    always "sb_upsidedown_pc_breasts_shad_layer"
    always "sb_upsidedown_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_upsidedown_pc_breasts_nipring_layer"
    if tattoo.chest:
        "sb_upsidedown_pc_breasts_tattoo_layer"

    always "sb_upsidedown_pc_face_freckles_layer"
    always "sb_upsidedown_pc_face_blush_layer"
    always "sb_upsidedown_pc_face_eyeshad_layer"

    group eyes:
        attribute up default "sb_upsidedown_eye_up_layered"
        attribute down "sb_upsidedown_eye_down_layered"
        attribute closed "sb_upsidedown_pc_face_eye_closed_eyeliner_layer"


    group face:
        attribute angry "sb_upsidedown_pc_face_mouth_pout_lipstick_layer"
        attribute angry "sb_upsidedown_pc_face_mouth_pout"
        attribute angry "sb_upsidedown_pc_face_brow_angry_layer"

        attribute neutral default "sb_upsidedown_pc_face_brow_neutral_layer"
        attribute neutral default "sb_upsidedown_pc_face_mouth_smile_lipstick_layer"
        attribute neutral default "sb_upsidedown_pc_face_mouth_smile"

        attribute ag "sb_upsidedown_pc_face_mouth_ag_lipstick_layer"
        attribute ag "sb_upsidedown_pc_face_mouth_ag"
        attribute ag "sb_upsidedown_pc_face_brow_worried_layer"

        attribute ah "sb_upsidedown_pc_face_mouth_ah_lipstick_layer"
        attribute ah "sb_upsidedown_pc_face_mouth_ah"
        attribute ah "sb_upsidedown_pc_face_brow_worried_layer"  

        attribute happy "sb_upsidedown_pc_face_mouth_happy_lipstick_layer"
        attribute happy "sb_upsidedown_pc_face_mouth_happy"
        attribute happy "sb_upsidedown_pc_face_brow_neutral_layer"

        attribute pain "sb_upsidedown_pc_face_mouth_ah_lipstick_layer"
        attribute pain "sb_upsidedown_pc_face_mouth_ah"
        attribute pain "sb_upsidedown_pc_face_brow_angry_layer"

        attribute pout "sb_upsidedown_pc_face_mouth_pout_lipstick_layer"
        attribute pout "sb_upsidedown_pc_face_mouth_pout"
        attribute pout "sb_upsidedown_pc_face_brow_worried_layer"

        attribute blow "sb_upsidedown_pc_face_brow_worried_layer"  
        attribute blowdeep "sb_upsidedown_pc_face_brow_worried_layer"  

    if player.gagged:
        "sb_upsidedown_pc_face_gag"
    if player.blind:
        "sb_upsidedown_pc_blind"
    group man:
        attribute noman default null
        attribute blow "sb_upsidedown_man_blow_layerd"
        attribute blowdeep "sb_upsidedown_man_blowdeep_layerd"
        attribute poke "sb_upsidedown_man_poke_layerd"
        attribute vag "sb_upsidedown_man_vag_layerd"
        attribute ass "sb_upsidedown_man_ass_layerd"


    always "sb_upsidedown_frame"

layeredimage sb_upsidedown_eye_up_layered:
    always "sb_upsidedown_pc_face_eye_up_iris_layer"
    always "sb_upsidedown_pc_face_eye_up_eye"
    always "sb_upsidedown_pc_face_eye_up_eyeliner_layer"

layeredimage sb_upsidedown_eye_down_layered:
    always "sb_upsidedown_pc_face_eye_down_iris_layer"
    always "sb_upsidedown_pc_face_eye_down_eye"
    always "sb_upsidedown_pc_face_eye_down_eyeliner_layer"

layeredimage sb_upsidedown_pc_face_gag:
    always "sb_upsidedown_pc_face_gag_lipstick_layer"

    always "sb_upsidedown_pc_face_gag_base_layer"
    always "sb_upsidedown_pc_face_gag_metal_layer"

layeredimage sb_upsidedown_man_poke_layerd:
    always "sb_upsidedown_man_poke_base_layer"
    always "sb_upsidedown_man_poke_shad_layer"

layeredimage sb_upsidedown_man_blow_layerd:
    always "sb_upsidedown_man_blow_lipstick_layer"
    always "sb_upsidedown_man_blow_base_layer"
    always "sb_upsidedown_man_blow_shad_layer"

layeredimage sb_upsidedown_man_blowdeep_layerd:
    always "sb_upsidedown_man_blow_lipstick_layer"
    always "sb_upsidedown_man_blowdeep_base_layer"
    always "sb_upsidedown_man_blowdeep_shad_layer"

layeredimage sb_upsidedown_man_vag_layerd:
    always "sb_upsidedown_man_vag_vag_layer"
    always "sb_upsidedown_man_vag_base_layer"
    always "sb_upsidedown_man_vag_shad_layer"

layeredimage sb_upsidedown_man_ass_layerd:
    always "sb_upsidedown_man_ass_vag_layer"
    always "sb_upsidedown_man_ass_base_layer"
    always "sb_upsidedown_man_ass_shad_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
