init -1:
    transform polaroid:
        anchor (0.5,0.5) xalign 0.65 yalign 0.0 zoom 0.85 rotate_pad False rotate renpy.random.randint(-8, 8)
        on show:
            alpha 0
            linear 0.1 zoom 0.9 alpha 1.0
            linear 0.1 zoom 0.85
            pause 3.0
            linear 0.5 alpha 0.0

init python:

    class Polaroid(object):
        def __init__(self, name, image, keywords=[], additional_keywords=[], outfit=[], who=["pc"], unlock_conditions=""):
            self.name = name 
            self.image = image 
            self.keywords = keywords 
            self.additional_keywords = additional_keywords 
            self.outfit = outfit 
            self.who = who 
            self.unlock_conditions = unlock_conditions 
            self.set_list()
        
        def set_list(self):
            global polaroid_list
            add_to_list(polaroid_list, self)
        
        def unlock(self):
            if not self in polaroid_list_unlocked:
                add_to_list(polaroid_list_unlocked, self)
        
        @property
        def unlocked(self):
            if self in polaroid_list_unlocked:
                return True
            else:
                return False

    def has_photos_to_sell():
        if not all(x in polaroid_list_sold for x in polaroid_list_unlocked):
            return True
        else:
            return False

    def photo_has_others(): 
        global polaroid_list_unlocked, polaroid_list_sold
        for i in polaroid_list_unlocked:
            if not i in polaroid_list_sold and i.who:
                return True
        else:
            return False

    def felix_not_have_photo_type(type): 
        global polaroid_list_sold, polaroid_list_unlocked
        for i in polaroid_list_unlocked:
            if i not in polaroid_list_sold and type in i.additional_keywords:
                return True
        else:
            return False

    def felix_photo_price():
        price = {"normal": 10, "slutty": 20, "underwear": 30, "nude": 50, "porn": 75, "bikini": 10}
        total = 0
        for i in polaroid_list_unlocked:
            if not i in polaroid_list_sold:
                if "bikini" in i.additional_keywords:
                    total += price["bikini"]
                
                if "porn" in i.additional_keywords:
                    total += price["porn"]
                elif "nude" in i.additional_keywords:
                    total += price["nude"]
                elif "underwear" in i.additional_keywords:
                    total += price["underwear"]
                elif "slutty" in i.additional_keywords:
                    total += price["slutty"]
                else:
                    total += price["normal"]
        return total

    def felix_sell_photos():
        player.add_money(felix_photo_price())
        for i in polaroid_list_unlocked:
            add_to_list(polaroid_list_sold, i)


    def show_activity_image(key, additional_key=[]): 
        global tab_top, polaroid_list_unlocked
        
        if not (inv.qty(item_polaroid_camera) and inv.qty(item_polaroid_blank)):
            return "No camera"
            return
        
        
        image_list = []
        additional_keys = additional_key
        here_list = npc_check_here()
        
        if c.underwear:
            additional_keys.append("underwear")
        if c.nude:
            additional_keys.append("nude")
        if c.cansee_breasts:
            additional_keys.append("topless")
        if player.has_perk(perk_slutty):
            additional_keys.append("slutty")
        
        for k in polaroid_list:
            if k.outfit and not tab_top in k.outfit:
                pass
            if key in k.keywords:
                if k.additional_keywords:
                    if any(x in k.additional_keywords for x in additional_keys):
                        image_list.append(k)
                else:
                    image_list.append(k)
                
                who_list = k.who
                
                if "pc" in who_list:
                    who_list.remove("pc")
                if who_list:
                    for people in k.who:
                        if not all(x in here_list for x in k.who) and k in image_list:
                            image_list.remove(k)
        
        if image_list:
            show_image = renpy.random.choice(image_list)
            if not show_image in polaroid_list_unlocked:
                add_to_list(polaroid_list_unlocked, show_image)
                inv.drop(item_polaroid_blank, notif=False)
                show_notif_popup("Recieved " + show_image.name + " polaroid")
                renpy.show_screen("polaroid_popup", show_image.image)
                inv.take(item_polaroid_taken, notif=False)
                show_image.unlock()
        
        return image_list

default polaroid_list = []
default polaroid_list_unlocked = []
default polaroid_list_sold = []

screen polaroid_popup(polaroid_image):
    modal False
    zorder 1
    frame at polaroid:
        background None
        add polaroid_image
    timer 4 action Hide ('polaroid_popup')

label polaroids_call:
    $ polaroid_list = [ ]
    $ polaroid_activity_soccer_1 = Polaroid("Playing football with the boys", "polaroid_activity_soccer_1", ["soccer"])
    $ polaroid_activity_soccer_2 = Polaroid("The boys are wearing me out", "polaroid_activity_soccer_2", ["soccer"])
    $ polaroid_activity_soccer_3 = Polaroid("You can't catch me", "polaroid_activity_soccer_3", ["soccer", "running"])

    $ polaroid_activity_bikini_1 = Polaroid("Splish splash", "polaroid_activity_bikini_1", ["running"], outfit=["swim"])
    $ polaroid_activity_bikini_2 = Polaroid("Fun at the beach", "polaroid_activity_bikini_2", ["relax", "swimming"], outfit=["swim"])
    $ polaroid_activity_bikini_3 = Polaroid("Getting a tan", "polaroid_activity_bikini_3", ["sunbathe"], ["slutty"], outfit=["swim"])

    $ polaroid_beach_bums = Polaroid("Beach bums", "polaroid_beach_bums", ["sunbathe", "relax", "talk"], outfit=["swim"], who=["zahra", "erika", "sandy"])
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
