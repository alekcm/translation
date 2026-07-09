


init python:
    def shop_buy_value():
        price_total = 0
        for i in wardrobe_clothes_list:
            if getattr(c, i):
                q = globals()["item_" + i + "_" + str(getattr(shop, i))]
                if not q in (item for sublist in wardrobe.inv for item in sublist):
                    price_total += q.value
        
        return price_total

    def shop_buy():
        player.add_money(-shop_buy_value())
        for i in wardrobe_clothes_list:
            if getattr(c, i):
                q = globals()["item_" + i + "_" + str(getattr(shop, i))]
                if not q in (item for sublist in wardrobe.inv for item in sublist):
                    wardrobe.take(q)

    def set_wardrobe_colours(primary=True):
        global tab_top, tab_left, clothing_colour_last_selected, primary_colour, secondary_colour
        if primary:
            suffix = "primary"
        else:
            suffix = "secondary"
        colour = getattr(globals()[tab_top], tab_left + "_" + suffix + "_colour")
        
        clothing_colour_last_selected = colour
        picker.set_color(clothing_colours[colour])
        picker.color_slot = colour
        if primary:
            primary_colour = colour
        else:
            secondary_colour = colour

    def wardrobe_clothes_cycle_function():
        if c.underwear:
            pc_strip()
        elif not c.exposed:
            pc_strip_tops()
        else:
            pc_dress(ignore_naked=True)

    def wardrobe_clothes_get_name(top=True):
        global tab_top, tab_left
        if top:
            if "school" in tab_top:
                return "UNIFORM"
            elif "daily" in tab_top:
                return "DAILY CLOTHES"
            elif "party" in tab_top:
                return "PARTY CLOTHES"
            elif "sport" in tab_top:
                return "SPORTSWEAR"
            elif "swim" in tab_top:
                return "SWIMMING SUIT"
            elif "home" in tab_top:
                return "HOMEWEAR"
            elif "work" in tab_top:
                return "WORK CLOTHES"
            return tab_top.upper()
        
        else:
            if "swim" in tab_top:
                if tab_left == "outfit":
                    return "SWIMSUITS"
                elif tab_left == "top":
                    return "BIKINI TOPS"
                elif tab_left == "bottom":
                    return "BIKINI BOTTOMS"
            else:
                if tab_left == "hat":
                    return "HEADWEAR"
                elif tab_left == "coat":
                    return "COATS"
                elif tab_left == "outfit":
                    return "OUTFITS"
                elif tab_left == "top":
                    return "TOPS"
                elif tab_left == "bottom":
                    return "BOTTOMS"
                elif tab_left == "bra":
                    return "BRAS"
                elif tab_left == "pants":
                    return "UNDERPANTS"
                elif tab_left == "bsuit":
                    return "BODYSUITS"
                elif tab_left == "gloves":
                    return "GLOVES"
                elif tab_left == "socks":
                    return "LEGWEAR"
            return tab_left.upper()

    def reset_speaking_char():
        global speaking_char
        speaking_char = None
transform button_clothing_tint_transform(colour):
    matrixcolor TintMatrix(get_clothing_colour(colour))






image button_wardrobe_colour_frame_idle:
    "button_wardrobe_colour_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_colour_frame_selected_idle = "button_wardrobe_colour_frame"
image button_wardrobe_colour_frame_hover = "button_wardrobe_coloura_frame"

image button_wardrobe_colour_framer_idle:
    "button_wardrobe_colour_framer"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_colour_framer_selected_idle = "button_wardrobe_colour_framer"
image button_wardrobe_colour_framer_hover = "button_wardrobe_coloura_framer"


image button_wardrobe_tab_frame_idle:
    "button_wardrobe_tab_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_tab_frame_selected_idle = "button_wardrobe_taba_frame"
image button_wardrobe_tab_frame_hover = "button_wardrobe_tab_frame"


