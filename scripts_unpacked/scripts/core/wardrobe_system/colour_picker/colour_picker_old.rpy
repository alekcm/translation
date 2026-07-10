image colour_bar_red = Solid("#bd0000")
image colour_bar_green = Solid("#00b618")
image colour_bar_blue = Solid("#0300b8")
image colour_bar_grey = Solid("#a0a0a0")
image colour_bar_thumb = Solid("#d84794", height=10, width=30)

screen colour_slider(colour):

    frame xysize (350,10) background None
    frame padding (1,1) background None:
        has bar
        xysize (330,10)
        value VariableValue(colour + "_value", round(1.0,3))
        right_bar "colour_bar_grey"
        left_bar "colour_bar_" + colour
        thumb "colour_bar_thumb"

        if "hair" in tab_left_acc:
            changed (update_hair_colours(clothing_colour_last_selected, red_value, green_value, blue_value))
        elif tab_left_acc == "eyes":
            changed (update_eye_colours(clothing_colour_last_selected, red_value, green_value, blue_value))
        else:
            changed (update_clothing_colours(clothing_colour_last_selected, red_value, green_value, blue_value))


screen colour_picker:

    frame:
        xysize (400,400)
        align (0.5, 0.5)
        padding (3,3)
        has vbox

        use colour_slider("red")
        use colour_slider("blue")
        use colour_slider("green")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
