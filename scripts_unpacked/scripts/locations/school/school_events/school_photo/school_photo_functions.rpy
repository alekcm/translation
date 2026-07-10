init python:
    class PhotoClass(object):
        
        
        
        
        def __init__(self):
            school_photo_list.append(self)
            self._done = False 
            self._tasteful = False 
            self._topless = False 
            self._nude = False 
            self._errotic = False 
            self._sex = False
            self._vsex = False 
            self._asex = False 
        
        @property
        def done(self):
            return self._done
        @property
        def tasteful(self):
            return self._tasteful
        @property
        def topless(self):
            return self._topless
        @property
        def nude(self):
            return self._nude
        @property
        def errotic(self):
            return self._errotic
        @property
        def sex(self):
            return self._asex + self._vsex
        @property
        def vsex(self):
            return self._vsex
        @property
        def asex(self):
            return self._asex
        
        
        
        @done.setter
        def done(self, amount):
            self._done += amount
        @tasteful.setter
        def tasteful(self, amount):
            self._tasteful += amount
        @topless.setter
        def topless(self, amount):
            self._topless += amount
        @nude.setter
        def nude(self, amount):
            self._nude += amount
            self._topless += amount
        @errotic.setter
        def errotic(self, amount):
            self._errotic += amount
            self._nude += amonut
            self._topless += amount
        @vsex.setter
        def vsex(self, amount):
            self._vsex += amount
            self._errotic += amount
            self._nude += amount
            self._topless += amount
        @asex.setter
        def asex(self, amount):
            self._asex += amount
            self._errotic += amount
            self._nude += amonut
            self._topless += amount
        
        
        
        
        def take_photo(self, var="done"):
            global school_photo_shoots_done, school_photo_date
            if not var == "done":
                setattr(self,var,1)
            self.done = 1
            school_photo_shoots_done += 1
            school_photo_date = t.day

    def photo_all(photo_var):
        amount = 0
        for i in school_photo_list:
            amount += getattr(i, photo_var)
        return amount

    def photo_clothes_vball_modest():
        work.reset_clothes()
        work.top = 8
        work.bottom = 8
        work.bra = c.bra
        work.pants = c.pants
        
        work.top_primary_colour = "crimson"
        work.top_secondary_colour = "pink"
        work.top_primary_trans = "trans_normal"
        work.top_secondary_trans = "trans_normal"
        
        work.bottom_primary_colour = "crimson"
        work.bottom_secondary_colour = "pink"
        work.bottom_primary_trans = "trans_normal"
        work.bottom_secondary_trans = "trans_normal"
        
        work.bra_primary_colour = c.bra_primary_colour
        work.bra_secondary_colour = c.bra_secondary_colour
        work.pants_primary_colour = c.pants_primary_colour
        work.pants_secondary_colour = c.pants_secondary_colour

    def photo_clothes_dance_modest():
        work.reset_clothes()
        work.top = 20
        work.bottom = 13
        work.bra = 3
        work.pants = 1
        work.socks = 1
        
        work.top_primary_colour = "white"
        work.bottom_primary_colour = "black"
        work.bra_primary_colour = "grey"
        work.bra_secondary_colour = "grey"
        work.pants_primary_colour = "black"
        work.pants_secondary_colour = "black"
        work.socks_primary_colour = "black"
        work.socks_secondary_colour = "black"

    def photo_clothes_dance_revealing():
        work.reset_clothes()
        work.top = 19
        work.bottom = 13
        work.pants = 5
        
        work.top_primary_colour = "white"
        work.bottom_primary_colour = "black"
        work.pants_primary_colour = "hotpink"

    def photo_clothes_witch():
        work.reset_clothes()
        work.outfit = 101
        work.hat = 101
        work.socks = 101
        work.pants = 2
        
        work.outfit_primary_colour = "pumpkin"
        work.outfit_secondary_colour = "black"
        work.hat_primary_colour = "pumpkin"
        work.hat_secondary_colour = "black"
        work.socks_primary_colour = "pumpkin"
        work.socks_secondary_colour = "black"
        work.pants_primary_colour = "pumpkin"
        work.pants_secondary_colour = "black"

    def photo_clothes_catgirl():
        work.reset_clothes()
        work.top = 102
        work.bottom = 102
        work.hat = 102
        work.socks = 6
        work.gloves = 1
        
        work.top_primary_colour = "black"
        work.top_secondary_colour = "pink"
        work.bottom_primary_colour = "black"
        work.bottom_secondary_colour = "pink"
        work.hat_primary_colour = "black"
        work.socks_primary_colour = "black"
        work.socks_secondary_colour = "pink"
        work.gloves_primary_colour = "black"
        work.gloves_secondary_colour = "pink"

    def photo_clothes_santa():
        work.reset_clothes()
        work.outfit = 100
        work.hat = 100
        work.socks = 100
        work.pants = 2
        
        work.outfit_primary_colour = "red"
        work.outfit_secondary_colour = "white"
        work.hat_primary_colour = "white"
        work.hat_secondary_colour = "red"
        work.socks_primary_colour = "white"
        work.socks_secondary_colour = "red"
        work.pants_primary_colour = "red"
        work.pants_secondary_colour = "red"

    def photo_acc_santa():
        accchangebak = copy.copy(acc)
        
        acc.makeup_on = True
        acc.eyeshadow = 1
        acc.blush = 0
        acc.lipstick = 1
        acc.nails = 1
        
        acc.eyeshadow_primary_colour = "red"
        acc.eyeliner_primary_colour = "crimson"
        acc.lipstick_primary_colour = "red"
        acc.nails_primary_colour = "red"

    def photo_clothes_elf():
        work.reset_clothes()
        work.outfit = 103
        work.hat = 100
        work.socks = 6
        work.pants = 2
        work.gloves = 2
        
        work.outfit_primary_colour = "lime"
        work.outfit_secondary_colour = "white"
        work.hat_primary_colour = "white"
        work.hat_secondary_colour = "lime"
        work.socks_primary_colour = "white"
        work.socks_secondary_colour = "red"
        work.gloves_primary_colour = "white"
        work.gloves_secondary_colour = "red"
        work.pants_primary_colour = "white"
        work.pants_secondary_colour = "white"

    def photo_acc_elf():
        accchangebak = copy.copy(acc)
        
        acc.makeup_on = True
        acc.eyeshadow = 1
        acc.blush = 0
        acc.lipstick = 1
        acc.nails = 1
        
        acc.eyeshadow_primary_colour = "lime"
        acc.eyeliner_primary_colour = "green"
        acc.lipstick_primary_colour = "red"
        acc.nails_primary_colour = "red"





    def photo_advance_checker(var):
        if var == "done":
            return
        elif not any(var in string for string in school_photo_quest.list):
            if renpy.has_label("school_photo_quest_photoshoot_warning_" + var):
                renpy.call("school_photo_quest_photoshoot_warning_" + var)

    def photo_pay(var):
        if var == "intro":
            amount = 25
        elif var == "done":
            amount = 50
        elif var == "tasteful":
            amount = 75
        elif var == "topless":
            amount = 85
        elif var == "nude":
            amount = 100
        elif var == "errotic":
            amount = 150
        elif var in ("vsex", "asex"):
            amount = 200
        else:
            amount = 50
        player.add_money(amount)

default school_photo_list = []
default school_photo_date = 0
default school_photo_shoots_done = 0
default school_photo_special_request = False

default school_photo_intro_quest_stage = 0
default school_photo_intro_quest_complete = False
default school_photo_intro_quest_reason = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
