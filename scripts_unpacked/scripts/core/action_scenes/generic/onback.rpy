

image sb_onback_larm_relaxed_base_layer:
    "sb_onback_larm_relaxed_base"
    skin_base_colour_transform()
image sb_onback_larm_relaxed_shad_layer:
    "sb_onback_larm_relaxed_shad"
    skin_shad_colour_transform()

image sb_onback_larm_tied_base_layer:
    "sb_onback_larm_tied_base"
    skin_base_colour_transform()
image sb_onback_larm_tied_shad_layer:
    "sb_onback_larm_tied_shad"
    skin_shad_colour_transform()

image sb_onback_larm_penis_base_layer:
    "sb_onback_larm_penis_base"
    skin_base_colour_transform()
image sb_onback_larm_penis_shad_layer:
    "sb_onback_larm_penis_shad"
    skin_shad_colour_transform()
image sb_onback_larm_penis_man_base_layer:
    "sb_onback_larm_penis_man_base"
    skin_base_colour_transform()
image sb_onback_larm_penis_man_shad_layer:
    "sb_onback_larm_penis_man_shad"
    skin_shad_colour_transform()
image sb_onback_larm_penis_man_nails_layer:
    "sb_onback_larm_penis_man_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_onback_larm_blow_base_layer:
    "sb_onback_larm_blow_base"
    skin_base_colour_transform()
image sb_onback_larm_blow_shad_layer:
    "sb_onback_larm_blow_shad"
    skin_shad_colour_transform()
image sb_onback_larm_blow_hand_base_layer:
    "sb_onback_larm_blow_man_base"
    skin_base_colour_transform()
image sb_onback_larm_blow_hand_shad_layer:
    "sb_onback_larm_blow_man_shad"
    skin_shad_colour_transform()



image sb_onback_rarm_relaxed_base_layer:
    "sb_onback_rarm_relaxed_base"
    skin_base_colour_transform()
image sb_onback_rarm_relaxed_shad_layer:
    "sb_onback_rarm_relaxed_shad"
    skin_shad_colour_transform()

image sb_onback_rarm_tied_base_layer:
    "sb_onback_rarm_tied_base"
    skin_base_colour_transform()
image sb_onback_rarm_tied_shad_layer:
    "sb_onback_rarm_tied_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_tied_nails_layer:
    "sb_onback_rarm_tied_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_onback_rarm_mast_base_layer:
    "sb_onback_rarm_mast_base"
    skin_base_colour_transform()
image sb_onback_rarm_mast_shad_layer:
    "sb_onback_rarm_mast_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_mast_hand_base_layer:
    "sb_onback_rarm_mast_hand_base"
    skin_base_colour_transform()
image sb_onback_rarm_mast_hand_shad_layer:
    "sb_onback_rarm_mast_hand_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_mast_hand_vag_layer:
    "sb_onback_rarm_mast_hand_vag"
    vagina_colour_transform()
image sb_onback_rarm_mast_hand_nails_layer:
    "sb_onback_rarm_mast_hand_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_onback_rarm_penis_base_layer:
    "sb_onback_rarm_penis_base"
    skin_base_colour_transform()
image sb_onback_rarm_penis_shad_layer:
    "sb_onback_rarm_penis_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_penis_man_base_layer:
    "sb_onback_rarm_penis_man_base"
    skin_base_colour_transform()
image sb_onback_rarm_penis_man_shad_layer:
    "sb_onback_rarm_penis_man_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_penis_man_nails_layer:
    "sb_onback_rarm_penis_man_nails"
    accessories_primary_colour_transform("nails", If(acc.nails, 1, 0))

image sb_onback_rarm_ass_base_layer:
    "sb_onback_rarm_ass_base"
    skin_base_colour_transform()
image sb_onback_rarm_ass_shad_layer:
    "sb_onback_rarm_ass_shad"
    skin_shad_colour_transform()
image sb_onback_rarm_ass_man_base_layer:
    "sb_onback_rarm_ass_man_base"
    skin_base_colour_transform()
