
layeredimage bg_school_locker_robin_bench_blowjob:
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_locker_benchblow_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_locker_benchblow_dan"
    else:
        "bg_school_locker_benchblow_drake"
    if (global_random_number % 2):
        "bg_school_locker_benchblow_robin_baggy"
    else:
        "bg_school_locker_benchblow_robin_hoodie"
layeredimage bg_school_locker_robin_stand_blowjob:
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_locker_standblow_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_locker_standblow_dan"
    else:
        "bg_school_locker_standblow_drake"
    if (global_random_number % 2):
        "bg_school_locker_standblow_robin_baggy"
    else:
        "bg_school_locker_standblow_robin_hoodie"
layeredimage bg_school_locker_robin_bench_sex:
    always "bg_school_locker_benchsex_robin"
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_locker_benchsex_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_locker_benchsex_dan"
    else:
        "bg_school_locker_benchsex_drake"
layeredimage bg_school_locker_robin_stand_sex:
    always "bg_school_locker_standsex_robin"
    if school_soccer_npc_sex_robin_boy_who() == nate:
        "bg_school_locker_standsex_nate"
    elif school_soccer_npc_sex_robin_boy_who() == dan:
        "bg_school_locker_standsex_dan"
    else:
        "bg_school_locker_standsex_drake"


layeredimage bg_school_locker_robin_sex:
    if t.minute > 30 and (t.day % 2 == 0): 
        "bg_school_locker_robin_bench_blowjob"
    elif t.minute > 30:
        "bg_school_locker_robin_stand_blowjob"
    elif not t.minute > 30 and (t.day % 2 == 0): 
        "bg_school_locker_robin_bench_sex"
    else:
        "bg_school_locker_robin_stand_sex"


layeredimage bg_school_locker_old:
    always "bg_school_locker_old_scene"
    if robin_here() and "soccer_sex_robin" in robin.list and not image_showing("robin"): 
        "bg_school_locker_robin_sex"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
