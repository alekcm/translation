
image sb_spitroast_bg_layer:
    "sb_spitroast_bg_" + loc_cur.loc_type


image sb_spitroast_pc_base_layer:
    "sb_spitroast_pc_base"
    skin_base_colour_transform()
image sb_spitroast_pc_shad_layer:
    "sb_spitroast_pc_shad"
    skin_shad_colour_transform()
image sb_spitroast_pc_hairshad_layer:
    get_hair_front_cg_filename("sb_spitroast_pc_hairshad")
    skin_shad_colour_transform()
image sb_spitroast_pc_nails_layer:
    "sb_spitroast_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_spitroast_manbsex_base_layer:
    "sb_spitroast_manbsex_base"
    npc2_skin_base_colour_transform()
image sb_spitroast_manbsex_shad_layer:
    "sb_spitroast_manbsex_shad"
    npc2_skin_shad_colour_transform()

image sb_spitroast_manbmast_base_layer:
    "sb_spitroast_manbmast_base"
    npc2_skin_base_colour_transform()
image sb_spitroast_manbmast_shad_layer:
    "sb_spitroast_manbmast_shad"
    npc2_skin_shad_colour_transform()
image sb_spitroast_manbmast_helm_layer:
    "sb_spitroast_manbmast_helm"
    npc2_skin_shad_colour_transform()

image sb_spitroast_manbinsert_base_layer:
    "sb_spitroast_manbinsert_base"
    npc2_skin_base_colour_transform()
image sb_spitroast_manbinsert_shad_layer:
    "sb_spitroast_manbinsert_shad"
    npc2_skin_shad_colour_transform()


image sb_spitroast_pc_larmmast_base_layer:
    "sb_spitroast_pc_larmmast_base"
    skin_base_colour_transform()
image sb_spitroast_pc_larmmast_shad_layer:
    "sb_spitroast_pc_larmmast_shad"
    skin_shad_colour_transform()
image sb_spitroast_pc_larmmast_arm_layer:
    "sb_spitroast_pc_larmmast_arm"
    skin_shad_colour_transform()
image sb_spitroast_pc_larmmast_nails_layer:
    "sb_spitroast_pc_larmmast_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_spitroast_pc_face_mouth_frown_lipstick_layer:
    "sb_spitroast_pc_face_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_pc_face_mouth_happy_lipstick_layer:
    "sb_spitroast_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_pc_face_mouth_neutral_lipstick_layer:
    "sb_spitroast_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_pc_face_mouth_shock_lipstick_layer:
    "sb_spitroast_pc_face_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_pc_face_mouth_smile_lipstick_layer:
    "sb_spitroast_pc_face_mouth_smile_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_pc_face_mouth_tounge_lipstick_layer:
    "sb_spitroast_pc_face_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_spitroast_blow_lipstick_layer:
    "sb_spitroast_blow_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_spitroast_pc_face_eyeshadow_layer:
    "sb_spitroast_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image sb_spitroast_pc_face_freckles_layer:
    "sb_spitroast_pc_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_spitroast_pc_face_blush_layer:
    "sb_spitroast_pc_face_blush"
    blush_opacity_transform()
image sb_spitroast_pc_spank_layer:
    "sb_spitroast_pc_spank"
    opacity_transform(bruise.ass)

image sb_spitroast_pc_face_eyeliner_up_layer:
    "sb_spitroast_pc_face_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_spitroast_pc_face_eyeliner_closed_layer:
    "sb_spitroast_pc_face_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_spitroast_pc_face_eyeliner_down_layer:
    "sb_spitroast_pc_face_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_spitroast_pc_face_eye_iris_down_layer:
    "sb_spitroast_pc_face_eye_iris_down"
    eye_colour_transform()
image sb_spitroast_pc_face_eye_iris_back_layer:
    "sb_spitroast_pc_face_eye_iris_back"
    eye_colour_transform()
