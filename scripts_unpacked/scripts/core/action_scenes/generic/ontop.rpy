

image sb_ontop_bg_layer:
    "sb_ontop_bg_" + loc_cur.loc_type


image sb_ontop_pc_body_base_layer:
    "sb_ontop_pc_body_base"
    skin_base_colour_transform()
image sb_ontop_pc_body_shad_layer:
    "sb_ontop_pc_body_shad"
    skin_shad_colour_transform()

image sb_ontop_pc_body_belly_base_layer:
    "sb_ontop_pc_belly_base"
    skin_base_colour_transform()
image sb_ontop_pc_body_belly_shad_layer:
    "sb_ontop_pc_belly_shad"
    skin_shad_colour_transform()

image sb_ontop_pc_breasts_base_layer:
    get_skin_filename("sb_ontop_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_ontop_pc_breasts_shad_layer:
    get_skin_filename("sb_ontop_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_ontop_pc_breasts_nips_layer:
    get_skin_filename("sb_ontop_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_ontop_pc_breasts_nipring_layer:
    get_skin_filename("sb_ontop_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_ontop_pc_breasts_tattoo_layer:
    get_skin_filename("sb_ontop_pc_breasts_tattoo", breasts=True)

image sb_ontop_pc_breasts_c_base_layer:
    get_skin_filename("sb_ontop_pc_breasts_c_base", breasts=True)
    skin_base_colour_transform()
image sb_ontop_pc_breasts_c_shad_layer:
    get_skin_filename("sb_ontop_pc_breasts_c_shad", breasts=True)
    skin_shad_colour_transform()
image sb_ontop_pc_breasts_c_nips_layer:
    get_skin_filename("sb_ontop_pc_breasts_c_nips", breasts=True)
    nipple_colour_transform()
image sb_ontop_pc_breasts_tattoo_c_layer:
    get_skin_filename("sb_ontop_pc_breasts_c_tattoo", breasts=True)

image sb_ontop_pc_clothes_maid_breasts_layer:
    get_skin_filename("sb_ontop_pc_clothes_maid_breasts", breasts=True)
image sb_ontop_pc_clothes_pub_breasts_layer:
    get_skin_filename("sb_ontop_pc_clothes_pub_breasts", breasts=True)

image sb_ontop_pc_writing_chest_layer:
    "sb_ontop_pc_writing_chest"
    writing_transform("chest")



image sb_ontop_pc_face_freckles_layer:
    "sb_ontop_pc_face_freckles"
    skin_shad_colour_transform()

image sb_ontop_pc_face_eyeliner_back_layer:
    "sb_ontop_pc_face_eyeliner_back_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_ontop_pc_face_eyeliner_up_layer:
    "sb_ontop_pc_face_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_ontop_pc_face_eyeliner_down_layer:
    "sb_ontop_pc_face_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_ontop_pc_face_iris_back_layer:
    "sb_ontop_pc_face_iris_back"
    eye_colour_transform()
image sb_ontop_pc_face_iris_up_layer:
    "sb_ontop_pc_face_iris_up"
    eye_colour_transform()
image sb_ontop_pc_face_iris_down_layer:
    "sb_ontop_pc_face_iris_down"
    eye_colour_transform()

image sb_ontop_pc_face_brow_worried_layer:
    "sb_ontop_pc_face_brow_worried"
    hair_colour_transform()

image sb_ontop_pc_face_mouth_happy_lipstick_layer:
    "sb_ontop_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_happy_layer:
    "sb_ontop_pc_face_mouth_happy"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_ontop_pc_face_mouth_surprise_lipstick_layer:
    "sb_ontop_pc_face_mouth_surprised_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_surprise_layer:
    "sb_ontop_pc_face_mouth_surprised"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_ontop_pc_face_mouth_shock_lipstick_layer:
    "sb_ontop_pc_face_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_shock_layer:
    "sb_ontop_pc_face_mouth_shock"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_ontop_pc_face_mouth_grit_lipstick_layer:
    "sb_ontop_pc_face_mouth_grit_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_grit_layer:
    "sb_ontop_pc_face_mouth_grit"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_ontop_pc_face_mouth_ag_lipstick_layer:
    "sb_ontop_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_ag_layer:
    "sb_ontop_pc_face_mouth_ag"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_ontop_pc_face_mouth_blow_lipstick_layer:
    "sb_ontop_pc_face_mouth_blow_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_ontop_pc_face_mouth_gag_lipstick_layer:
    "sb_ontop_pc_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_ontop_pc_face_mouth_gag_base_layer:
    "sb_ontop_pc_face_mouth_gag_base"
    gag_colour_transform()
image sb_ontop_pc_face_mouth_gag_metal_layer:
    "sb_ontop_pc_face_mouth_gag_metal"
    gag_metal_transform()

image sb_ontop_pc_face_eyeshadow_layer:
    "sb_ontop_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))
image sb_ontop_pc_face_blush_layer:
    "sb_ontop_pc_face_blush"
    blush_opacity_transform()

image sb_ontop_pc_face_brow_happy_layer:
    "sb_ontop_pc_face_brow_happy"
    hair_colour_transform()
image sb_ontop_pc_face_brow_worried_layer:
    "sb_ontop_pc_face_brow_worried"
    hair_colour_transform()
image sb_ontop_pc_face_brow_straight_layer:
    "sb_ontop_pc_face_brow_straight"
    hair_colour_transform()
image sb_ontop_pc_face_brow_angry_layer:
    "sb_ontop_pc_face_brow_angry"
    hair_colour_transform()


image sb_ontop_pc_hair_back_bun_2 = "sb_ontop_pc_hair_back_bun"
image sb_ontop_pc_hair_back_bun_3 = "sb_ontop_pc_hair_back_bun"
image sb_ontop_pc_hair_back_bun_4 = "sb_ontop_pc_hair_back_bun"
image sb_ontop_pc_hair_back_pony_2 = "sb_ontop_pc_hair_back_pony"
image sb_ontop_pc_hair_back_pony_3 = "sb_ontop_pc_hair_back_pony"
image sb_ontop_pc_hair_back_pony_4 = "sb_ontop_pc_hair_back_pony"

image sb_ontop_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_ontop_pc_hair_back")
    hair_colour_transform()

image sb_ontop_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_ontop_pc_hair_front")
    hair_colour_transform()







image sb_ontop_man_blow_front_base_layer:
    "sb_ontop_man_blow_front_base"
    npc2_skin_base_colour_transform()
image sb_ontop_man_blow_front_shad_layer:
    "sb_ontop_man_blow_front_shad"
    npc2_skin_shad_colour_transform()
image sb_ontop_man_blow_back_layer:
    "sb_ontop_man_blow_back"
    npc2_skin_shad_colour_transform()

image sb_ontop_man_lay_front_base_layer:
    "sb_ontop_man_lay_front_base"
    npc_skin_base_colour_transform()
image sb_ontop_man_lay_front_shad_layer:
    "sb_ontop_man_lay_front_shad"
    npc_skin_shad_colour_transform()
image sb_ontop_man_lay_back_base_layer:
    "sb_ontop_man_lay_back_base"
    npc_skin_base_colour_transform()
image sb_ontop_man_lay_back_shad_layer:
    "sb_ontop_man_lay_back_shad"
    npc_skin_shad_colour_transform()

image sb_ontop_man_behind_base_layer:
    "sb_ontop_man_behind_base"
    npc3_skin_base_colour_transform()
image sb_ontop_man_behind_shad_layer:
    "sb_ontop_man_behind_shad"
    npc3_skin_shad_colour_transform()

image sb_ontop_man_behind_hand_base_layer:
    "sb_ontop_man_behind_hand_base"
    npc3_skin_base_colour_transform()
image sb_ontop_man_behind_hand_shad_layer:
    "sb_ontop_man_behind_hand_shad"
    npc3_skin_shad_colour_transform()

image sb_ontop = LayeredImageProxy("sb_ontop_layer", Transform(align=(0.7, 0.0)))

layeredimage sb_ontop_layer:
    always "sb_ontop_bg_layer"

    group man_blow:
        attribute no_blow default null

        attribute blow "sb_ontop_man_blow_back_layer"

    group man_lay:
        attribute no_lay default null

        attribute lay "sb_ontop_man_lay_back_base_layer"
        attribute lay "sb_ontop_man_lay_back_shad_layer"

    group man_behind:
        attribute no_doggy default null

        attribute doggy "sb_ontop_man_behind_base_layer"
        attribute doggy "sb_ontop_man_behind_shad_layer"

    always "sb_ontop_pc_body_base_layer"
    always "sb_ontop_pc_body_shad_layer"
    if tattoo.ass:
        "sb_ontop_pc_tattoo_tramp"

    if c.outfit == 6:
        "sb_ontop_pub_body_layer"
    elif c.outfit == 20:
        "sb_ontop_maid_body_layer"

    group man_lay:
        attribute no_lay default null

        attribute lay "sb_ontop_man_lay_front_base_layer"
        attribute lay "sb_ontop_man_lay_front_shad_layer"

    if player.pregnancy >= 2:
        "sb_ontop_belly_layer"
    if c.outfit in (6,20):
        "sb_ontop_breasts_c_layer"
    else:
        "sb_ontop_breasts_layer"
    if writing.chest:
        "sb_ontop_pc_writing_chest_layer"
    always "sb_ontop_pc_hair_back_layer"
    always "sb_ontop_pc_face_eyeshadow_layer"
    always "sb_ontop_pc_face_blush_layer"
    if skin_effect.face: 
        "sb_ontop_pc_face_freckles_layer"
    group eyes:
        attribute back default "sb_ontop_pc_face_iris_back_layer"
        attribute back default "sb_ontop_pc_face_eye_back"
        attribute back default "sb_ontop_pc_face_eyeliner_back_layer"

        attribute down "sb_ontop_pc_face_iris_down_layer"
        attribute down "sb_ontop_pc_face_eye_down"
        attribute down "sb_ontop_pc_face_eyeliner_down_layer"

        attribute up "sb_ontop_pc_face_iris_up_layer"
        attribute up "sb_ontop_pc_face_eye_up"
        attribute up "sb_ontop_pc_face_eyeliner_up_layer"


    always if_any ["blow"] "sb_ontop_pc_face_mouth_blow_lipstick_layer"

    group mouth if_not ["blow"]:
        attribute happy "sb_ontop_pc_face_mouth_happy_lipstick_layer"
        attribute happy "sb_ontop_pc_face_mouth_happy_layer"

        attribute shock "sb_ontop_pc_face_mouth_shock_lipstick_layer"
        attribute shock "sb_ontop_pc_face_mouth_shock_layer"

        attribute surprise default "sb_ontop_pc_face_mouth_surprise_lipstick_layer"
        attribute surprise default "sb_ontop_pc_face_mouth_surprise_layer"

        attribute grit "sb_ontop_pc_face_mouth_grit_lipstick_layer"
        attribute grit "sb_ontop_pc_face_mouth_grit_layer"

        attribute ag "sb_ontop_pc_face_mouth_ag_lipstick_layer"
        attribute ag "sb_ontop_pc_face_mouth_ag_layer"

    group brows:
        attribute happy "sb_ontop_pc_face_brow_happy_layer"

        attribute shock "sb_ontop_pc_face_brow_worried_layer"

        attribute surprise default "sb_ontop_pc_face_brow_straight_layer"

        attribute grit "sb_ontop_pc_face_brow_angry_layer"

        attribute ag "sb_ontop_pc_face_brow_happy_layer"

    if player.gagged:
        "sb_ontop_gag_layer"

    always "sb_ontop_pc_hair_front_layer"

    group man_behind:
        attribute no_doggy default null

        attribute doggy "sb_ontop_man_behind_hand_base_layer"
        attribute doggy "sb_ontop_man_behind_hand_shad_layer"

    group man_blow:
        attribute no_blow default null

        attribute blow "sb_ontop_man_blow_front_base_layer"
        attribute blow "sb_ontop_man_blow_front_shad_layer"


    always "sb_ontop_frame"

layeredimage sb_ontop_maid_body_layer:
    if c.socks:
        "sb_ontop_pc_clothes_maid_socks"
    always "sb_ontop_pc_clothes_maid_body"
layeredimage sb_ontop_pub_body_layer:
    if c.socks:
        "sb_ontop_pc_clothes_pub_socks"
    always "sb_ontop_pc_clothes_pub_body"

layeredimage sb_ontop_belly_layer:
    if c.outfit == 6:
        "sb_ontop_pc_clothes_pub_belly"
    if c.outfit == 20:
        "sb_ontop_pc_clothes_maid_belly"
    if not c.outfit:
        "sb_ontop_pc_body_belly_base_layer"
    if not c.outfit:
        "sb_ontop_pc_body_belly_shad_layer"

layeredimage sb_ontop_breasts_layer:
    always "sb_ontop_pc_breasts_base_layer"
    always "sb_ontop_pc_breasts_shad_layer"
    always "sb_ontop_pc_breasts_nips_layer"
    if tattoo.chest:
        "sb_ontop_pc_breasts_tattoo_layer"
    if acc.nipring:
        "sb_ontop_pc_breasts_nipring_layer"
layeredimage sb_ontop_breasts_c_layer:
    always "sb_ontop_pc_breasts_c_base_layer"
    always "sb_ontop_pc_breasts_c_shad_layer"
    always "sb_ontop_pc_breasts_c_nips_layer"
    if tattoo.chest:
        "sb_ontop_pc_breasts_c_tattoo_layer"
    if c.outfit == 6:
        "sb_ontop_pc_clothes_pub_breasts_layer"
    elif c.outfit == 20:
        "sb_ontop_pc_clothes_maid_breasts_layer"

layeredimage sb_ontop_gag_layer:
    always "sb_ontop_pc_face_mouth_gag_lipstick_layer"
    always "sb_ontop_pc_face_mouth_gag_base_layer"
    always "sb_ontop_pc_face_mouth_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
