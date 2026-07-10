init python:
    class QuestClass(object):
        def __init__(self):
            
            self.questname = "" 
            self.questdesc = "" 
            self.queststage = 0
            self.quest = None
            self.goals = []
            self.stages = []
            self.reward = 0 
            self.reward_counter = 0 
            
            self.name = "" 
            self.sname = "" 
            
            self.faction = False 
            
            self.isjob = False 
            self.starttime = () 
            self.workdays = () 
            self.timesworked = 0 
            self.workedtoday = 0 
            self.workcycle = 0 
            self.clothes = "daily" 
            
            self.active = 0 
            self.stage = 0
            self.day_started = 0 
            self.day_completed = 0
            
            self.conversation_topics = [] 
            self.list = [] 
            self.dict = {} 
            
            self.attract = 0 
            
            self.hvirgin = False
            self.ovirgin = False
            self.vvirgin = False
            self.avirgin = False
            
            self.virginbaby = False
            self.rapebaby = False
            self.soldbaby = False
            self.soldprice = 0
            self.soldrequest = 0 
            
            self.hsex = 0
            self.osex = 0
            self.vsex = 0
            self.asex = 0
            
            self.swallow = 0
            self.facial = 0
            self.buk = 0
            self.creamsafe = 0
            self.creamnormal = 0
            self.creamdanger = 0
            self.creamanal = 0
            
            self._last_cumin = 0 
            
            self.preg = 0 
            self.pregbabies = 0 
            self.sold = 0 
            self.soldpricetotal = 0
            self.rape = 0
            self.assault = 0 
            
            self.missionvar1 = 0 
            self.missionvar2 = 0
            self.missionvar3 = 0
            self.missionvar4 = 0
            self.missionvar5 = 0
            self.missionvar6 = 0
            self.missionvar7 = 0
            self.missionvar8 = 0
            self.missionvar9 = 0
            self.missionvar10 = 0
            self.missionvar11 = 0 
            self.missionvar12 = 0
            self.missionvar13 = 0
            self.missionvar14 = 0
            self.missionvar15 = 0
            self.missionvar16 = 0
            self.missionvar17 = 0
            self.missionvar18 = 0
            self.missionvar19 = 0
            
            
            
            
            
            self.hat_primary_colour = "red"
            self.hat_secondary_colour = "red"
            self.outfit_primary_colour = "red"
            self.outfit_secondary_colour = "red"
            self.coat_primary_colour = "red"
            self.coat_secondary_colour = "red"
            self.jacket_primary_colour = "red"
            self.jacket_secondary_colour = "red"
            self.top_primary_colour = "red"
            self.top_secondary_colour = "red"
            self.bottom_primary_colour = "red"
            self.bottom_secondary_colour = "red"
            self.bra_primary_colour = "white"
            self.bra_secondary_colour = "white"
            self.pants_primary_colour = "white"
            self.bsuit_secondary_colour = "white"
            self.bsuit_primary_colour = "white"
            self.pants_secondary_colour = "white"
            self.bsuit_primary_colour = "white"
            self.bsuit_secondary_colour = "white"
            self.socks_primary_colour = "white"
            self.socks_secondary_colour = "white"
            self.gloves_primary_colour = "white"
            self.gloves_secondary_colour = "white"
            
            self.set_trans()
            
            self._hat = 0
            self._jacket = 0
            self._coat = 0
            self._outfit = 0
            self._top = 0
            self._bottom = 0
            self._bra = 0
            self._pants = 0
            self._bsuit = 0
            self._socks = 0
            self._gloves = 0
            
            
            self.race = 0
            self.hair_colour = 0
            self.eye_colour = 0
            self.breasts = 2
        
        def quest_list_add(self):
            add_to_list(quest_list, self)
        @property
        def sex(self):
            return self.vsex + self.asex
        @property
        def naughty(self):
            if self.sex or self.hsex or self.osex:
                return True
            else:
                return False
        
        @property
        def last_cumin(self):
            return t.day - self._last_cumin
        @property
        def creamvag(self):
            return sum([self.creamsafe, self.creamnormal, self.creamdanger])
        
        @property
        def preg_current(self):
            if player.pregnant and player.preg_father_class == self and player.preg_knows:
                return True
            else:
                return False
        @property
        def preg_knows(self):
            if player.pregnant and player.preg_father_class == self and player.preg_knows:
                return True
            else:
                return False
        
        @property
        def hat(self):
            return self._hat
        @property
        def jacket(self):
            return self._jacket
        @property
        def coat(self):
            return self._coat
        @property
        def top(self):
            return self._top
        @property
        def bottom(self):
            return self._bottom
        @property
        def outfit(self):
            return self._outfit
        @property
        def bra(self):
            return self._bra
        @property
        def pants(self):
            return self._pants
        @property
        def bsuit(self):
            return self._bsuit
        @property
        def socks(self):
            return self._socks
        @property
        def gloves(self):
            return self._gloves
        
        
        
        
        
        
        @hat.setter
        def hat(self, hats):
            global tab_top
            self._hat = hats
            if "work" in tab_top:
                c.hat = hats
        @jacket.setter
        def jacket(self, jackets):
            global tab_top
            self._jacket = jackets
            if "work" in tab_top:
                c.jacket = jackets
        @jacket.setter
        def coat(self, coats):
            global tab_top
            self._coat = coats
            if "work" in tab_top:
                c.coat = coats
        @top.setter
        def top(self, tops):
            global tab_top
            self._top = tops
            if "work" in tab_top:
                c.top = tops
        @bottom.setter
        def bottom(self, bottoms):
            global tab_top
            self._bottom = bottoms
            if "work" in tab_top:
                c.bottom = bottoms
        @outfit.setter
        def outfit(self, outfits):
            global tab_top
            self._outfit = outfits
            if "work" in tab_top:
                c.outfit = outfits
        @bra.setter
        def bra(self, bras):
            global tab_top
            self._bra = bras
            if "work" in tab_top:
                c.bra = bras
        @pants.setter
        def pants(self, pantss):
            global tab_top
            self._pants = pantss
            if "work" in tab_top:
                c.pants = pantss
        @bsuit.setter
        def bsuit(self, bsuits):
            global tab_top
            self._bsuit = bsuits
            if "work" in tab_top:
                c.bsuit = bsuits
        @socks.setter
        def socks(self, sockss):
            global tab_top
            self._socks = sockss
            if "work" in tab_top:
                c.socks = sockss
        @gloves.setter
        def gloves(self, glovess):
            global tab_top
            self._gloves = glovess
            if "work" in tab_top:
                c.gloves = glovess
        
        def set_trans(self):
            for i in clothes_wardrobe_list:
                setattr(self, i + "_primary_trans", "trans_normal")
                setattr(self, i + "_secondary_trans", "trans_normal")
        
        def quest_name(self, qname, qdesc, faction=None):
            self.questname = qname
            self.questdesc = qdesc
            if faction:
                self.faction = faction
            quests.append(Quest(qname, qdesc, faction, self.goals, self.stages))
        
        def quest_stage(self, id='no name', description='no description'):
            self.goals.append(Goal(id, description))
            self.stages.append(Stage(id))
        
        def activate(self):
            self.active = 1
            self.day_started = t.day
        def complete(self):
            self.active = 2
            self.stage = 100
            self.stagedesc = "Mission Complete"
            self.day_completed = t.day
        
        def isactive(self):
            if self.active == 1:
                return True
            else:
                return False
        def iscomplete(self):
            if self.active == 2:
                return True
            else:
                return False
        def failed(self):
            self.active = 2
            self.stage = 100
            self.stagedesc = "Mission Failed"
        def player_name(self, first, last):
            self.name = first
            self.sname = last
        def quest_stagedesc(self, desc):
            self.stagedesc = desc
        
        def quest_job(self, reward, starttime, days=""):
            if days == "":
                days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
            self.isjob = True
            self.reward = reward
            self.starttime = starttime
            self.workdays = days
        def work(self):
            if self.workcycle:
                self.workcycle = 0
                self.set_workedtoday()
                self.add_timesworked()
        def set_workedtoday(self):
            self.workedtoday = t.day
        def add_timesworked(self):
            self.timesworked += 1
        def can_work(self):
            if t.hour in self.starttime and t.wkday in self.workdays:
                return True
            else:
                return False
        
        def pay(self):
            self.workedtoday = t.day
            self.timesworked += 1
            player.add_money(self.reward)
        def pay_allure(self):
            self.workedtoday = t.day
            self.timesworked += 1
            player.add_money_allure(self.reward)
        
        
        
        
        
        
        def mission_cosmetic(self, race, hair, eye):
            self.race = race
            self.hair_colour = hair
            self.eye_colour = eye
        
        def set_mission_cosmetic(self):
            player.race = self.race
            player.hair_colour = self.hair_colour
            player.eye_colour = self.eye_colour
        
        
        
        
        def work_dress_set(self):
            
            for i in clothes_wardrobe_list:
                setattr(self, i, getattr(c, i))
                setattr(self, i + "_primary_colour", getattr(c, i + "_primary_colour"))
                setattr(self, i + "_secondary_colour", getattr(c, i + "_secondary_colour"))
        
        def work_dress(self, slow=False):
            global tab_top
            
            if not "work" in tab_top:
                self.clothes = tab_top
            
            for i in clothes_wardrobe_list:
                setattr(work, i + "_primary_colour", getattr(self, i + "_primary_colour"))
                setattr(work, i + "_secondary_colour", getattr(self, i + "_secondary_colour"))
                if getattr(self, i) and wardrobe.qty(globals()["item_" + i + "_" + str(getattr(self, i))]):
                    setattr(work, i, getattr(self, "_" + i))
                else:
                    setattr(work, i, 0)
            
            tab_top = "work"
            if slow:
                pc_dress_slow()
            else:
                pc_dress()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def pub_waitress_clothes(self):
            self.outfit_primary_colour = "crimson"
            self.outfit_secondary_colour = "white"
            self.pants_primary_colour = "crimson"
            self.pants_secondary_colour = "white"
            self.socks_primary_colour = "crimson"
            self.socks_secondary_colour = "white"
            
            self.hat = 0
            self.jacket = 0
            self.outfit = 9
            self.top = 0
            self.bottom = 0
            self.bra = 0
            self.pants = 3
            self.socks = 5
            self.gloves = 0
        
        def haven_clothes(self):
            self.top_primary_colour = "grey"
            self.top_secondary_colour = "black"
            self.bottom_primary_colour = "black"
            self.bottom_secondary_colour = "grey"
            self.pants_primary_colour = "black"
            self.pants_secondary_colour = "black"
            self.socks_primary_colour = "black"
            self.socks_secondary_colour = "grey"
            self.gloves_primary_colour = "black"
            self.gloves_secondary_colour = "white"
            
            for i in clothes_wardrobe_list:
                setattr(self, i + "_primary_trans", getattr(self, i + "_primary_trans"))
                setattr(self, i + "_secondary_trans", getattr(self, i + "_secondary_trans"))
            
            self.hat = 0
            self.jacket = 0
            self.outfit = 0
            self.top = 11
            self.bottom = 10
            self.bra = 0
            self.pants = 3
            self.socks = 5
            self.gloves = 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