image button_wardrobe_tab_right_frame_idle:
    "button_wardrobe_tab_right_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_tab_right_frame_selected_idle = "button_wardrobe_tab_right_frame"
image button_wardrobe_tab_right_frame_red:
    "button_wardrobe_tab_righta_frame"
    matrixcolor TintMatrix(wardrobe_red_colour)
image button_wardrobe_tab_right_frame_hover = "button_wardrobe_tab_righta_frame"

image button_wardrobe_tab_left_frame_idle:
    "button_wardrobe_tab_left_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_tab_left_frame_selected_idle = "button_wardrobe_tab_left_frame"
image button_wardrobe_tab_left_frame_red:
    "button_wardrobe_tab_lefta_frame"
    matrixcolor TintMatrix(wardrobe_red_colour)
image button_wardrobe_tab_left_frame_hover = "button_wardrobe_tab_lefta_frame"

image button_wardrobe_tab_top_frame_idle:
    "button_wardrobe_tab_top_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_tab_top_frame_selected_idle = "button_wardrobe_tab_top_frame"
image button_wardrobe_tab_top_frame_hover = "button_wardrobe_tab_topa_frame"

image button_wardrobe_tab_bottom_frame_idle:
    "button_wardrobe_tab_bottom_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_wardrobe_tab_bottom_frame_selected_idle = "button_wardrobe_tab_bottom_frame"
image button_wardrobe_tab_bottom_frame_hover = "button_wardrobe_tab_bottoma_frame"


image button_items_frame_idle:
    "button_items_frame"
    matrixcolor TintMatrix(Color(rgb = (0.847, 0.278, 0.580)))
image button_items_frame_selected_idle = "button_items_framea"
image button_items_frame_hover = "button_items_frame"

default wardrobe_red_colour = Color(rgb = (0.596, 0.109, 0.192))
default wardrobe_colour_selected = Color(rgb = (0.847, 0.278, 0.580))
default wardrobe_clothes_list = ["hat", "jacket", "coat", "top", "bottom", "bra", "pants", "socks", "outfit", "gloves"]

screen wardrobe_clothes_button(item):
    frame padding (2,2) xysize (126, 80) background None:
        add item[0].class_name pos (1,1)


        imagebutton auto "button_items_frame_%s":


            action [
                SelectedIf(SetVariable("c." + item[0].clothes_tab, item[0].clothes_number)),
                Function(clothes_set, item[0].clothes_tab, If(getattr(c, item[0].clothes_tab) == item[0].clothes_number, 0, item[0].clothes_number)),
                
                ],

screen wardrobe_buy_button(item):
    frame padding (2,2) xysize (126, 80) background None:
        if wardrobe.qty(item):

            add item.class_name pos (1,1) matrixcolor SaturationMatrix(0)
            add "button_items_owned"
        else:
            add item.class_name pos (1,1)
            text "£[item.value]" anchor (1.0,1.0) align (0.9,0.9) size 18

        imagebutton auto "button_items_frame_%s":
            action [Function(clothes_set, item.clothes_tab, item.clothes_number),
            SelectedIf(SetVariable("c." + item.clothes_tab, item.clothes_number )),
            Show("wardrobe_text", text_title=item.name, text_desc=item.desc)
            ],

screen wardrobe_take_choice_button(item):
    frame padding (0,0) xysize (126, 80) background None:
        if item in (item for sublist in wardrobe.inv for item in sublist):
            add item.class_name pos (1,1) matrixcolor SaturationMatrix(0)
            add "button_items_owned"
        else:
            add item.class_name pos (1,1)
            text "£[item.value]" anchor (1.0,1.0) align (0.9,0.9) size 18

        imagebutton auto "button_items_frame_%s":
            action [Function(clothes_set, item.clothes_tab, item.clothes_number),
            Function(wardrobe.take, item),
            Return()
            ],

