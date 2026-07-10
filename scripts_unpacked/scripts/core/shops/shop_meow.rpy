


screen meow_shop:
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.095
        xsize 970
        ysize 100
        has vbox
        hbox:
            text "MEOW"
        hbox:
            text "COST:" size 35
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.19
        xsize 970
        ysize 800


        has hbox

        vbox:

            imagebutton auto "button_wardrobe_hat_%s" action SetVariable ("tab_left_shop", "hat")
            imagebutton auto "button_wardrobe_outfit_%s" action SetVariable ("tab_left_shop", "outfit")
            imagebutton auto "button_wardrobe_top_%s" action SetVariable ("tab_left_shop", "top")
            imagebutton auto "button_wardrobe_bottom_%s" action SetVariable ("tab_left_shop", "bottom")
            imagebutton auto "button_wardrobe_bra_%s" action SetVariable ("tab_left_shop", "bra")
            imagebutton auto "button_wardrobe_pants_%s" action SetVariable ("tab_left_shop", "pants")
            imagebutton auto "button_wardrobe_socks_%s" action SetVariable ("tab_left_shop", "socks")
        hbox:
            box_wrap True

            if tab_left_shop == "hat":
                for i in list_hat:
                    if "meow" in get_outfit_shop(i) and not i in owned_hat:
                        imagebutton auto "wardrobe_hat_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "outfit":
                for i in list_outfit:
                    if "meow" in get_outfit_shop(i) and not i in owned_outfit:
                        imagebutton auto "wardrobe_outfit_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "top":
                for i in list_top:
                    if "meow" in get_outfit_shop(i) and not i in owned_top:
                        imagebutton auto "wardrobe_top_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "bottom":
                for i in list_bottom:
                    if "meow" in get_outfit_shop(i) and not i in owned_bottom:
                        imagebutton auto "wardrobe_bottom_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "bra":
                for i in list_bra:
                    if "meow" in get_outfit_shop(i) and not i in owned_bra:
                        imagebutton auto "wardrobe_bra_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "pants":
                for i in list_pants:
                    if "meow" in get_outfit_shop(i) and not i in owned_pants:
                        imagebutton auto "wardrobe_pants_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "socks":
                for i in list_socks:
                    if "meow" in get_outfit_shop(i) and not i in owned_socks:
                        imagebutton auto "wardrobe_socks_" + str(i) + "_%s":
                            action If (player.cash >= formattext_shop(i)[2], [Function (add_wardrobe, owned_top, i), Hide("shop_text"), Function(player.remove_money, formattext_shop(i)[2]), Function(pc_dress)], Show("no_money"))
                            hovered [Show("shop_text", text_title=formattext_shop(i)[0], text_cost=formattext_shop(i)[2], text_desc=formattext_shop(i)[1]), Function(pc_strip), SetVariable ("c." + tab_left_shop, i)]
                            unhovered [Hide("shop_text"), Function(pc_dress)]


    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.81
        yalign 0.095
        xsize 330
        ysize 900
    imagebutton auto "poi_return_%s" action [Hide("meow_shop"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
