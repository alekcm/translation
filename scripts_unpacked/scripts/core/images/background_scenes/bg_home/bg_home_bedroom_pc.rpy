image bg_bedroom:
    "bg_bedroom_scene"
    bg_tint_transform(True)

layeredimage bg_bedroom_scene:
    always "bg_bedroom_base"
    if not t.timeofday == "day":
        "bg_bedroom_curtan"
    if t.timeofday == "day" and weather_var == 1:
        "bg_bedroom_sunny"

    if t.day < 7:
        "bg_bedroom_dirty"
    else:
        "bg_bedroom_elements"

layeredimage bg_bedroom_dirty:
    always "bg_bedroom_dirty_1"
    if t.day < 4:
        "bg_bedroom_dirty_2"

layeredimage bg_bedroom_elements:
    always "bg_bedroom_posters"


    if quest_flyers.timesworked > 5:
        "bg_bedroom_detail_jobs_flyers"

    always "bg_bedroom_clothes"
    always "bg_bedroom_items"
    always "bg_bedroom_jobs"
    always "bg_bedroom_diary"

layeredimage bg_bedroom_posters:
    if quest_homeless.active or quest_homeless_start.active:
        "bg_bedroom_detail_poster_homeless"
    if quest_nudevball.isactive():
        "bg_bedroom_detail_poster_nudevball"
    if robin.isslut:
        "bg_bedroom_detail_poster_robinmeme"
    if robin.love >= 100 and emile.love >= 100:
        "bg_bedroom_detail_poster_robinemile"
    if quest_exhib.iscomplete():
        "bg_bedroom_detail_poster_exhib"
    if dani.love >= 100:
        "bg_bedroom_detail_poster_danidance"
    if player.has_perk(perk_freeuse):
        "bg_bedroom_detail_poster_freeuse"
    if cass.iswhore:
        "bg_bedroom_detail_poster_savingmira"
    if "park_bitch_intro" in robin.list and "can_bitch" in rachel.list:
        "bg_bedroom_detail_poster_bitching"
    if log.interactive("quest_dancevip_04"):
        "bg_bedroom_detail_poster_dancegirlsall"
    if player.has_perk(perk_whore):
        "bg_bedroom_detail_poster_whore"



layeredimage bg_bedroom_clothes:
    if len(wardrobe.inv) > 10:
        "bg_bedroom_detail_clothes_general"
    if len(wardrobe.inv) > 25:
        "bg_bedroom_detail_clothes_wardrobe"
    if len(wardrobe.inv) > 35:
        "bg_bedroom_detail_clothes_drawers"
    if len(wardrobe.inv) > 45:
        "bg_bedroom_detail_clothes_cupboard"
    if len(wardrobe.inv) > 60:
        "bg_bedroom_detail_clothes_floor"

layeredimage bg_bedroom_items:
    if player.has_perk(perk_alcoholic):
        "bg_bedroom_detail_items_booze"
    if player.has_perk(perk_smoker):
        "bg_bedroom_detail_items_ashtray"
    if inv.qty(item_buttplug) and not player.has_perk(perk_buttplug):
        "bg_bedroom_detail_items_buttplug"
    if inv.qty(item_ballgag) and not player.gagged:
        "bg_bedroom_detail_items_gag"
    if inv.qty(item_scrap_milkbottle) and player.lactating:
        "bg_bedroom_detail_items_milk"
    if any([inv.qty(item_chis), inv.qty(item_saw)]):
        "bg_bedroom_detail_items_tools"
    if wardrobe.qty(item_choker_6) and not acc.choker == 6:
        "bg_bedroom_detail_items_bitch"

layeredimage bg_bedroom_jobs:
    if quest_scav.active:
        "bg_bedroom_detail_jobs_scavving"

    if pub_waitress.timesworked > 5:
        "bg_bedroom_detail_jobs_bar"
    if school_dance_quest_show_count >= 3:
        "bg_bedroom_detail_jobs_dance"

layeredimage bg_bedroom_diary:
    if player.male_origin and not player.has_perk(perk_male):
        "bg_bedroom_detail_diary_formerman"
    if quest_mira_missing.active:
        "bg_bedroom_detail_diary_miramissing"
    if mira.dead:
        "bg_bedroom_detail_diary_miradead"
    if main_quest_04.active:
        "bg_bedroom_detail_diary_havenprep"
    if main_quest_05.iscomplete():
        "bg_bedroom_detail_diary_haven"
    if main_quest_02.active:
        "bg_bedroom_detail_diary_cosmetic"
    if log.completed("mq_01_b"):
        "bg_bedroom_detail_diary_simon"
    if player.pregbabies:
        "bg_bedroom_detail_diary_baby"
    if player.asex:
        "bg_bedroom_detail_diary_buttsex"
    if player.vsex:
        "bg_bedroom_detail_diary_sex"
    if player.preg_amount:
        "bg_bedroom_detail_diary_preg"
    if player.sold:
        "bg_bedroom_detail_diary_sold"
    if quest_gloryhole_create.iscomplete():
        "bg_bedroom_detail_diary_glory"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
