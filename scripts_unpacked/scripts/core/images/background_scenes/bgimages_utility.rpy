define config.gl2 = True

init -10 python:
    weather_colours = {

    "winter_day" : Color(rgb = (0.8,0.8,0.8)),
    "winter_dawn" : Color(rgb = (0.905, 0.768, 0.596)),
    "winter_night" : Color(rgb = (0.458, 0.470, 0.6)),

    "noshad_day" : Color(rgb = (0.8,0.8,0.8)),
    "noshad_dawn" : Color(rgb = (0.905, 0.768, 0.596)),
    "noshad_night" : Color(rgb = (0.458, 0.470, 0.6)),

    "shadow_day" : Color(rgb = (1,1,1)),
    "shadow_dawn" : Color(rgb = (0.905, 0.768, 0.596)),
    }

    weather_colours_inside = {

    "day" : Color(rgb = (1,1,1)),
    "dawn" : Color(rgb = (0.964, 0.917, 0.854)),
    "night" : Color(rgb = (0.756, 0.760, 0.823)),
    }

    weather_colours_outside = {

    "day" : Color(rgb = (1,1,1)),
    "dawn" : Color(rgb = (0.905, 0.768, 0.596)),
    "night" : Color(rgb = (0.458, 0.470, 0.6)),
    }

    weather_colours_dark_inside = {

    "day" : Color(rgb = (1,1,1)),
    "dawn" : Color(rgb = (0.905, 0.768, 0.596)),
    "night" : Color(rgb = (0.458, 0.470, 0.6)),
    }

    weather_colour_avatar = Color(rgb = (1,1,1))

    def get_avatar_weather_colour():
        global weather_colour_avatar
        return weather_colour_avatar



    def get_weather_colour(is_inside_but_dark):
        global weather_colour_avatar
        if not loc_cur.outside:
            if is_inside_but_dark:
                filename = t.timeofday
                weather_colour_avatar = weather_colours_dark_inside[filename]
                return weather_colours_dark_inside[filename]
            else:
                filename = t.timeofday
                weather_colour_avatar = weather_colours_inside[filename]
                return weather_colours_inside[filename]
        elif t.month == "Winter":
            filename = "winter_" + str(t.timeofday)
        elif not t.timeofday == "night" and weather_var == 1:
            filename = "shadow_" + str(t.timeofday)
        else:
            filename = "noshad_" + str(t.timeofday)
        
        if t.timeofday == "day" and t.hour in (t.timeofday_check()[0], t.timeofday_check()[-1]):
            return get_blend_color_weather(get_weather_colour_day(), If(t.hour == t.timeofday_check()[-1], t.minute / float(60), 1 - (t.minute / float(60))))
        elif t.timeofday == "dawn":
            return get_blend_color_weather(get_weather_colour_night(), If(t.hour == t.timeofday_check()[-1] + 1, 1 - t.minute / float(60), t.minute / float(60)))
        weather_colour_avatar = weather_colours[filename]            
        return weather_colours[filename]

    def get_weather_colour_day():
        if not loc_cur.outside:
            if is_inside_but_dark:
                weather_colour_avatar = weather_colours_dark_inside["day"]
                return weather_colours_dark_inside["day"]
            else:
                weather_colour_avatar = weather_colours_inside["day"]
                return weather_colours_inside["day"]
        elif t.month == "Winter":
            filename = "winter_day"
        elif not t.timeofday == "night" and weather_var == 1:
            filename = "shadow_day"
        else:
            filename = "noshad_day"           
        return weather_colours[filename]

    def get_weather_colour_dawn():
        if not loc_cur.outside:
            if is_inside_but_dark:
                weather_colour_avatar = weather_colours_dark_inside["dawn"]
                return weather_colours_dark_inside["dawn"]
            else:
                weather_colour_avatar = weather_colours_inside["dawn"]
                return weather_colours_inside["dawn"]
        elif t.month == "Winter":
            filename = "winter_dawn"
        elif not t.timeofday == "night" and weather_var == 1:
            filename = "shadow_dawn"
        else:
            filename = "noshad_dawn"           
        return weather_colours[filename]

    def get_weather_colour_night():
        if not loc_cur.outside:
            if is_inside_but_dark:
                weather_colour_avatar = weather_colours_dark_inside["night"]
                return weather_colours_dark_inside["night"]
            else:
                weather_colour_avatar = weather_colours_inside["night"]
                return weather_colours_inside["night"]
        elif t.month == "Winter":
            filename = "winter_night"
        else:
            filename = "noshad_night"           
        return weather_colours[filename]


    def get_blend_color_weather(colour_input, front_alpha=1, back_alpha=0):  
        color1 = colour_input
        if len(color1) < 4:
            color1 = colour_input[0]
        color2 = get_weather_colour_dawn()
        if len(color2) < 4:
            color2 = get_weather_colour_dawn()[0]
        front_alpha = float(front_alpha)
        alpha = (1.0 - (1.0 - back_alpha)*(1.0 - front_alpha));
        red   = (color1[0]  * (1.0 - front_alpha) + color2[0]   * front_alpha);
        green = (color1[1]  * (1.0 - front_alpha) + color2[1]   * front_alpha);
        blue  = (color1[2]  * (1.0 - front_alpha) + color2[2]   * front_alpha);
        return Color((int(red), int(green), int(blue)))


    def get_bg_brightness():
        brightness = 1
        saturation = 1
        if weather_var > 1 and not t.hour in dark and not t.month == "Winter":
            brightness = 0.85
        if t.month == "Summer" and weather_var == 1:
            brightness = 1.2
        if t.month in "Winter":
            saturation = 0.75
        elif weather_var > 1 and not t.hour in dark:
            saturation = 0.9
        return brightness, saturation

    def get_background_imagename():
        filename = "bg_" + loc_cur.bg_name
        return filename

    def get_background_filename(name="none", outside=True, winter=True, night=False): 
        if name == "none":
            filename = "bg_" + loc_cur.name
            return filename
        filename = "bg_" + name
        
        
        if night and t.timeofday == "night":
            filename = filename + "_night"
        elif outside:
            if t.hour in dark or weather_var > 1:
                filename = filename + "_noshad"
            else:
                filename = filename + "_shadow"
        return filename

    def get_background_noshad_filename(name="none", winter=True):
        if name == "none":
            filename = "bg_" + loc_cur.name
            return filename
        filename = "bg_" + name
        if winter and t.month == "Winter":
            filename = filename + "_winter"
        else:
            filename = filename + "_scene"
        return filename



    def get_image_filename():
        filename = "bg_" + loc_cur.name

    def get_background_filename_nowinter():
        filename = "bg_" + loc_cur.name
        if t.month == "Winter":
            filename = filename + "_winter"
        elif t.hour in dark or weather_var > 1:
            filename = filename + "_noshad"
        else:
            filename = filename + "_shadow"
        
        if not renpy.loadable("*/" + filename):
            get_background_filename_nowinter()
            return "bg_" + loc_cur.name
        
        return filename

    def get_button_outside_colour():
        
        filename = t.timeofday
        return weather_colours_outside[filename]

    def get_button_inside_colour():
        
        filename = t.timeofday
        return weather_colours_inside[filename]


transform bg_tint_transform(is_inside_but_dark=False):
    matrixcolor SaturationMatrix(get_bg_brightness()[1]) * SaturationMatrix(get_bg_brightness()[0]) * TintMatrix(get_weather_colour(is_inside_but_dark))
transform avatar_tint_transform():
    matrixcolor SaturationMatrix(get_bg_brightness()[1]) * SaturationMatrix(get_bg_brightness()[0]) * TintMatrix(get_avatar_weather_colour())
transform sky_dawn_transform():
    matrixcolor OpacityMatrix(bg_sky_trans())
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
