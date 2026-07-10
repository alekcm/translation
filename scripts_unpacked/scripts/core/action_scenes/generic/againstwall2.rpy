
image sb_againstwall2_bg_scene_layer:
    "sb_againstwall2_bg_" + loc_cur.loc_type


image sb_againstwall2_pc_larmwall_base_layer:
    "sb_againstwall2_pc_larmwall_base"
    skin_base_colour_transform()
image sb_againstwall2_pc_larmwall_shad_layer:
    "sb_againstwall2_pc_larmwall_shad"
    skin_shad_colour_transform()
image sb_againstwall2_pc_larmwall_nails_layer:
    "sb_againstwall2_pc_larmwall_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))

image sb_againstwall2_pc_larmmast_base_layer:
    "sb_againstwall2_pc_larmmast_base"
    skin_base_colour_transform()
image sb_againstwall2_pc_larmmast_shad_layer:
    "sb_againstwall2_pc_larmmast_shad"
    skin_shad_colour_transform()
image sb_againstwall2_pc_larmmast_arm_layer:
    "sb_againstwall2_pc_larmmast_arm"
    skin_shad_colour_transform()
image sb_againstwall2_pc_larmmast_nails_layer:
    "sb_againstwall2_pc_larmmast_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))


image sb_againstwall2_pc_headback_base_layer:
    "sb_againstwall2_pc_headback_base"
    skin_base_colour_transform()
image sb_againstwall2_pc_headback_shad_layer:
    "sb_againstwall2_pc_headback_shad"
    skin_shad_colour_transform()


image sb_againstwall2_pc_face_brow_straight_layer:
    "sb_againstwall2_pc_face_brow_straight"
    hair_colour_transform()
image sb_againstwall2_pc_face_brow_worried_layer:
    "sb_againstwall2_pc_face_brow_worried"
    hair_colour_transform()
image sb_againstwall2_pc_face_brow_angry_layer:
    "sb_againstwall2_pc_face_brow_angry"
    hair_colour_transform()

image sb_againstwall2_pc_face_mouth_ag_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_frown_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_happy_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_vhappy_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_vhappy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_neutral_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_pain_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_pain_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_shock_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_againstwall2_pc_face_mouth_tounge_lipstick_layer:
    "sb_againstwall2_pc_face_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_againstwall2_pc_face_eyeshadow_layer:
    "sb_againstwall2_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image sb_againstwall2_pc_face_eye_open_iris_layer:
    "sb_againstwall2_pc_face_eye_open_iris"
    eye_colour_transform()
image sb_againstwall2_pc_face_eye_wink_iris_layer:
    "sb_againstwall2_pc_face_eye_wink_iris"
    eye_colour_transform()

image sb_againstwall2_pc_face_eyeliner_open_layer:
    "sb_againstwall2_pc_face_eyeliner_open_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_againstwall2_pc_face_eyeliner_closed_layer:
    "sb_againstwall2_pc_face_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_againstwall2_pc_face_eyeliner_wink_layer:
    "sb_againstwall2_pc_face_eyeliner_wink_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_againstwall2_pc_face_freckles_layer:
    "sb_againstwall2_pc_face_freckles"
    skin_shad_colour_transform()
image sb_againstwall2_pc_face_blush_layer:
    "sb_againstwall2_pc_face_blush"
    blush_opacity_transform()


image sb_againstwall2_pc_hair_back_bun_2 = "sb_againstwall2_pc_hair_back_bun"
image sb_againstwall2_pc_hair_back_bun_3 = "sb_againstwall2_pc_hair_back_bun"
image sb_againstwall2_pc_hair_back_bun_4 = "sb_againstwall2_pc_hair_back_bun"
image sb_againstwall2_pc_hair_back_pony_4 = "sb_againstwall2_pc_hair_back_pony_3"

image sb_againstwall2_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_againstwall2_pc_hair_back")
    hair_colour_transform()

