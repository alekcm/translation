image sb_againstwall3_bg_plaster = "sb_againstwall3_bg_room"

image sb_againstwall3_bg_layer:
    "sb_againstwall3_bg_" + loc_cur.loc_type


image sb_againstwall3_pc_base_layer:
    "sb_againstwall3_pc_base"
    skin_base_colour_transform()
image sb_againstwall3_pc_shad_layer:
    "sb_againstwall3_pc_shad"
    skin_shad_colour_transform()
image sb_againstwall3_pc_hairshad_layer:
    get_hair_front_cg_filename("sb_againstwall3_pc_hairshad")
    skin_shad_colour_transform()
image sb_againstwall3_pc_nails_layer:
    "sb_againstwall3_pc_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))
image sb_againstwall3_pc_preg_layer:
    "sb_againstwall3_pc_preg"
    skin_base_colour_transform()
image sb_againstwall3_pc_spank_layer:
    "sb_againstwall3_pc_spank"
    opacity_transform(bruise.ass)

image sb_againstwall3_pc_breasts_base_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_againstwall3_pc_breasts_shad_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_againstwall3_pc_breasts_nips_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_againstwall3_pc_breasts_nipring_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_againstwall3_pc_breasts_tattoo_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_tattoo", breasts=True)

image sb_againstwall3_pc_breasts_dress_col_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_dress_col", breasts=True)
image sb_againstwall3_pc_breasts_dress_base_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_dress_base", breasts=True)
    skin_base_colour_transform()
image sb_againstwall3_pc_breasts_dress_shad_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_dress_shad", breasts=True)
    skin_shad_colour_transform()
image sb_againstwall3_pc_breasts_dress_tattoo_layer:
    get_skin_filename("sb_againstwall3_pc_breasts_dress_tattoo", breasts=True)


image sb_againstwall3_pc_face_freckles_layer:
    "sb_againstwall3_pc_face_freckles"
    skin_shad_colour_transform()
image sb_againstwall3_pc_face_blush_layer:
    "sb_againstwall3_pc_face_blush"
    blush_opacity_transform()

image sb_againstwall3_pc_face_mouth_ag_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall3_pc_face_mouth_grit_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_grit_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall3_pc_face_mouth_neutral_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall3_pc_face_mouth_happy_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall3_pc_face_mouth_smile_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_smile_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall3_pc_face_mouth_pout_lipstick_layer:
    "sb_againstwall3_pc_face_mouth_pout_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_againstwall3_pc_face_eyeshadow_layer:
    "sb_againstwall3_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image sb_againstwall3_pc_face_eyeliner_closed_layer:
    "sb_againstwall3_pc_face_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_againstwall3_pc_face_eyeliner_up_layer:
    "sb_againstwall3_pc_face_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_againstwall3_pc_face_eyeliner_wink_layer:
    "sb_againstwall3_pc_face_eyeliner_wink_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_againstwall3_pc_face_eyeliner_squint_layer:
    "sb_againstwall3_pc_face_eyeliner_squint_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_againstwall3_pc_face_eye_iris_up_layer:
    "sb_againstwall3_pc_face_eye_iris_up"
    eye_colour_transform()
image sb_againstwall3_pc_face_eye_iris_wink_layer:
    "sb_againstwall3_pc_face_eye_iris_wink"
    eye_colour_transform()
image sb_againstwall3_pc_face_eye_iris_squint_layer:
    "sb_againstwall3_pc_face_eye_iris_squint"
    eye_colour_transform()


image sb_againstwall3_pc_face_brow_straight_layer:
    "sb_againstwall3_pc_face_brow_straight"
    hair_colour_transform()
image sb_againstwall3_pc_face_brow_worried_layer:
    "sb_againstwall3_pc_face_brow_worried"
    hair_colour_transform()
image sb_againstwall3_pc_face_brow_angry_layer:
    "sb_againstwall3_pc_face_brow_angry"
    hair_colour_transform()
image sb_againstwall3_pc_face_brow_slant_layer:
    "sb_againstwall3_pc_face_brow_slant"
    hair_colour_transform()


image sb_againstwall3_mansex_base_layer:
    "sb_againstwall3_mansex_base"
    npc_skin_base_colour_transform()
