layeredimage bg_school_hallway_people:
    if t.wkday in weekdays and t.hour in (8,9,13,14,15) and calander_holiday == "":
        "bg_school_hallway_people_talk"
    if t.wkday in weekdays and t.hour in (8,9,13,14,15) and calander_holiday == "" and girl_dummy_1.showing:
        "bg_school_hallway_people_talk_preg"
    if t.wkday in weekdays and t.hour in (13,14,15,16,17) and calander_holiday == "":
        "bg_school_hallway_people_girl_walk"
    if t.wkday in weekdays and t.hour in (13,14,15,16,17) and calander_holiday == "" and girl_dummy_2.showing:
        "bg_school_hallway_people_girl_walk_preg"
    if t.wkday in weekdays and t.hour in (8,9,10,11,12,13) and calander_holiday == "":
        "bg_school_hallway_people_girl_locker"
    if t.wkday in weekdays and t.hour in (8,9,10,11,12,13) and calander_holiday == "" and girl_dummy_3.showing:
        "bg_school_hallway_people_girl_locker_preg"
    if t.wkday in weekdays and t.hour in workhours and calander_holiday == "":
        "bg_school_hallway_people_girl_far"
    if t.wkday in weekdays and t.hour in workhours and calander_holiday == "" and girl_dummy_4.showing:
        "bg_school_hallway_people_girl_far_preg"
    if t.wkday in weekdays and t.hour in (8,9,13,14,15,17,18) and calander_holiday == "":
        "bg_school_hallway_people_boy_walk"
    if t.wkday in weekdays and t.hour in (8,9,13,14,15,17,18) and calander_holiday == "":
        "bg_school_hallway_people_boy_locker"
    if robin_here() and not renpy.showing("robin"):
        "bg_school_hallway_people_robin"
    if robin_here() and robin.days_pregnant > (global_pregnancy_length * 0.75) and not renpy.showing("robin"): 
        "bg_school_hallway_people_robin_preg2"
    elif robin_here() and robin.days_pregnant > (global_pregnancy_length * 0.3) and not renpy.showing("robin"): 
        "bg_school_hallway_people_robin_preg1"

layeredimage bg_school_hallway:
    always "bg_school_hallway_scene"
    always "bg_school_hallway_people"

layeredimage bg_school_hallway_2f:
    always "bg_school_hallway_2f_scene"
    if dani_here() and not renpy.showing("dani"):
        "bg_school_hallway_2f_people_dani_base"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
