init python:


    class BodyPaint(object):
        def __init__(self):
            self.larm = 0
            self.rarm = 0
            self.chest = 0
            self.lnip = 0
            self.rnip = 0
            self.uboob = 0
            self.belly = 0
            self.vag = 0
            self.pubic = 0
            self.anus = 0
            self.ass = 0
            self.rleg = 0
            self.lleg = 0
            self.face = 0
            self.forehead = 0
            self.special = 0
            self.ass_counter = 0
        
        
        def heal_ass(self):
            if self.ass:
                if self.ass >= 1:
                    self.ass = 1
                self.ass -= 0.1
                if self.ass < 0.0:
                    self.ass = 0.0
            if player.has_perk(perk_spanked_ass) and self.ass < 0.4:
                player.remove_perk(perk_spanked_ass)
        
        def bruise_ass(self, amount=0.1): 
            self.ass += amount
            if self.ass >= 1:
                self.ass = 1
            if bruise.ass > 0.6:
                player.add_perk(perk_spanked_ass)
            refresh_avatar()
        
        def harm(self, where, amount=1):
            
            
            setattr(self, where, (getattr(self, where) +amount))
            
            if getattr(self, where) > 4:
                setattr(self, where, 4)
        
        def heal(self): 
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "pubic", "anus"):
                if isinstance(getattr(self, i), str):
                    setattr(self, i, 0)
                elif getattr(self, i) > 0:
                    if getattr(self, i) > 4:
                        setattr(self, i, 4)
                    else:
                        setattr(self, i, max(getattr(self, i) -numgen(1,2), 0))
        
        def heal_all(self): 
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "ass", "pubic", "anus"):
                if getattr(self, i) > 0:
                    setattr(self, i, 0)
        
        
        def can_write(self, body_part, what_pen="temp"):
            if isinstance(getattr(self, body_part), dict):
                if "tattoo" in getattr(self, body_part) or ("perm" in getattr(self, body_part) and getattr(self, body_part)["perm"] >= 5) or ("temp" in getattr(self, body_part) and what_pen == "temp"):
                    return False
                else:
                    return True
            else:
                return True
        
        
        def add_writing(self, body_part, what_pen): 
            if isinstance(getattr(self, body_part), dict): 
                if "tattoo" in getattr(self, body_part): 
                    return
                
                elif what_pen == "tattoo":
                    setattr(self, body_part, {what_pen: 5})
                
                elif "perm" in getattr(self, body_part):
                    if what_pen == "perm":
                        setattr(self, body_part, {what_pen: 5})
                    else:
                        setattr(self, body_part, getattr(self, body_part)["perm"] + 1)    
                else: 
                    return
            
            else:
                setattr(self, body_part, {what_pen: 5})
            refresh_avatar()
        
        def add_writing_random(self, what_pen="temp"): 
            ran_list = []
            for i in ("chest","belly","lleg","face","forehead", "ass", "pubic", "anus"):
                if not getattr(self,i):
                    ran_list.append(i)
            if not ran_list:
                return
            mark = renpy.random.choice(ran_list)
            self.add_writing(mark, what_pen)
            return
        
        def check_writing(self, what_pen="temp"):
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "ass", "pubic", "anus"):
                if isinstance(getattr(self, i), dict) and what_pen in getattr(self, i):
                    return True
            else:
                return False 
        
        def clean_writing(self, amount=1, tattoo=False): 
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "ass", "pubic", "anus"):
                if isinstance(getattr(self, i), dict):
                    if "tattoo" in getattr(self, i):
                        if tattoo:
                            setattr(self, i, 0)
                        else:
                            pass
                    elif "perm" in getattr(self, i):
                        getattr(self, i)["perm"] = getattr(self, i)["perm"] - amount
                        if getattr(self, i)["perm"] < 1:
                            setattr(self, i, 0)
                    else:
                        setattr(self, i, 0)
        
        def clean(self): 
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead", "ass", "pubic", "anus"):
                if isinstance(i, dict):
                    if "tattoo" in i:
                        return
                    elif "perm" in i:
                        i["perm"] -= 1
                        if i["perm"] < 1:
                            setattr(self, i, 0)
                    else:
                        setattr(self, i, 0)
                elif getattr(self, i) > 4:
                    setattr(self, i, 4)
        
        
        def all(self,amount):
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "ass", "pubic", "anus"):
                setattr(self, i, amount)
        
        def any(self):
            amount = 0
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead","special", "ass", "pubic", "anus"):
                if getattr(self, i):
                    amount += 1
            return amount
        
        def ass_counter_check(self,person):
            if self.ass:
                self.ass_counter += 1
                
                
                if not numgen(0,5) and not player.beingraped and not renpy.get_screen("blackout"):
                    renpy.say(person.name, "Keeping count of how many you get fucked by? Well here's another you dirty slut.")
                return
        
        def add_random(self, type="temp"):
            ran_list = []
            for i in ("larm","rarm","chest","belly","lleg","rleg","face","forehead", "ass", "pubic", "anus"):
                if not "tattoo" in getattr(self, i):
                    ran_list.append(i)
            if not ran_list:
                return
            mark = renpy.random.choice(ran_list)
            setattr(self,mark,1)
            return
        
        def perk_checker(self):
            for i in ["chest", "belly", "lleg","face","forehead", "ass", "pubic", "anus"]:
                if getattr(self, i) and not player.has_perk(globals()["perk_branded_" + i]):
                    player.add_perk(globals()["perk_branded_" + i])
                elif not getattr(self, i) and player.has_perk(globals()["perk_branded_" + i]):
                    player.remove_perk(globals()["perk_branded_" + i])
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
