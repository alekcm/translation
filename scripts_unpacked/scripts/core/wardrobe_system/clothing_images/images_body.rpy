



image pc_body_head_base_layer:
    get_avatar_skin_filenme("body_head_" + str(player.head) + "_base", False)
    skin_base_colour_transform()
image pc_body_head_shad_layer:
    get_avatar_skin_filenme("body_head_" + str(player.head) + "_shad", False)
    skin_shad_colour_transform()





image body_base_base:
    "pc_body_base"
    skin_base_colour_transform()
image body_base_shad:
    "pc_body_shad"
    skin_shad_colour_transform()





image body_armright_ext_1_base:
    "pc_body_armright_ext_1_base"
    skin_base_colour_transform()
image body_armright_ext_1_shad:
    "pc_body_armright_ext_1_shad"
    skin_shad_colour_transform()

image body_armright_ext_2_base:
    "pc_body_armright_ext_2_base"
    skin_base_colour_transform()
image body_armright_ext_2_shad:
    "pc_body_armright_ext_2_shad"
    skin_shad_colour_transform()

image body_armright_ext_3_base:
    "pc_body_armright_ext_3_base"
    skin_base_colour_transform()
image body_armright_ext_3_shad:
    "pc_body_armright_ext_3_shad"
    skin_shad_colour_transform()





image body_breast_base:
    get_breasts_filename(True)
    skin_base_colour_transform()




image pc_body_breast_base_1_layer:
    "pc_body_breast_1_base"
    skin_base_colour_transform()
image pc_body_breast_shad_1_layer:
    "pc_body_breast_1_shad"
    skin_shad_colour_transform()

image pc_body_breast_base_2_layer:
    "pc_body_breast_2_base"
    skin_base_colour_transform()
image pc_body_breast_shad_2_layer:
    "pc_body_breast_2_shad"
    skin_shad_colour_transform()

image pc_body_breast_base_3_layer:
    "pc_body_breast_3_base"
    skin_base_colour_transform()
image pc_body_breast_shad_3_layer:
    "pc_body_breast_3_shad"
    skin_shad_colour_transform()

image pc_body_breast_c_base_1_layer:
    "pc_body_breast_c_1_base"
    skin_base_colour_transform()
image pc_body_breast_c_shad_1_layer:
    "pc_body_breast_c_1_shad"
    skin_shad_colour_transform()

image pc_body_breast_c_base_2_layer:
    "pc_body_breast_c_2_base"
    skin_base_colour_transform()
image pc_body_breast_c_shad_2_layer:
    "pc_body_breast_c_2_shad"
    skin_shad_colour_transform()

image pc_body_breast_c_base_3_layer:
    "pc_body_breast_c_3_base"
    skin_base_colour_transform()
image pc_body_breast_c_shad_3_layer:
    "pc_body_breast_c_3_shad"
    skin_shad_colour_transform()












image pc_body_nips_1_1_layer:
    "pc_body_nips_1_1"
    nipple_colour_transform()
image pc_body_nips_1_2_layer:
    "pc_body_nips_1_2"
    nipple_colour_transform()
image pc_body_nips_1_3_layer:
    "pc_body_nips_1_3"
    nipple_colour_transform()

image pc_body_nips_2_1_layer:
    "pc_body_nips_2_1"
    nipple_colour_transform()
image pc_body_nips_2_2_layer:
    "pc_body_nips_2_2"
    nipple_colour_transform()
image pc_body_nips_2_3_layer:
    "pc_body_nips_2_3"
    nipple_colour_transform()

image pc_body_nips_3_1_layer:
    "pc_body_nips_3_1"
    nipple_colour_transform()
image pc_body_nips_3_2_layer:
    "pc_body_nips_3_2"
    nipple_colour_transform()
image pc_body_nips_3_3_layer:
    "pc_body_nips_3_3"
    nipple_colour_transform()

image pc_body_nips_c_1_1_layer:
    "pc_body_nips_c_1_1"
    nipple_colour_transform()
image pc_body_nips_c_1_2_layer:
    "pc_body_nips_c_1_2"
    nipple_colour_transform()
image pc_body_nips_c_1_3_layer:
    "pc_body_nips_c_1_3"
    nipple_colour_transform()

image pc_body_nips_c_2_1_layer:
    "pc_body_nips_c_2_1"
    nipple_colour_transform()
image pc_body_nips_c_2_2_layer:
    "pc_body_nips_c_2_2"
    nipple_colour_transform()
image pc_body_nips_c_2_3_layer:
    "pc_body_nips_c_2_3"
    nipple_colour_transform()

image pc_body_nips_c_3_1_layer:
    "pc_body_nips_c_3_1"
    nipple_colour_transform()
image pc_body_nips_c_3_2_layer:
    "pc_body_nips_c_3_2"
    nipple_colour_transform()
image pc_body_nips_c_3_3_layer:
    "pc_body_nips_c_3_3"
    nipple_colour_transform()




image body_preg_base:
    get_avatar_preg_belly_filenme(True)
    skin_base_colour_transform()
image body_preg_shad:
    get_avatar_preg_belly_filenme(False)
    skin_shad_colour_transform()




image pc_body_navel:
    "pc_body_bellynav"
    skin_shad_colour_transform()
image pc_body_muscle_0:
    "pc_body_bellytone_0"
    skin_shad_colour_transform(percent_scaler(20, 40, int(player._fitness), reverse=True, floatn=True))
image pc_body_muscle_1:
    "pc_body_bellytone_1"
    skin_shad_colour_transform(percent_scaler(40, 60, int(player._fitness), reverse=True, floatn=True))
