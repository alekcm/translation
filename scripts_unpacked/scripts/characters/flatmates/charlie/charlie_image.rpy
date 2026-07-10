layeredimage charlie_outfit_standard:
    always "charlie_glasses"
    if dis(dis_school) or (t.wkday in weekdays and t.hour in school_hours):
        "charlie_outfit_uni"
    elif dis(dis_home):
        "charlie_outfit_sport" 
    else:
        "charlie_outfit_casual"

layeredimage charlie:
    at sprite_highlight("charlie")
    always "charlie_base"

    group outfit auto:
        attribute standard default
        attribute nude:
            null

    always:
        if_any ["dress"] "charlie_makeup"
    always:
        if_not ["dress"] "charlie_glasses"
    group face auto:
        attribute neutral default

    group hair auto:
        attribute 1 default if_not ["dress"]
        attribute 2 default if_any ["dress"]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
