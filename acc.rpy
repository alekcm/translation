init python:

    def hair_cycle():
        if any(clothes in ["sport", "swim", "home"] for clothes in tab_top) or player.hair_neck == 1:
            renpy.jump("hair_event")
        elif player.hair_style_default == "loose":
            player.hair_style_default = "pony"
        elif player.hair_style_default == "pony":
            player.hair_style_default = "bun"
        elif player.hair_style_default == "bun":
            player.hair_style_default = "pig"
        else:
            player.hair_style_default = "loose"
        player.hair_style = player.hair_style_default

    def hair_cycle_front(number=6):
        player.hair_fringe += 1
        if player.hair_fringe > number:
            player.hair_fringe = 1

    def setacc(slot,number):
        setattr(acc, slot, number)
        setattr(accbak, slot, number)

    def acc_backup():
        for i in clothes_acc_list:
            setattr(accbak, i, getattr(acc, i))

    def acc_strip():
        acc_backup()
        for i in clothes_acc_list:
            setattr(acc, i, 0)

    def acc_dress():
        for i in clothes_acc_list:
            setattr(acc, i, getattr(accbak, i))

    def acc_shower():
        acc_backup()
        for i in clothes_acc_temp_list:
            setattr(acc, i, 0)

    def acc_shower_dress():
        acc_dress()

    class Accessories(object):
        def __init__(self):
            self.makeup_on = False
            self.eyeshadow = 0
            self.eyeliner = 1
            self.blush = 0
            self.lipstick = 0
            self.nails = 0
            
            self.gloves = 0
            self.glasses = 0
            self.mask = 0
            self.choker = 0
            self.necklace = 0
            self.neck = 0
            self.earring = 0
            self.ear = 0
            self.nipring = 0
            self.navelring = 0
            self.waist = 0
            self.vag = 0
            self.anus = 0
            
            
            
            
            
            
            
            self.eyeshadow_primary_colour = "custom6"
            self.eyeshadow_secondary_colour = "custom6"
            self.eyeliner_primary_colour = "custom1"
            self.eyeliner_secondary_colour = "custom1"
            self.blush_primary_colour = "custom10"
            self.blush_secondary_colour = "custom10"
            self.lipstick_primary_colour = "custom10"
            self.lipstick_secondary_colour = "custom10"
            self.nails_primary_colour = "custom10"
            self.nails_secondary_colour = "custom10"
            
            self.gloves_primary_colour = "red"
            self.gloves_secondary_colour = "silver"
            self.glasses_primary_colour = "custom6"
            self.glasses_secondary_colour = "silver"
            self.mask_primary_colour = "custom6"
            self.mask_secondary_colour = "silver"
            self.choker_primary_colour = "custom6"
            self.choker_secondary_colour = "silver"
            self.necklace_primary_colour = "custom6"
            self.necklace_secondary_colour = "silver"
            self.neck_primary_colour = "custom6"
            self.neck_secondary_colour = "silver"
            self.earring_primary_colour = "custom3"
            self.earring_secondary_colour = "silver"
            self.nipring_primary_colour = "custom3"
            self.nipring_secondary_colour = "silver"
            self.navelring_primary_colour = "custom3"
            self.navelring_secondary_colour = "silver"
            self.vag_primary_colour = "custom6"
            self.vag_secondary_colour = "silver"
            self.anus_primary_colour = "custom6"
            self.anus_secondary_colour = "silver"
        
        @property
        def sexual(self):
            for i in clothes_acc_list:
                if (not i == "anus") and getattr(self, i) and globals()["item_" + i + "_" + str(getattr(self, i))].sexual:
                    return True
            return False
        @property
        def perverted(self):
            for i in clothes_acc_list:
                if (not i == "anus") and getattr(self, i) and globals()["item_" + i + "_" + str(getattr(self, i))].perverted:
                    return True
            return False
        @property
        def gagged(self):
            if self.mask and globals()["item_mask_" + str(self.mask)].gagged:
                return True
            else:
                return False
        
        def shower(self):
            
            self.glasses = 0
            self.mask = 0
            self.choker = 0
            
            self.neck = 0
            
            
            
            self.waist = 0
        
        
        
        def makeup_reset(self):
            self.makeup_on = False
            self.eyeshadow = 0
            self.blush = 0
            self.lipstick = 0
            self.nails = 0
        
        def acc_remove(self): 
            self.gloves = 0
            self.glasses = 0
            self.mask = 0
            self.choker = 0
            self.necklace = 0
            self.neck = 0
            self.earring = 0
            self.nipring = 0
            self.navelring = 0
            self.waist = 0
            self.vag = 0
            self.anus = 0

    def set_acc_colours(primary=True):
        global tab_top_acc, tab_left_acc, clothing_colour_last_selected, primary_colour, secondary_colour
        if primary:
            suffix = "primary"
        else:
            suffix = "secondary"
        
        
        if "hair" in tab_left_acc:
            colour = str(player.hair_colour)
            picker.set_color(hair_colours[colour]) 
        elif tab_left_acc == "eyes":
            colour = str(player.eye_colour)
            picker.set_color(eye_colours[colour]) 
        elif tab_left_acc in ["skin", "breasts", "skin_effect"]:
            colour = player.skin_colour
            picker.set_color(skin_colours[colour])
        elif tab_left_acc == "nip_size":
            colour = str(player.nip_colour)
            picker.set_color(nipple_colours[colour])
        else:
            colour = getattr(acc, tab_left_acc + "_" + suffix + "_colour")
            picker.set_color(clothing_colours[colour]) 
        
        clothing_colour_last_selected = colour
        
        picker.color_slot = colour
        if primary:
            primary_colour = colour
        else:
            secondary_colour = colour
        refresh_avatar()

