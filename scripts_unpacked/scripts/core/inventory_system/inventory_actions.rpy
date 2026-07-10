init python:
    def item_add_all():
        for i in item_list:
            if i.stackable:
                inv.take(i, 10, notif=False)
            else:
                inv.take(i, 1, notif=False)

    def item_sucu_pill_passout():
        
        for _ in range(10):
            if numgen(0, 8):
                player.sex_cum(unknown, "face")
                player.sex_cum(unknown, "belly")
                player.sex_cum(unknown, "chest")
            else:
                if numgen():
                    player.sex_vag(unknown)
                    player.sex_cum(unknown, "inside")
                else:
                    player.sex_anal(unknown)
                    player.sex_cum(unknown, "anus")

    def item_cig_smoke(notif):
        inv.use(item_cigs, notif=notif)
        player.add_mood(2)
        player.add_perk(perk_smoking, mins=numgen(4,7))
        if item_cigs.used >= 40 and not numgen(0, 40):
            player.add_perk(perk_smoker)

    def item_cigs_smoke_auto(notif=False):
        if inv.qty(item_cigs) and item_cigs.last_used and player.has_perk(perk_smoker) and not player.having_sex and not numgen(0,5):
            item_cig_smoke(notif)

    def item_breastpump_use():
        times_milked = 0
        for i in range(inv.qty(item_milkbottle_empty)):
            if perk_lactating.dict["milk_amount"] >= 5:
                perk_lactating_milk(5)
                times_milked += 1
            else:
                break
        if times_milked:
            inv.drop(item_milkbottle_empty, times_milked)
            inv.take(item_scrap_milkbottle, times_milked)
            relax(times_milked * 5)
            refresh_avatar()

    def item_breastpump_can_use():
        if (any(substring for substring in ["toilet", "bathroom", "shower", "locker", "bedroom"] if substring in loc_cur.name) or (loc_cur.population <= 0 and not loc_cur.outside) and inv.qty(item_breastpump)):
            return True
        else:
            return False

default item_list = []
default item_inv_call = False

image item_mira_intel = "item_haven_intel"

