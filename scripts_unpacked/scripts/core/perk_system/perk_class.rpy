init python:
    class PerkClass(object):
        def __init__(
            self,
            name,
            desc,
            image,
            desc_extra=None, 
            diff=None, 
            allure_add=None,
            fertility_multi=None,
            desire_min=None,
            desire_max=None,
            desire_add=None,
            desire_multi=None,
            desire_multineg=None,
            mood_min=None,
            mood_max=None,
            mood_add=None,
            mood_multi=None,
            mood_multineg=None,
            tired_min=None,
            tired_max=None,
            tired_add=None,
            tired_multi=None,
            tired_multineg=None,
            confidence_min=None,
            confidence_max=None,
            confidence_add=None,
            confidence_multi=None,
            confidence_multineg=None,
            fitness_min=None,
            fitness_max=None,
            fitness_add=None,
            fitness_multi=None,
            fitness_multineg=None,
            int_min=None,
            int_max=None,
            int_add=None,
            int_multi=None,
            int_multineg=None,
            victim=False,
            not_victim=False,
            wildcard=False

        ):
            
            
            
            
            
            self.name = name
            self.desc = desc
            self.image = image
            self.diff = diff
            self.desc_extra = desc_extra
            
            self.allure_add = allure_add
            self.fertility_multi = fertility_multi
            
            self.desire_min = desire_min
            self.desire_max = desire_max
            self.desire_add = desire_add
            self.desire_multi = desire_multi
            self.desire_multineg = desire_multineg
            
            self.mood_min = mood_min
            self.mood_max = mood_max
            self.mood_add = mood_add
            self.mood_multi = mood_multi
            self.mood_multineg = mood_multineg
            
            self.tired_min = tired_min
            self.tired_max = tired_max
            self.tired_add = tired_add
            self.tired_multi = tired_multi
            self.tired_multineg = tired_multineg
            
            self.confidence_min = confidence_min
            self.confidence_max = confidence_max
            self.confidence_add = confidence_add
            self.confidence_multi = confidence_multi
            self.confidence_multineg = confidence_multineg
            
            self.fitness_min = fitness_min
            self.fitness_max = fitness_max
            self.fitness_add = fitness_add
            self.fitness_multi = fitness_multi
            self.fitness_multineg = fitness_multineg
            
            self.int_min = int_min
            self.int_max = int_max
            self.int_add = int_add
            self.int_multi = int_multi
            self.int_multineg = int_multineg
            
            self.victim = victim
            self.not_victim = not_victim
            self.wildcard = wildcard
            self.mins = None 
            self.hours = None 
            self.days = None 
            self.dict = {}
            self.list = []
            add_to_list(perk_list, self)
            if self.wildcard:
                add_to_list(perk_wildcard_list, self)


    def perk_choice_name():
        if selected_perk == None:
            return "", "", "", 1
        else:
            return selected_perk.name or "", selected_perk.desc or "", selected_perk.desc_extra or "", selected_perk.diff or 1

    def options_choice_name(text=""):
        return text

    def perk_commando_wardrobe_update():
        
        for i in wardrobe.inv[:]:
            if i[0].type == "bra" or i[0].type == "pants":
                wardrobe.drop(i[0], 100)
        for i in [c,school,daily,party,sport,home,work,shop]:
            i.pants = 0
            i.bra = 0

    def perk_bimbo_queue():
        if not "int_queue" in perk_bimbo.dict:
            perk_bimbo.dict["int_queue"] = []
        while len(perk_bimbo.dict["int_queue"]) >= 15:
            perk_bimbo.dict["int_queue"].pop()
        perk_bimbo.dict["int_queue"].insert(0,player.int)
    def perk_bimbo_qualify_checker():
        if not "int_queue" in perk_bimbo.dict:
            return 
        if player.has_perk([perk_princess, perk_nerd, perk_bimbo]):
            
            return False
        if len(perk_bimbo.dict["int_queue"]) == 15 and sum(i < 10 for i in perk_bimbo.dict["int_queue"]) >= 15:
            return True
        else:
            return False

    def perk_exhibitionist_homewear_update():
        
        for i in item_clothes_list[:]:
            if "home" in i.outfit:
                remove_from_list(i.outfit, "home")

    def perk_commando_queue():
        if not "commando_queue" in perk_commando.dict:
            perk_commando.dict["commando_queue"] = []
        if any(clothes in ["swim", "home", "work"] for clothes in tab_top):
            return
        if (t.hour % 3) == 0:
            while len(perk_commando.dict["commando_queue"]) >= 30:
                perk_commando.dict["commando_queue"].pop()
            if not player.has_perk(perk_commando):
                perk_commando.dict["commando_queue"].insert(0,If(not c.pants, True, False))
            else:
                perk_commando.dict["commando_queue"].insert(0,If(not c.pants or (c.pants and (c.pantsless or c.thong)), True, False))
    def perk_commando_qualify_checker():
        if sum(i == True for i in perk_commando.dict["commando_queue"]) >= 25 and not player.has_perk(perk_commando) and len(perk_commando.dict["commando_queue"]) == 30:
            return True
        else:
            return False
    def perk_commando_loose_checker():
        if sum(i == True for i in perk_commando.dict["commando_queue"]) <= 10 and player.has_perk(perk_commando) and len(perk_commando.dict["commando_queue"]) == 30:
            return True
        else:
            return False

    def perk_exhib_counter():
        if not "exhib_counter" in perk_exhibitionist.dict:
            perk_exhibitionist.dict["exhib_counter"] = 0
        if not "exhib_event_trigger" in perk_exhibitionist.dict:
            perk_exhibitionist.dict["exhib_event_trigger"] = 0
        
        if loc_cur.population >= 2 or npc_any_here():
            amount = 5 - min([c.cansee_ass_clothes_check(), c.cansee_vag_clothes_check(), c.cansee_breasts_clothes_check()])
            perk_exhibitionist.dict["exhib_counter"] += amount / 2
        elif loc_cur.population:
            amount = 5 - min([c.cansee_ass_clothes_check(), c.cansee_vag_clothes_check(), c.cansee_breasts_clothes_check()])
            if amount and not numgen(0,5):
                perk_exhibitionist.dict["exhib_counter"] += 1

    def perk_exhib_total_value():
        total_exhibitionist_value = perk_exhibitionist.dict["exhib_counter"]
        if player.has_perk(perk_exhibitionist):
            total_exhibitionist_value += 400
        for i in [perk_bambi, perk_meek, perk_fresh, perk_virgin]:
            if player.has_perk(i):
                total_exhibitionist_value -= 100
        for i in [perk_party_girl, perk_bimbo, perk_wildcard, perk_despondent, perk_blackout, perk_wasted, perk_freeuse, perk_sucu, perk_broken]:
            if player.has_perk(i):
                total_exhibitionist_value += 50
        
        if not player.has_perk(perk_exhibitionist) and total_exhibitionist_value > 400:
            total_exhibitionist_value = 400
        
        return total_exhibitionist_value

    def perk_exhib_weight(value):
        
        total_exhibitionist_value = perk_exhib_total_value()
        
        if total_exhibitionist_value > 600:
            return 100 if value == 6 else 0
        if total_exhibitionist_value < 50:
            return 100 if value == 0 else 0
        
        
        threshold = round (total_exhibitionist_value / 100.0, 2)
        
        if value > threshold + 1 or value < threshold - 1:
            return 0
        
        
        
        
        weight_upper = math.modf(total_exhibitionist_value/100.0 - 0.50)[0]
        
        if value >= threshold:
            return int(round(weight_upper * 100.0, 2))
        
        
        return int(min(100, round((1 - weight_upper) * 100.0, 2)))

    def perk_lactating_buildup():
        
        if not "milk_amount" in perk_lactating.dict:
            perk_lactating.dict["milk_amount"] = 0
        
        if perk_lactating.dict["milk_amount"] < 0:
            perk_lactating.dict["milk_amount"] = 0
        
        perk_lactating.dict["milk_amount"] += 2
        
        if perk_lactating.dict["milk_amount"] > 20:
            perk_lactating.dict["milk_amount"] = 20
        
        if perk_lactating.dict["milk_amount"] >= 15:
            player.add_perk(perk_milky)

    def perk_lactating_milk(amount=1):
        if not "milk_amount" in perk_lactating.dict:
            perk_lactating.dict["milk_amount"] = 0
        if not player.has_perk(perk_lactating, perk_milky):
            return
        
        perk_lactating.dict["milk_amount"] -= amount 
        if perk_lactating.dict["milk_amount"] < 10:
            
            player.remove_perk(perk_milky)

    def perk_lactating_queue():
        if not "fullmilk_queue" in perk_lactating.dict:
            perk_lactating.dict["fullmilk_queue"] = []
        
        if not player.has_perk(perk_lactating) or player.pregnant:
            return
        
        if (t.hour % 3) == 0:
            if len(perk_lactating.dict["fullmilk_queue"]) >= 20:
                perk_lactating_end()
            
            elif player.milky:
                perk_lactating.dict["fullmilk_queue"].insert(0,"True")
            else:
                perk_lactating.dict["fullmilk_queue"] = []

    def perk_lactating_tick():
        
        
        if player.has_perk(perk_lactating):
            perk_lactating_buildup()
            perk_lactating_queue()

    def perk_lactating_end():
        perk_lactating.dict["fullmilk_queue"] = []
        player.remove_perk(perk_milky)
        player.remove_perk(perk_lactating)

