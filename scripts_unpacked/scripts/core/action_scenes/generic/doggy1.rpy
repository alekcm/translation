define pink_tile = Color(rgb = (0.850, 0.827, 0.827))

image sb_doggy1_bg_layer:
    "sb_doggy1_bg_" + loc_cur.loc_type

image sb_doggy1_man_blow_base_layer:
    "sb_doggy1_man_blow_base"
    npc2_skin_base_colour_transform()
image sb_doggy1_man_blow_shad_layer:
    "sb_doggy1_man_blow_shad"
    npc2_skin_shad_colour_transform()


image sb_doggy1_pc_head_base_layer:
    "sb_doggy1_pc_head_base"
    skin_base_colour_transform()
image sb_doggy1_pc_head_shad_layer:
    "sb_doggy1_pc_head_shad"
    skin_shad_colour_transform()
image sb_doggy1_pc_hair_layer:
    "sb_doggy1_pc_hair"
    hair_colour_transform()
image sb_doggy1_pc_head_eyeshadow_layer:
    "sb_doggy1_pc_head_eyeshadow"
    accessories_primary_colour_transform("eyeshadow", If(acc.eyeshadow and acc.makeup_on,0.6,0))
image sb_doggy1_pc_head_freckles_layer:
    "sb_doggy1_pc_head_freckles"
    skin_shad_colour_transform(If(skin_effect.face,1,0))
image sb_doggy1_pc_head_blush_layer:
    "sb_doggy1_pc_head_blush"
    blush_opacity_transform()

image sb_doggy1_pc_eye_iris_layer:
    "sb_doggy1_pc_eye_iris"
    eye_colour_transform()
image sb_doggy1_pc_eye_eyeliner_open_layer:
    "sb_doggy1_pc_eye_eyeliner_open_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")
image sb_doggy1_pc_eye_eyeliner_closed_layer:
    "sb_doggy1_pc_eye_eyeliner_closed_" + str(acc.eyeliner)
    accessories_primary_colour_transform("eyeliner")


image sb_doggy1_pc_brow_normal_layer:
    "sb_doggy1_pc_brow_normal"
    hair_colour_transform()
image sb_doggy1_pc_brow_worried_layer:
    "sb_doggy1_pc_brow_worried"
    hair_colour_transform()
image sb_doggy1_pc_brow_angry_layer:
    "sb_doggy1_pc_brow_angry"
    hair_colour_transform()




image sb_doggy1_pc_mouth_ah_lipstick_layer:
    "sb_doggy1_pc_mouth_ah_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_ah_layer:
    "sb_doggy1_pc_mouth_ah"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_grit_lipstick_layer:
    "sb_doggy1_pc_mouth_grit_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_grit_layer:
    "sb_doggy1_pc_mouth_grit"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_neutral_lipstick_layer:
    "sb_doggy1_pc_mouth_neutral_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_neutral_layer:
    "sb_doggy1_pc_mouth_neutral"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_oh_lipstick_layer:
    "sb_doggy1_pc_mouth_oh_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_oh_layer:
    "sb_doggy1_pc_mouth_oh"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_shock_lipstick_layer:
    "sb_doggy1_pc_mouth_shock_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_shock_layer:
    "sb_doggy1_pc_mouth_shock"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_tounge_lipstick_layer:
    "sb_doggy1_pc_mouth_tounge_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and not acc.gagged and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_tounge_layer:
    "sb_doggy1_pc_mouth_tounge"
    matrixcolor OpacityMatrix(If(acc.gagged,0,1))

image sb_doggy1_pc_mouth_gag_lipstick_layer:
    "sb_doggy1_pc_mouth_gag_lipstick"
    accessories_primary_colour_transform("lipstick", If (acc.makeup_on and acc.lipstick,1,0))

image sb_doggy1_pc_mouth_gag_base_layer:
    "sb_doggy1_pc_mouth_gag_base"
    gag_colour_transform()
image sb_doggy1_pc_mouth_gag_metal_layer:
    "sb_doggy1_pc_mouth_gag_metal"
    gag_metal_transform()


image sb_doggy1_pc_arms_base_layer:
    "sb_doggy1_pc_arms_base"
    skin_base_colour_transform()