image sb_onback_rarm_ass_man_shad_layer:
    "sb_onback_rarm_ass_man_shad"
    skin_shad_colour_transform()


image sb_onback_body_base_layer:
    "sb_onback_body_base"
    skin_base_colour_transform()
image sb_onback_body_shad_layer:
    "sb_onback_body_shad"
    skin_shad_colour_transform()
image sb_onback_body_vag_layer:
    "sb_onback_body_vag"
    vagina_colour_transform()

image sb_onback_belly_base_3 = "sb_onback_belly_base_2"
image sb_onback_belly_shad_3 = "sb_onback_belly_shad_2"
image sb_onback_belly_base_layer:
    get_skin_filename("sb_onback_belly_base", preg=True)
    skin_base_colour_transform()
image sb_onback_belly_shad_layer:
    get_skin_filename("sb_onback_belly_shad", preg=True)
    skin_shad_colour_transform()


image sb_onback_face_brow_worried_layer:
    "sb_onback_face_brow_worried"
    hair_colour_transform()
image sb_onback_face_brow_happy_layer:
    "sb_onback_face_brow_happy"
    hair_colour_transform()
image sb_onback_face_brow_straight_layer:
    "sb_onback_face_brow_straight"
    hair_colour_transform()
image sb_onback_face_brow_angry_layer:
    "sb_onback_face_brow_angry"
    hair_colour_transform()

image sb_onback_face_eye_down_iris_layer:
    "sb_onback_face_eye_down_iris"
    eye_colour_transform()
image sb_onback_face_eye_up_iris_layer:
    "sb_onback_face_eye_up_iris"
    eye_colour_transform()
image sb_onback_face_eye_right_iris_layer:
    "sb_onback_face_eye_right_iris"
    eye_colour_transform()

image sb_onback_face_eye_down_eyeliner_layer:
    "sb_onback_face_eye_down_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_onback_face_eye_up_eyeliner_layer:
    "sb_onback_face_eye_up_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_onback_face_eye_right_eyeliner_layer:
    "sb_onback_face_eye_right_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_onback_face_eye_closed_eyeliner_layer:
    "sb_onback_face_eye_closed_eyeliner_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")

image sb_onback_face_mouth_oh_lipstick_layer:
    "sb_onback_face_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_neutral_lipstick_layer:
    "sb_onback_face_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_ooh_lipstick_layer:
    "sb_onback_face_mouth_ooh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_ah_lipstick_layer:
    "sb_onback_face_mouth_ah_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_ag_lipstick_layer:
    "sb_onback_face_mouth_ag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_happy_lipstick_layer:
    "sb_onback_face_mouth_happy_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_pout_lipstick_layer:
    "sb_onback_face_mouth_pout_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_gag_lipstick_layer:
    "sb_onback_face_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))
image sb_onback_face_mouth_blow_lipstick_layer:
    "sb_onback_man_facefuck_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))

image sb_onback_hair_front_layer:
    get_hair_front_cg_filename("sb_onback_hair_front")
    hair_colour_transform()
image sb_onback_hair_back_3 = "sb_onback_hair_back_4"
image sb_onback_hair_back_bun_4 = "sb_onback_hair_back_bun"
image sb_onback_hair_back_bun_3 = "sb_onback_hair_back_bun"
image sb_onback_hair_back_bun_2 = "sb_onback_hair_back_bun"
image sb_onback_hair_back_layer:
    get_hair_back_cg_filename("sb_onback_hair_back")
    hair_colour_transform()


image sb_onback_face_eyeshad_layer:
    "sb_onback_face_eyeshad"
    eyeshadow_colour_transform()


image sb_onback_face_freckles_layer:
    "sb_onback_face_freckles"
    skin_shad_colour_transform()

image sb_onback_face_blush_layer:
    "sb_onback_face_blush"
    blush_opacity_transform()

image sb_onback_writing_face_layer:
    "sb_onback_writing_face"
    writing_transform("face")
image sb_onback_writing_forehead_layer:
    "sb_onback_writing_forehead"
    writing_transform("forehead")
image sb_onback_writing_pubic_layer:
    "sb_onback_writing_pubic"
    writing_transform("pubic")
