

screen cosplay_shop:
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.095
        xsize 970
        ysize 100
        has vbox
        hbox:
            text "COSPLAY CLUB"
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
            imagebutton auto "button_wardrobe_socks_%s" action SetVariable ("tab_left_shop", "socks")
        hbox:
            box_wrap True
            if tab_left_shop == "hat":

                if not 2 in owned_hat:
                    imagebutton auto "wardrobe_hat_2_%s":
                        action If (player.cash >= hat_2_cost, [Function (add_wardrobe, owned_hat, 2), Hide("shop_text"), Function(player.remove_money, hat_2_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=hat_2_name, text_cost=hat_2_cost, text_desc=hat_2_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 2)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "outfit":
                if not 10 in owned_outfit:
                    imagebutton auto "wardrobe_outfit_10_%s":
                        action If (player.cash >= outfit_10_cost, [Function (add_wardrobe, owned_outfit, 10), Hide("shop_text"), Function(player.remove_money, outfit_10_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=outfit_10_name, text_cost=outfit_10_cost, text_desc=outfit_10_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 10)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "socks":
                if not 14 in owned_socks:
                    imagebutton auto "wardrobe_socks_14_%s":
                        action If (player.cash >= socks_14_cost, [Function (add_wardrobe, owned_socks, 14), Hide("shop_text"), Function(player.remove_money, socks_14_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_14_name, text_cost=socks_14_cost, text_desc=socks_14_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 14)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]




    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.81
        yalign 0.095
        xsize 330
        ysize 900
    imagebutton auto "poi_return_%s" action [Hide("cosplay_shop"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
