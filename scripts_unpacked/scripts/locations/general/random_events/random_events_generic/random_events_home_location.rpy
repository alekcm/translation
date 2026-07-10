label random_event_picker_home_location_tombola:
    jump expression WeightedChoice([
    
    ("robin_talk_sexobject_bedroom_thoughts", If (log.interactive("quest_robinslut_01") and not "sexobject_clothes_bedroom_thoughts" in robin.list, 100, 0)), 

    ("main_quest_03_fixer_home", If (main_quest_03.active == 1 and main_quest_03.stage == 2, 100, 0)),

    ("travel_dis", 1),
    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