label inventory_items:

    $ item_beer = Item("BOTTLE OF BEER", "A cheap bottle of homebrew alcohol", "item_beer", use_notif="Drank a beer", type="consumable", value=4)
    $ item_preg_test = Item("PREGNANCY TEST", "A cheap pregnancy test.", "item_preg_test", use_notif="Used a pregnancy test", type="consumable", value=50)
    $ item_brew = Item("HOMEMADE BREW", "A bottle of some sort of alcohol. Clearly made in some basement from a makeshift still and has a killer punch to it.", "item_brew", use_notif="Drank a brew", type="consumable", value=4)
    $ item_cigs = Item("ROLL-UPS", "A packet of home made roll up cigarettes.", "item_cigs", use_notif="Smoked a roll-up", type="consumable", value=2)
    $ item_map_pill = Item("MORNING AFTER PILL", "A pill that prevents pregnancy if taken after sex. Reduced effectiveness the longer you wait.", "item_map_pill", use_notif="Took a morning after pill", type="consumable", value=300)
    $ item_abort_pill = Item("ABORTION PILL", "A pill that will end your pregnancy if it is in an early enough stage.", "item_abort_pill", use_notif="Took an abortion pill", type="consumable", value=1200)
    $ item_joy = Item("JOY", "A small sweet that makes even the most miserable person happy.", "item_joy", use_notif="Took Joy", type="consumable", value=120)
    $ item_lebo = Item("LEBO", "A small pink pill that makes my libido go haywire.", "item_lebo", use_notif="Took Lebo", type="consumable", value=120)
    $ item_wakeup = Item("WAKEUP", "A powder that will give me all the energy I need.", "item_wakeup", use_notif="Took Wakeup", type="consumable", value=250)
    $ item_milktab = Item("MILK TAB", "A weird pill that induces lactation.", "item_milktab", use_notif="Took a Milk tab", type="consumable", value=250)
    $ item_winebottle = Item("BOTTLE OF WINE", "An original bottle of wine. Unlike most booze, this is not home made.", "item_winebottle", use_notif="Opened a wine bottle", type="consumable", value=75, locked=True)

    $ item_energydrink = Item("Energy drink", "A high caffeine and sugar drink.", "item_energydrink", use_notif="Drank an energy drink", type="consumable", value=20)
    $ item_energyfood = Item("Cereal bar", "Oats mixed with syrup formed into a bar.", "item_energyfood", use_notif="Ate an energy bar", type="consumable", value=20)
    $ item_bruisecream = Item("Ointment", "A cream to apply to wounds and injuries.", "item_bruisecream", use_notif="used ointment", type="consumable", value=50)

    $ item_mag_ent = Item("Entertainment magazine", "An old magazine of things that used to interest people.", "item_mag_ent", use_notif="Read a magazine", type="consumable", value=30)
    $ item_mag_porn = Item("Porn magazine", "A home made magazine with pictures of minimally dressed people.", "item_mag_porn", use_notif="Read a magazine", type="consumable", value=50)
    $ item_mag_felix = Item("Blaston special magazine", "A newly made magazine with pictures of minimally dressed people and local news.", "item_mag_felix", use_notif="Read a magazine", type="consumable", value=100, locked=True)

    $ item_sucu_pill = Item("Strange pill", "A weird pill I managed to dig up.", "item_sucu_pill", use_notif="Took strange pill", type="consumable")

    $ item_pepperspray = Item("Defensive spray", "A spray that will blind anyone who gets it in their eyes.", "item_pepperspray", use_notif="Used defensive spray", type="consumable", value=3000)
    $ item_razor = Item("SHAVING RAZOR", "A disposable razor for shaving hair in delicate areas.", "item_razor", type="consumable", value=6)

    $ item_poison = Item("POISON", "A bottle of a very lethal poison.", "item_poison", type="consumable", value=500)
    $ item_beer_poison = Item("POISONED BEER", "A bottle of beer that has been poisoned.", "item_beer_poison", type="consumable", value=0)

    $ item_pinkticket = Item("PINK TICKET", "Tickets I have earned though working in a pink room. Exchange at the motel reception.", "item_pinkticket", type="consumable", value=30)

    $ item_perm_marker = Item("PERMANENT MARKER", "A marker that is difficult to wash off.", "item_perm_marker", type="tool", value=150)
    $ item_felt_marker = Item("WASHABLE MARKER", "A marker that is easy to wash off.", "item_felt_marker", type="tool", value=100)
    $ item_nailpolish = Item("NAIL POLISH", "Nail polish allowing me to colour my nails.", "item_nailpolish", type="tool", value=350)
    $ item_hairdye = Item("HAIR DYE", "A dye allowing me to colour my hair.", "item_hairdye", type="tool", value=500)
    $ item_contacts = Item("CONTACT LENSES", "Contacts allowing me to colour my eyes.", "item_contacts", type="tool", value=500)

    $ item_tissue = Item("Tissues", "A pack of pocket tissues.", "item_tissue", type="consumable", value=2)

    $ item_alarm = Item("ALARM CLOCK", "A crank powered alarm clock I can carry with me.", "item_alarm", type="tool", value=45)

    $ item_chis = Item("CHISEL", "A wood chisel. Not very sharp but good enough to get the job done.", "item_chis", type="tool")
    $ item_saw = Item("WOOD SAW", "A small wood saw. It's seen better days but still has some life left in it.", "item_saw", type="tool")
    $ item_tape = Item("GAFFA TAPE", "A roll of very strong tape. I should use this sparingly else it will run out.", "item_tape", type="tool", stackable=True, value=35)

    $ item_polaroid_taken = Item("POLAROID PHOTO", "Photos I have taken on my camera.", "item_polaroid_taken", type="tool", stackable=True, value=20)
    $ item_polaroid_blank = Item("BLANK POLAROIDS", "Blank polaroids ready for use in a camera.", "item_polaroid_blank", type="consumable", value=10)
    $ item_polaroid_camera = Item("POLAROID CAMERA", "A camera that makes instant photos.", "item_polaroid_camera", type="tool", value=200)

    $ item_breastpump = Item("BREAST PUMP", "A breast pump for bottling milk.", "item_breastpump", type="tool", stackable=False, value=150)
    $ item_scrap_milkbottle = Item("FULL MILK BOTTLE", "A bottle of breast milk", "item_scrap_milkbottle", type="junk", act="item_scrap_action", value=15)
    $ item_milkbottle_empty = Item("EMPTY MILK BOTTLE", "An empty bottle for use with a breast pump.", "item_milkbottle_empty", type="tool", stackable=True, value=5)

    $ item_buttplug = Item("BUTTPLUG", "A fairly large, bright pink buttplug.", "item_buttplug", type="tool", value=200)
    $ item_blindfold = Item("BLINDFOLD", "A makeshift blindfold for... Blindfolding.", "item_blindfold", type="tool", value=20)
    $ item_bdsm = Item("BINDINGS", "A set of bindings for bedroom fun.", "item_bdsm", type="tool", value=300)
    $ item_ballgag = Item("BALLGAG", "A simple ballgag designed to silence people. Drooling optional.", "item_ballgag", type="tool", value=550)
    $ item_ballgag_locked = Item("LOCKABLE BALLGAG", "A ballgag designed to silence people. Has a lock on the back preventing it being opened. Doesn't have a key.", "item_ballgag_locked", type="tool", value=300)
    $ item_strapon = Item("A strapon penis", "A strapon penis. It is fairly large, bright pink and knobbled.", "item_ballgag_locked", type="tool", value=300)

    $ item_pregband = Item("MATERNITY BAND", "A band that helps support my back and baby bump", "item_pregband", type="tool", value=300)






    $ item_simon_satchel = Item("SIMON'S SATCHEL", "A small ragged bag presumably containing all the notes Simon managed to dig up on The Institute", "item_simon_satchel", type="mission", icon="item_satchel")
    $ item_haven_package = Item("MISSION PACKAGE", "A package of some of the gear I will need before infiltrating Haven.", "item_haven_package", type="mission", icon="item_package", stackable=True)
    $ item_robin_package = Item("SLUTTY CLOTHES", "A couple of outfits that maybe even a highway whore would be ashamed to wear.", "item_robin_package", type="mission", icon="item_package")

    $ item_mira_intel = Item("MIRA INTEL NOTES", "Notes about what I have discovered while investigating Mira's disappearance.", "item_mira_intel", type="mission", stackable=True)





    $ item_haven_crowbar = Item("CROWBAR", "A small crowbar that can be used to pry things off of other things.", "item_haven_crowbar", type="mission")
    $ item_haven_lighter = Item("LIGHTER", "A refillable cigarette lighter. Fairly uncommon these days.", "item_haven_lighter", type="mission")
    $ item_haven_fluid = Item("ACCELERANT", "A liquid fire accelerant used for getting barbecue's going.", "item_haven_fluid", type="mission")
    $ item_haven_intel = Item("INTEL NOTES", "Notes of whatever intelligence I have gathered in Haven. Best to keep this stuff written down.", "item_haven_intel", type="mission", stackable=True)





    $ item_scrap_cloth = Item("Cloth scraps", "Small scraps of cloth. Large enough for making repairs but not much else.", "item_scrap_cloth", type="junk", act="item_scrap_action", value=1)
    $ item_scrap_clothes = Item("Tattered clothing", "Mostly intact clothes. Far too tattered to wear but with some repair they might be good.", "item_scrap_clothes", type="junk", act="item_scrap_action", value=4)
    $ item_scrap_junk = Item("Reusable junk", "Junk that has seen better days, but with a bit repair could be usable again", "item_scrap_junk", type="junk", icon="item_scrap_can", act="item_scrap_action", value=1)
    $ item_scrap_metal = Item("Scrap metal", "Scrap metal that can probably be repurposed and reused.", "item_scrap_metal", type="junk", act="item_scrap_action", value=3)
    $ item_scrap_ele = Item("Scrap electronics", "Electronic components that can be used to repair broken equipment.", "item_scrap_ele", type="junk", act="item_scrap_action", value=7)
    $ item_scrap_mag = Item("Tattered magazine", "An old magazine that can probably be cleaned up and made readable.", "item_scrap_mag", type="junk", act="item_scrap_action", value=2)
    $ item_scrap_book = Item("Tattered book", "An old book that is still readable. It can probably be cleaned and sold.", "item_scrap_book", type="junk", act="item_scrap_action", value=9)
    $ item_scrap_jewel = Item("Damaged jewellery", "Jewellery that is dull or damaged but can possibly be repaired into something valuable.", "item_scrap_jewel", type="junk", act="item_scrap_action", value=6)
    $ item_scrap_gem = Item("Shiny stones", "Gems, pearls and any shiny stones that can be used in jewellery.", "item_scrap_gem", type="junk", act="item_scrap_action", value=20)
    $ item_scrap_seashell = Item("Seashells", "Nice looking seashells that can be used to make jewellery or other baubles.", "item_scrap_seashell", type="junk", act="item_scrap_action", value=1)


    return