screen wardrobe_colour_button_row(is_primary):
    hbox align (0, 0) xysize (50,20):



        for i in clothing_colour_custom:
            use wardrobe_colour_button(i, is_primary)
        frame padding (0,0) xysize (15,40) background None
        frame padding (0,0) xysize (41,40) background None:
            use wardrobe_trans_button(is_primary)

screen wardrobe_colour_button(colour, is_primary):
    if is_primary:
        $ suffix = "primary"
    else:
        $ suffix = "secondary"
    frame padding (0,0) xysize (41,40) background None:
        add "button_wardrobe_colour_base":
            matrixcolor TintMatrix(clothing_colours[colour])
        imagebutton auto "button_wardrobe_colour_frame_%s":
            action [
                SelectedIf(SetVariable ((tab_top + "." + tab_left + "_" + suffix + "_colour"), colour)),
                Function(get_custom_clothing_colours, colour),
                SetVariable ((suffix + "_colour"), colour), 
                SetVariable ((tab_top + "." + tab_left + "_" + suffix + "_colour"), colour), 
                
                SetVariable("clothing_colour_last_selected", colour),
                Function(picker.set_color, clothing_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen wardrobe_trans_button(is_primary):
    if is_primary:
        $ suffix = "primary"
    else:
        $ suffix = "secondary"
    frame padding (0,0) xysize (41,40) background None:
        add "button_wardrobe_colour_base"

        imagebutton auto "button_wardrobe_colour_frame_%s":
            action [
                Function(cycle_trans_material, tab_top, tab_left, is_primary),
                Function(refresh_avatar),
                ]

image button_wardrobe_tab_bsuit = "button_wardrobe_tab_pants"

screen wardrobe_tableft_button(text_title, text_desc, tab, strip=False, what_inv=wardrobe):
    if what_inv.check_type(tab) or what_inv.check_type(tab + "2"):
        frame padding (0,0) xysize (82,80) background None:
            add "button_wardrobe_tab_bg"
            add "button_wardrobe_tab_" + tab:
                if tab_left != tab:
                    matrixcolor TintMatrix(wardrobe_colour_selected)

            imagebutton auto "button_wardrobe_tab_frame_%s":


                action [
                    If(strip,Function(pc_strip_tops),Function(pc_dress, ignore_naked=True)), 
                    SetVariable ("tab_left", tab), 
                    Function(player.allure_function),
                    Function(set_wardrobe_colours),
                    ]

screen wardrobe_tableft_halfbutton(text_title, text_desc, tab, tab2, strip=True, strip2=True, what_inv=wardrobe, swap=False):
    if what_inv.check_type(tab) or what_inv.check_type(tab2):
        frame padding (0,0) xysize (82,80) background None:
            add "button_wardrobe_tab_bg"

            imagebutton auto "button_wardrobe_tab_top_frame_%s":
                focus_mask True


                action [
                    If(strip,Function(pc_strip_tops),Function(pc_dress, ignore_naked=True)), 
                    SetVariable ("tab_left", tab), 
                    Function(player.allure_function),
                    Function(set_wardrobe_colours),
                    Function(refresh_avatar),
                    ]
            imagebutton auto "button_wardrobe_tab_bottom_frame_%s":
                focus_mask True


                action [
                    If(strip2,Function(pc_strip_tops),Function(pc_dress, ignore_naked=True)), 
                    SetVariable ("tab_left", tab2), 
                    Function(player.allure_function),
                    Function(set_wardrobe_colours),
                    Function(refresh_avatar),
                    ]
            add "button_wardrobe_tab_" + (tab2 if swap else tab):
                if tab_left != tab and tab_left != tab2:
                    matrixcolor TintMatrix(wardrobe_colour_selected)

screen wardrobe_tabtop_button(text_title, text_desc, tab):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"
        add "button_wardrobe_tab_" + tab:
            if getattr(globals()[tab], "inappropriate") and not tab_top == tab:
                matrixcolor TintMatrix(wardrobe_red_colour)
            elif tab_top != tab:
                matrixcolor TintMatrix(wardrobe_colour_selected)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title=text_title, text_desc=text_desc),
            unhovered Hide("wardrobe_text"),
            action [
                Function(pc_dress, ignore_naked=True), 
                Function(tab_clothes, tab), 
                Function(player.allure_function), 
                Function(set_wardrobe_colours),
                Function(wardrobe_sethair),
                Function(pc_remove_bad_clothes),
                Function(refresh_avatar),
                ]

screen wardrobe_tabtop_half_button(text_title, text_desc, tab):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"

        imagebutton:
            if getattr(globals()[tab], "inappropriate") and not tab_top == tab:
                idle "button_wardrobe_tab_left_frame_red"
            else:
                if tab_top == tab:
                    idle "button_wardrobe_tab_left_frame_selected_idle"
                else:
                    idle "button_wardrobe_tab_left_frame_idle"
            hover "button_wardrobe_tab_left_frame_hover"

            focus_mask True


            action [
                Function(pc_dress, ignore_naked=True), 
                Function(tab_clothes, tab), 
                Function(player.allure_function), 
                Function(set_wardrobe_colours),
                Function(wardrobe_sethair),
                Function(pc_remove_bad_clothes),
                Function(refresh_avatar),
                ]

        imagebutton:
            if getattr(globals()[tab + "2"], "inappropriate") and not tab_top == (tab + "2"):
                idle "button_wardrobe_tab_right_frame_red"
            else:
                if tab_top == (tab + "2"):
                    idle "button_wardrobe_tab_right_frame_selected_idle"
                else:
                    idle "button_wardrobe_tab_right_frame_idle"
            hover "button_wardrobe_tab_right_frame_hover"
            selected_idle "button_wardrobe_tab_right_frame_selected_idle"
            focus_mask True


            action [
                Function(pc_dress, ignore_naked=True), 
                Function(tab_clothes, tab + "2"), 
                Function(player.allure_function), 
                Function(set_wardrobe_colours),
                Function(wardrobe_sethair),
                Function(pc_remove_bad_clothes),
                Function(refresh_avatar),
                ]

        add "button_wardrobe_tab_" + re.sub('[0-9]', '', tab):
            if re.sub('[0-9]', '', tab_top) != tab:
                matrixcolor TintMatrix(wardrobe_colour_selected)

screen wardrobe_clothes_cycle():
    textbutton "CYCLE CLOTHES" action [Function(wardrobe_clothes_cycle_function), Function(refresh_avatar)] text_style "quest_obj_stat_alt"


define tab_top_enter = "daily"

screen wardrobe_screen(what_inv=wardrobe, shop=False, shop_return=False):
    zorder 0
    $ what_inv.sort_clothes()
    $ reset_speaking_char()

    if cheats == 1:
        frame align (0,0.095):
            text "[tab_top] and [tab_left] and [primary_colour] and [secondary_colour] and [tab_top_enter] and [clothing_colour_last_selected]" size 15

    frame anchor (0,0) align (0.3,0.095) xysize (990,900):

        has vbox
        hbox:

            frame padding (0,0) xysize (82,80) background None:
                add "button_wardrobe_tab_bg"
                add "button_wardrobe_tab_frame_idle"

            if what_inv == wardrobe:
                use wardrobe_tabtop_half_button("SCHOOL UNIFORM", "Clothes needed to be worn while attending school. Schoolgirls are often seen as an easy target so wearing this may lead to increased harassment.", "school")
                use wardrobe_tabtop_half_button("EVERYDAY WEAR", "Typical clothes for most occasions.", "daily")
                use wardrobe_tabtop_half_button("PARTY CLOTHES", "Clothes typically worn to nightclubs or other social functions. Be careful, if you are too alluring then people can easily mistake you for a prostitute.", "party")
                use wardrobe_tabtop_half_button("SPORTS CLOTHES", "Clothes typically worn while working out. Comes with sports bras that help increase support while exercising.", "sport")
                use wardrobe_tabtop_half_button("SWIMMING COSTUME", "Swimsuits for swimming in the pool and bikinis for relaxing on the beach.", "swim")
                use wardrobe_tabtop_half_button("HOME CLOTHES", "Clothes for relaxing at home or sleeping in. Be careful, wearing too little might give your flatmates a nice eyeful.", "home")
            else:
                text "SHOP NAME TEXT" font "BRLNSB.TTF" size 30
        hbox:
            vbox:
                frame padding (0,0) xysize (82,80) background None:
                    add "button_wardrobe_tab_bg"
                    add "button_wardrobe_tab_frame_idle"
                if what_inv == wardrobe:
                    if "swim" in tab_top:
                        use wardrobe_tableft_button("SWIMSUITS", "Full body swimwear and summer bikinis", "outfit")
                        use wardrobe_tableft_button("BIKINI TOPS", "Bikini tops usually worn to the beach", "top")
                        use wardrobe_tableft_button("BIKINI BOTTOMS", "Bikini bottoms usually worn to the beach", "bottom")

                    else:
                        use wardrobe_tableft_button("HEADWEAR", "Hats and all manner of headwear", "hat")
                        use wardrobe_tableft_button("COATS", "Heavy coats to protect against the cold", "coat")
                        use wardrobe_tableft_button("OUTFITS", "Full body outfits that cover your upper and lower body", "outfit")
                        use wardrobe_tableft_button("TOPS", "Tops and any outerwear for your upper body", "top")
                        use wardrobe_tableft_button("BOTTOMS", "Everything for your lower body. Trousers, skirts, leggings and more", "bottom")
                        use wardrobe_tableft_halfbutton("BRAS", "Every girls best and worst friend. Gives you support and prevents poking nipples. Pinching and chaffing optional", "bra", "pants")

                        use wardrobe_tableft_button("BODYSUITS", "From tiny thongs to giant granny pants.", "bsuit", True)
                        use wardrobe_tableft_halfbutton("LEGWEAR", "Tights, stockings, garter belts and high socks. Worn under your trousers or skirt", "gloves", "socks", strip=False, swap=True)

                else:
                    use wardrobe_tableft_button("HEADWEAR", "Hats and all manner of headwear", "hat", what_inv=what_inv)
                    use wardrobe_tableft_button("COATS", "Heavy coats to protect against the cold", "coat", what_inv=what_inv)
                    use wardrobe_tableft_button("JACKETS", "Jackets, Blazers and Cardigans for wearing while at school. These are worn over your shirt", "jacket", what_inv=what_inv)
                    use wardrobe_tableft_button("OUTFITS", "Full body outfits that cover your upper and lower body", "outfit", what_inv=what_inv)
                    use wardrobe_tableft_button("TOPS", "Tops and any outerwear for your upper body", "top", what_inv=what_inv)
                    use wardrobe_tableft_button("BOTTOMS", "Everything for your lower body. Trousers, skirts, leggings and more", "bottom", what_inv=what_inv)
                    use wardrobe_tableft_button("BRAS", "Every girls best and worst friend. Gives you support and prevents poking nipples. Pinching and chaffing optional", "bra", True, what_inv=what_inv)
                    use wardrobe_tableft_button("UNDERPANTS", "From tiny thongs to giant granny pants.", "pants", True, what_inv=what_inv)
                    use wardrobe_tableft_button("BOSYSUITS", "Sexy bodysuits, wraps, body shapers and more.", "bsuit", True, what_inv=what_inv)
                    use wardrobe_tableft_button("LEGWEAR", "Tights, stockings, garter belts and high socks. Worn under your trousers or skirt", "socks", True, what_inv=what_inv)
                    use wardrobe_tableft_button("GLOVES", "Gloves and other hand/wrist clothing", "gloves", what_inv=what_inv)

            vbox:
                vbox:
                    use wardrobe_colour_button_row(True)
                    use wardrobe_colour_button_row(False)

                hbox:
                    box_wrap True
                    if what_inv == wardrobe:
                        for i in what_inv.inv:
                            if getattr(i[0], "type") == tab_left and re.sub('[0-9]', '', tab_top) in getattr(i[0], "outfit"):
                                use wardrobe_clothes_button(i)

                    else:
                        for i in what_inv.inv:
                            if getattr(i[0], "type") == tab_left:

                                use wardrobe_buy_button(i[0])

    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        has vbox ysize 880
        frame xsize 330 background None:
            has vbox
            spacing 0
            text wardrobe_clothes_get_name() size 38 color '#ffffff' font "BRLNSB.TTF"
            text wardrobe_clothes_get_name(False) size 32 color '#ffffff' font "BRLNSB.TTF"
            if getattr(c, tab_left):
                text globals()["item_" + tab_left + "_" + str(getattr(c, tab_left))].name size 26 color '#ffffff' font "BRLNSB.TTF"
                text globals()["item_" + tab_left + "_" + str(getattr(c, tab_left))].desc size 22
                null height 10
                hbox:
                    for i in ["skirt", "ass", "clevage", "belly", "braless", "thong", "slutty", "pantsless"]:
                        if getattr(globals()["item_" + tab_left + "_" + str(getattr(c, tab_left))], i):
                            add "button_wardrobe_type_icon_" + i

        if shop:
            $ clothes_value = shop_buy_value()
            textbutton "BUY FOR [clothes_value]" action Function(shop_buy) text_style "quest_obj_stat"
        else:
            hbox align (0.5, 1.0):
                use color_picker()
    if what_inv == wardrobe:
        use wardrobe_screen_jewel
    use wardrobe_screen_return(shop, shop_return)

screen wardrobe_screen_return(shop, shop_return, x=0.25, y=0.5):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            if origin_start_tutorial:
                action [
                    Hide("wardrobe_screen"), 
                    Function(pc_dress), 
                    SetVariable("tab_left", "top"), 
                    SetVariable("origin_start_tutorial", False), 
                    Jump("start_tutorial_bedroom")
                    ]
            else:

                action [
                    If(shop==True, [Function(tab_clothes, tab_top_enter)]), 
                    Hide("wardrobe_screen"), 
                    Hide("wardrobe_text"), 
                    Function(pc_dress_tops), 
                    SetVariable("tab_left", "top"), 
                    SetVariable("picker.color_slot", None),
                    Function(pc_remove_bad_clothes),
                    Function(refresh_avatar),
                    If(shop_return, Return(_return), Jump("world_wardrobe_close"))
                    ]

screen wardrobe_screen_jewel(x=0.25, y=0.42):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_jewel" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Hide("wardrobe_screen"),
                Hide("wardrobe_text"),
                Function(pc_dress),
                
                SetVariable("tab_top_acc", "makeup"),
                SetVariable("tab_left_acc", "eyeshadow"),
                Function(set_acc_colours),
                Function(pc_remove_bad_clothes),
                Function(refresh_avatar),
                Show("acc_screen")
            ]

