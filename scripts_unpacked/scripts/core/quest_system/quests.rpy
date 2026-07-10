init python:
    def quest_set_stage(id, desc, start=0, max=0, required=True, next=None):
        global goals, stages
        goals.append(Goal(id, desc, start=start, max=max, required=required))
        stages.append(Stage(id, next=next))

    def quest_set(name, desc, faction, quest, image=None):
        global Quest, goals, stages
        quests.append(Quest(name, desc, faction, quest, goals, stages, image=image))  

    def quest_update(qid):
        global goals, stages
        
        log._findquest(qid=qid).addgoals(goals)
        
        oldstages = []
        
        for stage in log._findquest(qid=qid)._stages.values():
            oldstages.append(stage)
        
        log._findquest(qid=qid)._stages = {}
        log._findquest(qid=qid).addstages(oldstages + stages)

define quest_list = []

label quests_call:
    $ quest_temp = None
    $ quests = [ ]

    call quests_institute_01_call from _call_quests_institute_01_call
    call quests_institute_02_call from _call_quests_institute_02_call
    call quests_institute_03_call from _call_quests_institute_03_call
    call quests_institute_04_call from _call_quests_institute_04_call
    call quests_institute_05_prep_call from _call_quests_institute_05_prep_call
    call quests_institute_05_call from _call_quests_institute_05_call
    call quests_institute_05_slave_call from _call_quests_institute_05_slave_call
    call mech_quest_ali_call from _call_mech_quest_ali_call
    call quest_gloryhole_create_call from _call_quest_gloryhole_create_call
    call quest_gloryhole_call from _call_quest_gloryhole_call
    call quest_scav_call from _call_quest_scav_call
    call quest_whore_call from _call_quest_whore_call
    call quest_paying_rent_call from _call_quest_paying_rent_call
    call quest_casino_call from _call_quest_casino_call

    call quest_photo_intro_call from _call_quest_photo_intro_call
    call quest_photo_call from _call_quest_photo_call
    call quest_photo_first_call from _call_quest_photo_first_call

    call quest_dance_call from _call_quest_dance_call
    call quest_cleaner_call from _call_quest_cleaner_call
    call quest_mira_missing_call from _call_quest_mira_missing_call
    call quest_exhib_call from _call_quest_exhib_call
    call quest_robinslut_call from _call_quest_robinslut_call
    call quest_wolfgang_call from _call_quest_wolfgang_call_1
    call quest_daniwine_call from _call_quest_daniwine_call_1
    call quest_dancevip_call from _call_quest_dancevip_call_1
    call quest_flyers_call from _call_quest_flyers_call_1
    call quest_nudevball_call from _call_quest_nudevball_call_1

    call quest_homeless_start_call from _call_quest_homeless_start_call_1
    call quest_homeless_call from _call_quest_homeless_call_1

    $ school_soccer_quest = QuestClass()
    $ school_dance_quest = QuestClass()
    $ school_bully_quest = QuestClass()
    $ school_newfriend_quest = QuestClass()
    $ school_photo_quest = QuestClass()



    $ pub_waitress = QuestClass()
    $ pub_waitress.quest_job(10,(17,18,19,20,21,22,23,0,1,2),("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
    $ goals = [ ]
    $ stages = [ ]
    $ quest_set_stage("pub_01", "Go to the pub in the evening to start a shift.")
    $ quest_set("Pub barmaid",
        "The pub on revel street is always in need for barmaids. I can work there every evening for tips.",
        "Jobs",
        pub_waitress,
        image="barmaid")


    $ market_flyer = QuestClass()
    $ market_flyer.quest_job(10,(9,10,11,12,13,14,15,16,17,18),("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"))
    $ goals = [ ]
    $ stages = [ ]
    $ quest_set_stage("flyer_01", "Go to the market whenever it is open to start a shift")
    $ quest_set("Flyer distributor",
        "The market has some work available handing out fliers. I can work there whenever the market is open.",
        "Jobs",
        market_flyer)


    $ log = Questlog(quests, "qlog", "qkey")
    return

label quests_institute_01_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_01 = QuestClass()

    $ quest_set_stage("mq_01_a", "I should meet [tucker.name] at the medical institute near Revel street and see what he has to say.")
    $ quest_set_stage("mq_01_b", "Go to the pub on Revel street and meet with [simon.fullname] to try and find out why he is investigating people who work for The Institute.")
    $ quest_set_stage("mq_01_c", "Return to [tucker.name] and tell him how it went.")

    $ quest_set("Introduction to The Institute",
        "I have been offered the chance to work with The Institute. Since I know very little about the organisation who saved me, I have decided to go and see what they are all about.",
        "Institute",
        main_quest_01,
        image="sherlock")
    return

label quests_institute_02_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_02 = QuestClass()



    $ quest_set_stage("mq_02_a", "Wait a few days for [simon.fullname] to expose himself.")
    $ quest_set_stage("mq_02_a_done", "Return to [tucker.name] and find out if [simon.fullname] has surfaced.")
    $ quest_set_stage("mq_02_b", "Undergo the experimental cosmetic surgery.")
    $ quest_set_stage("mq_02_c", "Go to the pub in the evening and leave a chalk mark on the door to arrange a meet with [simon.name].")
    $ quest_set_stage("mq_02_d", "Return to [tucker.name] with the package.")

    $ quest_set("Tracking down Simon Banks",
        "I was unable to get any information from [simon.fullname] but [tucker.name] assures me that my presence alone would have been enough to spook him into making moves that reveal his intentions.",
        "Institute",
        main_quest_02,
        image="cosmetic")


    $ goals = [ ]
    $ stages = [ ]

    $ quest_set_stage("mq_02_passed_a", "Wait a day then return to The Institute and meet with [nik.name] and [psy.name]")
    $ quest_set_stage("mq_02_passed_b", "Return to The Institute and meet with [nik.name] and [psy.name]")

    $ quest_set("Cosmetic what...?",
        "[tucker.name] was saying something about my body being unique and able to adapt to cosmetic changes. I need to find out what he means.",
        "Institute",
        main_quest_02,
        image="cosmetic")
    return

label quests_institute_03_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_03 = QuestClass()

    $ quest_set_stage("mq_03_a", "Visit [tucker.name] in his office.")
    $ quest_set_stage("mq_03_b", "Go home and think over what [tucker.name] told you.")
    $ quest_set_stage("mq_03_c", "If I am willing to work for The Institute, I should go and speak to [tucker.name].")

    $ quest_set("Becoming the Fixer",
        "After the completion of my first assignment with the Institute, it has given me a clearer idea of what might be expected of me. On leaving The Institute, [tucker.name] approached me and told me he has something important to discuss with me. When I have the time for a lengthy talk with him, I should pay him a visit at his office.",
        "Institute",
        main_quest_03,
        image="femme")
    return

label quests_institute_04_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_04 = QuestClass()

    $ quest_set_stage("mq_04_a", "Go to the security checkpoint and introduce myself to [miller.name] and find out about [ant.name].")
    $ quest_set_stage("mq_04_b", "Wait a day for [miller.name] to prepare the paperwork on [ant.name].")
    $ quest_set_stage("mq_04_c", "[miller.name] should have the papers ready now so I should pay him a visit.")
    $ quest_set_stage("mq_04_d", "Return to [tucker.name] and tell him what I managed to find out about [ant.name].")
    $ quest_set_stage("mq_04_e", "Wait a few days for [tucker.name]'s goons to recon Haven.")
    $ quest_set_stage("mq_04_f", "Return to [tucker.name] and find out what your next step is.")

    $ quest_set("Tracking a Curse",
        "[tucker.name] has asked me to go and find out what [miller.name] might know on [ant.name] in preparation for tracking him down.",
        "Institute",
        main_quest_04,
        image="femme")
    return

label quests_institute_05_prep_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_05_prep = QuestClass()

    $ quest_set_stage("mq_05_prep_a", "Go to the mechanics and pick up a package of tools.", required=False)
    $ quest_set_stage("mq_05_prep_b", "Go to the market and pick up my mission outfit.", required=False)
    $ quest_set_stage("mq_05_prep_c", "Go to the junk yard and pick up a package with my tracker.", required=False)
    $ quest_set_stage("mq_05_prep_d", "Take the packages back to [tucker.name].")

    $ quest_set("Preparing for a Curse",
        "[tucker.name] has asked me to pick up a few bits for my mission. Mostly so I can meet with the people that The Institute works with.",
        "Institute",
        main_quest_05_prep,
        image="femme")
    return

label quests_institute_05_call:
    $ goals = [ ]
    $ stages = [ ]

    $ main_quest_05 = QuestClass()

    $ quest_set_stage("mq_05_a", "When I am ready for a lengthy mission, I should go and see [tucker.name] at the hospital.")
    $ quest_set_stage("mq_05_b", "Explore Haven and see if I can find [ant.name].")


    $ goals.append(Goal("mq_05_upstairs", "Find a way upstairs to speak to [alex.nname].", required=False))
    $ goals.append(Goal("mq_05_info", "Snoop around and try to gain any info on where [ant.name] might be.", start=0, max=10, required=False))
    $ goals.append(Goal("mq_05_fire", "I found a lighter and an accelerant. I could set a fire somewhere as a distraction. Better not get caught though.", required=False))
    $ goals.append(Goal("mq_05_pipes", "I'm sure there is some way I can make a distraction in the pipes room.", required=False))
    $ goals.append(Goal("mq_05_pipesbreak", "I can break the pipes in the utility room to cause a huge distraction.", required=False))
    $ goals.append(Goal("mq_05_guard", "Find some way to get past the guard blocking the gate upstairs.", required=False))
    $ goals.append(Goal("mq_05_sprinklers", "Find a way to set off the sprinkler system.", start=0, max=4,  required=False))

    $ stages.append(Stage("mq_05_upstairs,mq_05_info,mq_05_fire,mq_05_pipes,mq_05_pipesbreak,mq_05_guard,mq_05_sprinklers", next="mq_05_c"))

    $ quest_set_stage("mq_05_c", "Leave Haven and report to [tucker.name].", next=False)







    $ quest_set("Haven",
        "[tucker.name] wants me to go under cover in a local homeless community called Haven. It will almost certainly be dangerous so I should should only go on this mission when I am fully prepared for the consequences.",
        "Institute",
        main_quest_05,
        image="haven")
    return

label quests_institute_05_slave_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_set_stage("mq_05_slave_a", "Survive.")

    $ quest_set("Slave",
        "I have been captured and imprisoned! Fuck! I need to wait for [tucker.name] or [emile.name] to get me the hell out of here.",
        "Institute",
        main_quest_05,
        image="haven")
    return

label mech_quest_ali_call:
    $ goals = [ ]
    $ stages = [ ]

    $ mech_quest_ali = QuestClass()

    $ quest_set_stage("mech_quest_ali_a", "Figure out a way to help [ali.name].")
    $ quest_set_stage("mech_quest_ali_b", "Help [dez.name] get [ali.name] to hold up her end of the deal.")
    $ quest_set_stage("mech_quest_ali_c", "Ignore the situation and see how it plays out.")

    $ quest_set("Alison's deal",
        "The girl who works in the mechanics shop made a deal she is unwilling to stick to. Should I stick my nose in or just see how it plays out?",
        "Mechanic",
        mech_quest_ali,
        image="femme")
    return

label quest_gloryhole_create_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_gloryhole_create = QuestClass()

    $ quest_set_stage("quest_gloryhole_a", "Find out what I need to make a hole in the wall.")
    $ quest_set_stage("quest_gloryhole_b_chis", "Get [nate.name] a chisel.", required=False)
    $ quest_set_stage("quest_gloryhole_b_saw", "Get [nate.name] a saw.", required=False)
    $ quest_set_stage("quest_gloryhole_b_tape", "Get [nate.name] some tape.")
    $ quest_set_stage("quest_gloryhole_c", "Make the gloryhole with [nate.name].")

    $ quest_set("Making a glory hole",
        "[nate.name] asked for help in trying to set up a glory hole in the toilets. But we need some tools to do so.",
        "Misc",
        quest_gloryhole_create,
        image="gloryhole")
    return

label quest_gloryhole_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_gloryhole = QuestClass()

    $ quest_set_stage("quest_gloryhole", "Create or use glory holes.")


    $ quest_set("Glory holes",
        "I have the tools to create more glory holes. I can use them myself or leave them for others to use.",
        "Jobs",
        quest_gloryhole,
        image="gloryhole")
    return

label quest_scav_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_scav = QuestClass()

    $ quest_set_stage("quest_scav", "Scavenge for and sell anything of value.")


    $ quest_set("Scavenger",
        "There is plenty of useful material and items just laying around. I can scavenge for it and sell it off for a nice profit.",
        "Jobs",
        quest_scav,
        image="scav")
    return

label quest_paying_rent_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_rent = QuestClass()

    $ quest_set_stage("quest_rent_a", "Rent needs to be paid every Sunday.")
    $ quest_set_stage("quest_rent_b", "I can clean up around the house to reduce rent payments.")
    $ quest_set_stage("quest_rent_c", "I can work in the casino to pay off my rent.")


    $ quest_set("Paying rent",
        "I am expected to pay rent if I want to keep living in the house.",
        "Misc",
        quest_rent,
        image="rent")
    return

label quest_casino_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_casino = QuestClass()

    $ quest_set_stage("casino_01", "Go to the casino at night to start a shift.")

    $ quest_set("Casino girl",
        "The casino needs girls to work and entertain gamblers.",
        "Jobs",
        quest_casino,
        image="casino")
    return

label quest_photo_intro_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_photo_intro = QuestClass()

    $ quest_set_stage("photo_intro_01", "Meet Felix in the darkroom once the academy is empty.")
    $ quest_set_stage("photo_intro_02", "If I am willing, I should go to the darkroom for a photo shoot.")
    $ quest_set_stage("photo_intro_03", "Wait a few days for Felix to develop the volleyball photos.")
    $ quest_set_stage("photo_intro_04", "See if there is any more photo work available.")
    $ quest_set_stage("photo_intro_05", "Wait a few days for Felix to develop the dance photos.")
    $ quest_set_stage("photo_intro_06", "See if there is any more photo work available.")
    $ quest_set_stage("photo_intro_07", "Felix is looking into where the fliers are going. I should wait a few days.")
    $ quest_set_stage("photo_intro_08", "See if Felix found out what happened to the fliers.")

    $ quest_set("Promotional material",
        "The academy is trying to attract people and I can help out.",
        "Jobs",
        quest_photo_intro,
        image="photo_promo")
    return

label quest_photo_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_photo = QuestClass()

    $ quest_set_stage("photo_01", "Felix might have more work available. I should go an see him.")
    $ quest_set_stage("photo_02", "If I am willing, I can model for some photos.", required=False)
    $ quest_set_stage("photo_03", "I can take photos and sell them off to Felix.", required=False)

    $ quest_set("Photo model",
        "I can get paid for posing for some photos.",
        "Jobs",
        quest_photo,
        image="photo")
    return

label quest_photo_first_call:
    $ goals = [ ]
    $ stages = [ ]



    $ quest_set_stage("photo_first_01", "Get some magazines and give them to Felix.", start=0, max=4)
    $ quest_set_stage("photo_first_02", "Do another photo shoot with Felix.")
    $ quest_set_stage("photo_first_03", "Wait a few days for Felix to make the magazine.")
    $ quest_set_stage("photo_first_04", "See if Felix has the magazine ready.")

    $ quest_set("Starting the magazine",
        "We need to get some ideas for the magazine and how to add in pictures that people will \"like\".",
        "Misc",
        quest_photo,
        image="photo")
    return

label quest_dance_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_dance = QuestClass()

    $ quest_set_stage("dance_01", "The girls do events on Monday to Wednesday.")

    $ quest_set("The Sweet Girls",
        "I was invited to be part of The Sweet girls.",
        "Jobs",
        quest_dance,
        image="dance")
    return

label quest_cleaner_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_cleaner = QuestClass()

    $ quest_set_stage("cleaner_01", "Find people who need cleaners and... Clean?")

    $ quest_set("Cleaner",
        "Lot's of people need a cleaner and it sounds like something I can do.",
        "Jobs",
        quest_cleaner,
        image="maid")
    return

label quest_mira_missing_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_mira_missing = QuestClass()

    $ quest_set_stage("mira_missing_01", "Ask around and see if anyone has seen Mira recently.")
    $ quest_set_stage("mira_missing_02", "I should tell Cass what I discovered.")
    $ quest_set_stage("mira_missing_03", "Wait for Cass to process what I told her.")
    $ quest_set_stage("mira_missing_04", "Meet Cass and ask around the highway if anyone has seen Mira")
    $ quest_set_stage("mira_missing_05", "Try to find out anything about Mira from people I know.")
    $ quest_set_stage("mira_missing_06", "Speak to Cass and tell her whores will only speak to whores.")
    $ quest_set_stage("mira_missing_07", "Meet Cass at night in Revel backstreets.")
    $ quest_set_stage("mira_missing_08", "Try and get info about Mira from people while pretending to be a whore.", start=0, max=10)
    $ quest_set_stage("mira_missing_09", "I found out what might have happened to Mira. But what can I do about it?")
    $ quest_set_stage("mira_missing_10", "Tell Cass that Mira is safe.")

    $ quest_set("Find Mira",
        "Mira seems to have vanished. I wonder what could have happened?",
        "Misc",
        quest_mira_missing,
        image="mira_missing")
    return

label quest_whore_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_whore = QuestClass()

    $ quest_set_stage("quest_whore_01", "Hang around busy areas and attract clients.", required=False)
    $ quest_set_stage("quest_whore_02", "Rent a pink room in the motel and wait for customers.", required=False)

    $ quest_set("Street walking",
        "The Institute gave me a body people are willing to pay money to spend time with. If I am willing I can agree to accept money for sex.",
        "Jobs",
        quest_whore,
        image="whore")
    return

label quest_exhib_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_exhib = QuestClass()

    $ quest_set_stage("quest_exhib_01", "Meet Rachel at night by the academy and show her the secret entrance.")
    $ quest_set_stage("quest_exhib_02", "Rachel is hanging out in the gym at night. I wonder what she is doing?")
    $ quest_set_stage("quest_exhib_03", "Turns out she has been getting naked and prancing around. I should speak to her and see why she is doing it.")
    $ quest_set_stage("quest_exhib_04", "She wants us to do weird things and push boundaries while being naked. I should speak to her in the gym at night if I am interested in playing.")

    $ quest_set("A place to be alone",
        "Rachel has asked me to show her how to get inside the academy at night so she can spend some time alone there. It sounds suspicious...",
        "Misc",
        quest_exhib,
        image="exhib")
    return

label quest_robinslut_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_robinslut = QuestClass()

    $ quest_set_stage("quest_robinslut_01", "Find somewhere to buy slutty clothes for Robin.")
    $ quest_set_stage("quest_robinslut_02", "Meet Robin at home and give her the outfits and makeup I bought.")

    $ quest_set("Making a slut",
        "Robin has told me she want's to be ogled as a sexpot and asked for my help in making her look like one.",
        "Misc",
        quest_robinslut,
        image="robinslut")
    return

label quest_daniwine_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_daniwine = QuestClass()

    $ quest_set_stage("quest_daniwine_01", "Find somewhere I can buy some wine.")
    $ quest_set_stage("quest_daniwine_02", "Gift some wine to Dani in the evening.")

    $ quest_set("Evening wine",
        "Dani want's to hang out at her place with a bottle of decent wine.",
        "Misc",
        quest_daniwine,
        image="wine")
    return

label quest_wolfgang_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_wolfgang = QuestClass()

    $ quest_set_stage("quest_wolfgang_01", "I can go to the park wearing specific clothes and have a lot of fun.")
    $ quest_set_stage("quest_wolfgang_02", "Maybe I can get someone else to run the gauntlet.")

    $ quest_set("Wolfgang bitch",
        "I found out some perverts in the park play a game where if you go into the park at night wearing specific clothes, they will treat you like a sex bitch. It seems it's all in good fun though and nothing will happen if I don't wear the clothes.",
        "Misc",
        quest_wolfgang,
        image="wolfgang")
    return

label quest_exhib_update_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_set_stage("quest_exhib_04", "She wants me to do weird things and push boundaries while being naked. I should speak to her in the gym at night if I am interested in playing.")

    return

label quest_dancevip_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_dancevip = QuestClass()

    $ quest_set_stage("quest_dancevip_01", "Meet the girls in Revel street in the evening.")
    $ quest_set_stage("quest_dancevip_02", "Give the VIP's a show they will never forget.")
    $ quest_set_stage("quest_dancevip_03", "Talk to the girl at the Academy gymnasium.")
    $ quest_set_stage("quest_dancevip_04", "Serve drinks and dance at the Revel street party on Saturday evenings.")


    $ quest_set("Dance VIP show",
        "Someone who spotted us dancing in the park wants us to entertain at a private party. Dancing, serving drinks and whatever else to make the guests happy.",
        "Jobs",
        quest_dancevip,
        image="dancevip")
    return

label quest_flyers_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_flyers = QuestClass()

    $ quest_set_stage("quest_flyers_01", "I should find places who wants flyers handed out.")

    $ quest_set("Flyering",
        "Stalls and shops want people to hand out flyers to attract customers. This sounds like something I can do to earn a bit of extra cash.",
        "Jobs",
        quest_flyers,
        image="flyers")
    return

label quest_nudevball_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_nudevball = QuestClass()

    $ quest_set_stage("quest_nudevball_01", "Go to the beach at night and meet people to play with.")

    $ quest_set("Nude volleyball",
        "Turns out a few of the girls gather on the beach and play volleyball. While naked. I can join them if I want to.",
        "Misc",
        quest_nudevball,
        image="nudevball")
    return

label quest_homeless_start_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_homeless_start = QuestClass()

    $ quest_set_stage("quest_homeless_start_01", "Look around and see if I can find my sister.")
    $ quest_set_stage("quest_homeless_start_02", "Find somewhere to sleep.")
    $ quest_set_stage("quest_homeless_start_03", "Investigate the city and see if I can find my sister.")
    $ quest_set_stage("quest_homeless_start_04", "I should visit my sister at the hospital on Revel street.")

    $ quest_set("Lost and alone",
        "My sister and I finally made it near the city, where we heard it was safe. Well, maybe it was safer but certainly not safe because we were run off the road by some lunatics and ended up crashing. Good job I wore a seatbelt. We were forced to run but ended up separated and when I finally managed to get my bearings, I had made it through a checkpoint while the guards were entirely focused on the lunatics.",
        "Misc",
        quest_homeless_start,
        image="homeless")
    return

label quest_homeless_call:
    $ goals = [ ]
    $ stages = [ ]

    $ quest_homeless = QuestClass()

    $ quest_set_stage("quest_homeless_01", "Find somewhere to stay. The slums might be a good place to start.")

    $ quest_set("Homeless",
        "I wasn't able to keep up with rent. Obviously the landlord was not too happy about this so kicked me out. I can probably find some temporary places to stay, but I need something more permanent so I need to look around and find somewhere new. Preferably cheaper than where I was before.",
        "Misc",
        quest_homeless,
        image="homeless")
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