image sb_doggy1_pc_arms_shad_layer:
    "sb_doggy1_pc_arms_shad"
    skin_shad_colour_transform()

image sb_doggy1_pc_armstied_base_layer:
    "sb_doggy1_pc_armstied_base"
    skin_base_colour_transform()
image sb_doggy1_pc_armstied_shad_layer:
    "sb_doggy1_pc_armstied_shad"
    skin_shad_colour_transform()

image sb_doggy1_pc_belly_shad_layer:
    get_skin_filename("sb_doggy1_pc_belly_shad", True)
    skin_shad_colour_transform()
image sb_doggy1_pc_belly_navring_layer:
    get_skin_filename("sb_doggy1_pc_belly_navring", True)
    accessories_secondary_colour_transform("navelring")

image sb_doggy1_pc_outfit_dungarees_belly_layer:
    get_skin_filename("sb_doggy1_pc_outfit_dungarees_belly", True)

image sb_doggy1_pc_bodytied_base_layer:
    get_skin_filename("sb_doggy1_pc_bodytied_base")
    skin_base_colour_transform()
image sb_doggy1_pc_bodytied_shad_layer:
    get_skin_filename("sb_doggy1_pc_bodytied_shad")
    skin_shad_colour_transform()

image sb_doggy1_pc_breasts_base_layer:
    get_skin_filename("sb_doggy1_pc_breasts_base", breasts=True)
    skin_base_colour_transform()
image sb_doggy1_pc_breasts_shad_layer:
    get_skin_filename("sb_doggy1_pc_breasts_shad", breasts=True)
    skin_shad_colour_transform()
image sb_doggy1_pc_breasts_nips_layer:
    get_skin_filename("sb_doggy1_pc_breasts_nips", breasts=True)
    nipple_colour_transform()