default had_pantsless_warning = False
default had_braless_warning = False
default had_sportsbra_warning = False
default had_thong_skirt_warning = False
default had_thong_ass_warning = False
default had_belly_preg_warning = False
default had_home_topless_warning = False
default had_home_bottomless_warning = False

label world_wardrobe_close:
    $ player.allure_function()
    if "swim" in tab_top:
        if loc(loc_bedroom):
            pcm "What am I going to do? Walk around the house in my bikini?"
            call screen wardrobe_screen

    elif c.exposed and not loc(loc_motel_pinkroom) and not loc_cur.home_location:
        if "ignored_exposed_prompt" in perk_exhibitionist.list:

            jump travel

        elif perk_exhibitionist.dict["exhib_counter"] > 300 and not "ignored_exposed_prompt" in perk_exhibitionist.list:

            pcm "I really should put something more on than this."
            pcm "Unless I want to be exposed..."
            menu:
                "Go out like this":
                    $ add_to_list(perk_exhibitionist.list, "ignored_exposed_prompt")
                    pcm "I can have a little fun like this."
                    jump travel
                "Dress up properly":
                    call screen wardrobe_screen 
        else:







            if not "exhib_practice_warning" in perk_exhibitionist.list:

                $ add_to_list(perk_exhibitionist.list, "exhib_practice_warning")
                pcm "If I want to be outside all naked, I should practice in the park at night first..."
            elif not numgen(0,5):

                pcm "If I want to be outside all naked, I should practice in the park at night first..."

            if not t.timeofday in "night":
                call screen wardrobe_screen 
            else:
                jump travel

    jump travel