image sb_onback_writing_lleg_layer:
    "sb_onback_writing_lleg"
    writing_transform("lleg")

image sb_onback_phair_layer:
    "sb_onback_phair"
    phair_colour_transform()

image sb_onback_face_mouth_gag_base_layer:
    "sb_onback_face_mouth_gag_base"
    gag_colour_transform()
image sb_onback_face_mouth_gag_metal_layer:
    "sb_onback_face_mouth_gag_metal"
    gag_metal_transform()
layeredimage sb_onback_gag_layered:
    always "sb_onback_face_mouth_gag_lipstick_layer"
    always "sb_onback_face_mouth_gag_base_layer"
    always "sb_onback_face_mouth_gag_metal_layer"



image sb_onback_legs_open_base_layer:
    "sb_onback_legs_open_base"
    skin_base_colour_transform()
image sb_onback_legs_open_shad_layer:
    "sb_onback_legs_open_shad"
    skin_shad_colour_transform()

image sb_onback_legs_closed_base_layer:
    "sb_onback_legs_closed_base"
    skin_base_colour_transform()
image sb_onback_legs_closed_shad_layer:
    "sb_onback_legs_closed_shad"
    skin_shad_colour_transform()

image sb_onback_legs_knee_base_layer:
    "sb_onback_legs_knee_base"
    skin_base_colour_transform()
image sb_onback_legs_knee_shad_layer:
    "sb_onback_legs_knee_shad"
    skin_shad_colour_transform()

image sb_onback_legs_relaxed_base_layer:
    "sb_onback_legs_relaxed_base"
    skin_base_colour_transform()
image sb_onback_legs_relaxed_shad_layer:
    "sb_onback_legs_relaxed_shad"
    skin_shad_colour_transform()

image sb_onback_legs_tied_base_layer:
    "sb_onback_legs_tied_base"
    skin_base_colour_transform()
image sb_onback_legs_tied_shad_layer:
    "sb_onback_legs_tied_shad"
    skin_shad_colour_transform()

image sb_onback_legs_lock_base_layer:
    "sb_onback_legs_lock_base"
    skin_base_colour_transform()
image sb_onback_legs_lock_shad_layer:
    "sb_onback_legs_lock_shad"
    skin_shad_colour_transform()



