


screen underwear_shop:
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

            imagebutton auto "button_wardrobe_bra_%s" action SetVariable ("tab_left_shop", "bra")
            imagebutton auto "button_wardrobe_pants_%s" action SetVariable ("tab_left_shop", "pants")
            imagebutton auto "button_wardrobe_socks_%s" action SetVariable ("tab_left_shop", "socks")
        hbox:
            box_wrap True

            if tab_left_shop == "bra":
                if not 1 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_fcup1a_%s.png":
                        action If (player.cash >= bra_fcup1a_cost, [Function (add_wardrobe, owned_bra, 1), Hide("shop_text"), Function(player.remove_money, bra_fcup1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_fcup1a_name, text_cost=bra_fcup1a_cost, text_desc=bra_fcup1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 1)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 2 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_fcup1b_%s.png":
                        action If (player.cash >= bra_fcup1b_cost, [Function (add_wardrobe, owned_bra, 2), Hide("shop_text"), Function(player.remove_money, bra_fcup1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_fcup1b_name, text_cost=bra_fcup1b_cost, text_desc=bra_fcup1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 2)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 7 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_cami1_%s.png":
                        action If (player.cash >= bra_cami1_cost, [Function (add_wardrobe, owned_bra, 7), Hide("shop_text"), Function(player.remove_money, bra_cami1_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_cami1_name, text_cost=bra_cami1_cost, text_desc=bra_cami1_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 7)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]


            elif tab_left_shop == "pants":
                if not 1 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_breif1a_%s.png":
                        action If (player.cash >= pants_breif1a_cost, [Function (add_wardrobe, owned_pants, 1), Hide("shop_text"), Function(player.remove_money, pants_breif1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_breif1a_name, text_cost=pants_breif1a_cost, text_desc=pants_breif1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 1)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 2 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_breif1b_%s.png":
                        action If (player.cash >= pants_breif1b_cost, [Function (add_wardrobe, owned_pants, 2), Hide("shop_text"), Function(player.remove_money, pants_breif1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_breif1b_name, text_cost=pants_breif1b_cost, text_desc=pants_breif1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 2)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 3 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_breif1c_%s.png":
                        action If (player.cash >= pants_breif1c_cost, [Function (add_wardrobe, owned_pants, 3), Hide("shop_text"), Function(player.remove_money, pants_breif1c_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_breif1c_name, text_cost=pants_breif1c_cost, text_desc=pants_breif1c_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 3)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 4 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_breif2a_%s.png":
                        action If (player.cash >= pants_breif2a_cost, [Function (add_wardrobe, owned_pants, 4), Hide("shop_text"), Function(player.remove_money, pants_breif2a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_breif2a_name, text_cost=pants_breif2a_cost, text_desc=pants_breif2a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 4)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 5 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_breif2b_%s.png":
                        action If (player.cash >= pants_breif2b_cost, [Function (add_wardrobe, owned_pants, 5), Hide("shop_text"), Function(player.remove_money, pants_breif2b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_breif2b_name, text_cost=pants_breif2b_cost, text_desc=pants_breif2b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 5)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 6 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_bshort1a_%s.png":
                        action If (player.cash >= pants_bshort1a_cost, [Function (add_wardrobe, owned_pants, 6), Hide("shop_text"), Function(player.remove_money, pants_bshort1a_cost), Function(pc_dress)], Show("no_money"),)
                        hovered [Show("shop_text", text_title=pants_bshort1a_name, text_cost=pants_bshort1a_cost, text_desc=pants_bshort1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 6)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 7 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_bshort1b_%s.png":
                        action If (player.cash >= pants_bshort1b_cost, [Function (add_wardrobe, owned_pants, 7), Hide("shop_text"), Function(player.remove_money, pants_bshort1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_bshort1b_name, text_cost=pants_bshort1b_cost, text_desc=pants_bshort1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 7)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 9 in owned_pants:
                    imagebutton auto "wardrobe/clothes/wardrobe_pants_gstring1a_%s.png":
                        action If (player.cash >= pants_gstring1a_cost, [Function (add_wardrobe, owned_pants, 9), Hide("shop_text"), Function(player.remove_money, pants_gstring1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=pants_gstring1a_name, text_cost=pants_gstring1a_cost, text_desc=pants_gstring1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 9)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]





            elif tab_left_shop == "socks":
                if not 8 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_thigh1d_%s.png":
                        action If (player.cash >= socks_thigh1d_cost, [Function (add_wardrobe, owned_socks, 8), Hide("shop_text"), Function(player.remove_money, socks_thigh1d_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_thigh1d_name, text_cost=socks_thigh1d_cost, text_desc=socks_thigh1d_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 8)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 9 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_thigh1e_%s.png":
                        action If (player.cash >= socks_thigh1e_cost, [Function (add_wardrobe, owned_socks, 9), Hide("shop_text"), Function(player.remove_money, socks_thigh1e_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_thigh1e_name, text_cost=socks_thigh1e_cost, text_desc=socks_thigh1e_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 9)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 10 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_thigh1f_%s.png":
                        action If (player.cash >= socks_thigh1f_cost, [Function (add_wardrobe, owned_socks, 10), Hide("shop_text"), Function(player.remove_money, socks_thigh1f_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_thigh1f_name, text_cost=socks_thigh1f_cost, text_desc=socks_thigh1f_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 10)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 11 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_garter1a_%s.png":
                        action If (player.cash >= socks_garter1a_cost, [Function (add_wardrobe, owned_socks, 11), Hide("shop_text"), Function(player.remove_money, socks_garter1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_garter1a_name, text_cost=socks_garter1a_cost, text_desc=socks_garter1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 11)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 12 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_garter1b_%s.png":
                        action If (player.cash >= socks_garter1b_cost, [Function (add_wardrobe, owned_socks, 12), Hide("shop_text"), Function(player.remove_money, socks_garter1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_garter1b_name, text_cost=socks_garter1b_cost, text_desc=socks_garter1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 12)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 13 in owned_socks:
                    imagebutton auto "wardrobe/clothes/wardrobe_socks_garter1c_%s.png":
                        action If (player.cash >= socks_garter1c_cost, [Function (add_wardrobe, owned_socks, 13), Hide("shop_text"), Function(player.remove_money, socks_garter1c_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=socks_garter1c_name, text_cost=socks_garter1c_cost, text_desc=socks_garter1c_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 13)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]


    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.81
        yalign 0.095
        xsize 330
        ysize 900
    imagebutton auto "poi_return_%s" action [Hide("underwear_shop"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