define clothes_tab_list = ["school", "school2", "daily", "daily2", "party", "party2", "sport", "sport2", "swim", "swim2", "home", "home2"]
define clothes_tab_noalt_list = ["school", "daily", "party", "sport", "swim", "home"]
define clothes_tab_all_list = ["c", "school", "school2", "daily", "daily2", "party", "party2", "sport", "sport2", "swim", "swim2", "home", "home2", "work", "shop"]
define clothes_list = ["hat", "coat", "jacket", "outfit", "top", "bottom", "bra", "pants", "bsuit", "socks", "gloves", "glasses", "choker", "nipring", "navelring", "mask"]

define clothes_wardrobe_list = ["hat", "gloves", "coat", "outfit", "top", "bottom", "socks", "bra", "pants", "bsuit"]
define clothes_wardrobe_tops_list = ["hat", "gloves", "jacket", "coat", "top", "bottom", "outfit"]
define clothes_wardrobe_under_list = ["socks", "bra", "pants", "bsuit"]
define clothes_wardrobe_upper_list = ["hat", "gloves", "jacket", "coat", "top", "outfit", "bra", "bsuit"]
define clothes_wardrobe_lower_list = ["bottom", "socks", "pants", "bsuit"]

define clothes_acc_list = ["glasses", "mask", "choker", "necklace", "neck", "earring", "nipring", "navelring", "waist", "vag", "anus"]
define clothes_acc_perm_list = ["earring", "necklace", "nipring", "navelring", "vag", "anus"]
define clothes_acc_temp_list = ["glasses", "mask", "choker", "neck", "waist"]

