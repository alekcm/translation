






























default picker = ColorPicker(300, 300, "#ff8335")

screen color_picker():











    default picker_hex = DynamicDisplayable(picker_hexcode, picker=picker)

    style_prefix 'cpicker'







    vbox:
        spacing 10
        use wardrobe_clothes_cycle()



        bar value FieldValue(picker, "hue_rotation", 1.0, action=refresh_avatar)

        add picker
























style cpicker_vbox:
    align (0.5, 0.5)
    spacing 25
style cpicker_hbox:
    align (0.5, 0.5)
    spacing 25
style cpicker_vbar:
    xysize (50, 600)
    base_bar At(Transform("#000", xysize=(50, 600)), spectrum(horizontal=False))
    thumb Transform("selector_bg", xysize=(50, 20))
    thumb_offset 10
style cpicker_bar:
    xysize (300, 50)
    base_bar At(Transform("#000", xysize=(300, 50)), spectrum())
    thumb Transform("selector_bg", xysize=(20, 50))
    thumb_offset 10
style cpicker_text:
    color "#fff"
style cpicker_button:
    padding (4, 4) insensitive_background "#fff"
style cpicker_button_text:
    color "#aaa"
    hover_color "#fff"
style cpicker_image_button:
    xysize (104, 104)
    padding (4, 4)
    hover_foreground "#fff2"




default picker2 = ColorPicker(600, 600, "#f93c3e",
    
    
    
    
    saved_colors={0 : "#f93c3e", 1 : "#ff8335"},
    
    
    last_saved_color=0)


default picker_swatch_v2 = DynamicDisplayable(picker_color, picker=picker2,
    xsize=100, ysize=100)


default picker_hex_v2 = DynamicDisplayable(picker_hexcode, picker=picker2)

screen color_picker_v2():


    default current_color = 0

    style_prefix 'cpicker'

    add "#21212d"

    hbox:

        vbar value FieldValue(picker2, "hue_rotation", 1.0)


        vbox:
            add picker2

            bar value FieldValue(picker2, "hue_rotation", 1.0)

        vbox:
            xsize 200 spacing 10 align (0.0, 0.0)


            for color_key in [0, 1]:
                if current_color == color_key:
                    button:


                        add picker_swatch_v2
                else:
                    imagebutton:


                        idle picker2.get_color(color_key)




                        action [Function(picker2.save_color, current_color),
                            SetScreenVariable("current_color", color_key),
                            Function(picker2.swap_to_saved_color, color_key)]


            add picker_hex_v2

            text "R: [picker2.color.rgb[0]:.2f]"
            text "G: [picker2.color.rgb[1]:.2f]"
            text "B: [picker2.color.rgb[2]:.2f]"

    textbutton "Return" align (1.0, 1.0) action Return()





screen four_corner_picker():




    default picker = ColorPicker(600, 600,
        four_corners=("#ff8335", "#f93c3e", "#292835", "#f7f7ed"))


    default picker_swatch = DynamicDisplayable(picker_color, picker=picker,
        xsize=100, ysize=100)


    default picker_hex = DynamicDisplayable(picker_hexcode, picker=picker)

    style_prefix 'cpicker'

    add "#21212d"

    hbox:
        spacing 25 align (0.5, 0.5)

        vbox:

            add picker


            bar value FieldValue(picker, "hue_rotation", 1.0) base_bar "#fff"
        vbox:
            xsize 200 spacing 10 align (0.0, 0.0)

            add picker_swatch


            add picker_hex

            text "R: [picker.color.rgb[0]:.2f]"
            text "G: [picker.color.rgb[1]:.2f]"
            text "B: [picker.color.rgb[2]:.2f]"



    textbutton "Return" action Return(picker.color) align (1.0, 1.0)




default chosen_color = "#8b0f55"
label how_to_use_color_picker():
    "Soon, you will be shown a colour picker."


    call screen color_picker()


    $ chosen_color = _return.hexcode

    $ color_tag = "{color=%s}" % chosen_color
    "[color_tag]You chose the colour [chosen_color].{/color}"


    "The next picker will let you select two different colours."
    call screen color_picker_v2()


    $ chosen_color1 = picker2.get_color(0).hexcode
    $ color1_tag = "{color=%s}" % chosen_color1
    $ chosen_color2 = picker2.get_color(1).hexcode
    $ color2_tag = "{color=%s}" % chosen_color2
    "[color1_tag]The first colour was [chosen_color1],{/color}[color2_tag] and the second was [chosen_color2].{/color}"


    "Next, you will be shown a four-corner colour picker."
    call screen four_corner_picker()
    $ chosen_color = _return.hexcode
    $ color_tag = "{color=%s}" % chosen_color
    "[color_tag]You chose the colour [chosen_color].{/color}"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
