
image bg_school_field_back_layer:
    get_background_filename("school_field_back")





layeredimage bg_school_field_back_robin_stand_layer:
    always "bg_school_field_back_robin_base"
    if robin.heavy_preg:
        "bg_school_field_back_robin_base_2"
    elif robin.showing:
        "bg_school_field_back_robin_base_1"
    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robin_hoodie"

layeredimage bg_school_field_back_robin_bgblow_layer:
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_field_back_bgblow_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_field_back_bgblow_dan"
    else:
        "bg_school_field_back_bgblow_drake"

    always "bg_school_field_back_bgblow_robin_base"
    if robin.showing:
        "bg_school_field_back_bgblow_robin_preg"
    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_bgblow_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_bgblow_robin_hoodie"

layeredimage bg_school_field_back_robin_freeuse_blow_layer:
    always "bg_school_field_back_robinblow_robin_base"
    if robin.showing:
        "bg_school_field_back_robinblow_robin_preg"

    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robinblow_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robinblow_robin_hoodie"

    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_field_back_robinblow_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_field_back_robinblow_dan"
    else:
        "bg_school_field_back_robinblow_drake"

layeredimage bg_school_field_back_robin_freeuse_sex_layer:
    always "bg_school_field_back_robinsex_robin_base"
    if robin.showing:
        "bg_school_field_back_robinsex_robin_preg"

    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robinsex_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_robinsex_robin_hoodie"

    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_field_back_robinsex_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_field_back_robinsex_dan"
    else:
        "bg_school_field_back_robinsex_drake"

layeredimage bg_school_field_back_robin_layer:

    if robin_here() and "soccer_free_use" in robin.list and "soccer_sex_robin" in robin.list and not image_showing("robin") and t.minute > 30:
        "bg_school_field_back_robin_freeuse_blow_layer"
    elif robin_here() and "soccer_free_use" in robin.list and "soccer_sex_robin" in robin.list and not image_showing("robin"):
        "bg_school_field_back_robin_freeuse_sex_layer"
    elif robin_here(loc_school_field_back_isolate) and "soccer_sex_robin" in robin.list and not image_showing("robin") and t.minute > 30: 
        "bg_school_field_back_robin_bgblow_layer"
    elif robin_here() and not image_showing("robin"):
        "bg_school_field_back_robin_stand_layer"

layeredimage bg_school_field_back_rachel_stand_layer:
    always "bg_school_field_back_rachel_base"
    if rachel.heavy_preg:
        "bg_school_field_back_rachel_base_belly"
    if t.timeofday == "day" and rachel.heavy_preg:
        "bg_school_field_back_rachel_casual_2"
    elif t.timeofday == "day":
        "bg_school_field_back_rachel_casual_0"

layeredimage bg_school_field_back_rachel_freeuse_blow_layer:
    always "bg_school_field_back_rachelblow_rachel_base"
    if robin.showing:
        "bg_school_field_back_rachelblow_rachel_preg"

    if t.timeofday == "day" and rachel.showing:
        "bg_school_field_back_rachelblow_rachel_casual_preg"
    elif t.timeofday == "day":
        "bg_school_field_back_rachelblow_rachel_casual"

    if school_soccer_npc_sex_rachel_boy_who() == nate:
        "bg_school_field_back_rachelblow_nate"
    elif school_soccer_npc_sex_rachel_boy_who() == dan:
        "bg_school_field_back_rachelblow_dan"
    else:
        "bg_school_field_back_rachelblow_drake"

layeredimage bg_school_field_back_rachel_freeuse_sex_layer:
    always "bg_school_field_back_rachelsex_rachel_base"
    if robin.showing:
        "bg_school_field_back_rachelsex_rachel_preg"

    if t.timeofday == "day" and rachel.showing:
        "bg_school_field_back_rachelsex_rachel_casual_preg"
    elif t.timeofday == "day":
        "bg_school_field_back_rachelsex_rachel_casual"

    if school_soccer_npc_sex_rachel_boy_who() == nate:
        "bg_school_field_back_rachelsex_nate"
    elif school_soccer_npc_sex_rachel_boy_who() == dan:
        "bg_school_field_back_rachelsex_dan"
    else:
        "bg_school_field_back_rachelsex_drake"