label item_simon_satchel_action:
    pcm "This is the bag I got off of [simon.fname]. I need to bring it back to [tucker.name]."
    jump item_action_end

label item_haven_package_action:
    pcm "I need these before taking on a mission to Haven. Once I have them all I should return to [tucker.name]."
    jump item_action_end

label item_haven_intel_action:
    if inv.qty(item_haven_intel) < 10:
        pcm "This is all the intel I have gathered. Think I need a little more before I can leave."
    else:
        pcm "This is all the intel I have gathered. I have enough to paint a pretty clear picture so I can leave [haven] if I want."
    jump item_action_end

label item_haven_crowbar_action:
    pcm "I might be able to use this to pry at something."
    if havengateguard.has_met:
        pcm "Could try the gate that leads upstairs, but I would need to get the guard away somehow."
    jump item_action_end

label item_haven_lighter_action:
    pcm "A cigarette lighter. I can probably trade it for something. Maybe someone has use of one."
    if inv.qty(item_haven_fluid):
        pcm "I could also use it with the accelerant I got my hands on to start a fire to distract the guards. Question is, where?"
    jump item_action_end

label item_haven_fluid_action:
    if inv.qty(item_haven_lighter):
        pcm "I can probably use this and the lighter to set a fire somewhere to distract the guards. Question is, where?"
    else:
        pcm "If I could get my hands on a lighter, I could probably start a fire somewhere to distract the guards."
    jump item_action_end

label item_brew_action:
    if dis_cur == dis_haven:
        jump haven_brewmaster_drink
    else:
        jump haven_brewmaster_drink

label item_cigs_action:



    if player.has_perk(perk_smoking):
        pcm "I am already smoking..."
        jump item_action_end
    "I take a roll up out and light it up."
    $ item_cig_smoke(notif=True)
    jump item_action_end