image sb_onback_breasts_base_layer:
    get_skin_filename("sb_onback_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_onback_breasts_shad_layer:
    get_skin_filename("sb_onback_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_onback_breasts_nips_layer:
    get_skin_filename("sb_onback_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_onback_breasts_nipring_layer:
    get_skin_filename("sb_onback_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_onback_belly_navring_3 = "sb_onback_belly_navring_2"
image sb_onback_belly_navring_layer:
    get_skin_filename("sb_onback_belly_navring", True)
    accessories_secondary_colour_transform("navelring")




image sb_onback_man_mission_base_layer:
    "sb_onback_man_mission_base"
    npc_skin_base_colour_transform()
image sb_onback_man_mission_shad_layer:
    "sb_onback_man_mission_shad"
    npc_skin_shad_colour_transform()
image sb_onback_man_mission_arm_base_layer:
    "sb_onback_man_mission_arm_base"
    npc_skin_base_colour_transform()
image sb_onback_man_mission_arm_shad_layer:
    "sb_onback_man_mission_arm_shad"
    npc_skin_shad_colour_transform()

image sb_onback_man_hump_base_layer:
    "sb_onback_man_hump_base"
    npc_skin_base_colour_transform()
image sb_onback_man_hump_shad_layer:
    "sb_onback_man_hump_shad"
    npc_skin_shad_colour_transform()
image sb_onback_man_hump_arm_base_layer:
    "sb_onback_man_hump_arm_base"
    npc_skin_base_colour_transform()
image sb_onback_man_hump_arm_shad_layer:
    "sb_onback_man_hump_arm_shad"
    npc_skin_shad_colour_transform()

image sb_onback_man_rightmast_hand_base_layer:
    "sb_onback_man_rightmast_hand_base"
    npc3_skin_base_colour_transform()
image sb_onback_man_rightmast_hand_shad_layer:
    "sb_onback_man_rightmast_hand_shad"
    npc3_skin_shad_colour_transform()
image sb_onback_man_rightmast_base_layer:
    "sb_onback_man_rightmast_base"
    npc3_skin_base_colour_transform()
image sb_onback_man_rightmast_shad_layer:
    "sb_onback_man_rightmast_shad"
    npc3_skin_shad_colour_transform()

image sb_onback_man_leftmast_hand_base_layer:
    "sb_onback_man_leftmast_hand_base"
    npc2_skin_base_colour_transform()
image sb_onback_man_leftmast_hand_shad_layer:
    "sb_onback_man_leftmast_hand_shad"
    npc2_skin_shad_colour_transform()
image sb_onback_man_leftmast_base_layer:
    "sb_onback_man_leftmast_base"
    npc2_skin_base_colour_transform()
image sb_onback_man_leftmast_shad_layer:
    "sb_onback_man_leftmast_shad"
    npc2_skin_shad_colour_transform()

image sb_onback_man_blow_base_layer:
    "sb_onback_man_facefuck_base"
    npc2_skin_base_colour_transform()
image sb_onback_man_blow_shad_layer:
    "sb_onback_man_facefuck_shad"
    npc2_skin_shad_colour_transform()

image sb_onback_man_blowdeep_base_layer:
    "sb_onback_man_facedeep_base"
    npc2_skin_base_colour_transform()
image sb_onback_man_blowdeep_shad_layer:
    "sb_onback_man_facedeep_shad"
    npc2_skin_shad_colour_transform()

image sb_onback = LayeredImageProxy("sb_onback_layered", Transform(xalign = (0.7)))

layeredimage sb_onback_layered: 
    if loc(loc_motel_pinkroom):
        "sb_onback_bg"
    else:
        "sb_onback_bg_blue"

    group rarm:
        attribute relax default "sb_onback_rarm_relaxed_base_layer"
        attribute relax default "sb_onback_rarm_relaxed_shad_layer"

        attribute tied "sb_onback_rarm_tied_base_layer"
        attribute tied "sb_onback_rarm_tied_shad_layer"
        attribute tied "sb_onback_rarm_tied_col"
        attribute tied "sb_onback_rarm_tied_nails_layer"

        attribute mast "sb_onback_rarm_mast_base_layer"
        attribute mast "sb_onback_rarm_mast_shad_layer"

        attribute l_penis if_any "man_left" "sb_onback_rarm_penis_base_layer"
        attribute l_penis if_any "man_left" "sb_onback_rarm_penis_shad_layer"

        attribute l_penis if_not "man_left" "sb_onback_rarm_relaxed_base_layer"
        attribute l_penis if_not "man_left" "sb_onback_rarm_relaxed_shad_layer"

        attribute handass if_any "facefuck" "sb_onback_rarm_ass_base_layer"
        attribute handass if_any "facefuck" "sb_onback_rarm_ass_shad_layer"

        attribute handass if_not "facefuck" "sb_onback_rarm_relaxed_base_layer"
        attribute handass if_not "facefuck" "sb_onback_rarm_relaxed_shad_layer"

    always "sb_onback_body_base_layer"
    always "sb_onback_body_shad_layer"
    always "sb_onback_body_vag_layer"

    if player.cum_locations["cum_belly"] and not player.pregnancy:
        "sb_onback_cum_belly"
    if writing.face:
        "sb_onback_writing_face_layer"
    if writing.forehead:
        "sb_onback_writing_forehead_layer"
    if writing.pubic:
        "sb_onback_writing_pubic_layer"
    if player.phair:
        "sb_onback_phair_layer"
    always "sb_onback_face_eyeshad_layer"
    if skin_effect.face:
        "sb_onback_face_freckles_layer"
    always "sb_onback_face_blush_layer"


    group brow:
        attribute straight default "sb_onback_face_brow_straight_layer"
        attribute worried "sb_onback_face_brow_worried_layer"
        attribute happy "sb_onback_face_brow_happy_layer"
        attribute angry "sb_onback_face_brow_angry_layer"

    group eye:
        attribute look_down default "sb_onback_face_eye_down_iris_layer" 
        attribute look_down default "sb_onback_face_eye_down_eye"
        attribute look_down default "sb_onback_face_eye_down_eyeliner_layer"

        attribute look_up "sb_onback_face_eye_up_iris_layer"
        attribute look_up "sb_onback_face_eye_up_eye"
        attribute look_up "sb_onback_face_eye_up_eyeliner_layer"

        attribute look_right "sb_onback_face_eye_right_iris_layer"
        attribute look_right "sb_onback_face_eye_right_eye"
        attribute look_right "sb_onback_face_eye_right_eyeliner_layer"

        attribute look_closed "sb_onback_face_eye_closed_eyeliner_layer"

    group mouth if_not["facefuck", "facefuck_deep"]:
        attribute oh default "sb_onback_face_mouth_oh_lipstick_layer"
        attribute oh default "sb_onback_face_mouth_oh"

        attribute neutral "sb_onback_face_mouth_neutral_lipstick_layer"
        attribute neutral "sb_onback_face_mouth_neutral"

        attribute ooh "sb_onback_face_mouth_ooh_lipstick_layer"
        attribute ooh "sb_onback_face_mouth_ooh"

        attribute ah "sb_onback_face_mouth_ah_lipstick_layer"
        attribute ah "sb_onback_face_mouth_ah"

        attribute ag "sb_onback_face_mouth_ag_lipstick_layer"
        attribute ag "sb_onback_face_mouth_ag"

        attribute happy "sb_onback_face_mouth_happy_lipstick_layer"
        attribute happy "sb_onback_face_mouth_happy"

        attribute pout "sb_onback_face_mouth_pout_lipstick_layer"
        attribute pout "sb_onback_face_mouth_pout"

    if player.cum_locations["cum_face"]:
        "sb_onback_cum_face"
    if player.cum_locations["cum_mouth"]:
        "sb_onback_cum_mouth"

    if player.gagged:
        "sb_onback_gag_layered"
    if player.blind:
        "sb_onback_blindfold"
    always "sb_onback_hair_back_layer"
    always "sb_onback_hair_front_layer"

    group larm:
        attribute down default "sb_onback_larm_relaxed_base_layer"
        attribute down default "sb_onback_larm_relaxed_shad_layer"

        attribute tied "sb_onback_larm_tied_base_layer"
        attribute tied "sb_onback_larm_tied_shad_layer"

        attribute r_penis if_any "man_right" "sb_onback_larm_penis_base_layer"
        attribute r_penis if_any "man_right" "sb_onback_larm_penis_shad_layer"

        attribute r_penis if_not "man_right" "sb_onback_larm_relaxed_base_layer"
        attribute r_penis if_not "man_right" "sb_onback_larm_relaxed_shad_layer"

        attribute blow if_any "facefuck" "sb_onback_larm_blow_base_layer"
        attribute blow if_any "facefuck" "sb_onback_larm_blow_shad_layer"

        attribute blow if_not "facefuck" "sb_onback_larm_relaxed_base_layer"
        attribute blow if_not "facefuck" "sb_onback_larm_relaxed_shad_layer"

    always "sb_onback_breasts_base_layer"
    always "sb_onback_breasts_shad_layer"
    always "sb_onback_breasts_nips_layer"

    if acc.nipring:
        "sb_onback_breasts_nipring_layer"

    if player.pregnancy:
        "sb_onback_belly_base_layer"
    if player.pregnancy:
        "sb_onback_belly_shad_layer"
    if acc.navelring:
        "sb_onback_belly_navring_layer"



    group man_facefuck:
        attribute no_facefuck default null
        attribute facefuck "sb_onback_face_mouth_blow_lipstick_layer"
        attribute facefuck "sb_onback_man_blow_base_layer"
        attribute facefuck "sb_onback_man_blow_shad_layer"

        attribute facefuck_deep "sb_onback_man_blowdeep_base_layer"
        attribute facefuck_deep "sb_onback_man_blowdeep_shad_layer"

    group man_mast_left:
        attribute no_man_left default null

        attribute man_left if_not "l_penis" "sb_onback_man_leftmast_hand_base_layer"
        attribute man_left if_not "l_penis" "sb_onback_man_leftmast_hand_shad_layer"

        attribute man_left if_any "l_penis" "sb_onback_man_leftmast_base_layer"
        attribute man_left if_any "l_penis" "sb_onback_man_leftmast_shad_layer"
        attribute man_left if_any "l_penis" "sb_onback_rarm_penis_man_base_layer"
        attribute man_left if_any "l_penis" "sb_onback_rarm_penis_man_shad_layer"
        attribute man_left if_any "l_penis" "sb_onback_rarm_penis_man_nails_layer"

    group man_mast_right:
        attribute no_man_right default null

        attribute man_right if_not "r_penis" "sb_onback_man_rightmast_hand_base_layer"
        attribute man_right if_not "r_penis" "sb_onback_man_rightmast_hand_shad_layer"

        attribute man_right if_any "r_penis" "sb_onback_man_rightmast_base_layer"
        attribute man_right if_any "r_penis" "sb_onback_man_rightmast_shad_layer"
        attribute man_right if_any "r_penis" "sb_onback_larm_penis_man_base_layer"
        attribute man_right if_any "r_penis" "sb_onback_larm_penis_man_shad_layer"
        attribute man_right if_any "r_penis" "sb_onback_larm_penis_man_nails_layer"

    group man_sex:
        attribute no_sex default null

        attribute missionary if_not ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_mission_arm_base_layer"
        attribute missionary if_not ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_mission_arm_shad_layer"

        attribute missionary if_any ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_hump_arm_base_layer"
        attribute missionary if_any ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_hump_arm_shad_layer"

        attribute hump "sb_onback_man_hump_arm_base_layer"
        attribute hump "sb_onback_man_hump_arm_shad_layer"

    group larm:

        attribute blow if_any "facefuck" "sb_onback_larm_blow_hand_base_layer"
        attribute blow if_any "facefuck" "sb_onback_larm_blow_hand_shad_layer"

    group rarm:
        attribute handass if_any "facefuck" "sb_onback_rarm_ass_man_base_layer"
        attribute handass if_any "facefuck" "sb_onback_rarm_ass_man_shad_layer"

    group dani:
        attribute no_dani null

        attribute dani_kiss "sb_onback_dani_kiss_arm"
        attribute dani_kiss_strapon "sb_onback_dani_kiss_arm"

        attribute dani_facesit "sb_onback_dani_facesit_body"


    group legs:
        attribute closed if_not ["missionary", "hump", "dani_sex", "dani_kiss"]  "sb_onback_legs_closed_base_layer"
        attribute closed if_not ["missionary", "hump", "dani_sex", "dani_kiss"]  "sb_onback_legs_closed_shad_layer"

        attribute open default "sb_onback_legs_open_base_layer"
        attribute open default "sb_onback_legs_open_shad_layer"

        attribute relaxed if_not ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_relaxed_base_layer"
        attribute relaxed if_not ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_relaxed_shad_layer"

        attribute relaxed if_any ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_open_base_layer"
        attribute relaxed if_any ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_open_shad_layer"

        attribute knee if_not ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_knee_base_layer"
        attribute knee if_not ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_knee_shad_layer"

        attribute knee if_any ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_open_base_layer"
        attribute knee if_any ["missionary", "hump", "dani_sex", "dani_kiss"] "sb_onback_legs_open_shad_layer"

        attribute tied "sb_onback_legs_tied_base_layer"
        attribute tied "sb_onback_legs_tied_shad_layer"

        attribute lock if_not "missionary" "sb_onback_legs_open_base_layer"
        attribute lock if_not "missionary" "sb_onback_legs_open_shad_layer"

    if player.cum_locations["cum_assin"]:
        if_any ["open", "tied", "knee"] "sb_onback_cum_anus"
    if player.cum_locations["cum_vagin"]:
        if_any ["open", "tied", "knee"] "sb_onback_cum_vagin"
    if player.cum_locations["cum_vagin"]:
        if_any "relaxed" "sb_onback_cum_vagin_relaxed"
    if player.cum_locations["cum_vagout"]:
        if_any ["open", "tied", "knee"] "sb_onback_cum_vagout"
    if player.cum_locations["cum_vagout"]:
        if_any "relaxed" "sb_onback_cum_vagout_relaxed"

    if writing.lleg:
        if_any ["open", "tied", "knee"] "sb_onback_writing_lleg_layer"
    if acc.anus:
        if_any ["open", "tied", "knee"] "sb_onback_plug"

    group rarm:
        attribute mast "sb_onback_rarm_mast_hand_base_layer"
        attribute mast "sb_onback_rarm_mast_hand_shad_layer"
        attribute mast "sb_onback_rarm_mast_hand_vag_layer"
        attribute mast "sb_onback_rarm_mast_hand_nails_layer"

    group robin:
        attribute robin_lay_open "sb_onback_robin_lay_layered"
        attribute robin_lay_open if_any ["strapon"] "sb_onback_robin_lay_strapon_layered"
        attribute robin_lay_open if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute robin_lay_open if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute robin_lay_open "sb_onback_robin_lay_legs_open"

        attribute robin_lay_closed "sb_onback_robin_lay_layered"
        attribute robin_lay_closed if_any ["strapon"] "sb_onback_robin_lay_strapon_layered"
        attribute robin_lay_closed if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute robin_lay_closed if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute robin_lay_closed "sb_onback_robin_lay_legs_closed"
        attribute robin_lay_closed if_any ["tied"] "sb_onback_legs_tied_base_layer"
        attribute robin_lay_closed if_any ["tied"] "sb_onback_legs_tied_shad_layer"

        attribute robin_lay_mast "sb_onback_robin_lay_layered"
        attribute robin_lay_mast if_any ["strapon"] "sb_onback_robin_lay_strapon"
        attribute robin_lay_mast if_not ["strapon"] "sb_onback_robin_lay_hand_mast"
        attribute robin_lay_mast if_any ["strapon"] "sb_onback_robin_lay_hand_mast_strapon"
        attribute robin_lay_mast if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute robin_lay_mast if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute robin_lay_mast "sb_onback_robin_lay_legs_open"

    group robin_face:
        attribute robin_neutral default if_any ["robin_lay_open", "robin_lay_closed", "robin_lay_mast"] "sb_onback_robin_lay_face_left"
        attribute robin_closed if_any ["robin_lay_open", "robin_lay_closed", "robin_lay_mast"] "sb_onback_dani_lay_face_closed"
        attribute robin_sleep if_any ["robin_lay_open", "robin_lay_closed", "robin_lay_mast"] "sb_onback_dani_lay_face_sleep"
        attribute robin_down if_any ["robin_lay_open", "robin_lay_closed", "robin_lay_mast"] "sb_onback_robin_lay_face_down"


    group dani:
        attribute no_dani null

        attribute dani_sex "sb_onback_dani_sex_layered"
        attribute dani_sex if_any ["strapon"] "sb_onback_dani_sex_strapon_layered"
        attribute dani_sex if_not ["tied"] "sb_onback_dani_sex_arm_open"
        attribute dani_sex if_any ["tied"] "sb_onback_dani_sex_arm_tied"

        attribute dani_kiss "sb_onback_dani_kiss_layered"
        attribute dani_kiss if_any ["strapon"] "sb_onback_dani_kiss_strapon"

        attribute dani_facesit if_not ["tied"] "sb_onback_dani_facesit_arm_open"
        attribute dani_facesit if_any ["tied"] "sb_onback_dani_facesit_arm_tied"

        attribute dani_lay_open "sb_onback_dani_lay_layered"
        attribute dani_lay_open if_any ["strapon"] "sb_onback_dani_lay_strapon_layered"
        attribute dani_lay_open if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute dani_lay_open if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute dani_lay_open "sb_onback_dani_lay_legs_open"

        attribute dani_lay_closed "sb_onback_dani_lay_layered"
        attribute dani_lay_closed if_any ["strapon"] "sb_onback_dani_lay_strapon_layered"
        attribute dani_lay_closed if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute dani_lay_closed if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute dani_lay_closed "sb_onback_dani_lay_legs_closed"
        attribute dani_lay_closed if_any ["tied"] "sb_onback_legs_tied_base_layer"
        attribute dani_lay_closed if_any ["tied"] "sb_onback_legs_tied_shad_layer"

        attribute dani_lay_mast "sb_onback_dani_lay_layered"
        attribute dani_lay_mast if_any ["strapon"] "sb_onback_dani_lay_strapon"
        attribute dani_lay_mast if_not ["strapon"] "sb_onback_dani_lay_hand_mast"
        attribute dani_lay_mast if_any ["strapon"] "sb_onback_dani_lay_hand_mast_strapon"
        attribute dani_lay_mast if_any ["open", "hump", "missionary"] "sb_onback_legs_open_base_layer"
        attribute dani_lay_mast if_any ["open", "hump", "missionary"] "sb_onback_legs_open_shad_layer"
        attribute dani_lay_mast "sb_onback_dani_lay_legs_open"



    group dani_face:
        attribute dani_neutral default if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_neutral"
        attribute dani_closed if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_closed"
        attribute dani_sleep if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_sleep"
        attribute dani_smile if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_smile"
        attribute dani_closed if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_closed"
        attribute dani_down if_any ["dani_lay_open", "dani_lay_closed", "dani_lay_mast"] "sb_onback_dani_lay_face_down"

    group man_sex:
        attribute no_sex default null

        attribute missionary if_not ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_mission_base_layer"
        attribute missionary if_not ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_mission_shad_layer"

        attribute missionary if_any ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_hump_base_layer"
        attribute missionary if_any ["facefuck", "facefuck_deep", "man_right", "man_left"] "sb_onback_man_hump_shad_layer"

        attribute hump "sb_onback_man_hump_base_layer"
        attribute hump "sb_onback_man_hump_shad_layer"

    group legs:

        attribute lock if_any "missionary" "sb_onback_legs_lock_base_layer"
        attribute lock if_any "missionary" "sb_onback_legs_lock_shad_layer"

    group dani_strapon:

        attribute no_strapon default null
        attribute strapon null

    always "sb_onback_frame"

layeredimage sb_onback_dani_lay_layered:
    always "sb_onback_dani_lay_body"
    if dani.heavy_preg:
        "sb_onback_dani_lay_preg_2"
    elif dani.showing:
        "sb_onback_dani_lay_preg_1"

layeredimage sb_onback_dani_lay_strapon_layered:
    if dani.heavy_preg:
        "sb_onback_dani_lay_strapon_2"
    elif dani.showing:
        "sb_onback_dani_lay_strapon_1"
    else:
        "sb_onback_dani_lay_strapon"

layeredimage sb_onback_dani_sex_layered:
    always "sb_onback_dani_sex_body"
    if dani.heavy_preg:
        "sb_onback_dani_sex_preg_2"
    elif dani.showing:
        "sb_onback_dani_sex_preg_1"

layeredimage sb_onback_dani_sex_strapon_layered:
    if dani.heavy_preg:
        "sb_onback_dani_sex_strapon_2"
    elif dani.showing:
        "sb_onback_dani_sex_strapon_1"
    else:
        "sb_onback_dani_sex_strapon"

layeredimage sb_onback_dani_kiss_layered:
    always "sb_onback_dani_kiss_body"
    if dani.heavy_preg:
        "sb_onback_dani_kiss_preg_2"
    elif dani.showing:
        "sb_onback_dani_kiss_preg_1"



layeredimage sb_onback_robin_lay_layered:
    always "sb_onback_robin_lay_body"
    if sum(player.cum_locations.values()) > 20:
        "sb_onback_robin_lay_cum"
    if robin.heavy_preg:
        "sb_onback_robin_lay_preg_2"
    elif robin.showing:
        "sb_onback_robin_lay_preg_1"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