layeredimage bg_school_field_back_rachel_layer:
    if rachel_here() and "soccer_sex_rachel" in rachel.list and not image_showing("rachel") and t.minute in irange(15,40):
        "bg_school_field_back_rachel_freeuse_blow_layer"
    elif rachel_here() and "soccer_sex_rachel" in rachel.list and not image_showing("rachel"):
        "bg_school_field_back_rachel_freeuse_sex_layer"
    elif rachel_here() and not image_showing("rachel"):
        "bg_school_field_back_rachel_stand_layer"

layeredimage bg_school_field_back_mira_layer:
    always "bg_school_field_back_mira_base"
    if mira.heavy_preg:
        "bg_school_field_back_mira_base_belly_2"
    elif mira.showing:
        "bg_school_field_back_mira_base_belly_1"

    if t.hour < 18:
        "bg_school_field_back_mira_casual"
    if t.hour < 18 and mira.heavy_preg:
        "bg_school_field_back_mira_casual_belly_2" 
    elif t.hour < 18 and mira.showing:
        "bg_school_field_back_mira_casual_belly_1"

    if t.hour >= 18:
        "bg_school_field_back_mira_whore"
    if t.hour >= 18 and mira.heavy_preg:
        "bg_school_field_back_mira_whore_belly_2" 
    elif t.hour >= 18 and mira.showing:
        "bg_school_field_back_mira_whore_belly_1"


layeredimage bg_school_field_back_full_layer:
    always:
        "bg_school_field_back_layer"
    if nate_here() and not ("soccer_sex_robin" in nate.list or "soccer_sex_rachel" in nate.list):
        "bg_school_field_back_nate"
    if dan_here() and not ("soccer_sex_robin" in dan.list or "soccer_sex_rachel" in dan.list):
        "bg_school_field_back_dan"
    if drake_here() and not ("soccer_sex_robin" in drake.list or "soccer_sex_rachel" in drake.list):
        "bg_school_field_back_drake"
    if school_soccer_hangingout() and (mira_here() or "soccer_hanging_out" in mira.list):
        "bg_school_field_back_mira_layer"




    always "bg_school_field_back_rachel_layer"
    always "bg_school_field_back_robin_layer"
image bg_school_field_back:
    "bg_school_field_back_full_layer"
    bg_tint_transform()





image bg_school_field_back_isolate_layer:
    get_background_filename("school_field_back_isolate")

layeredimage bg_school_field_back_isolate_blowjob:
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_field_back_isolate_standblow_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_field_back_isolate_standblow_dan"
    else:
        "bg_school_field_back_isolate_standblow_drake"
    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_isolate_standblow_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_isolate_standblow_robin_hoodie"

layeredimage bg_school_field_back_isolate_sex:
    always "bg_school_field_back_isolate_againstwall_robin_base"
    if robin.showing:
        "bg_school_field_back_isolate_againstwall_robin_preg"
    if (global_random_number % 2) and (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_isolate_againstwall_robin_baggy"
    elif (not "naked_for_boys" in robin.list or t.timeofday == "day"):
        "bg_school_field_back_isolate_againstwall_robin_hoodie"

    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_field_back_isolate_againstwall_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_field_back_isolate_againstwall_dan"
    else:
        "bg_school_field_back_isolate_againstwall_drake"


layeredimage bg_school_field_back_isolate_full:
    always "bg_school_field_back_isolate_layer"
    if robin_here() and "soccer_sex_robin" in robin.list and not image_showing("robin") and t.minute > 30: 
        "bg_school_field_back_isolate_blowjob"
    elif robin_here() and "soccer_sex_robin" in robin.list and not image_showing("robin"):
        "bg_school_field_back_isolate_sex"

image bg_school_field_back_isolate:
    "bg_school_field_back_isolate_full"
    bg_tint_transform()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
