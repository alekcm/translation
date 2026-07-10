image sb_onbelly_bg_layer:
    "sb_onbelly_bg_" + loc_cur.loc_type


image sb_onbelly_pc_legs_base_layer:
    "sb_onbelly_pc_legs_base"
    skin_base_colour_transform()
image sb_onbelly_pc_legs_shad_layer:
    "sb_onbelly_pc_legs_shad"
    skin_shad_colour_transform()
image sb_onbelly_pc_body_base_layer:
    "sb_onbelly_pc_body_base"
    skin_base_colour_transform()
image sb_onbelly_pc_body_shad_layer:
    "sb_onbelly_pc_body_shad"
    skin_shad_colour_transform()

image sb_onbelly_pc_spank_layer:
    "sb_onbelly_pc_spank"
    opacity_transform(bruise.ass)

image sb_onbelly_pc_breasts_base_layer:
    get_skin_filename("sb_onbelly_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_onbelly_pc_breasts_shad_layer:
    get_skin_filename("sb_onbelly_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_onbelly_pc_breasts_nips_layer:
    get_skin_filename("sb_onbelly_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_onbelly_pc_breasts_nipring_layer:
    get_skin_filename("sb_onbelly_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_onbelly_pc_breasts_nipbar_layer:
    get_skin_filename("sb_onbelly_pc_breasts_nipbar", breasts=True)
    accessories_secondary_colour_transform("nipring")
image sb_onbelly_pc_breasts_tattoo_layer:
    get_skin_filename("sb_onbelly_pc_breasts_tattoo", breasts=True)

image sb_onbelly_pc_breasts_dress_col_layer:
    get_skin_filename("sb_onbelly_pc_breasts_dress_col", breasts=True)
image sb_onbelly_pc_breasts_dress_base_layer:
    get_skin_filename("sb_onbelly_pc_breasts_dress_base", breasts=True)
    skin_base_colour_transform()
image sb_onbelly_pc_breasts_dress_shad_layer:
    get_skin_filename("sb_onbelly_pc_breasts_dress_shad", breasts=True)
    skin_shad_colour_transform()
image sb_onbelly_pc_breasts_dress_tattoo_layer:
    get_skin_filename("sb_onbelly_pc_breasts_dress_tattoo", breasts=True)


image sb_onbelly_pc_face_freckles_layer:
    "sb_onbelly_pc_face_freckles"
    skin_shad_colour_transform()
image sb_onbelly_pc_face_blush_layer:
    "sb_onbelly_pc_face_blush"
    blush_opacity_transform()

image sb_onbelly_pc_face_mouth_ag_lipstick_layer:
    "sb_onbelly_pc_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_onbelly_pc_face_mouth_oh_lipstick_layer:
    "sb_onbelly_pc_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_onbelly_pc_face_mouth_neutral_lipstick_layer:
    "sb_onbelly_pc_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))
image sb_onbelly_pc_face_mouth_happy_lipstick_layer:
    "sb_onbelly_pc_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.lipstick and acc.makeup_on,1,0))

image sb_onbelly_pc_face_eyeshadow_layer:
    "sb_onbelly_pc_face_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If (acc.makeup_on and acc.eyeshadow,0.6,0))

image sb_onbelly_pc_face_eye_eyeliner_up_layer:
    "sb_onbelly_pc_face_eye_eyeliner_up_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_onbelly_pc_face_eye_eyeliner_down_layer:
    "sb_onbelly_pc_face_eye_eyeliner_down_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_onbelly_pc_face_eye_eyeliner_back_layer:
    "sb_onbelly_pc_face_eye_eyeliner_back_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_onbelly_pc_face_eye_iris_back_layer:
    "sb_onbelly_pc_face_eye_iris_back"
    eye_colour_transform()
image sb_onbelly_pc_face_eye_iris_down_layer:
    "sb_onbelly_pc_face_eye_iris_down"
    eye_colour_transform()
image sb_onbelly_pc_face_eye_iris_up_layer:
    "sb_onbelly_pc_face_eye_iris_up"
    eye_colour_transform()


image sb_onbelly_pc_face_brow_straight_layer:
    "sb_onbelly_pc_face_brow_straight"
    hair_colour_transform()
image sb_onbelly_pc_face_brow_worried_layer:
    "sb_onbelly_pc_face_brow_worried"
    hair_colour_transform()
image sb_onbelly_pc_face_brow_angry_layer:
    "sb_onbelly_pc_face_brow_angry"
    hair_colour_transform()
image sb_onbelly_pc_face_brow_slant_layer:
    "sb_onbelly_pc_face_brow_slant"
    hair_colour_transform()

image sb_onbelly_pc_writing_face_layer:
    "sb_onbelly_pc_writing_face"
    writing_transform("face")
image sb_onbelly_pc_writing_forehead_layer:
    "sb_onbelly_pc_writing_forehead"
    writing_transform("forehead")
image sb_onbelly_pc_writing_chest_layer:
    "sb_onbelly_pc_writing_chest"
    writing_transform("chest")
image sb_onbelly_pc_writing_ass_layer:
    "sb_onbelly_pc_writing_ass"
    writing_transform("ass")
image sb_onbelly_pc_writing_anus_layer:
    "sb_onbelly_pc_writing_anus"
    writing_transform("anus")





image sb_onbelly_pc_hair_back_pony_2 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_pony_3 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_pony_4 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_bun_2 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_bun_3 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_bun_4 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_pig_2 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_pig_3 = "sb_onbelly_pc_hair_back_bun"
image sb_onbelly_pc_hair_back_pig_4 = "sb_onbelly_pc_hair_back_bun"

image sb_onbelly_pc_hair_back_layer:
    get_hair_back_cg_filename("sb_onbelly_pc_hair_back")
    hair_colour_transform()

image sb_onbelly_pc_hair_front_layer:
    get_hair_front_cg_filename("sb_onbelly_pc_hair_front")
    hair_colour_transform()



image sb_onbelly_pc_clothes_bottom_2_layer:
    "sb_onbelly_pc_clothing_bottom_2"
    bottom_primary_colour_transform()
image sb_onbelly_pc_clothes_bottom_comp_layer:
    "sb_onbelly_pc_clothing_bottom_comp"
    outfit_primary_colour_transform()
image sb_onbelly_pc_clothes_bottom_sch_layer:
    "sb_onbelly_pc_clothing_bottom_sch"
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_onbelly_pc_clothing_bottom_sch", "outfit")
image sb_onbelly_pc_clothes_bottom_tri_base_layer:
    "sb_onbelly_pc_clothing_bottom_tri_base"
    bottom_primary_colour_transform()
    clothing_alpha_transform("sb_onbelly_pc_clothing_bottom_tri_base", "bottom")
image sb_onbelly_pc_clothes_bottom_tri_trim_layer:
    "sb_onbelly_pc_clothing_bottom_tri_trim"
    bottom_secondary_colour_transform()

image sb_onbelly_pc_clothes_top_knot_layer:
    "sb_onbelly_pc_clothing_top_breasts_knot_" + str(player.breasts)
    top_primary_colour_transform()
image sb_onbelly_pc_clothes_top_comp_layer:
    "sb_onbelly_pc_clothing_top_breasts_comp_" + str(player.breasts)
    outfit_primary_colour_transform()
image sb_onbelly_pc_clothes_top_sch_layer:
    "sb_onbelly_pc_clothing_top_breasts_sch_" + str(player.breasts)
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_onbelly_pc_clothing_top_breasts_sch_" + str(player.breasts), "outfit")
image sb_onbelly_pc_clothes_top_tri_base_layer:
    "sb_onbelly_pc_clothing_top_breasts_tri_base_" + str(player.breasts)
    top_primary_colour_transform()
    clothing_alpha_transform("sb_onbelly_pc_clothing_top_breasts_tri_base_" + str(player.breasts), "top")
image sb_onbelly_pc_clothes_top_tri_trim_layer:
    "sb_onbelly_pc_clothing_top_breasts_tri_trim_" + str(player.breasts)
    top_secondary_colour_transform()
image sb_onbelly_pc_clothes_top_string_layer:
    "sb_onbelly_pc_clothing_top_breasts_string_" + str(player.breasts)
    top_primary_colour_transform()
    clothing_alpha_transform("sb_onbelly_pc_clothing_top_breasts_string_" + str(player.breasts), "top")



image sb_onbelly_man_hands_grope_base_layer:
    "sb_onbelly_man_hands_grope_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hands_grope_shad_layer:
    "sb_onbelly_man_hands_grope_shad"
    npc_skin_shad_colour_transform()


image sb_onbelly_man_hands_rub_base_layer:
    "sb_onbelly_man_hands_rub_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hands_rub_shad_layer:
    "sb_onbelly_man_hands_rub_shad"
    npc_skin_shad_colour_transform()


image sb_onbelly_man_hump_assjob_base_layer:
    "sb_onbelly_man_hump_assjob_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hump_assjob_shad_layer:
    "sb_onbelly_man_hump_assjob_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_hump_mast_base_layer:
    "sb_onbelly_man_hump_mast_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hump_mast_shad_layer:
    "sb_onbelly_man_hump_mast_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_hump_poke_base_layer:
    "sb_onbelly_man_hump_poke_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hump_poke_shad_layer:
    "sb_onbelly_man_hump_poke_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_hump_pokemast_base_layer:
    "sb_onbelly_man_hump_pokemast_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hump_pokemast_shad_layer:
    "sb_onbelly_man_hump_pokemast_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_hump_sex_base_layer:
    "sb_onbelly_man_hump_sex_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_hump_sex_shad_layer:
    "sb_onbelly_man_hump_sex_shad"
    npc_skin_shad_colour_transform()



image sb_onbelly_man_lay_cum_base_layer:
    "sb_onbelly_man_lay_cum_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_lay_cum_shad_layer:
    "sb_onbelly_man_lay_cum_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_lay_inside_base_layer:
    "sb_onbelly_man_lay_inside_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_lay_inside_shad_layer:
    "sb_onbelly_man_lay_inside_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_lay_mast_base_layer:
    "sb_onbelly_man_lay_mast_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_lay_mast_shad_layer:
    "sb_onbelly_man_lay_mast_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly_man_lay_poke_base_layer:
    "sb_onbelly_man_lay_poke_base"
    npc_skin_base_colour_transform()
image sb_onbelly_man_lay_poke_shad_layer:
    "sb_onbelly_man_lay_poke_shad"
    npc_skin_shad_colour_transform()

image sb_onbelly = LayeredImageProxy("sb_onbelly_layer", Transform(align=(0.6, 0.0)))

layeredimage sb_onbelly_layer:

    always "sb_onbelly_bg_layer"

    always "sb_onbelly_pc_legs_base_layer"
    always "sb_onbelly_pc_legs_shad_layer"
    always "sb_onbelly_pc_body_base_layer"
    always "sb_onbelly_pc_body_shad_layer"
    always "sb_onbelly_pc_spank_layer"
    always "sb_onbelly_pc_breasts_base_layer"
    always "sb_onbelly_pc_breasts_shad_layer"
    always "sb_onbelly_pc_breasts_nips_layer"
    if acc.nipring == 1 and not (c.top or c.outfit):
        "sb_onbelly_pc_breasts_nipring_layer"
    elif acc.nipring == 2 and not (c.top or c.outfit):
        "sb_onbelly_pc_breasts_nipbar_layer"
    if tattoo.chest:
        "sb_onbelly_pc_breasts_tattoo_layer"

    always "sb_onbelly_pc_face_eyeshadow_layer"
    if skin_effect.face:
        "sb_onbelly_pc_face_freckles_layer"
    always "sb_onbelly_pc_face_blush_layer"

    if writing.forehead:
        "sb_onbelly_pc_writing_forehead_layer"
    if writing.face:
        "sb_onbelly_pc_writing_face_layer"
    if writing.chest:
        "sb_onbelly_pc_writing_chest_layer"
    if writing.ass:
        "sb_onbelly_pc_writing_ass_layer"
    if writing.anus:
        "sb_onbelly_pc_writing_anus_layer"

    if c.top == 1:
        "sb_onbelly_pc_clothes_top_tri_base_layer"
    elif c.top == 2:
        "sb_onbelly_pc_clothes_top_knot_layer"
    elif c.top == 3:
        "sb_onbelly_pc_clothes_top_string_layer"
    elif c.outfit == 2:
        "sb_onbelly_pc_clothes_top_sch_layer"
    elif c.outfit == 5:
        "sb_onbelly_pc_clothes_top_comp_layer"
    if c.top == 1:
        "sb_onbelly_pc_clothes_top_tri_trim_layer"

    if c.bottom == 1:
        "sb_onbelly_pc_clothes_bottom_tri_base_layer"
    elif c.bottom == 2:
        "sb_onbelly_pc_clothes_bottom_2_layer"
    elif c.bottom == 3:
        "sb_onbelly_pc_clothing_bottom_string"
    elif c.outfit == 2:
        "sb_onbelly_pc_clothes_bottom_sch_layer"
    elif c.outfit == 5:
        "sb_onbelly_pc_clothes_bottom_comp_layer"
    if c.bottom == 1:
        "sb_onbelly_pc_clothes_bottom_tri_trim_layer"


    group brows:
        attribute slant default "sb_onbelly_pc_face_brow_slant_layer"
        attribute straight "sb_onbelly_pc_face_brow_straight_layer"
        attribute worried "sb_onbelly_pc_face_brow_worried_layer"
        attribute angry "sb_onbelly_pc_face_brow_angry_layer"

    group eyes:
        attribute down default "sb_onbelly_pc_face_eye_iris_down_layer"
        attribute down default "sb_onbelly_pc_face_eye_eye_down"
        attribute down default "sb_onbelly_pc_face_eye_eyeliner_down_layer"

        attribute up "sb_onbelly_pc_face_eye_iris_up_layer"
        attribute up "sb_onbelly_pc_face_eye_eye_up"
        attribute up "sb_onbelly_pc_face_eye_eyeliner_up_layer"

        attribute back "sb_onbelly_pc_face_eye_iris_back_layer"
        attribute back "sb_onbelly_pc_face_eye_eye_back"
        attribute back "sb_onbelly_pc_face_eye_eyeliner_back_layer"

    group mouth:
        attribute neutral default "sb_onbelly_pc_face_mouth_neutral_lipstick_layer"
        attribute neutral default "sb_onbelly_pc_face_mouth_neutral"

        attribute happy "sb_onbelly_pc_face_mouth_happy_lipstick_layer"
        attribute happy "sb_onbelly_pc_face_mouth_happy"

        attribute ag "sb_onbelly_pc_face_mouth_ag_lipstick_layer"
        attribute ag "sb_onbelly_pc_face_mouth_ag"

        attribute oh "sb_onbelly_pc_face_mouth_oh_lipstick_layer"
        attribute oh "sb_onbelly_pc_face_mouth_oh" 



    group man_body:
        attribute noman default null

        attribute kaan "sb_onbelly_kaan"

        attribute assjob "sb_onbelly_man_hump_assjob_base_layer"
        attribute assjob "sb_onbelly_man_hump_assjob_shad_layer"

        attribute mast "sb_onbelly_man_hump_mast_base_layer"
        attribute mast "sb_onbelly_man_hump_mast_shad_layer"

        attribute poke "sb_onbelly_man_hump_poke_base_layer"
        attribute poke "sb_onbelly_man_hump_poke_shad_layer"

        attribute pokemast "sb_onbelly_man_hump_pokemast_base_layer"
        attribute pokemast "sb_onbelly_man_hump_pokemast_shad_layer"

        attribute sex "sb_onbelly_man_hump_sex_base_layer"
        attribute sex "sb_onbelly_man_hump_sex_shad_layer"

        attribute lay_cum "sb_onbelly_man_lay_cum_base_layer"
        attribute lay_cum "sb_onbelly_man_lay_cum_shad_layer"

        attribute lay_poke "sb_onbelly_man_lay_poke_base_layer"
        attribute lay_poke "sb_onbelly_man_lay_poke_shad_layer"

        attribute lay_mast "sb_onbelly_man_lay_mast_base_layer"
        attribute lay_mast "sb_onbelly_man_lay_mast_shad_layer"

        attribute lay_sex "sb_onbelly_man_lay_inside_base_layer"
        attribute lay_sex "sb_onbelly_man_lay_inside_shad_layer"



    group man_hands:
        attribute noman default null
        attribute nohands null

        attribute grope if_any ["assjob", "sex", "poke", "kaan"] "sb_onbelly_man_hands_grope_base_layer"
        attribute grope if_any ["assjob", "sex", "poke", "kaan"] "sb_onbelly_man_hands_grope_shad_layer"

        attribute rub if_any ["assjob", "sex", "poke", "kaan"] "sb_onbelly_man_hands_rub_base_layer"
        attribute rub if_any ["assjob", "sex", "poke", "kaan"] "sb_onbelly_man_hands_rub_shad_layer"

    always "sb_onbelly_pc_hair_back_layer"
    always "sb_onbelly_pc_hair_front_layer"

    always:
        "sb_onbelly_frame"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