image sb_againstwall3_mansex_shad_layer:
    "sb_againstwall3_mansex_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall3_manpoke_base_layer:
    "sb_againstwall3_manpoke_base"
    npc_skin_base_colour_transform()
image sb_againstwall3_manpoke_shad_layer:
    "sb_againstwall3_manpoke_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall3_manmast_base_layer:
    "sb_againstwall3_manmast_base"
    npc_skin_base_colour_transform()
image sb_againstwall3_manmast_shad_layer:
    "sb_againstwall3_manmast_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall3_mancum_base_layer:
    "sb_againstwall3_mancum_base"
    npc_skin_base_colour_transform()
image sb_againstwall3_mancum_shad_layer:
    "sb_againstwall3_mancum_shad"
    npc_skin_shad_colour_transform()


image sb_againstwall3_pc_hair_back_bun_2 = "sb_againstwall3_pc_hair_back_pony"
image sb_againstwall3_pc_hair_back_bun_3 = "sb_againstwall3_pc_hair_back_pony"
image sb_againstwall3_pc_hair_back_bun_4 = "sb_againstwall3_pc_hair_back_bun"
image sb_againstwall3_pc_hair_back_pony_2 = "sb_againstwall3_pc_hair_back_pony"
image sb_againstwall3_pc_hair_back_pony_3 = "sb_againstwall3_pc_hair_back_pony"
image sb_againstwall3_pc_hair_back_pony_4 = "sb_againstwall3_pc_hair_back_pony"

image sb_againstwall3_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_againstwall3_pc_hair_back")
    hair_colour_transform()

image sb_againstwall3_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_againstwall3_pc_hair_front")
    hair_colour_transform()

image sb_againstwall3_pc_writing_chest_layer:
    "sb_againstwall3_pc_writing_chest"
    writing_transform("chest")
image sb_againstwall3_pc_writing_ass_layer:
    "sb_againstwall3_pc_writing_ass"
    writing_transform("ass")
image sb_againstwall3_pc_writing_anus_layer:
    "sb_againstwall3_pc_writing_anus"
    writing_transform("anus")
image sb_againstwall3_pc_writing_face_layer:
    "sb_againstwall3_pc_writing_face"
    writing_transform("face")
image sb_againstwall3_pc_writing_forehead_layer:
    "sb_againstwall3_pc_writing_forehead"
    writing_transform("forehead")


image sb_againstwall3_pc_clothes_bimbo_layer:
    "sb_againstwall3_pc_clothes_bimbo"
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_againstwall3_pc_clothes_bimbo", "outfit")

image sb_againstwall3_pc_clothes_bimbo_preg_layer:
    "sb_againstwall3_pc_clothes_bimbo_preg"
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_againstwall3_pc_clothes_bimbo_preg", "outfit")

layeredimage sb_againstwall3_breasts_nude:

    always:
        "sb_againstwall3_pc_breasts_base_layer"
    always:
        "sb_againstwall3_pc_breasts_shad_layer"
    always:
        "sb_againstwall3_pc_breasts_nips_layer"
    if tattoo.chest:
        "sb_againstwall3_pc_breasts_tattoo_layer"
    if acc.nipring:
        "sb_againstwall3_pc_breasts_nipring_layer"

layeredimage sb_againstwall3_breasts_dress:

    always:
        "sb_againstwall3_pc_breasts_dress_base_layer"
    always:
        "sb_againstwall3_pc_breasts_dress_shad_layer"
    always:
        "sb_againstwall3_pc_breasts_dress_col_layer"
    if tattoo.chest:
        "sb_againstwall3_pc_breasts_dress_tattoo_layer"