screen perk_choice_button(perk):
    $ colour = wardrobe_colour_selected
    frame padding (0,0) xysize (82,80) background None:
        add "button_wardrobe_tab_bg"
        add perk.image:
            if selected_perk != perk:
                matrixcolor TintMatrix(wardrobe_colour_selected)

        imagebutton auto "button_wardrobe_tab_frame_%s":
            hovered SetVariable("selected_perk", perk)
            action [Function(player.add_perk, perk), SetVariable("player.origin_perk", perk), Return()]

screen perk_choice(choices=[]):
    if perk_choice_name()[3] == 1:
        $ diff = "(Easy)"
    elif perk_choice_name()[3] == 2:
        $ diff = "(Normal)"
    elif perk_choice_name()[3] == 3:
        $ diff = "(Hard)"
    elif perk_choice_name()[3] == 4:
        $ diff = "(Very hard)"
    elif perk_choice_name()[3] == 5:
        $ diff = "(Very hard)"
    else:
        $ diff = ""

    $ choices = sorted(choices, key=lambda perk: perk.name)
    $ choices = sorted(choices, key=lambda perk: perk.diff)
    text perk_choice_name()[0] + " " + diff align (0.5,0.20) size 60 font "BRLNSB.TTF"
    vbox align (0.5,0.38) xysize (1200, 300):

        text perk_choice_name()[1] + "\n" + perk_choice_name()[2] size 24 text_align 0.5 align (0.5,0.0)

    hbox align (0.5,0.4) anchor (0.5, 0.5):
        for i in choices:
            if i == perk_waif:
                text "  "
            use perk_choice_button(i)
            if i == perk_waif:
                text "  "