image sb_spitroast_pc_face_eye_iris_up_layer:
    "sb_spitroast_pc_face_eye_iris_up"
    eye_colour_transform()

image sb_spitroast_pc_face_brow_straight_layer:
    "sb_spitroast_pc_face_brow_straight"
    hair_colour_transform()
image sb_spitroast_pc_face_brow_worried_layer:
    "sb_spitroast_pc_face_brow_worried"
    hair_colour_transform()
image sb_spitroast_pc_face_brow_angry_layer:
    "sb_spitroast_pc_face_brow_angry"
    hair_colour_transform()


image sb_spitroast_pc_hair_back_bun_2 = "sb_spitroast_pc_hair_back_bun"
image sb_spitroast_pc_hair_back_bun_3 = "sb_spitroast_pc_hair_back_bun"
image sb_spitroast_pc_hair_back_bun_4 = "sb_spitroast_pc_hair_back_bun"
image sb_spitroast_pc_hair_back_pony_4 = "sb_spitroast_pc_hair_back_pony_3"

image sb_spitroast_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_spitroast_pc_hair_back")
    hair_colour_transform()

image sb_spitroast_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_spitroast_pc_hair_front")
    hair_colour_transform()

image sb_spitroast_blow_base_layer:
    "sb_spitroast_blow_base"
    npc_skin_base_colour_transform()
image sb_spitroast_blow_shad_layer:
    "sb_spitroast_blow_shad"
    npc_skin_shad_colour_transform()


image sb_spitroast_mast_pc_base_layer:
    "sb_spitroast_mast_pc_base"
    skin_base_colour_transform()
image sb_spitroast_mast_pc_shad_layer:
    "sb_spitroast_mast_pc_shad"
    skin_shad_colour_transform()
image sb_spitroast_mast_pc_nails_layer:
    "sb_spitroast_mast_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_spitroast_mast_man_base_layer:
    "sb_spitroast_mast_man_base"
    npc_skin_base_colour_transform()
image sb_spitroast_mast_man_shad_layer:
    "sb_spitroast_mast_man_shad"
    npc_skin_shad_colour_transform()
image sb_spitroast_mast_man_helm_layer:
    "sb_spitroast_mast_man_helm"
    npc_skin_shad_colour_transform()

image sb_spitroast_manfront_base_layer:
    "sb_spitroast_manfront_base"
    npc_skin_base_colour_transform()
image sb_spitroast_manfront_shad_layer:
    "sb_spitroast_manfront_shad"
    npc_skin_shad_colour_transform()

image sb_spitroast_pc_writing_face_layer:
    "sb_spitroast_pc_writing_face"
    writing_transform("face")
image sb_spitroast_pc_writing_forehead_layer:
    "sb_spitroast_pc_writing_forehead"
    writing_transform("forehead")
image sb_spitroast_pc_writing_glasses_layer:
    "sb_spitroast_pc_writing_glasses"
    writing_transform("special")

image sb_spitroast = LayeredImageProxy("sb_spitroast_layered", Transform(xalign = (0.7)))

