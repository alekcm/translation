init python:

    def show_whore_image():
        image_list = ["activity_whore_finger", "activity_whore_smile"]
        if dis(dis_truckstop):
            if cass_here():
                image_list.append("cass_pose_whore_1")
                image_list.append("cass_pose_whore_2")
        
        for i in image_list:
            if renpy.showing(i):
                image_list.remove(i)
        renpy.scene()
        renpy.show(renpy.random.choice(image_list))
        renpy.with_statement(dissolve)

    def whore_customer_weight():
        base = 500
        if loc(loc_motel_pinkroom):
            base = base * 0.8
        if not t.timeofday == "night":
            base = base * 3
        if not dis(dis_truckstop):
            base = base * 3
        if weather_var in (3,4):
            base = base * 2
        
        return weightgen(player.allure, int(base))

    def whore_experiance_weight():
        
        
        
        if quest_whore.vsex <= 10:
            
            return True
        elif quest_whore.vsex > 30:
            
            return False
        
        if numgen(0, 30) < quest_whore.vsex:
            return False
        else:
            return True
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