image perk_cherry_taken = "perk_cherry"
image perk_cherry_sold = "perk_cherry"

image perk_tipsy = "perk_drunk"
image perk_wasted = "perk_drunk"
image perk_blackout = "perk_drunk"

image perk_branded_forehead = "perk_branded"
image perk_branded_face = "perk_branded"
image perk_branded_chest = "perk_branded"
image perk_branded_belly = "perk_branded"
image perk_branded_pubic = "perk_branded"
image perk_branded_pubic = "perk_branded"
image perk_branded_anus = "perk_branded"
image perk_branded_ass = "perk_branded"
image perk_branded_lleg = "perk_branded"

image perk_tech_virgin = "perk_virgin"
image perk_pure_virgin = "perk_virgin"

image perk_pregnant_0 = "perk_pregnant"
image perk_pregnant_1 = "perk_pregnant"
image perk_pregnant_2 = "perk_pregnant"
image perk_pregnant_3 = "perk_pregnant"

image perk_makeup = "button_wardrobe_tab_makeup"
image perk_beaten = "perk_bruised"

image perk_map = "perk_hangover"
image perk_smoking = "perk_smoker"

image perk_unwanted_preg = "perk_preg_notwant"
image perk_wanted_preg = "perk_preg_want"

image perk_gagged_locked = "perk_gagged"

image perk_drinking_beer_1 = "perk_drinking"
image perk_drinking_beer_2 = "perk_drinking"
image perk_drinking_beerbottle_1 = "perk_drinking"
image perk_drinking_beerbottle_2 = "perk_drinking"
image perk_drinking_wine_1 = "perk_drinking"
image perk_drinking_wine_2 = "perk_drinking"
image perk_drinking_wine_3 = "perk_drinking"
image perk_drinking_wine_4 = "perk_drinking"
image perk_drinking_brew_1 = "perk_drinking"
image perk_drinking_brew_2 = "perk_drinking"