label item_beer_action:
    if player.has_perk([perk_drinking_wine_4, perk_drinking_wine_3, perk_drinking_wine_2, perk_drinking_wine_1]):
        pcm "I should finish the bottle of wine first."
        jump item_action_end
    elif player.has_perk([perk_drinking_beerbottle_2, perk_drinking_beerbottle_1]):
        pcm "I'm already drinking a beer."
        jump item_action_end
    elif player.has_perk([perk_drinking_brew_2, perk_drinking_brew_1]):
        pcm "I am already drinking a brew."
        jump item_action_end
    $ inv.use(item_beer)
    $ player.add_perk(perk_drinking_beerbottle_2, mins=10)
    "I take a beer out of my purse and have a drink."
    $ player.drink()
    if player.drunk > 50:
        pc "Whoooo!"
    elif player.drunk > 100:
        pc "Ubb. *HIC*"
    else:
        pcm "That hit the spot."
    jump item_action_end

label item_winebottle_action:
    if player.has_perk([perk_drinking_wine_4, perk_drinking_wine_3, perk_drinking_wine_2, perk_drinking_wine_1]):
        pcm "I should finish the one I am drinking first."
        jump item_action_end
    elif player.has_perk([perk_drinking_beerbottle_2, perk_drinking_beerbottle_1]):
        pcm "I'm already drinking a beer."
        jump item_action_end
    elif player.has_perk([perk_drinking_brew_2, perk_drinking_brew_1]):
        pcm "I am already drinking a brew."
        jump item_action_end
    $ inv.use(item_winebottle)
    $ player.add_perk(perk_drinking_wine_4, mins=10)
    "I take out a bottle of wine, open it and start drinking."
    $ player.drink()
    if player.drunk > 50:
        pc "Whoooo!"
    elif player.drunk > 100:
        pc "Ubb. *HIC*"
    else:
        pcm "That hit the spot."
    jump item_action_end

label item_joy_action:
    if player.has_perk(perk_joy):
        pcm "No need. I still feel the effects of the last one."
        jump item_action_end
    "I take a Joy out of my purse and pop it in my mouth."
    $ inv.use(item_joy)
    $ player.face_excited()
    pc "Mmmm."
    $ player.add_perk(perk_joy, hours=4)
    $ player.add_mood(200)
    if player.has_perk(perk_joy_addict):
        $ perk_joy_addict.days = 5
    if not numgen(0, 20):
        $ player.add_perk(perk_joy_addict, days=5)
    jump item_action_end

label item_lebo_action:
    if player.has_perk(perk_lebo):
        pcm "I'm already going crazy from the one I'm on"
        jump item_action_end
    "I take a Lebo out of my purse and pop it in my mouth."
    $ inv.use(item_lebo)
    $ player.face_shy()
    pc "Oooh."
    $ player.add_perk(perk_lebo, hours=4)
    $ player.add_desire(1000)
    jump item_action_end

label item_wakeup_action:
    "I take some Wakeup out of my purse and give it a good sniff."
    $ inv.use(item_wakeup)
    $ player.face_excited()
    pc "Whoooo!"
    if player.has_perk(perk_wakeup_comedown):
        $ player.add_mood(30)
        $ player.remove_perk(perk_wakeup_comedown)
    $ player.add_perk(perk_wakeup, hours=2)
    $ player.add_tired(200)
    jump item_action_end

label item_map_pill_action:
    if player.has_perk(perk_map):
        pcm "I already feel shitty from the last one I took. I shouldn't be eating these like sweets."
        jump item_action_end
    elif player.has_perk(perk_broodmother):
        $ player.face_angry()
        pcm "Never going to happen."
        jump item_action_end
    elif player.has_perk(perk_preg_want):
        $ player.face_worried()
        if player.check_speech(5):
            $ NullAction()
        else:

            $ dialouge = renpy.random.choice([
            "Err, I'd rather not...",
            "Err, No thanks",
            "But I don't want to.",
            "I would rather keep it."
            ])
            pcm "[dialouge]"
            $ player.add_mood(-15)
            jump item_action_end
    elif player.last_cumin > 6:
        pcm "I don't remember doing anything dangerous recently. But I guess you can never be too careful."
        menu:
            "Take one anyway.":
                $ NullAction()
            "On second thoughts...":
                pcm "Probably shouldn't waste these."
                jump item_action_end
    pcm "Hope this works."
    $ inv.use(item_map_pill)
    $ player.preg_morningafter_pill()
    jump item_action_end

label item_abort_pill_action:
    if not player.preg_knows:
        pcm "I have no idea if I am pregnant. I shouldn't be taking these on a whim."
        jump item_action_end
    elif player.has_perk(perk_broodmother) or player.has_perk(perk_preg_want):
        $ player.face_angry()
        pcm "Never going to happen."
        jump item_action_end
    pcm "Ugh..."
    pcm "Well..."
    pcm "Here goes I suppose..."
    $ inv.use(item_abort_pill)
    $ player.preg_abortion()
    pcm "Bleh!"
    $ relax(5)
    jump item_action_end

