init python:

















    def get_hair_colour():
        return hair_colours[str(player.hair_colour)]

    def get_hair_fringe_filename():
        if player.hair_style == "haven":
            filename = "pc_hair_fringe_haven"
        else:
            filename = "pc_hair_fringe_" + str(player.hair_fringe)
        return filename
    def get_hair_fringe_shadow_filename():
        if player.hair_style == "haven":
            filename = "pc_hair_fringe_haven_shadow"
        else:
            filename = "pc_hair_fringe_" + str(player.hair_fringe) + "_shadow"
        return filename
    def get_hair_neck_filename(name):
        filename = "pc_hair_" + name + "_" + str(player.hair_neck)
        return filename
    def get_hair_brow_filename():
        filename = "pc_face_brow_" + str(player.brow)
        return filename
    def get_hair_pubic_filename():
        filename = "pc_phair_1_0"
        return filename
    def get_hair_filename(name,preg=True):
        if preg:
            filename = filename + "_" + player.pregnancy
        filename = "pc_phair_" + str(player.phair) + "_" + str(player.pregnancy)
        return filename

    def get_hair_back_filename():
        if player.hair_style == "haven":
            filename = "pc_hair_neck_haven"
        elif player.hair_style == "loose" or player.hair_neck == 1:
            filename = "pc_hair_loose_" + str(player.hair_neck)
        elif player.hair_style == "pig":
            filename = "pc_hair_pig"
        else:
            filename = "pc_hair_tied"
        return filename

    def get_hair_pony_filename():
        if player.hair_style == "haven":
            filename = "pc_hair_fringe_haven"
        elif player.hair_style == "pony":
            if player.hair_neck in (2,3):
                filename = "pc_hair_pony_short"
            elif player.hair_neck == 4:
                filename = "pc_hair_pony_long"
            else:
                filename = "pc_blank"
        elif player.hair_style == "bun":
            if player.hair_neck == 3:
                filename = "pc_hair_bun_small"
            elif player.hair_neck == 4:
                filename = "pc_hair_bun_big"
            else:
                return "pc_blank"
        elif player.hair_style == "pig":
            if player.hair_neck == 2:
                filename = "pc_hair_pig_short"
            elif player.hair_neck == 3:
                filename = "pc_hair_pig_med"
            elif player.hair_neck == 4:
                filename = "pc_hair_pig_long"
            else:
                filename = "pc_blank"
        else:
            return "pc_blank"
        return filename

    def get_hair_back_cg_filename(name):
        if player.hair_style == "haven":
            return name + "_3"
        elif player.hair_style == "loose" or player.hair_neck == 1:
            return name + "_" + str(player.hair_neck)
        elif player.hair_style == "bun":
            return name + "_bun_" + str(player.hair_neck)
        elif player.hair_style == "pony":
            return name + "_pony_" + str(player.hair_neck)
        elif player.hair_style == "pig":
            return name + "_pig_" + str(player.hair_neck)

    def get_hair_front_cg_filename(name):
        if player.hair_style == "haven":
            return name + "_1"
        filename = name + "_" + str(player.hair_fringe)
        return filename



















    def get_eye_colour():
        return eye_colours[str(player.eye_colour)]

    def get_eyeliner_filename():
        if player.eye == 4:
            filename = "pc_face_eyeliner_4"
        else:
            filename = "pc_face_eyeliner_" + str(acc.eyeliner) + "_" + str(player.eye)
        refresh_avatar()
        return filename
    def get_eye_filename():
        filename = "pc_face_eye_" + str(player.eye)
        if renpy.loadable("images/characters/pc/face/eye/" + filename + ".webp"):
            return filename
        else:
            return "pc_blank"
    def get_iris_filename():
        filename = "pc_face_iris_" + str(player.eye)
        if renpy.loadable("images/characters/pc/face/eye/" + filename + ".webp"):
            return filename
        else:
            return "pc_blank"
    def get_cg_filename():
        filename = "pc_face_iris_" + str(player.eye)
        if renpy.loadable("images/characters/pc/face/eye/" + filename + ".webp"):
            return filename
        else:
            return "pc_blank"

    def get_cg_filename(name, has_pregnancy_variations=False): 
        filename = name
        if has_pregnancy_variations:
            
            return filename + "_" + str(player.pregnancy)
        return filename

    def get_writing_colour(body_part):
        if not getattr(writing, body_part):
            return Color("#000") 
        if "tattoo" in getattr(writing, body_part):
            return Color(rgb = (0.227, 0.219, 0.223))
        elif "perm" in getattr(writing, body_part):
            return Color(rgb=(0.1922, 0.1608, 0.4000))
        else:
            return Color(rgb=(0.5020, 0.0902, 0.0902))

    def get_writing_opacity(body_part): 
        if not getattr(writing, body_part):
            return 0
        if "perm" in getattr(writing, body_part):
            return (getattr(writing, body_part)["perm"] * 20 / float(100))
        else:
            return 1


    desire_colours = {
    "1" : Color(rgb = (0.168, 0.486, 0.654)),
    "2" : Color(rgb = (0.333, 0.474, 0.662)),
    "3" : Color(rgb = (0.580, 0.450, 0.678)),
    "4" : Color(rgb = (0.854, 0.423, 0.698)),
    "5" : Color(rgb = (0.996, 0.411, 0.705)),
    "6" : Color(rgb = (0.439, 0.141, 0.141)),
    }

    def get_desire_colour():
        if player.beingraped:  
            return desire_colours["6"]
        elif player.desire > 80:
            return desire_colours["5"]
        elif player.desire > 60:
            return desire_colours["4"]
        elif player.desire > 40:
            return desire_colours["3"]
        elif player.desire > 20:
            return desire_colours["2"]
        else:
            return desire_colours["1"]



transform hair_colour_transform():
    matrixcolor TintMatrix(get_hair_colour())
transform phair_colour_transform():
    matrixcolor TintMatrix(get_hair_colour()) * OpacityMatrix(player.phair / float(10))
transform eye_colour_transform():
    matrixcolor TintMatrix(get_eye_colour())
transform desire_colour_transform(opacity=1):
    matrixcolor TintMatrix(get_desire_colour()) * OpacityMatrix(opacity)
transform opacity_transform(opacity=1):
    matrixcolor OpacityMatrix(opacity)
transform writing_opacity_transform(body_part):
    matrixcolor OpacityMatrix(get_writing_opacity(body_part))
transform writing_transform(body_part):
    matrixcolor ColorizeMatrix(get_writing_colour(body_part), get_writing_colour(body_part)) * OpacityMatrix(get_writing_opacity(body_part))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