label perks_call:
    $ perk_list = []
    $ perk_wildcard_list = []
    $ perk_virgin = PerkClass("Virgin", "I have never had sex and consider myself a virgin. This should make it easier for me to resist any temptations. I hope...", "perk_virgin", desire_max= -50)
    $ perk_tech_virgin = PerkClass("Technical virgin", "I have never had sex and consider myself a virgin... Although I have taken it in the bum.", "perk_tech_virgin")
    $ perk_fresh = PerkClass("Fresh start", "My body is brand new and is feeling good. Any activities I do will be a bit easier so I should workout or study as much as I can.", "perk_fresh", confidence_multi=1.2, fitness_multi=1.5, int_multi=2.0)

    $ perk_pure_virgin = PerkClass("Pure virgin", "I am committed to staying a virgin and keeping myself pure.", "perk_pure_virgin", desire_max= -100, confidence_min=10)
    $ perk_broken_virgin = PerkClass("Broken Virgin", "I once considered myself a pure virgin, but that was taken from me. Now I am used and worthless. My confidence and mood is shot and I am always horny.", "perk_broken_virgin", confidence_max=-30, desire_min=200, desire_max=600, mood_max=-40)

    $ perk_whore = PerkClass("Whore", "I have become adjusted to selling myself so much that I no longer shy away from the name \"Whore\". I will never get upset or feel unconfident when I agree to sell myself.", "perk_whore", confidence_min=10, desire_max=100, wildcard=True)
    $ perk_slut = PerkClass("Slut", "I have plenty of fun with men as I please. People call me a slut but I don't care any more. It doesn't matter what someone offers, I can agree to it.", "perk_slut", confidence_min=10, desire_min=30, desire_max=200, wildcard=True)
    $ perk_sucu = PerkClass("Sleeplessness", "This new body is weird. I can't seem to get any proper sleep. I wonder if there are other ways to boost my energy?", "perk_sucu", confidence_max=20, desire_max=300, fitness_min=20, tired_multi=0.05, fertility_multi=0.05)
    $ perk_broken = PerkClass("Broken", "I have been trained, used and abused beyond the point where I see any value in myself. I do as I am told.", "perk_broken", confidence_max=-60, desire_max=200, victim=True)
    $ perk_freeuse = PerkClass("Free use", "I have decided to be free use. I will never turn down offers for sex and will never accept money for it.", "perk_freeuse", confidence_add=20, desire_max=400, allure_add=100)
    $ perk_recovering = PerkClass("Recovering", "I am recovering from a recent trauma and feel like total shit. My mood, confidence and desire is in the toilet.", "perk_recovering", confidence_max=-20, desire_max=-1000, mood_max=-40)
    $ perk_numb = PerkClass("Numb to the world", "I have seen and experienced the horrors of the world and nothing phases me any more.", "perk_numb")
    $ perk_lightweight = PerkClass("Lightweight drinker", "Drinking almost anything damn near puts me on my back.", "perk_lightweight")
    $ perk_commando = PerkClass("Commando", "I utterly hate wearing underwear! It chafes and is annoying. Unless they are sexy of course.", "perk_commando", allure_add=50, confidence_min=5, mood_multi=1.2, wildcard=True)
    $ perk_creampie_lover = PerkClass("Creampie lover", "I love it when a guy finishes inside. I will never ask him to pull out and never ask for anal.", "perk_creampie_lover", wildcard=True)
    $ perk_buttslut = PerkClass("Buttslut", "I love it in the ass. I will always ask for it up the bum and love it when they cum inside.", "perk_buttslut", wildcard=True)
    $ perk_cherry = PerkClass("Popped cherry", "I recently had sex for the first time and feeling pretty great about myself.", "perk_cherry", allure_add=30, mood_add=20)
    $ perk_cherry_taken = PerkClass("Cherry taken", "I had my first time taken from me and am feeling pretty shit about it.", "perk_cherry_taken", mood_add=-20, mood_min=-30)
    $ perk_cherry_sold = PerkClass("Cherry sold", "I had sex for the first time in exchange for money and am feeling pretty bad about it.", "perk_cherry", mood_add=-10, mood_min=-30)

    $ perk_tipsy = PerkClass("Tipsy", "I am starting to feel the booze.", "perk_tipsy", desire_multi=1.5, desire_max=15, confidence_add=5, tired_add=15)
    $ perk_drunk = PerkClass("Drunk", "Oooh this feels good.", "perk_drunk", desire_multi=1.5, desire_max=25, confidence_add=10, int_add=-10, fitness_add=-10, tired_add=20)
    $ perk_wasted = PerkClass("Wasted", "I... *Ubbb*.", "perk_wasted", desire_multi=2.0, desire_max=40, confidence_add=10, int_add=-20, fitness_add=-15, tired_add=15, victim=True)
    $ perk_blackout = PerkClass("Blackout drunk", "##############.", "perk_blackout", desire_multi=1.5, desire_max=40, confidence_add=10, int_add=-50, fitness_add=-15, tired_add=-15, victim=True)

    $ perk_drinking_beer_1 = PerkClass("Drinking beer", "Mmmm, beer.", "perk_drinking_beer_1")
    $ perk_drinking_beer_2 = PerkClass("Drinking beer", "Mmmm, beer.", "perk_drinking_beer_2")

    $ perk_drinking_beerbottle_1 = PerkClass("Drinking beer", "Mmmm, beer.", "perk_drinking_beerbottle_1")
    $ perk_drinking_beerbottle_2 = PerkClass("Drinking beer", "Mmmm, beer.", "perk_drinking_beerbottle_2")

    $ perk_drinking_wine_1 = PerkClass("Drinking wine", "Mmmm, wine.", "perk_drinking_wine_1")
    $ perk_drinking_wine_2 = PerkClass("Drinking wine", "Mmmm, wine.", "perk_drinking_wine_2")
    $ perk_drinking_wine_3 = PerkClass("Drinking wine", "Mmmm, wine.", "perk_drinking_wine_3")
    $ perk_drinking_wine_4 = PerkClass("Drinking wine", "Mmmm, wine.", "perk_drinking_wine_4")

    $ perk_drinking_brew_1 = PerkClass("Drinking a brew", "Mmmm, disgusting.", "perk_drinking_brew_1")
    $ perk_drinking_brew_2 = PerkClass("Drinking a brew", "Mmmm, disgusting.", "perk_drinking_brew_2")


    $ perk_alcoholic = PerkClass("Alcoholic", "I can't live without booze. If anyone is offering, I will agree.", "perk_alcoholic", int_max=-20)
    $ perk_smoker = PerkClass("Smoker", "I really do enjoy having a smoke.", "perk_smoker")
    $ perk_smoking = PerkClass("Smoking", "I am having a cig.", "perk_smoking")
    $ perk_hangover = PerkClass("Hangover", "Ugh, I drunk waay too much and my head is killing me.", "perk_hangover", mood_add=-20, int_add=-5, fitness_add=-5, tired_add=-5)

    $ perk_joy = PerkClass("On Joy", "I feel so good. Fucking good. JOY!", "perk_joy", mood_max=100, mood_multi=2.0)
    $ perk_joy_addict = PerkClass("Joy addict", "I need Joy to be happy!", "perk_joy_addict", mood_max=-60, mood_multineg=5.0, mood_min=-20)

    $ perk_lebo = PerkClass("On Lebo", "This stuff is making me go wild!", "perk_lebo", desire_max=300, desire_multi=10.0, victim=True)
    $ perk_wakeup = PerkClass("On Wakeup", "This stuff gives me loads of energy!", "perk_wakeup")
    $ perk_wakeup_comedown = PerkClass("Coming down", "Ugh, shit! I need more Wakeup or Im gonna pass out", "perk_wakeup_comedown", tired_multineg=3, mood_min=-50)

    $ perk_branded_forehead = PerkClass("Branded whore", "I have a brand on my forehead advertising myself as a whore. Doesn't matter if I am one or not, people will still think I am up for sale.", "perk_branded_forehead", allure_add=30)
    $ perk_branded_face = PerkClass("Branded slut", "I have a brand on my cheek that tells everyone I am a slut. Doesn't matter if I am one or not, people will still think I am an easy lay.", "perk_branded_face", allure_add=30)
    $ perk_branded_chest = PerkClass("Branded cow", "I have a brand on my chest telling people I want to be milked. Moooo.", "perk_branded_chest", desire_min=40, allure_add=20)
    $ perk_branded_belly = PerkClass("Branded breeder", "I have a brand on my belly telling everyone I want to be knocked up. No way anyone will listen to me if I ask them to pull out.", "perk_branded_belly", desire_min=20, allure_add=10, fertility_multi=2)
    $ perk_branded_pubic = PerkClass("Branded creampie lover", "I have a brand on my pubis telling everyone to fill me up. This may be risky...", "perk_branded_pubic", desire_min=20)
    $ perk_branded_anus = PerkClass("Branded anal queen", "I have a brand on my ass cheek telling people who see it I want to be fucked in the ass.", "perk_branded_anus", desire_min=10)
    $ perk_branded_ass = PerkClass("Branded sex counter", "I have a running tally on my ass cheek to keep count of all the men I have had sex with.", "perk_branded_ass", desire_min=10)
    $ perk_branded_lleg = PerkClass("Branded fuck me instructions", "Though fairy hidden, I have instructions to anyone who sees it to try and fuck me.", "perk_branded_lleg", desire_min=10, allure_add=30)

    $ perk_buttplug = PerkClass("Plugged", "I have a plug in my ass. Makes it harder to move, but feels so good.", "perk_buttplug", desire_min=50, desire_max=150, fitness_add=-5)
    $ perk_gagged = PerkClass("Gagged", "Mmmmff nnnngggfff aaahhh ffffmmmmm...", "perk_gagged", desire_min=150, desire_max=300, allure_add=200, int_max=-200, int_add=-200, victim=True)
    $ perk_gagged_locked = PerkClass("Gagged", "Mmmmff nnnngggfff aaahhh ffffmmmmm...", "perk_gagged_locked", desire_min=150, desire_max=300, allure_add=200, int_max=-200, int_add=-200, confidence_add=-30, victim=True)
    $ perk_blind = PerkClass("Blindfolded", "I can't see a thing!", "perk_blind", confidence_add= -100, fitness_add= -100, victim=True)

    $ perk_slutty = PerkClass("Looking slutty", "I am dressed in a really revealing way. People no doubt think I am a slut.", "perk_slutty", desire_min=50, desire_max=150, confidence_add=5, allure_add=50)
    $ perk_pervert = PerkClass("Perverted", "I look like a pervert.", "perk_pervert", desire_min=50, desire_max=150, confidence_add=-5, allure_add=50, victim=True)
    $ perk_bitch = PerkClass("Bitch", "I am wearing clothes that indicate to those calling themselves \"the wolf pack\" that I am playing their game.", "perk_bitch", desire_min=50, desire_max=150, confidence_add=5, allure_add=50, victim=True)

    $ perk_preg_want = PerkClass("Baby crazy", "I am obsessed with getting pregnant. Hope it happens soon.", "perk_preg_want", fertility_multi=1.2)
    $ perk_preg_notwant = PerkClass("Child free", "I would do almost anything to make sure I do not have to carry a baby in me.", "perk_preg_notwant", fertility_multi=0.8)
    $ perk_pregband_preg = PerkClass("Belly support", "Ahh, so much better on my back.", "perk_pregband", confidence_add=5, mood_add=10)
    $ perk_pregband_notpreg = PerkClass("Belly support", "Ahh, so much better on my back.", "perk_pregband", fitness_add=5)

    $ perk_lactating = PerkClass("Lactating", "I am lactating.", "perk_lactating", fertility_multi=0.5)
    $ perk_milky = PerkClass("Milky", "My breasts are full of milk. I really need to do something about that.", "perk_milky", mood_add=-5, allure_add=50)

    $ perk_makeup = PerkClass("All made up", "I put some makeup on and am feeling good.", "perk_makeup", confidence_add=3, allure_add=10)
    $ perk_spanked_ass = PerkClass("Spanked ass", "I have a seriously red ass. Feels nice though.", "perk_spanked_ass", desire_multi=1.5, fitness_multi=0.9, mood_add=5)
    $ perk_cumstain = PerkClass("Cum stained", "People can see \"something\" on me making me look repulsive. No one will be attracted to me like this.", "perk_cumstain", mood_add=-20, mood_min=-30, allure_add=-500, victim=True)
    $ perk_dirty = PerkClass("Stinky", "Phew! I stink! No one will come near me until I clean myself up.", "perk_dirty", mood_add=-5, mood_min=-10, allure_add=-500)
    $ perk_upset = PerkClass("Upset", "I am not really feeling too nice", "perk_upset", mood_add=-10, mood_min=-100, mood_max=-20)
    $ perk_despondent = PerkClass("Despondent", "I really need to do something to pick me up.", "perk_despondent", mood_multi=2, desire_max= -400, allure_add= 400, victim=True)
    $ perk_map = PerkClass("Took plan B", "Ugh, this stuff is really kicking my ass", "perk_map", mood_add=-10, mood_min=-100, mood_max=-20)
    $ perk_recovering = PerkClass("Recovering", "I am recovering from trauma and feeling all sore and really shitty.", "perk_recovering", desire_max= -1000, mood_max= -50, mood_min=-30, allure_add= -100)
    $ perk_bruised = PerkClass("Bruised", "I have taken some hits and am feeling it.", "perk_bruised", mood_max= -20, mood_min=-20)
    $ perk_beaten = PerkClass("Black and blue", "My body feels like I fell off a cliff. Fuck it hurts all over.", "perk_beaten", desire_max= -30, mood_max= -40, mood_min=-50, allure_add= -50)

    $ perk_period = PerkClass("Menstruating", "It is that time of the month...", "perk_period", mood_min=-20, allure_add=-25, fertility_multi=-5)
    $ perk_period_late = PerkClass("Late period", "It is that time of the month... So why is nothing happening?", "perk_period_late")
    $ perk_ovulating = PerkClass("Ovulating", "It's the time of the month where unprotected sex is most dangerous.", "perk_ovulating", allure_add=25, fertility_multi=2)
    $ perk_pregnant_0 = PerkClass("Pregnant", "I am pregnant", "perk_pregnant_0")
    $ perk_pregnant_1 = PerkClass("Mildly pregnant", "I am pregnant and starting to show.", "perk_pregnant_1", fitness_multi=0.7, fitness_max=-10, fitness_min=-200)
    $ perk_pregnant_2 = PerkClass("Heavily pregnant", "I am pregnant and and completely unable to hide it. I have a huge belly.", "perk_pregnant_2", fitness_multi=0.5, fitness_max=-50, fitness_min=-200, allure_add=50)
    $ perk_pregnant_3 = PerkClass("About to pop", "I am pregnant and feel like a bus. It won't be long before I am ready to give birth.", "perk_pregnant_3", fitness_multi=0.1, fitness_max=-80, fitness_min=-200, allure_add=100)
    $ perk_inseminated = PerkClass("Inseminated", "I have recently had sex and it might have been dangerous.", "perk_inseminated")

    $ perk_unwanted_preg = PerkClass("Unwanted pregnancy", "I am pregnant but would rather not be.", "perk_unwanted_preg", mood_min=-50)
    $ perk_wanted_preg = PerkClass("Happily pregnant", "I am pregnant and happy about it.", "perk_wanted_preg")

    $ perk_exhibitionist = PerkClass("Exhibitionist", "Showing off my body gives me a huge thrill. People seeing me naked makes me really happy.", "perk_exhibitionist", wildcard=True)
    $ perk_slim = PerkClass("Great metabolism", "I always look like I am in shape, even when I am not.", "perk_slim")


    $ perk_waif = PerkClass("Waif", "There is nothing special at all about me. On the plus side, nothing bad either.", "perk_waif", diff=2, desc_extra="Comes with nothing good or bad.")
    $ perk_nerd = PerkClass("Nerd", "I have always been academically gifted. Any studying I do will lead to greater results, but my fitness has suffered because of it.", "perk_nerd", diff=2, desc_extra="Bonuses to gaining intelligence and speech/charisma checks.", int_min=20, fitness_max=-20, int_multi=1.5, fitness_multi=0.5, wildcard=True)
    $ perk_gym_bunny = PerkClass("Gym bunny", "I have always been into fitness. Any working out I do will lead to greater results, but my academic ability has suffered.", "perk_gym_bunny", diff=2, desc_extra="Bonuses to fitness gain and any fitness related checks.", fitness_min=20, int_max=-20, int_multi=0.5, fitness_multi=1.5, wildcard=True)
    $ perk_bimbo = PerkClass("Bimbo", "Err, like, yeah. Like I need to be smart when I am the sexiest person in the room and always happy.", "perk_bimbo", diff=1, desc_extra="Extra bouses to mood and confidence. Caps intelligence to a very low level.", allure_add=50, desire_max=50, int_max=-60, int_multi=0.2, confidence_min=10, mood_min=15, mood_multi=2.0, wildcard=True)
    $ perk_gamine = PerkClass("Gamine", "I already understand how this world works as it was not much different than how I lived before.", "perk_gamine", diff=1, desc_extra="Comes with the whore perk and bonus to confidence.", confidence_multi=2.0, confidence_min=10, mood_multi=0.8, wildcard=True, not_victim=True)
    $ perk_bambi = PerkClass("Bambi", "I am really fucking struggling in this new world. This place terrifies me.", "perk_bambi", diff=3, desc_extra="Low mood and double effect of alcohol. Will rarely stand up for herself.", confidence_min=-100, confidence_max=-70, mood_min=-50, mood_multi=0.75, allure_add=150, desire_max=-200, wildcard=True, victim=True)

    $ perk_broodmother = PerkClass("Broodmother", "Any time I am alone with a man, I am usually left with something in my belly. Just walking past one is almost enough to get me pregnant.", "perk_broodmother", diff=2, desc_extra="Huge fertility bonus and will actively try to get pregnant.", fertility_multi=3.0, wildcard=True)
    $ perk_wildcard = PerkClass("Wildcard", "How can anyone else claim to know what I am thinking when I don't even know?", "perk_wildcard", diff=2, desc_extra="Will randomly pass checks based on perks you do not have. Silly mode.")

    $ perk_party_girl = PerkClass("Party girl", "I am always up for some fun and it doesn't matter what kind.", "perk_party_girl", diff=1, desc_extra="Slut and alcoholic perks. Small mood and confidence bonus, small malus everywhere else.", int_max=-20,  int_multi=0.8, fitness_multi=0.8, confidence_multi=1.5, mood_multi=1.2, wildcard=True)
    $ perk_meek = PerkClass("Meek", "I have absoloutly no confidence in myself and will do almost anything anyone asks of me.", "perk_meek", diff=4, desc_extra="Malus to virtually every stat. Will never reject someone that want's something from her.", confidence_multi=0.2, allure_add=150, mood_multineg=1.5, mood_multi=0.7, fitness_multi=0.8, wildcard=True, victim=True)

    $ perk_addict = PerkClass("Addict", "I take to substances too well. I love everything and they love me.", "perk_addict", diff=4, desc_extra="Has an addiction to almost everything and malus to every stat.", confidence_multi=0.8, allure_add=-100, mood_multineg=1.2, mood_multi=0.7, fitness_multi=0.8, int_multi=0.5, wildcard=True, victim=True)
    $ perk_princess = PerkClass("Princess", "I lived a pampered life, Confident in myself without much backing it up. Prone to mood swings.", "perk_princess", diff=3, desc_extra="Mood will gain and loss at a huge rate. Very difficult to train stats.", confidence_multi=3.0, confidence_multineg=3.0, allure_add=150, mood_multi=3.0, mood_multineg=3.0, fitness_multi=0.3, int_multi=0.3, wildcard=True)
    $ perk_deadinside = PerkClass("Dead inside", "Life is shit no matter how you look at it. I am barely coasting by.", "perk_deadinside", diff=2, desc_extra="Depressed character", confidence_max=-70, confidence_min=10, mood_max=-70, mood_min=20, fitness_multi=0.8, int_multi=0.8, desire_add=-200, allure_add=-100, wildcard=True)

    $ perk_male = PerkClass("Former man", "I used to be a man, then some fucked up science experiment turned me into a girl...", "perk_male", confidence_max=-40, fitness_multi=2, allure_add=-20, desire_max=300)

    $ perk_origin_list = [perk_waif, perk_nerd, perk_gym_bunny, perk_bimbo, perk_gamine, perk_bambi, perk_broodmother, perk_party_girl, perk_meek, perk_princess, perk_addict, perk_deadinside, perk_wildcard]


    $ perk_survivor = PerkClass("Survivor", "I have been through a lot of shit and hopefully it made me stronger.", "perk_survivor", confidence_min=10, mood_multi=0.8, fitness_multi=1.2, not_victim=True)

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
