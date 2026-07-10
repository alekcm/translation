init python:
    def ashon_here(location=None, where=False, class_loc=False):
        if location == None:
            location = loc_cur
        cur_location = None
        
        if not ashon.isactive:
            cur_location = None
        elif t.hour in workhours: 
            cur_location = loc_junk_office
        
        if class_loc:
            return cur_location
        return npc_here_check(location, cur_location, where)

label junkyard_ash_sell:
    if not ashon.has_met:
        jump loc_junk_office_visit
    show ashon at right1 with dissolve
    if ashon.inv.value_junk() > 50 and not "shop_open" in ashon.conversation_topics:
        ashon.name "Hey [name]. Got some stuff refurbished you might wanna buy. Come have a look."
        $ add_to_list(ashon.conversation_topics, "shop_open")
        if not ashon.inv.shop_list:
            $ ashon.inv.shop_list = [item_alarm, [item_preg_test, 6], [item_tape, 2], item_saw]
            $ ashon.inv.stock()
        pc "Oh? What you got?"
        ashon.name "Have a look."
        call screen inventory_itemshop_screen(ashon.inv)
        ashon.name "Just mostly scraps for now, but should hopefully sell more stuff if you bring me more scrap."
        jump travel
    if ashon.inv.value_junk() > 10:
        ashon.name "Hey [name]. Got something for me?"
    else:
        ashon.name "What you got for me?"
    call screen inventory_junk_choice(ashon.inv, choices=[item_scrap_ele, item_scrap_junk, item_scrap_metal])
    ashon.name "Come back if you pick up anything else."
    hide ashon with dissolve
    jump travel

label junkyard_ash_shop:
    show ashon at right1 with dissolve
    pc "What you got to sell [ashon.nname]?"
    ashon.name "Have a look."
    call screen inventory_itemshop_screen(ashon.inv)
    ashon.name "Come back if you need something else."
    hide ashon with dissolve
    jump travel

label junkyard_ash_loiter:
    "I hang about killing time for a bit and having the odd chat with [ashon.name]."
    $ loiter(who=ashon)
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