label item_preg_test_action:
    if not (any(substring for substring in ["toilet", "bathroom", "shower", "locker"] if substring in loc_cur.name) or loc_cur.home_location):
        pcm "I should go somewhere more private to do this..."
        jump item_action_end

    if player.preg_knows:
        pcm "I already know I am pregnant. No point in wasting this."
        jump item_action_end
    "I take the test out of my bag, sit down and use it."
    $ inv.use(item_preg_test)
    if player.has_perk(perk_preg_want):
        pcm "Please be pregnant please be pregnant please be pregnant..."
    elif player.has_perk(perk_preg_notwant):
        pcm "Don't be pregnant don't be pregnant don't be pregnant..."
    else:
        pcm "Hmmm..."
    "I sit and wait for a result..."
    $ relax(5)
    pcm "Ah, it changed!"
    if player.preg_test():

        if player.has_perk(perk_wanted_preg):
            $ player.face_laugh()
            pcm "YES! Pregnant!"
        elif player.has_perk(perk_unwanted_preg):
            $ player.face_shock()
            pcm "FUCK! I'm pregnant."
            $ player.face_cry()
            pc "*SOB*"
        else:
            $ player.face_worried()
            pcm "It says I'm pregnant..."
    else:
        if player.has_perk(perk_preg_want):
            $ player.face_sad()
            pcm "Shit. Not pregnant..."
        elif player.has_perk(perk_preg_notwant):
            $ player.face_happy()
            pcm "Phew. Not pregnant."
        else:
            pcm "It says not pregnant."
    "I throw the test away, clean up and prepare to head out."
    jump item_action_end

label item_perm_marker_action:
    $ temp_var_1 = "perm"
    jump item_marker_action_dia
label item_felt_marker_action:
    $ temp_var_1 = "temp"
    jump item_marker_action_dia
label item_marker_action_dia:
    pcm "Hmm, I could use this to write something on myself..."
    if not player.check_sex_agree(5):
        pcm "No, that will just cause trouble..."
        jump item_action_end
    "NOTE*** This menu is temporary. I will do something better later."
    jump item_marker_action_menu
label item_marker_action_menu:
    menu:
        "\"Whore\" on forehead" if writing.can_write("forehead", temp_var_1):
            $ writing.add_writing("forehead", temp_var_1)
        "Slut heart on cheek" if writing.can_write("face", temp_var_1):
            $ writing.add_writing("face", temp_var_1)
        "\"Milk me\" on chest" if writing.can_write("chest", temp_var_1):
            $ writing.add_writing("chest", temp_var_1)
        "\"Fertile\" on stomach" if writing.can_write("belly", temp_var_1):
            $ writing.add_writing("belly", temp_var_1)
        "\"Cum here\" on pubis" if writing.can_write("pubic", temp_var_1):
            $ writing.add_writing("pubic", temp_var_1)
        "\"Anal queen\" on my ass" if writing.can_write("anus", temp_var_1):
            $ writing.add_writing("anus", temp_var_1)
        "\"Fuck me\" on my thigh" if writing.can_write("lleg", temp_var_1):
            $ writing.add_writing("lleg", temp_var_1)
        "Write a sex counter on my ass" if writing.can_write("ass", temp_var_1):
            $ writing.add_writing("ass", temp_var_1)
        "Never mind":
            jump item_action_end

    pcm "There we go."
    jump item_marker_action_menu

label item_nailpolish_action:
    pcm "It's nail polish. I can use it from my wardrobe to colour my nails."
    jump item_action_end

label item_hairdye_action:
    pcm "A box of hair dye. I can use it from my wardrobe to colour my hair."
    jump item_action_end

label item_contacts_action:
    pcm "Contact lenses. I can put them on at home to change my eye colour."
    jump item_action_end

