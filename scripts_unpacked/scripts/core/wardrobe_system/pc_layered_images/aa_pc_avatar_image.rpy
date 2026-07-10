init python:
    hair, face, world, outfit, top, bottom, bra, pants, socks, makeup = 1, 0, 0, 1, 0, 0, 0, 0, 0, 0 

define rarm_beer = ["beerr", "beerb", "coffee"]
define larm_beer = ["beerl", "beerb"]
define arm_beer = [larm_beer, rarm_beer]
define show_womb = False










layeredimage pc:  


    at sprite_highlight("pc")


    group dummy:
        attribute pc_dummy_attribute:
            null





    if grope_mastleft:
        "pc_grope_mastleft"
    if grope_mastright:
        "pc_grope_mastright"
    if grope_ass:
        "pc_grope_ass"





    if player.right_hand == "umb":
        "pc_body_armright_umb_canopy" anchor (0.0, 0.05)





    if c.hat == 1:
        "flappon_b_b_layered"
    elif c.hat == 2:
        "santa_ab_layered"
    elif c.hat == 6:
        "hat_sun_back_layer"

    if c.hat == 2:
        "santa_bb_layered"
    elif c.hat == 3:
        "witch_back_layered"





    if player.left_hand == "beer": 
        "body_armleft_beer_back"
    elif player.left_hand == "beer_bottle": 
        "body_armleft_beerbottle_back"
    elif player.left_hand == "wine_bottle": 
        "body_armleft_winebottle_back"
    elif player.left_hand == "brew" or player.left_hand == "flyer" or player.left_hand == "hat":
        "body_armleft_brew_back"
    elif player.cover_breasts:
        "body_armleft_cover_back_base"
    else:
        "body_armleft_back"

    if player.left_hand == "beer": 
        "body_armleft_beer_front"
    elif player.left_hand == "beer_bottle": 
        "body_armleft_beerbottle_front"
    elif player.left_hand == "wine_bottle": 
        "body_armleft_winebottle_front"
    elif player.left_hand == "brew" or player.left_hand == "flyer" or player.left_hand == "hat":
        "body_armleft_brew_front"
    elif player.cover_breasts:
        "body_armleft_cover_back_shad"
    else:
        "body_armleft_front"





    if c.top == 16:
        "shoulderlessruff_larm_layer"


    elif c.top == 24:
        "sweater_larm"
    elif c.top == 31:
        "crophoodie_larm_layerd"
    elif c.top == 38:
        "perry_larm_layerd"
    elif c.top == 39:
        "latextop_larm_layer"

    elif c.outfit == 32:
        "latexbody_larm_layer"
    elif c.outfit == 36:
        "highleggown_larm_layerd"
    elif c.outfit == 40:
        "rompersq_larm_layer"





    if acc.nails == 1 and player.left_hand == "":
        "polish_left_layered"





    if player.left_hand == "beer_bottle":
        "pc_body_armleft_beerbottle_above_bottle"
    if player.left_hand == "beer_bottle":
        "body_armleft_beerbottle_above_back"
    if player.left_hand == "beer_bottle":
        "body_armleft_beerbottle_above_front"

    if player.left_hand == "wine_bottle":
        "pc_body_armleft_winebottle_above_bottle"
    if player.left_hand == "wine_bottle":
        "body_armleft_winebottle_above_back"
    if player.left_hand == "wine_bottle":
        "body_armleft_winebottle_above_front"

    if player.left_hand == "brew" or player.left_hand == "flyer" or player.left_hand == "hat":
        "body_armleft_brew_above_back"
    if player.left_hand == "brew" or player.left_hand == "flyer" or player.left_hand == "hat":
        "body_armleft_brew_above_front"

    if c.gloves == 1:
        "fingerless_gloves_l_layer"
    elif c.gloves == 2:
        "sleeve_gloves_l_layer"
    elif c.gloves == 3:
        "server_gloves_l_layer"
    elif c.gloves == 4:
        "rubber_gloves_l"
    elif c.gloves == 5:
        "pads_gloves_l_layer"
    elif c.gloves == 6:
        "cow_gloves_l_layer"
    elif c.gloves == 7:
        "santa_gloves_l_layer"

    if c.gloves == 1 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "fingerless_gloves_l_above_layer"
    elif c.gloves == 2 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "sleeve_gloves_l_above_layer"
    elif c.gloves == 3 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "server_gloves_l_above_layer"
    elif c.gloves == 4 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "rubber_gloves_l_above"
    elif c.gloves == 5 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "pads_gloves_l_above_layer"
    elif c.gloves == 6 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "cow_gloves_l_above_layer"
    elif c.gloves == 7 and player.left_hand in ["flyer", "hat", "beer_bottle", "wine_bottle", "brew"]:
        "santa_gloves_l_above_layer"





    if c.top == 22:
        "sheerdrop_larm_layer"

    if c.coat == 2:
        "cropjump_coat_larm_layerd"
    elif c.coat == 4:
        "longcoat_larm_layer"
    elif c.coat == 7:
        "puff_coat_larm_layerd"
    elif c.coat == 9:
        "ziphoodie_coat_larm_layerd"
    elif c.coat == 10:
        "crophoodie_larm_layerd"
    elif c.coat == 12:
        "onesee_larm_layerd"
    elif c.coat == 13:
        "knithoodie_larm_layerd"







    if player.hair_neck > 0:
        "pc_hair_pony_layer"

    always "body_base_base"

    if player.right_hand == "cover_vag":
        "body_armright_ext_1_base"
    elif player.right_hand == "cover_breast":
        "body_armright_ext_3_base"
    elif not player.right_hand == "":
        "body_armright_ext_2_base"
    else:
        "body_armright_ext_1_base"

    if not (player.pregnancy or player.isfat):
        "pc_body_muscle"

    always "body_base_shad"
    if player.right_hand == "cover_vag":
        "body_armright_ext_1_shad"
    elif player.right_hand == "cover_breast":
        "body_armright_ext_3_shad"
    elif not player.right_hand == "":
        "body_armright_ext_2_shad"
    else:
        "body_armright_ext_1_shad"

    if player.pregnancy or player.isfat:
        "body_preg_base"
    if player.pregnancy or player.isfat:
        "body_preg_shad"

    always "pc_breasts"
    always "pc_bruise_spank"

    if junk_var == 0:
        "pc_tattoo_chest"

    always "pc_writing_body"


    if bruise.belly > 0:
        "pc_bruise_belly"

    if bruise.chest > 0:
        "pc_bruise_chest"

    if player.hair_neck > 0:
        "pc_hair_loose_layer"

    if acc.ear == 103:
        "ear_elf"




    if acc.nipring == 1:
        "nipring_layer"
    elif acc.nipring == 2:
        "nipheart_layer"





    if acc.navelring == 1:
        "navelheart_layer"







    if player.phair > 0:
        "pc_phair"



    if c.hat == 4:
        "hat_catgirl_base_layered"


    if c.hat == 4:
        "hat_catgirl_trim_layered"
    elif c.hat == 7:
        "hat_bunny_layer" anchor (0.0, 0.139)
    elif c.hat == 8:
        "hat_maid_layered"
    elif c.hat == 10:
        "hat_cow_layer"




    if player.hair_fringe > 0:
        "pc_hair_fringe_shadow"





    always:
        "pc_effect_cum_layer"






    if bruise.face > 0:
        "pc_bruise_face"





    if acc.eyeshadow == 1 and acc.makeup_on == True:
        "pc_face_eyeshadow_layer"
    if acc.blush == 1 and acc.makeup_on == True:
        "pc_face_blush_layer"






    if skin_effect.face:
        "pc_face_freckles_layer"
    if player.drool or player.has_perk(perk_blackout):
        "pc_face_effect_1"
    if player.puke:
        "pc_face_effect_3"
    if player.cry or player.beingraped:
        "pc_face_effect_5"
    always "pc_face_mood_flushed_layer"
    always "pc_face_effect_pink"
    if player.hygiene < 50:
        "pc_face_effect_sweat"

    always "pc_writing_face"

    if not blood.face == 0:
        "pc_blood_face"

    always "pc_face"





    if player.effect_heart and player.eye <=2:
        "pc_face_mood_heart"
    if player.effect_tired:
        "pc_face_mood_tired"

    if bruise.special == "haven":
        "bruise_eye"




    if c.bsuit == 1:
        "stringsuit_layer"
    elif c.bsuit == 2:
        "underboob_suit_layer"
    elif c.bsuit == 3:
        "frilly_suit_layer"
    elif c.bsuit == 4:
        "tleo_body"
    elif c.bsuit == 5:
        "open_body"
    elif c.bsuit == 6:
        "meshedsuit_layer"




    if c.bra == 1:
        "fcup_layer"
    elif c.bra == 2:
        "sport1_layer"
    elif c.bra == 3:
        "sport2_layer"
    elif c.bra == 4:
        "strapless_layer"
    elif c.bra == 5:
        "shelf_layer"
    elif c.bra == 6:
        "open_bra_layer"
    elif c.bra == 7:
        "stringfront_layer"
    elif c.bra == 8:
        "wrap_bra_layer"
    elif c.bra == 9:
        "frilly_bra_layer"
    elif c.bra == 10:
        "triangle_bra_layer"
    elif c.bra == 11:
        "simple_bra_layer"
    elif c.bra == 12:
        "half_bra_layer"
    elif c.bra == 13:
        "cow_bra_layer"
    elif c.bra == 14:
        "nipheart_bra_layer"




    if c.pants == 1:
        "briefs1_layer"
    elif c.pants == 2:
        "briefs2_layer"
    elif c.pants == 3:
        "briefs3_layer"
    elif c.pants == 4:
        "french_layer"
    elif c.pants == 5:
        "thong1_layer"
    elif c.pants == 6:
        "bargirl_pants_layer"
    elif c.pants == 7:
        "stripthong_layer"
    elif c.pants == 8:
        "highleg_layer"
    elif c.pants == 9:
        "open_pants_layer"
    elif c.pants == 10:
        "lowride_pants_layer"
    elif c.pants == 11:
        "cstring_layer"
    elif c.pants == 12:
        "crossstring_layer"
    elif c.pants == 13:
        "maid_pants_layer"
    elif c.pants == 14:
        "wrap_pants_layer"
    elif c.pants == 15:
        "strappy_pants_layer"
    elif c.pants == 16:
        "cow_pants_layer"






    if player.has_perk([perk_pregband_preg, perk_pregband_notpreg]):
        "pregband"



    if c.socks == 1:
        "tights_layer"
    elif c.socks == 2:
        "high_stocking_layer"
    elif c.socks == 3:
        "stocking_layer"
    elif c.socks == 4:
        "schsocks_layer"
    elif c.socks == 5:
        "thinstripesocks_layer"
    elif c.socks == 6:
        "thickstripesocks_layer"
    elif c.socks == 7:
        "bargirl_socks_layer"
    elif c.socks == 8:
        "garter_socks_layer"
    elif c.socks == 9:
        "bumhigh_layer"
    elif c.socks == 10:
        "pointed_layer"
    elif c.socks == 11:
        "diamond_layer"
    elif c.socks == 12:
        "socks_server_layer"
    elif c.socks == 13:
        "leggings_layer"
    elif c.socks == 14:
        "maid_socks_layer"
    elif c.socks == 15:
        "polkadotsocks_layer"
    elif c.socks == 16:
        "polkastripesocks_layer"
    elif c.socks == 17:
        "kneepads_layer"
    elif c.socks == 18:
        "catsocks_layer"
    elif c.socks == 20:
        "cowsocks_layer"
    elif c.socks == 21:
        "santa_socks_layer"




    if grope_penisinside:
        "pc_grope_penisinside"
    if grope_penispoke and c.skirt:
        "pc_grope_penispoke"






    if c.top == 12:
        "shirt_layer"






    if c.bottom == 1:
        "microbikini_bottom_layer"
    elif c.bottom == 2:
        "knotbikini_bottom"
    elif c.bottom == 3:
        "stringbikini_bottom_layer"
    elif c.bottom == 4:
        "trousers"
    elif c.bottom == 5:
        "skirtpleat"
    elif c.bottom == 6:
        "skirtstraight"
    elif c.bottom == 7:
        "skirtflared"

    elif c.bottom == 8:
        "vballshorts_layer"
    elif c.bottom == 9:
        "yoga_layer"
    elif c.bottom == 10:
        "havenshorts_layer"
    elif c.bottom == 11:
        "micromini_layer"
    elif c.bottom == 12:
        "straptrousers_layer"
    elif c.bottom == 13:
        "dancemini_layer"
    elif c.bottom == 14:
        "rags_bottom"
    elif c.bottom == 15:
        "pleatmini_layer"
    elif c.bottom == 16:
        "shortshorts_layer"
    elif c.bottom == 17:
        "flaredshorts_layer"
    elif c.bottom == 18:
        "jeantorn_layer"
    elif c.bottom == 19:
        "frillskirt_layer"
    elif c.bottom == 20:
        "highskirt_base"
    elif c.bottom == 21:
        "heartpatch_layer"
    elif c.bottom == 22:
        "harlequin_bottom_layer"
    elif c.bottom == 23:
        "hipjeans_layer"
    elif c.bottom == 24:
        "rippedhipjeans_layer"
    elif c.bottom == 25:
        "rippedskirt_layer"
    elif c.bottom == 26:
        "sweatpants_layer"
    elif c.bottom == 27:
        "sweatshorts_layer"
    elif c.bottom == 28:
        "micromini2_layer"
    elif c.bottom == 29:
        "sweatpantsband_layer"
    elif c.bottom == 30:
        "minitight_layer"
    elif c.bottom == 31:
        "latextrou_layered"
    elif c.bottom == 32:
        "jayshorts_layer"
    elif c.bottom == 33:
        "knotskirt_layer"
    elif c.bottom == 34:
        "ruffskirt_layer"
    elif c.bottom == 35:
        "santa_skirt_layer"
    elif c.bottom == 36:
        "bloomers_base"
    elif c.bottom == 37:
        "trousers_stripe_base"
    elif c.bottom == 38:
        "yogashorts_layer"
    elif c.bottom == 39:
        "shortscut_layer"



    if c.socks == 19:
        "latexboots_layer"





    if c.top == 1:
        "microbikini_top_layer"
    elif c.top == 2:
        "knotbikini_top"
    elif c.top == 3:
        "stringbikini_top_layer"
    elif c.top == 4:
        "loosetee_layer"
    elif c.top == 5:
        "croptop"
    elif c.top == 6:
        "vestskin_layer"
    elif c.top == 7:
        "teeskin_layer"
    elif c.top == 8:
        "vballtop_layer"
    elif c.top == 9:
        "croptee_layer"
    elif c.top == 10:
        "strappy_layer"
    elif c.top == 11:
        "haventop_layer"

    elif c.top == 13:
        "haltertop_layer"
    elif c.top == 14:
        "knotfront_layer"
    elif c.top == 15:
        "shoulderless_layer"
    elif c.top == 16:
        "shoulderlessruff_layer"
    elif c.top == 17:
        "sleevelessneck_layer"
    elif c.top == 18:
        "vestloose_layer"
    elif c.top == 19:
        "undercrop_layer"
    elif c.top == 20:
        "knotted_layer"
    elif c.top == 21:
        "rags_top_layer"
    elif c.top == 22:
        "sheerdrop_layer"
    elif c.top == 23:
        "sportloose_layer"
    elif c.top == 24:
        "sweater_layerd"
    elif c.top == 25:
        "vestlong_layer"


    elif c.top == 27:
        "heartpatch_top_layerd"
    elif c.top == 28:
        "harlequin_top_layerd"
    elif c.top == 29:
        "rippedtee_layerd"
    elif c.top == 30:
        "boobwindow_layerd"
    elif c.top == 31:
        "crophoodie_layerd"
    elif c.top == 32:
        "meshtop_layerd"
    elif c.top == 33:
        "strappycross_layer"
    elif c.top == 34:
        "only_layer"
    elif c.top == 35:
        "chiwindow_layer"
    elif c.top == 36:
        "boobtube_layer"
    elif c.top == 37:
        "deepv_layer"
    elif c.top == 38:
        "perry_layerd"
    elif c.top == 39:
        "latextop_layered"
    elif c.top == 40:
        "jaytee_layered"
    elif c.top == 41:
        "drapetop_layered"
    elif c.top == 42:
        "rufftop_layered"
    elif c.top == 43:
        "santa_top_layered"
    elif c.top == 44:
        "sleevelessmuff_layered"
    elif c.top == 45:
        "shirtbaggy_layered"
    elif c.top == 46:
        "shoulderlesstee_layered"



    if c.outfit == 1:
        "hospitalgown_layer"
    elif c.outfit == 2:
        "schswimsuit"
    elif c.outfit == 3:
        "summerdress"
    elif c.outfit == 4:
        "bodycon"
    elif c.outfit == 5:
        "compswimsuit_layer"
    elif c.outfit == 6:
        "bargirl_layer"
    elif c.outfit == 7:
        "shoulderwrap_layer"
    elif c.outfit == 8:
        "backlessmini"
    elif c.outfit == 9:
        "rags_outfit_layer"
    elif c.outfit == 10:
        "bodyconmaternal_layer"
    elif c.outfit == 11:
        "bimbodress"
    elif c.outfit == 12:
        "halterdress_layer"
    elif c.outfit == 13:
        "sidestrapdress_layer"
    elif c.outfit == 14:
        "patchdress_layer"
    elif c.outfit == 15:
        "collardress_layer"
    elif c.outfit == 16:
        "serverdress_layer" 
    elif c.outfit == 17:
        "corsetdress_layer"
    elif c.outfit == 18:
        "bunnyoutfit_layer"
    elif c.outfit == 19:
        "dungarees_layer"
    elif c.outfit == 20:
        "maid_outfit_layer"
    elif c.outfit == 21:
        "puffdress_outfit_layer"
    elif c.outfit == 22:
        "paledress_layer"
    elif c.outfit == 23:
        "frillydress_outfit_layer"
    elif c.outfit == 24:
        "frontdress_outfit_layer"
    elif c.outfit == 25:
        "gothdress_outfit_layer"
    elif c.outfit == 26:
        "highlegdress_layer"
    elif c.outfit == 27:
        "cheongsam_layer"
    elif c.outfit == 28:
        "chinesedress_layer"
    elif c.outfit == 29:
        "nicedress_layer"
    elif c.outfit == 30:
        "deephalter_layer"
    elif c.outfit == 31:
        "waistband_layerd"
    elif c.outfit == 32:
        "latexbody_layered"
    elif c.outfit == 33:
        "latexdress_layered"
    elif c.outfit == 34:
        "latexwindow_layered"
    elif c.outfit == 35:
        "teestrapdress_layered"
    elif c.outfit == 36:
        "highleggown_layered"
    elif c.outfit == 37:
        "crumpdress_layered"
    elif c.outfit == 38:
        "romper_layered"
    elif c.outfit == 39:
        "ruffpj_layered"
    elif c.outfit == 40:
        "rompersq_layered"
    elif c.outfit == 41:
        "romperv_layered"
    elif c.outfit == 42:
        "knitdress_flat"





    if acc.choker == 1 and not c.top == 12:
        "choker_clasp_b_layered"
    elif acc.choker == 2 and not c.top == 12:
        "choker_thick_b_layered"
    elif acc.choker == 3 and not c.top == 12:
        "choker_catgirl_base_layered"
    elif acc.choker == 4 and not c.top == 12:
        "choker_bowtie_layer"

    if acc.choker == 1 and not c.top == 12:
        "choker_clasp_f_layered"
    elif acc.choker == 2 and not c.top == 12:
        "choker_thick_f_layered"
    elif acc.choker == 3 and not c.top == 12:
        "choker_catgirl_trim_layered"
    elif acc.choker == 5 and not c.top == 12:
        "cow_choker"
    elif acc.choker == 6 and not c.top == 12:
        "wolf_choker"


    if c.top == 26:
        "shirt_sleeveless_layer"





    if c.coat == 1:
        "teehood_coat_layerd"
    elif c.coat == 2:
        "cropjump_coat_layerd"
    elif c.coat == 3:
        "sleevelesscoat_coat_layerd"
    elif c.coat == 4:
        "longcoat_body_layer"
    elif c.coat == 5:
        "coat_server_body_layer"
    elif c.coat == 6:
        "waistcoat_coat_layerd"
    elif c.coat == 7:
        "puff_coat_layerd"
    elif c.coat == 8:
        "sleevelesshoodie_coat_layerd"
    elif c.coat == 9:
        "ziphoodie_coat_layerd"
    elif c.coat == 10:
        "crophoodie_layerd"
    elif c.coat == 11:
        "bftee_layerd"
    elif c.coat == 12:
        "onesee_layerd"
    elif c.coat == 13:
        "knithoodie_base_body"




    if grope_penispoke and not c.skirt:
        "pc_grope_penispoke"

    always:
        "pc_jacket_abovebottoms"

    if grope_hips:
        "pc_grope_hips"





    if grope_breasts1:
        "pc_grope_breasts1"
    elif grope_breasts2:
        "pc_grope_breasts2"
    if (grope_breasts2 or grope_breasts1) and player.milky and c.cansee_nips and player.breasts == 3:
        "pc_extra_milksquirt_3"
    elif (grope_breasts2 or grope_breasts1) and player.milky and c.cansee_nips and player.breasts == 2:
        "pc_extra_milksquirt_2"
    elif (grope_breasts2 or grope_breasts1) and player.milky and c.cansee_nips and player.breasts == 1:
        "pc_extra_milksquirt_1"
































    if player.left_hand == "cover_breast":
        "body_armleft_cover_front_base"
    if player.left_hand == "cover_breast":
        "body_armleft_cover_front_shad"
    if acc.nails == 1 and player.left_hand == "cover_breast":
        "polish_left_covered_layered"






    if c.top == 16 and player.left_hand == "cover_breast":
        "shoulderlessruff_larm_above_layer"
    elif c.top == 24 and player.left_hand == "cover_breast":
        "sweater_above_larm"
    elif c.top == 38 and player.left_hand == "cover_breast":
        "perry_larm_above_layerd"
    elif c.top == 39 and player.left_hand == "cover_breast":
        "latextop_larm_above_layer" 


    if c.outfit == 32 and player.left_hand == "cover_breast":
        "latexbody_larm_above_layer"
    elif c.outfit == 36 and player.left_hand == "cover_breast":
        "highleggown_larm_above_layered"
    elif c.outfit == 40 and player.left_hand == "cover_breast":
        "rompersq_larm_above_layer"


    if c.gloves == 1 and player.cover_breasts:
        "fingerless_gloves_l_above_layer"
    elif c.gloves == 2 and player.cover_breasts:
        "sleeve_gloves_l_above_layer"
    elif c.gloves == 3 and player.cover_breasts:
        "server_gloves_l_above_layer"
    elif c.gloves == 4 and player.cover_breasts:
        "rubber_gloves_l_above"
    elif c.gloves == 5 and player.cover_breasts:
        "pads_gloves_l_above_layer"
    elif c.gloves == 6 and player.cover_breasts:
        "cow_gloves_l_above_layer"
    elif c.gloves == 7 and player.cover_breasts:
        "santa_gloves_l_above_layer"


    if c.top == 22 and player.left_hand == "cover_breast":
        "sheerdrop_larm_above_layer"


    if c.coat == 2 and player.left_hand == "cover_breast":
        "cropjump_coat_larm_above_layered"
    elif c.coat == 4 and player.left_hand == "cover_breast":
        "longcoat_larm_above_layer"
    elif c.coat == 7 and player.left_hand == "cover_breast":
        "puff_coat_larm_above_layerd"
    elif c.coat == 9 and player.left_hand == "cover_breast":
        "ziphoodie_coat_larm_above_layerd"
    elif c.coat == 10 and player.left_hand == "cover_breast":
        "crophoodie_larm_above_layerd"
    elif c.coat == 12 and player.left_hand == "cover_breast":
        "onesee_larm_above_layerd"
    elif c.coat == 13 and player.left_hand == "cover_breast":
        "knithoodie_larm_coverabove_layerd"






    if player.left_hand == "brew":
        "pc_body_armleft_brew_above_jar"
    if player.left_hand == "flyer":
        "pc_body_armleft_fliers"
    if player.left_hand == "hat":
        "pc_body_armleft_buskhat"





    if player.right_hand == "umb":
        "body_armright_umb_back"
    elif player.right_hand == "beer" or player.right_hand == "coffee":
        "body_armright_beer_back"
    elif player.cover_vagina:
        "body_armright_cover_back"
    elif player.cover_breasts:
        "body_armright_coverb_back"
    else:
        "body_armright_back"

    if player.right_hand == "umb":
        "body_armright_umb_front"
    elif player.right_hand == "beer" or player.right_hand == "coffee":
        "body_armright_beer_front"
    elif player.cover_vagina:
        "body_armright_cover_front"
    elif player.cover_breasts:
        "body_armright_coverb_front"
    else:
        "body_armright_front"



















    if acc.nails == 1 and player.right_hand == "cover_vag":
        "polish_right_cover_layered"
    elif acc.nails == 1 and player.right_hand == "cover_breast":
        "polish_right_coverb_layered"
    elif acc.nails == 1 and player.right_hand == "":
        "polish_right_layered"





    if c.top == 16:
        "shoulderlessruff_rarm_layer"


    elif c.top == 24:
        "sweater_rarm"
    elif c.top == 31:
        "crophoodie_rarm_layerd"
    elif c.top == 38:
        "perry_rarm_layerd"
    elif c.top == 39:
        "latextop_rarm_layer"

    elif c.outfit == 32:
        "latexbody_rarm_layer"
    elif c.outfit == 36:
        "highleggown_rarm_layerd"
    elif c.outfit == 40:
        "rompersq_rarm_layer"






    if c.gloves == 1:
        "fingerless_gloves_r_layer"
    elif c.gloves == 2:
        "sleeve_gloves_r_layer"
    elif c.gloves == 3:
        "server_gloves_r_layer"
    elif c.gloves == 4:
        "rubber_gloves_r"
    elif c.gloves == 5:
        "pads_gloves_r_layer"
    elif c.gloves == 6:
        "cow_gloves_r_layer"
    elif c.gloves == 7:
        "santa_gloves_r_layer"





    if c.top == 22:
        "sheerdrop_rarm_layer"

    if c.coat == 2:
        "cropjump_coat_rarm_layerd"
    elif c.coat == 4:
        "longcoat_rarm_layer"
    elif c.coat == 7:
        "puff_coat_rarm_layerd"
    elif c.coat == 9:
        "ziphoodie_coat_rarm_layerd"
    elif c.coat == 10:
        "crophoodie_rarm_layerd"
    elif c.coat == 12:
        "onesee_rarm_layerd"
    elif c.coat == 13:
        "knithoodie_rarm_layerd"






    if acc.glasses:
        "pc_glasses_back"





    if player.has_perk(perk_gagged):
        "pc_mask_ballgag_layer"
    elif player.has_perk(perk_gagged_locked):
        "pc_mask_ballgag_red_layer"
    if player.has_perk(perk_blind):
        "pc_misc_blindfold"





    if player.hair_fringe > 0:
        "pc_hair_fringe_layer"





    if acc.glasses:
        "pc_glasses_front"





    if c.hat == 1:
        "flappon_f_b_layered"
    elif c.hat == 2:
        "santa_af_layered"
    elif c.hat == 3:
        "witch_base_layered" anchor (0.0, 0.054)
    elif c.hat == 5:
        "hat_visor_layer"
    elif c.hat == 6:
        "hat_sun_front_layer"

    if c.hat == 1:
        "flappon_f_a_layered"
    elif c.hat == 2:
        "santa_bf_layered"
    elif c.hat == 3:
        "witch_trim_layered" anchor (0.0, 0.054)
    elif c.hat == 9:
        "hat_ghost_layered"





    if player.effect_high == True:
        "pc_face_mood_high"
    if player.tear == 1:
        "pc_face_effect_6"
    if player.rainbow:
        "pc_face_rainbow"

    if player.has_perk(perk_smoking) and player.mouth in (1,8,10, 12) and (t.minute % 3 != 0) and not player.gagged:
        "pc_cig_mouth"
    elif player.right_hand == "umb" and player.has_perk(perk_smoking):
        "pc_cig_umb"
    elif (player.right_hand == "beer" or player.right_hand == "coffee") and player.has_perk(perk_smoking):
        "pc_cig_beer"
    elif player.cover_vagina and player.has_perk(perk_smoking):
        "pc_cig_cover_vag"
    elif player.cover_breasts and player.has_perk(perk_smoking):
        "pc_cig_cover_breast"
    elif player.has_perk(perk_smoking):
        "pc_cig_down"




    if player.right_hand == "umb":
        "pc_body_armright_umb_handle" anchor (0.0, 0.05)
    elif player.right_hand == "beer":
        "pc_body_armright_beer_glass"
    elif player.right_hand == "coffee":
        "pc_body_armright_beer_coffee"
    if player.left_hand == "beer":
        "pc_body_armleft_beer_glass"









