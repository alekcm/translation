init python:
    def vball_image():
        image_list = ["activity_vball_pc"]
        if robin_here():
            image_list.extend(["activity_vball_robin_ass_layered", "activity_vball_robin_ball_layered", "activity_vball_robin_play_layered", "activity_vball_robin_strech_layered"])
        if erika_here():
            image_list.extend(["activity_vball_erika_back_layered", "activity_vball_erika_back_layered"])
        if zahra_here():
            image_list.extend(["activity_vball_zahra_ass_layered", "activity_vball_zahra_front_layered", "activity_vball_zahra_sit_layered"])
        if sandy_here():
            image_list.extend(["activity_vball_sandy_ass_layered", "activity_vball_sandy_ball_layered", "activity_vball_sandy_hand_layered"])
        if rachel_here():
            image_list.extend(["activity_vball_rachel_fall", "activity_vball_rachel_wait", "activity_vball_rachel_wave"])
        
        renpy.scene() 
        renpy.show(renpy.random.choice(image_list))  
        renpy.with_statement(dissolve)

image activity_vball_pc_hands_base_layer:
    "activity_vball_pc_hands_base"
    skin_base_colour_transform()
image activity_vball_pc_hands_shad_layer:
    "activity_vball_pc_hands_shad"
    skin_shad_colour_transform()

image activity_vball_pc = LayeredImageProxy("activity_vball_pc_layeredimage", Transform(align=(0.7, 0.0)))

layeredimage activity_vball_pc_layeredimage:
    always "activity_vball_pc_base"
    always "activity_vball_pc_hands_base_layer"
    always "activity_vball_pc_hands_shad_layer"



layeredimage activity_vball_erika_back_layered:
    always "activity_vball_erika_back_base"
    if people_nude_beach_vball():
        "activity_vball_erika_back_nude"
    else:
        "activity_vball_erika_back_bikini"

layeredimage activity_vball_erika_ball_layered:
    always "activity_vball_erika_ball_base"
    if people_nude_beach_vball():
        "activity_vball_erika_ball_nude"
    else:
        "activity_vball_erika_ball_bikini"







layeredimage activity_vball_robin_ass_layered:
    always "activity_vball_robin_ass_base"
    if not people_nude_beach_vball():
        "activity_vball_robin_ass_bikini"

layeredimage activity_vball_robin_ball_layered:
    always "activity_vball_robin_ball_base"
    if not people_nude_beach_vball():
        "activity_vball_robin_ball_bikini"

layeredimage activity_vball_robin_play_layered:
    always "activity_vball_robin_play_base"
    if not people_nude_beach_vball():
        "activity_vball_robin_play_bikini"

layeredimage activity_vball_robin_strech_layered:
    always "activity_vball_robin_strech_base"
    if not people_nude_beach_vball():
        "activity_vball_robin_strech_bikini"



layeredimage activity_vball_sandy_ass_layered:
    always "activity_vball_sandy_ass_base"
    if people_nude_beach_vball():
        "activity_vball_sandy_ass_nude"
    else:
        "activity_vball_sandy_ass_bikini"

layeredimage activity_vball_sandy_ball_layered:
    always "activity_vball_sandy_ball_base"
    if people_nude_beach_vball():
        "activity_vball_sandy_ball_nude"
    else:
        "activity_vball_sandy_ball_bikini"

layeredimage activity_vball_sandy_hand_layered:
    always "activity_vball_sandy_hand_base"
    if people_nude_beach_vball():
        "activity_vball_sandy_hand_nude"
    else:
        "activity_vball_sandy_hand_bikini"



layeredimage activity_vball_zahra_ass_layered:
    always "activity_vball_zahra_ass_base"
    if not people_nude_beach_vball():
        "activity_vball_zahra_ass_bikini"

layeredimage activity_vball_zahra_front_layered:
    always "activity_vball_zahra_front_base"
    if people_nude_beach_vball():
        "activity_vball_zahra_front_nude"
    else:
        "activity_vball_zahra_front_bikini"

layeredimage activity_vball_zahra_sit_layered:
    always "activity_vball_zahra_sit_base"
    if people_nude_beach_vball():
        "activity_vball_zahra_sit_nude"
    else:
        "activity_vball_zahra_sit_bikini"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
