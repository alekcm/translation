init python:
    def shop_open(what_inv):
        _window_hide(auto=True)
        wardrobe_copy_tab(tab_top, "shop")  
        tab_clothes("shop")
        renpy.call_screen("wardrobe_screen", what_inv=what_inv, shop=True, shop_return=True)
        tab_top_enter = tab_top

    def shops_create_list():
        global shop_list
        shop_list = []
        for obj in gc.get_objects():
            if isinstance(obj, Inventory):
                if obj.shop_list:
                    add_to_list(shop_list, obj)

    def shops_restock():
        if t.wkday in ("Wednesday", "Saturday"):
            for i in shop_list:  
                i.stock()


default shop_list = []

label shops_call:
    $ shop_list = []





    $ shop_pub = Inventory("Pub stockroom")
    $ shop_pub.shop_list = [[item_outfit_6, 3], [item_socks_7, 4], [item_pants_6, 10]]
    $ shop_pub.stock()


    $ shop_needle = Inventory("Needle girls stall")
    $ shop_needle.shop_list = [
    [item_outfit_2, 3], 

    [item_top_8, 4], 
    [item_top_12, 10],

    [item_bottom_4, 4], 
    [item_bottom_5, 10],
    [item_bottom_8, 5],

    ]

    $ shop_needle.stock()


    $ add_to_list(lake_dealer.inv.shop_list, [ 
    [item_tissue, 50], 
    [item_beer, 20], 
    [item_joy, 10], 
    [item_lebo, 6], 
    [item_wakeup, 2], 
    [item_map_pill, 6],
    [item_abort_pill, 2],
    [item_pepperspray, 1], 
    [item_poison, 1],
    [item_chis, 1],
    [item_bruisecream, 2],
    ])
    $ lake_dealer.inv.stock()


    $ shop_funwear = Inventory("Funwear")
    python:
        for i in item_clothes_list:
            if not "swim" in i.outfit and (i.slutty or i.braless or i.thong):
                shop_funwear.shop_list.append(i)
    $ shop_funwear.stock(50)


    $ shop_piercings = Inventory("Piercing's and accessories")

    $ add_to_list(shop_piercings.shop_list, [ 
    [item_tissue, 50], 
    [item_felt_marker, 1], 
    [item_perm_marker, 1], 
    [item_nipring_1, 1], 
    [item_navelring_1, 1], 

    [item_choker_1, 1], 
    [item_glasses_6, 1],
    [item_bdsm, 1],
    [item_pants_11, 1], 
    ])
    $ shop_piercings.stock()


    python:
        for i in item_clothes_list:
            if "swim" in i.outfit:
                sandy.inv.shop_list.append(i)
    $ add_to_list(sandy.inv.shop_list, [item_glasses_2, item_glasses_3])
    $ sandy.inv.stock()


    $ shop_corner = Inventory("Corner shop")

    $ add_to_list(shop_corner.shop_list, [ 
    [item_tissue, 100], 
    [item_cigs, 40], 
    [item_beer, 10], 
    [item_energydrink, 3], 
    [item_energyfood, 7],
    [item_preg_test, 3], 
    [item_razor, 3], 
    [item_bruisecream, 1],
    [item_tape, 1], 
    [item_mag_ent, 2], 
    ])
    $ shop_corner.stock()


    $ ashon.inv.shop_list = [
    item_alarm, 
    [item_preg_test, 6], 
    [item_tape, 2],
    [item_tissue, 50], 
    item_saw,]
    $ ashon.inv.stock()


    $ jaylee.inv.shop_list = [
    [item_mag_ent, 2], 
    [item_mag_porn, 2], 
    item_nipring_1, 
    item_navelring_1, 
    item_buttplug, 
    item_choker_2, 
    item_glasses_5, 
    [item_map_pill, 3], 
    item_abort_pill,
    [item_tissue, 50], 
    ]
    $ jaylee.inv.stock(80)


    $ felix.inv.shop_list = [
    item_polaroid_camera,
    [item_polaroid_blank, 20], 
    ]
    $ felix.inv.stock()


    $ shop_motel = Inventory("Motel shop")

    $ add_to_list(shop_motel.shop_list, [ 
    [item_hat_8, 2], 
    [item_outfit_20, 2], 
    [item_pants_13, 4], 
    [item_socks_14, 2], 
    [item_energydrink, 3], 
    [item_energyfood, 7],
    [item_preg_test, 3], 
    [item_razor, 3], 
    [item_bruisecream, 5],
    [item_lebo, 6],
    [item_mag_porn, 4],
    [item_tissue, 50], 
    ])
    $ shop_motel.stock()


    $ shop_milk = Inventory("Milk farm")

    $ add_to_list(shop_milk.shop_list, [ 
    item_breastpump, 
    [item_milkbottle_empty, 25], 
    [item_milktab, 4], 

    item_hat_10, 
    item_choker_5, 
    item_bra_13, 
    item_pants_16, 
    item_gloves_6, 
    item_socks_20, 
    ])
    $ shop_milk.stock()


    $ havenvik.inv.shop_list = [
    [item_beer, 30],
    [item_brew, 100], 
    [item_winebottle, 2],
    [item_cigs, 100],
    [item_joy, 5],
    [item_lebo, 1], 
    [item_abort_pill, 2],
    item_pepperspray, 
    ]
    $ havenvik.inv.stock()


    $ stall_clothes_random = Inventory("Market stall")
    $ stall_clothes_random.shop_list = item_clothes_list
    $ stall_clothes_random.stock(5)

    $ stall_items_random = Inventory("Market stall")
    $ stall_items_random.shop_list = [[item_preg_test, 3], [item_cigs, 100], [item_razor, 3], [item_bruisecream, 2], [item_perm_marker, 2], [item_felt_marker, 3], [item_nailpolish, 1],
    [item_hairdye, 1], [item_contacts, 1], [item_alarm, 1], [item_tape, 5], [item_tissue, 50], 
    ]
    $ stall_items_random.stock(20)

    $ stall_booze_random = Inventory("Market stall")
    $ stall_booze_random.shop_list = [[item_cigs, 100], [item_beer, 3], [item_winebottle, 1], [item_energydrink, 3], [item_mag_ent, 2],
    [item_mag_porn, 5] 
    ]
    $ stall_booze_random.stock(20)

    $ stall_junk_seller = Inventory("Market stall")





    $ shop_item_test = Inventory()
    python:
        for i in item_list:
            if i.stackable:
                shop_item_test.take(i, 20)
            else:
                shop_item_test.take(i, 1)


    $ shop_test = Inventory()
    $ shop_test.shop_list = item_clothes_list
    $ shop_test.stock()







    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