layeredimage pc_face:

    always "pc_brows"
    always "pc_mouth"
    always "pc_eyes"

layeredimage pc_mouth:

    if acc.gagged:
        "pc_lipstick_layer"
    elif player.mouth == 1 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_1_layer" 
    elif player.mouth == 2 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_2_layer"
    elif player.mouth == 3 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_3_layer"
    elif player.mouth == 4 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_4_layer"
    elif player.mouth == 5 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_5_layer"
    elif player.mouth == 6 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_6_layer"
    elif player.mouth == 7 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_7_layer"
    elif player.mouth == 8 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_8_layer"
    elif player.mouth == 9 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_9_layer"
    elif player.mouth == 10 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_10_layer"
    elif player.mouth == 11 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_11_layer"
    elif player.mouth == 12 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_12_layer"
    elif player.mouth == 13 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_13_layer"
    elif player.mouth == 14 and acc.lipstick and acc.makeup_on:
        "pc_lipstick_mouth_14_layer"

    if player.gagged:
        "pc_face_mouth_4"
    elif player.mouth == 1:
        "pc_face_mouth_1"
    elif player.mouth == 2:
        "pc_face_mouth_2"
    elif player.mouth == 3:
        "pc_face_mouth_3"
    elif player.mouth == 4:
        "pc_face_mouth_4"
    elif player.mouth == 5:
        "pc_face_mouth_5"
    elif player.mouth == 6:
        "pc_face_mouth_6"
    elif player.mouth == 7:
        "pc_face_mouth_7"
    elif player.mouth == 8:
        "pc_face_mouth_8"
    elif player.mouth == 9:
        "pc_face_mouth_9"
    elif player.mouth == 10:
        "pc_face_mouth_10"
    elif player.mouth == 11:
        "pc_face_mouth_11"
    elif player.mouth == 12:
        "pc_face_mouth_12"
    elif player.mouth == 13:
        "pc_face_mouth_13"
    elif player.mouth == 14:
        "pc_face_mouth_14"