define clothing_colour_last_selected = False

define clothing_colour_all = ["black","grey","white","navy","blue","crimson","brown","green","pumpkin","pink","magenta","yellow"]

define clothing_colour_school = ["black","grey","white","crimson","pink"]
define clothing_colour_metals = ["silver","steel","gold"]
define clothing_colour_makeup = ["brown","orange","pink", "purple", "red", "crimson", "magenta", "hotpink"]
define clothing_colour_makeup_custom = ["custommakeup1", "custommakeup2", "custommakeup3", "custommakeup4", "custommakeup5", "custommakeup6", "custommakeup7", "custommakeup8"]
define clothing_colour_custom = ["custom1", "custom2", "custom3", "custom4", "custom5", "custom6", "custom7", "custom8", "custom9", "custom10", "custom11", "custom12"]
define hair_colours_list = ["hair1","hair2","hair3","hair4","hair5","hair6","hair7","hair8"]
define hair_colours_custom_list = ["hair9","hair10","hair11","hair12","hair13","hair14","hair15","hair16"]
define eye_colours_list = ["eye0","eye1","eye2","eye3","eye4","eye5"]
define eye_colours_custom_list = ["eye6","eye7","eye8","eye9","eye10", "eye11"]
define skin_colours_list = ["1_0_base","2_0_base","3_0_base","4_0_base","5_0_base"]
define skin_colours_custom_list = ["6_0_base","7_0_base","8_0_base","9_0_base","10_0_base"]