layeredimage sb_againstwall3:

    always:
        "sb_againstwall3_bg_layer"
    group bg auto





    if c.outfit == 6 :
        "sb_againstwall3_breasts_dress"
    else:
        "sb_againstwall3_breasts_nude"


    always "sb_againstwall3_pc_base_layer"
    always "sb_againstwall3_pc_shad_layer"
    if player.pregnancy >= 2:
        "sb_againstwall3_pc_preg_layer"

    if c.outfit == 6:
        "sb_againstwall3_pc_dress"
    if c.outfit == 6 and player.pregnancy >= 2:
        "sb_againstwall3_pc_dress_preg"
    if c.outfit == 11 and player.pregnancy >= 2:
        "sb_againstwall3_pc_clothes_bimbo_preg_layer"
    elif c.outfit == 11:
        "sb_againstwall3_pc_clothes_bimbo_layer"
    always "sb_againstwall3_pc_nails_layer"
    if c.socks== 7:
        "sb_againstwall3_pc_socks"
    always "sb_againstwall3_pc_hairshad_layer"

    if skin_effect.face:
        "sb_againstwall3_pc_face_freckles_layer"
    always "sb_againstwall3_pc_face_blush_layer"
    always "sb_againstwall3_pc_spank_layer"

    if tattoo.ass:
        "sb_againstwall3_pc_tattoo_tramp"
    if writing.chest:
        "sb_againstwall3_pc_writing_chest_layer"
    if writing.ass:
        "sb_againstwall3_pc_writing_ass_layer"
    if writing.anus:
        "sb_againstwall3_pc_writing_anus_layer"
    if writing.face:
        "sb_againstwall3_pc_writing_face_layer"
    if writing.forehead:
        "sb_againstwall3_pc_writing_forehead_layer"


    group brow auto:
        attribute straight default:
            "sb_againstwall3_pc_face_brow_straight_layer"
        attribute worried:
            "sb_againstwall3_pc_face_brow_worried_layer"
        attribute angry:
            "sb_againstwall3_pc_face_brow_angry_layer"
        attribute slant:
            "sb_againstwall3_pc_face_brow_slant_layer"

    always:
        "sb_againstwall3_pc_face_eyeshadow_layer"

    group eye:
        attribute up default:
            "sb_againstwall3_pc_face_eye_iris_up_layer"
        attribute up default:
            "sb_againstwall3_pc_face_eye_eye_up"
        attribute up default:
            "sb_againstwall3_pc_face_eyeliner_up_layer"

        attribute closed :
            "sb_againstwall3_pc_face_eyeliner_closed_layer"

        attribute wink:
            "sb_againstwall3_pc_face_eye_iris_wink_layer"
        attribute wink:
            "sb_againstwall3_pc_face_eye_eye_wink"
        attribute wink:
            "sb_againstwall3_pc_face_eyeliner_wink_layer"

        attribute squint:
            "sb_againstwall3_pc_face_eye_iris_squint_layer"
        attribute squint:
            "sb_againstwall3_pc_face_eye_eye_squint"
        attribute squint:
            "sb_againstwall3_pc_face_eyeliner_squint_layer"

    group pc_face_mouth:
        attribute ag:
            "sb_againstwall3_pc_face_mouth_ag_lipstick_layer"
        attribute ag

        attribute happy:
            "sb_againstwall3_pc_face_mouth_happy_lipstick_layer"
        attribute happy

        attribute pout:
            "sb_againstwall3_pc_face_mouth_pout_lipstick_layer"
        attribute pout

        attribute neutral default:
            "sb_againstwall3_pc_face_mouth_neutral_lipstick_layer"  
        attribute neutral default

        attribute smile:
            "sb_againstwall3_pc_face_mouth_smile_lipstick_layer"
        attribute smile

        attribute grit:
            "sb_againstwall3_pc_face_mouth_grit_lipstick_layer"
        attribute grit

    if player.beingraped:
        "sb_againstwall3_pc_face_tear"

    group man:
        attribute noman default:
            null

        attribute poke:
            "sb_againstwall3_manpoke_base_layer"
        attribute poke:
            "sb_againstwall3_manpoke_shad_layer"

        attribute cum:
            "sb_againstwall3_mancum_base_layer"
        attribute cum:
            "sb_againstwall3_mancum_shad_layer"

        attribute sex:
            "sb_againstwall3_mansex_base_layer"
        attribute sex:
            "sb_againstwall3_mansex_shad_layer"

        attribute mast:
            "sb_againstwall3_manmast_base_layer"
        attribute mast:
            "sb_againstwall3_manmast_shad_layer" 

    always:
        "sb_againstwall3_pc_hair_back_layer"
    always:
        "sb_againstwall3_pc_hair_front_layer"


    always:
        "sb_againstwall3_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