layeredimage pc_eyes:





    if player.eye == 1:
        "pc_face_iris_1_layer"
    elif player.eye == 2:
        "pc_face_iris_2_layer"
    elif player.eye == 5:
        "pc_face_iris_5_layer"
    elif player.eye == 6:
        "pc_face_iris_6_layer"


    if player.eye == 1:
        "pc_face_eye_1"
    elif player.eye == 2:
        "pc_face_eye_2"
    elif player.eye == 5:
        "pc_face_eye_5"
    elif player.eye == 6:
        "pc_face_eye_6"



    if player.eye == 4:
        "pc_face_eyeliner_4_layer"

    elif acc.eyeliner == 1 and player.eye == 1:
        "pc_face_eyeliner_1_1_layer"
    elif acc.eyeliner == 1 and player.eye == 2:
        "pc_face_eyeliner_1_2_layer"
    elif acc.eyeliner == 1 and player.eye == 3:
        "pc_face_eyeliner_1_3_layer"
    elif acc.eyeliner == 1 and player.eye == 5:
        "pc_face_eyeliner_1_5_layer"
    elif acc.eyeliner == 1 and player.eye == 6:
        "pc_face_eyeliner_1_6_layer"

    elif acc.eyeliner == 2 and player.eye == 1:
        "pc_face_eyeliner_2_1_layer"
    elif acc.eyeliner == 2 and player.eye == 2:
        "pc_face_eyeliner_2_2_layer"
    elif acc.eyeliner == 2 and player.eye == 3:
        "pc_face_eyeliner_2_3_layer"
    elif acc.eyeliner == 2 and player.eye == 5:
        "pc_face_eyeliner_2_5_layer"
    elif acc.eyeliner == 2 and player.eye == 6:
        "pc_face_eyeliner_2_6_layer"

    elif acc.eyeliner == 3 and player.eye == 1:
        "pc_face_eyeliner_3_1_layer"
    elif acc.eyeliner == 3 and player.eye == 2:
        "pc_face_eyeliner_3_2_layer"
    elif acc.eyeliner == 3 and player.eye == 3:
        "pc_face_eyeliner_3_3_layer"
    elif acc.eyeliner == 3 and player.eye == 5:
        "pc_face_eyeliner_3_5_layer"
    elif acc.eyeliner == 3 and player.eye == 6:
        "pc_face_eyeliner_3_6_layer"

    elif acc.eyeliner == 4 and player.eye == 1:
        "pc_face_eyeliner_4_1_layer"
    elif acc.eyeliner == 4 and player.eye == 2:
        "pc_face_eyeliner_4_2_layer"
    elif acc.eyeliner == 4 and player.eye == 3:
        "pc_face_eyeliner_4_3_layer"
    elif acc.eyeliner == 4 and player.eye == 5:
        "pc_face_eyeliner_4_5_layer"
    elif acc.eyeliner == 4 and player.eye == 6:
        "pc_face_eyeliner_4_6_layer"

