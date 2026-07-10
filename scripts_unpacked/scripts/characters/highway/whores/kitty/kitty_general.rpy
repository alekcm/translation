init python:
    def anita_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if t.time_from_to(12.00, 02.00):
            if kitty.hour_number in (0,1,2):
                cur_location = loc_highway
            elif kitty.hour_number  in (3,4,5):
                cur_location = loc_motel
            elif kitty.hour_number  in (6,7,8):
                cur_location = loc_truckstop
            else:
                cur_location = loc_highway_slum
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

    def kitty_here(location=None, where=False, class_loc=False):
        return anita_here(location, where, class_loc)

layeredimage kitty:
    at sprite_highlight("kitty")
    always "whore_3_base"
    if kitty.heavy_preg:
        "whore_3_belly_2"
    elif kitty.showing:
        "whore_3_belly_1"

label kitty_talk_picker:


    if not "kitty_meet_chain" in kitty.dict:
        $ kitty.dict["kitty_meet_chain"] = 0


    show kitty at right1 with dissolve

    jump expression WeightedChoice([

    ("kitty_talk_subject", 20),

    
    ("kitty_talk_haven_thanks", If(log.completed("Haven") and not "haven_thanks" in kitty.list, 5000, 0)),
    ("kitty_meet_chain_" + str(kitty.dict["kitty_meet_chain"]), If(renpy.has_label("kitty_meet_chain_" + str(kitty.dict["kitty_meet_chain"])) and not log.interactive("quest_whore_01"), 500, 0)),

    ])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