label item_sucu_pill_action:
    if not item_sucu_pill.used:
        pcm "Some strange pill I picked up. I have no idea what it does so probably shouldn't be taking it."
        $ item_sucu_pill.used += 1
        jump item_action_end
    elif item_sucu_pill.used == 1:
        pcm "Seems to have some kind of heart on it and sort of looks like a Lebo pill."
        $ item_sucu_pill.used += 1
        jump item_action_end
    elif item_sucu_pill.used == 2:
        pcm "No way I should be taking something like this. Though the heart on it does make it look interesting."
        $ item_sucu_pill.used += 1
        jump item_action_end
    elif item_sucu_pill.used == 3:
        pcm "Why am I so interested in this thing?"
        $ item_sucu_pill.used += 1
        jump item_action_end
    else:
        pcm "Hmmm..."
        pcm "Whatever..."
        pcm "Should I really try it?"
        menu:
            "Take it":
                $ player.face_worried()
                pcm "I really shouldn't..."
                pcm "Ah fuck it!"
                $ inv.use(item_sucu_pill)
                pcm "..."
                pcm "Err..."
                $ player.face_shy()
                pcm "I feel really hot."
                pcm "Really, really hot..."
                pcm "Fuck! I knew it was a bad idea."
                $ player.face_puke()
                pc "Nnnnng!"
                pc "Fuck fuck fuck."
                show screen blackout(50) with dissolve
                pc "Uh oh..."
                pc "I felllll alallll fwwww..."
                show screen blackout(100) with dissolve
                $ travel_isolate()
                $ pc_strip()
                $ player.add_perk(perk_sucu)
                $ time_sleep_rough()
                $ item_sucu_pill_passout()

                $ player.face_sleep()
                $ player.sex_hideaction()
                pause 2.0
                show screen blackout(75) with dissolve
                pc "Uggghhh..."
                show screen blackout(50) with dissolve
                $ player.face_worried()
                pc "What the fuckkkkk..."
                show screen blackout(25) with dissolve
                pc "Ugh..."
                hide screen blackout with dissolve
                pc "..."
                pcm "Fuck, I am naked."
                $ player.face_puke()
                pcm "And I stink. Ugh. I am covered in it..."
                pcm "I feel like shit..."
                pcm "..."
                $ player.face_worried()
                pcm "Actually. No I don't..."
                $ player.face_happy()
                pcm "I feel pretty great actually."
                pcm "What the fuck."
                $ player.face_neutral()
                pcm "Wow."
                pcm "Err. Well feeling great doesn't change the fact I am standing here with my arse out covered in cum."
                pcm "Better do something about that..."
                jump item_action_end
            "No. Too dangerous":
                pcm "Yeah. Shouldn't risk it."
                jump item_action_end

label item_chis_action:
    if log.interactive("quest_gloryhole"):
        pcm "I can use this along with a saw to make a glory hole in public toilets."
    else:
        pcm "A chisel. Not sure what I will do with it but it's in workable condition."
        if log.interactive("quest_gloryhole_a"):
            pcm "Hmm, actually I can use this to make a hole for [nate.name]'s glory hole project."
            pcm "Will probably need something to make the hole a circle though. A saw maybe?"
            $ log.markdone("quest_gloryhole_a")
            $ log.activate("quest_gloryhole_b_saw")
    jump item_action_end

label item_saw_action:
    if log.interactive("quest_gloryhole"):
        pcm "I can use this along with a chisel to make a glory hole in public toilets."
    else:
        pcm "A small wood saw. Not sure what I will do with it but it's in workable condition."
        if log.interactive("quest_gloryhole_a"):
            pcm "Hmm, actually I can use this to make a hole for [nate.name]'s glory hole project."
            pcm "Will probably need something to start the hole with though. A chisel?"
            $ log.markdone("quest_gloryhole_a")
            $ log.activate("quest_gloryhole_b_saw")
    jump item_action_end

label item_tape_action:
    pcm "Some extremely strong tape"
    if log.interactive("quest_gloryhole"):
        pcm "I can use this along with a saw and chisel to make a glory hole in public toilets."
    jump item_action_end

label item_pepperspray_action:
    pcm "Something I can spray at someone to get them off my back."
    jump item_action_end

label item_scrap_action:
    pcm "Junk that I can probably sell off somewhere."
    jump item_action_end

label item_alarm_action:
    if alarm_set:

        pcm "My alarm clock. It's set for [alarm_hour]:00."
    else:
        pcm "My alarm clock. It's not set."
    menu:
        "Set the alarm time" if not alarm_set:
            jump item_alarm_set
        "Turn off the alarm" if alarm_set:
            $ alarm_set = False
            pcm "There we go, it won't go off anymore."
            jump item_action_end
        "Put back":
            jump item_action_end

label item_alarm_set:
    menu:
        "Add 1 hour":
            $ alarm_hour += 1
            if alarm_hour >= 25:
                $ alarm_hour = 0
            jump item_alarm_set
        "Reduce by 1 hour.":
            $ alarm_hour -= 1
            if alarm_hour <= 0:
                $ alarm_hour = 23
            jump item_alarm_set
        "Set for [alarm_hour]:00":
            $ alarm_set = True
            pcm "There we go. Set for [alarm_hour]:00"
            jump item_action_end

label item_razor_action:
    if any(substring for substring in ["toilet", "bathroom", "shower", "locker"] if substring in loc_cur.name):

        pcm "I can use this on my hair below. Should I?"
        menu:
            "Yes, use it.":
                $ pc_striptease()
                pause 0.2
                pcm "Right..."
                $ relax(5)
                $ inv.use(item_razor)
                $ player.phair_shave()
                pcm "There we go..."
                $ pc_dress_slow()
                jump item_action_end
            "Not right now":
                jump item_action_end
    else:
        pcm "I can use this in the bathroom to groom my body hair."
        jump item_action_end