layeredimage pc_brows:


    if player.brow == 1:
        "pc_face_brow_1_layer"
    elif player.brow == 2:
        "pc_face_brow_2_layer"
    elif player.brow == 3:
        "pc_face_brow_3_layer"
    elif player.brow == 4:
        "pc_face_brow_4_layer"

layeredimage pc_breasts:


    if player.breasts == 1 and player.breasts_free:
        "pc_body_breast_base_1_layer"
    elif player.breasts == 2 and player.breasts_free:
        "pc_body_breast_base_2_layer"
    elif player.breasts == 3 and player.breasts_free:
        "pc_body_breast_base_3_layer"

    if player.breasts == 1 and player.breasts_free:
        "pc_body_breast_shad_1_layer"
    elif player.breasts == 2 and player.breasts_free:
        "pc_body_breast_shad_2_layer"
    elif player.breasts == 3 and player.breasts_free:
        "pc_body_breast_shad_3_layer"





    if player.breasts == 1 and player.breasts_lifted:
        "pc_body_breast_c_base_1_layer"
    elif player.breasts == 2 and player.breasts_lifted:
        "pc_body_breast_c_base_2_layer"
    elif player.breasts == 3 and player.breasts_lifted:
        "pc_body_breast_c_base_3_layer"

    if player.breasts == 1 and player.breasts_lifted:
        "pc_body_breast_c_shad_1_layer"
    elif player.breasts == 2 and player.breasts_lifted:
        "pc_body_breast_c_shad_2_layer"
    elif player.breasts == 3 and player.breasts_lifted:
        "pc_body_breast_c_shad_3_layer"




    if player.breasts == 1 and player.breasts_free and player.nip_size == 1:
        "pc_body_nips_1_1_layer"
    elif player.breasts == 1 and player.breasts_free and player.nip_size == 2:
        "pc_body_nips_1_2_layer"
    elif player.breasts == 1 and player.breasts_free and player.nip_size == 3:
        "pc_body_nips_1_3_layer"

    elif player.breasts == 2 and player.breasts_free and player.nip_size == 1:
        "pc_body_nips_2_1_layer"
    elif player.breasts == 2 and player.breasts_free and player.nip_size == 2:
        "pc_body_nips_2_2_layer"
    elif player.breasts == 2 and player.breasts_free and player.nip_size == 3:
        "pc_body_nips_2_3_layer"

    elif player.breasts == 3 and player.breasts_free and player.nip_size == 1:
        "pc_body_nips_3_1_layer"
    elif player.breasts == 3 and player.breasts_free and player.nip_size == 2:
        "pc_body_nips_3_2_layer"
    elif player.breasts == 3 and player.breasts_free and player.nip_size == 3:
        "pc_body_nips_3_3_layer"


    elif player.breasts == 1 and player.nip_size == 1:
        "pc_body_nips_c_1_1_layer"
    elif player.breasts == 1 and player.nip_size == 2:
        "pc_body_nips_c_1_2_layer"
    elif player.breasts == 1 and player.nip_size == 3:
        "pc_body_nips_c_1_3_layer"

    elif player.breasts == 2 and player.nip_size == 1:
        "pc_body_nips_c_2_1_layer"
    elif player.breasts == 2 and player.nip_size == 2:
        "pc_body_nips_c_2_2_layer"
    elif player.breasts == 2 and player.nip_size == 3:
        "pc_body_nips_c_2_3_layer"

    elif player.breasts == 3 and player.nip_size == 1:
        "pc_body_nips_c_3_1_layer"
    elif player.breasts == 3 and player.nip_size == 2:
        "pc_body_nips_c_3_2_layer"
    elif player.breasts == 3 and player.nip_size == 3:
        "pc_body_nips_c_3_3_layer"

    if player.breasts == 1 and player.breasts_free and player.milky:
        "pc_extra_milkleak_1"
    elif player.breasts == 2 and player.breasts_free and player.milky:
        "pc_extra_milkleak_2"
    elif player.breasts == 3 and player.breasts_free and player.milky:
        "pc_extra_milkleak_3"

    elif player.breasts == 1 and player.milky:
        "pc_extra_milkleak_c_1"
    elif player.breasts == 2 and player.milky:
        "pc_extra_milkleak_c_2"
    elif player.breasts == 3 and player.milky:
        "pc_extra_milkleak_c_3"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
