init python:
    def cheat_clothes():
        for i in item_clothes_list:  
            if not wardrobe.qty(i): 
                wardrobe.take(i)

    def cheat_clothes_shoptest():
        for i in item_clothes_list:
            if not shop_test.qty(i): 
                shop_test.take(i)

    def cheat_unrestrict_wardrobe():
        global wardrobe_restricted
        wardrobe_restricted = not wardrobe_restricted

    def cheat_pass_time_slow(amount=1):
        t.minute = amount 

label item_debug_shop_label:
    call screen inventory_itemshop_screen(shop_item_test)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
