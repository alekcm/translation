init python:
    class Maths(object): 
        def __init__(self):
            self.total = 0

label after_load:

    if game_version < "0.3.1.02":

        $ robin = Npc(fname="Robin", sname="Albescu", love=0, bio_image="robin", bio_group="flatmate",
        bio_text="She and I live together.", 
        is_female=True)

        $ loc_bedroom_robin = Location("Robin's bedroom", "loc_bedroom_robin", outside=False, forbid_outfit=["swim"], forbid_exposed=False, loc_type="room")

    if game_version < "0.3.1.04":
        python:
            for i in npc_all:
                setattr(i, "preg_who", {})
                setattr(i, "babies_who", {})

    if game_version < "0.3.1.06":
        $ item_pants_7 = Item("STRIP THONG", "A pair of thong knickers that only covers the strip area.", "item_pants_7", type="pants", value=40)
        $ item_top_22 = Item("SHEER DROP TOP", "A Thin top held loosely by thin shoulder straps and left to hang on the body.", "item_top_22", type="top", outfit=["daily", "party"], belly=True, pokenips=True, clevage=True, slutty=True, value=250)
        $ item_bottom_15 = Item("PLEATED MINI SKIRT", "A pleated micro mini skirt that doesn't offer a lot of modesty.", "item_bottom_15", type="bottom", outfit=["daily", "school", "party"], skirt=True, slutty=True, value=180)
        $ add_to_list(item_clothes_list, [item_pants_7, item_top_22, item_bottom_15])

        $ item_robin_package = Item("SLUTTY CLOTHES", "A couple of outfits that maybe even a highway whore would be ashamed to wear.", "item_robin_package", type="mission", icon="item_package")

        $ muff = Character('Muffled voice', color="#ffffff")
        $ distvoice = Character('Distant voice', color="#ffffff")

    if game_version < "0.3.1.07":
        $ robinman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy I got wild with while hanging out with Robin", virginname="some guy while hanging out with Robin")
    if game_version < "0.3.1.08":
        $ item_outfit_15 = Item("50's STYLE DRESS", "A modest dress associated with 1950's American housewives.", "item_outfit_15", type="outfit", outfit=["daily", "party"], skirt=True, value=260)
        $ item_socks_8 = Item("GARTER BELT AND STOCKINGS", "A classic garter belt holding up stockings.", "item_socks_8", type="socks", value=150)
        $ item_pants_8 = Item("HIGH LEG THONG", "A pair of high legged thong knickers.", "item_pants_8", type="pants", thong=True, value=60)
        $ item_pants_9 = Item("OPEN CROTCH PANTIES", "A sexy pair of crotchless knickers. Perfect for sexiness or easy access.", "item_pants_9", type="pants", pantsless=True, thong=True, value=150)
        $ item_bra_5 = Item("STRAPLESS SHELF BRA", "A bra that only acts as support and does little for modesty.", "item_bra_5", type="bra", clevage=True, braless=True, value=50)
        $ item_bra_6 = Item("OPEN FRONT BRA", "A sexy bra that gives support but also exposes your nipples. Perfect for a night out or in.", "item_bra_6", type="bra", clevage=True, braless=True, value=150)
        $ item_top_23 = Item("LOOSE SPORTS TOP", "A thin and loose sports top allowing for excellent mobility and breathability.", "item_top_23", type="top", outfit=["daily", "sport", "home"], belly=True, pokenips=True, clevage=True, value=250)
        $ item_bottom_16 = Item("SPORTY SHORTS", "A short pair of shorts that allow excellent mobility while working out.", "item_bottom_16", type="bottom", outfit=["daily", "sport", "home"], ass=True, slutty=True, value=180)
        $ add_to_list(item_clothes_list, [item_outfit_15, item_socks_8, item_pants_8, item_pants_9, item_bra_5, item_bra_6, item_top_23, item_bottom_16])
    if game_version < "0.3.1.09":
        $ item_socks_9 = Item("BUM HIGH SOCKS", "Socks that go right up to the persons crotch. Can be mistaken for leggings.", "item_socks_9", type="socks", value=100)
        $ item_pants_10 = Item("LOW RIDE PANTS", "A pair of underwear designed to be worn very low on the hips.", "item_pants_10", type="pants", value=80)
        $ add_to_list(item_clothes_list, [item_socks_9, item_pants_10])
    if game_version < "0.3.1.10":
        $ mateo = Npc(fname="Mateo", sname="Garcia", skinbase=(0.902, 0.659, 0.608), skinshad=(0.745, 0.475, 0.443), bio_image="mateo", bio_group="beach",
        bio_text="A poser on the beach that sometimes plays volleyball. Though probably spends more time ogling the girls than actually playing.")
        $ kaan = Npc(fname="Kaan", sname="Demir", skinbase=(0.725, 0.529, 0.463), skinshad=(0.631, 0.4, 0.341), bio_image="kaan", bio_group="beach",
        bio_text="A prettyboy who hangs out at the beach. Spends his days posing and his nights drinking.")
    if game_version < "0.3.1.11":
        $ item_top_24 = Item("FORM FITTING SWEATER", "A thin and form fitting sweater. Perfect for chilly nights or working out in the winter", "item_top_24", type="top", outfit=["daily", "sport", "home"], pokenips=True, value=250)
        $ item_top_25 = Item("LONG VEST", "A thin and form fitting sweater. Perfect for chilly nights or working out in the winter", "item_top_25", type="top", outfit=["daily", "sport", "home"], pokenips=True, value=250)
        $ item_top_26 = Item("SLEEVELESS SHIRT", "A collared sleeveless shirt with a pointed lower trim.", "item_top_26", type="top", outfit=["daily", "school", "party"], pokenips=True, value=250)
        $ item_bottom_17 = Item("FLARED SHORTS", "A heavily flared pair of shorts giving maximum movement and freedom. Often mistaken for a skirt.", "item_bottom_17", type="bottom", outfit=["daily", "sport", "home"], ass=True, slutty=True, value=180)
        $ item_bottom_18 = Item("TORN JEAN SHORTS", "Stylishly torn jean shorts.", "item_bottom_18", type="bottom", outfit=["daily", "party"], ass=True, value=180)
        $ item_bottom_19 = Item("FRILLY TIGHT SKIRT", "A form fitting but smart looking skirt with lower frills.", "item_bottom_19", type="bottom", outfit=["daily", "party", "school"], ass=True, skirt=True, value=180)
        $ item_socks_10 = Item("POINTED THIGH HIGHS", "Set of thigh high socks/stockings with a pointed front.", "item_socks_10", type="socks", value=100)
        $ item_socks_11 = Item("DIAMOND THIGH HIGHS", "Set of thigh high socks/stockings with a diamond pattern front.", "item_socks_11", type="socks", value=100)
        $ item_pants_11 = Item("C STRING", "A very discreet and uncomfortable set of underwear.", "item_pants_11", type="pants", thong=True, value=80)
        $ item_pants_12 = Item("CROSS STRING", "A small thong with a cross string pattern at the front.", "item_pants_12", type="pants", thong=True, value=80)
        $ item_bra_7 = Item("STRING FRONT BRA", "A top masquerading as a bra. Covers breasts and not a lot else.", "item_bra_7", type="bra", clevage=True, value=150)
        $ item_hat_5 = Item("VISOR HAT", "An open headed cap with a beak to help block the sun but stay cool.", "item_hat_5", type="hat", value=100, fringe=False)
        $ item_hat_6 = Item("WIDE BRIM SUN HAT", "A large hat for wearing in the sun to keep cool and protect from sunburn.", "item_hat_6", type="hat", value=100, hair="loose")
        $ add_to_list(item_clothes_list, [item_top_24, item_top_25, item_top_26, item_bottom_17, item_bottom_18, item_bottom_19, item_socks_10, item_socks_11])
        $ add_to_list(item_clothes_list, [item_pants_11, item_pants_12, item_bra_7, item_hat_5, item_hat_6])

        python:
            for i in item_clothes_list:
                i.hat_fringe = True
        $ item_hat_1.hat_hair = "loose"
        $ item_hat_2.hat_hair = "loose"
        $ item_hat_6.hat_hair = "loose"
        $ item_hat_5.hat_fringe = False
        $ player._hair_fringe = 2
        $ player.hair_fringe_default = player.hair_fringe

    if game_version < "0.3.1.12":
        $ player.having_sex = False
        $ item_coat_1 = Item("COAT", "Description to follow.", "item_coat_1", type="coat", value=500)
        $ item_coat_2 = Item("COAT", "Description to follow.", "item_coat_2", type="coat", value=500)
        $ item_coat_3 = Item("COAT", "Description to follow.", "item_coat_3", type="coat", value=500)
        $ item_coat_4 = Item("LONG COAT", "A thigh length coat with a high collar for keeping warm.", "item_coat_4", type="coat", value=500)
        $ add_to_list(item_clothes_list, [item_coat_1, item_coat_2, item_coat_3, item_coat_4])
        $ item_robin_package.type = "mission"

    if game_version < "0.3.1.13":
        $ erika = Npc(fname="Erika", sname="Schmidt", love=0, bio_image="erika", bio_group="beach",
        bio_text="Likes to hang out by the lake playing volleyball and drinking.", 
        is_female=True)
        $ zahra = Npc(fname="Zahra", sname="Adel", love=0, bio_image="zahra", bio_group="beach",
        bio_text="Likes to hang out by the lake playing volleyball and drinking.", 
        is_female=True)
    if game_version < "0.3.1.15":
        $ girl_dummy_1 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
        $ girl_dummy_2 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
        $ girl_dummy_3 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
        $ girl_dummy_4 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
        $ girl_dummy_5 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
        $ girl_dummy_6 = Npc(fname="Dummy", sname="Girl", is_female=True, isslut=True)
    if game_version < "0.3.1.16":
        $ perk_period_late = PerkClass("Late period", "It is that time of the month... So why is nothing happening?", "perk_period_late")
        if player.has_perk(perk_period) and player.pregnant and not player.preg_knows:
            $ player.remove_perk(perk_period)
            $ player.add_perk(perk_period_late)
        $ perk_gagged = PerkClass("Gagged", "Mmmmff nnnngggfff aaahhh ffffmmmmm..", "perk_gagged", desire_min=150, desire_max=300)
        $ perk_slutty = PerkClass("Looking slutty", "I am dressed in a really revealing way. People no doubt think I am a slut.", "perk_slutty", desire_min=50, desire_max=150, confidence_add=5)
        $ perk_pervert = PerkClass("Perverted", "I look like a pervert.", "perk_pervert", desire_min=50, desire_max=150, confidence_add=-5)
        python:
            for i in item_clothes_list:
                i.sexual = False
                i.perverted = False
                i.gagged = False


    if game_version < "0.3.1.18":
        python:
            for i in npc_all:
                i.can_sex = False
                i.can_gift = False
                i.abort = False
    if game_version < "0.3.1.19":
        $ item_hat_7 = Item("BUNNY EARS", "A set of bunny ears.", "item_hat_7", type="hat", value=100)
        $ item_socks_12 = Item("CASINO SOCKS", "A set of reverse bunny socks reaching up past the bum.", "item_socks_12", type="socks", value=150)
        $ item_outfit_16 = Item("CASINO DRESS", "A short and low cut dress worn by the servers at the casino", "item_outfit_16", type="outfit", outfit=["daily", "party"], skirt=True, clevage=True, slutty=True, pokenips=True, value=260)
        $ item_gloves_3 = Item("CASINO GLOVES", "A set of gloves/cuffs worn at the casino.", "item_gloves_3", type="gloves", value=40, locked=True)
        $ item_coat_5 = Item("CASINO SERVER COAT", "A coat worn in the casino.", "item_coat_5", type="coat", value=500)
        $ item_glasses_6 = Item("CASINO MASK", "A mask used to hide my identity while still allowing people to see most of my face.", "item_glasses_6", type="glasses", value=350)

        $ add_to_list(item_clothes_list, [item_hat_7, item_socks_12, item_outfit_16, item_gloves_3, item_coat_5, item_glasses_6])
        python:
            for i in npc_all:
                i.can_sex = False
                i.can_gift = False
    if game_version < "0.3.1.20":
        $ oskar = Npc(fname="Oskar", sname="Bergstrom", bio_image="oskar", bio_group="flatmate",
        bio_text="The landlord of the flat The Institute set me up in.")
    if game_version < "0.3.1.22":
        $ item_socks_13 = Item("HIGH WAIST LEGGINGS", "A pair of simple leggings for the cold weather.", "item_socks_13", type="socks", value=150)
        $ item_outfit_17 = Item("CORSET DRESS", "A short dress with a corset upper body that enhances form and shows off more than just a litle.", "item_outfit_17", type="outfit", outfit=["daily", "party"], skirt=True, clevage=True, slutty=True, pokenips=True, value=260)
        $ item_outfit_18 = Item("BUNNY LEOTARD", "A skimpy leotard wit a bunny tail.", "item_outfit_18", type="outfit", outfit=["daily", "party"], clevage=True, thong=True, slutty=True, pokenips=True, value=300)
        $ item_bottom_20 = Item("HIGH WAIST PENCIL SKIRT", "A high wasted low cut skirt for professional wear.", "item_bottom_20", type="bottom", outfit=["daily", "party", "school"], ass=True, skirt=True, slutty=True, value=250)
        $ item_coat_6 = Item("WAISTCOAT", "An elegant waistcoat perfect for formal occasions.", "item_coat_6", type="coat", value=500)
        $ item_choker_4 = Item("BOW TIE COLLAR", "A shirt collar with a bow tie.", "item_choker_4", type="choker", value=150)
        $ add_to_list(item_clothes_list, [item_socks_13, item_outfit_17, item_outfit_18, item_bottom_20, item_coat_6, item_choker_4])
    if game_version < "0.3.1.24":
        $ loc_revel_backstreet = Location("Revel backstreet", "loc_revel_backstreet", can_whore=True, can_sleep=True, can_eat=True)
    if game_version < "0.3.1.25":
        $ loc_office_ll = Location("Landlord's office", "loc_office_ll", outside=False, population=0, opening_hours=[9,10,11,12,13,14,15], events=False)
        $ dis_home_area = District("dis_home_area", "loc_stairwell", 0, ["loc_stairwell", "loc_office_ll"])
        $ add_to_list(dis_residential.sub_districts, dis_home_area)
        $ loc_stairwell.district = dis_residential
        $ loc_office_ll.district = dis_residential
        $ loc_stairwell.desc = "Courtyard"

    if game_version < "0.3.1.26":
        $ quests = [ ]
        call quest_paying_rent_call from _call_quest_paying_rent_call_1
        $ log.addquests(quests)
    if game_version < "0.3.1.27":
        $ item_gloves_4 = Item("RUBBER GLOVES", "A set of rubber gloves for cleaning.", "item_gloves_4", type="gloves", value=10, locked=True)
        $ item_outfit_19 = Item("SHORTS DUNGAREES", "A pair of dungaree overalls in shorts design", "item_outfit_19", type="outfit", outfit=["daily"], ass=True, value=300)
        $ item_outfit_20 = Item("MAID DRESS", "A classic maid dress.", "item_outfit_20", type="outfit", outfit=["daily", "party", "home"], ass=True, clevage=True, thong=True, slutty=True, skirt=True, pokenips=True, value=700, locked=True)
        $ item_socks_14 = Item("MAID KNEE HIGH SOCKS", "A pair of knee high socks with a frill trim.", "item_socks_14", type="socks", value=150)
        $ item_hat_8 = Item("MAID BONNET", "A frilly maid bonnet.", "item_hat_8", type="hat", value=100)
    if game_version < "0.3.1.28":
        $ loc_office_ll_back = Location("Landlord's office back room", "loc_office_ll_back", outside=False, population=0, opening_hours=[9,10,11,12,13,14,15], events=False, locked=True)
        $ dis_home_area = District("dis_home_area", "loc_stairwell", 0, ["loc_stairwell", "loc_office_ll", "loc_office_ll_back"])
        $ loc_office_ll_back.district = dis_residential
        $ loc_stairwell.district = dis_residential
        $ loc_office_ll.district = dis_residential
    if game_version < "0.3.1.30":
        $ shops_create_list()
    if game_version < "0.3.1.31":
        $ add_to_list(dis_revel.locs, loc_revel_backstreet)
        $ loc_revel_backstreet.district = dis_revel
        $ perk_unwanted_preg = PerkClass("Unwanted pregnancy", "I am pregnant but would rather not be.", "perk_unwanted_preg")
        $ perk_wanted_preg = PerkClass("Happily pregnant", "I am pregnant and happy about it.", "perk_wanted_preg")
    if game_version < "0.3.1.32":
        $ quests = [ ]
        call quest_casino_call from _call_quest_casino_call_1
        $ log.addquests(quests)
    if game_version < "0.3.1.33":
        $ loc_school_darkroom.opening_hours = irange(15,20)
    if game_version < "0.3.1.34":
        $ quests = [ ]
        call quest_photo_call from _call_quest_photo_call_1
        $ log.addquests(quests)
    if game_version < "0.3.1.35":
        $ item_poison = Item("POISON", "A bottle of a very lethal poison.", "item_poison", type="consumable", value=500)
        $ item_beer_poison = Item("POISONED BEER", "A bottle of beer that has been poisoned.", "item_beer_poison", type="consumable", value=0)
    if game_version < "0.3.1.36":
        $ quests = [ ]
        call quest_dance_call from _call_quest_dance_call_1
        $ log.addquests(quests)
        if school_dance_quest_on_team:
            $ log.assign("The Sweet Girls")
    if game_version < "0.3.1.37":
        $ log._findquest(qid="Cosmetic what...?")._image = "cosmetic"
        $ log._findquest(qid="Tracking down Simon Banks")._image = "cosmetic"
    if game_version < "0.3.1.38":
        $ pub_waitress.dict["wear_pants"] = True
        $ pub_waitress.dict["wear_socks"] = True
    if game_version < "0.3.1.39":
        $ loc_school_field_back_isolate = Location("Behind lockers", "loc_school_field_back_isolate", loc_type="grass", population=0)
        $ dis_misc = District("dis_misc", "loc_alley", 30, ["loc_alley", "loc_bushes", "loc_cupboard", "loc_rocks", "loc_school_field_back_isolate", "loc_gloryhole_stall"], map_enabled=False)
    if game_version < "0.3.1.40":
        $ loc_shop_tattoo = Location("Tattoo parlour", "loc_shop_tattoo", outside=False, opening_hours=irange(12,23), loc_type="plaster", events=False)
        $ loc_shop_funwear = Location("Funwear shop", "loc_shop_funwear", outside=False, opening_hours=irange(12,23), loc_type="plaster", events=False)
        $ add_to_list(dis_revel.locs, loc_shop_tattoo)
        $ add_to_list(dis_revel.locs, loc_shop_funwear)
        $ loc_shop_tattoo.district = dis_revel
        $ loc_shop_funwear.district = dis_revel
    if game_version < "0.3.1.41":
        $ item_energydrink = Item("Energy drink", "A high caffeine and sugar drink.", "item_energydrink", use_notif="Drank an energy drink", type="consumable", value=20)
        $ item_energyfood = Item("Cereal bar", "Oats mixed with syrup formed into a bar.", "item_energyfood", use_notif="Ate an energy bar", type="consumable", value=20)
        $ item_mag_ent = Item("Entertainment magazine", "A magazine about local news and happenings.", "item_mag_ent", use_notif="Read a magazine", type="consumable", value=50)
        $ item_mag_porn = Item("Porn magazine", "A home made magazine with pictures of minimally dressed people.", "item_mag_porn", use_notif="Read a magazine", type="consumable", value=100)
        $ loc_shop_corner = Location("Corner shop", "loc_shop_corner", loc_type="plaster", isolate_loc="loc_alley", outside=False, population=0, opening_hours=irange(8, 20), events=False)
        $ add_to_list(dis_residential.locs, loc_shop_corner)
        $ loc_shop_corner.district = dis_residential
    if game_version < "0.3.1.46":
        python:
            for i in npc_all:
                i.classname = Character(i._fname, callback=name_callback, cb_name=i._fname.lower(), image=If(i.bio_image, i.bio_image, i._fname))

    if game_version < "0.3.1.47":
        python:
            for i in npc_all:
                i.classname = Character(i.setname, callback=name_callback, cb_name=i._fname.lower(), image=If(i.bio_image, i.bio_image, i._fname))
                i._original_name = i._fname
    if game_version < "0.3.1.50":
        $ nurse = Npc(fname="Sede", sname="Lilly", rank="Nurse", is_female=True, bio_image="nurse", colour="#c0f2ff", bio_group="institute",
        bio_text="One of the first faces I saw when I woke up in The Institute following my near death, or actual death I suppose, experience.\n")
        $ psy = Npc(fname="Tess", sname="Brooker", rank="Dr.", is_female=True, bio_image="brooker", colour="#d3c0ff", bio_group="institute",
        bio_text="The Psychologist assigned to me by The Institute to look after my mental health...")
    if game_version < "0.3.1.51":
        python:
            for i in npc_all:
                i.dead_location = ""
                i.dead_message = ""
    if game_version < "0.3.1.52":
        $ receptionist = Npc(fname="Krystal", sname="Apatite", nname="Receptionist", is_female=True, bio_image="receptionist", colour="#ffc0ff", bio_group="institute", isslut=True,
        bio_text="The receptionist at the front desk of the hospital.")
    if game_version < "0.3.1.54":
        $ quests = [ ]
        call quest_cleaner_call from _call_quest_cleaner_call_1
        $ log.addquests(quests)
    if game_version < "0.3.1.56":
        python:
            for i in dis_home.locs:
                i._population = 0
    if game_version < "0.3.1.57":
        $ class_updater(Location, "clean_last", -500)
    if game_version < "0.3.1.59":
        $ quests = [ ]
        call quest_cleaner_call from _call_quest_cleaner_call_2
        $ log.addquests(quests)
    if game_version < "0.3.1.60":
        $ dis_home = District("dis_home", "loc_kitchen", 0, ["loc_bedroom", "loc_kitchen", "loc_common", "loc_bathroom", "loc_hallway", "loc_bedroom_robin"])
        python:
            for i in dis_home.locs:
                i.district = dis_residential
        if len(shop_list) > 30:
            $ shop_list = []
            call shops_call from _call_shops_call_2
    if game_version < "0.3.1.64":
        $ item_pants_13 = Item("FRILLY PANTIES", "A pair of frilly panties that goes well with the maid dress.", "item_pants_13", type="pants", value=100)
    if game_version < "0.3.1.65":
        python:
            for i in perk_list:
                i.wildcard = False



    if game_version < "0.3.2.01":
        $ oskar_thug = Npc(fname="Thug", sname="", colour="#da7a8a", pregname="I am carrying the child of one of the landlord's thugs", virginname="one of the landlords thugs", abort=True)

    if game_version < "0.3.2.03":
        $ item_hat_9 = Item("GHOST HEAD", "A spooky season ghost head.", "item_hat_9", type="hat", hair="bun", fringe=False, value=25)
        $ item_socks_15 = Item("POLKA DOT THIGH HIGHS", "A pair of polka dot thigh high socks.", "item_socks_15", type="socks", value=30)
        $ item_socks_16 = Item("POLKA AND STRIPED KNEE HIGHS", "A mixed pair of polka dot and striped thigh high socks.", "item_socks_16", type="socks", value=30)
        $ item_outfit_21 = Item("PUFF SLEEVED DRESS", "A dress with puffed sleeves and a low cut front.", "item_outfit_21", type="outfit", outfit=["daily", "party"], clevage=True, slutty=True, skirt=True, pokenips=True, value=350)
        $ item_outfit_22 = Item("T-SHIRT DRESS", "A dress in the style of a very long t-shirt.", "item_outfit_22", type="outfit", outfit=["daily", "party", "sport", "home"], skirt=True, pokenips=True, value=70)
        $ item_outfit_23 = Item("FRILLY DRESS", "An elegant, puffy skirt dress that is perfect for formal occasions.", "item_outfit_23", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, value=500)
        $ item_outfit_24 = Item("BUSTIER LOIN DRESS", "A bustier dress with a loin dress front and back.", "item_outfit_24", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, slutty=True, clevage=True, ass=True, value=350)
        $ item_outfit_25 = Item("GOTHIC DRESS", "A long, puffy and frilly dress in a gothic style.", "item_outfit_25", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, clevage=True, value=800)
        $ item_top_27 = Item("HEART PATCH TOP", "A top with heart patches.", "item_top_27", type="top", outfit=["daily", "sport", "home"], pokenips=True, value=50)
        $ item_top_28 = Item("HARLEQUIN TOP", "A top in a harlequin style.", "item_top_28", type="top", outfit=["daily", "sport", "home"], pokenips=True, value=50)
        $ item_top_29 = Item("RAGGED T-SHIRT", "A t-shirt that is mostly rags now.", "item_top_29", type="top", pokenips=True, slutty=True, value=5)
        $ item_top_30 = Item("BOOB WINDOW TOP", "A loose shoulder hung top with a boob window.", "item_top_30", type="top", outfit=["daily", "party"], pokenips=True, clevage=True, value=130)
        $ item_top_31 = Item("CROPPED HOODIE", "A fairly simple hoodie that has been cropped, leaving te belly and underboob exposed.", "item_top_31", type="top", outfit=["daily", "sport", "home"], clevage=True, belly=True, slutty=True, value=200)
        $ item_bottom_21 = Item("HEART PATCH SHORTS", "A pair of comfortable shorts with heart patches on them.", "item_bottom_21", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=50)
        $ item_bottom_22 = Item("HARLEQUIN SHORTS", "A pair of shorts in a harlequin style.", "item_bottom_22", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=50)
        $ item_bottom_23 = Item("LOW RISE JEANS", "A pair of form fitting low rise jeans.", "item_bottom_23", type="bottom", outfit=["daily", "party", "school"], ass=True, value=200)
        $ item_bottom_24 = Item("RAGGED JEANS", "What was once a pair of form fitting jeans is now mostly holes.", "item_bottom_24", type="bottom", outfit=["daily", "party", "school"], ass=True, slutty=True, value=10)
        $ item_bottom_25 = Item("RIPPED SKIRT", "Some rags fashioned into a makeshift skirt.", "item_bottom_25", type="bottom", ass=True, slutty=True, skirt=True, value=5)
        $ item_bottom_26 = Item("SWEAT PANTS", "A low rise pair of workout sweat pants.", "item_bottom_26", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=60)
        $ item_bottom_27 = Item("WORKOUT SHORTS", "A simple pair of sweat shorts for working out in.", "item_bottom_27", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=60)
    if game_version < "0.3.2.04":
        $ item_bra_8 = Item("HOMEMADE WRAP BRA", "A bra made of scrap cloth.", "item_bra_8", type="bra", clevage=True, value=10)
        $ item_pants_14 = Item("HOME MADE WRAP KNICKERS", "A pair of knickers using scrap cloth.", "item_pants_14", type="pants", thong=True, value=10)
        $ item_pants_15 = Item("STRAPPY UNDERWEAR", "A pair of knickers with strappy sides.", "item_pants_15", type="pants", thong=True, value=80)
        $ item_outfit_26 = Item("HIGH LEG DRESS", "A low cut dress with a very high leg line.", "item_outfit_26", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, clevage=True, ass=True, slutty=True, value=400)
        $ item_outfit_27 = Item("CHEONGSAM", "A traditional chinese dress.", "item_outfit_27", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, value=600)
        $ item_outfit_28 = Item("ORIENTAL DRESS", "A sexualised version of a traditional oriental dress.", "item_outfit_28", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, slutty=True, clevage=True, ass=True, value=250)
        $ item_top_32 = Item("MESH TOP", "A form fitting top with a mesh window.", "item_top_32", type="top", outfit=["daily", "sport", "party", "home"], clevage=True, belly=True, slutty=True, value=200)
        $ item_top_33 = Item("STRAPPY TOP", "A short top with cross style shoulder straps.", "item_top_33", type="top", outfit=["daily", "sport", "party", "home"], clevage=True, belly=True, slutty=True, value=200)
        $ item_top_34 = Item("BUSTIER TOP", "A strapless bustier top.", "item_top_34", type="top", outfit=["daily", "party", "home"], clevage=True, belly=True, slutty=True, value=200)
        $ item_top_35 = Item("BOOB WINDOW TOP", "A tight top with a large boob window.", "item_top_35", type="top", outfit=["school", "daily", "party", "home"], clevage=True, belly=True, slutty=True, value=200)
    if game_version < "0.3.2.06":
        $ item_outfit_29 = Item("SHOULDER PUFF DRESS", "A modest dress with puffy shoulders.", "item_outfit_29", type="outfit", outfit=["daily", "party"], skirt=True, value=120)
        $ item_outfit_30 = Item("DEEP HALTER DRESS", "A halter dress with a deep v reaching the belly button.", "item_outfit_30", type="outfit", outfit=["daily", "party"], skirt=True, pokenips=True, clevage=True, slutty=True, value=300)
        $ item_outfit_31 = Item("WAISTBAND DRESS", "A dress with a large waistband.", "item_outfit_31", type="outfit", outfit=["daily", "party"], skirt=True, clevage=True, value=300)
        $ item_top_37 = Item("DEEP V T-SHIRT", "A t-shirt with a deep v neckline.", "item_top_37", type="top", outfit=["school", "daily", "party", "home"], pokenips=True, clevage=True, belly=True, slutty=True, value=80)
        $ item_top_38 = Item("SHOULDER TOP", "An off the shoulder top with long sleeves.", "item_top_38", type="top", outfit=["school", "daily", "party", "home"], pokenips=True, clevage=True, belly=True, slutty=True, value=80)
        $ item_bottom_29 = Item("HIGH BAND SWEATPANTS", "A high waisted pair of baggy sweatpants.", "item_bottom_29", type="bottom", outfit=["daily", "sport", "home"], value=150)
        $ item_bottom_30 = Item("HIGH WAIST MINISKIRT", "A high waist high hemline skirt.", "item_bottom_30", type="bottom", outfit=["school" ,"daily", "sport", "home"], ass=True, skirt=True, slutty=True, value=130)
    if game_version < "0.3.2.07":
        $ quests = [ ]
        call quest_mira_missing_call from _call_quest_mira_missing_call_1
        $ log.addquests(quests)
    if game_version < "0.3.2.08":
        $ paige = Npc(fname="Paige", sname="Williams", rank="P.C.", is_female=True, colour="#c3bcff", bio_image="paige", bio_group="police", 
        bio_text="A rookie that usually works the reception at the security office. Hopes to do something more but is not very well respected by her colleages.")
        $ fun_girl = Npc(fname="Salesgirl", sname="Funwear", colour="#fdbcff", is_female=True, iswhore=True)
        $ loc_changingroom = Location("Changing room", "loc_changingroom")
    if game_version < "0.3.2.09":

        $ rose = Npc(fname="Samira", sname="Touati", nname="Rose bud", colour="#ffd3f0", is_female=True, iswhore=True, bio_image="rose", bio_group="whore", 
        bio_text="One of the whores who works the highway.")
        $ charity = Npc(fname="Nilay", sname="Kaya", nname="Charity", colour="#ffd3d3", is_female=True, iswhore=True, bio_image="charity", bio_group="whore", 
        bio_text="One of the whores who works the highway.")
        $ kitty = Npc(fname="Anita", sname="Amaya", nname="Kitty", colour="#dad3ff", is_female=True, iswhore=True, bio_image="kitty", bio_group="whore", 
        bio_text="One of the whores who works the highway.")
        $ pursy = Npc(fname="Vivian", sname="Walker", nname="Pursy", colour="#d3e5ff", is_female=True, iswhore=True, bio_image="pursy", bio_group="whore", 
        bio_text="One of the whores who works the highway.")
        $ quests = [ ]
        call quest_whore_call from _call_quest_whore_call_1
        call polaroids_call from _call_polaroids_call_1
        $ log.addquests(quests)
    if game_version < "0.3.2.10":
        python:
            for i in npc_all:
                i._wname = ""
        $ cass._wname = "Gingersnap"
        $ mira._wname = "Perra"
    if game_version < "0.3.2.12":
        $ log.deletequest("Photo model", "Jobs")
        $ log.deletequest("Photo model", "Jobs")
        $ quests = [ ]
        call quest_photo_intro_call from _call_quest_photo_intro_call_1
        call quest_photo_call from _call_quest_photo_call_2
        $ log.addquests(quests)
        $ item_polaroid_blank = Item("BLANK POLAROIDS", "Blank polaroids ready for use in a camera.", "item_polaroid_blank", type="consumable", value=10)
        $ item_polaroid_camera = Item("POLAROID CAMERA", "A camera that makes instant photos.", "item_polaroid_camera", type="tool", value=200)
    if game_version < "0.3.2.13":
        $ item_polaroid_taken = Item("POLAROID PHOTO", "Photos I have taken on my camera.", "item_polaroid_taken", type="tool", stackable=True, value=20)
        $ quests = [ ]
        call quest_photo_first_call from _call_quest_photo_first_call_1
        $ log.addquests(quests)
        $ item_mag_felix = Item("Blaston special magazine", "A newly made magazine with pictures of minimally dressed people and local news.", "item_mag_felix", use_notif="Read a magazine", type="consumable", value=100)
    if game_version < "0.3.2.16":
        $ quests = [ ]
        call quest_exhib_call from _call_quest_exhib_call_1
        $ log.addquests(quests)
    if game_version < "0.3.2.18":
        $ quests = [ ]
        call quest_robinslut_call from _call_quest_robinslut_call_1
        $ log.addquests(quests)
        $ loc_office_ll.opening_hours = irange(8,18)
    if game_version < "0.3.2.21":
        $ loc_office_pi = Location("Private Investigator", "loc_office_pi", outside=False, opening_hours=irange(12,23), loc_type="room", events=False)
        $ loc_office_pi_back = Location("P.I. back room", "loc_office_pi_back", outside=False, loc_type="room", events=False, locked=True)
        $ add_to_list(dis_revel.locs, [loc_office_pi, loc_office_pi_back])
        $ loc_office_pi.district = dis_revel
        $ loc_office_pi_back.district = dis_revel
    if game_version < "0.3.2.22":
        $ perk_freeuse = PerkClass("Free use", "I have decided to be free use. I will never turn down offers for sex and will never accept money for it.", "perk_freeuse", confidence_add=20, desire_max=400, allure_add=100)

        $ loc_flat1 = Location("Some guys flat", "loc_flat1", loc_type="room", population=0, outside=False, events=False)
        $ loc_flat2 = Location("Some guys flat", "loc_flat2", loc_type="room", population=0, outside=False, events=False)
        $ loc_flat3 = Location("Some guys flat", "loc_flat3", loc_type="room", population=0, outside=False, events=False)
        $ loc_flat4 = Location("Some guys flat", "loc_flat4", loc_type="room", population=0, outside=False, events=False)
        $ loc_flat5 = Location("Some guys flat", "loc_flat5", loc_type="room", population=0, outside=False, events=False)

        $ loc_slumtent = Location("Some guys tent", "loc_slumtent", loc_type="room", population=0, outside=False, events=False)

        $ loc_lorry = Location("Back of a lorry", "loc_lorry", loc_type="room", population=0, outside=False, events=False)
        $ add_to_list(dis_misc.locs, [loc_flat1, loc_flat2, loc_flat3, loc_flat4, loc_flat5, loc_slumtent, loc_lorry])

        $ loc_list = []
        $ loc_diner = Location("Truck stop diner", "loc_diner", loc_type="plaster", can_eat=True)
        $ loc_diner_toilet_girls = Location("Women's toilet", "loc_diner_toilet_girls", loc_type="tile", can_gloryhole=True)
        $ loc_diner_toilet_boys = Location("Men's toilet", "loc_diner_toilet_boys", loc_type="tile", can_gloryhole=True)
        $ loc_diner_changingroom = Location("Diner changingroom", "loc_diner_changingroom", loc_type="plaster")

        $ dis_diner = District("dis_diner", "loc_diner", 40, loc_list)

        $ loc_list = []
        $ loc_motel = Location("Motel", "loc_motel", loc_type="plaster")
        $ loc_motel_lobby = Location("Motel lobby", "loc_motel_lobby", loc_type="plaster")
        $ loc_motel_pool = Location("Motel pool", "loc_motel_pool", loc_type="plaster")
        $ loc_motel_room = Location("Motel room", "loc_motel_room", outside=False, locked=True, loc_type="room")
        $ loc_motel_pinkroom = Location("Motel pink room", "loc_motel_pinkroom", outside=False, locked=True, loc_type="room")

        $ dis_motel = District("dis_motel", "loc_motel", 40, loc_list)

        $ loc_list = []
        $ loc_truckstop = Location("Truck stop", "loc_truckstop", can_whore=True, can_loiter=True, can_sleep=True)
        $ loc_highway = Location("Highway overpass", "loc_highway", can_whore=True, can_loiter=True)
        $ loc_highway_slum = Location("Highway slum", "loc_highway_slum", can_sleep=True)
        $ loc_busstop_truckstop = Location("Bus stop", "loc_busstop_truckstop")

        $ dis_truckstop = District("dis_truckstop","loc_truckstop", 60, loc_list, sub_districts=[dis_diner, dis_motel])
    if game_version < "0.3.2.23":

        $ loc_truckstop_truck_1 = Location("Between the trucks", "loc_truckstop_truck_1", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry")
        $ loc_truckstop_truck_2 = Location("Between the trucks", "loc_truckstop_truck_2", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_1")
        $ loc_truckstop_truck_3 = Location("Between the trucks", "loc_truckstop_truck_3", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_1")
        $ loc_truckstop_truck_4 = Location("Between the trucks", "loc_truckstop_truck_4", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_2")
        $ loc_truckstop_truck_5 = Location("Between the trucks", "loc_truckstop_truck_5", loc_type="conc", population=0, events=False, isolate_loc="loc_lorry_2")


        $ loc_lorry_1 = Location("Back of a lorry", "loc_lorry_1", loc_type="room", population=0, outside=False, events=False)
        $ loc_lorry_2 = Location("Back of a lorry", "loc_lorry_2", loc_type="room", population=0, outside=False, events=False)
        python:
            for i in [loc_truckstop_truck_1, loc_truckstop_truck_2, loc_truckstop_truck_3, loc_truckstop_truck_4, loc_truckstop_truck_5, loc_lorry, loc_lorry_1, loc_lorry_2]:
                i.district= dis_misc

        $ add_to_list(dis_misc.locs, [loc_truckstop_truck_1, loc_truckstop_truck_2, loc_truckstop_truck_3, loc_truckstop_truck_4, loc_truckstop_truck_5, loc_lorry, loc_lorry_1, loc_lorry_2])
        $ motel_recep = Npc(fname="Receptionist", sname="Motel", colour="#fdbcff", is_female=True)

        $ loc_motel_shower = Location("Motel shower", "loc_motel_shower", outside=False, loc_type="tile", population=0, events=False)
        $ add_to_list(dis_motel.locs, loc_motel_shower)
        $ loc_motel_shower.district = dis_truckstop

    if game_version < "0.3.2.25":
        $ item_blindfold = Item("BLINDFOLD", "A makeshift blindfold for... Blindfolding.", "item_blindfold", type="tool", value=20)
        $ item_bdsm = Item("BINDINGS", "A set of bindings for bedroom fun.", "item_bdsm", type="tool", value=300)
        $ item_pregband = Item("MATERNITY BAND", "A band that helps support my back and baby bump", "item_pregband", type="tool", value=300)
        $ item_ballgag = Item("BALLGAG", "A simple ballgag designed to silence people. Drooling optional.", "item_ballgag", type="tool", value=550)
        $ item_ballgag_locked = Item("LOCKABLE BALLGAG", "A ballgag designed to silence people. Has a lock on the back preventing it being opened. Doesn't have a key", "item_ballgag_locked", type="tool", value=300)
        $ item_outfit_32 = Item("LATEX CATSUIT", "A full body latex catsuit. Shiny.", "item_outfit_32", type="outfit", outfit=["daily", "party"], ass=True, slutty=True, pokenips=True, value=300)
        $ item_outfit_33 = Item("LATEX DRESS", "A latex dress. Shiny.", "item_outfit_33", type="outfit", outfit=["daily", "party"], ass=True, slutty=True, skirt=True, pokenips=True, value=300)
        $ item_outfit_34 = Item("LATEX OPEN DRESS", "A latex dress with an open boob window. Shiny.", "item_outfit_34", type="outfit", outfit=["daily", "party"], ass=True, slutty=True, skirt=True, pokenips=True, value=300)
        $ item_top_39 = Item("LATEX TOP", "A long sleeve, latex crop top. Shiny.", "item_top_39", type="top", outfit=["daily", "party"], slutty=True, pokenips=True, value=100)
        $ item_bottom_31 = Item("LATEX TROUSERS", "A pair of latex trousers. Shiny.", "item_bottom_31", type="bottom", outfit=["daily", "party"], ass=True, slutty=True, value=130)

        $ perk_pregband_preg = PerkClass("Belly support", "Ahh, so much better on my back.", "perk_pregband", confidence_add=5, mood_add=10)
        $ perk_pregband_notpreg = PerkClass("Belly support", "Ahh, so much better on my back.", "perk_pregband", fitness_add=5)
        $ perk_gagged_locked = PerkClass("Gagged", "Mmmmff nnnngggfff aaahhh ffffmmmmm...", "perk_gagged_locked", desire_min=150, desire_max=300, allure_add=200, int_max=-200, int_add=-200, confidence_add=-30)
        $ perk_blind = PerkClass("Blindfolded", "I can't see a thing!", "perk_blind", confidence_add= -100, fitness_add= -100)

        $ loc_junk_1.can_whore=True
        $ dis_junkyard.add_whore_locations()
        show screen foreground_scene(_layer="fg_bg_screen") 

    if game_version < "0.3.2.26":
        $ item_pinkticket = Item("PINK TICKET", "Tickets I have earned though working in a pink room. Exchange at the motel reception.", "item_pinkticket", type="consumable", value=200)
        $ item_mira_intel = Item("MIRA INTEL NOTES", "Notes about what I have discovered while investigating Mira's disappearance.", "item_mira_intel", type="mission", stackable=True)

    if game_version < "0.3.2.28":
        $ streetpervert = Npc(fname="Pervert", sname="", pregname="I am carrying the child of a pervert who I let fuck me in the bushes", virginname="some random pervert who fucked me", abort=True)
        $ quest_temp = None
    if game_version < "0.3.2.29":
        $ item_tissue = Item("Tissues", "A pack of pocket tissues.", "item_tissue", type="consumable", value=2)

        $ loc_motel_pinkroom2 = Location("Motel pink room", "loc_motel_pinkroom2", outside=False, locked=True, loc_type="room", population=0, events=False)
        $ loc_motel_room2 = Location("Motel room", "loc_motel_room2", outside=False, locked=True, loc_type="room", population=0, events=False)

        $ add_to_list(dis_truckstop.locs, [loc_motel_pinkroom2, loc_motel_room2])
        $ add_to_list(dis_motel.locs, [loc_motel_pinkroom2, loc_motel_room2])
        $ loc_motel_pinkroom2.district = dis_truckstop
        $ loc_motel_room2.district = dis_truckstop

    if game_version < "0.3.2.32":
        $ item_outfit_35 = Item("T-SHIRT DRESS", "A dress with a t-shirt design. Has straps and a collar for detail.", "item_outfit_35", type="outfit", outfit=["daily", "party"], ass=True, skirt=True, pokenips=True, value=250)
        $ item_outfit_36 = Item("HIGH LEG GOWN", "A gown with a high let slit. Low cut with sleeves", "item_outfit_36", type="outfit", outfit=["daily", "party"], ass=True, skirt=True, slutty=True, pokenips=True, value=400)
        $ item_socks_17 = Item("KNEE PADS", "Perfect for when you spend a lot of time on your knees", "item_socks_17", type="socks", value=50)
        $ item_socks_18 = Item("CAT SOCKS", "A cute pair of socks with cat ears and cat face. Meow!", "item_socks_18", type="socks", value=50)
        $ item_socks_19 = Item("LATEX BOOTS", "A pair of thigh high latex boots. Shiny!", "item_socks_19", type="socks", value=100)
    if game_version < "0.3.2.33":
        python:
            for i in npc_all:
                i.hour_number = 1
                i.day_number = 1
                i.noon_number = 1

    if game_version < "0.3.2.35":
        $ loc_list = []

        $ loc_highway_slum = Location("Highway slum", "loc_highway_slum", can_sleep=True)
        $ loc_highway_slum_still = Location("Slum still", "loc_highway_slum_still", outside=False, population=0, events=False, loc_type="room", opening_hours=(15,16,17,18,19,20,21,22,23,0,1,2,3))
        $ dis_slum = District("dis_slum", "loc_highway_slum", 40, loc_list)
        $ loc_list = dis_truckstop._locs
        $ dis_truckstop = District("dis_truckstop","loc_truckstop", 60, loc_list, sub_districts=[dis_diner, dis_motel, dis_slum])

        $ havenvik.inv.shop_list = [
        [item_beer, 30],
        [item_brew, 100], 
        [item_cigs, 100],
        [item_joy, 5],
        [item_lebo, 1], 
        [item_abort_pill, 2],
        item_pepperspray,
        ]
        $ havenvik.inv.stock()

    if game_version < "0.3.2.36":

        $ loc_highway_slum_street = Location("Slum row", "loc_highway_slum_street", can_sleep=True)
        $ add_to_list(dis_slum.locs, loc_highway_slum_street)
        $ loc_highway_slum_street.district = dis_truckstop

        $ loc_list = []
        $ loc_walk_junk_rails = Location("Abandoned rails", "loc_walk_junk_rails", outside=False, locked=True, population=0)
        $ loc_walk_slum_pipe = Location("Sewer pipe", "loc_walk_slum_pipe", locked=True, population=0)
        $ dis_walk = District("dis_walk", "loc_walk_junk_rails", 80, loc_list, map_enabled=False)

    if game_version < "0.3.2.37":
        $ whore = Npc(fname="Patron", sname="", colour="#fdbcff", is_female=True, iswhore=True)

    if game_version < "0.3.2.40":
        $ item_coat_7 = Item("HEAVY SWEATER", "A very heavy sweater, useful as a coat in winter.", "item_coat_7", type="coat", value=500)
        $ item_coat_8 = Item("BODY WARMER HOODIE", "A hoodie with no sleeves. Perfect for when it gets cold during summer nights.", "item_coat_8", type="coat", value=500)
        $ item_coat_9 = Item("ZIP HOODIE", "A front zip hoodie", "item_coat_9", type="coat", value=500)
        $ item_coat_10 = Item("CROPPED HOODIE", "A fairly simple hoodie that has been cropped, leaving the belly and underboob exposed.", "item_coat_10", type="coat", clevage=True, belly=True, value=500)

        $ item_outfit_37 = Item("CRUMPLE DRESS", "A dress with a crumple effect", "item_outfit_37", type="outfit", outfit=["daily", "party"], ass=True, skirt=True, slutty=True, pokenips=True, value=400)

        $ item_gloves_5 = Item("ELBOW PADS", "A pair of elbow pads.", "item_gloves_5", type="gloves", value=50, locked=True)

        $ item_top_40 = Item("T-SHIRT", "A simple t-shirt like the one Jaylee wears", "item_top_40", type="top", outfit=["daily", "sport", "home"], value=50)

        $ item_bottom_32 = Item("JEAN SHORTS", "A pair of jean shorts similar to the ones Jaylee wears.", "item_bottom_32", type="bottom", outfit=["daily"], ass=True, value=130)
    if game_version < "0.3.2.41":
        $ item_coat_11 = Item("BOYFRIEND T-SHIRT", "An over sized t-shirt usually stolen from a man. Does not come with boyfriend smell.", "item_coat_11", type="coat", value=300)
        $ item_coat_12 = Item("BEAR ONESIE", "A big fluffy onesie that looks like a bear.", "item_coat_12", type="coat", value=500)
        $ item_outfit_38 = Item("ROMPER", "A one piece romper", "item_outfit_38", type="outfit", outfit=["daily", "party", "home"], ass=True, pokenips=True, value=400)
        $ item_outfit_39 = Item("RUFFLED BABYDOLL", "A sheer pair of pyjamas with ruffles barely leaving something to the imagination.", "item_outfit_39", type="outfit", outfit=["daily", "party", "home"], ass=True, skirt=True, slutty=True, clevage=True, value=200)
        python:
            for i in item_clothes_list:
                i.covers_top = False
                i.covers_bottom = False
            for i in item_list:
                i.covers_top = False
                i.covers_bottom = False
    if game_version < "0.3.2.43":
        $ pinkroom_man = Npc(fname="Punter", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True)
        $ pinkroom_man2 = Npc(fname="Customer", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True)
        $ pinkroom_man3 = Npc(fname="Guy", sname="", pregname="I am carrying the child of a punter I had sex with in a pink room", virginname="a pinkroom punter", abort=True)

        $ pinkroom_tiedtrain = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me while I was tied up and men were taking turns fucking me", virginname="a pinkroom punter while I was tied up and taken turns on", abort=True)
        $ pinkroom_group = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me as part of a pinkroom gangbang", virginname="a group of guys who gangbanged me", abort=True)

        $ item_pinkticket.value=50
    if game_version < "0.3.2.44":
        $ guy_tiedtrain = Npc(fname="Punter", sname="", pregname="I am carrying the child of someone who fucked me while I was tied up and men were taking turns fucking me", virginname="a guy while I was tied up and taken turns on", abort=True)
    if game_version < "0.3.2.45":
        $ perk_despondent = PerkClass("Despondent", "I really need to do something to pick me up.", "perk_despondent", mood_multi=2, desire_max= -400, allure_add= 400)
    if game_version < "0.3.2.47":
        $ punter = Npc(fname="Punter", sname="", pregname="I am carrying the child of one of some punter", virginname="some random punter", abort=True)
        $ whore = Npc(fname="Whore", sname="", colour="#fdbcff", is_female=True, iswhore=True)
    if game_version < "0.3.2.48":
        $ player.sex_holes = []
        $ player.sex_man_amount = 0
    if game_version < "0.3.2.49":
        $ guy_gangbang = Npc(fname="Guy", sname="", pregname="I am carrying the child of someone from a gangbang", virginname="a guy from a gangbang", abort=True)
        $ guy_gangbang_r = Npc(fname="Guy", sname="", pregname="I am carrying the child of one of the guys who gang raped me", virginname="a guy while I was gang raped", abort=True)





    if game_version < "0.3.3.05":
        call quest_exhib_update_call from _call_quest_exhib_update_call
        $ quest_update("A place to be alone")
        $ player.force_uncover = False
        $ player.force_cover = False

    if game_version < "0.3.3.10":

        python:
            for i in ["c", "school", "daily", "party", "sport", "swim", "home", "work", "shop", "temp_outfit"]:
                setattr(globals()[i], "_bsuit", 0)
                setattr(globals()[i], "bsuit_primary_colour", "custom3")
                setattr(globals()[i], "bsuit_secondary_colour", "custom10")
                setattr(globals()[i], "bsuit_primary_colour", "custom3")
                setattr(globals()[i], "bsuit_primary_trans", "trans_normal")
                setattr(globals()[i], "bsuit_secondary_trans", "trans_normal")

        $ school2 = Clothes()
        $ daily2 = Clothes()
        $ party2 = Clothes()
        $ sport2 = Clothes()
        $ swim2 = Clothes()
        $ home2 = Clothes()

        call clothes from _call_clothes

        $ player._pregnancy = 0

        $ clothing_colours["custom9"] = Color(rgb = (0.913, 0.513, 0.384))
        $ clothing_colours["custom10"] = Color(rgb = (1, 0.411, 0.705))
        $ clothing_colours["custom11"] = Color(rgb = (0.662, 0.168, 0.623))
        $ clothing_colours["custom12"] = Color(rgb = (0.929, 0.827, 0.207))

        python:
            for i in item_clothes_list:
                i.exposed_ass = False
                i.exposed_nips = False
                i.exposed_vag = False

        $ item_bra_1.exposed_nips = "pri"
        $ item_bra_5.exposed_nips=True
        $ item_bra_6 .exposed_nips=True
        $ item_bra_7.exposed_nips="pri"
        $ item_bra_10.exposed_nips="pri"
        $ item_bra_11.exposed_nips="pri"
        $ item_bra_12.exposed_nips="pri"

        $ item_pants_1.exposed_vag="pri"
        $ item_pants_2.exposed_vag="pri"
        $ item_pants_3.exposed_vag="pri"
        $ item_pants_4.exposed_vag="pri"
        $ item_pants_5.exposed_vag, item_pants_5.exposed_ass = "pri", True
        $ item_pants_6.exposed_vag, item_pants_6.exposed_ass = "pri", True
        $ item_pants_7.exposed_vag, item_pants_7.exposed_ass = "pri", True
        $ item_pants_8.exposed_vag, item_pants_8.exposed_ass = "pri", True
        $ item_pants_9.exposed_vag, item_pants_9.exposed_ass = True, True
        $ item_pants_10.exposed_vag, item_pants_10.exposed_ass = "pri", True
        $ item_pants_11.exposed_ass=True
        $ item_pants_12.exposed_ass=True
        $ item_pants_15.exposed_ass=True

        $ item_bsuit_1.exposed_ass, item_bsuit_1.exposed_nips = True, True
        $ item_bsuit_2.exposed_ass, item_bsuit_2.exposed_nips = True, True
        $ item_bsuit_3.exposed_ass, item_bsuit_3.exposed_nips, item_bsuit_3.exposed_vag = "pri", "pri", "pri"

        $ item_outfit_2.exposed_ass, item_outfit_2.exposed_vag, item_outfit_2.exposed_nips = "pri", "pri", "pri"
        $ item_outfit_4.exposed_nips, item_outfit_4.exposed_ass, item_outfit_4.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_8.exposed_nips, item_outfit_8.exposed_ass, item_outfit_8.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_9.exposed_nips, item_outfit_9.exposed_ass, item_outfit_9.exposed_vag = True, True, "pri"
        $ item_outfit_10.exposed_nips, item_outfit_10.exposed_ass, item_outfit_10.exposed_vag = "pri", "sec", "sec"
        $ item_outfit_11.exposed_nips, item_outfit_11.exposed_ass, item_outfit_11.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_12.exposed_nips, item_outfit_12.exposed_ass, item_outfit_12.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_24.exposed_nips, item_outfit_24.exposed_ass, item_outfit_24.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_26.exposed_nips, item_outfit_26.exposed_ass, item_outfit_26.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_28.exposed_nips, item_outfit_28.exposed_ass, item_outfit_28.exposed_vag = "pri", "pri", "pri"
        $ item_outfit_30.exposed_nips, item_outfit_30.exposed_ass, item_outfit_30.exposed_vag = True, "pri", "pri"
        $ item_outfit_39.exposed_nips, item_outfit_39.exposed_ass = True, True

        $ item_top_1.exposed_nips="pri"
        $ item_top_3.exposed_nips="pri"
        $ item_top_4.exposed_nips="pri"
        $ item_top_5.exposed_nips="pri"
        $ item_top_6.exposed_nips="pri"
        $ item_top_7.exposed_nips="pri"
        $ item_top_13.exposed_nips="pri"
        $ item_top_14.exposed_nips="pri"
        $ item_top_15.exposed_nips="pri"
        $ item_top_18.exposed_nips="pri"
        $ item_top_19.exposed_nips="pri"
        $ item_top_21.exposed_nips="pri"
        $ item_top_22.exposed_nips="pri"
        $ item_top_23.exposed_nips="pri"
        $ item_top_25.exposed_nips="pri"
        $ item_top_26.exposed_nips="pri"
        $ item_top_29.exposed_nips="pri"
        $ item_top_33.exposed_nips="pri"
        $ item_top_34.exposed_nips="pri"
        $ item_top_35.exposed_nips="pri"
        $ item_top_36.exposed_nips="pri"
        $ item_top_37.exposed_nips="pri"
        $ item_top_41.exposed_nips="pri"
        $ item_top_42.exposed_nips="pri"

        $ item_bottom_1.exposed_vag="pri"
        $ item_bottom_3.exposed_vag, item_bottom_3.exposed_ass = "pri", True
        $ item_bottom_11.exposed_vag, item_bottom_11.exposed_ass = "pri", "pri"
        $ item_bottom_14.exposed_ass=True
        $ item_bottom_19.exposed_vag, item_bottom_19.exposed_ass = "pri", "pri"
        $ item_bottom_25.exposed_ass=True
        $ item_bottom_28.exposed_vag, item_bottom_28.exposed_ass = "pri", True
        $ item_bottom_30.exposed_vag, item_bottom_30.exposed_ass = "pri", "pri"
        $ item_bottom_33.exposed_vag, item_bottom_33.exposed_ass = True, "pri"
        $ item_bottom_34.exposed_vag, item_bottom_34.exposed_ass = True, True

    if game_version < "0.3.3.12":
        $ player.skin_colour = "6_0_base"
        $ quest_list = []
        $ class_list_creator(QuestClass, "quest_list")
        python:
            for i in quest_list:
                i._bsuit = 0
                i.bsuit_primary_colour = "white"
                i.bsuit_secondary_colour = "white"

    if game_version < "0.3.3.13":
        $ skin_colours["6_0_base"] = Color(rgb = (0.976, 0.827, 0.729))
        $ skin_colours["6_0_shad"] = Color(rgb = (0.894, 0.709, 0.607))

        $ skin_colours["7_0_base"] = Color(rgb = (0.894, 0.709, 0.607))
        $ skin_colours["7_0_shad"] = Color(rgb = (0.752, 0.525, 0.447))

        $ skin_colours["8_0_base"] = Color(rgb = (0.545, 0.407, 0.333))
        $ skin_colours["8_0_shad"] = Color(rgb = (0.364, 0.258, 0.231))

        $ skin_colours["9_0_base"] = Color(rgb = (0.686, 0.509, 0.486))
        $ skin_colours["9_0_shad"] = Color(rgb = (0.490, 0.349, 0.352))

        $ skin_colours["10_0_base"] = Color(rgb = (0.972, 0.843, 0.717))
        $ skin_colours["10_0_shad"] = Color(rgb = (0.819, 0.627, 0.517))

        $ nipple_colours["9"] = Color(rgb = (0.854, 0.572, 0.462))
        $ nipple_colours["10"] = Color(rgb = (0.709, 0.458, 0.368))
        $ nipple_colours["11"] = Color(rgb = (0.286, 0.211, 0.192))
        $ nipple_colours["12"] = Color(rgb = (0.415, 0.301, 0.305))
        $ nipple_colours["13"] = Color(rgb = (0.741, 0.509, 0.380))

    if game_version < "0.3.3.14":
        python:
            for i in item_clothes_list:
                i.always_locked=False
            for i in perk_list:
                i.mins=None
        $ perk_smoking = PerkClass("Smoking", "I am having a cig.", "perk_smoking")
        $ item_cigs._last_used = 0

    if game_version < "0.3.3.15":
        $ loc_list = ["loc_park", "loc_park_toilet", "loc_park_toilet_boys", "loc_park_toilet_girls"]

        $ loc_park_path = Location("Park scenic path", "loc_park_path", can_whore=True, loc_type="grass", isolate_loc="loc_bushes")
        $ loc_park_gazebo = Location("Park gazebo", "loc_park_gazebo", can_whore=True, loc_type="grass", population=1, isolate_loc="loc_bushes")
        $ loc_park_toilet_girls_stall = Location("Women's toilet stall", "loc_park_toilet_girls_stall", outside=False, population=1, loc_type="tile", can_gloryhole=True)
        $ dis_park = District("dis_park", "loc_park", 30, loc_list)
        $ add_to_list(dis_residential.sub_districts, dis_park)
        $ dis_residential.add_sub_district_locs()
        $ dis_residential.add_locations()
        $ loc_park_toilet_boys.outside=False
        $ loc_park_toilet_girls.outside=False

        $ loc_list = dis_walk._locs
        $ loc_walk_park_forest = Location("Muddy path", "loc_walk_park_forest", outside=True, locked=True, population=0)
        $ loc_walk_school_forest = Location("Field trees", "loc_walk_school_forest", locked=True, population=0)
        $ loc_walk_park_shrubs = Location("Shrubbery", "loc_walk_park_shrubs", locked=True, population=0)
        $ loc_walk_lake_shrubs = Location("Sparse bushes", "loc_walk_lake_shrubs", locked=True, population=0)
        $ dis_walk.add_locations()

        $ loc_school_secret_entrance = Location("School secret entrance", "loc_school_secret_entrance", loc_type="grass", isolate_loc="loc_school_secret_entrance", events=False)
        $ add_to_list(dis_school._locs, "loc_school_secret_entrance")
        $ dis_school.add_locations()
        if school_soccer_quest_backentrance["used"]:
            $ loc_school_secret_entrance.locked = False

    if game_version < "0.3.3.16":
        $ streetpervert = Npc(fname="Pervert", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True)
        $ streetguy = Npc(fname="Guy", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True)
        $ streetman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy I met in the street", virginname="some random pervert who fucked me", abort=True)

    if game_version < "0.3.3.18":
        $ perk_lactating = PerkClass("Lactating", "I am lactating.", "perk_lactating", fertility_multi=0.5)
        $ perk_milky = PerkClass("Milky", "My breasts are full of milk. I really need to do something about that.", "perk_milky", mood_add=-5, allure_add=50)
    if game_version < "0.3.3.19":
        $ player.force_cover_breasts = False
        $ player.force_cover_vag = False

    if game_version < "0.3.3.21":
        $ hucow = Npc(fname="Milkmaid", sname="Hucow", colour="#d6d5b9", is_female=True, iswhore=True)

        $ item_choker_5 = Item("HUCOW COLLAR", "A bell collar like that of a cow.", "item_choker_5", type="choker", value=150, locked=True)
        $ item_gloves_6 = Item("HUCOW GLOVS", "A pair of elbow length gloves with a cow pattern.", "item_gloves_6", type="gloves", value=50, locked=True)
        $ item_socks_20 = Item("HUCOW SOCKS", "A pair of thigh high socks with a cow print.", "item_socks_20", type="socks", value=100, locked=True)
        $ item_pants_16 = Item("HUCOW PANTS", "A pair of knickers with a cow print.", "item_pants_16", type="pants", thong=True, value=80, exposed_ass=True, locked=True)
        $ item_bra_13 = Item("HUCOW BRA", "A bra that doesn't offer much support. But prevents milk leakage and has a cow pattern.", "item_bra_13", type="bra", clevage=True, value=50, locked=True)
        $ item_hat_10 = Item("HUCOW EARS", "Floppy cow ears.", "item_hat_10", type="hat", value=25, locked=True)

        $ item_breastpump = Item("BREAST PUMP", "A breast pump for bottling milk.", "item_breastpump", type="tool", stackable=False, value=150)
        $ item_scrap_milkbottle = Item("FULL MILK BOTTLE", "A bottle of breast milk", "item_scrap_milkbottle", type="junk", act="item_scrap_action", value=30)
        $ item_milkbottle_empty = Item("EMPTY MILK BOTTLE", "An empty bottle for use with a breast pump.", "item_milkbottle_empty", type="tool", stackable=True, value=5)
        $ item_milktab = Item("MILK TAB", "A weird pill that induces lactation.", "item_milktab", use_notif="Took a Milk tab", type="consumable", value=250)

        $ player.dict = {}
        $ player.list = []

        $ loc_market_stall_milk = Location("Milkmaid stall", "loc_market_stall_milk")
        $ add_to_list(dis_commercial._locs, "loc_market_stall_milk")
        $ loc_market_stall_milk.district = dis_commercial
        $ dis_revel.add_sub_district_locs()
        $ dis_revel.add_locations()

    if game_version < "0.3.3.22":
        $ mason = Npc(fname="Terry", sname="Mason", colour="#ad8181", skinbase=(0.898, 0.803, 0.760), skinshad=(0.827, 0.658, 0.639), bio_image="mason", bio_group="staff",
        bio_text="The volleyball coach at the academy.\nI don't really know much about him.")

    if game_version < "0.3.3.23":
        if 'beach_vball_asked' in globals() and beach_vball_asked:
            $ add_to_list(loc_beach_gym.list, "beach_vball_asked")

    if game_version < "0.3.3.24":
        $ perk_bitch = PerkClass("Bitch", "I am wearing clothes that indicate to those calling themselves \"the wolf pack\" that I am playing their game.", "perk_bitch", desire_min=50, desire_max=150, confidence_add=5, allure_add=50)
        $ item_choker_6 = Item("BITCH COLLAR", "A collar that indicates I am playing the wolf gauntlet. I will find myself in dangerous (but fun) situations wearing this.", "item_choker_6", type="choker", value=20, locked=True)
        $ quests = [ ]
        call quest_wolfgang_call from _call_quest_wolfgang_call
        $ log.addquests(quests)

    if game_version < "0.3.3.25":
        $ wolf = Npc(fname="Wolfman", sname="", pregname="I was bred by someone from the wolfgang", virginname="Some wolfgang stud", abort=True)

    if game_version < "0.3.3.26":
        $ item_top_43 = Item("MISS SANTA TOP", "A fluffy santa bustier.", "item_top_43", type="top", outfit=["daily", "sport", "home", "party"], clevage=True, belly=True, value=80)
        $ item_bottom_35 = Item("MISS SANTA SKIRT", "A skirt with a fluffy trim.", "item_bottom_35", type="bottom", outfit=["daily", "party", "sport", "home"], skirt=True, value=130)
        $ item_gloves_7 = Item("MISS SANTA GLOVES", "A pair of fluffy wrist warmers", "item_gloves_7", type="gloves", value=50)
        $ item_socks_21 = Item("MISS SANTA SOCKS", "A pair of thigh high socks with a fluffy top.", "item_socks_21", type="socks", value=100)

    if game_version < "0.3.3.31":
        $ dis_park._npc_desc = "At the park."
        $ dis_home._npc_desc = "Somewhere at home."
        $ dis_home_area._npc_desc = "Around the home area."
        $ dis_beach._npc_desc = "At the beach somewhere."
        $ dis_lake._npc_desc = "Around the lake area."
        $ dis_school._npc_desc = "At the academy somewhere."
        $ dis_pub._npc_desc = "At the pub."
        $ dis_hospital._npc_desc = "At the hospital."
        $ dis_commercial._npc_desc = "Around the shopping area."
        $ dis_revel._npc_desc = "Revel street somewhere."
        $ dis_motel._npc_desc = "At the hospital."
        $ dis_hospital._npc_desc = "The Motel somewhere."
        $ dis_slum._npc_desc = "In the slums."
        $ dis_truckstop._npc_desc = "Somewhere around the truck stop."
        $ dis_junkyard._npc_desc = "At the junkyard."
        $ dis_checkpoint._npc_desc = "At the security checkpoint."
        $ dis_haven._npc_desc = "Somewhere in Haven."

        $ loc_park_field = Location("Park grassy field", "loc_park_field", loc_type="grass", population=1, isolate_loc="loc_bushes")
        $ loc_park_field.district = dis_park
        $ add_to_list(dis_park._locs, "loc_park_field")
        $ dis_residential.add_sub_district_locs()
        $ dis_residential.add_locations()

    if game_version < "0.3.3.32":
        $ item_bottom_36 = Item("WORKOUT BLOOMERS", "Stretchy and form fitting shorts for working out in.", "item_bottom_36", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=130)
        $ item_top_44 = Item("SLEEVELESS MUFFLER TOP", "A sleeveless top with a neck muffler.", "item_top_44", type="top", outfit=["daily", "sport", "home"], belly=True, pokenips=True, value=80)

    if game_version < "0.3.3.33":
        $ player._prop = ""
        python:
            try:
                perk_wildcard_list
            except:
                perk_wildcard_list = []
        $ perk_party_girl = PerkClass("Party girl", "I am always up for some fun and it doesn't matter what kind.", "perk_party_girl", int_max=-20, int_multi=0.5, confidence_multi=1.5, wildcard=True)
        $ perk_meek = PerkClass("Meek", "I have absoloutly no confidence in myself and will do almost anything anyone asks of me.", "perk_meek", confidence_multi=0.2, wildcard=True)
        $ add_to_list(perk_origin_list, [perk_party_girl, perk_meek])
        python:
            for i in item_list:
                i.locked_always = False

    if game_version < "0.3.3.34":
        $ item_outfit_40 = Item("OPEN CHEST ROMPER SHORTS", "A one piece romper with short legs and an open square chest.", "item_outfit_40", type="outfit", outfit=["daily", "party", "home"], ass=True, clevage=True, value=200)
        $ item_outfit_41 = Item("SHOULDER ROMPER", "A one piece romper with open shoulders.", "item_outfit_41", type="outfit", outfit=["daily", "party", "home"], ass=True, clevage=True, value=200)

    if game_version < "0.3.3.35":
        $ clothesman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy who gave me clothes to cover myself up with", virginname="some random pervert who fucked me after I was caught naked", abort=True, is_unique=False)
    if game_version < "0.3.3.37":
        python:
            for i in perk_list:
                i.victim=False
                i.not_victim=False
            for i in [perk_broken, perk_wasted, perk_blackout, perk_lebo, perk_gagged, perk_gagged_locked, perk_blind, perk_pervert, perk_bitch, perk_cumstain, perk_despondent, perk_bambi, perk_meek]:
                i.victim=True
            perk_gamine.not_victim=True


        $ motelman = Npc(fname="Man", sname="", pregname="I am carrying the child of some guy from the motel", virginname="some random pervert from the motel", abort=True, is_unique=False)

    if game_version < "0.3.4.02":
        $ loc_bedroom_dani = Location("Dani's bedroom", "loc_bedroom_dani", outside=False, population=0, events=False, locked=True, loc_type="room")
        $ loc_bedroom_dani.district = dis_residential
        $ add_to_list(dis_home_area.locs, loc_bedroom_dani)
        $ add_to_list(dis_residential.locs, loc_bedroom_dani)

    if game_version < "0.3.4.03":
        python:
            for i in npc_all:
                i._love_cap = 100
                i._love_desc = ""
        $ dani._virginname="I lost my virginity to Dani and her giant pink strap-on."

    if game_version < "0.3.4.04":
        $ player._left_hand = ""
        $ player._right_hand = ""

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

        $ item_winebottle = Item("BOTTLE OF WINE", "An original bottle of wine. Unlike most booze, this is not home made.", "item_winebottle", use_notif="Opened a wine bottle", type="consumable", value=200)
        $ quests = [ ]
        call quest_daniwine_call from _call_quest_daniwine_call
        $ log.addquests(quests)

    if game_version < "0.3.4.07":
        $ item_coat_13 = Item("KNIT HOODIE", "A shoulder hoodie. Mostly for fashion and not warmth.", "item_coat_13", type="coat", value=500, exposed_nips=True)
        $ item_bottom_37 = Item("DRESS TROUSERS", "A pair of smart looking dress trousers.", "item_bottom_37", type="bottom", outfit=["daily", "party", "school"], ass=True, value=130)
        $ item_bottom_38 = Item("YOGA SHORTS", "Very form fitting but also stretchy pair of workout shorts", "item_bottom_38", type="bottom", outfit=["daily", "sport", "home"], ass=True, value=130)
        $ item_top_45 = Item("BAGGY SHIRT", "A simple, very loose, short sleeved dress shirt.", "item_top_45", type="top", outfit=["daily", "school", "party"], belly=True, pokenips=True, value=80)
        $ item_top_46 = Item("SHOULDERLESS T-SHIRT", "A typical t-shirt with the shoulders cut out for extra flexibility and ventilation.", "item_top_46", type="top", outfit=["daily", "sport", "home"], belly=True, pokenips=True, value=80)



    if game_version < "0.3.4.11":
        $ quests = [ ]
        call quest_dancevip_call from _call_quest_dancevip_call
        $ log.addquests(quests)

    if game_version < "0.3.4.12":
        $ loc_list = []
        $ loc_party_main = Location("Main room", "loc_party_main", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_kitchen = Location("Kitchen", "loc_party_kitchen", loc_type="tile", population=0, outside=False, events=False)
        $ loc_party_bedroom1 = Location("Main bedroom", "loc_party_bedroom1", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_bedroom2 = Location("Small bedroom", "loc_party_bedroom2", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_terrace = Location("Terrace", "loc_party_terrace", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_entrance = Location("Building entrance", "loc_party_entrance", loc_type="plaster", population=0, outside=False, events=False)
        $ dis_partyhouse = District("dis_partyhouse", "loc_party_main", 0, loc_list, npc_desc="At the private party house.")
        $ add_to_list(dis_revel.sub_districts, dis_partyhouse)
        $ loc_party_main.district = dis_revel
        $ loc_party_kitchen.district = dis_revel
        $ loc_party_bedroom1.district = dis_revel
        $ loc_party_bedroom2.district = dis_revel
        $ loc_party_terrace.district = dis_revel
        $ loc_party_entrance.district = dis_revel

    if game_version < "0.3.4.14":
        $ theo = Npc(fname="Theo", sname="Georgiou", colour="#d7d3ff", skinbase=(0.988, 0.850, 0.772), skinshad=(0.956, 0.705, 0.564), bio_image="theo", bio_group="party",
        bio_text="A guy who arranges private parties for folk who have a bit more money than most.")

    if game_version < "0.3.4.15":
        $ loc_list = []
        $ loc_party_stage = Location("Stage", "loc_party_stage", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_hall = Location("Hallway", "loc_party_hall", loc_type="plaster", population=0, outside=False, events=False)
        $ add_to_list(dis_revel.sub_districts, dis_partyhouse)
        $ loc_party_stage.district = dis_revel
        $ loc_party_hall.district = dis_revel
        $ add_to_list(dis_partyhouse._locs, ["loc_party_stage", "loc_party_hall"])

    if game_version < "0.3.4.16":
        $ class_updater(Location, "drinking_location", False)

        $ loc_party_hall.drinking_location = True
        $ loc_party_entrance.drinking_location = True
        $ loc_party_kitchen.drinking_location = True
        $ loc_party_main.drinking_location = True
        $ loc_party_stage.drinking_location = True
        $ loc_party_terrace.drinking_location = True

        $ loc_pub.drinking_location = True
        $ loc_school_field_back.drinking_location = True
        python:
            for i in npc_all:
                i._drunk = 0
                i._drunk_default = 15

        $ rachel._drunk_default = 30
        $ robin._drunk_default = 25

    if game_version < "0.3.4.19":

        $ partyman = Npc(fname="Man", sname="", pregname="I am carrying the child of one of the guys I had sex with at the dance party", virginname="one of the guys at the dance party", abort=True, is_unique=False)


        $ loc_party_bedroom3 = Location("Main bedroom", "loc_party_bedroom3", loc_type="room", population=0, outside=False, events=False)
        $ loc_party_bedroom4 = Location("Small bedroom", "loc_party_bedroom4", loc_type="room", population=0, outside=False, events=False)

        $ loc_party_bedroom3.district = dis_revel
        $ loc_party_bedroom4.district = dis_revel

        $ add_to_list(dis_partyhouse._locs, ["loc_party_bedroom3", "loc_party_bedroom4"])

    if game_version < "0.3.4.20":
        $ partyman2 = Npc(fname="Reveller", sname="", pregname="I am carrying the child of one of the guys I had sex with at the dance party", virginname="one of the guys at the dance party", abort=True, is_unique=False)

    if game_version < "0.3.4.21":
        $ goals = [ ]
        $ stages = [ ]

        $ quest_set_stage("quest_dancevip_03", "Talk to the girl at the Academy gymnasium.")
        $ quest_set_stage("quest_dancevip_04", "Serve drinks and dance at the Revel street party on Saturday evenings.")

        $ quest_update("Dance VIP show")

        python:
            for i in npc_all: 
                i.hate_message = ""
                i.hate = False
                i.sex_who_class = {}

    if game_version < "0.3.4.22":
        $ perk_addict = PerkClass("Addict", "I take to substances too well. I love everything and they love me.", "perk_addict", confidence_multi=0.8, allure_add=-100, mood_multineg=1.2, mood_multi=0.7, fitness_multi=0.8, int_multi=0.5, wildcard=True, victim=True)
        $ perk_princess = PerkClass("Princess", "I lived a pampered life, Confident in myself without much backing it up. Prone to mood swings.", "perk_princess", confidence_multi=3.0, confidence_multineg=3.0, allure_add=150, mood_multi=3.0, mood_multineg=3.0, fitness_multi=0.3, int_multi=0.3, wildcard=True)
        $ add_to_list(perk_origin_list, [perk_princess, perk_addict])

    if game_version < "0.3.4.23":
        $ quests = [ ]
        call quest_flyers_call from _call_quest_flyers_call
        $ log.addquests(quests)

    if game_version < "0.3.4.24":
        $ flyergirl = Npc(fname="Flyerer", sname="", colour="#b9c8d6", is_female=True, iswhore=True)
        if loc_market.visited:
            $ log.assign("Flyering")

    if game_version < "0.3.4.25":
        $ perk_deadinside = PerkClass("Dead inside", "Life is shit no matter how you look at it. I am barely coasting by.", "perk_deadinside", confidence_max=-70, confidence_min=10, mood_max=-70, mood_min=20, fitness_multi=0.8, int_multi=0.8, desire_add=-200, allure_add=-100, wildcard=True)
        $ add_to_list(perk_origin_list, [perk_deadinside])

    if game_version < "0.3.4.26":
        python:
            for i in npc_all:
                i.sex_les = 0
                i.nosex_les = 0

    if game_version < "0.3.4.27":
        $ mira_kidnapper= Npc(fname="Kidnapper", sname="", pregname="Text", virginname="text", abort=True, is_unique=False)
    if game_version < "0.3.4.28":
        $ item_bruisecream = Item("Ointment", "A cream to apply to wounds and injuries.", "item_bruisecream", use_notif="used ointment", type="consumable", value=50)
    if game_version < "0.3.4.29":
        $ loc_revel_backstreet_stairwell = Location("Appartment block", "loc_revel_backstreet_stairwell", events=False, outside=False, loc_type="plaster", locked=True)
        $ loc_revel_backstreet_stairwell.district = dis_revel
    if game_version < "0.3.4.30":
        $ item_strapon = Item("A strapon penis", "A strapon penis. It is fairly large, bright pink and knobbled.", "item_ballgag_locked", type="tool", value=300)

        python:
            for i in perk_list:
                i.desc_extra = ""
                i.diff = 1
    if game_version < "0.3.4.32":
        $ stall_junk_seller = Inventory("Market stall")
    if game_version < "0.3.4.33":
        python:
            for i in perk_list:
                if not i.desc_extra:
                    i.desc_extra = "Start a new game to get this description."
                if not i.diff:
                    i.diff = 3
    if game_version < "0.3.4.34":
        python:
            for i in item_clothes_list:
                i.bra_nolift = False
            for i in item_list:
                i.bra_nolift = False
        $ item_bra_14 = Item("HEART PASTIES", "Hearts taped over the nipples. These also prevent nipple poke through clothing.", "item_bra_14", type="bra", braless=True, perverted=True, bra_nolift=True, value=150)

    if game_version < "0.3.4.35":
        $ tiedman_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)
        $ tiedman2_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)
        $ tiedman3_dani = Npc(fname="Drunk guy", sname="from the pub", pregname="I am carrying the child of some guy Dani invited over while she had me tied up.", virginname="some guy Dani invited over while she had me tied in her bedroom", abort=True, is_unique=False)

    if game_version < "0.3.5.01":
        if school_dance_quest_show_count >= 12 and not quest_dancevip.active:
            $ school_dance_quest_show_count = 8
        if not havenvik.inv.does_stock(item_winebottle):
            $ havenvik.inv.add_to_stock(item_winebottle, 2)
        if item_winebottle.locked and log.interactive("quest_daniwine_02"):
            $ item_winebottle.locked = False
        $ item_winebottle.value = 75





    if game_version < "0.3.5.02":
        python:
            for i in diary_list:
                i.left_pic = None
                i.right_pic = None

    if game_version < "0.3.5.04":
        $ quests = [ ]
        call quest_nudevball_call from _call_quest_nudevball_call
        $ log.addquests(quests)
        if "nude_vball" in loc_beach_hangout.list:
            $ log.assign("Nude volleyball")
    if game_version < "0.3.5.07":
        $ scavver = Npc(fname="Scavver", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)
        $ scavver2 = Npc(fname="Scavanger", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)
        $ scavver3 = Npc(fname="Scavving guy", sname="", pregname="I am carrying the child of some scavver", virginname="some random scavver who fucked me", abort=True, is_unique=False)
    if game_version < "0.3.5.08":
        $ player._soldprice = 0
    if game_version < "0.3.5.10":
        $ robinpubmotel = Npc(fname="Patron", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)
        $ robinpubmotel2 = Npc(fname="Pub guy", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)
        $ robinpubmotel3 = Npc(fname="Boozer", sname="", pregname="I am carrying the child of some guy I went to the motel with after drinking with Robin and having an orgy", virginname="some guy in the motel while having group sex with Robin", abort=True, is_unique=False)
    if game_version < "0.3.5.12":
        $ class_updater(Location, "man_amount", 0)

    if game_version < "0.3.5.13":
        if loc_list_all == []:
            $ class_list_creator(Location, "loc_list_all")

    if game_version < "0.3.5.14":
        $ perk_slim = PerkClass("Great metabolism", "I always look like I am in shape, even when I am not.", "perk_slim")

    if game_version < "0.3.5.15":
        $ player._phair = 0
        $ player._hair_length = 0
        $ salongirl = Npc(fname="Beautician", sname="", colour="#ec98ef", is_female=True, isslut=True)

    if game_version < "0.3.5.16":
        python:
            for i in loc_list_all:
                i.home_location = False

        $ loc_bedroom.home_location = True
        $ loc_motel_room.home_location = True
        $ loc_office_pi_back.home_location = True
        $ loc_junk_trailer.home_location = True
        if "can_sleep" in loc_bedroom_dani.list or dani.dead:
            $ loc_bedroom_dani.home_location = True

    if game_version < "0.3.5.17":
        $ loc_list = []
        $ loc_highway_slum_home = Location("Slum home", "loc_highway_slum_home", can_sleep=True, outside=False, events=False, population=0, loc_type="room", home_location=True, locked=True)
        $ loc_highway_slum_home.district = dis_truckstop
        $ add_to_list(dis_slum._locs, ["loc_highway_slum_home"])

        $ neighbour = Npc(fname="Violet", sname="Blunt", colour="#ec98ef", is_female=True, iswhore=True)
        python:
            for i in npc_all:
                i.dead_time = 0

    if game_version < "0.3.5.19":
        $ quests = [ ]
        call quest_homeless_start_call from _call_quest_homeless_start_call
        call quest_homeless_call from _call_quest_homeless_call
        $ log.addquests(quests)

    if game_version < "0.3.5.21":
        $ loc_list = []
        $ loc_homeless_start_1 = Location("Bushes", "loc_homeless_start_1", loc_type="grass", population=0, events=False)
        $ loc_homeless_start_2 = Location("Bushes", "loc_homeless_start_2", loc_type="grass", population=0, events=False)
        $ loc_homeless_start_3 = Location("Bushes", "loc_homeless_start_3", loc_type="grass", population=0, events=False)
        $ loc_homeless_start_4 = Location("Bushes", "loc_homeless_start_4", loc_type="grass", population=0, events=False)
        $ loc_homeless_start_5 = Location("Bushes", "loc_homeless_start_5", loc_type="grass", population=0, events=False)

        $ loc_homeless_start_1.district = dis_misc
        $ loc_homeless_start_2.district = dis_misc
        $ loc_homeless_start_3.district = dis_misc
        $ loc_homeless_start_4.district = dis_misc
        $ loc_homeless_start_5.district = dis_misc

        $ add_to_list(dis_misc._locs, ["loc_homeless_start_1", "loc_homeless_start_2", "loc_homeless_start_3", "loc_homeless_start_4", "loc_homeless_start_5"])

        $ pre_bf = Npc(fname="Boyfriend", sname="", nname="", pregname="I am carrying the child of a guy I was dating before the world went to shit.", virginname="a guy I was dating when I was a teenager.", is_unique=True)

    if game_version < "0.3.5.22":
        $ goals = [ ]
        $ stages = [ ]
        $ quest_set_stage("quest_homeless_start_04", "I should visit my sister at the hospital on Revel street.")
        $ quest_update("Lost and alone")

    if game_version < "0.3.5.25":
        $ class_updater(Clothes, ["breast_coverage", "vag_coverage", "ass_coverage"], 0)
    if game_version < "0.3.5.28":
        $ player.set_preg_father_colour()
    if game_version < "0.3.5.31":
        $ item_bottom_39 = Item("MINI DAISY DUKES", "A pair of low rise jeans, cut off at the bottom to form a pair of hot pants.", "item_bottom_39", type="bottom", outfit=["daily", "sport", "home"], ass=True, slutty=True, value=80)

    if game_version < "0.3.5.36":
        python:
            for i in diary_list:
                try:
                    i.day
                except:
                    i.day = 0

    if game_version < "0.3.6.01.2":
        python:
            for i in npc_all:
                i._lust_multi = 1

    if game_version < "0.3.6.02.1":
        $ loc_office_ll.locked = False
    if game_version < "0.3.6.02.2":
        $ item_outfit_30.exposed_nips="pri"
    if game_version < "0.3.6.03.1":
        $ rent_convert_ledger()
        python:
            temp_var_1 = log.quest("Making a glory hole")
            if not temp_var_1.completed():
                temp_var_1.goal("quest_gloryhole_b_chis").required(False)
                temp_var_1.goal("quest_gloryhole_b_saw").required(False)
                if log.interactive("quest_gloryhole_b_chis") ^ log.interactive("quest_gloryhole_b_saw"):
                    temp_var_1.stage("stage3")
                if log.interactive("quest_gloryhole_c"):
                    temp_var_1.stage("stage4")
                elif temp_var_1.stage() and temp_var_1.stage().id() == "stage4": 
                    log.complete_quest(quest=temp_var_1)

    if game_version < config.version:



        $ game_version = config.version
        $ renpy.block_rollback()

    $ player.sex_hideaction()
    return


label test_add:
    $ perk_gagged = PerkClass("Gagged", "Mmmmff nnnngggfff aaahhh ffffmmmmm..", "perk_gagged", desire_min=150, desire_max=300)
    $ perk_slutty = PerkClass("Looking slutty", "I am dressed in a really revealing way. People no doubt think I am a slut.", "perk_slutty", desire_min=50, desire_max=150, confidence_add=5)
    $ perk_pervert = PerkClass("Perverted", "I look like a pervert.", "perk_pervert", desire_min=50, desire_max=150, confidence_add=-5)
    python:
        for i in item_clothes_list:
            i.sexual = False
            i.perverted = False
            i.gagged = False
    $ item_mask_1 = Item("BALLGAG", "A simple ballgag designed to silence people. Drooling optional.", "item_mask_1", type="mask", value=550, gagged=True, perverted=True)
    $ add_to_list(item_clothes_list, item_mask_1)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