image pc_body_muscle_2:
    "pc_body_bellytone_2"
    skin_shad_colour_transform(percent_scaler(60, 80, int(player._fitness), floatn=True))
image pc_body_muscle_3:
    "pc_body_bellytone_3"
    skin_shad_colour_transform(percent_scaler(80, 100, int(player._fitness), floatn=True))

layeredimage pc_body_muscle:
    if int(player._fitness) >= 80  and not player.pregnancy:
        "pc_body_muscle_3"
    if int(player._fitness) >= 60 and not player.pregnancy:
        "pc_body_muscle_2"
    if int(player._fitness) <= 60 and not player.pregnancy:
        "pc_body_muscle_1"
    if int(player._fitness) <= 40 and not player.pregnancy:
        "pc_body_muscle_0"
    always "pc_body_navel"






image body_armleft_beer_back:
    get_avatar_skin_filenme("body_armleft_beer_back", False)
    skin_base_colour_transform()
image body_armleft_beer_front:
    get_avatar_skin_filenme("body_armleft_beer_front", False)
    skin_shad_colour_transform()


image body_armleft_beerbottle_back:
    get_avatar_skin_filenme("body_armleft_beerbottle_back", False)
    skin_base_colour_transform()
image body_armleft_beerbottle_front:
    get_avatar_skin_filenme("body_armleft_beerbottle_front", False)
    skin_shad_colour_transform()

image body_armleft_beerbottle_above_back:
    get_avatar_skin_filenme("body_armleft_beerbottle_above_back", False)
    skin_base_colour_transform()
image body_armleft_beerbottle_above_front:
    get_avatar_skin_filenme("body_armleft_beerbottle_above_front", False)
    skin_shad_colour_transform()


image body_armleft_winebottle_back:
    get_avatar_skin_filenme("body_armleft_winebottle_back", False)
    skin_base_colour_transform()
image body_armleft_winebottle_front:
    get_avatar_skin_filenme("body_armleft_winebottle_front", False)
    skin_shad_colour_transform()

image body_armleft_winebottle_above_back:
    get_avatar_skin_filenme("body_armleft_winebottle_above_back", False)
    skin_base_colour_transform()
image body_armleft_winebottle_above_front:
    get_avatar_skin_filenme("body_armleft_winebottle_above_front", False)
    skin_shad_colour_transform()


image body_armleft_brew_back:
    get_avatar_skin_filenme("body_armleft_brew_back", False)
    skin_base_colour_transform()
image body_armleft_brew_front:
    get_avatar_skin_filenme("body_armleft_brew_front", False)
    skin_shad_colour_transform()

image body_armleft_brew_above_back:
    get_avatar_skin_filenme("body_armleft_brew_above_back", False)
    skin_base_colour_transform()
image body_armleft_brew_above_front:
    get_avatar_skin_filenme("body_armleft_brew_above_front", False)
    skin_shad_colour_transform()


image body_armleft_back:
    get_avatar_skin_filenme("body_armleft_back", False)
    skin_base_colour_transform()
image body_armleft_front:
    get_avatar_skin_filenme("body_armleft_front", False)
    skin_shad_colour_transform()


image body_armleft_cover_back_base:
    get_avatar_skin_filenme("body_armleft_cover_back_base", False)
    skin_base_colour_transform()
image body_armleft_cover_back_shad:
    get_avatar_skin_filenme("body_armleft_cover_back_shad", False)
    skin_shad_colour_transform()
image body_armleft_cover_front_base:
    get_avatar_skin_filenme("body_armleft_cover_front_base", False)
    skin_base_colour_transform()
image body_armleft_cover_front_shad:
    get_avatar_skin_filenme("body_armleft_cover_front_shad", False)
    skin_shad_colour_transform()






image body_armright_back:
    get_avatar_skin_filenme("body_armright_back", False)
    skin_base_colour_transform()
image body_armright_front:
    get_avatar_skin_filenme("body_armright_front", False)
    skin_shad_colour_transform()


image body_armright_umb_back:
    get_avatar_skin_filenme("body_armright_umb_back", False)
    skin_base_colour_transform()
image body_armright_umb_front:
    get_avatar_skin_filenme("body_armright_umb_front", False)
    skin_shad_colour_transform()


image body_armright_beer_back:
    get_avatar_skin_filenme("body_armright_beer_back", False)
    skin_base_colour_transform()
image body_armright_beer_front:
    get_avatar_skin_filenme("body_armright_beer_front", False)
    skin_shad_colour_transform()


image body_armright_cover_back:
    get_avatar_skin_filenme("body_armright_cover_base", False)
    skin_base_colour_transform()
image body_armright_cover_front:
    get_avatar_skin_filenme("body_armright_cover_shad", False)
    skin_shad_colour_transform()


image body_armright_coverb_back:
    get_avatar_skin_filenme("body_armright_coverb_base", False)
    skin_base_colour_transform()
image body_armright_coverb_front:
    get_avatar_skin_filenme("body_armright_coverb_shad", False)
    skin_shad_colour_transform()





image clevage_back:
    get_avatar_skin_filenme("body_clevage_back", True)
    skin_base_colour_transform()
image clevage_front:
    get_avatar_skin_filenme("body_clevage_front", True)
    skin_shad_colour_transform()
image clevage_back_tanlines:
    get_avatar_skin_filenme("body_clevage_back_tanlines", True)
    skin_base_notan_colour_transform()
image clevage_front_tanlines:
    get_avatar_skin_filenme("body_clevage_front_tanlines", True)
    skin_shad_notan_colour_transform()







image pc_hair_fringe_shadow:
    get_hair_fringe_shadow_filename()
    skin_shad_colour_transform()


















image pc_face_freckles_layer:
    "pc_face_freckles"
    skin_shad_colour_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
