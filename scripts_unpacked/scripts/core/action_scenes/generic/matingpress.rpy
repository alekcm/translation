
image sb_matingpress_bg_layer:
    "sb_matingpress_bg_" + loc_cur.loc_type


image sb_matingpress_pc_head_base_layer:
    "sb_matingpress_pc_head_base"
    skin_base_colour_transform()
image sb_matingpress_pc_head_shad_layer:
    "sb_matingpress_pc_head_shad"
    skin_shad_colour_transform()


image sb_matingpress_pc_head_eyeshadow_layer:
    "sb_matingpress_pc_head_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))
image sb_matingpress_pc_head_freckles_layer:
    "sb_matingpress_pc_head_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_matingpress_pc_head_blush_layer:
    "sb_matingpress_pc_head_blush"
    blush_opacity_transform()


image sb_matingpress_pc_head_eye_up_iris_layer:
    "sb_matingpress_pc_head_eye_up_iris"
    eye_colour_transform()
image sb_matingpress_pc_head_eye_down_iris_layer:
    "sb_matingpress_pc_head_eye_down_iris"
    eye_colour_transform()
image sb_matingpress_pc_head_eye_down_eyeliner_layer:
    "sb_matingpress_pc_head_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_matingpress_pc_head_eye_up_eyeliner_layer:
    "sb_matingpress_pc_head_eye_up_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_matingpress_pc_head_brow_neutral_layer:
    "sb_matingpress_pc_head_brow_neutral"
    hair_colour_transform()
image sb_matingpress_pc_head_brow_angry_layer:
    "sb_matingpress_pc_head_brow_angry"
    hair_colour_transform()
image sb_matingpress_pc_head_brow_worried_layer:
    "sb_matingpress_pc_head_brow_worried"
    hair_colour_transform()


image sb_matingpress_pc_head_mouth_neutral_lipstick_layer:
    "sb_matingpress_pc_head_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_matingpress_pc_head_mouth_frown_lipstick_layer:
    "sb_matingpress_pc_head_mouth_frown_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_matingpress_pc_head_mouth_happy_lipstick_layer:
    "sb_matingpress_pc_head_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_matingpress_pc_head_mouth_angry_lipstick_layer:
    "sb_matingpress_pc_head_mouth_angry_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_matingpress_pc_head_mouth_oh_lipstick_layer:
    "sb_matingpress_pc_head_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_matingpress_pc_head_mouth_gag_lipstick_layer:
    "sb_matingpress_pc_head_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_matingpress_pc_head_mouth_gag_base_layer:
    "sb_matingpress_pc_head_mouth_gag_base"
    gag_colour_transform()
image sb_matingpress_pc_head_mouth_gag_metal_layer:
    "sb_matingpress_pc_head_mouth_gag_metal"
    gag_metal_transform()

image sb_matingpress_pc_head_writing_forehead_layer:
    "sb_matingpress_pc_head_writing_forehead"
    writing_transform("forehead")
image sb_matingpress_pc_head_writing_face_layer:
    "sb_matingpress_pc_head_writing_face"
    writing_transform("face")



image sb_matingpress_pc_hair_back_bun_2 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_bun_3 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_bun_4 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_pony_2 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_pony_3 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_pony_4 = "sb_matingpress_pc_hair_back_bun"
image sb_matingpress_pc_hair_back_pig_2 = "sb_matingpress_pc_hair_back_pig"
image sb_matingpress_pc_hair_back_pig_3 = "sb_matingpress_pc_hair_back_pig"
image sb_matingpress_pc_hair_back_pig_4 = "sb_matingpress_pc_hair_back_pig"
image sb_matingpress_pc_hair_back_3 = "sb_matingpress_pc_hair_back_2"
image sb_matingpress_pc_hair_back_4 = "sb_matingpress_pc_hair_back_2"

image sb_matingpress_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_matingpress_pc_hair_front")
    hair_colour_transform()
image sb_matingpress_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_matingpress_pc_hair_back")
    hair_colour_transform()


