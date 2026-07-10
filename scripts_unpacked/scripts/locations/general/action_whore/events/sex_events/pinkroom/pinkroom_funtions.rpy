init python:

    def show_pinkroom_image():
        image_list = ["activity_windowshow_front", "activity_windowshow_ass"]
        
        renpy.scene()
        renpy.show(renpy.random.choice(image_list))
        renpy.with_statement(dissolve)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