layeredimage sb_spitroast_layered: 

    always "sb_spitroast_bg_layer"

    always "sb_spitroast_pc_base_layer"
    always "sb_spitroast_pc_hairshad_layer"
    always "sb_spitroast_pc_shad_layer"
    always "sb_spitroast_pc_nails_layer"
    always "sb_spitroast_pc_spank_layer"

    if player.cum_locations["cum_face"]:
        "sb_spitroast_pc_cum_face"
    if player.cum_locations["cum_mouth"]:
        "sb_spitroast_pc_cum_mouth"

    group brow:
        attribute straight default "sb_spitroast_pc_face_brow_straight_layer"
        attribute worried "sb_spitroast_pc_face_brow_worried_layer"
        attribute angry "sb_spitroast_pc_face_brow_angry_layer"

    always "sb_spitroast_pc_face_eyeshadow_layer"
    if skin_effect.face:
        "sb_spitroast_pc_face_freckles_layer"
    always "sb_spitroast_pc_face_blush_layer"

    group eye:
        attribute up default "sb_spitroast_pc_face_eye_iris_up_layer"
        attribute up default "sb_spitroast_pc_face_eye_eye_up"
        attribute up default "sb_spitroast_pc_face_eyeliner_up_layer"

        attribute closed "sb_spitroast_pc_face_eyeliner_closed_layer"

        attribute down "sb_spitroast_pc_face_eye_iris_down_layer"
        attribute down "sb_spitroast_pc_face_eye_eye_down"
        attribute down "sb_spitroast_pc_face_eyeliner_down_layer"

        attribute back "sb_spitroast_pc_face_eye_iris_back_layer"
        attribute back "sb_spitroast_pc_face_eye_eye_back"
        attribute back "sb_spitroast_pc_face_eyeliner_up_layer"


    group manbehind:
        attribute noman default null

        attribute insert "sb_spitroast_manbinsert_base_layer"
        attribute insert "sb_spitroast_manbinsert_shad_layer"

        attribute cum "sb_spitroast_manbmast_base_layer"
        attribute cum "sb_spitroast_manbmast_shad_layer"
        attribute cum "sb_spitroast_manbmast_helm_layer"

        attribute sex "sb_spitroast_manbsex_base_layer"
        attribute sex "sb_spitroast_manbsex_shad_layer"


    if player.beingraped:
        "sb_spitroast_pc_face_tear"

    if writing.face:
        "sb_spitroast_pc_writing_face_layer"
    if writing.forehead:
        "sb_spitroast_pc_writing_forehead_layer"
    if writing.special == "glasses":
        "sb_spitroast_pc_writing_glasses_layer"

    always "sb_spitroast_pc_hair_back_layer"
    always "sb_spitroast_pc_hair_front_layer"

    group mouth:
        attribute frown "sb_spitroast_pc_face_mouth_frown_lipstick_layer"
        attribute frown "sb_spitroast_pc_face_mouth_frown"

        attribute happy "sb_spitroast_pc_face_mouth_happy_lipstick_layer"
        attribute happy "sb_spitroast_pc_face_mouth_happy"

        attribute neutral "sb_spitroast_pc_face_mouth_neutral_lipstick_layer"
        attribute neutral "sb_spitroast_pc_face_mouth_neutral"

        attribute shock "sb_spitroast_pc_face_mouth_shock_lipstick_layer"
        attribute shock "sb_spitroast_pc_face_mouth_shock"

        attribute neutral default "sb_spitroast_pc_face_mouth_neutral_lipstick_layer"
        attribute neutral default "sb_spitroast_pc_face_mouth_neutral"

        attribute smile "sb_spitroast_pc_face_mouth_smile_lipstick_layer"
        attribute smile "sb_spitroast_pc_face_mouth_smile"

        attribute tounge "sb_spitroast_pc_face_mouth_tounge_lipstick_layer"
        attribute tounge "sb_spitroast_pc_face_mouth_tounge"

        attribute blow null

    group penis:
        attribute blow "sb_spitroast_blow_lipstick_layer"
        attribute blow "sb_spitroast_blow_base_layer"
        attribute blow "sb_spitroast_blow_shad_layer"

    always "sb_spitroast_manfront_base_layer"
    always "sb_spitroast_manfront_shad_layer"

    group penis:

        attribute nopenis default null


        attribute mast "sb_spitroast_mast_man_base_layer"
        attribute mast "sb_spitroast_mast_man_shad_layer"
        attribute mast "sb_spitroast_mast_man_helm_layer"
        attribute mast "sb_spitroast_mast_pc_base_layer"
        attribute mast "sb_spitroast_mast_pc_shad_layer"
        attribute mast "sb_spitroast_mast_pc_nails_layer"


    always "sb_spitroast_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
