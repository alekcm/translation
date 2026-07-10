

screen sport_shop:
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.095
        xsize 970
        ysize 100
        has vbox
        hbox:
            text "SPORT EXPERT"
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

            imagebutton auto "button_wardrobe_outfit_%s" action SetVariable ("tab_left_shop", "outfit")
            imagebutton auto "button_wardrobe_top_%s" action SetVariable ("tab_left_shop", "top")
            imagebutton auto "button_wardrobe_bottom_%s" action SetVariable ("tab_left_shop", "bottom")
            imagebutton auto "button_wardrobe_bra_%s" action SetVariable ("tab_left_shop", "bra")

        hbox:
            box_wrap True

            if tab_left_shop == "outfit":
                if not 2 in owned_outfit:
                    imagebutton auto "wardrobe/clothes/wardrobe_outfit_swimsuit1_%s.png":
                        action If (player.cash >= outfit_schswim_cost, [Function (add_wardrobe, owned_outfit, 2), Hide("shop_text"), Function(player.remove_money, outfit_schswim_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=outfit_schswim_name, text_cost=outfit_schswim_cost, text_desc=outfit_schswim_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 2)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 5 in owned_outfit:
                    imagebutton auto "wardrobe/clothes/wardrobe_outfit_swimsuit2a_%s.png":
                        action If (player.cash >= outfit_compswim_cost, [Function (add_wardrobe, owned_outfit, 5), Hide("shop_text"), Function(player.remove_money, outfit_compswim_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=outfit_compswim_name, text_cost=outfit_compswim_cost, text_desc=outfit_compswim_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 5)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 6 in owned_outfit:
                    imagebutton auto "wardrobe/clothes/wardrobe_outfit_swimsuit2b_%s.png":
                        action If (player.cash >= outfit_compswimmesh_cost, [Function (add_wardrobe, owned_outfit, 6), Hide("shop_text"), Function(player.remove_money, outfit_compswimmesh_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=outfit_compswimmesh_name, text_cost=outfit_compswimmesh_cost, text_desc=outfit_compswimmesh_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 6)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]


            elif tab_left_shop == "top":
                if not 3 in owned_top:
                    imagebutton auto "wardrobe/clothes/wardrobe_top_vball_%s.png":
                        action If (player.cash >= top_vball_cost, [Function (add_wardrobe, owned_top, 3), Hide("shop_text"), Function(player.remove_money, top_vball_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=top_vball_name, text_cost=top_vball_cost, text_desc=top_vball_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 3)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

                if not 6 in owned_top:
                    imagebutton auto "wardrobe/clothes/wardrobe_top_crop2_%s.png":
                        action If (player.cash >= top_crop2_cost, [Function (add_wardrobe, owned_top, 6), Hide("shop_text"), Function(player.remove_money, top_crop2_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=top_crop2_name, text_cost=top_crop2_cost, text_desc=top_crop2_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 6)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

                if not 7 in owned_top:
                    imagebutton auto "wardrobe/clothes/wardrobe_top_hoodiepull_%s.webp":
                        action If (player.cash >= top_hoodiepull_cost, [Function (add_wardrobe, owned_top, 7), Hide("shop_text"), Function(player.remove_money, top_hoodiepull_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=top_hoodiepull_name, text_cost=top_hoodiepull_cost, text_desc=top_hoodiepull_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 7)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

                if not 8 in owned_top:
                    imagebutton auto "wardrobe/clothes/wardrobe_top_hoodiezip_%s.webp":
                        action If (player.cash >= top_hoodiezip_cost, [Function (add_wardrobe, owned_top, 8), Hide("shop_text"), Function(player.remove_money, top_hoodiezip_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=top_hoodiezip_name, text_cost=top_hoodiezip_cost, text_desc=top_hoodiezip_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 8)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]


            elif tab_left_shop == "bottom":
                if not 4 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_vball_%s.png":
                        action If (player.cash >= bottom_vball_cost, [Function (add_wardrobe, owned_bottom, 4), Hide("shop_text"), Function(player.remove_money, bottom_vball_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_vball_name, text_cost=bottom_vball_cost, text_desc=bottom_vball_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 4)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 6 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_yoga1a_%s.png":
                        action If (player.cash >= bottom_yoga1a_cost, [Function (add_wardrobe, owned_bottom, 6), Hide("shop_text"), Function(player.remove_money, bottom_yoga1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_yoga1a_name, text_cost=bottom_yoga1a_cost, text_desc=bottom_yoga1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 6)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 7 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_yoga1b_%s.png":
                        action If (player.cash >= bottom_yoga1b_cost, [Function (add_wardrobe, owned_bottom, 7), Hide("shop_text"), Function(player.remove_money, bottom_yoga1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_yoga1b_name, text_cost=bottom_yoga1b_cost, text_desc=bottom_yoga1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 7)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 8 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_yoga1c_%s.png":
                        action If (player.cash >= bottom_yoga1c_cost, [Function (add_wardrobe, owned_bottom, 8), Hide("shop_text"), Function(player.remove_money, bottom_yoga1c_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_yoga1c_name, text_cost=bottom_yoga1c_cost, text_desc=bottom_yoga1c_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 8)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 9 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_shshorts_%s.png":
                        action If (player.cash >= bottom_shshorts_cost, [Function (add_wardrobe, owned_bottom, 9), Hide("shop_text"), Function(player.remove_money, bottom_shshorts_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_shshorts_name, text_cost=bottom_shshorts_cost, text_desc=bottom_shshorts_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 9)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 10 in owned_bottom:
                    imagebutton auto "wardrobe/clothes/wardrobe_bottom_track_%s.webp":
                        action If (player.cash >= bottom_track_cost, [Function (add_wardrobe, owned_bottom, 10), Hide("shop_text"), Function(player.remove_money, bottom_track_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bottom_track_name, text_cost=bottom_track_cost, text_desc=bottom_track_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 10)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]

            elif tab_left_shop == "bra":
                if not 3 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_sport1a_%s.png":
                        action If (player.cash >= bra_sport1a_cost, [Function (add_wardrobe, owned_bra, 3), Hide("shop_text"), Function(player.remove_money, bra_sport1a_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_sport1a_name, text_cost=bra_sport1a_cost, text_desc=bra_sport1a_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 3)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 4 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_sport1b_%s.png":
                        action If (player.cash >= bra_sport1b_cost, [Function (add_wardrobe, owned_bra, 4), Hide("shop_text"), Function(player.remove_money, bra_sport1b_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_sport1b_name, text_cost=bra_sport1b_cost, text_desc=bra_sport1b_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 4)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 5 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_sport1c_%s.png":
                        action If (player.cash >= bra_sport1c_cost, [Function (add_wardrobe, owned_bra, 5), Hide("shop_text"), Function(player.remove_money, bra_sport1c_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_sport1c_name, text_cost=bra_sport1c_cost, text_desc=bra_sport1c_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 5)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 6 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_sport1d_%s.png":
                        action If (player.cash >= bra_sport1d_cost, [Function (add_wardrobe, owned_bra, 6), Hide("shop_text"), Function(player.remove_money, bra_sport1d_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_sport1d_name, text_cost=bra_sport1d_cost, text_desc=bra_sport1d_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 6)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]
                if not 8 in owned_bra:
                    imagebutton auto "wardrobe/clothes/wardrobe_bra_sport2_%s.png":
                        action If (player.cash >= bra_sport2_cost, [Function (add_wardrobe, owned_bra, 8), Hide("shop_text"), Function(player.remove_money, bra_sport2_cost), Function(pc_dress)], Show("no_money"))
                        hovered [Show("shop_text", text_title=bra_sport2_name, text_cost=bra_sport2_cost, text_desc=bra_sport2_desc), Function(pc_strip), SetVariable ("c." + tab_left_shop, 8)]
                        unhovered [Hide("shop_text"), Function(pc_dress)]





    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.81
        yalign 0.095
        xsize 330
        ysize 900
    imagebutton auto "poi_return_%s" action [Hide("sport_shop"), Show("mall_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