label item_buttplug_action:
    $ player.face_neutral()
    if not any(substring for substring in ["toilet", "bathroom", "shower", "locker", "bedroom", "trailer"] if substring in loc_cur.name):
        $ player.face_worried()
        pcm "I should do this somewhere more private."
    elif acc.anus:
        $ pc_striptease()
        pcm "So much easier putting it in than taking it out."
        pc "Nnng..."
        $ acc.anus = 0
        pcm "Phew, that's it out."
        $ pc_dress_slow()
        pcm "Feel kinda empty now..."
    else:
        pcm "Right..."
        $ pc_striptease()
        pcm "Here goes..."
        pc "Nnng..."
        show screen sex_action_flash("anal")
        $ acc.anus = 1
        if not inv.qty(item_buttplug):
            $ inv.take(item_buttplug)
        $ player.add_desire(100)
        $ player.face_shock()
        with grope_trans
        pcm "Ooohh..."
        $ pc_dress_slow()
        pcm "So full up..."
    jump item_action_end

label item_robin_package_action:
    pcm "Some outfits I picked up for [robin.name]. I should chat with her and show her what I got."
    jump item_action_end

label item_poison_action:
    pcm "A bottle of poison. I need to be careful with this stuff."
    if (school_bully_quest_bully_event_stage >= 8 or school_bully_quest_bully_cass_target) and not shane.dead:
        if school_bully_quest_bully_cass_target:
            pcm "I can give this to [cass.nname] and help with her bully problem..."
        elif inv.qty(item_beer) >= 4:
            $ player.face_worried()
            pcm "I could maybe put them in the beers I have and hope those two cunts at school steal them from me..."
            pcm "Fuck..."
            pcm "There is no way that they will be alright afterwards though..."
            menu:
                "Do it":
                    pcm "..."
                    pcm "Ugh..."
                    $ inv.drop(item_beer, 4, notif=True)
                    $ inv.drop(item_poison, notif=True)
                    $ inv.take(item_beer_poison, 4, notif=True)
                    pcm "Well, that's it done..."
                "Don't do it":
                    pcm "Doing that is going too far..."
        else:
            $ player.face_worried()
            pcm "If I had more beers, I could poison them and hope the cunts in school steal them..."
    if (oskar.rape and oskar.sex > 5) or oskar.hate or loc_kitchen.locked:
        if inv.qty(item_beer) >= 4:
            $ player.face_worried()
            if oskar.rape:
                pcm "I could maybe put them in the beers I have and somehow get that rapist landlord to drink them..."
            elif oskar.hate:
                pcm "I could maybe put them in the beers I have and somehow get that piece of shit landlord to drink them..."
            else:
                pcm "I could use this to maybe get rid of [oskar.name]..."
                pcm "Fuck... Did he even do anything wrong to deserve this?"
                if "knows_dani_sex_oskar" in dani.list:
                    pcm "Well, he is basically raping [dani.nname] to let her stay in her shithole..."
                    pcm "That is her buisness though."
                pcm "I mean I am supposed to pay rent and get kicked out if I don't..."

            pcm "Fuck..."
            pcm "There is no way that he will be alright afterwards though..."
            menu:
                "Do it":
                    pcm "..."
                    pcm "Ugh..."
                    $ inv.drop(item_beer, 4, notif=True)
                    $ inv.drop(item_poison, notif=True)
                    $ inv.take(item_beer_poison, 4, notif=True)
                    pcm "Well, that's it done..."
                "Don't do it":
                    pcm "Doing that is going too far..."
        else:
            $ player.face_worried()
            pcm "If I had more beers, I could poison them and sneak them into [oskar]'s office..."
    jump item_action_end

label item_beer_poison_action:
    pcm "I had better not drink this or I'll end up dead."
    if not numgen(0,5) and not quest_homeless_start.active:
        pcm "Well, dead again..."
    jump item_action_end

label item_mag_ent_action:
    pcm "Let's see here..."
    "I hang around flipping through the magazine and reading what is there."
    $ inv.drop(item_mag_ent)
    $ inv.take(item_scrap_mag)
    $ relax(20)
    $ player.add_mood(20)
    $ player.add_desire(20)
    jump item_action_end

label item_mag_porn_action:
    $ player.face_shy()
    pcm "Let's see here. ♥"
    "I hang around flipping through the magazine and reading what is there."
    $ inv.drop(item_mag_porn)
    $ inv.take(item_scrap_mag)
    $ relax(20)
    $ player.add_mood(10)
    $ player.add_desire(1000)
    jump item_action_end

label item_energydrink_action:
    if player.tired >= 70:
        pcm "I should probably save this for when I am tired."
        jump item_action_end
    $ inv.drop(item_energydrink)
    $ inv.take(item_scrap_junk)
    "I take an energy drink out my bag and have a drink."
    $ player.add_tired(10)
    $ relax(4)
    jump item_action_end

label item_energyfood_action:
    if player.hunger >= 70:
        pcm "I should probably save this for when I am hungry."
        jump item_action_end
    $ inv.drop(item_energyfood)
    "I take a cereal bar out my bag and eat it."
    $ player.eat()
    $ relax(4)
    jump item_action_end