define wardrobe_restricted = True

screen wardrobe_tabtop_button_tutorial(tab):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"

        add "button_wardrobe_tab_" + tab:
            if tab_left != tab and tab_left != tab + "2":
                matrixcolor TintMatrix(wardrobe_red_colour)
            elif tab_top != tab:
                matrixcolor TintMatrix(wardrobe_colour_selected)

        add "button_wardrobe_tab_right_frame_idle"
        add "button_wardrobe_tab_left_frame_idle"






screen wardrobe_tableft_button_tutorial(tab):
    if wardrobe.check_type(tab):
        frame padding (0,0) xysize (82,80) background None:
            add "button_wardrobe_tab_bg"
            add "button_wardrobe_tab_" + tab:
                if tab_left != tab:
                    matrixcolor TintMatrix(wardrobe_colour_selected)
            add "button_wardrobe_tab_frame_idle"

screen wardrobe_colour_button_row_tutorial(is_primary):
    hbox align (0, 0) xysize (50,20):
        for i in clothing_colour_custom:
            use wardrobe_colour_button_tutorial(i, is_primary)
        frame padding (0,0) xysize (15,40) background None
        frame padding (0,0) xysize (41,40) background None:
            use wardrobe_colour_button_tutorial("white", is_primary)

screen wardrobe_colour_button_tutorial(colour, is_primary):
    if is_primary:
        $ suffix = "primary"
    else:
        $ suffix = "secondary"
    frame padding (0,0) xysize (41,40) background None:
        add "button_wardrobe_colour_base":
            matrixcolor TintMatrix(clothing_colours[colour])
        add "button_wardrobe_colour_frame_idle"

