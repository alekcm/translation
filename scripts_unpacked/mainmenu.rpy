init python:

    def main_menu_image_cycle():
        
        main_menu_image_start()


    def main_menu_image_start_devil():
        renpy.show("mainmenu conf look_devil")
        
        renpy.show(renpy.random.choice(["mainmenu devil devil_talk devil_hair tee", "mainmenu devil devil_talk devil_hair strapless"]))
        
        renpy.pause(2)
        renpy.show("mainmenu grin")
        
        renpy.pause(1)
        renpy.show("mainmenu forward")
        
        renpy.show(renpy.random.choice(["mainmenu halter", "mainmenu croptop"]))
        
        renpy.pause(4)
        
        renpy.show("mainmenu devil_pout conf look_angel")
        
        renpy.show(renpy.random.choice(["mainmenu angel angel_talk angel_hair uni", "mainmenu angel angel_talk angel_hair sumdress"]))
        
        renpy.pause(2)
        renpy.show("mainmenu smile")
        
        renpy.pause(1)
        renpy.show("mainmenu forward devil_talk")
        
        renpy.show(renpy.random.choice(["mainmenu cardigan", "mainmenu blouse"]))
        
        
        return
layeredimage mainmenu_1:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_smile"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_2:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_angel"
    always:
        "mainmenu_middle_mouth_conf"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_3:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_talk"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_angel"
    always:
        "mainmenu_middle_mouth_conf"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_4:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_talk"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_angel"
    always:
        "mainmenu_middle_mouth_smile"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_5:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_talk"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_smile"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_6:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_talk"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_smile"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_7:
    always:
        "mainmenu_bg"
    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_devil"
    always:
        "mainmenu_middle_mouth_conf"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_8:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_tee"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_devil"
    always:
        "mainmenu_middle_mouth_conf"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_9:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_tee"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_devil"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_10:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_tee"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_11:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_tee"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_halter"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_12:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_tee"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"
    always:
        "mainmenu_devil_horns"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_halter"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_13:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_devil"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"
    always:
        "mainmenu_devil_horns"

    always:
        "mainmenu_angel_body"
    always:
        "mainmenu_angel_face_pout"
    always:
        "mainmenu_angel_hair"
    always:
        "mainmenu_angel_clothes_uni"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_halter"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_14:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_devil_body"
    always:
        "mainmenu_devil_clothes_devil"
    always:
        "mainmenu_devil_face_talk"
    always:
        "mainmenu_devil_hair"
    always:
        "mainmenu_devil_horns"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_halter"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15a:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_halter"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15b:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_crop"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15c:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_blouse"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15d:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_dress"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15e:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_shirt"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"
layeredimage mainmenu_15f:
    always:
        "mainmenu_bg"

    always:
        "mainmenu_middle_body"
    always:
        "mainmenu_middle_clothes_cardigan"
    always:
        "mainmenu_middle_eye_forward"
    always:
        "mainmenu_middle_mouth_grin"
    always:
        "mainmenu_middle_hair"

image mainmenu:

    "mainmenu_1"
    pause 2
    "mainmenu_2" with Dissolve(0.5)
    pause 0.5
    "mainmenu_3" with Dissolve(5)
    pause 5
    "mainmenu_4" with Dissolve(0.5)
    pause 0.5
    "mainmenu_5" with Dissolve(0.5)
    pause 0.5
    "mainmenu_6" with Dissolve(2)
    pause 5
    "mainmenu_7" with Dissolve(0.5)
    pause 0.5
    "mainmenu_8" with Dissolve(5)
    pause 5
    "mainmenu_9" with Dissolve(0.5)
    pause 0.5
    "mainmenu_10" with Dissolve(0.5)
    pause 0.5
    "mainmenu_11" with Dissolve(5)
    pause 5
    "mainmenu_12" with Dissolve(5)
    pause 5
    "mainmenu_13" with Dissolve(5)
    pause 8
    "mainmenu_14" with Dissolve(5)
    pause 8
    "mainmenu_15a" with Dissolve(5)
    pause 8
    block:
        choice:
            "mainmenu_15a" with Dissolve(2)
        choice:
            "mainmenu_15b" with Dissolve(2)
        choice:
            "mainmenu_15c" with Dissolve(2)
        choice:
            "mainmenu_15d" with Dissolve(2)
        choice:
            "mainmenu_15e" with Dissolve(2)
        choice:
            "mainmenu_15f" with Dissolve(2)
        pause 5
        repeat
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