image button_wardrobe_tab_skin_effect = "button_wardrobe_tab_skin"
image button_wardrobe_tab_eyes = "button_wardrobe_tab_iris"
image button_wardrobe_tab_hair_length = "button_wardrobe_tab_hair"
image button_wardrobe_tab_nip_size = "button_wardrobe_tab_breasts"

screen acc_colour_button(colour, is_primary, round=False, metal=False):
    if is_primary:
        $ suffix = "primary"
    else:
        $ suffix = "secondary"

    $ icon = "button_wardrobe_colour_frame_%s"
    $ icon_but = "button_wardrobe_colour_base"
    if round:
        $ icon = "button_wardrobe_colour_framer_%s"
        $ icon_but = "button_wardrobe_colour_baser"
    if metal:
        $ icon_but = "button_wardrobe_colour_basem"


    frame padding (0,0) xysize (41,40) background None:
        add icon_but:
            matrixcolor TintMatrix(clothing_colours[colour])
        imagebutton auto icon:
            action [
                SelectedIf(SetVariable (("acc." + tab_left_acc + "_" + suffix + "_colour"), colour)),
                
                
                
                
                Function(get_custom_clothing_colours, colour),
                SetVariable (( suffix + "_colour"), colour), 
                
                SetVariable (("acc." + tab_left + "_" + suffix + "_colour"), colour),
                SetVariable("clothing_colour_last_selected", colour),
                Function(picker.set_color, clothing_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen acc_screen_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in clothing_colour_custom:
                use acc_colour_button(i, True)
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in clothing_colour_metals:
                use acc_colour_button(i, False, metal=True)

screen acc_screen_makeup_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in clothing_colour_makeup_custom:
                use acc_colour_button(i, True, round=True)
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in clothing_colour_metals:
                use acc_colour_button(i, False, metal=True)

screen acc_hair_colour_button(colour):
    $ icon = "button_wardrobe_colour_frame_%s"
    $ icon_but = "button_wardrobe_colour_base"

    frame padding (0,0) xysize (41,40) background None:
        add icon_but:
            matrixcolor TintMatrix(hair_colours[colour])
        imagebutton auto icon:
            action [
                SelectedIf(SetVariable ("player.hair_colour", colour)),
                SetVariable("clothing_colour_last_selected", colour),
                Function(get_custom_hair_colours, colour),
                Function(picker.set_color, hair_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen acc_eye_colour_button(colour):
    $ icon = "button_wardrobe_colour_frame_%s"
    $ icon_but = "button_wardrobe_colour_base"

    frame padding (0,0) xysize (41,40) background None:
        add icon_but:
            matrixcolor TintMatrix(eye_colours[colour])
        imagebutton auto icon:
            action [
                SelectedIf(SetVariable ("player.eye_colour", colour)),
                SetVariable("clothing_colour_last_selected", colour),
                Function(get_custom_eye_colours, colour),
                Function(picker.set_color, eye_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen acc_skin_colour_button(colour):
    $ icon = "button_wardrobe_colour_frame_%s"
    $ icon_but = "button_wardrobe_colour_base"

    frame padding (0,0) xysize (41,40) background None:
        add icon_but:
            matrixcolor TintMatrix(skin_colours[colour])
        imagebutton auto icon:
            action [
                SelectedIf(SetVariable ("player.skin_colour", colour)),
                SetVariable("clothing_colour_last_selected", colour),
                Function(get_custom_skin_colours, colour),
                Function(picker.set_color, skin_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen acc_nips_colour_button(colour):
    $ icon = "button_wardrobe_colour_frame_%s"
    $ icon_but = "button_wardrobe_colour_base"

    frame padding (0,0) xysize (41,40) background None:
        add icon_but:
            matrixcolor TintMatrix(nipple_colours[colour])
        imagebutton auto icon:
            action [
                SelectedIf(SetVariable ("player.nip_colour", colour)),
                SetVariable("clothing_colour_last_selected", colour),
                Function(get_custom_nip_colours, colour),
                Function(picker.set_color, nipple_colours[colour]),
                SetVariable("picker.color_slot", colour),
                Function(refresh_avatar),
                ]

screen acc_screen_hair_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in hair_colours_custom_list:
                use acc_hair_colour_button(i)
        frame padding (0,0) xysize (41,40) background None

screen acc_screen_eyes_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in eye_colours_custom_list:
                use acc_eye_colour_button(i)
        frame padding (0,0) xysize (41,40) background None

screen acc_screen_skin_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in skin_colours_custom_list:
                use acc_skin_colour_button(i)
        frame padding (0,0) xysize (41,40) background None

screen acc_screen_nips_colours():
    vbox:
        hbox anchor (0,0) align (0,0) xysize (50,20):
            for i in nipple_colours_custom_list:
                use acc_nips_colour_button(i)
        frame padding (0,0) xysize (41,40) background None

screen acc_screen_top_button(tabtop, tableft, strip=False):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"
        add "button_wardrobe_tab_" + tabtop:
            if not tab_top_acc == tabtop:
                matrixcolor TintMatrix(wardrobe_colour_selected)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            action [
                Function(If(strip, pc_strip, pc_dress)), 
                SetVariable ("tab_top_acc", tabtop), 
                SetVariable ("tab_left_acc", tableft), 
                Function(player.allure_function),
                Function(set_acc_colours),
                Function(refresh_avatar),
                ]

screen acc_screen_left_button(items):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"
        add "button_wardrobe_tab_" + items:
            if not tab_left_acc == items:
                matrixcolor TintMatrix(wardrobe_colour_selected)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            action [
                SetVariable ("tab_left_acc", items), 
                Function(player.allure_function),
                Function(set_acc_colours),
                Function(refresh_avatar),
                ]

screen acc_screen_left_makeup_button(items):
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"
        add "button_wardrobe_tab_" + items:
            if not tab_left_acc == items:
                matrixcolor TintMatrix(wardrobe_colour_selected)
        add "button_wardrobe_tab_frame_idle"

screen acc_screen_item_makeup_button(items):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_" + items pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title=str.upper(items), text_desc=""),
            unhovered Hide("wardrobe_text"),
            if tab_left_acc != items:
                action [
                    SelectedIf(SetVariable("acc." + items, 1)),
                    SetVariable("tab_left_acc", items),
                    SetVariable("acc.makeup_on", True),
                    Show("wardrobe_text", text_title=str.upper(items), text_desc=""),
                    Function(set_acc_colours),
                    Function(refresh_avatar),
                ]
            else:

                action [
                    SelectedIf(SetVariable("acc." + items, 1)), 
                    SetVariable("acc.makeup_on", True),
                    SetVariable("tab_left_acc", items),
                    SetVariable("acc." + items, If(getattr(acc, items), 0, 1)),
                    Show("wardrobe_text", text_title=str.upper(items), text_desc=""),
                    Function(set_acc_colours),
                    Function(refresh_avatar),
                ],

screen acc_screen_item_hair_button():
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_hair" pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="HAIR DYE", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [SelectedIf(SetVariable("tab_left_acc", "hair")), Show("wardrobe_text", text_title="HAIR DYE", text_desc=""),
            Function(set_acc_colours)]

screen acc_screen_item_hair_neck_button(value):
    $ newvalue = value * 10 - 10
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_hairlength_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="HAIR LENGTH", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("player._hair_length", newvalue)), 
                SetVariable("tab_left_acc", "hair_length"),
                SetVariable("player._hair_length", newvalue), 
                Show("wardrobe_text", text_title="HAIR LENGTH", text_desc=""),
                Function(set_acc_colours)
                ]

screen acc_screen_item_hair_fringe_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_hairfringe_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="HAIR FRINGE", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("player.hair_fringe", value)), 
                SetVariable("tab_left_acc", "hair_fringe"),
                SetVariable("player.hair_fringe", value), 
                Show("wardrobe_text", text_title="HAIR FRINGE", text_desc=""),
                Function(set_acc_colours)
                ]















screen acc_screen_item_hair_p_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_phair_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="PUBIC HAIR", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(value == 0 and player._phair == -10 or value == 1 and player._phair == 10),
                SetVariable("tab_left_acc", "phair"),
                
                Show("wardrobe_text", text_title="PUBIC HAIR", text_desc=""),
                Function(set_acc_colours), 
                Function(If(value == 0, player.phair_wax, player.phair_fullgrow))
                ]

screen acc_screen_item_breastsize_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_breasts_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="BREAST SIZE", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("player.breasts", value)), 
                SetVariable("tab_left_acc", "breasts"),
                SetVariable("player.breasts", value), 
                Show("wardrobe_text", text_title="BREAST SIZE", text_desc=""),
                Function(set_acc_colours)
                ]