screen wardrobe_clothes_button_tutorial(item):
    frame padding (0,0) xysize (126, 80) background None:
        add item[0].class_name pos (1,1)
        add "button_items_frame_idle"


screen wardrobe_screen_tutorial():
    frame anchor (0,0) align (0.3,0.095) xysize (990,900):
        has vbox
        hbox:


            frame padding (0,0) xysize (82,80) background None:
                add "button_wardrobe_tab_bg"
                add "button_wardrobe_tab_frame_idle"

            for i in clothes_tab_noalt_list:
                use wardrobe_tabtop_button_tutorial(i)

        hbox:
            vbox:
                frame padding (0,0) xysize (82,80) background None:
                    add "button_wardrobe_tab_bg"
                    add "button_wardrobe_tab_frame_idle"
                for i in clothes_list:
                    use wardrobe_tableft_button_tutorial(i)

            vbox:
                vbox:
                    use wardrobe_colour_button_row_tutorial(True)
                    use wardrobe_colour_button_row_tutorial(False)

                hbox:
                    box_wrap True

                    for i in wardrobe.inv:
                        if getattr(i[0], "type") == tab_left and tab_top in getattr(i[0], "outfit"):
                            frame padding (0,0) xysize (126, 80) background None:
                                use wardrobe_clothes_button_tutorial(i)

    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        $ NullAction()

screen bedroom_screen_tutorial:
    imagebutton auto "poi_wardrobe_%s":
        action [Hide("text_hov"), Show("wardrobe_screen"), Hide("bedroom_screen_tutorial"), SetVariable("origin_start_tutorial", True)]
        pos (1045,526)
        hovered Show("text_hov", text="Open your wardrobe", posi=(1045,526))
        unhovered Hide("text_hov")
    imagebutton auto "poi_sleep_%s":
        action [Hide("text_hov"), Jump ("start_tutorial_sleep")]
        pos (1605, 666)
        hovered Show("text_hov", text="Go to sleep", posi=(1605, 666))
        unhovered Hide("text_hov")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