image sb_againstwall2_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_againstwall2_pc_hair_front")
    hair_colour_transform()


image sb_againstwall2_pc_belly_base_layer:
    get_skin_filename("sb_againstwall2_pc_belly_base", preg=True)
    skin_base_colour_transform()
image sb_againstwall2_pc_belly_shad_layer:
    get_skin_filename("sb_againstwall2_pc_belly_shad", preg=True)
    skin_shad_colour_transform()

image sb_againstwall2_pc_breasts_base_layer:
    get_skin_filename("sb_againstwall2_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_againstwall2_pc_breasts_shad_layer:
    get_skin_filename("sb_againstwall2_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()

image sb_againstwall2_pc_belly_nips_layer:
    get_skin_filename("sb_againstwall2_pc_belly_nips", breasts=True)
    nipple_colour_transform()
image sb_againstwall2_pc_belly_nipring_layer:
    get_skin_filename("sb_againstwall2_pc_belly_niprings", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_againstwall2_pc_body_base_layer:
    get_skin_filename("sb_againstwall2_pc_body_base")
    skin_base_colour_transform()
image sb_againstwall2_pc_body_shad_layer:
    get_skin_filename("sb_againstwall2_pc_body_shad")
    skin_shad_colour_transform()

image sb_againstwall2_pc_body_vag_layer:
    get_skin_filename("sb_againstwall2_pc_body_vag")
    vagina_colour_transform()
image sb_againstwall2_pc_body_nails_layer:
    "sb_againstwall2_pc_body_nails"
    accessories_primary_colour_transform("nails", If(acc.nails and acc.makeup_on, 1, 0))
image sb_againstwall2_pc_body_spank_layer:
    "sb_againstwall2_pc_body_spank"
    opacity_transform(bruise.ass)



image sb_againstwall2_man_pokevaghold_base_layer:
    "sb_againstwall2_man_pokevaghold_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_pokevaghold_shad_layer:
    "sb_againstwall2_man_pokevaghold_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall2_man_pokevaghand_base_layer:
    "sb_againstwall2_man_pokevaghand_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_pokevaghand_shad_layer:
    "sb_againstwall2_man_pokevaghand_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall2_man_pokeasshold_base_layer:
    "sb_againstwall2_man_pokeasshold_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_pokeasshold_shad_layer:
    "sb_againstwall2_man_pokeasshold_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall2_man_pokeasshand_base_layer:
    "sb_againstwall2_man_pokeasshand_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_pokeasshand_shad_layer:
    "sb_againstwall2_man_pokeasshand_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall2_man_insidevag_base_layer:
    "sb_againstwall2_man_insidevag_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_insidevag_shad_layer:
    "sb_againstwall2_man_insidevag_shad"
    npc_skin_shad_colour_transform()
image sb_againstwall2_man_insidevag_skin_layer:
    "sb_againstwall2_man_insidevag_skin"
    skin_base_colour_transform()
image sb_againstwall2_man_insidevag_vag_layer:
    "sb_againstwall2_man_insidevag_vag"
    vagina_colour_transform()

image sb_againstwall2_man_insideass_base_layer:
    "sb_againstwall2_man_insideass_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_insideass_shad_layer:
    "sb_againstwall2_man_insideass_shad"
    npc_skin_shad_colour_transform()

image sb_againstwall2_man_cum_base_layer:
    "sb_againstwall2_man_mast_base"
    npc_skin_base_colour_transform()
image sb_againstwall2_man_cum_shad_layer:
    "sb_againstwall2_man_mast_shad"
    npc_skin_shad_colour_transform()



image sb_againstwall2_pc_belly_pub_dress_layer:
    get_skin_filename("sb_againstwall2_pc_belly_pub_dress", preg=True)

image sb_againstwall2_pc_breasts_pub_dress_layer:
    get_skin_filename("sb_againstwall2_pc_breasts_pub_dress", breasts=True)
image sb_againstwall2_pc_breasts_pub_base_layer:
    get_skin_filename("sb_againstwall2_pc_breasts_pub_base", breasts=True)
    skin_base_colour_transform()
image sb_againstwall2_pc_breasts_pub_shad_layer:
    get_skin_filename("sb_againstwall2_pc_breasts_pub_shad", breasts=True)
    skin_shad_colour_transform()

image sb_againstwall2_effect_rain_loop:
    "sb_againstwall2_effect_rain1"
    .03
    "sb_againstwall2_effect_rain2"
    .03
    "sb_againstwall2_effect_rain3"
    .03
    repeat

layeredimage sb_againstwall2:

    always: 
        "sb_againstwall2_bg_scene_layer"
    group bg auto

    group larm:
        attribute wall default:
            "sb_againstwall2_pc_larmwall_base_layer" 
        attribute wall default:
            "sb_againstwall2_pc_larmwall_shad_layer"
        attribute wall default:
            "sb_againstwall2_pc_larmwall_nails_layer"

    always:
        "sb_againstwall2_pc_headback_base_layer"
    always:
        "sb_againstwall2_pc_headback_shad_layer"
    if skin_effect.face:
        "sb_againstwall2_pc_face_freckles_layer"
    always "sb_againstwall2_pc_face_blush_layer"


    if writing.face:
        "sb_againstwall2_pc_writing_cheek"
    if writing.forehead:
        "sb_againstwall2_pc_writing_forehead"
    if writing.special == "glasses":
        "sb_againstwall2_pc_writing_glasses"

    group brow auto:
        attribute straight default:
            "sb_againstwall2_pc_face_brow_straight_layer"
        attribute worried:
            "sb_againstwall2_pc_face_brow_worried_layer"
        attribute angry:
            "sb_againstwall2_pc_face_brow_angry_layer"

    always:
        "sb_againstwall2_pc_face_eyeshadow_layer"


    group eye:
        attribute open default:
            "sb_againstwall2_pc_face_eye_open_iris_layer"
        attribute open default:
            "sb_againstwall2_pc_face_eye_open_eye"
        attribute open default:
            "sb_againstwall2_pc_face_eyeliner_open_layer"

        attribute closed :
            "sb_againstwall2_pc_face_eyeliner_closed_layer"

        attribute wink :
            "sb_againstwall2_pc_face_eye_wink_iris_layer"
        attribute wink :
            "sb_againstwall2_pc_face_eye_wink_eye"
        attribute wink :
            "sb_againstwall2_pc_face_eyeliner_wink_layer"

    if player.beingraped:
        "sb_againstwall2_pc_face_eye_tear"

    always:
        "sb_againstwall2_pc_hair_back_layer"
    always:
        "sb_againstwall2_pc_hair_front_layer"

    group pc_face_mouth:
        attribute ag:
            "sb_againstwall2_pc_face_mouth_ag_lipstick_layer"
        attribute ag

        attribute frown:
            "sb_againstwall2_pc_face_mouth_frown_lipstick_layer"
        attribute frown

        attribute happy:
            "sb_againstwall2_pc_face_mouth_happy_lipstick_layer"
        attribute happy

        attribute vhappy:
            "sb_againstwall2_pc_face_mouth_vhappy_lipstick_layer"
        attribute vhappy

        attribute neutral default:
            "sb_againstwall2_pc_face_mouth_neutral_lipstick_layer"
        attribute neutral default

        attribute pain:
            "sb_againstwall2_pc_face_mouth_pain_lipstick_layer"
        attribute pain

        attribute shock:
            "sb_againstwall2_pc_face_mouth_shock_lipstick_layer"
        attribute shock

        attribute tounge:
            "sb_againstwall2_pc_face_mouth_tounge_lipstick_layer"
        attribute tounge

    group larm:

        attribute mast:
            "sb_againstwall2_pc_larmmast_arm_layer"


    always:
        "sb_againstwall2_pc_belly_base_layer"
    always:
        "sb_againstwall2_pc_belly_shad_layer"
    if c.outfit == 6:
        "sb_againstwall2_pc_belly_pub_dress_layer"

    if c.outfit == 6:
        "sb_againstwall2_pc_breasts_pub_base_layer"
    else:
        "sb_againstwall2_pc_breasts_base_layer"
    if c.outfit == 6:
        "sb_againstwall2_pc_breasts_pub_shad_layer"
    else:
        "sb_againstwall2_pc_breasts_shad_layer"
    if c.outfit == 6:
        "sb_againstwall2_pc_breasts_pub_dress_layer"



    if c.cansee_breasts:
        "sb_againstwall2_pc_belly_nips_layer"
    if acc.nipring and c.cansee_breasts:
        "sb_againstwall2_pc_belly_nipring_layer"

    always:
        "sb_againstwall2_pc_body_base_layer"
    always:
        "sb_againstwall2_pc_body_shad_layer"
    if c.outfit == 6:
        "sb_againstwall2_pc_body_pub_dress"
    if c.socks == 7:
        "sb_againstwall2_pc_body_pub_socks"

    always:
        "sb_againstwall2_pc_body_spank_layer"
    always:
        "sb_againstwall2_pc_body_vag_layer"
    always:
        "sb_againstwall2_pc_body_nails_layer"


    if writing.anus:
        "sb_againstwall2_pc_writing_anal"
    if writing.ass:
        "sb_againstwall2_pc_writing_ass"

    if player.cum_locations["cum_vagin"]:
        "sb_againstwall2_pc_cum_vagin"
    if player.cum_locations["cum_assin"]:
        "sb_againstwall2_pc_cum_assin"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "sb_againstwall2_pc_cum_assout"

    group larm:

        attribute mast:
            "sb_againstwall2_pc_larmmast_base_layer"  
        attribute mast:
            "sb_againstwall2_pc_larmmast_shad_layer"
        attribute mast:
            "sb_againstwall2_pc_larmmast_nails_layer"

    group man:
        attribute noman default:  
            null

        attribute pokevag:
            "sb_againstwall2_man_pokevaghold_base_layer"
        attribute pokevag:
            "sb_againstwall2_man_pokevaghold_shad_layer"

        attribute pokevaghand:
            "sb_againstwall2_man_pokevaghand_base_layer"
        attribute pokevaghand:
            "sb_againstwall2_man_pokevaghand_shad_layer"

        attribute pokeass:
            "sb_againstwall2_man_pokeasshold_base_layer"
        attribute pokeass:
            "sb_againstwall2_man_pokeasshold_shad_layer"

        attribute pokeasshand:
            "sb_againstwall2_man_pokeasshand_base_layer"
        attribute pokeasshand:
            "sb_againstwall2_man_pokeasshand_shad_layer"

        attribute insidevag:
            "sb_againstwall2_man_insidevag_skin_layer"
        attribute insidevag:
            "sb_againstwall2_man_insidevag_base_layer"
        attribute insidevag:
            "sb_againstwall2_man_insidevag_shad_layer"
        attribute insidevag:
            "sb_againstwall2_man_insidevag_vag_layer"

        attribute insideass:
            "sb_againstwall2_man_insideass_base_layer"
        attribute insideass:
            "sb_againstwall2_man_insideass_shad_layer"

        attribute cum:
            "sb_againstwall2_man_cum_base_layer"
        attribute cum:
            "sb_againstwall2_man_cum_shad_layer"

    group shower_:


        attribute noshower default:
            null
        attribute shower:
            null

    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_againstwall2_effect_rain_loop"
    if any(i in loc_cur.name for i in ["shower", "bathroom"]):
        "sb_againstwall2_effect_steam"

    always:
        "sb_againstwall2_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