image sb_doggy1_pc_breasts_nipring_layer:
    get_skin_filename("sb_doggy1_pc_breasts_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_doggy1_pc_breaststied_base_layer:
    get_skin_filename("sb_doggy1_pc_breaststied_base", breasts=True)
    skin_base_colour_transform()
image sb_doggy1_pc_breaststied_shad_layer:
    get_skin_filename("sb_doggy1_pc_breaststied_shad", breasts=True)
    skin_shad_colour_transform()
image sb_doggy1_pc_breaststied_nips_layer:
    get_skin_filename("sb_doggy1_pc_breaststied_nips", breasts=True)
    nipple_colour_transform()
image sb_doggy1_pc_breaststied_nipring_layer:
    get_skin_filename("sb_doggy1_pc_breaststied_nipring", breasts=True)
    accessories_secondary_colour_transform("nipring")

image sb_doggy1_pc_bellytied_base_3 = "sb_doggy1_pc_bellytied_base_2"
image sb_doggy1_pc_bellytied_shad_3 = "sb_doggy1_pc_bellytied_shad_2"
image sb_doggy1_pc_bellytied_navring_3 = "sb_doggy1_pc_bellytied_navring_2"
image sb_doggy1_pc_bellytied_base_layer:
    get_skin_filename("sb_doggy1_pc_bellytied_base", True)
    skin_base_colour_transform()
image sb_doggy1_pc_bellytied_shad_layer:
    get_skin_filename("sb_doggy1_pc_bellytied_shad", True)
    skin_shad_colour_transform()
image sb_doggy1_pc_bellytied_navring_layer:
    get_skin_filename("sb_doggy1_pc_bellytied_navring", True)
    accessories_secondary_colour_transform("navelring")

image sb_doggy1_pc_outfit_maid_breasts_layer:
    get_skin_filename("sb_doggy1_pc_outfit_maid_breasts", breasts=True)
image sb_doggy1_pc_outfit_pub_breasts_layer:
    get_skin_filename("sb_doggy1_pc_outfit_pub_breasts", breasts=True)
image sb_doggy1_pc_outfit_dungarees_breasts_layer:
    get_skin_filename("sb_doggy1_pc_outfit_dungarees_breasts", breasts=True)

image sb_doggy1_pc_legs_base_layer:
    get_skin_filename("sb_doggy1_pc_legs_base", False)
    skin_base_colour_transform()
image sb_doggy1_pc_legs_shad_layer:
    get_skin_filename("sb_doggy1_pc_legs_shad", False)
    skin_shad_colour_transform()
image sb_doggy1_pc_legs_insert_shad_layer:
    get_skin_filename("sb_doggy1_pc_legs_insert_shad", False)
    skin_shad_colour_transform(0.4)
image sb_doggy1_pc_legs_insertvag_shad_layer:
    get_skin_filename("sb_doggy1_pc_legs_insertvag_shad", False)
    skin_shad_colour_transform()
image sb_doggy1_pc_legs_vag_layer:
    get_skin_filename("sb_doggy1_pc_legs_vag", False)
    vagina_colour_transform()
image sb_doggy1_pc_legs_phair_layer:
    "sb_doggy1_pc_legs_phair"
    phair_colour_transform()
image sb_doggy1_pc_legs_spank_layer:
    "sb_doggy1_pc_legs_spank"
    opacity_transform(bruise.ass)


image sb_doggy1_man_poke_base_layer:
    "sb_doggy1_man_poke_base"
    npc_skin_base_colour_transform()
image sb_doggy1_man_poke_shad_layer:
    "sb_doggy1_man_poke_shad"
    npc_skin_shad_colour_transform()

image sb_doggy1_man_vag_base_layer:
    "sb_doggy1_man_vag_base"
    npc_skin_base_colour_transform()
image sb_doggy1_man_vag_shad_layer:
    "sb_doggy1_man_vag_shad"
    npc_skin_shad_colour_transform()
image sb_doggy1_man_vag_vag_layer:
    "sb_doggy1_man_vag_vag"
    vagina_colour_transform()

image sb_doggy1_man_anal_base_layer:
    "sb_doggy1_man_anal_base"
    npc_skin_base_colour_transform()
image sb_doggy1_man_anal_shad_layer:
    "sb_doggy1_man_anal_shad"
    npc_skin_shad_colour_transform()
image sb_doggy1_man_anal_vag_layer:
    "sb_doggy1_man_anal_vag"
    vagina_colour_transform(0.7)

image sb_doggy1_writing_anus_layer:
    "sb_doggy1_writing_anus"
    writing_transform("anus")
image sb_doggy1_writing_ass_layer:
    "sb_doggy1_writing_ass"
    writing_transform("ass")
image sb_doggy1_writing_face_layer:
    "sb_doggy1_writing_face"
    writing_transform("face")
image sb_doggy1_writing_forehead_layer:
    "sb_doggy1_writing_forehead"
    writing_transform("forehead")
image sb_doggy1_writing_glasses_layer:
    "sb_doggy1_writing_glasses"
    writing_transform("special")

image sb_doggy1_pc_bodytied_writing_belly_layer:
    get_skin_filename("sb_doggy1_pc_bodytied_writing_belly", preg=True)
    writing_transform("belly")

image sb_doggy1_pc_clothes_bimbo_layer:
    "sb_doggy1_pc_clothes_bimbo_" + str(player.pregnancy)
    outfit_primary_colour_transform()
    clothing_alpha_transform("sb_doggy1_pc_clothes_bimbo_" + str(player.pregnancy), "outfit")

image sb_doggy1 = LayeredImageProxy("sb_doggy1_layered", Transform(xalign = (0.65)))

layeredimage sb_doggy1_layered:

    always "sb_doggy1_bg_layer"

    group bg: 
        attribute grass "sb_doggy1_bg_grass"
        attribute conc "sb_doggy1_bg_conc"
        attribute beach "sb_doggy1_bg_beach"
        attribute room "sb_doggy1_bg_room"
        attribute plaster "sb_doggy1_bg_plaster"
        attribute tile "sb_doggy1_bg_tile"

    group man_front:
        attribute no_blow default null
        attribute blow "sb_doggy1_man_blow_base_layer"
        attribute blow "sb_doggy1_man_blow_shad_layer"

    group head:
        attribute head_down default "sb_doggy1_pc_head_base_layer"
        attribute head_down default "sb_doggy1_pc_head_shad_layer"
        attribute head_down default "sb_doggy1_pc_hair_layer"
        attribute head_down default "sb_doggy1_pc_head_freckles_layer"
        attribute head_down default "sb_doggy1_pc_head_blush_layer"
        attribute head_down default "sb_doggy1_pc_head_eyeshadow_layer"

        attribute blow null
        attribute no_head null
        attribute body_tied null

    group eye if_any "head_down":
        attribute open default "sb_doggy1_pc_eye_iris_layer"
        attribute open default "sb_doggy1_pc_eye_eye"
        attribute open default "sb_doggy1_pc_eye_eyeliner_open_layer"

        attribute closed "sb_doggy1_pc_eye_eyeliner_closed_layer"

    group brow if_any "head_down":
        attribute normal default "sb_doggy1_pc_brow_normal_layer"
        attribute worried "sb_doggy1_pc_brow_worried_layer"
        attribute angry "sb_doggy1_pc_brow_angry_layer"

    group mouth if_any "head_down":
        attribute ah "sb_doggy1_pc_mouth_ah_lipstick_layer"
        attribute ah "sb_doggy1_pc_mouth_ah_layer"

        attribute grit "sb_doggy1_pc_mouth_grit_lipstick_layer"
        attribute grit "sb_doggy1_pc_mouth_grit_layer"
        attribute pain "sb_doggy1_pc_mouth_grit_lipstick_layer"
        attribute pain "sb_doggy1_pc_mouth_grit_layer"

        attribute neutral default "sb_doggy1_pc_mouth_neutral_lipstick_layer"
        attribute neutral default "sb_doggy1_pc_mouth_neutral_layer"

        attribute oh "sb_doggy1_pc_mouth_oh_lipstick_layer"
        attribute oh "sb_doggy1_pc_mouth_oh_layer"

        attribute shock "sb_doggy1_pc_mouth_shock_lipstick_layer"
        attribute shock "sb_doggy1_pc_mouth_shock_layer"

        attribute tounge "sb_doggy1_pc_mouth_tounge_lipstick_layer"
        attribute tounge "sb_doggy1_pc_mouth_tounge_layer"

        attribute ag "sb_doggy1_pc_mouth_tounge_lipstick_layer"
        attribute ag "sb_doggy1_pc_mouth_tounge_layer"

    if player.gagged:
        "sb_doggy1_gag"

    if writing.face:
        if_any "head_down" "sb_doggy1_writing_face_layer"
    if writing.forehead:
        if_any "head_down" "sb_doggy1_writing_forehead_layer"
    if writing.special == "glasses":
        if_any "head_down" "sb_doggy1_writing_glasses_layer"


    group body:
        attribute body_up default "sb_doggy1_pc_arms_base_layer"
        attribute body_up default "sb_doggy1_pc_arms_shad_layer"

    if c.outfit == 6:
        if_not "body_tied" "sb_doggy1_pc_outfit_pub_breasts_layer"
    if c.outfit == 19:
        if_not "body_tied" "sb_doggy1_pc_outfit_dungarees_breasts_layer" 
    if c.gloves == 4:
        if_not "body_tied" "sb_doggy1_pc_outfit_dungarees_gloves"
    if c.outfit == 20:
        if_not "body_tied" "sb_doggy1_pc_outfit_maid_breasts_layer" 

    if not c.outfit in (6,19,20):
        if_not "body_tied" "sb_doggy1_pc_breasts_base_layer"
    if not c.outfit in (6,19,20):
        if_not "body_tied" "sb_doggy1_pc_breasts_shad_layer"
    if not c.outfit in (6,19,20):
        if_not "body_tied" "sb_doggy1_pc_breasts_nips_layer"
    if acc.nipring and not c.outfit in (6,19,20):
        if_not "body_tied" "sb_doggy1_pc_breasts_nipring_layer"

    group body:
        attribute body_up default "sb_doggy1_pc_belly_shad_layer"

        attribute body_tied "sb_doggy1_pc_bodytied_base_layer"
        attribute body_tied "sb_doggy1_pc_bodytied_shad_layer"

    always if_not "body_up" "sb_doggy1_pc_breaststied_base_layer"
    always if_not "body_up" "sb_doggy1_pc_breaststied_shad_layer"
    always if_not "body_up" "sb_doggy1_pc_breaststied_nips_layer"
    if acc.nipring:
        if_not "body_up" "sb_doggy1_pc_breaststied_nipring_layer"
    if player.showing:
        if_not "body_up" "sb_doggy1_pc_bellytied_base_layer"
    if player.showing:
        if_not "body_up" "sb_doggy1_pc_bellytied_shad_layer"
    if  acc.navelring:
        if_not "body_up" "sb_doggy1_pc_bellytied_navring_layer"
    if writing.belly:
        if_not "body_up" "sb_doggy1_pc_bodytied_writing_belly_layer"

    if acc.navelring and not c.outfit:
        if_not "body_tied" "sb_doggy1_pc_belly_navring_layer"

    if c.outfit == 11:
        if_not "body_tied" "sb_doggy1_pc_clothes_bimbo_layer"
    elif c.outfit == 19:
        if_not "body_tied" "sb_doggy1_pc_outfit_dungarees_belly_layer"




    if c.outfit == 6:
        "sb_doggy1_pc_outfit_pub_breasts_layer"
    if c.outfit == 6: 
        "sb_doggy1_pc_outfit_pub_body"



    if c.outfit == 20: 
        "sb_doggy1_pc_outfit_maid_body"

    always "sb_doggy1_pc_legs_base_layer"



    group man_behind:
        attribute noman null default
        attribute poke "sb_doggy1_pc_legs_insert_shad_layer"

        attribute vag "sb_doggy1_pc_legs_insert_shad_layer"  

        attribute anal "sb_doggy1_pc_legs_insert_shad_layer"

    always "sb_doggy1_pc_legs_shad_layer"
    always "sb_doggy1_pc_legs_vag_layer"
    if player.phair and not (c.pants or c.outfit == 19):
        "sb_doggy1_pc_legs_phair_layer"
    always "sb_doggy1_pc_legs_spank_layer"

    if writing.anus:
        "sb_doggy1_writing_anus_layer"
    if writing.ass:
        "sb_doggy1_writing_ass_layer"

    if player.cum_locations["cum_vagin"]:
        "sb_doggy1_cum_vag"
    if player.cum_locations["cum_assin"]:
        "sb_doggy1_cum_anal"
    if player.cum_locations["cum_assout"] or player.cum_locations["cum_vagout"]:
        "sb_doggy1_cum_ass"

    if c.outfit == 19: 
        "sb_doggy1_pc_outfit_dungarees_body"

    if c.socks == 7:
        "sb_doggy1_pc_outfit_pub_socks"
    if c.socks == 14:
        "sb_doggy1_pc_outfit_maid_socks"


    if c.pants == 6 and c.outfit == 6:
        "sb_doggy1_pc_outfit_pub_pants"
    if c.pants == 13 and c.outfit == 20:
        "sb_doggy1_pc_outfit_maid_pants"




    group body:
        attribute body_tied "sb_doggy1_pc_armstied_base_layer"
        attribute body_tied "sb_doggy1_pc_armstied_shad_layer"
        attribute body_tied "sb_doggy1_pc_armstied_col"

    group man_behind:
        attribute noman default null

        attribute poke "sb_doggy1_man_poke_base_layer"
        attribute poke "sb_doggy1_man_poke_shad_layer"

        attribute vag "sb_doggy1_pc_legs_insertvag_shad_layer"
        attribute vag "sb_doggy1_man_vag_base_layer"
        attribute vag "sb_doggy1_man_vag_shad_layer"
        attribute vag "sb_doggy1_man_vag_vag_layer"

        attribute anal "sb_doggy1_man_anal_vag_layer"  
        attribute anal "sb_doggy1_man_anal_base_layer"
        attribute anal "sb_doggy1_man_anal_shad_layer"


    always:
        "sb_doggy1_frame"

layeredimage sb_doggy1_gag:
    always "sb_doggy1_pc_mouth_gag_lipstick_layer"
    always "sb_doggy1_pc_mouth_gag_base_layer"
    always "sb_doggy1_pc_mouth_gag_metal_layer"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