screen acc_screen_item_nips_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_nipsize_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="NIPPLE SIZE", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("player.nip_size", value)), 
                SetVariable("tab_left_acc", "nip_size"),
                SetVariable("player.nip_size", value), 
                Show("wardrobe_text", text_title="NIPPLE SIZE", text_desc=""),
                Function(set_acc_colours)
                ]

screen acc_screen_item_eyes_button():
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_eyeliner_1" pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="EYE COLOUR", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [SelectedIf(SetVariable("tab_left_acc", "eyes")), Show("wardrobe_text", text_title="EYE COLOUR", text_desc=""),
            Function(set_acc_colours)]

screen acc_screen_item_skin_button():
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_blush" pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="SKIN COLOUR", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [SelectedIf(SetVariable("tab_left_acc", "skin")), Show("wardrobe_text", text_title="SKIN COLOUR", text_desc=""),
            Function(set_acc_colours)]

screen acc_screen_item_freckles_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_freckles_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text", text_title="FRECKLES", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("skin_effect.face", value)), 
                SetVariable("tab_left_acc", "skin_effect"),
                SetVariable("skin_effect.face", value), 
                Show("wardrobe_text", text_title="FRECKLES", text_desc=""),
                Function(set_acc_colours)]

screen acc_screen_item_makeup_eyeliner_button(value):
    frame padding (0,0) xysize (82,80) background None:
        add "item_makeup_eyeliner_" + str(value) pos (4,4)
        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered Show("wardrobe_text",  text_title="EYELINER", text_desc=""),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("acc.eyeliner", value)),
                SetVariable("tab_left_acc", "eyeliner"),
                Show("wardrobe_text", text_title="EYELINER", text_desc=""),
                Function(set_acc_colours)
                ],

