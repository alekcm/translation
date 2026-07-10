layeredimage bg_school_toilet_girls:
    always "bg_school_toilet_girls_base"
    if rachel_here(loc_school_toilet_girls) and rachel.showing and not renpy.showing("rachel"):
        "bg_toilet_girls_people_rachel_preg"
    elif rachel_here(loc_school_toilet_girls) and not renpy.showing("rachel"):
        "bg_toilet_girls_people_rachel"
    if t.wkday in weekdays and t.hour in school_hours and t.minute in irange(10, 20):
        "bg_toilet_girls_people_lipstick"
    if t.wkday in weekdays and t.hour in school_hours and (t.minute in irange(5, 15) or t.minute in irange(40, 50)) and girl_dummy_3.showing:
        "bg_toilet_girls_people_smoke_preg"
    elif t.wkday in weekdays and t.hour in school_hours and (t.minute in irange(5, 15) or t.minute in irange(40, 50)):
        "bg_toilet_girls_people_smoke"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
