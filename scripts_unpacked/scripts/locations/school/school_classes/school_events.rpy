label dis_school_closed:
    if any(clothes in ["swim", "temp_outfit"] for clothes in tab_top) or c.inappropriate:
        pc "They will be closing soon so I had better get changed before I leave."
        $ pc_dress_event("party", loc_school_locker_girls, loc_school)
    else:
        pc "Looks like they are starting to close the school so I had better leave."
        $ walk(loc_school)
    jump travel

label school_class_absent:
    pc "I am too late for classes and can't really use the school facilities while classes are going on."
    pc "I'll have to come back tomorrow."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
