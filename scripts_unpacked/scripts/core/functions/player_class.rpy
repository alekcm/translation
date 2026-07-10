init python:

    class PlayerStats(object):
        def __init__(self):
            
            
            
            
            self.race = 1
            self.skin_colour = "6_0_base"
            
            self.hair_colour = 2
            self._hair_length = 40
            self._hair_fringe = 2
            self.hair_fringe_default = 2
            self.hair_style = "loose"
            self.hair_style_default = "loose" 
            
            self._phair = 10
            self.breasts = 2
            
            self.eye_liner = 1
            self.nip_size = 1
            self.nip_colour = 1
            
            self.eye_colour = 1
            
            self.body_conf = 0 
            
            self.eyeshad_colour = 0
            self.blush_colour = 0
            self.makeup = False
            
            self.drool = 0
            self.cry = 0
            self.tear = 0
            self.puke = 0
            self.rainbow = 0
            
            self.brow = 1
            self.mouth = 1
            self.eye = 1
            
            self.male_origin = False
            
            self._prop = ""
            
            
            self._left_hand = ""
            self._right_hand = ""
            
            
            self.cash = 0
            
            
            
            
            
            
            
            
            self._desire = 0.0
            self._tired = 80.0
            self._mood = 80.0
            self.mood_queue = []
            self._confidence = 0.0
            self._fitness = 0.0
            self._int = 0.0
            
            
            self._allure = 0
            self.hunger = 100
            self.hygiene = 100
            
            self._drunk = 0
            self._high = 0
            
            self.drunkaddict = False
            self.drunkaddictamount = 0 
            
            self.highaddict = False
            self.highaddictamount = 0
            
            self.smokeaddict = False
            self.smokeaddictamount = 0
            
            
            
            
            self._pregnancy = 1 
            self.pregnant = 0 
            self.days_pregnant = 0 
            self.pregpills = False 
            
            
            self.pregbabies = 0 
            
            self.preg_desire = 0 
            self.preg_want = False 
            self.preg_notwant = False 
            self.preg_amount = 0 
            
            self.tanline_top = 0
            self.tanline_bottom = 0
            self.suntan = 0
            
            
            
            self.hvirgin = True 
            self.ovirgin = True
            self.vvirgin = True
            self.avirgin = True
            self.virgin_pregcheck = True 
            self.want_sexlocation = 0 
            self.have_sexlocation = 0 
            self.want_pullout = True
            self.have_pullout = True
            
            self.firstvsex = "I have never had sex so must be a virgin."
            self.firstasex = ""
            self.person = "" 
            
            self.father = "" 
            self.preg_father_class = nosex 
            self.preg_father_colour = False
            self.preg_quest_class = nosex 
            
            self.selling = False 
            self.beingraped = False
            self.having_sex = False
            self.virginbaby = False
            self.rapebaby = False  
            self.soldbaby = False
            self._soldprice = 0
            self.soldrequest = "" 
            self.sex_holes = [] 
            self.sex_man_amount = 0 
            
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
            
            self.sold = 0 
            self.soldpricetotal = 0
            self.rape = 0
            self.assault = 0 
            self._last_cumin = 0
            
            self.force_uncover = False 
            self.force_cover = False 
            self.force_cover_breasts = False
            self.force_cover_vag = False
            
            
            
            
            self.sexday = 0 
            
            self.cycle_conditions = {
            "length_mens" : 5,
            "length_foll" : 9,
            "length_ovulate" : 5,
            "length_lut" : 10,
            "length_no_cycle" : 3,

            "count_stage" : -1, 
            "count_cycle" : 14,

            "stage" : "no_cycle",

            "chance_mens" : 99,
            "chance_foll" : 20,
            "chance_ovulate" : 5,
            "chance_lut" : 35,
            "chance_no_cycle" : 35, 

            "chance_base" : 1
            }
            
            self.cum_locations = { 
            "cum_hand" : 0,
            "cum_mouth" : 0,
            "cum_face" : 0,
            "cum_chest" : 0,
            "cum_belly" : 0,
            "cum_vagout" : 0,
            "cum_vagin" : 0,
            "cum_assout" : 0,
            "cum_assin" : 0,
            }
            
            self.cum_mouth = 0
            self.cum_face = 0
            self.cum_chest = 0
            self.cum_belly = 0
            self.cum_vagout = 0
            self.cum_vagin = 0
            self.cum_assout = 0
            self.cum_assin = 0
            
            
            self.perk_list = []
            self.origin_perk = None
            
            self.reset_sex_status() 
            
            self.dict = {} 
            self.list = []
        
        @property
        def phair(self):
            if self._phair <= 0:
                
                return 0
            elif self._phair > 10:
                return 10
            else:
                return self._phair
        
        def phair_grow(self):
            self._phair += 1
        def phair_fullgrow(self):
            self._phair = 10
        def phair_wax(self):
            self._phair = -10
        def phair_shave(self):
            self._phair = -2
        
        @property
        def hair_neck(self):
            if self._hair_length >= 30:
                return 4
            elif self._hair_length >= 20:
                return 3
            elif self._hair_length >= 10:
                return 2
            else:
                return 1
        def hair_grow(self):
            if numgen(0,10):
                self._hair_length += 1
        
        def hair_daily_grow(self):
            self.hair_grow()
            self.phair_grow()
        
        @property
        def soldprice(self):
            if isinstance(self._soldprice, int):
                return self._soldprice
            elif isinstance(self._soldprice, Inventory):
                return str(self._soldprice.value()) + " of goods"
        
        @soldprice.setter
        def soldprice(self, amount):
            self._soldprice = amount
        
        @property
        def pregnancy(self): 
            if cheat_fetish_preg_fantasy and self.pregnant:
                return 3
            
            preg = 0
            
            if self.days_pregnant >= (global_pregnancy_length * 0.8):
                preg = 3
            elif self.days_pregnant >= (global_pregnancy_length * 0.5):
                preg = 2
            elif self.days_pregnant >= (global_pregnancy_length * 0.3):
                preg = 1
            
            else: 
                if self.has_perk(perk_slim): 
                    preg = 0
                elif self._fitness < 20: 
                    preg = 1
                else:
                    preg = 0
            
            if cheat_fetish_cumflation: 
                cumflate = (self.cum_locations["cum_vagin"] + self.cum_locations["cum_assin"] + self.cum_locations["cum_mouth"]) / 8
                preg = preg + cumflate
                if preg > 3:
                    preg = 3
            
            return preg
        
        
        
        
        @pregnancy.setter
        def pregnancy(self, amount):
            
            
            
            self._pregnancy = amount
        
        
        @property
        def isfat(self):
            if self.pregnancy == 1 and self.days_pregnant < (global_pregnancy_length * 0.3):
                return True
            return False 
        
        @property
        def prop(self):
            return self._prop
        
        @prop.setter
        def prop(self, what):
            self._prop = what
            refresh_avatar()
        
        @property
        def left_hand(self):
            if self._left_hand == "flyer":
                return "flyer"
            elif self._left_hand == "hat":
                return "hat"
            elif self._left_hand == "beer" or self.has_perk([perk_drinking_beer_1, perk_drinking_beer_2]):
                return "beer"
            elif self._left_hand == "beer_bottle" or self.has_perk([perk_drinking_beerbottle_1, perk_drinking_beerbottle_2]):
                return "beer_bottle"
            elif self._left_hand == "wine_bottle" or self.has_perk([perk_drinking_wine_1, perk_drinking_wine_2, perk_drinking_wine_3, perk_drinking_wine_4]):
                return "wine_bottle"
            elif self._left_hand == "brew" or self.has_perk([perk_drinking_brew_1, perk_drinking_brew_2]):
                return "brew"
            elif self.cover_breasts:
                return "cover_breast"
            else:
                return ""
        
        @left_hand.setter
        def left_hand(self, what):
            self._left_hand = what 
            refresh_avatar()
        
        def left_hand_reset(self):
            self.left_hand = ""
        
        def busk(self):
            self.face_happy()
            self.left_hand = "hat"
        def busk_end(self):
            self.face_normal()
            self.left_hand = ""
        def flyer(self):
            self.face_happy()
            self.left_hand = "flyer"
            refresh_avatar()
        @property
        def right_hand(self):
            global weather_var
            if loc_cur.outside and not loc(loc_beach_water) and weather_var >= 3:
                return "umb"
            elif self._right_hand == "beer":
                return "beer"
            elif self._right_hand == "coffee":
                return "coffee"
            elif self.cover_vagina:
                return "cover_vag"
            elif self.cover_breasts:
                return "cover_breast"
            else:
                return ""
        
        @right_hand.setter
        def right_hand(self, what):
            self._right_hand = what
            refresh_avatar()
        
        def right_hand_reset(self):
            self.right_hand = ""
        
        def hands_reset(self):
            self.left_hand_reset()
            self.right_hand_reset()
            refresh_avatar()
        
        
        
        @property
        def lactating(self):
            if self.has_perk(perk_lactating):
                return True
            else:
                return False
        
        @property
        def milky(self): 
            if self.has_perk(perk_milky) and not any([c.bra == 13]):
                return True
            else:
                return False
        
        @property
        def breasts_lifted(self):
            if not (c.cansee_breasts and not ((c.bra and not c.bra_nolift) or (c.bsuit))) or grope_breasts1 or grope_breasts2:
                return True
            else:
                return False
        @property
        def breasts_free(self):
            return not self.breasts_lifted
        
        @property
        def desire(self):
            return self.stat_calulate("desire")
        @property
        def tired(self):
            return self.stat_calulate("tired")
        @property
        def mood(self):
            if self.stat_calulate("mood") < 0:
                self.add_perk(perk_despondent)
            else:
                self.remove_perk(perk_despondent)
            return self.stat_calulate("mood")
        @property
        def confidence(self):
            return self.stat_calulate("confidence")
        @property
        def fitness(self):
            return self.stat_calulate("fitness")
        @property
        def int(self):
            return self.stat_calulate("int")
        @property
        def allure(self):
            return self.stat_calulate("allure")
        
        @property
        def drunk(self):
            return int(self._drunk)
        @property
        def high(self):
            return int(self._high)
        
        @property
        def sex(self):
            return sum([self.vsex, self.asex])
        
        @property
        def creamvag(self):
            return sum([self.creamsafe, self.creamnormal, self.creamdanger])
        
        @property
        def last_cumin(self):
            if self._last_cumin:
                return t.day - self._last_cumin
            else:
                return 0
        
        @property
        def showing(self):
            if self.pregnancy >= 2:
                return True
            else:
                return False
        
        @property
        def cum_visible(self):
            if self.cum_visible_check():
                self.add_perk(perk_cumstain)
            else:
                self.remove_perk(perk_cumstain)
            return self.cum_visible_check()
        
        @property
        def iswhore(self):
            if self.has_perk([perk_whore, perk_branded_forehead, perk_freeuse]) or (dis(dis_truckstop) and quest_whore.sold and ("party" in tab_top or self.has_perk([perk_slutty, perk_pervert]))):
                return True
            else:
                return False
        @property
        def isslut(self):
            if self.has_perk([perk_slut, perk_branded_face, perk_freeuse]):
                return True
            else:
                return False
        @property
        def isbroken(self):
            if self.has_perk([perk_broken]):
                return True
            else:
                return False
        
        @property
        def slutty(self):
            if self.has_perk([perk_slutty, perk_pervert]) or (c.exposed and not dis(dis_beach)):
                return True
            else:
                return False
        
        @property
        def perverted(self):
            if self.has_perk([perk_pervert]) or (c.exposed and not dis(dis_beach)):
                return True
            else:
                return False
        
        @property
        def preg_knows(self):
            if self.has_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_2, perk_pregnant_3]):
                return True
            else:
                return False
        
        @property
        def recovering(self):
            if self.has_perk(perk_recovering):
                return True
            else:
                return False
        
        @property
        def effect_drunk(self):
            return False
            if self.has_perk(perk_recovering):
                return True
            else:
                return False
        @property
        def effect_high(self):
            return False
            if self.has_perk(perk_recovering):
                return True
            else:
                return False
        @property
        def effect_angry(self):
            return False
            if self.has_perk(perk_recovering):
                return True
            else:
                return False
        @property
        def effect_tired(self):
            if self._tired <= 20:
                return True
            else:
                return False
        @property
        def effect_heart(self):
            if self.check_horny(extreme=True):
                return True
            else:
                return False
        
        @property
        def sweat(self):
            if self.hygiene <= 25:
                return 1
            else:
                return 0
        
        
        @property
        def shy(self):
            if self.has_perk([perk_drunk, perk_wasted, perk_blackout]) or self.check_horny(extreme=True):
                return 2
            elif self.has_perk(perk_tipsy) or self.check_horny():
                return 1
            else:
                return 0
        
        @property
        def hair_fringe(self):
            return self._hair_fringe
        @hair_fringe.setter
        def hair_fringe(self, number):
            self._hair_fringe = number
            if number:
                self.hair_fringe_default = number
        
        
        
        
        
        @property
        def dont_cover_self(self):
            
            
            
            
            
            
            
            if self.force_uncover:
                return True
            if self.having_sex and not self.beingraped:
                
                return True
            if self.has_perk([perk_exhibitionist, perk_broken]): 
                
                return True
            if tab_top == "work": 
                return True
            
            
            location = loc_cur
            
            if location.population == 0 and not location.outside:
                
                return True
            if any(name in location.name for name in ["locker", "toilet", "shower", "bath"]) and not location.mens_room:
                
                return True
            
            district = location.get_district()
            
            if district is dis_beach or (tab_top in "swim" and district is dis_lake and not c.exposed):
                
                return True
            
            if self.has_perk(perk_whore) and (district is dis_truckstop or location is loc_motel): 
                
                return True
            
            if wolfgang_can_play():
                return True
            
            get_screen = renpy.get_screen 
            
            if get_screen("wardrobe_screen") or get_screen("acc_screen") or get_screen("surgery_screen"):
                
                return True
            
            return False
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        @property
        def cover_breasts(self):
            if self.force_cover or self.force_cover_breasts:
                return True
            elif c.cansee_breasts_clothes_check() == 5 or self.dont_cover_self: 
                return False
            elif self.confidence < ((If(loc_cur.population >= 2, 6, 4) - c.cansee_breasts_clothes_check()) * 10):
                return True
            else:
                return False
        
        
        @property
        def cover_vagina(self):
            if self.force_cover or self.force_cover_vag:
                return True
            elif c.cansee_vag_clothes_check() == 5 or self.dont_cover_self:
                return False   
            elif self.confidence < ((If(loc_cur.population >= 2, 7, 5) - c.cansee_vag_clothes_check()) * 10):  
                return True    
            else:
                return False
        
        
        @property
        def cover_ass(self):
            
            if self.force_cover:
                return True
            elif c.cansee_ass_clothes_check() == 5 or self.dont_cover_self:
                return False   
            elif self.confidence < ((If(loc_cur.population >= 2, 6, 4) - c.cansee_ass_clothes_check()) * 10):  
                return True    
            else:
                return False
            refresh_avatar()
        
        @property
        def covering(self):
            if self.cover_vagina or self.cover_breasts or self.cover_ass:
                return True
            else:
                return False
        
        def uncover(self):
            self.force_cover = False 
            self.force_cover_breasts = False
            self.force_cover_vag = False
            self.force_uncover = True
            refresh_avatar()
        def cover(self):
            self.force_uncover = False
            self.force_cover = True
            refresh_avatar()
        def cover_breasts_force(self):
            self.force_uncover = False
            self.force_cover_breasts = True
            refresh_avatar()
        def cover_vag_force(self):
            self.force_uncover = False
            self.force_cover_vag = True
            refresh_avatar()
        def cover_reset(self):
            self.force_uncover = False
            self.force_cover = False
            self.force_cover_breasts = False
            self.force_cover_vag = False
            refresh_avatar()
        
        
        
        
        
        @property
        def gagged(self):
            return self.has_perk([perk_gagged, perk_gagged_locked])
        
        @property
        def blind(self):
            return self.has_perk([perk_blind])
        
        @property
        def plugged(self):
            return self.has_perk([perk_buttplug])
        
        
        
        
        
        def add_perk(self, perk, check=True, days=None, hours=None, mins=None, notif=False, origin=False):
            add_to_list(self.perk_list, perk)
            if check:
                self.check_perk_combo()
            if days:
                if not perk.days or perk.days < days:
                    perk.days = days
            if hours:
                if not perk.hours or perk.hours < hours:
                    perk.hours = hours
            if mins:
                if not perk.mins or perk.mins < mins:
                    perk.mins = mins
            if notif:
                show_notif_popup("Gained the " + str(perk.name) + " perk")
            if origin:
                self.origin_perk = perk
        
        def remove_perk(self, perk, check=True, notif=False):
            if perk == self.origin_perk:
                return
            if check:
                self.check_perk_combo()
            if isinstance(perk, list):
                for i in perk:
                    remove_from_list(self.perk_list, i)
            else:
                remove_from_list(self.perk_list, perk)
            if notif:
                show_notif_popup("Lost the " + str(perk.name) + " perk")
        
        def remove_perk_pregnancy(self):
            self.remove_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_2, perk_pregnant_3])
            self.remove_perk([perk_unwanted_preg, perk_wanted_preg])
        
        def has_perk(self, perk, wildcard=True, notif=False):
            
            if not isinstance(perk, list):
                perk = [perk]
            for i in perk:
                if i in self.perk_list:
                    if notif:
                        self.stat_popup_screen(i.name)
                    
                    return True
                elif wildcard and notif and self.wildcard_perk_check(i):
                    show_notif_popup("Wildcard " + str(i.name))
                    return True
            else:
                return False
        
        def deg_perk(self, days=False, mins=False):
            if days:
                for i in self.perk_list:
                    if i.days:
                        i.days = i.days - 1
                        if i.days < 1:
                            i.days = None
                            self.remove_perk(i)
            elif mins:
                for i in self.perk_list:
                    if i.mins:
                        i.mins = i.mins - mins
                        if i.mins < 1:
                            i.mins = None
                            if "perk_drinking" in i.image:
                                self.deg_perk_alcohol()
                            self.remove_perk(i)
            else:
                for i in self.perk_list:
                    if i.hours:
                        i.hours = i.hours - 1
                        if i.hours < 1:
                            i.hours = None
                            if i == perk_wakeup:
                                self.add_tired(-70)
                                self.add_mood(-40)
                                self.add_perk(perk_wakeup_comedown, hours=3)
                            self.remove_perk(i)
        
        def drink_current(self):
            
            self.deg_perk_alcohol()
        def deg_perk_alcohol(self):
            
            if self.has_perk(perk_drinking_wine_4):
                self.drink()
                self.remove_perk(perk_drinking_wine_4)
                self.add_perk(perk_drinking_wine_3, mins=10)
            elif self.has_perk(perk_drinking_wine_3):
                self.drink()
                self.remove_perk(perk_drinking_wine_3)
                self.add_perk(perk_drinking_wine_2, mins=10)
            elif self.has_perk(perk_drinking_wine_2):
                self.drink()
                self.remove_perk(perk_drinking_wine_2)
                self.add_perk(perk_drinking_wine_1, mins=10)
            elif self.has_perk(perk_drinking_wine_1):
                self.drink()
                self.remove_perk(perk_drinking_wine_1)
                inv.take(item_scrap_junk)
            
            elif self.has_perk(perk_drinking_beer_2):
                self.drink(spiked=True)
                self.remove_perk(perk_drinking_beer_2)
                self.add_perk(perk_drinking_beer_1, mins=10)
            elif self.has_perk(perk_drinking_beer_1):
                self.drink(spiked=True)
                self.remove_perk(perk_drinking_beer_1)
            
            
            elif self.has_perk(perk_drinking_beerbottle_2):
                self.drink()
                self.remove_perk(perk_drinking_beerbottle_2)
                self.add_perk(perk_drinking_beerbottle_1, mins=10)
            elif self.has_perk(perk_drinking_beerbottle_1):
                self.drink()
                self.remove_perk(perk_drinking_beerbottle_1)
                inv.take(item_scrap_junk)
            
            elif self.has_perk(perk_drinking_brew_2):
                self.drink(amount=40, spiked=True)
                self.remove_perk(perk_drinking_brew_2)
                self.add_perk(perk_drinking_brew_1, mins=10)
            elif self.has_perk(perk_drinking_brew_1):
                self.drink(amount=40, spiked=True)
                self.remove_perk(perk_drinking_brew_1)
                inv.take(item_milkbottle_empty)
        
        def has_perk_drinking(self):
            if self.has_perk([
            perk_drinking_wine_4, 
            perk_drinking_wine_3, 
            perk_drinking_wine_2, 
            perk_drinking_wine_1,
            perk_drinking_beer_2,
            perk_drinking_beer_1,
            perk_drinking_beerbottle_2,
            perk_drinking_beerbottle_1,
            perk_drinking_brew_2,
            perk_drinking_brew_1,
            ]):
                return True
            else:
                return False
        
        @property
        def smoking(self):
            return self.has_perk(perk_smoking)
        
        @property
        def drinking(self):
            return self.has_perk_drinking()
        
        def drink_finish(self):
            while self.has_perk_drinking():
                self.deg_perk_alcohol()
            else:
                return
        
        def wildcard_perk_check(self, perk):
            if perk_wildcard in self.perk_list and not numgen(0,4) and perk.wildcard:
                return True
            else:
                return False
        
        def check_perk_combo(self):
            
            
            
            if self.has_perk(perk_gamine, wildcard=False) and not self.has_perk([perk_whore, perk_smoker, perk_numb], wildcard=False):
                self.add_perk(perk_whore, check=False)
                self.add_perk(perk_smoker, check=False) 
                self.add_perk(perk_numb, check=False)
            
            if self.has_perk(perk_bimbo, wildcard=False) and not self.has_perk(perk_slim, wildcard=False):
                self.add_perk(perk_slim, check=False)
            
            if self.has_perk(perk_gym_bunny, wildcard=False) and not self.has_perk(perk_slim, wildcard=False):
                self.add_perk(perk_slim, check=False)
            
            if self.has_perk(perk_exhibitionist, wildcard=False) and not self.has_perk(perk_commando, wildcard=False):
                self.add_perk(perk_commando, check=False)
            
            if self.has_perk([perk_bambi, perk_nerd], wildcard=False) and not self.has_perk(perk_lightweight, wildcard=False):
                self.add_perk(perk_lightweight, check=False)
            
            if self.has_perk(perk_broodmother, wildcard=False) and (not self.has_perk([perk_creampie_lover, perk_preg_want], wildcard=False) or self.has_perk(perk_preg_notwant, wildcard=False)):
                self.add_perk([perk_creampie_lover, perk_preg_want], check=False)
                self.remove_perk(perk_preg_notwant, check=False)
            
            if self.has_perk(perk_party_girl, wildcard=False) and not self.has_perk([perk_alcoholic, perk_smoker, perk_slut], wildcard=False):
                self.add_perk([perk_alcoholic, perk_smoker, perk_slut], check=False)
            
            if self.has_perk(perk_meek, wildcard=False) and not self.has_perk([perk_broken, perk_numb, perk_lightweight], wildcard=False):
                self.add_perk([perk_broken, perk_numb, perk_lightweight], check=False) 
            
            if self.has_perk(perk_addict, wildcard=False) and not self.has_perk([perk_whore, perk_broken, perk_smoker, perk_alcoholic, perk_joy_addict, perk_numb], wildcard=False):
                self.add_perk([perk_whore, perk_broken, perk_smoker, perk_alcoholic, perk_joy_addict, perk_numb], check=False) 
            
            if self.has_perk(perk_princess, wildcard=False) and not self.has_perk([perk_lightweight, perk_slim], wildcard=False):
                self.add_perk([perk_lightweight, perk_slim], check=False) 
            
            if self.has_perk(perk_deadinside, wildcard=False) and not self.has_perk([perk_numb, perk_preg_notwant], wildcard=False):
                self.add_perk([perk_numb, perk_preg_notwant], check=False)
            
            
            
            if self.pregnant and self.preg_knows:
                self.remove_perk([perk_period, perk_period_late, perk_ovulating, perk_inseminated], check=False)
            if acc.choker == 6 and not self.has_perk(perk_bitch):
                self.add_perk(perk_bitch, check=False)
            elif not acc.choker == 6 and self.has_perk(perk_bitch, wildcard=False):
                self.remove_perk(perk_bitch, check=False)
        
        
        
        
        def check_effect_perks(self):
            self.add_perk(perk_dirty) if self.hygiene < 20 else self.remove_perk(perk_dirty)
            self.add_perk(perk_spanked_ass) if bruise.ass > 0.6 else self.remove_perk(perk_spanked_ass)
            self.add_perk(perk_buttplug) if acc.anus else self.remove_perk(perk_buttplug)
            self.add_perk(perk_bruised) if sum([bruise.face, bruise.chest, bruise.belly]) > 3 else self.remove_perk(perk_bruised)
            [self.add_perk(perk_beaten), self.remove_perk(perk_bruised)] if sum([bruise.face, bruise.chest, bruise.belly]) > 6 else self.remove_perk(perk_beaten)
            self.add_perk(perk_makeup) if (sum([acc.eyeshadow, acc.blush, acc.lipstick]) and acc.makeup_on) else self.remove_perk(perk_makeup)
            
            self.add_perk(perk_slutty) if c.slutty or acc.sexual else self.remove_perk(perk_slutty)
            self.add_perk(perk_pervert) if acc.perverted or self.cum_visible or (c.exposed and not (any([dis(dis_home), dis(dis_lake)]) or not loc_cur.population)) else self.remove_perk(perk_pervert)
            self.add_perk(perk_bitch) if acc.choker == 6 else self.remove_perk(perk_bitch)
        
        def check_preg_perks(self):
            self.add_perk(perk_pregnant_0)
            if self.has_perk(perk_preg_notwant) or (self.rapebaby and not self.has_perk(perk_preg_want)):
                self.add_perk(perk_unwanted_preg)
            elif self.has_perk(perk_preg_want):
                self.add_perk(perk_wanted_preg)
            self.remove_perk([perk_preg_notwant, perk_preg_want, perk_ovulating, perk_period, perk_period_late, perk_inseminated])
        
        def sex_virgin_perk_check(self):
            if not self.vvirgin and self.has_perk([perk_virgin, perk_tech_virgin], wildcard=False):
                self.remove_perk(perk_virgin)
                self.remove_perk(perk_tech_virgin)
            if not self.vvirgin and self.has_perk(perk_pure_virgin, wildcard=False):
                self.remove_perk(perk_pure_virgin)
                self.add_perk(perk_broken_virgin, days=14)
                self.add_perk(perk_numb)
                self.remove_perk(perk_recovering)
            if not self.avirgin and self.has_perk(perk_virgin, wildcard=False):
                self.remove_perk(perk_virgin)
                self.add_perk(perk_tech_virgin)
        
        def pick_random_origin_perk(self):
            global perk_origin_list
            perk = renpy.random.choice(perk_origin_list)
            self.origin_perk = perk
            self.add_perk(perk)
        
        
        
        
        def stat_calulate(self, what):
            bonus = 0
            
            for i in self.perk_list:
                if getattr(i, what + "_add"):
                    bonus += getattr(i, what + "_add")
            total = int(getattr(self, "_" + what) + bonus)
            if not what in ["mood"] and total < 0:
                total = 0
            return total
        
        def allure_function(self):
            self.sex_isslut_calculate()
            self.sex_iswhore_calculate()
            
            allure = 0
            
            allure += (
                self._desire / 8 +
                self._confidence / 4 +
                self._fitness / 2 +
                self._mood / 6
            )
            
            
            
            allure -= (100 - self.hygiene)
            
            clothing = c
            outfit = tab_top
            
            is_swim = "swim" in outfit
            is_school = "school" in outfit
            is_party = "party" in outfit
            is_home = "home" in outfit
            is_sport = "sport" in outfit
            
            if is_swim: 
                allure += 30 
                if clothing.thong:
                    allure += 15
                if clothing.clevage:
                    allure += 10
                if clothing.belly:
                    allure += 5
                if clothing.outfit == 0: 
                    if clothing.braless:
                        allure += 50
                    if clothing.pantsless:
                        allure += 80
            
            else:
                if is_school: 
                    allure += 10
                elif is_party or is_home: 
                    allure += 20
                elif is_sport: 
                    allure += 30
                
                
                if not (clothing.outfit or clothing.top):
                    if not clothing.bra: 
                        allure += 100
                    else:
                        if is_sport: 
                            allure += 30
                        else:
                            allure += 60
                if not (clothing.outfit or clothing.bottom):
                    if clothing.pantsless: 
                        allure += 150
                    elif clothing.thong: 
                        allure += 80
                    else:
                        allure += 60
                if clothing.thong:
                    if clothing.ass: 
                        allure += 15
                    if clothing.skirt: 
                        allure += 8 
                
                if clothing.skirt:
                    if clothing.pantsless: 
                        allure += 30
                    elif clothing.thong:
                        allure += 15
                    else:
                        allure += 5 
                
                if clothing.clevage:
                    if clothing.braless:
                        if self.breasts == 1:
                            allure += 20
                        elif self.breasts == 2:
                            allure += 35
                        else:
                            allure += 60
                    else:
                        if self.breasts == 1:
                            allure += 5
                        elif self.breasts == 2:
                            allure += 20
                        else:
                            allure += 35
                if clothing.pokenips: 
                    if outside:
                        allure += 20
                    else:
                        allure += 10
                if clothing.belly:
                    if self.isfat:
                        allure -= 20
                    elif self.pregnancy > 0: 
                        allure += 10
                    else:
                        allure += 5
                if clothing.slutty:
                    allure += 50
            
            
            
            self.cum_visible_check()
            if allure < 0 or self.cum_visible: 
                self._allure = 0
            
            self._allure = allure
        def add_desire(self, amount):
            max_desire = 100
            
            total_amount = amount
            if amount > 0:
                for i in self.perk_list:
                    if i.desire_multi:
                        total_amount = total_amount * i.desire_multi
            
            else:
                for i in self.perk_list:
                    if i.desire_multineg:
                        total_amount = total_amount * i.desire_multineg
            
            for i in self.perk_list:
                if i.desire_max:
                    max_desire += i.desire_max
            
            min_desire = 0
            for i in self.perk_list:
                if i.desire_min:
                    min_desire += i.desire_min
            if min_desire < 0:
                min_desire = 0
            
            self._desire += total_amount
            
            if self._desire > max_desire:
                self._desire = max_desire
            if self._desire < min_desire:
                self._desire = min_desire
            self.face_normal()
        
        def add_desire_random(self, amount=10):
            get_amount = numgen(int(amount * 0.5), int(amount * 1.5))
            self.add_desire(get_amount)
        
        def add_mood(self, amount):
            self.add_comfort_chance()
            max_mood = 100
            
            total_amount = amount
            if amount > 0:
                for i in self.perk_list:
                    if i.mood_multi:
                        total_amount = total_amount * i.mood_multi
            else:
                for i in self.perk_list:
                    if i.mood_multineg:
                        total_amount = total_amount * i.mood_multineg
            for i in self.perk_list:
                if i.mood_max:
                    max_mood += i.mood_max
            
            min_mood = 0
            for i in self.perk_list:
                if i.mood_min:
                    min_mood += i.mood_min
            if min_mood < -50:
                min_mood = -50
            
            self._mood += total_amount
            
            if self._mood > max_mood:
                self._mood = max_mood
            if self._mood < min_mood:
                self._mood = min_mood
            self.face_normal()
        
        def add_mood_queue(self):
            while len(self.mood_queue) >= 10:
                self.mood_queue.pop()
            self.mood_queue.insert(0,self.mood)
            if (t.hour % 2) == 0:
                if renpy.random.randint(0, 2000) < sum(self.mood_queue):
                    self.add_conf_chance()
                if renpy.random.randint(0, 2000) > sum(self.mood_queue):
                    self.remove_conf_chance()
        
        def set_mood(self, amount):
            self.add_mood(-100)
            self.add_mood(amount)
        
        def mood_hit(self,num_min=3, num_max=10):
            moodamount = renpy.random.randint(num_min, num_max)
            self.add_mood(-moodamount)
        
        def add_tired(self, amount, sucu=False):
            max_tired = 100
            
            total_amount = amount
            if amount > 0: 
                if self.has_perk(perk_sucu) and sucu:
                    
                    total_amount = total_amount
                else:
                    for i in self.perk_list:
                        if i.tired_multi:
                            total_amount = total_amount * i.tired_multi
            else:
                for i in self.perk_list:
                    if i.tired_multineg:
                        total_amount = total_amount * i.tired_multineg
            
            for i in self.perk_list:
                if i.tired_max:
                    max_tired += i.tired_max
            
            min_tired = 0
            for i in self.perk_list:
                if i.tired_min:
                    min_tired += i.tired_min
            if min_tired < 0:
                min_tired = 0
            
            self._tired += total_amount
            
            if self._tired > max_tired:
                self._tired = max_tired
            if self._tired < min_tired:
                self._tired = min_tired
            self.face_normal()
        
        def set_tired(self, amount):
            self.add_tired(-100)
            self.add_tired(amount)
        
        def add_conf(self, amount):
            self.add_comfort_chance()
            max_confidence = 100
            total_amount = amount
            if amount > 0:
                for i in self.perk_list:
                    if i.confidence_multi:
                        total_amount = total_amount * i.confidence_multi
            
            for i in self.perk_list:
                if i.confidence_max:
                    max_confidence += i.confidence_max
            
            min_confidence = 0
            for i in self.perk_list:
                if i.confidence_min:
                    min_confidence += i.confidence_min
            if min_confidence < 0:
                min_confidence = 0
            
            self._confidence += total_amount
            
            if self._confidence > max_confidence:
                self._confidence = max_confidence
            if self._confidence < min_confidence:
                self._confidence = min_confidence
            self.face_normal()
        
        def add_conf_chance(self):
            if renpy.random.randint(1, 100) > self._confidence:
                self.add_conf(1)
        
        def remove_conf_chance(self):
            if renpy.random.randint(1, 100) < self._confidence:
                self.add_conf(-1)
        
        def add_int(self, amount=1):
            self.add_comfort_chance()
            max_int = 100
            
            total_amount = amount
            if amount > 0:
                for i in self.perk_list:
                    if i.int_multi:
                        total_amount = total_amount * i.int_multi
            
            for i in self.perk_list:
                if i.int_max:
                    max_int += i.int_max
            
            min_int = 0
            for i in self.perk_list:
                if i.int_min:
                    min_int += i.int_min
            if min_int < 0:
                min_int = 0
            
            if numgen(1, 100) > self._int:
                self._int += total_amount
            
            if self._int > max_int:
                self._int = max_int
            if self._int < min_int:
                self._int = min_int
            self.face_normal()
        
        def remove_int(self, amount):
            self._int -= amount
            if self._int < 0:
                self._int = 0
            return
        
        def add_fitness(self, amount=1):
            self.add_comfort_chance()
            max_fitness = 100
            total_amount = amount
            if amount > 0:
                for i in self.perk_list:
                    if i.fitness_multi:
                        total_amount = total_amount * i.fitness_multi
            
            for i in self.perk_list:
                if i.fitness_max:
                    max_fitness += i.fitness_max
            
            min_fitness = 0
            for i in self.perk_list:
                if i.fitness_min:
                    min_fitness += i.fitness_min
            if min_fitness < 0:
                min_fitness = 0
            
            if numgen(1, 100) > self._fitness:
                self._fitness += total_amount
            
            if self._fitness > max_fitness:
                self._fitness = max_fitness
            if self._fitness < min_fitness:
                self._fitness = min_fitness
            
            if self.isfat and self._confidence <= 30: 
                self.add_conf(1)
            if self._confidence <= 30 and numgen(1, 100) < 33: 
                self.add_conf(1)
            
            if self.isfat and self._fitness >= 20:
                if self.days_pregnant < (global_pregnancy_length * 0.3):
                    self.pregnancy = 0
            
            elif self.pregnancy == False and self._fitness < 20:
                if self.pregnant in (0,3):
                    self.pregnancy = 1
            
            refresh_avatar()
            self.face_normal()
        
        def set_fitness(self, amount):
            self.add_fitness(-100)
            self._fitness = amount
            self.update_stats()
        
        def remove_fitness(self, amount):
            self._fitness -= amount
            if self._fitness < 0:
                self._fitness = 0
            if self.pregnancy == False and self._fitness < 20:
                if self.pregnant in (0,3):
                    self.pregnancy = 1
            
            refresh_avatar()
        
        def update_stats(self):
            self.add_desire(0)
            self.add_mood(0)
            self.add_tired(0)
            self.add_conf(0)
            self.add_int(0)
            self.add_fitness(0)
        
        def eat(self):
            self.hunger += 100
            if self.hunger > 100:
                self.hunger = 100
            elif self.hunger < 0:
                self.hunger = 0
        
        def add_hunger(self, amount):
            self.hunger -= amount
            if self.hunger > 100:
                self.hunger = 100
            elif self.hunger < 0:
                self.hunger = 0
        
        def add_hygiene(self, amount):
            self.hygiene -= amount
            if self.hygiene > 100:
                self.hygiene = 100
            elif self.hygiene < 0:
                self.hygiene = 0
        
        def add_comfort(self, amount):
            self.body_conf += amount
            if self.body_conf > 0:
                self.body_conf = 0
        
        def add_comfort_chance(self, timer=False):
            if self.body_conf >= 0:
                return
            elif not numgen(0,40):
                if timer:
                    if (t.hour % 3) == 0:
                        self.body_conf += 1
                else:
                    self.body_conf += 1
        
        def stat_deg(self):
            randomnum = renpy.random.randint(1, 100)
            randomnum2 = renpy.random.randint(1, 100)
            
            
            
            if self._fitness >= 15 and randomnum < self._fitness: 
                self._fitness -= 1
            if self._fitness >= 15 and randomnum2 < self._fitness: 
                self._fitness -= 1
            
            if self._int >= 30 and randomnum < self._int: 
                self._int -= 1
            if self._int >= 30 and randomnum2 < self._int: 
                self._int -= 1
            
            if self._confidence >= 60 and randomnum < 50: 
                self._confidence -= 1
            if self._confidence >= 60 and randomnum2 < self._confidence: 
                self._confidence -= 1
            
            if self._confidence <= 10: 
                self._confidence += 1
            if self._confidence <= 30 and randomnum < 50: 
                self._confidence += 1
            if self.pregnancy == 2:
                self._fitness -= 2
            elif self.pregnancy > 2:
                self._fitness -= 4
            
            if self._confidence < 0:
                self._confidence = 0
            if self._int < 0:
                self._int = 0
            if self._fitness < 0:
                self._fitness = 0
            if self.pregnancy == 0 and self._fitness < 20:
                if self.pregnant in (0,3):
                    self.pregnancy = 1
        
        
        
        
        
        def drink(self, amount=10, spiked=False, who=None):
            amount = numgen(1, 8) + amount
            self.add_drunk(amount)
            
            
            if who:
                if not isinstance(who, list):
                    who = [who]
                for i in who:
                    i.drink()
            
            if spiked:
                self.spike_chance()
        
        def beer(self, spiked=False):
            
            randomnum = renpy.random.randint(1, 8)
            amount = randomnum + 10
            self.add_drunk(amount)
            if self._confidence <= 20 and randomnum == 1:
                self.add_conf(1)
            renpy.show_screen("drink")
            if self.right_hand == "beer":
                self.right_hand = ""
            if self.right_hand == "beer":
                self.right_hand = ""
            if spiked:
                self.spike_chance()
        
        def vodka(self):
            
            randomnum = renpy.random.randint(1, 8)
            amount = randomnum + 25
            self.add_drunk(amount)
            if self._confidence <= 20 and randomnum == 1:
                self.add_conf(1)
            renpy.show_screen("drink")
            if self.prop == "beerr":
                self.prop = ""
            elif self.prop == "beerb":
                self.prop = "beerl"
            elif self.prop == "beerl":
                self.prop = ""
        
        def add_drunk(self, amount):
            if self.has_perk(perk_alcoholic):
                amount = amount * 0.5
            if self.has_perk(perk_lightweight):
                amount = amount * 2
            
            if amount > 0 and self.has_perk(perk_hangover, wildcard=False) and perk_hangover.hours:
                self._drunk += perk_hangover.hours * 20
                perk_hangover.hours = None
                self.remove_perk(perk_hangover)
                show_notif_popup("Hair of the dogs back")
            self._drunk += amount
            tiredamount = amount / 4
            moodamount = amount / 2
            
            self.add_mood(moodamount)
            
            self.drunkaddictamount += amount
            if self._drunk > 200:
                self._drunk = 200.0
            elif self._drunk < 0:
                self._drunk = 0.0
            if self.drunkaddictamount >= 500 or self.has_perk(perk_alcoholic):
                self.add_perk(perk_alcoholic, days=7)
            
            
            if self.drunkaddictamount > 3000:
                self.drunkaddictamount = 3000
            elif self.drunkaddictamount < 0:
                self.drunkaddictamount = 0
            self.drunk_perk_checks()
            self.face_normal()
        
        def drunk_perk_checks(self):
            if self.drunk > 100:
                self.add_perk(perk_blackout)
            else:
                self.remove_perk(perk_blackout)
            
            if self.drunk in irange(81,100):
                self.add_perk(perk_wasted)
            else:
                self.remove_perk(perk_wasted)
            
            if self.drunk in irange(50,80):
                self.add_perk(perk_drunk)
            else:
                self.remove_perk(perk_drunk)
            
            if self.drunk in irange(25,49):
                self.add_perk(perk_tipsy)
            else:
                self.remove_perk(perk_tipsy)
        
        def add_high(self, amount):
            self._high += amount
            tiredamount = amount / 4
            self.add_tired(tiredamount)
            self.add_mood(5)
            
            self.highaddictamount += amount
            if self._high > 100:
                self._high = 100
            elif self._high < 0:
                self._high = 0
            if self.highaddictamount >= 500:
                self.highaddict = True
            elif self.highaddictamount < 0:
                self.highaddict = False
            if self.highaddictamount > 10000:
                self._high = 10000
            elif self.highaddictamount < 0:
                self.highaddictamount = 0
            self.face_normal()
        
        def inhib_degrade(self, mins):
            mins = float(mins)
            if self._drunk > 0:
                drunk = mins / 10
                self._drunk -= drunk
            if self._high > 0:
                high = mins / 20
                self._high -= high
            if self._drunk == 0 and self.drunkaddictamount > 0:
                drunkadd = mins / 20
                self.drunkaddictamount -= drunkadd
            if self._high == 0 and self.highaddictamount > 0:
                highadd = mins / 20
                self.highaddictamount -= highadd
            if self._drunk > 150:
                self._drunk = 150
            elif self._drunk < 0:
                self._drunk = 0
            if self._high > 150:
                self._high = 150
            elif self._high < 0:
                self._high = 0
            self.drunk_perk_checks()
            
            return
        
        def inhib_sleep(self): 
            if self.drunk > 0 or self.high > 0:
                inhib = ((self.drunk + self.high) / 15)
                if inhib > 0:
                    self.add_perk(perk_hangover, hours=inhib)
                self._drunk = 0
                self._high = 0
                self.remove_perk([perk_drunk, perk_tipsy, perk_wasted, perk_blackout])
        
        def inhib_puke(self):
            self.add_mood(-50)
            self.add_desire(-50)
            self.add_tired(-30)
            self.add_hunger(100)
            self.add_conf(-5)
            randomnum = renpy.random.randint(15, 30)
            self._drunk = randomnum
            self.face_normal
        
        def spike_chance(self):
            if not numgen(0,40):
                self.add_perk(perk_lebo, hours=4)
                self.add_desire(1000)
            if not numgen(0,40):
                self.add_perk(perk_joy, hours=4)
                self.add_mood(200) 
        
        def is_working(self, sexy_job_only=False):
            
            
            if dis(dis_partyhouse) and school_dance_at_party():
                return True
            elif dis(dis_pub) and pub_waitress.workcycle:
                return True
            elif quest_flyers.workcycle and not sexy_job_only:
                return True
            elif quest_cleaner.workcycle and not sexy_job_only:
                return True
            elif loc(loc_park) and tab_top in "work":
                return True
            elif quest_scav.workcycle and not sexy_job_only:
                return True
            else:
                return False
        
        
        
        
        
        
        def add_suntan(self,amount):
            self.suntan += amount
            if self.suntan > 1:
                self.suntan = 1
            if self.suntan < 0:
                self.suntan = 0
        
        
        
        
        
        def surgery_vvirgin(self):
            self.vvirgin = True
            self.firstvsex = "I have never had sex so must be a virgin."
            self.creamsafe = 0
            self.creamnormal = 0
            self.creamdanger = 0
            self.firstasex = ""
            self.vsex = 0
            self.preg_desire = 0
            self.sex_iswhore_calculate()
            self.sex_isslut_calculate()
        
        def surgery_avirgin(self):
            self.avirgin = True
            self.firstasex = ""
            self.asex = 0
            self.creamanal = 0
            self.sex_iswhore_calculate()
            self.sex_isslut_calculate()
        
        def surgery_allvirgin(self):
            self.hvirgin = True
            self.ovirgin = True
            self.hsex = 0
            self.osex = 0
            self.swallow = 0
            self.facial = 0
            self.sex_iswhore_calculate()
            self.sex_isslut_calculate()
        
        def surgery_all_sex_stats(self):
            self.surgery_vvirgin()
            self.surgery_avirgin()
            self.surgery_allvirgin()
            self.sold = 0 
            self.soldpricetotal = 0
            self.rape = 0
            self.assault = 0
            self.sex_iswhore_calculate()
            self.sex_isslut_calculate()
        
        
        
        
        
        def sex_hideaction(self):
            
            renpy.hide_screen("sex_action_flash")
            renpy.hide_screen("cum_action")
            renpy.hide_screen("punch")
            renpy.hide_screen("spank_bum")
            renpy.hide_screen("sex_action_image", layer="fg_screen")
            renpy.hide_screen("sex_cum_action_image", layer="fg_screen")
            renpy.hide_screen("nosex_cum_action_image", layer="fg_screen")
        
        def sex_cum_location_offer(self, 
        choice_inside="Cum inside me", 
        choice_pullout="Pullout!",
        choice_preg_want="Fuck me fuck me. Fill me! \u2665", 
        choice_preg_know="I'm pregnant so cum where you want", 
        difficulty=2, cum_want="", cum_notwant="", cum_pullout="", cum_pullout_anal="", cum_pullout_bj="", cum_pullout_poke="", cum_bj="",  
        block_anal_check=False, block_broken=False, block_drunk=False, block_horny=False, block_nowill=False,
        ):
            want_pullout = False
            
            if "mouth" in self.sex_holes:
                if not self.gagged:
                    renpy.say(pcc, "Mmmmff!")
                else:
                    renpy.say(None, "I can't refuse.")
                want_pullout = False
            
            elif self.selling and self.soldrequest == "creampie":
                if not self.gagged:
                    renpy.say(pcc, "You wanted to cum inside? Fill me up!")
                else:
                    renpy.say(None, "I wiggle my bum making it clear he can do as he wants inside me.")
                want_pullout = False
            
            elif self.has_perk(perk_creampie_lover) and not self.cycle_conditions["stage"] == "ovulate":
                if not self.gagged:
                    renpy.say(pcc, "I love it inside me! Fill me up!")
                else:
                    renpy.say(None, "I wiggle my bum making it clear he can do as he wants inside me.")
                want_pullout = False
            
            elif self.preg_knows:
                if not self.gagged:
                    renpy.say(pcc, "I'm already pregnant so cum where you want.")
                else:
                    renpy.say(None, "I don't make much reaction, making it clear I don't care where he cums.")
                want_pullout = False
            
            elif self.has_perk([perk_broodmother, perk_preg_want]):
                if not self.gagged:
                    renpy.say(pcc, "Inside of course. Get me pregnant!")
                else:
                    renpy.say(None, "I wiggle my bum making it clear he can do as he wants inside me.")
                want_pullout = False
            
            
            elif self.has_perk(perk_sucu):
                renpy.say(pcmc, "I need it in me!")
                want_pullout = False
            
            elif self.isbroken and not block_broken: 
                if not self.gagged:
                    renpy.say(pcc, "Cum where you want to.")
                else:
                    renpy.say(None, "I don't make much reaction, making it clear he can cum where he wants.")
                want_pullout = False
            
            elif self.cycle_conditions["stage"] == "mens" or self.cycle_conditions["stage"] == "no_cycle":
                if not self.gagged:
                    renpy.say(pcmc, "Doesn't matter where you cum. Put it where you want.")
                else:
                    renpy.say(None, "I don't make much reaction, making it clear he can cum where he wants.")
                want_pullout = False
            
            elif self.has_perk(perk_preg_notwant): 
                if not self.gagged:
                    renpy.say(pcc, "I don't want to end up pregnant.")
                else:
                    renpy.say(None, "I try to pull away from him and hope he understands I don't want it inside me.")
                want_pullout = True
            
            elif player.check_drunk(5) and not block_drunk: 
                if not self.gagged:
                    renpy.say(pcc, "Fuck I am too drunk to care where you cum.")
                else:
                    renpy.say(None, "I don't make much reaction, making it clear he can cum where he wants.")
                want_pullout = False
            
            else:
                if self.check_pullout(): 
                    _window_hide(auto=True)
                    want_pullout = renpy.display_menu([
                    (choice_inside, False),
                    (choice_pullout, True), 
                    ("Haaaa \u2665", If(numgen(1, 10) <= 3, True, False)),
                    ])
                    _window_show(auto=True)
                    
                    if want_pullout:
                        self.add_preg_desire(-5)
                    else:
                        self.add_preg_desire(10)
                
                else:
                    if not self.gagged:
                        renpy.say(pcc, "Haaaa \u2665")
                    want_pullout = If(numgen(1, 10) <=3, True, False)
            
            self.want_pullout = want_pullout
            self.have_pullout = self.check_speech(difficulty, notif=False)
            
            if self.want_pullout:
                
                if self.check_sex_agree(4, notif=False) and renpy.has_label(cum_bj) and not self.preg_knows: 
                    renpy.say(pcmc, "Should suck him off so he doesn't decide to cum inside.")
                    renpy.jump(cum_bj)
                
                if self.have_pullout and renpy.has_label(cum_pullout): 
                    if renpy.random.randint(1, 10) == 1 and (block_anal_check or (not block_anal_check and self.check_anal_agree(notif=False))) and renpy.has_label(cum_pullout_anal): 
                        renpy.jump(cum_pullout_anal)
                    elif renpy.random.randint(1, 10) > 3 and renpy.has_label(cum_pullout_bj): 
                        renpy.jump(cum_pullout_bj)
                    else: 
                        renpy.jump(cum_pullout)
                
                elif not self.have_pullout: 
                    if self.preg_knows and renpy.has_label(cum_want): 
                        renpy.say(pcmc, "Fuck it, I am already pregnant so who cares.")
                        renpy.jump(cum_want)
                    if renpy.random.randint(1, 8) == 1 and renpy.has_label(cum_pullout_poke):
                        renpy.jump(cum_pullout_poke)
                    elif renpy.has_label(cum_notwant): 
                        renpy.jump(cum_notwant)
            
            else: 
                if renpy.random.randint(1, 5) == 1 and renpy.has_label(cum_pullout_poke):
                    renpy.jump(cum_pullout_poke)
                elif renpy.random.randint(1, 10) == 1 and (block_anal_check or (not block_anal_check and self.check_anal_agree(notif=False))) and renpy.has_label(cum_pullout_anal): 
                    renpy.jump(cum_pullout_anal)
                elif renpy.random.randint(1, 15) == 1 and renpy.has_label(cum_pullout_bj): 
                    renpy.jump(cum_pullout_bj)
                elif renpy.random.randint(1, 20) == 1 and renpy.has_label(cum_pullout): 
                    renpy.jump(cum_pullout)
                elif renpy.has_label(cum_want):
                    renpy.jump(cum_want)
        
        def sex_cum_anal_location_offer(self, 
        choice_inside="Mmm, fill me up!", 
        choice_pullout="Mmm. Pull out and cover me with your cum!",
        difficulty=1, cum_want="", cum_notwant="", cum_pullout="",  
        block_anal_check=False, block_broken=False, block_drunk=False, block_horny=False, block_nowill=False,
        ):
            want_pullout = False
            
            if "mouth" in self.sex_holes:
                if not self.gagged:
                    renpy.say(pcc, "Mmmmff!")
                else:
                    renpy.say(None, "I can't refuse.")
                want_pullout = False
            
            elif self.selling and self.soldrequest == "creampie":
                if not self.gagged:
                    renpy.say(pcc, "You wanted to cum inside? Fill me up!")
                else:
                    renpy.say(None, "I wiggle my bum making it clear he can do as he wants inside me.")
                want_pullout = False
            
            elif self.has_perk(perk_creampie_lover, notif=True):
                if not self.gagged:
                    renpy.say(pcc, "I love it inside me! Fill me up!")
                else:
                    renpy.say(None, "I wiggle my bum making it clear he can do as he wants inside me.")
                want_pullout = False
            
            elif self.has_perk(perk_sucu, notif=True):
                renpy.say(pcmc, "I need it in me!")
                want_pullout = False
            
            elif self.has_perk([perk_meek, perk_broken], notif=True) and not block_broken: 
                renpy.say(pcmc, "Cum where you want to.")
                want_pullout = False
            
            elif player.check_drunk(5) and not block_drunk: 
                renpy.say(pcmc, "Fuck I am too drunk to care where you cum.")
                want_pullout = False
            
            else:
                if self.check_pullout(): 
                    _window_hide(auto=True)
                    want_pullout = renpy.display_menu([
                    (choice_inside, False),
                    (choice_pullout, True), 
                    ("Haaaa \u2665", If(numgen(1, 10) <= 3, True, False)),
                    ])
                    _window_show(auto=True)
                
                else:
                    if not self.gagged:
                        renpy.say(pcc, "Haaaa \u2665")
                    want_pullout = If(numgen(1, 10) <=3, True, False)
            
            self.want_pullout = want_pullout
            self.have_pullout = self.check_speech(difficulty, notif=False)
            
            if self.want_pullout:
                
                if self.have_pullout and renpy.has_label(cum_pullout): 
                    if renpy.has_label(cum_pullout): 
                        renpy.jump(cum_pullout)
                
                elif not self.have_pullout: 
                    if renpy.has_label(cum_notwant): 
                        renpy.jump(cum_notwant)
            
            else: 
                if renpy.random.randint(1, 20) == 1 and renpy.has_label(cum_pullout): 
                    renpy.jump(cum_pullout)
                elif renpy.has_label(cum_want):
                    renpy.jump(cum_want)
        
        
        def sex_location_offer(self, diff=2, option1="",option2="", option3="", always_3=True, sex_other="", sex_vag_want="", sex_vag_notwant="", sex_anal="", who=""):  
            
            vag = self.check_vag_agree()  
            anal = self.check_anal_agree()  
            if isinstance(who, Npc): 
                who = who.name
            if option1 == "":
                option1 = self.sex_location_offer_vag_description()   
            if option2 == "":
                option2 = self.sex_location_offer_anal_description()
            
            if self.isbroken:
                self.want_sexlocation = 0
                if self.have_sexlocation:
                    self.want_sexlocation = self.have_sexlocation
                elif sex_vag_want:
                    self.want_sexlocation = 1
                elif sex_anal:
                    self.want_sexlocation = 2
            
            elif option3 and always_3:
                if vag and anal:
                    self.want_sexlocation = renpy.display_menu([(option1, 1), (option2, 2), (option3, 0)])
                elif vag and not anal:
                    self.want_sexlocation = renpy.display_menu([(option1, 1), (option3, 0)])
                elif anal and not vag:
                    self.want_sexlocation = renpy.display_menu([(option2, 2), (option3, 0)])
                else:
                    self.want_sexlocation = 0
            
            elif not vag and not anal:
                
                self.want_sexlocation = 0
            elif not vag and anal:
                
                self.want_sexlocation = 2
            elif vag and not anal:
                
                self.want_sexlocation = 1
            else:
                
                _window_hide(auto=True)
                if option3:
                    self.want_sexlocation = renpy.display_menu([(option1, 1),(option2, 2), (option3, 0)])
                else:
                    self.want_sexlocation = renpy.display_menu([(option1, 1),(option2, 2)])
            
            self.sex_location_offer_picker(diff)
            if sex_vag_want and self.have_sexlocation == 1 and self.want_sexlocation == 2:
                
                renpy.say(who, "What? I want to fuck your pussy!")
                if self.vvirgin:
                    if self.soldprice:
                        renpy.say(pcmc, "Selling my virginity for £" + str(self.soldprice) + " just feels dirty...")
                    else:
                        renpy.say(pcmc, "I don't think I am ready to lose my virginity...")
                if not self.gagged:
                    renpy.say(pcc, "Sorry mate, In my bum or nothing.")
                self.spank()
                if self.check_speech(2):
                    self.have_sexlocation = 2
                    if renpy.has_label(sex_anal):
                        renpy.jump(sex_anal)
                else:
                    if renpy.has_label(sex_vag_notwant):
                        renpy.jump(sex_vag_notwant)
            elif self.want_sexlocation == 1 and renpy.has_label(sex_vag_want):
                renpy.jump(sex_vag_want)
            elif self.want_sexlocation == 2 and renpy.has_label(sex_anal):
                renpy.jump(sex_anal)
            else:
                if renpy.has_label(sex_other):
                    renpy.jump(sex_other)
                elif renpy.has_label(sex_vag_want):
                    renpy.jump(sex_vag_want)  
        
        def sex_location_offer_picker(self, diff=2):
            if self.want_sexlocation == 0:
                
                randomnum = renpy.random.randint(1, 10)
                if randomnum == 1:
                    self.have_sexlocation = 2
                else:
                    self.have_sexlocation = 1
            elif self.want_sexlocation == 1:
                
                self.have_sexlocation = 1
            else:
                
                randomnum = renpy.random.randint(1, 10)
                if randomnum == 1:
                    self.have_sexlocation = 2
                else:
                    if self.check_speech(diff):
                        self.have_sexlocation = 2
                    else:
                        self.have_sexlocation = 1
            _window_show(auto=True)
            return
        
        def sex_location_offer_vag_description(self):
            option1 = ""
            if self.has_perk(perk_preg_want) and not self.preg_knows:
                if self.cycle_conditions["stage"] == "ovulate":
                    option1 = "This is a good time so use my pussy"
                else:
                    option1 = "In my pussy"
            elif self.has_perk(perk_preg_notwant) and not self.preg_knows:
                if self.cycle_conditions["stage"] == "ovulate":
                    option1 = "This is a dangerous time... But you can use my pussy"
                else:
                    option1 = "Hope I don't regret this, but you can use my pussy"
            else:
                option1 = "Use my pussy"
            return option1
        def sex_location_offer_anal_description(self):
            option2 = ""
            if self.cycle_conditions["stage"] == "mens" and not player.pregnant:
                option2 = "Use my arse since I am on my period"
            elif self.has_perk(perk_preg_want) and not self.preg_knows:
                option2 = "Ugh, can't get pregnant from it but use my arse"
            elif self.has_perk(perk_preg_notwant) and not self.preg_knows:
                option2 = "Use my arse so I don't get pregnant"
            else:
                option2 = "Put it in my bum"
            return option2
        
        def sex_location(self,location):
            
            self.sexlocation = location
        
        def sex_finger(self, person):
            
            
            
            
            renpy.show_screen("vagsex_action")
        
        def sex_pen_popup(location="vag"):
            if renpy.get_screen("blackout"):
                return "Broken"
            if location == "vag" and self.vvirgin:
                renpy.show_screen("sex_action_flash", "virgin")
            else:
                renpy.show_screen("sex_action_flash", location)
            
            penetratenum = renpy.random.randint(1, 3)
            renpy.show_screen("sex_action_image", location)
        
        def sex_cum_popup(location="vag"):
            if renpy.get_screen("blackout"):
                return "bkeoeo"
            cumnum = renpy.random.randint(1, 3)
            renpy.show_screen("sex_cum_action_image", location)  
        
        def nosex_les(self, person):
            person.nosex_les += 1
        
        def sex_les(self, person):
            person.sex_les += 1
        
        def sex_hand(self, person, quest=None):
            
            
            if self.sex_man_amount: 
                self.sex_man_amount -= 1
            if self.soldprice:
                self.sex_sold(person, self.soldprice, quest)
            call_label = False
            if self.hsex == 0:
                call_label = True
                self.hvirgin = False
                person.hvirgin = True
                if quest:
                    quest.hvirgin + True
            person.hsex += 1
            self.hsex += 1
            if quest:
                quest.hsex += 1
        
        def sex_oral(self, person, quest=None):
            
            
            if self.sex_man_amount: 
                self.sex_man_amount -= 1
            if self.soldprice:
                self.sex_sold(person, self.soldprice, quest)
            if self.osex == 0:
                self.ovirgin = False
                person.ovirgin = True
                if quest:
                    quest.ovirgin = True
            person.osex += 1
            self.osex += 1
            if quest:
                quest.osex += 1
        
        def sex_vag(self, person, quest=None):
            self.having_sex = True
            
            if person.is_female:
                
                if self.vsex == 0:
                    if quest:
                        quest.vvirgin = True
                    person.vvirgin = True 
                    self.vvirgin = False
                    renpy.show_screen("sex_action_flash", "virgin")
                    self.sex_virgin(person, quest)
                    diary_virginity_func(person, quest) 
                    if self.beingraped:
                        self.add_perk(perk_cherry_taken, hours=48)
                    elif self.selling:
                        self.add_perk(perk_cherry_sold, hours=24)
                    else:
                        self.add_perk(perk_cherry, hours=24)
                else:
                    renpy.show_screen("sex_action_flash")
                if self.beingraped:
                    self.face_pain()
                else:
                    self.face_happy()
                
                self.vsex += 1
                if quest:
                    quest.vsex += 1
                sex_pen_popup(location="vag") 
                
                return
            
            if self.sex_man_amount: 
                self.sex_man_amount -= 1
            if self.soldprice:
                self.sex_sold(person, self.soldprice, quest)
            if self.vsex == 0:
                if quest:
                    quest.vvirgin = True
                person.vvirgin = True 
                self.vvirgin = False
                renpy.show_screen("sex_action_flash", "virgin")
                self.sex_virgin(person, quest)
                diary_virginity_func(person, quest) 
                if self.beingraped:
                    self.add_perk(perk_cherry_taken, hours=48)
                elif self.selling:
                    self.add_perk(perk_cherry_sold, hours=24)
                else:
                    self.add_perk(perk_cherry, hours=24)
            else:
                renpy.show_screen("sex_action_flash")
            if self.beingraped:
                self.face_pain()
            else:
                self.face_happy()
            person.vsex += 1
            self.vsex += 1
            if quest:
                quest.vsex += 1
            sex_pen_popup(location="vag")
            
            if self.sex_cum_pregcheck("insert", quest):
                
                self.preg(person, quest)
            
            if self.beingraped: 
                self.sex_forced_pen(person, quest)
            
            if not self.beingraped:
                self.add_preg_desire(1)
                if self.cycle_conditions["stage"] == "ovulate":
                    self.add_preg_desire(2)
            
            if writing.ass:
                writing.ass_counter_check(person)
        
        
        
        def sex_anal(self, person, quest=None):
            self.having_sex = True
            
            if person.is_female:
                
                if self.asex == 0:
                    person.avirgin = True 
                    self.avirgin = False
                    self.firstasex = person.fullname
                    if quest:
                        quest.avirgin = True
                
                if self.beingraped:
                    self.face_pain()
                else:
                    self.face_happy()
                
                renpy.show_screen("sex_action_flash", "anal")
                sex_pen_popup(location="anal") 
                
                self.asex += 1
                if quest:
                    quest.asex += 1
                
                
                
                
                return
            if self.sex_man_amount: 
                self.sex_man_amount -= 1
            if self.soldprice:
                self.sex_sold(person, self.soldprice, quest)
            if self.asex == 0:
                person.avirgin = True 
                self.avirgin = False
                self.firstasex = person.fullname
                if quest:
                    quest.avirgin = True
            
            if self.beingraped:
                self.face_pain()
            else:
                self.face_happy()
            
            renpy.show_screen("sex_action_flash", "anal")
            sex_pen_popup(location="anal")
            person.asex += 1
            self.asex += 1
            if quest:
                quest.asex += 1
            self.add_preg_desire(-1)
            if self.beingraped: 
                self.sex_forced_pen(person, quest)
            
            if writing.ass:
                writing.ass_counter_check(person)
        
        
        def sex_sold(self, person, price, quest=None):
            
            self.selling = True
            
            self.sold += 1
            person.sold += 1
            self.soldpricetotal += self.soldprice
            person.soldpricetotal += self.soldprice
            if quest:
                quest.sold += 1
                quest.soldpricetotal += self.soldprice
            
            if not (self.iswhore or self.isslut or self.isbroken):
                self.add_mood(-10)
                self.add_conf(-3)
            self.add_desire(-20)
            self.sex_iswhore_calculate()
            if self.soldprice and not self.sex_man_amount:
                self.soldprice = 0
        
        def sex_forced(self, person, quest=None):
            self.beingraped = True
            person.assault += 1
            self.assault += 1
            if self.assault >= 20:
                player.add_perk(perk_numb)
            if quest:
                quest.assault += 1
            if not self.isbroken:
                self.add_desire(-20)
                
                self.add_mood(-15)
        
        def sex_forced_pen(self, person, quest=None):
            if quest:
                quest.assault -= 1
                quest.rape += 1
            self.assault -= 1  
            self.rape += 1
            if self.rape >= 5:
                self.add_perk(perk_numb)
            person.assault -= 1
            person.rape += 1
            if not self.recovering:
                self.add_conf(-20)
            
            
            
            if not self.isbroken:
                self.add_desire(-100)
                self.add_mood(-100)
                self.add_tired(-30)
                if self._tired <= 20: 
                    self._tired = 20
                self.add_drunk(-10)
                if not self.has_perk([perk_slut, perk_broken, perk_numb, perk_whore], wildcard=False):
                    self.add_perk(perk_recovering, days=numgen(1, 5))
        
        def sex_blackout(self, person, quest=None, times=1, forced=False):
            if forced:
                self.sex_forced(person)
            for _ in range(times):
                if not numgen(0,10): 
                    if numgen():
                        self.sex_cum(person, "ass", quest)
                    else:
                        self.sex_cum(person, "pullout", quest)
                elif numgen(0,5):
                    self.sex_vag(person, quest)
                    if numgen():
                        self.sex_cum(person, "inside", quest)
                    else:
                        self.sex_cum(person, "pullout", quest)
                else:
                    self.sex_anal(person, quest)
                    self.sex_cum(person, "anus", quest)
            
            self.sex_hideaction()
        
        def sex_pub_puke(self):
            randomnum = renpy.random.randint(0, 10)
            if randomnum > 7:
                self.sex_forced(unknown)
                randomnum = renpy.random.randint(0, 3)
                if randomnum == 0:
                    self.sex_anal(unknown)
                    randomnum = renpy.random.randint(0, 3)
                    if randomnum == 0:
                        self.sex_cum(unknown, "anal")
                    else:
                        self.sex_cum(unknown, "ass")
                else:
                    self.sex_vag(unknown)
                    randomnum = renpy.random.randint(0, 5)
                    if randomnum == 0:
                        self.sex_cum(unknown, "ass")
                    elif randomnum == 1:
                        self.sex_cum(unknown, "pullout")
                    else:
                        self.sex_cum(unknown, "inside")
            else:
                randomnum = renpy.random.randint(0, 1)
                if randomnum == 1:
                    self.sex_cum(unknown, "ass") 
                else:
                    self.sex_cum(unknown, "pullout") 
        
        def sex_sleep(self):
            self.sex_forced(unknown)
            randomnum = renpy.random.randint(0, 3)
            if randomnum == 0:
                self.sex_anal(unknown)
                randomnum = renpy.random.randint(0, 3)
                if randomnum == 0:
                    self.sex_cum(unknown, "anal")
                else:
                    self.sex_cum(unknown, "ass")
            else:
                self.sex_vag(unknown)
                randomnum = renpy.random.randint(0, 5)
                if randomnum == 0:
                    self.sex_cum(unknown, "ass")
                elif randomnum == 1:
                    self.sex_cum(unknown, "pullout")
                else:
                    self.sex_cum(unknown, "inside")
        
        def sex_end(self):
            
            if self.beingraped == True or self.selling == True:
                self.reset_sex_status()
            else:
                
                self.reset_sex_status()
                self.add_mood(-10)
                self.add_desire(100)
                self.add_conf(-5)
                self.having_sex = False
        
        def sex_cum(self, person, where="", quest=None, no_sex=False, during_dia=False):
            location = where
            
            if person == nosex:
                no_sex = True
            
            if self.beingraped:
                self.face_cry()
            
            if during_dia: 
                self.add_mood(numgen(0,10))
                self.add_desire(-numgen(30,80))
                renpy.show_screen("cum_action", "pink", numgen(1,2))
                return
            
            if numgen(1, 100) > self._confidence and not (self.beingraped or self.selling):
                self.add_conf(1)
            
            if not (location == "self" or person.is_female):
                renpy.show_screen("cum_action")
                if self.has_perk(perk_sucu):
                    self.add_tired(10, sucu=True)
                person.cum()
            
            if not (location in ("face", "hand", "mouth") or no_sex):
                self.add_desire(-numgen(60,120))
            
            if not (self.recovering and no_sex) or not self.beingraped:
                self.add_mood(10)
            
            if location == "self": 
                self.add_mood(10)
                self.add_desire(-numgen(60,120))
                renpy.show_screen("cum_action", "pink", numgen(1,2))
            elif person.is_female: 
                self.add_mood(10)
                self.add_desire(-numgen(60,120))
                renpy.show_screen("cum_action", "pink", numgen(1,2))
                person.cum()
            elif location == "face":
                sex_cum_popup("face")
                self.facial += 1
                person.facial += 1
                if quest:
                    quest.facial += 1
                self.sex_cum_apply("cum_face")
            
            elif location == "hand":
                self.sex_cum_apply("cum_hand")
            elif location == "mouth":
                sex_cum_popup("mouth")
                self.swallow += 1
                person.swallow += 1
                if quest:
                    quest.swallow += 1
                self.sex_cum_apply("cum_mouth")
            
            
            elif location in ("chest", "tits"):
                self.sex_cum_apply("cum_chest")
                self.buk += 1
                person.buk += 1
                if quest:
                    quest.buk += 1
            
            elif location in ("stomach", "belly"):
                self.sex_cum_apply("cum_belly")
                self.buk += 1
                person.buk += 1
                if quest:
                    quest.buk += 1
                sex_cum_popup("poke")
            
            elif location in ("anal", "anus"):
                self.creamanal += 1
                person.creamanal += 1
                if quest:
                    quest.creamanal += 1
                self.sex_cum_apply("cum_assin") 
                sex_cum_popup("anal")
            
            elif location == "ass":
                self.sex_cum_apply("cum_assout")
                self.buk += 1
                person.buk += 1
                if quest:
                    quest.buk += 1
                sex_cum_popup("ass")
            
            elif location == "pullout":
                self.sex_cum_apply("cum_vagout")
                self.sex_cum_apply("cum_belly")
                self.add_preg_desire(-1)
                self.buk += 1
                person.buk += 1
                if quest:
                    quest.buk += 1
                sex_cum_popup("poke")
            
            elif location == "inside":
                self.sex_cum_apply("cum_vagin")
                sex_cum_popup("vag")
                if self.virgin_pregcheck == True and self.pregpills == False:
                    
                    self.add_preg_desire(20)
                    if not self.vvirgin:
                        if self.beingraped:
                            desc = "\n\nThe arsehole finished inside me so I hope I dont end up carrying the rapist cunts baby..."
                        elif self.selling:
                            desc = "\n\nHe ended up finishing inside me, so I hope I don't end up carrying a baby of someone who paid to fuck me..."
                        else:
                            if person == ghman:
                                desc = "\n\nI could feel him cumming and I kept pressing against him anyway. I could have stopped him or pulled out, but I didn't want to. I wanted to feel him inside me for my first time."
                            else:
                                desc = "\n\nHe ended up finishing inside me. They say you can't get pregnant your first time, but we all know what horse shit that is."
                            if self.has_perk(perk_preg_want) and not self.has_perk(perk_period):
                                desc = desc + " Maybe I will be lucky and end up with something nice in my belly."
                            elif self.has_perk(perk_preg_notwant) and not self.has_perk(perk_period):
                                desc = desc + " Hopefully luck is on my side and I don't end up swelling up like a baloon."
                        
                        diary_virginity.description = diary_virginity.description + desc
                if self.pregpills == True:
                    self.add_preg_desire(-1)
                    self.creamsafe += 1
                    person.creamsafe += 1
                    if quest:
                        quest.creamsafe
                else:
                    if self.cycle_conditions["stage"] == "mens":
                        self.creamsafe += 1
                        person.creamsafe += 1
                        if quest:
                            quest.creamsafe += 1
                    elif self.cycle_conditions["stage"] == "ovulate":
                        self.creamdanger += 1
                        person.creamdanger += 1
                        if quest:
                            quest.creamdanger += 1
                        self.add_preg_desire(2)
                    else:
                        self.creamnormal += 1
                        person.creamnormal += 1
                        if quest:
                            quest.creamnormal += 1
                        self.add_preg_desire(1)
            
            
            
            if self.sex_cum_pregcheck(where, quest):
                self.preg(person, quest)
            else:
                self.reset_sex_status()
        
        def sex_cum_pregcheck(self, where, quest=None):
            if self.cycle_conditions["stage"] in ("mens", "no_cycle"):
                return False
            stage = self.cycle_conditions["stage"]
            fertility = self.cycle_get_fertility()
            if where == "inside" and not player.has_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_2, perk_pregnant_3]):
                self.add_perk(perk_inseminated, hours=6)
                fertility = 4 / fertility
            elif where == "pullout":
                fertility = 30 / fertility
            
            
            elif where == "insert":
                
                
                fertility = 80 / fertility
            else:
                return False
            
            self._last_cumin = t.day
            
            if not numgen(0, int(fertility)):
                return True
            else:
                return False
        
        def sex_cum_apply(self, where):
            cumamount = renpy.random.randint(1, 3)
            self.cum_locations[where] += cumamount
            if self.cum_locations[where] >= 20:
                self.cum_locations[where] = 20
        
        
        def sex_virgin(self, person, quest):
            
            if not person.virginname in ["", "some random"]: 
                self.firstvsex = person.virginname
            elif self.selling == True:
                if person.virginname == "some random":
                    self.firstvsex = "I sold my virginity to some random " + str(person.fullname) + " for £ " + str(self.soldprice) + "."
                else:
                    self.firstvsex = "I sold my virginity to " + str(person.fullname) + " for £ " + str(self.soldprice) + "."
                
                if self._drunk > 50:
                    self.firstvsex = self.firstvsex + " I was pretty drunk at the time."
                elif self._drunk > 80:
                    self.firstvsex = self.firstvsex + " I was totally wasted at the time."
            
            elif self.beingraped == True:
                if person.virginname == "some random":
                    self.firstvsex = "Some random " + str(person.fullname)
                else:
                    self.firstvsex = str(person.fullname)
                
                if self._drunk > 50:
                    self.firstvsex = str(self.firstvsex) + " took my virginity when he raped me while I was drunk."
                elif self._drunk > 80:
                    self.firstvsex = str(self.firstvsex) + " took my virginity when he raped while I was completely wasted."
                else:
                    self.firstvsex = str(self.firstvsex) + " took my virginity when he raped me."
            
            else:
                if person.virginname == "some random":
                    self.firstvsex = "Some random " + str(person.fullname) + " claimed my virginity"
                else:
                    self.firstvsex = str(person.fullname) + " claimed my virginity"
                
                if self._drunk > 50:
                    self.firstvsex = self.firstvsex + " while I was pretty drunk."
                elif self._drunk > 80:
                    self.firstvsex = self.firstvsex + " while I was totally wasted."
                else:
                    self.firstvsex = self.firstvsex + "."  
        
        def sex_isslut_calculate(self):
            if self.has_perk(perk_slut, wildcard=False):
                return "Already has the perk"
            totalsex = 0
            for i in npc_all:
                if not i.is_female:
                    if i.is_unique:
                        if i.sex and not (i.rape or i.sold):
                            totalsex += 1
                    elif i.sex:
                        totalsex += ((i.sex * 0.7) - (i.rape + i.sold))
            if totalsex > 20:
                self.add_perk(perk_slut)
            return totalsex
        
        def sex_iswhore_calculate(self):
            if self.sold > 30 and not self.has_perk(perk_whore, wildcard=False):
                self.add_perk(perk_whore)
        
        
        
        
        
        def preg(self, person, quest=None):
            if self.pregnant or self.pregpills or self.cycle_conditions["stage"] == "no_cycle" or not cheat_pregnancy_enabled:
                self.reset_sex_status()
                
                return
            else:
                self.pregnant = 1
                self.preg_father_class = person
                self.set_preg_father_colour(person)
                if quest:
                    self.preg_quest_class = quest
                if self.virgin_pregcheck:
                    self.virginbaby = True
                self.preg_father(person)
                self.reset_sex_status()
        
        def preg_father(self, person):
            if person == unknown:
                self.father = "I am pregnant but I have no idea who the father is."
            elif person == rapist:
                self.rapebaby = True
                self.father = "I was impregnated after being raped."
            
            else:
                if player.vvirgin:
                    self.father = "I have no idea how. But somehow I have managed to get pregnant despite being a virgin at the time... "
                if person.pregname == "":
                    self.father = str(self.father) + "I am carrying the child of " + str(person.fullname)
                else:
                    self.father = str(self.father) + str(person.pregname)
                
                if self.beingraped:
                    self.rapebaby = True
                    self.father = str(self.father) + " who impregnated me while raping me."
                elif self.selling:
                    self.soldbaby = True
                    self.father = str(self.father) + " who paid to fuck me."
                else:
                    self.father = str(self.father) + "."
                
                if self._drunk >= 80:
                    self.father = str(self.father) + " I was shit drunk at the time and didn't really know what was going on."
                if self.virgin_pregcheck and not self.vvirgin:
                    self.father = str(self.father) + " I was a virgin while being impregnated."
                if not self.soldprice == 0: 
                    self.father = str(self.father) + " It cost him £ " + str(self.soldprice) + " to make me carry his baby."
            self.reset_sex_status()
        
        def set_preg_father_colour(self, person=None):
            global npc_race, npc_race2, npc_race3
            if isinstance(person, Npc):
                if person.skinbase:
                    self.preg_father_colour = person.skinshad
                elif person is tempname:
                    self.preg_father_colour = get_npc_skin_colour(False)
                elif person is tempname2:
                    self.preg_father_colour = get_npc2_skin_colour(False)
                elif person is tempname3:
                    self.preg_father_colour = get_npc3_skin_colour(False)
                else:
                    self.preg_father_colour = get_npc_skin_colour(False)
            else:
                self.preg_father_colour = get_skin_colour(False)
        
        def preg_text(self):
            if self.preg_knows:
                desc = self.father
            elif not cheat_pregnancy_enabled:
                desc = "I am unable to get pregnant so I don't have to worry about that."
            elif self.has_perk(perk_preg_want):
                if self.vvirgin:
                    desc = "I am not pregnant. I should probably lose my virginity to someone to help fix that."
                else:
                    desc = "I am not pregnant yet but let's hope it will happen soon."
            elif self.has_perk(perk_preg_notwant):
                desc = "I am not pregnant and let's keep it that way."
            else:
                desc = "I am not pregnant."
            return desc
        
        def preg_test(self):
            global global_pregnancy_length
            if self.days_pregnant >= (global_pregnancy_length * 0.04):
                if not self.preg_knows:
                    if self.pregnant > 0:
                        self.preg_amount += 1
                        self.check_preg_perks()
                        self.preg_desire = 0
                    if self.vvirgin == True:
                        self.firstvsex = "I am still a virgin but somehow managed to get pregnant."
                    if self.virginbaby == True and self.vvirgin == False:
                        self.firstvsex = str(self.firstvsex) + " I found out some time later that he also got me pregnant."
                    if not self.pregbabies:
                        diary_preg_first_func()
                    else:
                        diary_preg_again_func()
                    self.preg_father_class.preg += 1
                    if not self.preg_quest_class == nosex:
                        self.preg_quest_class.preg += 1
                return True
            else:
                return False
        
        
        def give_birth(self, pass_time=True):
            if pass_time:
                t.hour = numgen(10,30) 
            
            diary_preg_birth_func() 
            self.pregbabies += 1
            self.preg_father_class.pregbabies += 1
            if not self.preg_quest_class == nosex:
                self.preg_quest_class.pregbabies += 1
            self.pregnant = 0
            self.father = ""
            self.preg_father_class = nosex
            self.preg_quest_class = nosex
            self.remove_perk_pregnancy()
            self.preg_desire = 0
            if self._fitness <= 20:
                
                self.pregnancy = 1 
            else:
                
                self.pregnancy = 0
            
            self.reset_baby_status()
            self.add_perk(perk_recovering, days=numgen(2, 7))
            self.cycle_conditions["stage"] = "no_cycle"
            self._desire = 0
            self._mood = 20 
            self._tired = 20 
            self.reset_pregnancy() 
            self.face_normal() 
            if self.vvirgin == True:
                self.vvirgin = False
                self.firstvsex = "I managed to get pregnant and gave birth to a child without ever having a man inside me. Giving birth no doubt destroyed my hymen so I can't really call myself a virgin anymore."
        
        def preg_abortion(self):
            diary_preg_abort_func() 
            self.pregnant = 0
            self.father = ""
            self.preg_father_class = nosex
            self.preg_quest_class = nosex
            self.add_preg_desire(-300)
            
            self.add_perk(perk_preg_notwant)
            self.remove_perk_pregnancy()
            if self._fitness <= 20:
                
                self.pregnancy = 1 
            else:
                
                self.pregnancy = 0
            
            self.reset_baby_status()
            self.add_perk(perk_recovering, days=numgen(1, 3))
            
            self.cycle_conditions["stage"] = "no_cycle"
            self._desire = 0
            self._mood = 20 
            self._tired = 20 
            self.reset_pregnancy() 
            self.face_normal() 
        
        def preg_morningafter_pill(self):
            chance = 100 - (self.last_cumin * 20)
            self.add_perk(perk_map, hours=6) 
            if numgen(0, 100) <= chance:
                if self.pregnant and self.days_pregnant < 5:
                    self.remove_perk_pregnancy()
                    self.pregnant = 0
                    self.father = ""
                    self.preg_father_class = nosex
                    self.preg_quest_class = nosex
                    self.reset_baby_status()
                    self.reset_pregnancy() 
                    self.face_normal() 
            self.add_mood(-15)
            self.add_conf(-2)
            self.add_preg_desire(-30)
        
        def preg_day(self):
            global global_pregnancy_length
            if self.pregnant > 0:
                self.days_pregnant += 1
                
                if self.days_pregnant > global_pregnancy_length and self.pregnant < 2:
                    self.pregnant = 2
                
                elif self.pregnancy == 3 and not self.has_perk(perk_pregnant_3):
                    self.remove_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_2])
                    self.add_perk(perk_pregnant_3)
                    self.add_perk(perk_lactating)
                    perk_lactating_buildup()
                elif self.pregnancy == 2 and not self.has_perk(perk_pregnant_2):
                    self.remove_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_3])
                    self.add_perk(perk_pregnant_2)
                    self.preg_test()
                elif self.pregnancy == 1 and not self.has_perk(perk_pregnant_1):
                    if self.preg_knows:
                        self.add_perk(perk_pregnant_1)
                    self.remove_perk(perk_pregnant_0)
                elif self.pregnancy == 0 and self.preg_knows and not self.has_perk(perk_pregnant_0):
                    self.remove_perk([perk_pregnant_1, perk_pregnant_2, perk_pregnant_3])
                    self.add_perk(perk_pregnant_0)
            else:
                self.remove_perk_pregnancy()
        
        
        
        def add_preg_desire(self, amount):
            self.preg_desire += amount
            self.check_preg_desire()
        
        def check_preg_desire(self):
            total_amount = self.preg_desire
            if self.preg_knows:
                self.remove_perk(perk_preg_notwant)
                self.remove_perk(perk_preg_want)
                self.preg_desire = 0
                
                
                
                return
            
            if writing.belly:
                total_amount += 50
            
            
            if self.preg_desire > 100:
                self.preg_desire = 100
            elif self.preg_desire < -100:
                self.preg_desire = -100
        
        
        
        
        
        
        
        
        
        
        
        
        
        def reset_pregnancy(self):
            self.days_pregnant = 0
        
        def having_sex_time(self):
            
            
            desire_amount = 4
            if self.selling:
                if self.has_perk(perk_whore):
                    desire_amount = desire_amount * 0.5
                else:
                    desire_amount = desire_amount * 0.1
            if self.has_perk(perk_slut):
                desire_amount = desire_amount * 2
            if not self.beingraped:
                self.add_desire_random(desire_amount)
                if weightgen(clamp((self.desire - 200), 0, 1000), 1000):
                    player.sex_cum(nosex, during_dia=True)
                    if not self.gagged:
                        renpy.say(pcc, rlist.having_sex_cum_dialogue)
        
        
        
        def reset_sex_status(self, arrival=False): 
            
            
            if not (self.sex_man_amount or self.sex_holes):
                if arrival:
                    
                    self.beingraped = False 
                    self.selling = False
                    self.soldprice = 0
                    self.sexlocation = 0
                    self.soldrequest = ""
                self.having_sex = False
                self.want_pullout = True
                self.have_pullout = True
                if self.vvirgin == False and self.virgin_pregcheck == True:
                    self.virgin_pregcheck = False
                self.sex_perk_calculate()
        
        def reset_baby_status(self):
            self.rapebaby = False
            self.soldbaby = False
            self.virginbaby = False
        
        def sex_perk_calculate(self):
            self.sex_isslut_calculate()
            self.sex_virgin_perk_check()
            if self.asex > 5 and self.asex > (self.vsex * 2) and not self.has_perk(perk_buttslut):
                self.add_perk(perk_buttslut)
            elif not (self.asex > 5 and self.asex > (self.vsex * 2)) and self.has_perk(perk_buttslut):
                self.remove_perk(perk_buttslut)
        
        
        
        
        
        
        def cycle(self): 
            stage = self.cycle_conditions["stage"]
            self.cycle_conditions["count_stage"] += 1
            
            if self.cycle_conditions["count_stage"] >= self.cycle_conditions["length_" + stage]:
                self.cycle_set_stage()
            randomnum = renpy.random.randint(1, 50)
        
        def cycle_days_left(self):
            return self.cycle_conditions["length_" + self.cycle_conditions["stage"]] - self.cycle_conditions["count_stage"] 
        
        def cycle_gamestart_randomiser(self):
            for _ in range(numgen(20,50)):
                self.cycle()
        
        def cycle_set_stage(self):
            if self.preg_knows:
                return
            
            self.cycle_conditions["count_stage"] = 0
            
            if self.cycle_conditions["stage"] == "no_cycle":
                self.cycle_conditions["stage"] = "mens"
                self.pregpills = False
                self.add_perk(perk_period)
            elif self.cycle_conditions["stage"] == "mens":
                self.cycle_conditions["stage"] = "foll"
                if self.has_perk(perk_period_late):
                    self.preg_test()
                self.remove_perk([perk_period, perk_period_late])
            
            elif self.cycle_conditions["stage"] == "foll":
                self.cycle_conditions["stage"] = "ovulate"
                if not player.has_perk([perk_pregnant_0, perk_pregnant_1, perk_pregnant_2, perk_pregnant_3]):
                    self.add_perk(perk_ovulating)
            elif self.cycle_conditions["stage"] == "ovulate":
                self.cycle_conditions["stage"] = "lut"
                self.remove_perk(perk_ovulating)
            elif self.cycle_conditions["stage"] == "lut":
                self.cycle_conditions["stage"] = "mens"
                self.pregpills = False
                if self.pregnant:
                    self.add_perk(perk_period_late)
                else:
                    self.add_perk(perk_period)
            return self.cycle_conditions["stage"]
        
        def cycle_get_fertility(self):
            fertility = self.cycle_conditions["chance_base"]
            for i in self.perk_list:
                if i.fertility_multi:
                    fertility = fertility * i.fertility_multi
            return fertility
        
        
        
        
        
        
        def spank(self,x=0.05,y=0.7,z=0.4):
            bruise.bruise_ass()
            renpy.show_screen("spank_bum", x,y,z)
            renpy.transition(vpunch)
            
            if not self.beingraped:
                self.add_desire(8)
                if self._desire >= 200:
                    self.face_orgasm()
                else:
                    self.face_surprised()
                renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_shock, how="burst")
            else:
                self.face_pain()
                renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_negative, how="burst")
            return
        
        def punch(self, ko=False):
            if self.isbroken:
                self.add_desire(100)
            else:
                self.add_mood(-60)
                self.add_conf(-4)
            self.add_tired(-numgen(10,25))
            renpy.transition(hpunch)
            randomnum = renpy.random.randint(1, 3)
            if randomnum == 1:
                renpy.show_screen("punch",0.15,0.3)
                bruise.harm("face", numgen(1,3))
                blood.face = 5
            elif randomnum == 2:
                renpy.show_screen("punch",0.18,0.45)
                bruise.harm("chest", numgen(1,3))
            elif randomnum == 3:
                renpy.show_screen("punch",0.15,0.6)
                bruise.harm("belly", numgen(1,3))
            player.face_pain()
            renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_pain, how="burst")
            refresh_avatar()
            if sum([bruise.face, bruise.chest, bruise.belly]) >= 12 and player.tired <= 10 and numgen() and ko:
                renpy.jump("action_beaten_start")
        
        
        def punch_face(self):
            renpy.transition(hpunch)
            renpy.show_screen("punch",0.15,0.3)
            bruise.harm("face", numgen(1,3))
            blood.face = 5
            player.face_pain()
            refresh_avatar()
        
        def grope(self, hands=True, steal=False, strip=False, trans=None):
            global grope_penisinside, grope_penispoke
            if trans == None:
                trans = grope_trans
            if hands:
                num = numgen(1,3)
                if num == 1:
                    self.grope_breasts(steal, strip, trans)
                elif num == 2:
                    self.grope_hips(steal, strip, trans)
                else:
                    if any([grope_penisinside, grope_penispoke]):  
                        self.grope_hips(steal, strip, trans)
                    else:
                        self.grope_ass(steal, strip, trans)
            else:
                self.grope_react()
                renpy.transition(trans)
        
        def milk(self, amount=1):
            perk_lactating_milk(amount)
        
        def grope_react(self):
            if self.check_sex_agree(5, notif=False) and not self.beingraped:
                self.add_desire_random(10)
                self.eye = 6
                self.mouth = 1  
                renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_accept, how="say")
            
            else:
                if not self.beingraped:
                    self.add_desire_random(5)
                    renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_suprise, how="say")
                else:
                    renpy.show_screen("text_char_speak", text=rlist.avatar_react_exclaim_negative, how="say")
                
                self.face_shock()
        
        def grope_breasts(self, steal=False, strip=False, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.grope_react()
            if trans == None:
                trans = grope_trans
            grope_ass = False
            grope_hips = False 
            if numgen(0,1):
                grope_breasts1 = False
                grope_breasts2 = True
            else:
                grope_breasts2 = False
                grope_breasts1 = True
            if (steal and not numgen(0, 30)) or strip:
                self.grope_strip_upper(steal)
            self.grope_breasts_popup_func()
            self.milk()
            renpy.transition(trans)
        
        def grope_hips(self, steal=False, strip=False, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.grope_react()
            if trans == None:
                trans = grope_trans 
            grope_ass = False
            grope_breasts1 = False 
            grope_breasts2 = False
            grope_hips = True
            if (steal and not numgen(0, 30)) or strip:
                self.grope_strip(steal)
            self.grope_hips_popup_func()
            renpy.transition(trans)
        
        def grope_ass(self,steal=False, strip=False, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.grope_react()
            if trans == None:
                trans = grope_trans
            bruise.ass += 0.1
            grope_ass = True
            grope_breasts1 = False 
            grope_breasts2 = False
            grope_hips = False
            if (steal and not numgen(0, 30)) or strip:
                self.grope_strip_lower(steal)
            self.grope_hips_popup_func()
            renpy.transition(trans)
        
        def grope_poke(self, steal=False, strip=False, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass, grope_penisinside, grope_penispoke
            self.grope_react()
            if trans == None:
                trans = grope_trans
            if not any([grope_breasts1, grope_breasts2, grope_hips]):
                grope_hips = True
            grope_ass = False
            grope_penisinside = False
            grope_penispoke = True
            if (steal and not numgen(0, 30)) or strip:
                self.grope_strip_lower(steal)
            self.grope_hips_popup_func()
            renpy.transition(trans)
        
        def grope_insert(self, steal=False, strip=False, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass, grope_penisinside, grope_penispoke
            self.grope_react()
            if trans == None:
                trans = grope_trans
            if not any([grope_breasts1, grope_breasts2, grope_hips]):
                grope_hips = True
            grope_ass = False
            grope_penisinside = True
            grope_penispoke = False
            if (steal and not numgen(0, 30)) or strip:
                self.grope_strip_lower(steal)
            self.grope_hips_popup_func()
            renpy.transition(trans)
        
        def grope_end(self, trans=None):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass, grope_penispoke, grope_penisinside, grope_mastleft, grope_mastright
            grope_breasts1 = False
            grope_breasts2 = False
            grope_hips = False
            grope_ass = False
            grope_penispoke = False
            grope_penisinside = False
            grope_mastleft = False
            grope_mastright = False
            renpy.with_statement(trans)
        
        def grope_breasts_popup_func(self):
            if renpy.showing("grope_popup_breasts_1") and not renpy.showing("grope_popup_breasts_2"):
                renpy.show_screen("grope_popup_breasts_2")
            elif renpy.showing("grope_popup_breasts_2") and not renpy.showing("grope_popup_breasts_1"):
                renpy.show_screen("grope_popup_breasts_1")
            else:
                renpy.show_screen(random(["grope_popup_breasts_1", "grope_popup_breasts_2"]))
        
        def grope_hips_popup_func(self):
            
            
            
            
            
            
            renpy.show_screen("grope_popup_hips_1")
        
        def mug(self, bully=False):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            if not numgen(0,10):
                self.grope_end()
                self.punch()
            num = numgen(1,3)
            if num == 1:
                self.mug_breasts()
            elif num == 2:
                self.mug_hips()
            else:
                if any([grope_penisinside, grope_penispoke]):
                    self.mug_hips()
                else:
                    self.mug_ass()
            
            if numgen() and self.cash > 10: 
                self.remove_money(10)
            if not numgen(0, 10) and inv.qty(item_beer):
                inv.drop(item_beer)
            if not numgen(0, 10) and inv.qty(item_cigs):
                inv.drop(item_cigs, numgen(5,20))
            if bully and inv.qty(item_beer_poison):
                shane.inv.take(item_beer_poison, inv.qty(item_beer_poison))
                inv.drop(item_beer_poison, 10)
            else:
                self.add_mood(-5)
        
        def mug_breasts(self):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.face_shock()
            
            grope_ass = False
            grope_hips = False 
            if numgen(0,1):
                grope_breasts1 = False
                grope_breasts2 = True
            else:
                grope_breasts2 = False
                grope_breasts1 = True
            
            if not numgen(0, 5):
                self.grope_strip_upper(steal=True)
            renpy.transition(grope_trans)
        
        def mug_hips(self, steal=False):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.face_shock()
            
            grope_ass = False
            grope_breasts1 = False 
            grope_breasts2 = False
            grope_hips = True
            
            if not numgen(0, 5):
                self.grope_strip(steal=True)
            renpy.transition(grope_trans)
        
        def mug_ass(self):
            global grope_breasts1, grope_breasts2, grope_hips, grope_ass
            self.face_shock()
            bruise.ass += 0.1
            grope_ass = True
            grope_breasts1 = False 
            grope_breasts2 = False
            grope_hips = False
            if not numgen(0, 5):
                self.grope_strip_lower(steal=True)
            renpy.transition(grope_trans)
        
        def grope_strip(self, steal=False):
            if numgen():
                self.grope_strip_upper(steal)
            else:
                self.grope_strip_lower(steal)
        
        def grope_strip_upper(self, steal=False):
            if not steal:
                pc_set_temp_outfit()
            if c.coat:
                c.coat = 0
            elif c.top or c.outfit:
                c.top, c.outfit = 0, 0
            elif c.bra or c.bsuit:
                c.bra, c.bsuit = 0, 0
            else:
                pc_strip_upper()
        
        def grope_strip_lower(self, steal=False):
            if not steal:
                pc_set_temp_outfit()
            if c.skirt and c.pants:
                c.pants = 0
            elif c.bottom or c.outfit:
                c.bottom, c.outfit = 0, 0
            elif c.pants or c.bsuit:
                c.pants, c.bsuit = 0, 0
            else:
                pc_strip_lower()
        
        
        
        
        
        def masturbate(self, open=False):
            if open:
                self.eye = 2
            else:
                self.eye = 3
            self.brow = 3
            self.mouth = 4
            self.force_cover_vag = True
        
        def masturbate_cum(self):
            self.face_orgasm()
            self.force_cover_vag = True
            self.sex_cum(nosex, "self")
        
        def masturbate_end(self):
            self.face_shy()
            self.hands_reset()
        
        
        
        
        
        
        def set_hair(self, hair="auto", fringe=True):
            if hair and not hair in ("none","auto"):
                self.hair_style = hair
            elif self.hair_style == "haven":
                pass
            elif "sport" in tab_top:
                self.hair_style = "pony"
            elif "swim" in tab_top or "work" in tab_top:
                self.hair_style = "bun"
            elif "home" in tab_top:
                self.hair_style = "loose"
            else:
                self.hair_style = self.hair_style_default
            
            if fringe:
                self.hair_fringe = self.hair_fringe_default
            else:
                self.hair_fringe = 0
            refresh_avatar()
        
        
        
        
        def stat_popup_screen(self, message=""):
            if not message == "" or not renpy.get_screen("choice"):
                show_notif_popup(message)
        
        
        def check_vag_agree(self, notif=True):
            if writing.pubic:
                return True
            if self.has_perk(perk_preg_notwant) and not (self.cycle_conditions["stage"] == "mens" and self.check_sex_agree(4, notif=False)): 
                return False
            elif self.cycle_conditions["stage"] == "ovulate" and not self.check_sex_agree(2, notif=False): 
                return False
            else:
                return True
        
        def check_anal_agree(self, notif=True):
            if acc.anus:
                
                return False
            elif writing.anus or self.has_perk(perk_period, wildcard=False): 
                return True
            elif (self.has_perk(perk_preg_want) or self.has_perk(perk_broodmother, wildcard=False)) and not (self.has_perk(perk_period, wildcard=False) or self.preg_knows): 
                return False
            elif self.vvirgin: 
                return True
            elif self.asex <= 5 and not self.check_sex_agree(3, notif=False): 
                return False
            else:
                return True
        
        
        
        
        
        
        
        
        
        def check_pullout_agree(self): 
            if writing.pubic or writing.belly:
                return False
            randomnum = renpy.random.randint(0, 60)
            base = (((self._int + self._fitness + self._confidence) * 2 ) + randomnum) - (self._desire + self.drunk) - 30 
            
            
            if base >= 40:
                return True
            else:
                return False
        
        def check_pullout(self): 
            if writing.pubic or player.has_perk(perk_creampie_lover) or self.has_perk(perk_preg_want) or self.has_perk(perk_sucu):
                return False
            if self.has_perk(perk_preg_notwant):
                return True
            else:
                total = (self.drunk / 3 + self.desire / 10 + self.preg_desire / 2) - (self.confidence + self.int * 2)
                randomnum = renpy.random.randint(0, 100)
                if total > randomnum:
                    return False
                else:
                    return True
        
        def check_whore(self, notif=True, vag_sex=True): 
            if self.has_perk(perk_freeuse):
                if notif:
                    show_notif_popup("I am free use")
                return True
            elif self.has_perk(perk_sucu):
                if notif:
                    show_notif_popup("Succubus")
                return True
            elif self.has_perk(perk_deadinside):
                if notif:
                    show_notif_popup("It might make me feel alive")
                return True
            elif self.iswhore or self.isbroken:
                if self.iswhore and notif:
                    show_notif_popup("I am a whore")
                elif notif:
                    show_notif_popup("I never refuse")
                return True
            
            result = False
            
            if vag_sex:
                if not (self.soldrequest == "vag" or self.soldrequest == "creampie" or self.soldrequest == ""):
                    vag_sex = False
            
            if (self.vvirgin and vag_sex) or self.recovering:
                if self.check_poor(notif=False) and self.check_sex_agree(2, notif=False) and self.soldrequest == "nosex":
                    show_notif_popup("It's not like we want's anythin naughty")
                    return True
                elif self.check_poor(notif=False) and self.check_sex_agree(4, notif=False):  
                    show_notif_popup("I don't want to, but I need money")
                    return True
                elif self.vvirgin and vag_sex:
                    show_notif_popup("I won't sell my virginity")
                    return False
                else:
                    show_notif_popup("I am still suffering from what happened before") 
                    return False
            
            amount = (((self.vsex + self.asex) + (self.sold * 10) + (If(self.check_poor(notif=False), 20, 0)) + (If(self.isslut, 40, 0)) + self._drunk + self._confidence + self.desire) / 4 + If(self.is_working(), 30, 0))  - If(self.vvirgin,50,0)
            randomnum = renpy.random.randint(0, 100)
            
            if amount > randomnum:
                if self.is_working(True):
                    show_notif_popup("This job kind of expects it")
                else:
                    show_notif_popup("Agreed to be a whore")
                return True
            
            elif self.has_perk([perk_preg_want, perk_broodmother]):
                show_notif_popup("I don't want to, but this could give me a baby")
                return True
            
            elif self.check_poor(notif=False) and player.check_sex_agree(4, notif=False):  
                show_notif_popup("I don't want to, but I need money")
                return True
            
            else:
                show_notif_popup("Refused to be a whore")
                return False
        
        def set_whore_price(self, diff=0, inv=False):
            bonus = diff * 35
            bonusrandom = numgen(0,50)
            base = ((bonus + bonusrandom + (self._allure / 4) + (self._fitness / 2) + (self._confidence ) + (self._mood / 4)) - ((self._drunk / 2) + (100 - self._int))) / 2
            totalamount = round_num(base)
            if totalamount <= 0:
                totalamount = 10
            if inv:
                payment_inv = Inventory()
                payment_inv.add_inv_to_value(totalamount)
                self._soldprice = payment_inv
            else:
                self.soldprice = totalamount
            return totalamount 
        
        def check_poor(self, notif=True):
            
            if self.cash <= 300:
                if notif:
                    show_notif_popup("I am dead broke")
                return True
            else:
                return False
        
        def check_sell_clothes(self, what, block_broken=True):
            if what in ("hat", "socks", "gloves", "coat"):
                
                renpy.say(pcmc, "No harm in selling is there? Not like I am left exposed or anything.")
                return True
            else:
                if self.has_perk(perk_exhibitionist, notif=True):
                    return True
                elif what in ["top", "outfit", "bottom"]:
                    renpy.say(pcmc, "If I sell, I'm going to be left exposed...")
                elif what == "pants" and c.skirt:
                    renpy.say(pcmc, "Selling my pants while wearing this skirt is going to leave my arse flapping in the wind...")
                elif what == "pants" and not c.bottom:
                    renpy.say(pcmc, "Selling my pants is going to leave my arse totally exposed...")
                    return False
                elif what == "bra" and not c.top:
                    renpy.say(pcmc, "Selling my bra is going to leave me with my tits out...")
                    return False
                else:
                    renpy.say(pcmc, "Hmmm, won't do any harm will it?")
                if self.check_poor() or not self.check_nowill():
                    return True
        
        
        def check_drunk(self,diff, notif=True): 
            if diff == 1:
                randomnum = renpy.random.randint(20, 100) 
            elif diff == 2:
                randomnum = renpy.random.randint(40, 100) 
            elif diff == 3:
                randomnum = renpy.random.randint(60, 100) 
            elif diff >= 4:
                randomnum = renpy.random.randint(80, 100) 
            
            if self._drunk > randomnum:
                if notif and diff >= 3:
                    show_notif_popup("Totally wasted drunk")
                return True
            else:
                return False
        
        def check_victim(self, notif=True):
            victim_points = 0
            for i in self.perk_list:
                if i.victim:
                    victim_points += 5
                elif i.not_victim:
                    victim_points -= 5
            if victim_points >= 0:
                result = weightgen(victim_points, 200)
                if result and notif:
                    self.stat_popup_screen("Easy target")
                return result
            
            else:
                return False
        
        def check_nowill(self, notif=True, block_face=False, block_broken=False, drink_related=False): 
            result = False
            
            
            
            if drink_related:
                if self.has_perk(perk_alcoholic):
                    if notif:
                        self.stat_popup_screen("I wont turn down booze")
                    return True
                elif player.has_perk(perk_deadinside):
                    if notif:
                        self.stat_popup_screen("It might make me feel alive")
                    return True
                elif player.drunk >= 90:
                    if notif:
                        self.stat_popup_screen("More booze!")
                    return True
            
            
            
            elif self.isbroken:
                if block_broken:
                    result = False 
                else: 
                    result = True
            elif self.confidence >= 40:
                result = False
            elif self.confidence < 20:
                result = True
            else:
                will = (self.confidence - 20)
                if self.drunk:
                    
                    
                    if drink_related:
                        will -= (self._drunk / 5)
                    else:
                        will += (self._drunk / 10)
                
                will += ((self.mood / 10) - 4) 
                will += ((self.tired / 10) - 4) 
                if player.has_perk([perk_recovering]):
                    will -= 2
                
                if will < numgen(0,20):
                    result = True
                else:
                    result = False
            
            if result == False:
                if notif:
                    self.stat_popup_screen("You have the willpower")
                return result
            else:
                if notif:
                    self.stat_popup_screen("No willpower")
                if not block_face:
                    self.face_meek()
                return result
        
        def check_sex_agree_blocker(self, value):
            if self.has_perk([perk_meek, perk_bambi, perk_male]):
                if ((t.day + 14) / 7) < value:
                    
                    return True
            return False
        
        def check_sex_agree(self, diff=3, notif=True, exhibitionist=False):
            if player.has_perk(perk_freeuse):
                if notif:
                    self.stat_popup_screen("I am free use")
                return True
            if exhibitionist and player.has_perk(perk_exhibitionist):
                if notif:
                    self.stat_popup_screen("Exhibitionist")
                return True
            if player.has_perk(perk_sucu):
                if notif:
                    self.stat_popup_screen("Succubus")
                return True
            if player.has_perk(perk_deadinside):
                if notif:
                    self.stat_popup_screen("It might make me feel alive")
                return True
            if player.has_perk(perk_despondent):
                if notif:
                    self.stat_popup_screen("Anything to cheer me up")
                return True
            
            
            
            
            
            if diff == 0:
                randomnum = renpy.random.randint(0, 40) 
            if diff == 1:
                randomnum = renpy.random.randint(0, 70) 
            elif diff == 2:
                randomnum = renpy.random.randint(0, 101) 
            elif diff == 3:
                randomnum = renpy.random.randint(0, 170) 
            elif diff == 4:
                randomnum = renpy.random.randint(0, 230) 
            elif diff >= 5:
                randomnum = renpy.random.randint(0, 300) 
            
            amount = (self.desire + self.drunk + self.confidence + (self.vsex + self.asex) + ((self.hsex + self.osex) / 2) + (If(self.has_perk(perk_slut), 60,0)) + (If(self.has_perk(perk_whore), 20,0)) + (If(self.has_perk(perk_bimbo), 30,0))) + (If(self.isbroken, 100,0)) - ((If(self.vvirgin, If(self.asex,40,100),0)) + (If(self.recovering, 150,0)))
            if writing.chest:
                amount += 30
            if c.slutty or c.exposed:
                amount += 30
            elif self.allure > 130:
                amount += 15
            if player.has_perk(perk_broodmother, wildcard=False) and not player.has_perk(perk_period, wildcard=False):
                if player.has_perk(perk_ovulating, wildcard=False):
                    amount += 100
                else:
                    amount += 30
            
            if amount >= randomnum:
                if notif:
                    self.stat_popup_screen("Accepted sexual advances")
                return True
            else:
                if notif:
                    self.stat_popup_screen("Rejected sexual advances")
                return False
        
        def check_sex_agree_choice(self, diff=3, option1="" ,option2="",notif=True, block_drunk=False,block_horny=False, block_broken=False,block_nowill=True, exhibitionist=False):
            if self.check_sex_agree(diff, notif=False, exhibitionist=exhibitionist):
                if option1 == "":  
                    option1 = "Agree" 
                if option2 == "":
                    option2 = "Refuse"
                if player.has_perk(perk_freeuse):
                    if notif:
                        self.stat_popup_screen("I am free use")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                
                
                
                
                
                
                if player.has_perk(perk_despondent):
                    if notif:
                        self.stat_popup_screen("Anything to cheer me up")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                if self.isbroken and not block_broken and self.check_nowill():
                    if notif:
                        self.stat_popup_screen("Too broken to refuse")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                elif self.gagged:
                    if notif:
                        self.stat_popup_screen("Gagged and can't refuse")  
                    
                    return True
                elif exhibitionist and self.has_perk(perk_exhibitionist):
                    if notif:
                        self.stat_popup_screen("Exhibitionist")
                    if not self.gagged:    
                        renpy.say(pcc,option1)
                    return True
                elif self.check_drunk(5) and not block_drunk:
                    if notif:
                        self.stat_popup_screen("Too drunk to care")
                    if not self.gagged:    
                        renpy.say(pcc,option1)
                    return True
                elif self.check_horny(extreme=True) and not block_horny:
                    if notif:
                        self.stat_popup_screen("Too horny to care")
                    if not self.gagged:    
                        renpy.say(pcc,option1)
                    return True
                elif self.check_nowill(notif=False) and not block_nowill:
                    if notif:
                        self.stat_popup_screen("No will to resist")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                else:
                    _window_hide(auto=True)
                    result = renpy.display_menu([(option1, True),(option2, False)])
                    
                    
                    
                    
                    
                    return result
            else:
                if notif or diff == 0:
                    self.stat_popup_screen("Sex check failed")
                
                return False
        
        def check_whore_agree_choice(self, option1="" ,option2="", request=0, notif=True, exhibitionist=False, block_broken=False):
            if not self.soldprice:
                self.set_whore_price(1)
            if option1 == "":
                option1 = "Sure, okay." 
            if self.has_perk(perk_broken):
                option1 = "If you say so..."
            if option2 == "":
                option2 = "No, I don't think so."
            
            if request:
                self.soldrequest = request
            
            if not self.check_whore():
                if not self.gagged:
                    renpy.say(pcc,option2)
                return False
            else:
                if self.gagged:
                    if notif:
                        self.stat_popup_screen("Gagged and can't refuse")  
                    
                    return True
                elif self.isbroken and not block_broken and self.check_nowill():
                    if notif:
                        self.stat_popup_screen("Too broken to refuse")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                elif player.has_perk(perk_freeuse):
                    if notif:
                        self.stat_popup_screen("I am free use")
                    if not self.gagged:
                        renpy.say(pcc,"Sure, but I won't take your money.")
                    else:
                        renpy.say(None, "I make gestures to refuse the money.")
                    self.soldprice = 0
                    return True
                elif player.has_perk(perk_sucu) and player.tired < 20:
                    if notif:
                        self.stat_popup_screen("Tired with sleeplessness")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                
                elif exhibitionist and self.has_perk(perk_exhibitionist):
                    if notif:
                        self.stat_popup_screen("Exhibitionist")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                elif self.check_drunk(5) and self.check_horny(extreme=True):
                    if notif:
                        self.stat_popup_screen("Too drunk and horny")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                if player.has_perk(perk_despondent):
                    if notif:
                        self.stat_popup_screen("Anything to cheer me up")
                    if not self.gagged:
                        renpy.say(pcc,option1)
                    return True
                
                else:
                    _window_hide(auto=True)
                    result = renpy.display_menu([(option1, True),(option2, False)])
                    return result
        
        def check_int(self,diff=2, notif=True):
            base = diff * 16
            int_total = self.int - (self.drunk / 3)
            if weightgen(int_total, base):
                if notif:
                    self.stat_popup_screen("Intelligence check passed")
                return True
            else:
                if notif:
                    self.stat_popup_screen("Intelligence check failed")
                return False
        
        def check_speech(self,diff=2, notif=True):
            base = diff * 16
            speech_total = ((self.int + self.confidence) / 2) - (self.drunk / 3)
            if weightgen(speech_total, base):
                if notif:
                    self.stat_popup_screen("Speech check passed")
                return True
            else:
                if notif:
                    self.stat_popup_screen("Speech check failed")
                return False
        
        def check_strength(self, diff=3, notif=True):
            
            
            
            if diff == 1:
                randomnum = renpy.random.randint(0, 30) 
            elif diff == 2:
                randomnum = renpy.random.randint(0, 50) 
            elif diff == 3:
                randomnum = renpy.random.randint(30, 70) 
            elif diff == 4:
                randomnum = renpy.random.randint(60, 100) 
            elif diff == 5:
                randomnum = renpy.random.randint(100, 130) 
            
            base = (self._fitness + (self._confidence / 2)) - ((self._drunk / 2))
            if base > randomnum:
                if notif:
                    self.stat_popup_screen("I am strong enough")
                return True
            else:
                if notif:
                    self.stat_popup_screen("Not strong enough")
                return False
        
        def check_fight(self, diff=3, notif=True, can_spray=True):
            global danger_content
            if not danger_content:
                self.stat_popup_screen("Fight won")
                return True
            if self.soldrequest == "forced" and self.selling:
                if notif:
                    self.stat_popup_screen("Pretending to fight back")
                return False
            if self.has_perk([perk_despondent, perk_deadinside]):
                if notif:
                    self.stat_popup_screen("I don't care enough to fight back")
                return False
            if can_spray:
                
                npc_rescue()
            
            if self.has_perk(perk_freeuse):
                if notif:
                    self.stat_popup_screen("I am free use")
                return False
            if self.check_nowill(notif=False):
                if notif:
                    if self.has_perk(perk_broken):
                        self.stat_popup_screen("Too broken to resist")
                    else:
                        self.stat_popup_screen("Too scared to fight back")
                return False
            
            result = None
            if inv.qty(item_pepperspray) and can_spray:
                
                
                _window_hide(auto=True)
                if self.has_perk([perk_sucu, perk_broken, perk_meek, perk_broken_virgin, perk_freeuse]):
                    result = renpy.display_menu([("Use pepper spray", True),("Fight him off", False), ("Don't resist", "agree")])
                else:
                    result = renpy.display_menu([("Use pepper spray", True),("Fight him off", False)])
                if result == True:
                    inv.use(item_pepperspray)  
                    return True
            
            elif self.has_perk([perk_sucu, perk_broken, perk_broken_virgin, perk_freeuse]):
                result = renpy.display_menu([("Fight him off", False), ("Don't resist", "agree")])
            
            if result == "agree":
                if notif:
                    self.stat_popup_screen("Not resisting")
                return False
            
            if diff == 1:
                randomnum = renpy.random.randint(0, 30) 
            elif diff == 2:
                randomnum = renpy.random.randint(0, 50) 
            elif diff == 3:
                randomnum = renpy.random.randint(30, 70) 
            elif diff == 4:
                randomnum = renpy.random.randint(60, 100) 
            elif diff == 5:
                randomnum = renpy.random.randint(100, 130) 
            
            base = (self._fitness + (self._confidence / 2)) - ((self._drunk / 2) + (If(self.has_perk([perk_broken, perk_bambi]), 40,0)))
            if base > randomnum:
                if notif:
                    self.stat_popup_screen("Fight won")
                return True
            else:
                if notif:
                    self.stat_popup_screen("Not strong enough")
                return False
        
        def check_horny(self, extreme=False, very_extreme=False):
            base = 150
            if very_extreme:
                base = 1500
            elif extreme:
                base = 600
            if (self.desire + (self.drunk / 4) + If(player.has_perk(perk_lebo), 800, 0)) > base:
                return (self.desire - base) + (player.drunk / 4) + If(player.has_perk(perk_lebo), 800, 0)
            else:
                return 0
        
        def check_clothes(self):
            counter = 0
            if self.iswhore or self.isslut or self.isbroken:
                return
            else:
                
                if (self.allure > 100 or (c.clevage and not c.bra) or (c.skirt and c.thong)) and not self.check_sex_agree(1, notif=False):
                    counter += 1
                if (c.skirt and not c.pants) and self.check_sex_agree(2, notif=False):
                    counter += 1
                if (c.slutty or c.underwear or c.cansee_bra or c.cansee_pants or c.cansee_ass) and not self.check_sex_agree(3, notif=False):
                    counter += 1
                if c.cansee_breasts and not self.check_sex_agree(4, notif=False): 
                    counter += 1
                if (c.cansee_vagina or c.nude) and not self.check_sex_agree(5, notif=False):
                    counter += 1
                while counter:
                    counter -= 1
                    self.mood_hit()
                    self.remove_conf_chance()
        
        
        
        
        
        
        
        def can_sport(self, pregnant=False, drunk=False, tired=False, mood=False, rain=False, snow=False, returnto="travel"):
            reason = False
            if not self.can_sport_pregnant(pregnant):
                reason = sport_blocker_pregnant
            elif not self.can_sport_snow(snow):
                reason = sport_blocker_snow
            elif not self.can_sport_rain(rain):
                reason = sport_blocker_rain
            elif not self.can_sport_drunk(drunk):
                reason = sport_blocker_drunk
            elif not self.can_sport_tired(tired):
                reason = sport_blocker_tired
            elif not self.can_sport_mood(mood):
                reason = sport_blocker_mood
            else:
                return
            _window_show(auto=True)
            renpy.say(pcmc,renpy.random.choice(reason))
            if returnto == "return":
                return
            else:
                renpy.jump(returnto)
        
        def can_sport_check(self, pregnant=False, drunk=False, tired=False, mood=False, rain=False, snow=False, returnto="travel"):
            if all ((self.can_sport_pregnant(pregnant), self.can_sport_snow(snow), self.can_sport_rain(rain), self.can_sport_drunk(drunk), self.can_sport_tired(tired), self.can_sport_mood(mood))):
                return True
            else:
                return False
        def can_sport_pregnant(self, pregnant=False):
            if self.pregnancy >= 2 and pregnant == False:
                return False
            else:
                return True
        def can_sport_rain(self,rain=False):
            if weather_var == 3 and rain == False and outside:
                return False
            else:
                return True
        
        def can_sport_snow(self,snow=False):
            if weather_var == 4 and snow == False and outside:
                return False
            else:
                return True
        
        def can_sport_drunk(self,drunk=False):
            if self._drunk >= 70 and drunk == False:
                return False
            else:
                return True
        
        def can_sport_tired(self,tired=False):
            if self._tired < 20 and tired == False:
                return False
            else:
                return True
        def can_sport_mood(self, mood=False): 
            if self._fitness < 35 and self._mood < 20 and mood == False:
                return False
            else:
                return True
        
        
        
        
        
        def add_money(self, amount, notif=True): 
            self.cash += amount
            if notif:
                if amount > 0:
                    self.stat_popup_screen("£" + str(amount) + " added")
                else:
                    self.stat_popup_screen("£" + str(amount) + " spent")
        def remove_money(self, amount, notif=True): 
            self.cash -= amount
            if notif:
                self.stat_popup_screen("£" + str(amount) + " spent")
        
        def add_money_allure(self,amount): 
            randomamount = int(amount / 20)
            randomnum = renpy.random.randint(0, randomamount)
            allure = int(self._allure / 10)
            total = amount + allure + randomamount
            self.cash += total
        def spend(self,amount,notif=True):
            self.remove_money(amount, notif)
        
        def add_money_whore(self, notif=True): 
            if not self.soldprice:
                return
            elif self.has_perk(perk_freeuse):
                renpy.say(pcc, "I do this for free, keep your money.")
                return
            
            if isinstance(self._soldprice, Inventory):
                inv_transfer_to_player(self._soldprice, notif)
            else:
                self.add_money(self.soldprice, notif)
            remove_from_list(quest_whore.list, "should_pay")
        
        
        
        
        def face_normal(self):
            self.drool = 0
            self.cry = 0
            self.rainbow = 0
            self.puke = 0
            self.tear = 0
            
            if self._drunk >= 60:
                self.mouth = 11
            elif self.mood <= 20:
                self.mouth = 12
            elif self.mood >= 100:
                self.mouth = 3
            else:
                self.mouth = 1
            if self.mood <= 20:
                self.brow = 3
                self.tear = 1
            else:
                self.brow = 1
                self.tear = 0
            if self.tired <= 20:
                self.eye = 2
            else:
                self.eye = 1
            
            
            if self.has_perk(perk_despondent):
                self.face_meek()
            elif self.cover_breasts or self.cover_vagina:
                self.face_worried()
        
        
        def face_neutral(self):
            self.rainbow = 0
            self.mouth = 1
            self.brow = 1
            self.eye = 1
            self.tear = 0
        def face_annoyed(self):
            self.rainbow = 0
            self.brow = 1
            self.mouth = 8
            self.eye = 2
        def face_happy(self):
            self.rainbow = 0
            self.eye = 1
            self.mouth = 3
            self.brow = 2
        def face_laugh(self):
            self.rainbow = 0
            self.eye = 1
            self.mouth = 6
            self.brow = 2
        def face_excited(self):
            self.rainbow = 0
            self.brow = 2
            self.mouth = 6
            self.eye = 3
        def face_orgasm(self):
            self.rainbow = 0
            self.brow = 2
            self.mouth = 7
            self.eye = 3
        def face_exercise(self):
            self.rainbow = 0
            self.brow = 2
            if self._fitness < 30:
                self.mouth = 4
            else:
                self.mouth = 2
            if self._fitness < 20:
                self.eye = 2
        def face_sad(self):
            self.rainbow = 0
            self.mouth = 8
            self.brow = 3
            self.eye = 1
        def face_angry(self):
            self.eye = 2
            self.rainbow = 0
            self.mouth = 8
            self.brow = 4
        def face_worried(self):
            self.rainbow = 0
            self.eye = 1
            self.mouth = 8
            self.brow = 3
        def face_cry(self):
            self.rainbow = 0
            self.cry = 1
            self.mouth = 12
            self.brow = 3
            self.eye = 1
        def face_tears(self):
            self.rainbow = 0
            self.tear = 1
            self.mouth = 12
            self.brow = 3
            self.eye = 1
        def face_surprised(self):
            self.rainbow = 0
            self.brow = 2
            self.mouth = 2
            self.eye = 1
        def face_puke(self):
            self.rainbow = 0
            self.brow = 3
            self.eye = 2
            self.mouth = 10
            self.puke = 1
        def face_puke2(self):
            self.brow = 3
            self.eye = 4
            self.mouth = 9
            self.puke = 1
            
            
            self.tear = 1
            self.rainbow = 1
        def face_bleh(self):
            self.brow = 3
            self.eye = 4
            self.mouth = 7
            self.puke = 1
            self.tear = 1
        def face_shame(self):
            self.rainbow = 0
            self.brow = 3
            self.mouth = 9
        def face_shy(self):
            self.rainbow = 0
            self.brow = 3
        def face_pain(self):
            self.rainbow = 0
            self.brow = 4
            self.tear = 1
            self.eye = 2
            self.mouth = 5
        def face_meek(self):
            self.rainbow = 0
            self.eye = 6
            self.mouth = 8
        def face_shock(self):
            self.rainbow = 0
            self.eye = 1
            self.mouth = 9
            self.brow = 3
        def face_wail(self):
            self.rainbow = 0
            self.eye = 3
            self.mouth = 9
            self.brow = 3
            self.cry = 1
        def face_confused(self): 
            self.eye = 1
            self.mouth = 2
            self.brow = 3
            self.rainbow = 0
        def face_conf(self):
            self.face_confused() 
        def face_sleep(self):
            self.eye = 3
            self.mouth = 8
            self.brow = 1
            self.rainbow = 0
        def face_shout(self):
            self.mouth = 4
            self.brow = 4
            self.eye = 3
        def face_mmm(self):
            self.mouth = 1
            self.brow = 3
            self.eye = 3
        def face_frown(self):
            self.brow = 1
            self.eye = 1
            self.mouth = 8
        def face_suspicious(self):
            self.brow = 1
            self.eye = 2
            self.mouth = 8
        def face_sus(self):
            self.face_suspicious()
        def face_evil(self):
            self.brow = 4
            self.eye = 1
            self.mouth = 3
        def face_grit(self):
            self.brow = 4
            self.eye = 2
            self.mouth = 5
        def face_howl(self):
            self.brow = 4
            self.eye = 3
            self.mouth = 4
        def face_tired(self):
            self.eye = 2
            self.mouth = 12
            self.brow = 3
        
        
        def face_icon_desire(self):
            if self.recovering:
                self.face_pain()
            elif self.has_perk(perk_lebo) or self.desire > 600:
                self.face_orgasm()
            elif self.desire < 200:
                self.face_worried()
            else:
                self.face_happy()
        
        def face_icon_allure(self):
            if self.allure == 0:
                self.face_puke()
            elif self.allure < 300:
                self.face_worried()
            else:
                self.face_happy()
        
        def face_icon_tired(self):
            if self.tired < 20:
                self.face_sleep()
            elif self.tired < 40:
                self.face_tired()
            else:
                self.face_happy()
        
        def face_icon_mood(self):
            if self.mood > 100:
                self.face_laugh()
            elif self.mood > 60:
                self.face_happy()
            elif self.mood > 40:
                self.face_neutral()
            elif self.mood > 0:
                self.face_sad()
            else:
                self.eye = 4
                self.mouth = 12
                self.brow = 3
        
        def face_icon_conf(self):
            if self.confidence > 80:
                self.face_laugh()
            elif self.confidence > 60:
                self.face_happy()
            elif self.confidence > 40:
                self.face_neutral()
            elif self.confidence > 0:
                self.face_worried()
            else:
                self.face_shock()
        
        def face_icon_fitness(self):
            if self.pregnant and self.preg_knows:
                if self.has_perk(perk_unwanted_preg):
                    self.face_angry()
                elif self.has_perk(perk_wanted_preg):
                    self.face_happy()
                else:
                    self.face_worried()
            elif self.fitness > 60:
                self.face_happy()
            elif self.fitness > 40:
                self.face_neutral()
            elif self.fitness > 20:
                self.face_worried()
            else:
                self.face_sad()
        
        def face_icon_int(self):
            if self.has_perk([perk_bimbo, perk_princess]):
                self.face_happy()
            elif self.int > 60:
                self.face_happy()
            elif self.int > 40:
                self.face_neutral()
            elif self.int > 20:
                self.face_worried()
            else:
                self.mouth = 9
                self.brow = 3
                self.eye = 2
                self.drool = 1
        
        def face_icon_cycle(self):
            if self.pregnant and self.preg_knows:
                
                self.face_icon_fitness()
            elif self.has_perk(perk_period_late):
                if self.has_perk(perk_preg_want):
                    self.face_happy()
                elif self.has_perk(perk_preg_notwant):
                    self.face_shock()
                else:
                    self.face_worried()
            elif self.has_perk(perk_period):
                self.face_angry()
            elif self.has_perk(perk_ovulating):
                if self.has_perk(perk_preg_want):
                    self.face_happy()
                else:
                    self.face_worried()
            else:
                self.face_normal()
        
        
        
        
        
        def shower(self):
            global shower_warning
            shower_warning = False
            acc.makeup_on = False
            relax(15)
            if self.has_perk(perk_sucu) and not loc_cur == loc_haven_cell:
                self.cum_clean_outside()
            else:
                self.cum_clean()
            self.hygiene = 100
            self.face_normal()
            writing.clean_writing()
            blood.clean()
            refresh_avatar()
        
        def wash(self):
            global shower_warning
            shower_warning = False
            self.cum_clean_outside()
            self.hygiene = max(self.hygiene, 75)
            self.face_normal()
            blood.clean()
            writing.clean_writing()
            refresh_avatar()
        
        def cum_degrade(self):
            for place, value in self.cum_locations.items():
                if value:
                    if place in ("cum_mouth", "cum_assin", "cum_vagin") and self.has_perk(perk_sucu):
                        self.add_tired(20, sucu=True)
                    elif self.has_perk(perk_sucu):
                        self.add_tired(5, sucu=True) 
                    refresh_avatar()
                if value > 0:
                    self.cum_locations[place] -= 1
                if value < 0:
                    self.cum_locations[place] = 0
                if value > 20:
                    self.cum_locations[place] = 20
        
        
        
        
        
        def cum_clean(self):
            for place, value in self.cum_locations.items():
                if value != 0:
                    self.cum_locations[place] = 0
                refresh_avatar()
        
        def cum_clean_outside(self):
            self.cum_locations["cum_mouth"] = 0
            self.cum_locations["cum_face"] = 0
            self.cum_locations["cum_chest"] = 0
            self.cum_locations["cum_belly"] = 0
            self.cum_locations["cum_vagout"] = 0
            self.cum_locations["cum_assout"] = 0
        
        def cum_visible_check(self):
            if any(self.cum_locations.values()):
                if any((self.cum_locations["cum_mouth"], self.cum_locations["cum_face"])):
                    return True
                elif self.cum_locations["cum_chest"] and c.clevage:
                    return True
                elif self.cum_locations["cum_belly"] and c.belly:
                    return True
                elif (self.cum_locations["cum_assout"] or self.cum_locations["cum_vagout"]) and ("swim" in tab_top or (c.bottom == 0 and c.outfit == 0)):
                    return True
                else:
                    return False
            else:
                return False
        
        def cum_any_check(self):
            if any(self.cum_locations.values()):
                return True
            else:
                return False
        
        def cum_amount(self):
            if sum(self.cum_locations.values()):
                return True
            else:
                return False
        
        def is_dirty(self): 
            if any(self.cum_locations.values()) or player.hygiene <= 25:
                return True
            else:
                return False
        
        def looks_dirty(self): 
            if self.cum_visible_check() or player.hygiene <= 25:
                return True
            else:
                return False
        
        
        
        
        
        def makeup_apply(self):
            self.eyeshad_colour = 1
            self.blush_colour = 1
            self.makeup = True
        def makeup_strip(self):
            self.eyeshad_colour = 0
            self.blush_colour = 0
            self.makeup = False
        
        
        
        def diceroll(self, input1, max):
            global temp_var_1
            randomnum = renpy.random.randint(0, max)
            base = input1
            if base > randomnum:
                temp_var_1 = True
            else:
                temp_var_1 = False
        
        
        
        
        
        
        def description(self):
            desc = "I currently look like a short girl with "
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            desc = desc + get_color_name(hair_colours[player.hair_colour]) + " hair, "
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            desc = desc + get_color_name(eye_colours[player.eye_colour]) + " eyes"
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            desc = desc + " and have "
            
            if self.breasts == 1:
                desc = desc + "small, perky breasts"
            elif self.breasts == 2:
                desc = desc + "firm, modest breasts"
            elif self.breasts == 3:
                desc = desc + "massive breasts"
            
            if self.pregnancy == 3:
                desc = desc + " and a huge belly. It is obvious that I am heavily pregnant."
            elif self.pregnancy == 2:
                desc = desc + ". I can no longer hide my large belly and it is obvious I am pregnant."
            elif self.pregnancy == 1:
                if self.preg_knows:
                    desc = desc + " and a belly that is slowly growing, but if I keep it covered it is not obvious I am pregnant."
                else:
                    desc = desc + " and a bit of a belly that should probably be dealt with."
            else:
                if player.fitness > 40:
                    desc = desc + " with a slim waist that has some muscle definition."
                elif player.fitness > 70:
                    desc = desc + " with a slim waist with strong muscle definition."
                else:
                    desc = desc + " with a slim waist."
            
            return desc
        
        def comfort_description(self):
            if self.body_conf < -125:
                desc = "While I was given a new body, it feels totally alien to me. I am struggling to get by in it and can barely tell my body what it should do."
                if player.has_perk(perk_male):
                    desc = desc + " I guess it shouldn't be such a shock though since I used to be a guy. It is going to take some time to get adjusted so things as they are."
            elif self.body_conf < -75:
                desc = "While I was given a new body, it still feels quite odd. I am struggling to get by in it and end up doing the wrong things with it."
                if player.has_perk(perk_male):
                    desc = desc + " I guess it shouldn't be such a shock though since I used to be a guy. It is going to take some time to get adjusted so things as they are."
            elif self.body_conf < -50:
                desc = "I am starting to get adjusted to the new body I was given. Things are still a bit weird but I find myself forgetting that I used to live in a different one."
            elif self.body_conf < 0:
                desc = "While I still make mistakes with my new body now and then, I am starting to get the hang of it. I mostly forget that I used to live my life in a different one."
            else:
                desc = ""
            return desc
        
        def description_sex(self):
            desc = ""
            if writing.face or writing.forehead:
                if writing.face and writing.forehead:
                    desc = "I have a heart on my cheek and \"whore\" written on my forehead. Anyone who sees it will expect that I am a whore who loves being paid to fuck."
                elif writing.face:
                    desc = "I have a heart drawn on my face letting anyone who sees it know that I am a slut."
                elif writing.forehead:
                    desc = "I have the word \"Whore\" written on my forehead so anyone who sees it will think I am up for sale."
            
            elif player.vvirgin:
                if self.isslut and self.iswhore:
                    desc = "I have somehow managed to remain a virgin despite having many encounters with men. I think I am pretty much slutty whore but I won't allow anyone inside my most intimate place."
                elif self.iswhore:
                    desc = "Despite being an experienced whore, I have managed to remain a virgin and keep some semblance of purity."
                elif self.isslut:
                    desc = "I am a massive cock tease. I like to play with men as much as I want, but never give them what they are after. Just getting what I want is enough."
                elif player.avirgin:
                    desc = "I am a virgin and have never had anal sex."
                elif player.asex >= 25:
                    desc = "I am a virgin butt slut who loves to take it in the arse."
                else:
                    desc = "While I have had anal sex, I am still a virgin."
            else:
                if self.isbroken:
                    desc = "People have taken what they want from me so often that I no longer see any value in myself or my body so I have become accustomed to letting people use me as they please."
                elif self.isslut and self.iswhore:
                    desc = "I love sex. I fuck almost anyone for pleasure or money. Usually both."
                elif self.iswhore:
                    desc = "I have become accustomed to selling my body for money to get by in these dark times."
                elif self.isslut:
                    desc = "There is nothing else that can describe me than calling myself a slut. I have as much fun with men as I please."
                else:
                    desc = "I lost my virginity to " + self.firstvsex
                    if player.avirgin:
                        if acc.anus > 0:
                            desc = desc + " I am still an anal virgin if you don't count the plug that's up my bum."
                        else:
                            desc = desc + " I am still an anal virgin."
            if writing.ass:
                if writing.ass_counter == 1:
                    desc = desc + " The tally markers on my ass cheek tells me [writing.ass_counter] person has fucked me since the count started."
                elif writing.ass_counter > 1:
                    desc = desc + " The tally markers on my ass cheek tells me [writing.ass_counter] people have fucked me since the count started."
                else:
                    desc = desc + " I am keeping a tally on my ass cheek counting how many have fucked me today but it is currently zero."
            return desc
        
        def description_period(self):
            desc = ""
            if self.preg_knows == False:
                if self.pregpills:
                    desc = "I am on the pill so I shouldn't be able to get pregnant."
                elif self.cycle_conditions["stage"] == "no_cycle":
                    desc = "My periods have stopped so I won't be able to get pregnant until they start again."
                elif self.cycle_conditions["stage"] == "mens":
                    desc = "This time of the month is around my period, so I probably won't get pregnant."
                elif self.cycle_conditions["stage"] == "ovulate":
                    if self.has_perk(perk_preg_want):
                        desc = "This is the time of my cycle where I am most fertile. Unprotected sex should lead to me getting pregnant."
                    elif self.has_perk(perk_preg_notwant):
                        desc = "This is a very dangerous time in my cycle to be having unprotected sex. If I am not careful I could end up pregnant."
                    else:
                        desc = "This is a fairly dangerous time of my cycle. Unprotected sex could lead to me getting pregnant."
                else:
                    desc = "This is a normal time of my cycle."
            else:
                desc = "I am pregnant so don't have to worry about that time of the month."
            return desc
        
        
        
        def cheat_add_desire(self):
            self._desire += 10
            if self._desire > 100:
                self._desire = 100
        def cheat_remove_desire(self):
            self._desire -= 10
            if self._desire < 0:
                self._desire = 0
        
        def cheat_add_tired(self):
            self._tired += 10
            if self._tired > 100:
                self._tired = 100
        def cheat_remove_tired(self):
            self._tired -= 10
            if self._tired < 0:
                self._tired = 0
        
        def cheat_add_mood(self):
            self._mood += 10
            if self._mood > 100:
                self._mood = 100
        def cheat_remove_mood(self):
            self._mood -= 10
            if self._mood < 0:
                self._mood = 0
        
        def cheat_add_conf(self):
            self._confidence += 10
            if self._confidence > 100:
                self._confidence = 100
        def cheat_remove_conf(self):
            self._confidence -= 10
            if self._confidence < 0:
                self._confidence = 0
        
        def cheat_add_fitness(self):
            self._fitness += 10
            if self._fitness > 100:
                self._fitness = 100
            if self.isfat == True and self._fitness >= 20:
                if self.days_pregnant < (global_pregnancy_length * 0.3):
                    self.pregnancy = 0
            
            refresh_avatar()
        
        def cheat_remove_fitness(self):
            self._fitness -= 10
            if self._fitness < 0:
                self._fitness = 0
            if self.isfat == False and self._fitness < 20:
                if self.pregnant in (0,3):
                    self.pregnancy = 1
            
            refresh_avatar()
        
        def cheat_add_int(self):
            self._int += 10
            if self._int > 100:
                self._int = 100
        def cheat_remove_int(self):
            self._int -= 10
            if self._int < 0:
                self._int = 0
        
        def cheat_add_money(self):
            self.cash += 1000
        
        def cheat_remove_money(self):
            self.cash -= 1000
        
        def cheat_preg_day(self, amount=10):
            for _ in range(amount):
                self.preg_day()
        
        def cheat_bukake(self):
            self.sex_cum_apply("cum_mouth")
            self.sex_cum_apply("cum_face")
            self.sex_cum_apply("cum_chest") 
            self.sex_cum_apply("cum_belly")
            self.sex_cum_apply("cum_vagout")
            self.sex_cum_apply("cum_vagin")
            self.sex_cum_apply("cum_assout")
        
        def cheat_suntan(self,amount):
            self.suntan += amount
        
        def generate_pre_game_stats(self, man, amount=200, children=False, fertility=0.1, regen=15):
            
            
            
            
            
            
            fertility_base = self.cycle_conditions["chance_base"] 
            self.cycle_conditions["chance_base"] = fertility
            
            
            if not man.skinshad:
                man._skinbase = get_npc_skin_colour(True).rgb
                man._skinshad = get_npc_skin_colour(False).rgb
                man._virginname = rlist.pre_game_bf_virgin
                man._pregname = rlist.pre_game_bf_preg
            if regen:
                
                regen = numgen(int(regen * 0.5), int(regen * 1.5))
            
            for _ in range(amount):
                self.cycle_gamestart_randomiser()
                
                
                if regen and not numgen(0,regen):
                    npc_all.append(man)
                    man = npc_all[-1]
                    npc_race_picker()
                    man._skinbase = get_npc_skin_colour(True).rgb
                    man._skinshad = get_npc_skin_colour(False).rgb
                    man._virginname = rlist.pre_game_bf_virgin
                    man._pregname = rlist.pre_game_bf_preg
                
                output = WeightedChoice([
                
                ("hj", 70), 
                ("bj", 100), 
                ("sex", 60), 
                ("anal", 2), 
                ])
                if output == "hj":
                    self.sex_hand(man)
                    self.sex_cum(man, random(["chest", "belly", "face", "hand"]))
                elif output == "bj":
                    self.sex_oral(man)
                    self.sex_cum(man, random(["chest", "belly", "face", "mouth", "mouth", "mouth", "mouth"]))
                elif output == "anal":
                    self.sex_anal(man)
                    self.sex_cum(man, random(["anal", "ass", "pullout", "anal"]))
                else:
                    
                    self.sex_vag(man)
                    self.sex_cum(man, random(["inside", "inside", "inside", "inside", "chest", "belly", "pullout", "pullout", "pullout", "pullout"]))
                self.reset_sex_status() 
                
                if self.pregnant:
                    if children:
                        self.cheat_preg_day(10)
                        if self.days_pregnant > global_pregnancy_length:
                            self.give_birth(pass_time=False)
                        elif not numgen(0,10):
                            self.preg_abortion()
                    elif self.days_pregnant == 0:
                        self.cheat_preg_day(numgen(0, int(global_pregnancy_length * 0.8)))
            
            
            
            self.cycle_conditions["chance_base"] = fertility_base
            
            
            
            
            self.sex_hideaction()
            self.cum_clean()
            self.preg_day() 
            for i in self.perk_list:
                if any([i.mins, i.hours, i.days]):
                    self.remove_perk(i)
            
            
            for i in ["hsex", "osex", "vsex", "asex", "swallow", "facial", "creamvag", "creamanal"]:
                if getattr(self, i) and not i in sex_first_time_dict:
                    add_to_list(sex_first_time_dict, i)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