screen acc_screen_item_button(item):
    frame padding (2,2) xysize (126, 80) background None:
        add item[0].class_name pos (1,1)
        imagebutton auto "button_items_frame_%s":
            hovered Show("wardrobe_text", text_title=item[0].name, text_desc=item[0].desc),
            unhovered Hide("wardrobe_text"),
            action [
                SelectedIf(SetVariable("acc." + item[0].clothes_tab, item[0].clothes_number)),
                SetVariable("acc." + item[0].clothes_tab, If(getattr(acc, item[0].clothes_tab) == item[0].clothes_number, 0, item[0].clothes_number)),
                Show("wardrobe_text", text_title=item[0].name, text_desc=item[0].desc)
                ],

image button_wardrobe_tab_buttplug = "perk_buttplug"

screen acc_screen():
    zorder 0
    if cheats == 1:
        frame align (0,0.095):
            text "[tab_top_acc] and [tab_left_acc] and [primary_colour] and [secondary_colour]"
    frame anchor (0,0) align (0.3,0.095) xysize (990,900):
        has vbox
        hbox:
            frame padding (0,0) xysize (82,80) background None:
                add "button_wardrobe_tab_bg"
                add "button_wardrobe_tab_frame_idle"

            use acc_screen_top_button("makeup", "eyeshadow")
            use acc_screen_top_button("items", "glasses")
            use acc_screen_top_button("piercing", "nipring", strip=True)

        hbox:
            vbox:
                frame padding (0,0) xysize (82,80) background None:
                    add "button_wardrobe_tab_bg"
                    add "button_wardrobe_tab_frame_idle"

                if tab_top_acc == "makeup":
                    $ makeup_list = ["eyeliner"]
                    $ makeup_list.append("eyeshadow")
                    $ makeup_list.append("lipstick")
                    $ makeup_list.append("blush")
                    if inv.qty(item_nailpolish):
                        $ makeup_list.append("nails")
                    if inv.qty(item_hairdye):
                        $ makeup_list.append("hair")
                    if inv.qty(item_contacts):
                        $ makeup_list.append("eyes")


                    for i in makeup_list:
                        use acc_screen_left_makeup_button(i)

                elif tab_top_acc == "items":
                    for i in ("glasses", "choker", "mask"):
                        use acc_screen_left_button(i)

                elif tab_top_acc == "piercing":
                    for i in ("nipring", "navelring"):
                        use acc_screen_left_button(i)

            vbox:
                vbox:
                    if tab_top_acc == "makeup" and "hair" in tab_left_acc:
                        use acc_screen_hair_colours()
                    elif tab_top_acc == "makeup" and tab_left_acc == "eyes":
                        use acc_screen_eyes_colours()
                    elif tab_top_acc == "makeup" and tab_left_acc in ["skin", "breasts", "skin_effect"]:
                        use acc_screen_skin_colours()
                    elif tab_top_acc == "makeup" and tab_left_acc in ["nip_size"]:
                        use acc_screen_nips_colours()
                    elif tab_top_acc == "makeup":
                        use acc_screen_makeup_colours()
                    else:
                        use acc_screen_colours()

                hbox:
                    vbox:

                        if tab_top_acc == "makeup":
                            hbox:
                                for i in (1,2,3,4):
                                    use acc_screen_item_makeup_eyeliner_button(i)
                            hbox:
                                use acc_screen_item_makeup_button("eyeshadow")
                            hbox:
                                use acc_screen_item_makeup_button("lipstick")
                            hbox:
                                use acc_screen_item_makeup_button("blush")

                            if inv.qty(item_nailpolish):
                                hbox:
                                    use acc_screen_item_makeup_button("nails")

                            if inv.qty(item_hairdye):
                                hbox:
                                    use acc_screen_item_hair_button()


                            if inv.qty(item_contacts):
                                hbox:
                                    use acc_screen_item_eyes_button()



                    for i in wardrobe.inv:
                        if getattr(i[0], "type") == tab_left_acc:
                            frame padding (0,0) xysize (126, 80) background None:
                                use acc_screen_item_button(i)

    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        has vbox xsize 330 ysize 880
        hbox align (0.5, 1.0):
            use color_picker()

    use acc_screen_wardrobe()
    use acc_screen_return()


screen acc_screen_return(x=0.25, y=0.50):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                If(shop==True, [Function(tab_clothes, tab_top_enter)]),
                Hide("acc_screen"),
                Hide("wardrobe_text"),
                Function(pc_dress),
                SetVariable("tab_left", "top"),
                SetVariable("picker.color_slot", None),
                Jump("world_wardrobe_close")
            ]
screen surgery_screen_return(x=0.25, y=0.50):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Hide("surgery_screen"), 
                Hide("wardrobe_text"), 
                SetVariable("picker.color_slot", None),
                Function(pc_dress), 
                Return(_return)
                ]

screen acc_screen_wardrobe(x=0.25, y=0.42):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_wardrobe" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [
                Hide("acc_screen"),
                Function(pc_dress),
                If(tab_left in clothes_wardrobe_under_list, pc_strip_tops),
                Function(set_wardrobe_colours),
                Function(refresh_avatar),
                Show("wardrobe_screen")
            ]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