label item_bruisecream_action:
    if sum([bruise.face, bruise.chest, bruise.belly]):
        pcm "I take out the cream and rub it over my wounds."
        $ inv.drop(item_bruisecream)
        $ inv.take(item_scrap_junk)
        $ relax(4)
        $ bruise.heal()
    else:
        pcm "I don't really need to use this."
    jump item_action_end

label item_blindfold_action:
    if player.has_perk(perk_blind):
        "I remove the blindfold from over my head."
        $ player.remove_perk(perk_blind)
    else:
        pcm "This is probably a bad idea..."
        $ player.add_perk(perk_blind)
    jump item_action_end

label item_ballgag_action:
    if player.has_perk(perk_gagged_locked):
        pcm "I am already gagged with this thing locked on my face..."
    elif player.has_perk(perk_gagged):
        "I remove the ballgag from my mouth."
        $ player.remove_perk(perk_gagged)
        pc "Ahh, can talk finally!"
    else:
        pcm "This is probably a bad idea..."
        $ player.add_perk(perk_gagged)
        pc "Something, doesn't matter because gagged."
    jump item_action_end

label item_ballgag_locked_action:
    if player.has_perk(perk_gagged):
        pcm "I am already gagged..."
    elif player.has_perk(perk_gagged_locked):
        pcm "Damn thing is locked. I can't get rid of it."
        "Dev note. There is nowhere to properly remove this yet. Do you want to remove it now?"
        menu:
            "Remove it":
                $ player.remove_perk(perk_gagged_locked)
            "Leave it":
                $ NullAction()
    else:

        pcm "This is a very bad idea..."
        menu:
            "Put it on and lock it anyway":
                $ player.add_perk(perk_gagged_locked)
                pc "Something, doesn't matter because gagged."
            "I had better not.":
                $ NullAction()
    jump item_action_end

label item_pregband_action:
    if player.has_perk([perk_pregband_notpreg, perk_pregband_preg]):
        "I take of the maternity band."
        $ player.remove_perk([perk_pregband_notpreg, perk_pregband_preg])
    elif not player.pregnancy:
        pcm "Not sure what help this is."
        $ player.add_perk(perk_pregband_notpreg)
    else:
        "I put on the maternity band."
        $ player.add_perk(perk_pregband_preg)
        pcm "Hopefully this can help my back from aching."
    jump item_action_end

label item_pinkticket_action:
    pcm "I should give these to the receptionist at the motel."
    jump item_action_end

label item_tissue_action:
    if not player.cum_visible:
        pcm "I don't need to use that right now."
        jump item_action_end
    "I take out a tissue and use it to wipe myself off."
    $ player.cum_clean_outside()
    $ player.add_hygiene(5)
    $ inv.drop(item_tissue)
    jump item_action_end

label item_milktab_action:
    pcm "This will make me start to lactate. Do I really want that?"
    menu:
        "Yes, take it":
            $ inv.drop(item_milktab)
            $ player.add_perk(perk_lactating)
            $ perk_lactating_buildup()
            "I pop it in my mouth and suck on it for a bit."
            $ relax(4)
            jump item_action_end
        "No, not now":
            jump item_action_end

label item_breastpump_action_jump:
    $ item_inv_call = True

label item_breastpump_action:
    if not "milk_amount" in perk_lactating.dict:
        $ perk_lactating.dict["milk_amount"] = 0
    if not player.has_perk(perk_lactating):
        pcm "I don't have any use for this."
        jump item_action_end
    if not inv.qty(item_breastpump):
        pcm "I need to buy a pump or something."
        jump item_action_end
    elif not perk_lactating.dict["milk_amount"] > 5:
        $ player.face_meek()
        $ player.cover_breasts_force()
        pcm "I don't have anything left right now."
        $ player.uncover()
        $ player.face_normal()
        jump item_action_end
    elif not inv.qty(item_milkbottle_empty):
        pcm "I don't have any empty bottles left."
        jump item_action_end
    else:
        if item_breastpump_can_use():
            if dani_here() and loc(loc_bedroom_dani):
                pc "Hope you don't mind if I milk myself."
                if dani.sex_les:
                    dani.name "Oh? Can I watch?"
                    pc "Pervert."
                else:
                    dani.name "Sure, no problem."
            $ pc_strip_upper()
            $ player.face_meek()
            $ player.cover_breasts_force()
            "I take out the pump and stand pump my breasts for a while."
            $ item_breastpump_use()
            pcm "That should do it..."
            $ player.uncover()
            $ player.face_normal()
            $ pc_dress()
            jump item_action_end
        else:
            pcm "I should go somewhere private to do this."
            jump item_action_end

label item_mira_intel_action:
    pcm "These are the notes me and [cass.name] have managed to dig up about [mira.name]."
    jump item_action_end

label item_none_action:
    "DESCRIPTION NEEDS TO BE ADDED HERE"
    jump item_action_end



label item_action_end:



    if item_inv_call:
        $ item_inv_call = False
        jump travel
    else:
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