image sb_matingpress_pc_breasts_base_layer:
    get_skin_filename("sb_matingpress_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_matingpress_pc_breasts_shad_layer:
    get_skin_filename("sb_matingpress_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_matingpress_pc_breasts_nips_layer:
    get_skin_filename("sb_matingpress_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_matingpress_pc_breasts_nipring_layer:
    get_skin_filename("sb_matingpress_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")



image sb_matingpress_pc_belly_base_layer:
    "sb_matingpress_pc_belly_base"
    skin_base_colour_transform()
image sb_matingpress_pc_belly_shad_layer:
    "sb_matingpress_pc_belly_shad"
    skin_shad_colour_transform()

image sb_matingpress_pc_belly_writing_layer:
    "sb_matingpress_pc_belly_writing_" + str(player.pregnancy)
    writing_transform("belly")
image sb_matingpress_pc_belly_navring_layer:
    "sb_matingpress_pc_belly_navring"
    accessories_secondary_colour_transform("navelring")


image sb_matingpress_pc_legs_base_layer:
    "sb_matingpress_pc_legs_base"
    skin_base_colour_transform()
image sb_matingpress_pc_legs_shad_layer:
    "sb_matingpress_pc_legs_shad"
    skin_shad_colour_transform()
image sb_matingpress_pc_legs_vag_layer:
    "sb_matingpress_pc_legs_vag"
    vagina_colour_transform()
image sb_matingpress_robin_facesit_hands_vag_layer:
    "sb_matingpress_robin_facesit_hands_vag"
    vagina_colour_transform()
image sb_matingpress_dani_anal_pc_layer:
    "sb_matingpress_dani_anal_pc"
    vagina_colour_transform()

image sb_matingpress_pc_legs_spank_layer:
    "sb_matingpress_pc_legs_spank"
    opacity_transform(bruise.ass)
image sb_matingpress_pc_legs_writing_ass_layer:
    "sb_matingpress_pc_legs_writing_ass"
    writing_transform("ass")
image sb_matingpress_pc_legs_writing_anus_layer:
    "sb_matingpress_pc_legs_writing_anus"
    writing_transform("anus")


image sb_matingpress_pc_hands_base_layer:
    "sb_matingpress_pc_hands_base"
    skin_base_colour_transform()
image sb_matingpress_pc_hands_shad_layer:
    "sb_matingpress_pc_hands_shad"
    skin_shad_colour_transform()


image sb_matingpress_man_vag_base_layer:
    "sb_matingpress_man_vag_base"
    npc_skin_base_colour_transform()
image sb_matingpress_man_vag_shad_layer:
    "sb_matingpress_man_vag_shad"
    npc_skin_shad_colour_transform()
image sb_matingpress_man_vag_pc_base_layer:
    "sb_matingpress_man_vag_pc_base"
    skin_base_colour_transform()

image sb_matingpress_man_anal_base_layer:
    "sb_matingpress_man_anal_base"
    npc_skin_base_colour_transform()
image sb_matingpress_man_anal_shad_layer:
    "sb_matingpress_man_anal_shad"
    npc_skin_shad_colour_transform()

image sb_matingpress_man_poke_base_layer:
    "sb_matingpress_man_poke_base"
    npc_skin_base_colour_transform()
image sb_matingpress_man_poke_shad_layer:
    "sb_matingpress_man_poke_shad"
    npc_skin_shad_colour_transform()

image sb_matingpress = LayeredImageProxy("sb_matingpress_layered", Transform(xalign = (0.9)))

layeredimage sb_matingpress_layered:

    always "sb_matingpress_bg_layer"

    always "sb_matingpress_pc_head_base_layer"
    always "sb_matingpress_pc_head_shad_layer"

    always "sb_matingpress_pc_head_eyeshadow_layer"
    always "sb_matingpress_pc_head_freckles_layer"
    always "sb_matingpress_pc_head_blush_layer"

    group face:
        attribute neutral "sb_matingpress_pc_head_mouth_neutral_lipstick_layer" default
        attribute neutral "sb_matingpress_pc_head_mouth_neutral" default
        attribute neutral "sb_matingpress_pc_head_brow_neutral_layer" default

        attribute oh "sb_matingpress_pc_head_mouth_oh_lipstick_layer"
        attribute oh "sb_matingpress_pc_head_mouth_oh"
        attribute oh "sb_matingpress_pc_head_brow_neutral_layer"

        attribute angry "sb_matingpress_pc_head_mouth_angry_lipstick_layer"
        attribute angry "sb_matingpress_pc_head_mouth_angry"
        attribute angry "sb_matingpress_pc_head_brow_angry_layer"

        attribute frown "sb_matingpress_pc_head_mouth_frown_lipstick_layer"
        attribute frown "sb_matingpress_pc_head_mouth_frown"
        attribute frown "sb_matingpress_pc_head_brow_worried_layer"

        attribute happy "sb_matingpress_pc_head_mouth_happy_lipstick_layer"
        attribute happy "sb_matingpress_pc_head_mouth_happy"
        attribute happy "sb_matingpress_pc_head_brow_neutral_layer"

    group eyes:
        attribute up "sb_matingpress_pc_head_eye_up_iris_layer" default
        attribute up "sb_matingpress_pc_head_eye_up_eye" default
        attribute up "sb_matingpress_pc_head_eye_up_eyeliner_layer" default

        attribute down "sb_matingpress_pc_head_eye_down_iris_layer"
        attribute down "sb_matingpress_pc_head_eye_down_eye"
        attribute down "sb_matingpress_pc_head_eye_down_eyeliner_layer"

    if writing.forehead:
        "sb_matingpress_pc_head_writing_forehead_layer"
    if writing.face:
        "sb_matingpress_pc_head_writing_face_layer"
    if player.cum_locations["cum_face"]:
        "sb_matingpress_pc_head_cum"
    if player.gagged:
        "sb_matingpress_gag_layered"

    always "sb_matingpress_pc_hair_back_layer"
    always "sb_matingpress_pc_hair_front_layer"

    group dani:
        attribute no_dani null default

        attribute dani_sit "sb_matingpress_dani_facesit"

        attribute dani_sit_strap "sb_matingpress_dani_facesit_strap"

    group robin:
        attribute no_robin null default

        attribute robin_sit "sb_matingpress_robin_facesit"

    always "sb_matingpress_pc_breasts_base_layer"
    always "sb_matingpress_pc_breasts_shad_layer"
    always "sb_matingpress_pc_breasts_nips_layer"
    if acc.nipring:
        "sb_matingpress_pc_breasts_nipring_layer"

    if player.showing:
        "sb_matingpress_belly_layered"

    group dani:
        attribute no_dani null default

        attribute dani_69 "sb_matingpress_dani_69_body"
    group robin:
        attribute no_robin null default

        attribute robin_69 "sb_matingpress_robin_69_body"

    always "sb_matingpress_pc_legs_base_layer"
    always "sb_matingpress_pc_legs_shad_layer"
    always "sb_matingpress_pc_legs_vag_layer"

    always "sb_matingpress_pc_legs_spank_layer"
    if writing.ass:
        "sb_matingpress_pc_legs_writing_ass_layer"
    if writing.anus:
        "sb_matingpress_pc_legs_writing_anus_layer"

    if player.cum_locations["cum_assin"]:
        "sb_matingpress_pc_legs_cum_ass"
    if player.cum_locations["cum_vagin"]:
        "sb_matingpress_pc_legs_cum_vag"
    if player.cum_locations["cum_vagout"]:
        "sb_matingpress_pc_legs_cum_vagout"
    if player.cum_locations["cum_assout"]:
        "sb_matingpress_pc_legs_cum_assout"

    if acc.anus:
        "sb_matingpress_pc_legs_plug"

    group hands:
        attribute no_hands null 

        attribute hands "sb_matingpress_pc_hands_base_layer" default
        attribute hands "sb_matingpress_pc_hands_shad_layer" default

    group robin:
        attribute no_robin null default

        attribute robin_sit if_not ["vag", "anal", "poke"] "sb_matingpress_robin_facesit_hands_vag_layer"
        attribute robin_sit if_not ["vag", "anal", "poke"] "sb_matingpress_robin_facesit_hands"

        attribute robin_69 "sb_matingpress_robin_69_head"

        attribute robin_lick "sb_matingpress_robin_lick"

    group dani:
        attribute no_dani null default

        attribute dani_sit "sb_matingpress_robin_facesit_hands_vag_layer"
        attribute dani_sit "sb_matingpress_dani_facesit_hands"


        attribute dani_69 "sb_matingpress_dani_69_head"

        attribute dani_lick "sb_matingpress_dani_lick"

        attribute dani_poke "sb_matingpress_dani_poke"

        attribute dani_vag "sb_matingpress_dani_vag"

        attribute dani_anal "sb_matingpress_dani_anal"
        attribute dani_anal "sb_matingpress_dani_anal_pc_layer"



    group man:
        attribute noman null default

        attribute vag "sb_matingpress_man_vag_pc_base_layer"
        attribute vag "sb_matingpress_man_vag_base_layer"
        attribute vag "sb_matingpress_man_vag_shad_layer"

        attribute anal "sb_matingpress_man_anal_base_layer"
        attribute anal "sb_matingpress_man_anal_shad_layer"

        attribute poke "sb_matingpress_man_poke_base_layer"
        attribute poke "sb_matingpress_man_poke_shad_layer"



    always "sb_matingpress_frame"

layeredimage sb_matingpress_gag_layered:
    always "sb_matingpress_pc_head_mouth_gag_lipstick_layer"
    always "sb_matingpress_pc_head_mouth_gag_base_layer"
    always "sb_matingpress_pc_head_mouth_gag_metal_layer"

layeredimage sb_matingpress_belly_layered:
    always "sb_matingpress_pc_belly_base_layer"
    always "sb_matingpress_pc_belly_shad_layer" 
    if writing.belly and player.pregnancy >= 2:
        "sb_matingpress_pc_belly_writing_layer"
    if acc.navelring:
        "sb_matingpress_pc_belly_navring_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
