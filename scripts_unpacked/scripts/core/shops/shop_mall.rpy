define tab_left_shop = "jacket"


label mall_screen_label:
    hide screen travel_screen
    hide screen travel_but_text
    show screen mall_screen
    $ renpy.pause(hard=True)

screen mall_screen:
    zorder 0
    frame:
        xanchor 0.0
        yanchor 0.0
        xalign 0.3
        yalign 0.095
        xsize 1300
        ysize 900
        add "mall_map"
        imagebutton auto "mall_school_%s":
            action [Hide("mall_screen"), Hide("shop_desc"), SetVariable ("shop_open", "school"), SetVariable ("tab_left_shop", "top"),Function(shop_set_backup), Show("shop_interface")]
            hovered Show("shop_desc", text_name="SCHOOL SPIRIT", text_desc="Everything you will ever need for school")
            unhovered Hide("shop_desc") focus_mask True
        imagebutton auto "mall_sport_%s":
            action [Hide("mall_screen"), Hide("shop_desc"), SetVariable ("shop_open", "sport"), SetVariable ("tab_left_shop", "top"),Function(shop_set_backup), Show("shop_interface")]
            hovered Show("shop_desc", text_name="SPORT EXPERT", text_desc="Clothing and equipment for all your sporting needs.")
            unhovered Hide("shop_desc") focus_mask True
        imagebutton auto "mall_meow_%s":
            action [Hide("mall_screen"), Hide("shop_desc"), SetVariable ("shop_open", "meow"), SetVariable ("tab_left_shop", "top"),Function(shop_set_backup), Show("shop_interface")]
            hovered Show("shop_desc", text_name="MEOW", text_desc="Clothing for all the fasionable girls.")
            unhovered Hide("shop_desc") focus_mask True
        imagebutton auto "mall_underwear_%s":
            action [Hide("mall_screen"), Hide("shop_desc"), SetVariable ("shop_open", "underwear"), SetVariable ("tab_left_shop", "top"),Function(shop_set_backup), Show("shop_interface")]
            hovered Show("shop_desc", text_name="INTIMII", text_desc="Intimate apparel shop.")
            unhovered Hide("shop_desc") focus_mask True
        imagebutton auto "mall_cosplay_%s":
            action [Hide("mall_screen"), Hide("shop_desc"), SetVariable ("shop_open", "cosplay"), SetVariable ("tab_left_shop", "top"),Function(shop_set_backup), Show("shop_interface")]
            hovered Show("shop_desc", text_name="COSPLAY CLUB", text_desc="Fancy dress, cosplay and seasonal outfits.")
            unhovered Hide("shop_desc") focus_mask True
    imagebutton auto "poi_return_%s" action [Hide("mall_screen"), Show("travel_screen")] xalign 0.25 yalign 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
