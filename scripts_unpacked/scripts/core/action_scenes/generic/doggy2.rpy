

image sb_doggy2_bg_layer:
    "sb_doggy2_bg_" + loc_cur.loc_type





image sb_doggy2_manblow_body_base_layer:
    "sb_doggy2_manblow_body_base"
    npc2_skin_base_colour_transform()
image sb_doggy2_manblow_body_shad_layer:
    "sb_doggy2_manblow_body_shad"
    npc2_skin_shad_colour_transform()



image sb_doggy2_pc_body_base_layer:
    "sb_doggy2_pc_body_base"
    skin_base_colour_transform()
image sb_doggy2_pc_body_shad_layer:
    "sb_doggy2_pc_body_shad"
    skin_shad_colour_transform()
image sb_doggy2_pc_body_vag_layer:
    "sb_doggy2_pc_body_vag"
    vagina_colour_transform()

image sb_doggy2_pc_breasts_base_layer:
    get_skin_filename("sb_doggy2_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_doggy2_pc_breasts_shad_layer:
    get_skin_filename("sb_doggy2_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_doggy2_pc_breasts_back_layer:
    get_skin_filename("sb_doggy2_pc_breasts_back", breasts=True)
    skin_shad_colour_transform()
image sb_doggy2_pc_breasts_nips_layer:
    get_skin_filename("sb_doggy2_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_doggy2_pc_breasts_nipring_layer:
    get_skin_filename("sb_doggy2_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_doggy2_pc_belly_base_layer:
    get_skin_filename("sb_doggy2_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_doggy2_pc_belly_shad_layer:
    get_skin_filename("sb_doggy2_pc_belly_shad", preg=True)
    skin_shad_colour_transform()

image sb_doggy2_pc_body_spank_layer:
    "sb_doggy2_pc_body_spank"
    opacity_transform(bruise.ass)



image sb_doggy2_pc_headback_base_layer:
    "sb_doggy2_pc_headback_base"
    skin_base_colour_transform()
image sb_doggy2_pc_headback_shad_layer:
    "sb_doggy2_pc_headback_shad"
    skin_shad_colour_transform()
image sb_doggy2_pc_headback_face_freckles_layer:
    "sb_doggy2_pc_headback_face_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_doggy2_pc_headback_face_blush_layer:
    "sb_doggy2_pc_headback_face_blush"
    blush_opacity_transform()

image sb_doggy2_pc_headback_hair_back_bun_2 = "sb_doggy2_pc_headback_hair_back_bun"
image sb_doggy2_pc_headback_hair_back_bun_3 = "sb_doggy2_pc_headback_hair_back_bun"
image sb_doggy2_pc_headback_hair_back_bun_4 = "sb_doggy2_pc_headback_hair_back_bun"
image sb_doggy2_pc_headback_hair_back_pony_4 = "sb_doggy2_pc_headback_hair_back_pony_3"

image sb_doggy2_pc_headback_hair_back_layer:
    get_hair_back_cg_filename("sb_doggy2_pc_headback_hair_back")
    hair_colour_transform()
image sb_doggy2_pc_headback_hair_front_layer:
    get_hair_front_cg_filename("sb_doggy2_pc_headback_hair_front")
    hair_colour_transform()

image sb_doggy2_pc_headback_face_eyeshadow_layer:
    "sb_doggy2_pc_headback_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))

image sb_doggy2_pc_headback_face_mouth_frown_lipstick_layer:
    "sb_doggy2_pc_headback_face_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_doggy2_pc_headback_face_mouth_frown_layer:
    "sb_doggy2_pc_headback_face_mouth_frown"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_doggy2_pc_headback_face_mouth_neutral_lipstick_layer:
    "sb_doggy2_pc_headback_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_doggy2_pc_headback_face_mouth_neutral_layer:
    "sb_doggy2_pc_headback_face_mouth_neutral"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_doggy2_pc_headback_face_mouth_happy_lipstick_layer:
    "sb_doggy2_pc_headback_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_doggy2_pc_headback_face_mouth_happy_layer:
    "sb_doggy2_pc_headback_face_mouth_happy"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_doggy2_pc_headback_face_mouth_shock_lipstick_layer:
    "sb_doggy2_pc_headback_face_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_doggy2_pc_headback_face_mouth_shock_layer:
    "sb_doggy2_pc_headback_face_mouth_shock"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))
image sb_doggy2_pc_headback_face_mouth_gag_lipstick_layer:
    "sb_doggy2_pc_headback_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_doggy2_pc_headback_face_mouth_gag_base_layer:
    "sb_doggy2_pc_headback_face_mouth_gag_base"
    gag_colour_transform()
image sb_doggy2_pc_headback_face_mouth_gag_metal_layer:
    "sb_doggy2_pc_headback_face_mouth_gag_metal"
    gag_metal_transform()

image sb_doggy2_pc_headforward_face_mouth_gag_base_layer:
    "sb_doggy2_pc_headforward_face_mouth_gag_base"
    gag_colour_transform()
image sb_doggy2_pc_headforward_face_mouth_gag_metal_layer:
    "sb_doggy2_pc_headforward_face_mouth_gag_metal"
    gag_metal_transform()

image sb_doggy2_pc_headback_face_eye_iris_normal_layer:
    "sb_doggy2_pc_headback_face_eye_iris_normal"
    eye_colour_transform()
image sb_doggy2_pc_headback_face_eye_iris_wink_layer:
    "sb_doggy2_pc_headback_face_eye_iris_wink"
    eye_colour_transform()
image sb_doggy2_pc_headback_face_eye_iris_squint_layer:
    "sb_doggy2_pc_headback_face_eye_iris_angry"
    eye_colour_transform()

image sb_doggy2_pc_headback_face_eye_eye_squint = "sb_doggy2_pc_headback_face_eye_eye_angry"

image sb_doggy2_pc_headback_face_eyeliner_normal_layer:
    "sb_doggy2_pc_headback_face_eyeliner_normal_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_doggy2_pc_headback_face_eyeliner_wink_layer:
    "sb_doggy2_pc_headback_face_eyeliner_wink_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_doggy2_pc_headback_face_eyeliner_squint_layer:
    "sb_doggy2_pc_headback_face_eyeliner_angry_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_doggy2_pc_headback_face_eyeliner_closed_layer:
    "sb_doggy2_pc_headback_face_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_doggy2_pc_headback_face_brow_straight_layer:
    "sb_doggy2_pc_headback_face_brow_straight"
    hair_colour_transform()
image sb_doggy2_pc_headback_face_brow_worried_layer:
    "sb_doggy2_pc_headback_face_brow_worried"
    hair_colour_transform()
image sb_doggy2_pc_headback_face_brow_slant_layer:
    "sb_doggy2_pc_headback_face_brow_slant"
    hair_colour_transform()
image sb_doggy2_pc_headback_face_brow_angry_layer:
    "sb_doggy2_pc_headback_face_brow_angry"
    hair_colour_transform()



image sb_doggy2_pc_headforward_base_layer:
    "sb_doggy2_pc_headforward_base"
    skin_base_colour_transform()
image sb_doggy2_pc_headforward_shad_layer:
    "sb_doggy2_pc_headforward_shad"
    skin_shad_colour_transform()

image sb_doggy2_pc_headforward_hair_back_bun_2 = "sb_doggy2_pc_headforward_hair_back_bun"
image sb_doggy2_pc_headforward_hair_back_bun_3 = "sb_doggy2_pc_headforward_hair_back_bun"
image sb_doggy2_pc_headforward_hair_back_bun_4 = "sb_doggy2_pc_headforward_hair_back_bun"
image sb_doggy2_pc_headforward_hair_back_pony_4 = "sb_doggy2_pc_headforward_hair_back_pony_3"

image sb_doggy2_pc_headforward_hair_back_layer:
    get_hair_back_cg_filename("sb_doggy2_pc_headforward_hair_back")
    hair_colour_transform()
image sb_doggy2_pc_headforward_hair_front_layer:
    get_hair_front_cg_filename("sb_doggy2_pc_headforward_hair_front")
    hair_colour_transform()



image sb_doggy2_pc_clothes_bimbo_layer:
    "sb_doggy2_pc_clothes_bimbo_" + str(player.pregnancy)
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_doggy2_pc_clothes_bimbo_" + str(player.pregnancy), "outfit")

image sb_doggy2_pc_outfit_maid_breasts_base_layer:
    get_skin_filename("sb_doggy2_pc_outfit_maid_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_doggy2_pc_outfit_maid_breasts_shad_layer:
    get_skin_filename("sb_doggy2_pc_outfit_maid_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_doggy2_pc_outfit_maid_breasts_col_layer:
    get_skin_filename("sb_doggy2_pc_outfit_maid_breasts_col", breasts=True)
image sb_doggy2_pc_outfit_maid_belly_layer:
    get_skin_filename("sb_doggy2_pc_outfit_maid_belly", preg=True)

image sb_doggy2_pc_outfit_pub_breasts_base_layer:
    get_skin_filename("sb_doggy2_pc_outfit_pub_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_doggy2_pc_outfit_pub_breasts_shad_layer:
    get_skin_filename("sb_doggy2_pc_outfit_pub_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_doggy2_pc_outfit_pub_breasts_col_layer:
    get_skin_filename("sb_doggy2_pc_outfit_pub_breasts_col", breasts=True)
image sb_doggy2_pc_outfit_pub_belly_layer:
    get_skin_filename("sb_doggy2_pc_outfit_pub_belly", preg=True)

image sb_doggy2_pc_outfit_dungarees_breasts_col_layer:
    get_skin_filename("sb_doggy2_pc_outfit_dungarees_breasts_col", breasts=True)
image sb_doggy2_pc_outfit_dungarees_belly_layer:
    get_skin_filename("sb_doggy2_pc_outfit_dungarees_belly", preg=True)


image sb_doggy2_mancum_base_layer:
    "sb_doggy2_mancum_base"
    npc_skin_base_colour_transform()
image sb_doggy2_mancum_shad_layer:
    "sb_doggy2_mancum_shad"
    npc_skin_shad_colour_transform()

image sb_doggy2_manpoke_body_base_layer:
    "sb_doggy2_manpoke_body_base"
    npc_skin_base_colour_transform()
image sb_doggy2_manpoke_body_shad_layer:
    "sb_doggy2_manpoke_body_shad"
    npc_skin_shad_colour_transform()
image sb_doggy2_manpoke_ass_base_layer:
    "sb_doggy2_manpoke_ass_base"
    npc_skin_base_colour_transform()
image sb_doggy2_manpoke_ass_shad_layer:
    "sb_doggy2_manpoke_ass_shad"
    npc_skin_shad_colour_transform()
image sb_doggy2_manpoke_asshold_base_layer:
    "sb_doggy2_manpoke_asshold_base"
    npc_skin_base_colour_transform()
image sb_doggy2_manpoke_asshold_shad_layer:
    "sb_doggy2_manpoke_asshold_shad"
    npc_skin_shad_colour_transform()
image sb_doggy2_manpoke_vag_base_layer:
    "sb_doggy2_manpoke_vag_base"
    npc_skin_base_colour_transform()
image sb_doggy2_manpoke_vag_shad_layer:
    "sb_doggy2_manpoke_vag_shad"
    npc_skin_shad_colour_transform()
image sb_doggy2_manpoke_vaghold_base_layer:
    "sb_doggy2_manpoke_vaghold_base"
    npc_skin_base_colour_transform()
image sb_doggy2_manpoke_vaghold_shad_layer:
    "sb_doggy2_manpoke_vaghold_shad"
    npc_skin_shad_colour_transform()

image sb_doggy2_mansex_body_base_layer:
    "sb_doggy2_mansex_body_base"
    npc_skin_base_colour_transform()
image sb_doggy2_mansex_body_shad_layer:
    "sb_doggy2_mansex_body_shad"
    npc_skin_shad_colour_transform()

image sb_doggy2_mansex_anal_base_layer:
    "sb_doggy2_mansex_anal_base"
    npc_skin_base_colour_transform()
image sb_doggy2_mansex_anal_shad_layer:
    "sb_doggy2_mansex_anal_shad"
    npc_skin_shad_colour_transform()

image sb_doggy2_mansex_vag_base_layer:
    "sb_doggy2_mansex_vag_base"
    npc_skin_base_colour_transform()
image sb_doggy2_mansex_vag_vag_layer:
    "sb_doggy2_mansex_vag_vag"
    vagina_colour_transform()

image sb_doggy2_manblow_hand_base_layer:
    "sb_doggy2_manblow_hand_base"
    npc2_skin_base_colour_transform()
image sb_doggy2_manblow_hand_shad_layer:
    "sb_doggy2_manblow_hand_shad"
    npc2_skin_shad_colour_transform()
image sb_doggy2_manblow_hand_hair_layer:
    "sb_doggy2_manblow_hand_hair"
    hair_colour_transform()

image sb_doggy2 = LayeredImageProxy("sb_doggy2_layered", Transform(xalign = (0.80)))

layeredimage sb_doggy2_layered:

    always "sb_doggy2_bg_layer"

    group man_front:
        attribute no_blow default null
        attribute blow "sb_doggy2_manblow_body_base_layer"
        attribute blow "sb_doggy2_manblow_body_shad_layer"

    always "sb_doggy2_pc_body_base_layer"
    always "sb_doggy2_pc_body_shad_layer"
    always "sb_doggy2_pc_body_spank_layer"
    if tattoo.ass:
        "sb_doggy2_pc_body_tattoo_tramp"

    if player.breasts > 1 and not c.outfit in (6,19,20):
        "sb_doggy2_pc_breasts_back_layer"
    always "sb_doggy2_pc_belly_base_layer"
    always "sb_doggy2_pc_belly_shad_layer"

    if not c.outfit in (6,19,20):
        "sb_doggy2_pc_breasts_base_layer"
    if not c.outfit in (6,19,20):
        "sb_doggy2_pc_breasts_shad_layer"
    if not c.outfit in (6,19,20):
        "sb_doggy2_pc_breasts_nips_layer"
    if acc.nipring and not c.outfit in (6,19,20):
        "sb_doggy2_pc_breasts_nipring_layer"

    if writing.ass:
        "sb_doggy2_pc_body_writing_ass"
    if writing.anus:
        "sb_doggy2_pc_body_writing_anus"

    if player.cum_locations["cum_assin"]:
        "sb_doggy2_pc_body_cum_anus"
    if player.cum_locations["cum_vagin"]:
        "sb_doggy2_pc_body_cum_vag"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "sb_doggy2_pc_body_cum_ass"

    group head:
        attribute head_back default "sb_doggy2_pc_headback_base_layer"
        attribute head_back default "sb_doggy2_pc_headback_shad_layer"
        attribute head_back default "sb_doggy2_pc_headback_hair_back_layer"
        attribute head_back default "sb_doggy2_pc_headback_face_freckles_layer"
        attribute head_back default "sb_doggy2_pc_headback_face_blush_layer"

        attribute head_forward "sb_doggy2_pc_headforward_base_layer"
        attribute head_forward "sb_doggy2_pc_headforward_shad_layer"

    group head:
        attribute head_forward "sb_doggy2_pc_headforward_hair_back_layer"
        attribute head_forward "sb_doggy2_pc_headforward_hair_front_layer"

    if writing.forehead:
        if_any "head_back" "sb_doggy2_pc_headback_writing_forehead"
    if writing.face:
        if_any "head_back" "sb_doggy2_pc_headback_writing_face"

    if player.cum_locations["cum_face"]:
        if_any "head_back" "sb_doggy2_pc_headback_cum_face"
    if player.cum_locations["cum_mouth"]:
        if_any "head_back" "sb_doggy2_pc_headback_cum_mouth"

    group pc_headback_face_mouth if_any "head_back":
        attribute frown "sb_doggy2_pc_headback_face_mouth_frown_lipstick_layer"
        attribute frown "sb_doggy2_pc_headback_face_mouth_frown_layer"

        attribute neutral default "sb_doggy2_pc_headback_face_mouth_neutral_lipstick_layer"
        attribute neutral default "sb_doggy2_pc_headback_face_mouth_neutral_layer"

        attribute happy "sb_doggy2_pc_headback_face_mouth_happy_lipstick_layer"
        attribute happy "sb_doggy2_pc_headback_face_mouth_happy_layer"

        attribute shock "sb_doggy2_pc_headback_face_mouth_shock_lipstick_layer"
        attribute shock "sb_doggy2_pc_headback_face_mouth_shock_layer"

    always:
        if_any "head_back" "sb_doggy2_pc_headback_face_eyeshadow_layer"

    group pc_headback_face_eye_eye if_any "head_back":
        attribute normal default "sb_doggy2_pc_headback_face_eye_iris_normal_layer"
        attribute normal default "sb_doggy2_pc_headback_face_eye_eye_normal"
        attribute normal default "sb_doggy2_pc_headback_face_eyeliner_normal_layer"

        attribute wink "sb_doggy2_pc_headback_face_eye_iris_wink_layer"
        attribute wink "sb_doggy2_pc_headback_face_eye_eye_wink"
        attribute wink "sb_doggy2_pc_headback_face_eyeliner_wink_layer"

        attribute squint "sb_doggy2_pc_headback_face_eye_iris_squint_layer"
        attribute squint "sb_doggy2_pc_headback_face_eye_eye_squint"
        attribute squint "sb_doggy2_pc_headback_face_eyeliner_squint_layer"

        attribute closed "sb_doggy2_pc_headback_face_eyeliner_closed_layer"

    group brow if_any "head_back":
        attribute straight default "sb_doggy2_pc_headback_face_brow_straight_layer"
        attribute worried "sb_doggy2_pc_headback_face_brow_worried_layer"
        attribute slant "sb_doggy2_pc_headback_face_brow_slant_layer"
        attribute angry "sb_doggy2_pc_headback_face_brow_angry_layer"

    if player.gagged:
        if_any "head_back" "sb_doggy2_headback_gag"
    if player.gagged:
        if_any "head_forward" "sb_doggy2_headforward_gag"

    group head:
        attribute head_back default "sb_doggy2_pc_headback_hair_front_layer"

    if c.outfit == 6:
        "sb_doggy2_outfit_pub"
    elif c.outfit == 11:
        "sb_doggy2_pc_clothes_bimbo_layer"
    elif c.outfit == 19:
        "sb_doggy2_outfit_dungarees"
    elif c.outfit == 20:
        "sb_doggy2_outfit_maid"

    group man_behind:
        attribute noman default null

        attribute cum "sb_doggy2_mancum_base_layer"  
        attribute cum "sb_doggy2_mancum_shad_layer"

        attribute pokevag "sb_doggy2_manpoke_vag_base_layer"
        attribute pokevag "sb_doggy2_manpoke_vag_shad_layer"
        attribute pokevag "sb_doggy2_manpoke_body_base_layer"
        attribute pokevag "sb_doggy2_manpoke_body_shad_layer"

        attribute pokeass "sb_doggy2_manpoke_ass_base_layer"
        attribute pokeass "sb_doggy2_manpoke_ass_shad_layer"
        attribute pokeass "sb_doggy2_manpoke_body_base_layer"
        attribute pokeass "sb_doggy2_manpoke_body_shad_layer"

        attribute pokevaghold "sb_doggy2_manpoke_vaghold_base_layer"
        attribute pokevaghold "sb_doggy2_manpoke_vaghold_shad_layer"
        attribute pokevaghold "sb_doggy2_manpoke_body_base_layer"
        attribute pokevaghold "sb_doggy2_manpoke_body_shad_layer"

        attribute pokeasshold "sb_doggy2_manpoke_asshold_base_layer"
        attribute pokeasshold "sb_doggy2_manpoke_asshold_shad_layer"
        attribute pokeasshold "sb_doggy2_manpoke_body_base_layer"
        attribute pokeasshold "sb_doggy2_manpoke_body_shad_layer"

        attribute insidevag "sb_doggy2_mansex_vag_base_layer"
        attribute insidevag "sb_doggy2_mansex_vag_vag_layer"
        attribute insidevag "sb_doggy2_mansex_body_base_layer"
        attribute insidevag "sb_doggy2_mansex_body_shad_layer"

        attribute insideass "sb_doggy2_mansex_anal_base_layer"
        attribute insideass "sb_doggy2_mansex_anal_shad_layer"
        attribute insideass "sb_doggy2_mansex_body_base_layer"
        attribute insideass "sb_doggy2_mansex_body_shad_layer"

    group handhair:
        attribute nohand default null

        attribute pullhair "sb_doggy2_manblow_hand_base_layer"
        attribute pullhair "sb_doggy2_manblow_hand_shad_layer"
        attribute pullhair "sb_doggy2_manblow_hand_hair_layer"

    always "sb_doggy2_frame"

layeredimage sb_doggy2_outfit_maid:
    if c.socks:
        "sb_doggy2_pc_outfit_maid_socks"
    if c.pants:
        "sb_doggy2_pc_outfit_maid_pants"
    always "sb_doggy2_pc_outfit_maid_breasts_shad_layer"
    always "sb_doggy2_pc_outfit_maid_breasts_base_layer"
    always "sb_doggy2_pc_outfit_maid_breasts_col_layer"
    always "sb_doggy2_pc_outfit_maid_belly_layer"
    always "sb_doggy2_pc_outfit_maid_body"

layeredimage sb_doggy2_outfit_dungarees:
    always "sb_doggy2_pc_outfit_dungarees_breasts_col_layer"
    always "sb_doggy2_pc_outfit_dungarees_belly_layer"
    always "sb_doggy2_pc_outfit_dungarees_body"

layeredimage sb_doggy2_outfit_pub:
    if c.socks:
        "sb_doggy2_pc_outfit_pub_socks"
    if c.pants:
        "sb_doggy2_pc_outfit_pub_pants"

    always "sb_doggy2_pc_outfit_pub_breasts_base_layer"
    always "sb_doggy2_pc_outfit_pub_breasts_shad_layer"
    always "sb_doggy2_pc_outfit_pub_breasts_col_layer"
    always "sb_doggy2_pc_outfit_pub_belly_layer"
    always "sb_doggy2_pc_outfit_pub_body"

layeredimage sb_doggy2_headback_gag:
    always "sb_doggy2_pc_headback_face_mouth_gag_lipstick_layer"
    always "sb_doggy2_pc_headback_face_mouth_gag_base_layer"
    always "sb_doggy2_pc_headback_face_mouth_gag_metal_layer"
layeredimage sb_doggy2_headforward_gag:
    always "sb_doggy2_pc_headforward_face_mouth_gag_base_layer"
    always "sb_doggy2_pc_headforward_face_mouth_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
