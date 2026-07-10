

screen school_shop:
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.095
        xsize 970
        ysize 100
        has vbox
        hbox:
            text "SCHOOL SPIRIT"
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
            imagebutton auto "button_wardrobe_outfit_%s" action SetVariable ("tab_left_shop", "jacket")
            imagebutton auto "button_wardrobe_top_%s" action SetVariable ("tab_left_shop", "top")
            imagebutton auto "button_wardrobe_bottom_%s" action SetVariable ("tab_left_shop", "bottom")
            imagebutton auto "button_wardrobe_socks_%s" action SetVariable ("tab_left_shop", "socks")
        hbox:
            box_wrap True
            if tab_left_shop == "jacket":

                if not 1 in owned_jacket:
                    imagebutton auto "wardrobe/clothes/wardrobe_jacket_cardigan_%s.png":
                        action If (player.cash >= jacket_cardigan_cost, [Function (add_wardrobe, owned_jacket, 1), Hide("shop_text"), Function(player.remove_money, jacket_cardigan_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=jacket_cardigan_name, text_cost=jacket_cardigan_cost, text_desc=jacket_cardigan_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 1)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
            elif tab_left_shop == "top":
                if not 4 in owned_top:
                    imagebutton auto "wardrobe/clothes/wardrobe_top_shirtruf_%s.png":
                        action If (player.cash >= top_schshirt_cost, [Function (add_wardrobe, owned_top, 4), Hide("shop_text"), Function(player.remove_money, top_schshirt_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=top_schshirt_name, text_cost=top_schshirt_cost, text_desc=top_schshirt_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 4)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
            elif tab_left_shop == "bottom":
                if not 1 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_jeans1_%s.png":
                        action If (player.cash >= bottom_jeans1_cost, [Function (add_wardrobe, owned_bottom, 1), Hide("shop_text"), Function(player.remove_money, bottom_jeans1_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_jeans1_name, text_cost=bottom_jeans1_cost, text_desc=bottom_jeans1_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 1)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 5 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_schskirt_%s.png":
                        action If (player.cash >= bottom_schskirt_cost, [Function (add_wardrobe, owned_bottom, 5), Hide("shop_text"), Function(player.remove_money, bottom_schskirt_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_schskirt_name, text_cost=bottom_schskirt_cost, text_desc=bottom_schskirt_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 5)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 12 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_pencilskirt_%s.webp":
                        action If (player.cash >= bottom_pencilskirt_cost, [Function (add_wardrobe, owned_bottom, 12), Hide("shop_text"), Function(player.remove_money, bottom_pencilskirt_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_pencilskirt_name, text_cost=bottom_pencilskirt_cost, text_desc=bottom_pencilskirt_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 12)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
            elif tab_left_shop == "socks":
                if not 5 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_thigh1a_%s.png":
                        action If (player.cash >= socks_thigh1a_cost, [Function (add_wardrobe, owned_socks, 5), Hide("shop_text"), Function(player.remove_money, socks_thigh1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_thigh1a_name, text_cost=socks_thigh1a_cost, text_desc=socks_thigh1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 5)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]




    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.81
        yalign 0.095
        xsize 330
        ysize 900
    imagebutton auto "poi_return_%s" action [Hide("school_shop"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
