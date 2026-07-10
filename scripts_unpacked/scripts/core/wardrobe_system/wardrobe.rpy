init python:
    config.use_cpickle = False
    config.save_dump = False

    def wardrobe_copy_tab(tab_source, tab_to):
        
        
        
        globals()[tab_to] = copy.deepcopy(globals()[tab_source])

    def wardrobe_sethair():
        hair = "auto"
        fringe = True
        if c.hat:
            hat = globals()["item_hat_" + str(c.hat)]
            hair = getattr(hat, "hat_hair", hair)
            fringe = getattr(hat, "hat_fringe", fringe)
        
        player.set_hair(hair, fringe)

    def wardrobe_shirt_cycle_collar():
        if not c.top == 4:
            clothes_set("school", "top", 4)
        else:
            c.shirt_collar += 1
            if c.shirt_collar > 4:
                c.shirt_collar = 1
            school.shirt_collar = c.shirt_collar
    def wardrobe_shirt_cycle_body():
        if not c.top == 4:
            clothes_set("school", "top", 4)
        else:
            c.shirt_body += 1
            if c.shirt_body > 2:
                c.shirt_body = 1
            school.shirt_body = c.shirt_body
    def wardrobe_shirt_collar_button():
        renpy.ui.imagebutton(auto=("wardrobe_clothes_frame_%s"),
        action=Function(wardrobe_shirt_cycle_collar),
        hovered=Show("wardrobe_text", text_title="SHIRT COLLAR",
        text_desc=""), unhovered=Hide("wardrobe_text"))
    def wardrobe_shirt_body_button():
        renpy.ui.imagebutton(auto=("wardrobe_clothes_frame_%s"),
        action=Function(wardrobe_shirt_cycle_body),
        hovered=Show("wardrobe_text", text_title="SHIRT BODY",
        text_desc=""), unhovered=Hide("wardrobe_text"))

    def wardrobe_main_button():
        if tab_left == "hat":
            return owned_hat
        elif tab_left == "jacket":
            return owned_jacket
        elif tab_left == "outfit":
            return owned_outfit
        elif tab_left == "top":
            return owned_top
        elif tab_left == "bottom":
            return owned_bottom
        elif tab_left == "bra":
            return owned_bra
        elif tab_left == "pants":
            return owned_pants
        elif tab_left == "socks":
            return owned_socks
        elif tab_left == "gloves":
            return owned_gloves

    def formattext(number):
        global tab_left
        str1 = (tab_left + "_" + str(number))
        str2 = (tab_left + "_" + str(number))
        str3 = (tab_left + "_" + str(number))
        return (globals()[str1].name, globals()[str2].desc, globals()[str3].cost)

    def formattext_shop(number):
        global tab_left_shop
        str1 = (tab_left_shop + "_" + str(number))
        str2 = (tab_left_shop + "_" + str(number))
        str3 = (tab_left_shop + "_" + str(number))
        return (globals()[str1].name, globals()[str2].desc, globals()[str3].cost)

    def get_outfit(number):
        global tab_left
        str1 = tab_left + "_" + str(number)
        return globals()[str1].outfit

    def get_outfit_shop(number):
        global tab_left_shop
        str1 = tab_left_shop + "_" + str(number)
        return globals()[str1].shop

    def clothes_set(outfit_type, number):
        global tab_top
        setattr(c, outfit_type, number)
        setattr(globals()[tab_top], outfit_type, number)
        player.allure_function()


    def tab_clothes(outfit):
        global tab_top, tab_left
        for i in clothes_wardrobe_list:
            setattr(c, i, getattr(globals()[outfit], i))
        
        tab_top = outfit
        tab_left = "outfit" if c.outfit else "top"
        
        return

    def get_outfit_class(outfit=None, alt_outfit=False):
        global tab_top
        if outfit == None:
            outfit = tab_top
        
        if alt_outfit:
            return globals()[outfit + str(alt_outfit)]
        else:
            return globals()[outfit]

    def dress_default():
        
        global tab_top
        if "daily" in tab_top:
            tab_top = "school"
        elif "school" in tab_top:
            school.top = 4
            school.bottom = 5
            school.jacket = 1
        elif "sport" in tab_top:
            sport.outfit = 0
            sport.top = 3
            sport.bottom = 4
        elif "swim" in tab_top:
            sport.outfit = 2
            sport.top = 0
            sport.bottom = 0
        dress()

    def pc_strip_work():
        for i in clothes_wardrobe_list:
            setattr(work, i, 0)

    def pc_strip(temp=False):
        if temp:
            pc_set_temp_outfit()
        for i in clothes_wardrobe_list:
            setattr(c, i, 0)

    def pc_dress(outfit=None, ignore_naked=False): 
        global tab_top, clothes_wardrobe_list
        if not outfit == None:
            pc_set_outfit(outfit, ignore_naked)
        
        for i in clothes_wardrobe_list:
            if getattr(get_outfit_class(), i) and wardrobe.qty(globals()["item_" + i + "_" + str(getattr(get_outfit_class(), i))]):
                setattr(c, i, getattr(get_outfit_class(), i))
            else:
                setattr(c, i, 0)
        refresh_avatar()

    def pc_set_outfit(outfit=None, ignore_naked=False):
        global tab_top
        if not outfit == None and outfit in clothes_tab_list:
            
            outfit_list = []
            outfit = re.sub("[0-9]$", "", outfit)
            if not get_outfit_class(outfit).inappropriate or ignore_naked: 
                outfit_list.append(outfit)
            if not get_outfit_class(outfit, "2").inappropriate or ignore_naked:
                outfit_list.append(outfit + "2")
            
            if outfit_list:
                tab_top = random(outfit_list)
            else:
                pc_find_appropriate_outfit()
        
        elif not outfit == None:
            tab_top = outfit
        return

    def pc_find_appropriate_outfit():
        global tab_top
        for i in clothes_tab_list:
            if not globals()[i].inappropriate and not ("swim" in i or "home" in i):
                pc_set_outfit(i)
                return
        else: 
            renpy.call("wardrobe_no_appropriate_outfit_call") 


    def pc_set_clothing(tab, slot, number, colour_pri="blue", colour_sec="blue", trans_pri="trans_normal", trans_sec="trans_normal"):
        setattr(tab, slot, number)
        setattr(tab, slot + "_primary_colour", colour_pri)
        setattr(tab, slot + "_secondary_colour", colour_sec)
        setattr(tab, slot + "_primary_trans", trans_pri)
        setattr(tab, slot + "_secondary_trans", trans_sec)

    def pc_dress_event(tab, where="", where2="", say="There we go...", events=None, force_dress=False):
        global loc_cur, loc_from, tab_top
        if tab in tab_top:
            
            return
        if where == "":
            if loc_cur.population == 0 or (loc(loc_school_field, loc_school_field_back) and t.timeofday == "night"):
                where = loc_cur
            else:
                where = loc_cur.isolate_loc 
        if where2 == "":
            where2 = where
        if not isinstance(where, list):
            where = [where]
        if not isinstance(where2, list):
            where2 = [where2]
        if not loc_cur == where[-1]: 
            renpy.pause (.5)
            renpy.scene()
            for i in where:
                walk(i)
        pc_striptease()
        renpy.pause (.5)
        if tab in clothes_tab_list:
            pc_set_outfit(tab)
        else:
            tab_top = tab
        
        pc_dress_slow(force_dress=force_dress)
        
        renpy.say(pcc, say)
        
        if where2 == None:
            return
        elif not loc_cur == where2[-1]: 
            renpy.pause (.5)
            for i in where2:
                walk(i)
            renpy.pause (.5)


    def pc_strip_tops(slow=False, temp=False):
        for i in clothes_wardrobe_tops_list:
            if getattr(c, i):
                setattr(c, i, 0)
                if slow:
                    renpy.pause (.5)
        if temp:
            pc_set_temp_outfit()

    def pc_strip_random(group=False):
        
        removed = False 
        for i in clothes_wardrobe_tops_list:
            if getattr(c, i):
                setattr(c, i, 0)
                removed = True
                if not group:
                    break
        if removed:
            return
        for i in clothes_wardrobe_under_list:
            if getattr(c, i):
                setattr(c, i, 0)
                removed = True
                if not group:
                    break

    def pc_dress_tops(slow=False, force_dress=False):
        for i in clothes_wardrobe_tops_list[::-1]:
            if getattr(get_outfit_class(), i) and (wardrobe.qty(globals()["item_" + i + "_" + str(getattr(get_outfit_class(), i))]) or force_dress):
                setattr(c, i, getattr(get_outfit_class(), i))
                if slow:
                    renpy.pause (.5)
            else:
                setattr(c, i, 0)

    def pc_strip_under(slow=False, temp=False):
        for i in clothes_wardrobe_under_list:
            if getattr(c, i):
                setattr(c, i, 0)
                if slow:
                    renpy.pause (.5)
        if temp:
            pc_set_temp_outfit()

    def pc_dress_under(slow=False, force_dress=False):
        for i in clothes_wardrobe_under_list[::-1]:
            if getattr(get_outfit_class(), i) and (wardrobe.qty(globals()["item_" + i + "_" + str(getattr(get_outfit_class(), i))]) or force_dress):
                setattr(c, i, getattr(get_outfit_class(), i))
                if slow:
                    renpy.pause (.5)
            else:
                setattr(c, i, 0)

    def pc_strip_upper(slow=False, temp=False):
        for i in clothes_wardrobe_upper_list:
            if getattr(c, i):
                setattr(c, i, 0)
                if slow:
                    renpy.pause (.5)
        if temp:
            pc_set_temp_outfit()

    def pc_dress_upper(slow=False, force_dress=False):
        for i in clothes_wardrobe_upper_list[::-1]:
            if getattr(get_outfit_class(), i) and (wardrobe.qty(globals()["item_" + i + "_" + str(getattr(get_outfit_class(), i))]) or force_dress):
                setattr(c, i, getattr(get_outfit_class(), i))
                if slow:
                    renpy.pause (.5)
            else:
                setattr(c, i, 0)

    def pc_strip_lower(slow=False, temp=False):
        for i in clothes_wardrobe_lower_list:
            if getattr(c, i) > 0:
                setattr(c, i, 0)
                if slow:
                    renpy.pause (.5)
        if temp:
            pc_set_temp_outfit()

    def pc_dress_lower(slow=False, force_dress=False):
        for i in clothes_wardrobe_lower_list[::-1]:
            if getattr(get_outfit_class(), i) and (wardrobe.qty(globals()["item_" + i + "_" + str(getattr(get_outfit_class(), i))]) or force_dress):
                setattr(c, i, getattr(get_outfit_class(), i))
                if slow:
                    renpy.pause (.5)
            else:
                setattr(c, i, 0)

    def pc_striptease(temp=False):
        pc_strip_upper(slow=True)
        pc_strip_lower(slow=True)
        if temp:
            pc_set_temp_outfit()

    def pc_dress_slow(outfit=None, force_dress=False):
        if not outfit == None:
            pc_set_outfit(outfit)
        pc_dress_under(slow=True, force_dress=force_dress)
        pc_dress_tops(slow=True, force_dress=force_dress)

    def pc_dress_quick(outfit="none"):
        global tab_top
        if not outfit == "none":
            tab_top = outfit
        
        pc_dress_under()
        renpy.pause (.5)
        pc_dress()
        return

    def pc_loose_clothes():
        if "temp_outfit" in tab_top:
            return
        if dis(dis_haven) or dis(dis_partyhouse):
            return
        if loc_cur in dis_misc.locs:
            return
        if loc(loc_motel_pinkroom) or (loc(loc_motel_pinkroom, True) and loc(loc_motel_shower)):
            pc_set_temp_outfit()
            return
        
        tab_obj = globals()[tab_top]
        
        for i in clothes_wardrobe_list:
            c_val = getattr(c, i)
            tab_val = getattr(tab_obj, i)
            
            if c_val == 0 and tab_val != 0:
                if cheats:
                    renpy.say("", "DEBUG. You have lost some clothes.")
                
                item_name = "item_" + i + "_" + str(tab_val)
                wardrobe.drop(globals()[item_name])
                setattr(tab_obj, i, 0)
        return

    def pc_loose_clothes_random():
        for i in clothes_wardrobe_list:
            if getattr(c, i) and not numgen(0, 2):
                setattr(c, i, 0)

    def pc_dress_lost_clothes(): 
        for i in clothes_wardrobe_lower_list:
            if not getattr(c,i) and getattr(globals()[tab_top], i) and not numgen(0,3):
                setattr(globals()[tab_top], i, 0)
        pc_dress_slow()

    def pc_lost_clothes():
        global tab_top
        for i in clothes_wardrobe_list:
            if not getattr(c, i) == getattr(globals()[tab_top], i):
                return True
        return False

    def pc_set_temp_outfit(): 
        global tab_top
        if tab_top == "temp_outfit":
            return
        for i in clothes_wardrobe_list:
            setattr(temp_outfit, i + "_primary_colour", getattr(globals()[tab_top],i + "_primary_colour"))
            setattr(temp_outfit, i + "_secondary_colour", getattr(globals()[tab_top],i + "_secondary_colour"))
            setattr(temp_outfit, i + "_primary_trans", getattr(globals()[tab_top],i + "_primary_trans"))
            setattr(temp_outfit, i + "_secondary_trans", getattr(globals()[tab_top],i + "_secondary_trans"))
            setattr(temp_outfit, i, getattr(c,i))
        tab_top = "temp_outfit"

    def pc_remove_clothes_exhibitionist():
        removed = False
        if any([c.pants, c.bsuit, c.bra]):
            c.pants = 0
            c.bsuit = 0
            c.bra = 0
            removed = True
        for i in clothes_wardrobe_list:
            if getattr(c, i) and numgen():
                removed = True
                setattr(c, i, 0)
        if removed:
            pc_set_temp_outfit()
        
        return removed
        
        
        
        
        tab_top_backup = tab_top
        tab_top = "temp_outfit"

    def pc_remove_bad_clothes():
        global tab_top
        for i in clothes_wardrobe_list:
            if getattr(c, i) == 0:
                continue 
            newtab = re.sub("[0-9]$", "", tab_top)
            item = globals()["item_" + i + "_" + str(getattr(c, i))]
            if newtab not in item._outfit:
                setattr(c, i, 0)
                setattr(globals()[tab_top], i, 0)

    class ClothesType(object):
        def __init__(self, tab, number, skirt=0, clevage=0, belly=0, ass=0, thong=0, slutty=0, nips=0, hair="", name="", desc="", cost=0, outfit=["school", "daily", "sport", "party", "home"], shop=[]):
            self.name = name
            self.desc = desc
            self.cost = cost
            self.outfit = outfit
            self.owned = False
            self.hat_hair = hair
            self.shop = shop
            self.tab = tab
            self.number = number
            
            
            
            self.get_price(tab, skirt, clevage, belly, ass, thong, slutty, cost, shop)
        
        
        
        
        
        
        
        
        
        def get_class_name(self):
            return str(self.__name__)
        
        def addlist(self, alist, number):
            global list_hat, list_jacket, list_outfit, list_top, list_bottom, list_pants, list_bra, list_socks, list_gloves
            add_to_list(alist, number)
        
        def addprop(self, list, number):
            
            if not number in list:
                list.append(number)
        
        def outfit_prop(self, skirt, clevage, belly, ass, thong, slutty, nips):
            if skirt:
                if self.list == list_outfit:
                    self.addprop(cloo_skirt, self.number)
                elif self.list == list_bottom:
                    self.addprop(clo_skirt, self.number)
            
            if clevage:
                if self.list == list_outfit:
                    self.addprop(cloo_clevage, self.number)
                elif self.list == list_top:
                    self.addprop(clo_clevage, self.number)
            
            if belly:
                if self.list == list_outfit:
                    self.addprop(cloo_belly, self.number)
                elif self.list == list_top:
                    self.addprop(clo_belly, self.number)
            
            if ass:
                if self.list == list_outfit:
                    self.addprop(cloo_ass, self.number)
                elif self.list == list_bottom:
                    self.addprop(clo_ass, self.number)
            
            if thong:
                if self.list == list_outfit:
                    self.addprop(cloo_thong, self.number)
                elif self.list == list_pants:
                    self.addprop(clo_thong, self.number)
            
            if slutty:
                if self.list == list_outfit:
                    self.addprop(cloo_slutty, self.number)
                elif self.list == list_bottom:
                    self.addprop(clo_botslutty, self.number)
                elif self.list == list_top:
                    self.addprop(clo_topslutty, self.number)
            
            if nips:
                if self.list == list_outfit:
                    self.addprop(cloo_nips, self.number)
                elif self.list == list_top:
                    self.addprop(clo_nips, self.number)
                elif self.list == list_bra:
                    self.addprop(bra_nips, self.number)
        
        def get_price(self, tab, skirt, clevage, belly, ass, thong, slutty, cost, shop):
            totalcost = cost
            if tab == "hat":
                totalcost += 500
            elif tab == "jacket":
                totalcost += 1000
            elif tab == "outfit":
                totalcost += 2000
            elif tab in ("top", "bottom"):
                totalcost += 800
            elif tab == "bra":
                totalcost += 400
            elif tab == "pants":
                totalcost += 300
            elif tab in ("socks", "gloves"):
                totalcost += 600
            
            amount = sum((skirt, clevage, belly, ass, thong, slutty))
            if amount > 0:
                totalcost += amount * 200
            if "cosplay" in shop:
                totalcost += 500
            elif "meow" in shop:
                totalcost += 200
            self.cost = totalcost
            return totalcost



    class Clothes(object):
        def __init__(self, hat=0, jacket=0, outfit=0, top=0, bottom=0, bra=0, pants=0, bsuit=0, socks=0, gloves=0, coat=0):
            self._hat = hat
            self._jacket = jacket
            self._outfit = outfit
            self._top = top
            self._bottom = bottom
            self._bra = bra
            self._pants = pants
            self._socks = socks
            self._bsuit = bsuit
            self._gloves = gloves
            
            self._coat = coat
            
            self._shirt_body = 1
            self._shirt_collar = 1
            
            
            
            self.breast_coverage = 0
            self.vag_coverage = 0
            self.ass_coverage = 0
            
            self._skirt = False 
            self._clevage = False 
            self._belly = False 
            self._ass = False 
            self._braless = False 
            self._pantsless = False 
            self._thong = False 
            self._slutty = False 
            self._pokenips = False 
            
            self.hat_primary_colour = "custom6"
            self.hat_secondary_colour = "custom3"
            self.outfit_primary_colour = "custom6"
            self.outfit_secondary_colour = "custom10"
            self.jacket_primary_colour = "custom6"
            self.jacket_secondary_colour = "custom10"
            self.top_primary_colour = "custom6"
            self.top_secondary_colour = "custom10"
            self.bottom_primary_colour = "custom6"
            self.bottom_secondary_colour = "custom10"
            self.bra_primary_colour = "custom3"
            self.bra_secondary_colour = "custom10"
            self.pants_primary_colour = "custom3"
            self.pants_secondary_colour = "custom10"
            self.bsuit_primary_colour = "custom3"
            self.bsuit_secondary_colour = "custom10"
            self.socks_primary_colour = "custom6"
            self.socks_secondary_colour = "custom3"
            self.gloves_primary_colour = "custom6"
            self.gloves_secondary_colour = "custom3"
            self.coat_primary_colour = "custom6"
            self.coat_secondary_colour = "custom3"
            
            self.hat_primary_trans = "trans_normal"
            self.hat_secondary_trans = "trans_normal"
            self.outfit_primary_trans = "trans_normal"
            self.outfit_secondary_trans = "trans_normal"
            self.jacket_primary_trans = "trans_normal"
            self.jacket_secondary_trans = "trans_normal"
            self.top_primary_trans = "trans_normal"
            self.top_secondary_trans = "trans_normal"
            self.bottom_primary_trans = "trans_normal"
            self.bottom_secondary_trans = "trans_normal"
            self.bra_primary_trans = "trans_normal"
            self.bra_secondary_trans = "trans_normal"
            self.pants_primary_trans = "trans_normal"
            self.pants_secondary_trans = "trans_normal"
            self.bsuit_primary_trans = "trans_normal"
            self.bsuit_secondary_trans = "trans_normal"
            self.socks_primary_trans = "trans_normal"
            self.socks_secondary_trans = "trans_normal"
            self.gloves_primary_trans = "trans_normal"
            self.gloves_secondary_trans = "trans_normal"
            self.coat_primary_trans = "trans_normal"
            self.coat_secondary_trans = "trans_normal"
        
        
        
        
        @property
        def hat(self):
            return self._hat
        @property
        def jacket(self):
            return self._jacket
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
        
        @property
        def coat(self):
            return self._coat
        
        @property
        def shirt_body(self):
            return self._shirt_body
        @property
        def shirt_collar(self):
            return self._shirt_collar
        
        
        @property
        def skirt(self):
            if self.outfit:
                return getattr(globals()["item_outfit_" + str(self._outfit)], "skirt")  
            elif self.bottom:
                return getattr(globals()["item_bottom_" + str(self._bottom)], "skirt")
            else:
                return False
        @property
        def clevage(self):
            if self.bra and getattr(globals()["item_bra_" + str(self._bra)], "clevage"):
                if self.outfit:
                    return getattr(globals()["item_outfit_" + str(self._outfit)], "clevage")
                elif self.top:
                    return getattr(globals()["item_top_" + str(self._top)], "clevage")
                else:
                    return True
            elif not self.bra:
                if self.outfit:
                    return getattr(globals()["item_outfit_" + str(self._outfit)], "clevage")
                elif self.top:
                    return getattr(globals()["item_top_" + str(self._top)], "clevage")
                else:
                    return True
            else:
                return False
        
        @property
        def ass(self):
            if self.outfit:
                return getattr(globals()["item_outfit_" + str(self._outfit)], "ass")
            elif self.bottom:
                return getattr(globals()["item_bottom_" + str(self._bottom)], "ass")
            else:
                return True
        @property
        def belly(self):
            if self.outfit:
                return getattr(globals()["item_outfit_" + str(self._outfit)], "belly")
            elif self.top:
                return getattr(globals()["item_top_" + str(self._top)], "belly")
            else:
                return True
        @property
        def braless(self):
            if self._bra and not getattr(globals()["item_bra_" + str(self._bra)], "braless"):
                return False
            else:
                return True
        @property
        def bra_nolift(self):
            if self._bra and not getattr(globals()["item_bra_" + str(self._bra)], "bra_nolift") or self._bsuit and not getattr(globals()["item_bsuit_" + str(self._bsuit)], "bra_nolift"):
                
                return False
            else:
                return True
        @property
        def pantsless(self):
            if self._pants and not getattr(globals()["item_pants_" + str(self._pants)], "pantsless"):
                return False
            else:
                return True
        @property
        def thong(self):
            if (self._pants and getattr(globals()["item_pants_" + str(self._pants)], "thong")) or (self._bottom and getattr(globals()["item_bottom_" + str(self._bottom)], "thong")):
                return True
            else:
                return False
        
        @property
        def slutty(self):
            if self.exposed or self.inappropriate:
                return True
            elif (self.outfit and getattr(globals()["item_outfit_" + str(self._outfit)], "slutty")) or (self.top and getattr(globals()["item_top_" + str(self._top)], "slutty")) or (self.bottom and getattr(globals()["item_bottom_" + str(self._bottom)], "slutty")):
                return True
            else:
                return False
        
        @property
        def pokenips(self):
            can_poke = False
            if self._bra and not getattr(globals()["item_bra_" + str(self._bra)], "braless"):
                can_poke = False
            elif acc.nipring == 2: 
                can_poke = False
            elif self._outfit:
                can_poke = getattr(globals()["item_outfit_" + str(self._outfit)], "pokenips")
            elif self._top:
                can_poke = getattr(globals()["item_top_" + str(self._top)], "pokenips")
            if can_poke and (player.check_horny() or loc_cur.outside):
                return True
            else:
                return False
        
        @property
        def exposed(self):
            return self.exposed_check()
        @property
        def inappropriate(self):
            return self.inappropriate_check()
        @property
        def appropriate(self):
            return not self.inappropriate_check()
        
        @property
        def cansee_breasts(self):
            if self.cansee_breasts_clothes_check() == 0: 
                return True
            else:
                return False
        @property
        def cansee_nips(self):
            if self.cansee_breasts_clothes_check() == 0:
                return True
            else:
                return False
        def cansee_breasts_clothes_check(self): 
            return self.breast_coverage
        def cansee_breasts_clothes_check_setter(self): 
            
            
            amount = 0
            
            g = globals()  
            wardrobe = clothes_wardrobe_list 
            for i in wardrobe:
                clothes_value = getattr(self, i)
                
                if not clothes_value: 
                    continue
                
                inv_item = "item_" + i + "_" + str(clothes_value)
                clothes = g[inv_item]
                
                if not (i in ("top", "outfit", "coat", "bra") or clothes.covers_top): 
                    continue
                
                nips = clothes.exposed_nips 
                
                if nips == False:
                    self.breast_coverage = 5
                    return
                elif nips == True:
                    pass
                else:
                    
                    pri_trans = getattr(self, i + "_primary_trans")
                    sec_trans = getattr(self, i + "_secondary_trans")
                    
                    
                    if nips == "pri" and pri_trans == "trans_sheer" or nips == "sec" and sec_trans == "trans_sheer":
                        amount += 2
                    elif nips == "pri" and pri_trans == "trans_normal" or nips == "sec" and sec_trans == "trans_normal":
                        amount += 4
                    else:
                        amount += 1
                
                if amount >= 5:
                    
                    self.breast_coverage = 5
                    return
            self.breast_coverage = min(amount, 5)
        
        @property
        def cansee_bra(self):
            if not self._top and not self._outfit and not self._coat and self._bra:
                return True
            else:
                return False
        @property
        def cansee_vagina(self):
            if self.cansee_vag_clothes_check() == 0:
                return True
            else:
                return False
        
        @property
        def cansee_vag(self):
            
            return self.cansee_vagina
        
        def cansee_vag_clothes_check(self): 
            return self.vag_coverage
        def cansee_vag_clothes_check_setter(self):  
            
            
            amount = 0
            
            g = globals()  
            wardrobe = clothes_wardrobe_list 
            for i in wardrobe:
                clothes_value = getattr(self, i)
                
                if not clothes_value: 
                    continue
                
                inv_item = "item_" + i + "_" + str(clothes_value)
                clothes = g[inv_item]
                
                if not (i in ("bottom", "outfit", "pants") or clothes.covers_bottom): 
                    continue
                
                vag = clothes.exposed_vag 
                
                if vag == False:
                    self.vag_coverage = 5
                    return
                elif vag == True:
                    pass
                else:
                    
                    pri_trans = getattr(self, i + "_primary_trans")
                    sec_trans = getattr(self, i + "_secondary_trans")
                    
                    
                    if vag == "pri" and pri_trans == "trans_sheer" or vag == "sec" and sec_trans == "trans_sheer":
                        amount += 2
                    elif vag == "pri" and pri_trans == "trans_normal" or vag == "sec" and sec_trans == "trans_normal":
                        amount += 4
                    else:
                        amount += 1
                
                if amount >= 5:
                    
                    self.vag_coverage = 5
                    return
            self.vag_coverage = min(amount, 5)
        
        @property
        def cansee_ass(self):
            if self.cansee_ass_clothes_check() == 0:
                return True
            else:
                return False
        
        
        
        
        
        def cansee_ass_clothes_check(self): 
            return self.ass_coverage
        def cansee_ass_clothes_check_setter(self):  
            
            
            amount = 0
            
            g = globals()  
            wardrobe = clothes_wardrobe_list 
            for i in wardrobe:
                clothes_value = getattr(self, i)
                
                if not clothes_value: 
                    continue
                
                inv_item = "item_" + i + "_" + str(clothes_value)
                clothes = g[inv_item]
                
                if not (i in ("bottom", "outfit", "pants") or clothes.covers_bottom): 
                    continue
                
                ass = clothes.exposed_ass 
                
                if ass == False:
                    self.ass_coverage = 5
                    return
                elif ass == True:
                    pass
                else:
                    
                    pri_trans = getattr(self, i + "_primary_trans")
                    sec_trans = getattr(self, i + "_secondary_trans")
                    
                    
                    if ass == "pri" and pri_trans == "trans_sheer" or ass == "sec" and sec_trans == "trans_sheer":
                        amount += 2
                    elif ass == "pri" and pri_trans == "trans_normal" or ass == "sec" and sec_trans == "trans_normal":
                        amount += 4
                    else:
                        amount += 1
                
                if amount >= 5:
                    
                    self.ass_coverage = 5
                    return
            self.ass_coverage = min(amount, 5)
        
        @property
        def cansee_pants(self):
            if not self._bottom and not self._outfit and self._pants:
                return True
            else:
                return False
        
        @property
        def cansee_underwear(self):
            if self.cansee_pants or self.cansee_bra:
                return True
            else:
                return False
        
        @property
        def nude(self):
            if self.cansee_breasts and self.cansee_vagina:
                return True
            else:
                return False
        
        @property
        def nude_parts(self):
            if self.cansee_breasts or self.cansee_vagina:
                return True
            else:
                return False
        
        @property
        def underwear(self):
            if self.cansee_bra and self.cansee_pants:
                return True
            else:
                return False
        @property
        def clothed(self):
            if not self.underwear and not self.nude:
                return True
            else:
                return False
        
        @property
        def outerwear(self):
            for i in clothes_wardrobe_tops_list:
                if getattr(self, i):
                    return True
            return False
        
        
        @jacket.setter
        def jacket(self, jackets):
            self._jacket = jackets
            self.clothing_checks()
        
        @hat.setter
        def hat(self, hats):
            self._hat = hats
            wardrobe_sethair()
            self.clothing_checks()
        
        
        @top.setter
        def top(self, tops):
            global wardrobe_restricted
            self._top = tops
            if self._top > 0 and wardrobe_restricted:
                self._outfit = 0
            
            self.clothing_checks()
        
        
        @bottom.setter
        def bottom(self, bottoms):
            global wardrobe_restricted
            self._bottom = bottoms
            if self._bottom > 0 and wardrobe_restricted:
                self._outfit = 0
            
            self.clothing_checks()
        
        @outfit.setter
        def outfit(self, outfits):
            global wardrobe_restricted
            self._outfit = outfits
            if self._outfit > 0 and wardrobe_restricted:
                self._top = 0
                self._bottom = 0
            
            self.clothing_checks()
        
        @bra.setter
        def bra(self, bras):
            global wardrobe_restricted
            self._bra = bras
            if self.bsuit and wardrobe_restricted:
                self._bsuit = 0
            
            self.clothing_checks()
        
        @pants.setter
        def pants(self, pantss):
            global wardrobe_restricted
            self._pants = pantss
            if self._bsuit and wardrobe_restricted:
                self._bsuit = 0
            
            self.clothing_checks()
        
        @bsuit.setter
        def bsuit(self, bsuits):
            global wardrobe_restricted
            self._bsuit = bsuits
            if self._bsuit and wardrobe_restricted:
                self._bra = 0
                self._pants = 0
            
            self.clothing_checks()
        @socks.setter
        def socks(self, sockss):
            self._socks = sockss
        
        @gloves.setter
        def gloves(self, glovess):
            self._gloves = glovess
            refresh_avatar()
        
        @coat.setter
        def coat(self, coats):
            self._coat = coats
            refresh_avatar()
        
        def clothing_checks(self):
            
            player.check_effect_perks()
            self.cansee_breasts_clothes_check_setter()
            self.cansee_vag_clothes_check_setter()
            self.cansee_ass_clothes_check_setter()
            refresh_avatar()
        
        def exposed_check(self):
            
            
            if self.nude_parts:
                return True
            else:
                return False
        
        def can_access_vag(self):
            if self.pants and not self.pantsless:
                return False
            elif (self.bottom or self.outfit) and not self.skirt:
                return False
            else:
                return True
        
        def can_access_pants(self):
            if not self.pants:
                return False
            elif (self.bottom or self.outfit) and not self.skirt:
                return False
            else:
                return True
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        def inappropriate_check(self):
            if self == swim or self == swim2:
                if player.has_perk([perk_slut, perk_exhibitionist, perk_broken]) or dis(dis_beach):
                    return False
                elif self.nude_parts:
                    if player.confidence >= 40 or player.fitness >= 40:
                        return False
                    else:
                        return True
                else:
                    return False
            
            elif self == sport:
                if self.nude_parts:
                    return True
                else:
                    return False
            
            elif self == home:
                if player.has_perk([perk_slut, perk_exhibitionist, perk_broken]):
                    return False
                elif self.nude_parts:
                    return True
                else:
                    return False
            
            
            elif self == work:
                
                
                
                return False
            
            elif self.nude_parts:
                return True
            else:
                return False
        
        def outfit_colours(self,op,os,jp,js,tp,ts,bp,bs,brp,brs,pp,ps,sp,ss):
            self.outfit_primary_colour = op
            self.outfit_secondary_colour = os
            self.jacket_primary_colour = jp
            self.jacket_secondary_colour = js
            self.top_primary_colour = tp
            self.top_secondary_colour = ts
            self.bottom_primary_colour = bp
            self.bottom_secondary_colour = bs
            self.bra_primary_colour = brp
            self.bra_secondary_colour = brs
            self.pants_primary_colour = pp
            self.pants_secondary_colour = ps
            self.socks_primary_colour = sp
            self.socks_secondary_colour = ss
        
        
        def description_outfit(self):
            desc = ""
            if "school" in tab_top:
                desc = "I am wearing my school uniform. While it is not a very revealing outfit generally, people tend to love a girl in a school uniform so it can still draw attention."
            elif "daily" in tab_top:
                desc = "I am wearing my normal daily outfit."
            elif "party" in tab_top:
                desc = "I am wearing my party outfit. Sometimes elegant, often revealing. I should be careful as people often mistake me for a whore when I wear my party clothes."
            elif "sport" in tab_top:
                desc = "I am wearing my sports outfit."
            elif "swim" in tab_top:
                desc = "I am wearing my swimwear. Even the most modest swimming outfits leave little to the imagination so I will no doubt be drawing attention to myself while wearing it."
            elif "home" in tab_top:
                desc = "I am wearing my home clothes. Often a lot more revealing than anything I wear on the streets so I should be careful or else my flatmates might get a good eyeful."
            return desc
        
        
        def description_top(self):
            desc = ""
            if player.cum_visible:
                desc = desc + "People can see my cum stained clothes so it doesn't matter what clothes I am wearing, I just look like a dirty highway hooker. "
            
            if self.exposed:
                desc = desc + "My body is exposed and people can see my more intimate parts. "
            elif self.slutty:
                desc = desc + "I am wearing clothes that most would consider slutty so will be drawing a lot of attention. "
                if player.has_perk(perk_exhibitionist):
                    desc = desc + "But I love showing off so wearing slutty clothes makes me feel great. "
                elif player.has_perk(perk_slut):
                    desc = desc + "But I am a slut so what do I care? "
            elif player.has_perk(perk_bambi):
                desc = desc + "It doesn't seem to matter what I wear, I always seem to attract attention. "
            elif player.allure < 50:
                if player.has_perk(perk_bimbo):
                    desc = desc + "My clothes are boooring. "
                else:
                    desc = desc + "My clothing is considered to be fairly modest. "
            elif player.allure > 150:
                if player.has_perk(perk_bimbo):
                    desc = desc + "My clothes look really sexy. Guys might think I am for sale but I don't care as long as I look good! "
                else:
                    desc = desc + "My clothing choice turns heads and brings me so much attention that people may mistake me for a prostitute. "
            elif player.allure > 100:
                desc = desc + "My clothing choice turns most peoples heads and I look very attractive. "
            else:
                desc = desc + "My clothing choice makes me look quite attractive. "
            
            if self.top == 0 and self.outfit == 0:
                if self.bra == 0:
                    desc = desc + "I am not wearing a top and my breasts are clearly on display. "
                else:
                    desc = desc + "I have no top on and am just wearing a bra. "
            
            elif self.slutty:
                if "sport" in tab_top:
                    desc = desc + "I am wearing clothes that leaves very little to the imagination. While it is not so uncommon to wear revealing clothes while doing sports, that won't stop people from thinking I am up for sale. "
                else:
                    desc = desc + "I am wearing clothes that leaves very little to the imagination. Extremely revealing and no doubt making anyone who sees me think I am up for sale. "
            elif self.clevage:
                if self.belly:
                    if self.bra == 0:
                        desc = desc + "my top exposes my stomach, cleavage and it is obvious I am not wearing a bra because my breasts bounce around and my nipples poke through my top. "
                    else:
                        desc = desc + "My top exposes my stomach and my cleavage is on display. "
                else:
                    if self.bra == 0:
                        desc = desc + "My top perfectly exposes my cleavage and it is obvious I am not wearing a bra because my breasts bounce around and my nipples poke through my top. "
                    
                    else:
                        desc = desc + "I am wearing a top that gives a good view of my cleavage."
            elif self.belly:
                if self.bra == 0:
                    desc = desc + "I am wearing a top that shows off my belly and since I am not wearing a bra, my breasts bounce around as I walk and my nipples poke through my top. "
                else:
                    desc = desc + "I am wearing a top that shows off my belly."
            else:
                desc = desc + "I am wearing a fairly modest top that leaves a lot to the imagination. "
            
            if self.belly:
                if player.pregnancy > 1:
                    desc = desc + "With my stomach exposed, my pregnant belly is clearly on display. "
                elif player.pregnancy == 1 and player.preg_knows:
                    desc = desc + "With my stomach exposed, it is obvious that I am in the early stages of pregnancy. "
                elif player.isfat:
                    desc = desc + "With my stomach exposed, people can clearly see my pot belly. "
            
            
            return desc
        
        def description_bottom(self):
            desc = ""
            if self.bottom == 0 and self.outfit == 0:
                if self.pants == 0:
                    desc = desc + "I am not wearing anything below the waist and my bare ass is open for everyone to see."
                else:
                    if self.pantsless:
                        desc = desc + "I am only wearing a pair of pants below the waist. If I can call them pants since they leave nothing to the imagination."
                    elif self.thong:
                        desc = desc + "I have just a thong on, so while my pussy is somewhat hidden, my ass is on full display."
                    else:
                        desc = desc + "I only have a pair of pants on. Not really modest but it at least means I'm not on full display."
            
            
            
            elif self.skirt:
                if self.ass:
                    if self.pants == 0:
                        desc = desc + "I have a tight skirt on that shows off my ass. I have no pants on and I am a gust of wind away from showing off my pussy. "
                    elif self.thong:
                        desc = desc + "I have a tight skirt on that shows off my ass. I have a thong on under my skirt and my panty line can be seen making it obvious. "
                    else:
                        desc = desc + "I have a tight skirt on that shows off my ass."
                else:
                    if self.pants == 0:
                        desc = desc + "I have a skirt with no pants on and I am a gust of wind away from showing off my arse and pussy. "
                    elif self.thong:
                        desc = desc + "I have a skirt with a thong on. People might be able to get a glimpse of my bare arse. "
                    else:
                        desc = desc + "I have a skirt with a normal pair of pants on underneath. "
            
            elif self.ass:
                if self.pants == 0:
                    desc = desc + "I have a tight pair of bottoms on that shows off my ass. Though I don't have pants on so I have no visible panty line. "
                elif self.thong:
                    desc = desc + "I have a tight pair of bottoms on that shows off my ass. I have a thong on and it can be noticed in my panty line. "
                else:
                    desc = desc + "I have a tight pair of bottoms on that shows off my ass as well as my panty line. "
            
            else:
                desc = desc + "I have a modest pair of bottoms on that doesn't draw much attention as I walk."
            
            return desc
        
        def reset_clothes(self):
            self.jacket = 0
            self.outfit = 0
            self.top = 0
            self.bottom = 0
            self.bra = 0
            self.pants = 0
            self.socks = 0
            self.hat = 0
            self.gloves = 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
