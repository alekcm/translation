init python:
    class Npc:  
        def __init__(self, fname="", sname="", nname="", wname="", rank="", love=10, bio_image="", bio_text="", bio_group="", colour="#ffffff", pregname="", virginname="", skinbase="", skinshad="", is_female=False, iswhore=False, isslut=False, stay_virgin=False, is_unique=True, abort=False, dead_location="", dead_message="", drunk_default=15):
            self._fname = fname 
            self._sname = sname
            self._nname = nname
            self._wname = wname
            self._rank = rank
            self._fullname = fname + " " + sname
            self._original_name = fname 
            
            
            
            
            self._colour = colour
            
            self.is_unique = is_unique 
            self.bio_image = bio_image
            self.bio_group = bio_group
            self.bio_text = bio_text
            
            self._pregname = pregname
            self._virginname = virginname
            self._love = love 
            self._love_cap = 100 
            self._love_desc = None 
            self._lust = 0 
            self._lust_multi = 1
            self._sexy = False 
            self._naked = False 
            
            self._drunk = 0 
            self._drunk_default = drunk_default 
            
            self.virginbaby = False
            self.rapebaby = False
            self.soldbaby = False
            self.soldprice = 0
            self.soldrequest = 0 
            
            self.hvirgin = False 
            self.ovirgin = False
            self.vvirgin = False
            self.avirgin = False
            
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
            self.assault = 0
            self.rape = 0
            self.abort = abort 
            
            self._cum_last = 0 
            self._last_cumin = 0 
            
            self.vvirgin_know = False 
            self.preg = 0 
            self._preg_current = False 
            self.pregbabies = 0 
            
            self._skinbase = skinbase
            self._skinshad = skinshad
            
            self.seen_breasts = False
            self.seen_vagina = False
            self.seen_ass = False
            
            self.active = True 
            self.hate = False 
            self.hate_message = ""
            self.dead = False
            self.dead_location = dead_location
            self.dead_message = dead_message
            self.dead_time = 0 
            self.last_spoke_to = 0
            self.last_spoke_to_hours = 0
            self.conversation_topics = [] 
            self.list = []
            self.dict = {} 
            
            
            self.hour_number = 1
            self.day_number = 1
            self.noon_number = 1
            
            
            
            self.is_female = is_female
            
            self.is_pregnant = False 
            self.pregnant_who = "" 
            self.days_pregnant = 0 
            
            self.sex_who = {} 
            self.sex_who_class = {} 
            self.preg_who = {} 
            self.babies_who = {} 
            
            self.iswhore = iswhore
            self.isslut = isslut
            self.stay_virgin = stay_virgin
            
            
            
            
            
            self.nosex_les = 0 
            self.sex_les = 0 
            
            
            self.can_sex = False
            self.can_gift = False
            
            self.add_to_list()
            
            
            self.inv = Inventory(self._fname + "'s Inventory")
            
            
            self.classname = Character(self.setname_start, color=self._colour, callback=name_callback, cb_name=self.setname.lower(), image=If(bio_image, bio_image, self._fname))
        
        @property
        def name(self):
            showname = self.classname
            self.talk_checker(showname)
            
            return showname
        @property
        def setname(self):
            if self.iswhore and self._wname and dis(dis_truckstop):
                showname = self._wname
            elif not self._rank == "":
                showname = self._rank + " " + self._sname
            elif self.love > 40 and self._nname:
                showname = self._nname
            else:
                showname = self._fname
            return showname
        @property
        def setname_start(self):
            
            if not self._rank == "":
                showname = self._rank + " " + self._sname
            else:
                showname = self._fname
            return showname
        @property
        def fname(self):
            showname = self._fname
            self.talk_checker(showname)
            return showname
        @property
        def sname(self):
            showname = self._sname
            self.talk_checker(showname)
            return showname
        @property
        def nname(self):
            if self._nname == "":
                showname = self._fname
            else:
                showname = self._nname
            self.talk_checker(showname)
            return showname
        @property
        def wname(self):
            if self._wname == "":
                showname = self._fname
            else:
                showname = self._wname
            self.talk_checker(showname)
            return showname
        @property
        def pname(self):
            
            if self.is_female:
                showname = "Miss " + self._sname
            else:
                showname = "Mr " + self._sname
            self.talk_checker(showname)
            return showname
        @property
        def fullname(self):
            if self._rank == "":
                showname = self._fname + " " + self._sname
            else:
                showname = self._rank + " " + self._fname + " " + self._sname
            self.talk_checker(showname)
            return showname
        @property
        def rank(self):
            showname = self._rank
            self.talk_checker(showname)
            return showname
        @property
        def diaryname(self):
            showname = ""
            if self._rank:
                showname = showname + self._rank + " "
            showname = showname + self._fname + " "
            if self._nname:
                showname = showname + "\"" + self._nname + "\" "
            showname = showname + self._sname
            return showname
        @property
        def has_met(self):
            if self.last_spoke_to:
                return True
            else:
                return False
        @property
        def spoke_to_hours_ago(self):
            if self.last_spoke_to_hours:
                return (t.hours_total - self.last_spoke_to_hours)
            else:
                return False
        @property
        def spoke_to_days_ago(self):
            if self.last_spoke_to:
                return (t.day - self.last_spoke_to)
            else:
                return False
        
        @property
        def isactive(self):
            if self.active and not self.dead:
                return True
            else:
                return False
        
        @property
        def creamvag(self):
            return sum([self.creamsafe, self.creamnormal, self.creamdanger])
        
        @property
        def pregname(self):
            return self._pregname
        @property
        def virginname(self):
            if self._virginname == "":
                return self._fullname
            else:
                return self._virginname
        @property
        def love(self):
            if self.hate:
                return 0
            love = self._love / 20
            if love >= 100:
                return 100
            return love
        
        @property
        def love_cap(self):
            return self._love_cap
        @property
        def love_desc(self):
            if self._love_desc:
                return self._love_desc
            desc = ""
            if self.hate:
                if self.hate_message:
                    desc = self.hate_message
                else:
                    if self.is_female:
                        desc = "She utterly hates me..."
                    else:
                        desc = "He utterly hates me..."
            elif self.love < 20:
                desc = "Me and " + self._fname + " are practically strangers."
            elif self.love < 40:
                desc = "I think " + self._fname + " thinks of me as an acquaintance."
            elif self.love < 60:
                desc = "Me and " + self._fname + " are starting to become friends."
            elif self.love < 80:
                desc = "Me and " + self.nname + " are good friends."
            else:
                desc = "Me and " + self.nname + " couldn't be any closer."
            return desc
        
        @property
        def lust(self):
            return int((self._lust / 10) * self.lust_multi)
        @property
        def lust_multi(self):
            base = self._lust_multi
            if player.isslut:
                base += 0.2
            if player.isbroken:
                base += 0.5
            if (self.sex or self.sex_les) and self.is_unique:
                base += 0.2
            if (self.sex or self.sex_les) and self.is_unique and self.isslut: 
                base += 0.5
            return base
        
        @property
        def lust_desc(self):
            desc = ""
            afname = self.fname
            anname = self.nname
            if self.lust < 20:
                desc = self._fname + " doesn't show any interest in me sexually."
            elif self.lust < 40:
                desc = "Other than the odd look, I don't think " + self._fname + " is interested in me."
            elif self.lust < 60:
                desc = "I catch " + self._fname + " looking at me in that way now and then."
            elif self.lust < 80:
                desc = self.nname + " can hardly keep his eyes off me."
            else:
                desc = self.nname + " can barely contain his desires when he is around me."
            return desc
        
        @property
        def drunk(self):
            if self._drunk > 100:
                return 100
            return self._drunk
        @property
        def drunk_default(self):
            return self._drunk_default
        def add_drunk(self):
            self._drunk += self.drunk_default
            if self._drunk >= 120:
                self._drunk = 120
        def drink(self):
            
            self.add_drunk()
        def drink_max(self):
            self._drunk = 120 
        
        def remove_drunk(self, amount=10): 
            self._drunk -= amount
            if self._drunk <= 0:
                self._drunk = 0
        def undrink(self, amount=10):
            
            self.remove_drunk(amount)
        
        @property
        def is_sober(self):
            if self.drunk < 15:
                return True
            return False
        @property
        def is_tipsy(self):
            if self.drunk >= 40:
                return True
            return False
        @property
        def tipsy(self):
            return self.is_tipsy
        @property
        def is_wasted(self):
            if self.drunk >= 80:
                return True
            return False
        @property
        def wasted(self):
            return self.is_wasted
        @property
        def is_blackout(self):
            if self.drunk >= 100:
                return True
            return False
        @property
        def blackout(self):
            return self.is_blackout
        
        def sober(self):
            self._drunk = 0
        
        @property
        def last_cumin(self):
            return t.day - self._last_cumin
        
        @property
        def sexy(self):
            return self._sexy
        
        @property
        def naked(self):
            if self.seen_all:
                return True
            else:
                return False
        
        @property
        def naughty(self):
            if any([self.hsex,self.osex,self.vsex,self.asex,self.facial]):
                return True
            else:
                return False
        
        
        @property
        def sex(self):
            return self.vsex + self.asex
        
        @property
        def skinbase(self):
            if self._skinbase:
                return Color(rgb = self._skinbase) 
            else:
                return False
        @property
        def skinshad(self):
            if self._skinshad:
                return Color(rgb = self._skinshad)
            else:
                return False
        
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
        def seen_any(self):
            if any([self.seen_ass, self.seen_breasts, self.seen_vagina]): 
                return True
            else:
                return False
        @property
        def seen_all(self):
            if all([self.seen_ass, self.seen_breasts, self.seen_vagina]):
                return True
            else:
                return False
        @property
        def seen_naked(self):
            return self.seen_all
        
        @property
        def alive(self):
            return not self.dead
        
        @property
        def showing(self):
            
            if self.days_pregnant > (global_pregnancy_length * 0.3):
                return True
            else:
                return False
        
        @property
        def heavy_preg(self):
            
            global cheat_fetish_preg_fantasy
            if cheat_fetish_preg_fantasy and self.is_pregnant:
                return True
            if self.days_pregnant > (global_pregnancy_length * 0.7):
                return True
            else:
                return False
        
        @name.setter
        def name(self):
            
            if c.cansee_breasts:
                self.seen_breasts = True
            if c.cansee_ass:
                self.seen_ass = True
            if c.cansee_vagina:
                self.seen_vagina = True
            if c.cansee_bra or c.cansee_pants or c.underwear or player.allure > 150:
                self._sexy = True
        
        
        
        def add_love(self, amount=1):
            
            
            self._love += amount
            pass
        
        
        def add_lust(self, amount): 
            amount = amount * 10
            self.add_lust_self(amount)
        def add_lust_self(self, amount): 
            self._lust += amount
            if self._lust > 1000:
                self._lust = 1000
            elif self._lust < 0:
                self._lust = 0
        
        def cum(self): 
            self.reset_lust()
            self._cum_last = t.hours_total
        def reset_lust(self): 
            self._lust = 0
        def can_gain_lust(self):
            if t.hours_total in irange(self._cum_last,self._cum_last + 2):
                return False
            else:
                return True
        def want_sex(self):
            
            return self.can_gain_lust()
        
        def meet(self):
            global new_diary_people_entry
            if not self.has_met:
                if self.bio_text:
                    add_to_list(diary_people_list, self)
                    new_diary_people_entry = True
                    show_notif_popup(self.fullname + " added to the biography")
                self.last_spoke_to = t.day
                self.last_spoke_to_hours = t.hours_total
        
        def talk_checker(self, showname):
            global speaking_char_class
            speaking_char_class = self
            if cheat_name_who == showname or (hasattr(showname, "name") and getattr(showname, "name") == cheat_name_who):
                if not self.has_met and self.bio_text:
                    self.meet()
                if not self.last_spoke_to == t.day:
                    self.last_spoke_to = t.day
                if not self.last_spoke_to_hours == t.hours_total:
                    self.last_spoke_to_hours = t.hours_total
                if self.can_gain_lust():
                    self.talk_lust_add()
                self.talk_love_add()
            return
        
        def talk_love_add(self, amount=1):
            if self.love >= 100:
                return
            self._love += amount
        
        def talk_lust_add(self):
            amount = 0
            if player.allure == 0:
                amount -= 5
            if player.allure > 50:
                amount += (player.allure - 50) / 8
            if player.desire > 80:
                amount += 2
            
            if c.cansee_breasts:
                self.seen_breasts = True
                amount += 20
            if c.cansee_ass:
                self.seen_ass = True
                amount += 20
            if c.cansee_vagina:
                self.seen_vagina = True
                amount += 40
            if c.cansee_bra or c.cansee_pants or c.underwear or player.allure > 200:
                self._sexy = True
            
            self.add_lust_self(amount)
        
        def kill(self, death_message=""):
            if self.is_female:
                self.preg_abort()
            if death_message:
                self.dead_message = death_message
            self.dead = True
            self.dead_time = t.day
        
        @property 
        def days_dead(self):
            if not self.dead_time:
                return 0
            return t.day - self.dead_time
        
        
        
        
        
        def have_sex(self, who, vaginal=True, anal=True, anal_reduce=False, forced=False, sold=False, block_spray=False, cum=False, preg_force=False):  
            if self.dead or who.dead:
                return
            if forced and self.inv.qty(item_pepperspray) and not block_spray:
                return
            self.sex_add_list(who)
            if forced:
                self.rape += 1
            if sold:
                self.sold += 1
            if not numgen():
                self.osex += 1
            if not numgen():
                self.hsex += 1
            if (vaginal and (not numgen(0,3) or (anal_reduce and numgen()))) or preg_force:
                self.vsex += 1
                if self.inv.qty(item_map_pill):
                    self.inv.drop(item_map_pill)
                else:
                    self.preg_check(who, preg_force) 
            elif anal and ((not numgen() and not anal_reduce) or (anal_reduce and not numgen(0,3))):
                self.asex += 1
            if cum:
                self.cum()
                who.cum()
        
        def have_sex_milti(self, who, vaginal=True, forced=False, sold=False, times=1):
            
            for _ in range(times):
                self.have_sex(who, vaginal, forced, sold)
        
        def sex_add_list(self, who):
            name = getattr(who,"name")
            if not (name in self.sex_who and who in self.sex_who_class):
                self.sex_who[name] = 1
                self.sex_who_class[who] = 1
            else:
                self.sex_who[name] += 1
                self.sex_who_class[who] += 1
        
        
        
        
        def preg_check(self,who, force=False):
            if self.is_pregnant:
                
                return
            if force:
                self.preg_force(who)
            name = getattr(who,"name")
            if not numgen(0, If(self.iswhore, 50, 8)):
                self.is_pregnant = True
                self.pregnant_who = who
        
        def preg_force(self, who):
            if self.is_pregnant:
                return
            self.is_pregnant = True
            self.pregnant_who = who
        
        def preg_pass_day(self):
            if self.is_pregnant:
                if self.inv.qty(item_abort_pill) and self.pregnant_who.abort:
                    self.preg_abort(True)
                self.days_pregnant += 1
                if self.days_pregnant >= (global_pregnancy_length * 0.2) and not "pregnant" in self.conversation_topics:
                    add_to_list(self.conversation_topics, "pregnant")
                    self.preg += 1
                    if not self.pregnant_who.setname in self.preg_who:
                        self.preg_who[self.pregnant_who.setname] = 1
                    else:
                        self.preg_who[self.pregnant_who.setname] += 1
                if self.days_pregnant == (global_pregnancy_length * 0.5) and not self.setname + "_pregnant" in self.pregnant_who.conversation_topics:
                    
                    add_to_list(self.pregnant_who.conversation_topics, self.setname + "_pregnant")
                if self.days_pregnant >= global_pregnancy_length:
                    self.preg_birth()
            elif not self.is_pregnant and self.days_pregnant > 0:
                self.days_pregnant = 0
        
        def preg_birth(self):
            name = getattr(self.pregnant_who,"name")
            self.is_pregnant = False
            self.days_pregnant = 0
            self.pregbabies += 1
            remove_from_list(self.conversation_topics, "pregnant")
            remove_from_list(self.pregnant_who.conversation_topics, self._fname + "_pregnant")
            
            if not name in self.babies_who:
                self.babies_who[name] = 1
            else:
                self.babies_who[name] += 1
            self.pregnant_who = nosex
        
        def preg_abort(self, use_pill=False):
            if self.is_female and self.is_pregnant:
                if use_pill:
                    self.inv.drop(item_abort_pill)
                self.is_pregnant = False
                self.days_pregnant = 0
                remove_from_list(self.conversation_topics, "pregnant")
                remove_from_list(self.pregnant_who.conversation_topics, self._fname + "_pregnant")
                
                self.pregnant_who = nosex
        
        def add_to_list(self):
            npc_all.append(self)
            if self.is_unique:
                add_to_list(npc_unique, self)
            if self.is_female:
                add_to_list(npc_girls, self)
            if self.is_pregnant:
                add_to_list(npc_girls_pregnant, self)
            if self.iswhore:
                add_to_list(npc_girls_whore, self)
        
        def add_whore(self):
            if not self in npc_girls_whore:
                npc_girls_whore.append(self)
        def remove_whore(self):
            if self in npc_girls_whore:
                npc_girls_whore.remove(self)

