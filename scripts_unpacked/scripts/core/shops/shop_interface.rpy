init python:

    def shop_clothes_button(num):
        global tab_top_shop, tab_left_shop, tab_top
        renpy.ui.imagebutton(auto=("wardrobe_clothes_frame_%s"),
        action=If (player.cash >= formattext_shop(num)[2],
        [Function (add_wardrobe, shop_main_button()[1], num), Function(shop_get_backup), Function(pc_dress), Hide("shop_text"), Function(player.remove_money, formattext_shop(num)[2])],
        Show("no_money")),
        hovered=[Show("shop_text", text_title=formattext_shop(num)[0], text_cost=formattext_shop(num)[2], text_desc=formattext_shop(num)[1]), Function(tab_clothes, "shop", shop), Function(pc_strip), Function(clothes_set, shop, tab_left_shop, num)],
        unhovered=[Hide("shop_text"), Function(shop_get_backup), Function(pc_dress)])

    def shop_set_backup():
        global tab_top_backup, tab_top
        tab_top_backup = tab_top
    def shop_get_backup():
        global tab_top_backup, tab_top
        
        if tab_top_backup == "school":
            tab_clothes("school", school)
        elif tab_top_backup == "daily":
            tab_clothes("daily", daily)
        elif tab_top_backup == "party":
            tab_clothes("party", party)
        elif tab_top_backup == "sport":
            tab_clothes("sport", sport)
        elif tab_top_backup == "swim":
            tab_clothes("swim", swim)
        elif tab_top_backup == "home":
            tab_clothes("home", home)
        else:
            tab_clothes("daily", daily)

    def shop_main_button():
        if tab_left_shop == "hat":
            return (list_hat, owned_hat)
        elif tab_left_shop == "jacket":
            return (list_jacket, owned_jacket)
        elif tab_left_shop == "outfit":
            return (list_outfit, owned_outfit)
        elif tab_left_shop == "top":
            return (list_top, owned_top)
        elif tab_left_shop == "bottom":
            return (list_bottom, owned_bottom)
        elif tab_left_shop == "bra":
            return (list_bra, owned_bra)
        elif tab_left_shop == "pants":
            return (list_pants, owned_pants)
        elif tab_left_shop == "socks":
            return (list_socks, owned_socks)
        elif tab_left_shop == "gloves":
            return (list_gloves, owned_gloves)

    def shop_set_colour_button_hover(colour, is_primary):
        if is_primary:
            suffix = "primary"
        else:
            suffix = "secondary"
        
        image_name = "wardrobe/button_wardrobe_colour_frame_%s.webp"
        
        renpy.ui.imagebutton(auto=(image_name), action=[SetVariable (( suffix + "_colour"), colour), SetVariable ((tab_top + "." + tab_left + "_" + suffix + "_colour"), colour), SetVariable (("c." + tab_left + "_" + suffix + "_colour"), colour)])

screen shop_interface(what_inv):

    $ inv_type_list = []
    for i in what_inv.inv:
        $ add_to_list(inv_type_list, getattr(i[0], type))

    frame anchor (0,0) align (0.3,0.095) xysize (970,100):
        has vbox
        hbox:
            text what_inv.name.upper()
        hbox:
            text "COST:" size 35
    frame anchor (0,0) align (0.3,0.19) xysize (970,800):
        has hbox
        vbox:
            for i in inv_type_list:

                frame padding (0,0) xysize (82,80):
                    add "button_wardrobe_tab_bg"
                    add "button_wardrobe_tab_" + i:
                        if tab_left_shop != i:
                            matrixcolor TintMatrix(colour_selected)
                    imagebutton auto "button_wardrobe_tab_frame_%s" action SetVariable ("tab_left_shop", i)

    frame:
        anchor (0,0) align (0.81,0.095) xysize (330,900)

    imagebutton auto "poi_return_%s" action [Hide("shop_interface"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