label npc_call:

    $ nosex = Npc()



    $ emile = Npc(fname="Emile", sname="Bangtail", colour="#c1c7ff", love=0, bio_image="emile", bio_group="flatmate",
    bio_text="My younger sister. Or is she now my older sister? I don't suppose it matters any more.\n After getting into a car crash and me ending up hospitalised, she waited and looked over me for two seasons for me to get better.\nI don't remember too much about our relationship in the past, but she feels familiar and the moment I saw her again I knew she was my sister.\nI should probably try and spend some more time with her to get to know her again. It's clear she is looking out for me and has my best interests in mind.", 
    is_female=True)
    $ emile.dict["tut_anger"] = 0


    $ robin = Npc(fname="Robin", sname="Albescu", colour="#ffd5bc", love=0, bio_image="robin", bio_group="flatmate",
    bio_text="She and I live together.", 
    is_female=True, drunk_default=25)
    $ oskar = Npc(fname="Oskar", sname="Bergstrom", colour="#d0ffc4", skinbase=(0.964, 0.8, 0.756), skinshad=(0.949, 0.635, 0.533), bio_image="oskar", bio_group="flatmate",
    bio_text="The landlord of the flat The Institute set me up in.")
    $ oskar_thug = Npc(fname="Thug", sname="", colour="#da7a8a", pregname="I am carrying the child of one of the landlord's thugs", virginname="one of the landlords thugs", abort=True)


    $ tucker = Npc(fname="James", sname="Tucker", rank="Dr.", colour="#beffd9", bio_image="tucker", bio_group="institute",
    bio_text="He has been assigned by The Institute to oversee my rehabilitation into the wider world.\nI wonder what his motives are? He says he is just looking out for me, but I cannot see what benefit he or The Institute gets out of it.\nI suppose time will tell...")
    $ nik = Npc(fname="Ratan", sname="Nikolas", rank="Dr.", bio_image="nikolas", colour="#ffd4c0", bio_group="institute",
    bio_text="One of the first faces I saw when I woke up in The Institute following my near death, or actual death I suppose, experience.\n")
    $ nurse = Npc(fname="Sede", sname="Lilly", rank="Nurse", is_female=True, bio_image="nurse", colour="#c0f2ff", bio_group="institute",
    bio_text="One of the first faces I saw when I woke up in The Institute following my near death, or actual death I suppose, experience.\n")
    $ psy = Npc(fname="Tess", sname="Brooker", rank="Dr.", is_female=True, bio_image="brooker", colour="#d3c0ff", bio_group="institute",
    bio_text="The Psychologist assigned to me by The Institute to look after my mental health...")
    $ receptionist = Npc(fname="Krystal", sname="Apatite", nname="Receptionist", is_female=True, bio_image="receptionist", colour="#ffc0ff", bio_group="institute", isslut=True,
    bio_text="The receptionist at the front desk of the hospital.")

    $ ant = Npc(fname="Brandon", sname="Curse", rank="Dr.")


    $ cam = Npc(fname="Erik", sname="Campbell", rank="Chief", bio_group="police")
    $ miller = Npc(fname="Toby", sname="Miller", rank="Chief", bio_group="police")
    $ betty = Npc(fname="Betty", sname="Parson", rank="Sgt.", is_female=True, bio_group="police")
    $ paige = Npc(fname="Paige", sname="Williams", rank="P.C.", is_female=True, bio_image="paige", bio_group="police", colour="#c3bcff",
    bio_text="A rookie that usually works the reception at the security office. Hopes to do something more but is not very well respected by her colleages.")
    $ police = Npc(fname="Security agent", pregname="I am carrying the child of some random security agent", virginname="some random security agent", abort=True, is_unique=False)
    $ police1 = Npc(fname="Security agent 1", pregname="I am carrying the child of some random security agent", virginname="some random security agent", abort=True, is_unique=False)
    $ police2 = Npc(fname="Security agent 2", pregname="I am carrying the child of some random security agent", virginname="some random security agent", abort=True, is_unique=False)


    $ ali = Npc(fname="Alison", sname="Vassos", nname="Ali", is_female=True, bio_image="ali", bio_group="mechanic", stay_virgin=True, 
    bio_text="She works at the mechanics shop in the industrial area.")
    $ dez = Npc(fname="Dezydery", sname="Nowak", nname="Dez", bio_image="dez", bio_group="mechanic", 
    bio_text="The boss at the mecanics shop in the industrial area. A sleezy pervert and probably an alcoholic.")

    $ jaylee = Npc(fname="Jaylee", sname="Bright", nname="Jay", is_female=True, bio_image="jaylee", bio_group="mechanic", stay_virgin=True, 
    bio_text="A scavver that works at the junkyard.")
    $ ashon = Npc(fname="Ashon", sname="Bright", nname="Ash", bio_image="ashon", bio_group="mechanic", 
    bio_text="The manager of the junkyard.")




    $ svet = Npc(fname="Svetlana", sname="Makarava", nname="Svet", colour="#c1ecff", is_female=True, iswhore=True, bio_image="svet_layer happy", bio_group="dancet", 
    bio_text="She is the leader of the dance troupe at the acadamey.\nShe comes across as quite harsh but deep down she cares a lot for the girls she dances with.")

    $ rachel = Npc(fname="Rachel", sname="Taylor", colour="#f4c6ff", is_female=True, bio_image="rachel happy", bio_group="dancet", isslut=True, drunk_default=30,
    bio_text="One of the girls from the academy's dance troupe.\nShe seems to have never ending energy and really looks up to [svet.name]. I wonder if they have some kind of history?\nIt seems nothing in this shitty new world can keep the smile off her face, and even worse she almost seems to enjoy putting herself at risk.\nI am starting to think she might be a bit dangerous to be around.")

    $ anabel = Npc(fname="Anabel", sname="Desmond", nname="Ana", colour="#faffd0", is_female=True, bio_image="anabel happy", bio_group="dancet", stay_virgin=True,
    bio_text="One of the newer members of the acadamy's dance troup who joined alongside her close friend [dani.nname].\nShe seems a lot more righteous than you would expect around here, almost to a fault. I guess it has something to do with her ample assets bringing her a lot more attention than she would like.\nI am worried that if she doesn't get used to the new world we live in, it will leave her broken and bitter.")

    $ dani = Npc(fname="Danielle", sname="Rabel", nname="Dani", colour="#ffd3d3", is_female=True, bio_image="dani happy", bio_group="dancet", 
    virginname="I lost my virginity to Dani and her giant pink strapon.",
    bio_text="One of the newer members of the acadamy's dance troup who joined alongside her close friend [anabel.name].\nShe seems eager to make new friends and is fitting in well with the dance troupe. I get the impression though that she is in need of money more than most. ")

    $ drake = Npc(fname="Drake", sname="Singer", colour="#feffd3", skinbase=(0.929, 0.756, 0.670), skinshad=(0.886, 0.611, 0.498), bio_image="drake", bio_group="soccer",
    bio_text="One of the boys who are always hanging out at the academy's football field.\nHe is probably the most normal of the bunch and able to hold a normal conversation.")
    $ nate = Npc(fname="Nate", sname="Taylor", colour="#ffdcd3", skinbase=(0.901, 0.666, 0.576), skinshad=(0.827, 0.537, 0.458), bio_image="nate", bio_group="soccer",
    bio_text="One of the boys who are always hanging out at the academy's football field.\nHe is a total pervert and can barely even have a conversation with a girl without saying something stupid.")
    $ dan = Npc(fname="Dan", sname="Bloom", colour="#d3dfff", skinbase=(0.929, 0.725, 0.670), skinshad=(0.705, 0.537, 0.478), bio_image="dan", bio_group="soccer",
    bio_text="One of the boys who are always hanging out at the academy's football field.\nHe hardly ever talks so it can be hard to get to know him. Seems to be a pretty good guy though.")

    $ shane = Npc(fname="Shane", sname="Simmons", colour="#d3daff", skinbase=(0.901, 0.666, 0.572), skinshad=(0.831, 0.537, 0.454), bio_image="shane", bio_group="bully",
    bio_text="A cunt. Cunt cunt cunt cunt!\nAll he seems to do is make trouble for people.\nDid I mention he is a cunt?\nFucking cunt!", abort=True)
    $ marcus = Npc(fname="Marcus", sname="Andal", colour="#d7ffd3", skinbase=(0.752, 0.607, 0.549), skinshad=(0.682, 0.498, 0.447), bio_image="marcus", bio_group="bully",
    bio_text="Cunt's little boyfriend.\nFuck this arsehole too.\nHope they both end up in a shallow grave somewhere.", abort=True)
    $ josh = Npc(fname="Josh", sname="Orich")
    $ shanewhore = Npc(fname="Shane", sname="Simmons", pregname="I am carrying the child of someone who had sex with me while [shane.name] was selling me.", virginname="some guy who paid [shane.name] to make me have sex with him.", abort=True, is_unique=False)

    $ felix = Npc(fname="Felix", sname="Vincenzo", bio_group="academy", bio_image="felix", bio_text="Someone who runs the photography department at the academy.")

    $ cass = Npc(fname="Cassidy", sname="O'Reilly", nname="Cass", wname="Gingersnap", colour="#ffe5d3", is_female=True, bio_image="cass", bio_group="academy", bio_text="A girl I met on one of the first days of school.")
    $ mira = Npc(fname="Mira", sname="Bhatti", wname="Perra", colour="#d7d3ff", is_female=True, iswhore=True, bio_image="mira", bio_group="academy",
    bio_text="A girl I met on one of the first days of school.")

    $ schoolguy = Npc(fname="Guy", pregname="I am carrying the child of some random guy from school", virginname="some random guy from school", abort=True, is_unique=False)

    $ frida = Npc(fname="Frida", sname="Johansen", colour="#d3ffd3", is_female=True, bio_image="frida", bio_group="academy", isslut=True,
    bio_text="One of the Needle girls that repair and maintain clothes.")
    $ saskia = Npc(fname="Saskia", sname="Tamm", nname="Sassy", colour="#d3f6ff", is_female=True, bio_image="saskia", bio_group="academy", isslut=True,
    bio_text="One of the Needle girls that repair and maintain clothes.")

    $ mason = Npc(fname="Terry", sname="Mason", colour="#ad8181", skinbase=(0.898, 0.803, 0.760), skinshad=(0.827, 0.658, 0.639), bio_image="mason", bio_group="academy",
    bio_text="The volleyball coach at the academy.\nI don't really know much about him.")


    $ sandy = Npc(fname="Sandy", sname="Sparrow", colour="#ffd3f0", is_female=True, isslut=True, bio_image="sandy happy", bio_group="beach", 
    bio_text="A girl I met who works at a kiosk by the lakes boardwalk. She sells swimwear and makes jewelery out of seashells.")
    $ lake_dealer = Npc(fname="Shady guy", colour="#d4d3ff", skinbase=(0.984, 0.835, 0.760), skinshad=(0.905, 0.670, 0.580), pregname="I am carrying the child of the shady dealer from the lake", virginname="the shady drug dealer by the lake")
    $ mateo = Npc(fname="Mateo", sname="Garcia", colour="#d3eaff", skinbase=(0.902, 0.659, 0.608), skinshad=(0.745, 0.475, 0.443), bio_image="mateo", bio_group="beach",
    bio_text="A poser on the beach that sometimes plays volleyball. Though probably spends more time ogling the girls than actually playing.")
    $ kaan = Npc(fname="Kaan", sname="Demir", colour="#ffd8d3", skinbase=(0.725, 0.529, 0.463), skinshad=(0.631, 0.4, 0.341), bio_image="kaan", bio_group="beach",
    bio_text="A prettyboy who hangs out at the beach. Spends his days posing and his nights drinking.")
    $ erika = Npc(fname="Erika", sname="Schmidt", colour="#d3feff", love=0, bio_image="erika", bio_group="beach",
    bio_text="Likes to hang out by the lake playing volleyball and drinking.", is_female=True)
    $ zahra = Npc(fname="Zahra", sname="Adel", colour="#ffd3e4", love=0, bio_image="zahra", bio_group="beach",
    bio_text="Likes to hang out by the lake playing volleyball and drinking.", is_female=True)




    $ rose = Npc(fname="Samira", sname="Touati", nname="Rose bud", wname="Rose bud", colour="#ffd3f0", is_female=True, iswhore=True, bio_image="rose", bio_group="whore", 
    bio_text="One of the whores who works the highway.")
    $ charity = Npc(fname="Nilay", sname="Kaya", nname="Charity", wname="Charity", colour="#ffd3d3", is_female=True, iswhore=True, bio_image="charity", bio_group="whore", 
    bio_text="One of the whores who works the highway.")
    $ kitty = Npc(fname="Anita", sname="Amaya", nname="Kitty", wname="Kitty", colour="#dad3ff", is_female=True, iswhore=True, bio_image="kitty", bio_group="whore", 
    bio_text="One of the whores who works the highway.")
    $ pursy = Npc(fname="Vivian", sname="Walker", nname="Pursy", wname="Pursy", colour="#d3e5ff", is_female=True, iswhore=True, bio_image="pursy", bio_group="whore", 
    bio_text="One of the whores who works the highway.")


    $ simon = Npc(fname="Simon", sname="Banks", colour="#d7d3ff", skinbase=(0.988, 0.850, 0.772), skinshad=(0.956, 0.705, 0.564), bio_image="simon", bio_group="misc",
    bio_text="A private investigator I met while on a mission for The Institute.")
    $ bob = Npc(fname="Bob", sname="Cray", colour="#d3f6ff", skinbase=(0.803, 0.623, 0.560), skinshad=(0.564, 0.419, 0.396), bio_image="bob", bio_group="misc",
    bio_text="A rank and file worker at the hospital who spends most of their time at the pub. \nNot at all shocking to find out his marrage is on the rocks considering he is always drunk.")
    $ trixie = Npc(fname="Trixie", sname="Bell", nname="", colour="#ffd3e0", is_female=True, bio_image="trixie happy", bio_group="misc", iswhore=True,
    bio_text="A girl I met working at the bar. Very bubbly and speaks in a weird way.")
    $ alex = Npc(fname="Alex", sname="White", nname="Big Al", colour="#d6d3ff", )
    $ theo = Npc(fname="Theo", sname="Georgiou", colour="#d7d3ff", skinbase=(0.988, 0.850, 0.772), skinshad=(0.956, 0.705, 0.564), bio_image="theo", bio_group="misc",
    bio_text="A guy who arranges private parties for folk who have a bit more money than most.")

    $ fun_girl = Npc(fname="Salesgirl", sname="Funwear", colour="#fdbcff", is_female=True, iswhore=True)
    $ motel_recep = Npc(fname="Receptionist", sname="Motel", colour="#fdbcff", is_female=True)
    $ hucow = Npc(fname="Milkmaid", sname="Hucow", colour="#d6d5b9", is_female=True, iswhore=True)
    $ flyergirl = Npc(fname="Flyerer", sname="", colour="#b9c8d6", is_female=True, iswhore=True)
    $ salongirl = Npc(fname="Beautician", sname="", colour="#ec98ef", is_female=True, isslut=True)
    $ neighbour = Npc(fname="Violet", sname="Blunt", colour="#ec98ef", is_female=True, iswhore=True)


    $ pre_bf = Npc(fname="Boyfriend", sname="", nname="", pregname="", virginname="", is_unique=True)



    $ pubpatron = Npc(fname="Patron", sname="from the pub", pregname="I am carrying the child of some random guy from the pub", virginname="some random guy from the pub", colour="#c8ffc8", abort=True, is_unique=False)
    $ pubtoiletgang = Npc(fname="Patron", sname="from the pub", pregname="I am carrying the child of one of the guys that gang raped you while you were puking in the pub toilets", virginname="some random guy from the pub", colour="#c8ffc8", abort=True, is_unique=False)

    $ whore = Npc(fname="Whore", sname="", colour="#fdbcff", is_female=True, iswhore=True, is_unique=False)

    $ pinkroom_man = Npc(fname="Punter", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True, is_unique=False)
    $ pinkroom_man2 = Npc(fname="Customer", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True, is_unique=False)
    $ pinkroom_man3 = Npc(fname="Guy", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True, is_unique=False)

    $ pinkroom_tiedtrain = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me while I was tied up and men were taking turns fucking me", virginname="a pinkroom punter while I was tied up and taken turns on", abort=True, is_unique=False)
    $ pinkroom_group = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me as part of a pinkroom gangbang", virginname="a group of guys who gangbanged me", abort=True, is_unique=False)

    $ guy_tiedtrain = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me while I was tied up and men were taking turns fucking me", virginname="a guy while I was tied up and taken turns on", abort=True, is_unique=False)

    $ guy_gangbang = Npc(fname="Guy", sname="", pregname="I am carrying the child of someone from a gangbang", virginname="a guy from a gangbang", abort=True, is_unique=False)
    $ guy_gangbang_r = Npc(fname="Guy", sname="", pregname="I am carrying the child of one of the guys who gang raped me", virginname="a guy while I was gang raped", abort=True, is_unique=False)

    $ punter = Npc(fname="Punter", sname="", pregname="I am carrying the child of one of some punter", virginname="some random punter", abort=True, is_unique=False)
    $ highpayer = Npc(fname="Punter", sname="", pregname="I am carrying the child of one of some punter", virginname="some random punter", abort=True, is_unique=False)

    $ parkpervert_dani = Npc(fname="Pervert", sname="", pregname="I am carrying the child of a pervert in the park who I let fuck me in the bushes", virginname="some random pervert who fucked me in the bushes", abort=True, is_unique=False)
    $ busgroper = Npc(fname="Groper", sname="on the bus", pregname="I am carrying the child of a pervert from the bus", virginname="some random pervert who I let fuck me on the bus", abort=True, is_unique=False)
    $ ghman = Npc(fname="Gloryhole", sname="man", pregname="I am carrying the child of someone I had sex with at the gloryhole", virginname="Some gloryhole customer", abort=True, is_unique=False)

    $ wolf = Npc(fname="Wolfman", sname="", pregname="I was bred by someone from the wolfgang", virginname="Some wolfgang stud", abort=True, is_unique=False)

    $ streetpervert = Npc(fname="Pervert", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True, is_unique=False)
    $ streetguy = Npc(fname="Guy", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True, is_unique=False)
    $ streetman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True, is_unique=False)

    $ flyerman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True, is_unique=False)


    $ motelman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy from the motel", virginname="some random pervert from the motel", abort=True, is_unique=False)

    $ scavver = Npc(fname="Scavver", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)
    $ scavver2 = Npc(fname="Scavanger", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)
    $ scavver3 = Npc(fname="Scavving guy", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)

    $ muff = Character('Muffled voice', color="#ffffff")
    $ distvoice = Character('Distant voice', color="#ffffff")

    $ robinman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy I got wild with while hanging out with Robin", virginname="some guy while hanging out with Robin", abort=True, is_unique=False)
    $ robinpubmotel = Npc(fname="Patron", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)
    $ robinpubmotel2 = Npc(fname="Pub guy", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)
    $ robinpubmotel3 = Npc(fname="Boozer", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)

    $ mira_kidnapper= Npc(fname="Kidnapper", sname="", pregname="Text", virginname="text", abort=True, is_unique=False)

    $ clothesman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy who gave me clothes to cover myself up with", virginname="some random pervert who fucked me after I was caught naked", abort=True, is_unique=False)

    $ partyman = Npc(fname="Partygoer", sname="", pregname="I am carrying the child of one of the guys I had sex with at the dance party", virginname="one of the guys at the dance party", abort=True, is_unique=False)
    $ partyman2 = Npc(fname="Reveller", sname="", pregname="I am carrying the child of one of the guys I had sex with at the dance party", virginname="one of the guys at the dance party", abort=True, is_unique=False)


    $ tiedman_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)
    $ tiedman2_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)
    $ tiedman3_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)

    $ girl_dummy_1 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    $ girl_dummy_2 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    $ girl_dummy_3 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    $ girl_dummy_4 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    $ girl_dummy_5 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    $ girl_dummy_6 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)




    $ hav = Character('Haven resident', color="#ffffff")
    $ havguard = Character('Haven guard', color="#ffffff")
    $ havguard1 = Character('Haven guard 1', color="#ffffff")
    $ havguard2 = Character('Haven guard 2', color="#ffffff")
    $ havguard3 = Character('Haven guard 3', color="#ffffff")

    $ havmuff = Character('Muffled voice', color="#ffffff")
    $ havwhore = Character('Haven whore', color="#ffffff")
    $ havgirl = Character('Haven girl', color="#ffffff")

    $ havguardw = Character('Haven guard', color="#ffffff")


    image havguard = ("shadm")
    image havguard1 = ("shadm")
    image havguard2 = ("shadm")
    image havman = ("shadm")
    image havman2 = ("shadm")
    image havenman = ("shadm")

    $ havenman = Npc(fname="Haven", sname="resident", pregname="I am carrying the child of some random Haven resident", virginname="some random", is_unique=False)
    $ havenpeeper = Npc(fname="Haven", sname="peeper", pregname="I am carrying the child of the peeper from Haven", virginname="I gave my virginity to the Haven peeper.")

    $ havenvik = Npc(fname="Viktor", sname="the Brewmaster", pregname="I am carrying the child of Viktor, the Brewmaster in Haven who I let fuck me in exchange for some bottles of brew")

    $ havenpsleeper = Npc(fname="Haven", sname="peeper", pregname="I am carrying the child of someone who took advantage of me in Haven while I slept", virginname="My virginity was taken by someone who took advantage of me while I slept in Haven", is_unique=False)
    $ havenpsleepergang = Npc(fname="Haven", sname="peeper", pregname="I am carrying the child of one of the guys who gangbanged me in haven while I was drunk", virginname="My virginity was taken when I was gang raped in Haven while I was passed out drunk.", is_unique=False)
    $ havenpsleeperforce = Npc(fname="Haven", sname="peeper", pregname="I am carrying the child of someone who raped me in Haven while I was in bed", virginname="My virginity was taken when I was raped in Haven while in bed.", is_unique=False)

    $ havenvent = Npc(fname="Haven", sname="Vent", pregname="I am carrying the child of one of the people who raped me while I was stuck in a vent in Haven", virginname="My virginity was taken while I was stuck in a vent and gang raped in Haven.", is_unique=False)

    $ havenblackmail = Npc(fname="Haven", sname="Blackmailer", pregname="I am carrying the child of someone from Haven who blackmailed me into fucking him after he caught me stealing.", virginname="My virginity was taken by someone in Haven after being caught stealing and being blackmailed into fucking him.", is_unique=False)

    $ havenguardgb = Npc(fname="Haven", sname="Guard", pregname="I am carrying the child of one of the guards from Haven from when they had group sex with me.", virginname="My virginity was taken while I was passed around and gang fucked by the guards in Haven.", is_unique=False)
    $ havengateguard = Npc(fname="Gate guard", sname="from Haven", pregname="I am carrying the child of the gate guard from Haven.", virginname="I gave my virginity to the gate guard in Haven.")
    $ havenmeanguard = Npc(fname="Mean guard", sname="from Haven", pregname="I am carrying the child of one of the guards from Haven.", virginname="I gave my virginity to one of the guards in Haven.")

    $ haventrainer = Npc(fname="Trainer", sname="client", pregname="I am carrying the child of the man in charge of training me.", virginname="y virginity was taken while I was being trained as a sex slave.", is_unique=False)
    $ havenbrothel = Npc(fname="Brothel", sname="client", pregname="I am carrying the child of someone who had sex with me while I was trapped in the underground brothel.", virginname="some random", is_unique=False)








    $ anon = Npc(fname="Unknown voice", is_unique=False)

    $ unknown = Npc(fname="Unknown guy", pregname="some unknown guy", abort=True, is_unique=False)
    $ rapist = Npc(fname="Rapist", pregname="some filthy rapist", abort=True, is_unique=False)
    $ lover = Npc(fname="Lover", pregname="", is_unique=False)

    $ tempname = unknown
    $ tempname2 = unknown
    $ tempname3 = unknown



    python:
        for i in npc_girls:
            i.pregnant_who = nosex

    $ add_to_list(diary_people_list, [emile, nik, tucker])
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
