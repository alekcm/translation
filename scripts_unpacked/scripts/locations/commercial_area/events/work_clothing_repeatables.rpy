

label work_clothing:
    $ work_clothing_events_counter = 0
    "You arrive to work and do a job. events will trigger from here"
    call time_round_to_hour_random from _call_time_round_to_hour_random



    jump work_clothing_weights

label work_clothing_end:

    $ randomnum = renpy.random.randint(1, 10)
    if randomnum >= 8:
        jump work_clothing_fasion_quest_hub







    $ work_clothing_workdays += 1
    $ player.cash += work_clothing_salary
    "You are done with work and start preparing to go home"
    if t.hour < 21:
        call time_round_to_hour_random from _call_time_round_to_hour_random_1

    "Tally your money depending on events and pay you"
    "I will also say something depending on the work counter and it will effect my stats"
    jump commercial_area_mall_screen







label work_clothing_weights:
    if t.hour == 20 and t.minute > 30 or t.hour > 20:
        jump work_clothing_end
    else:

        if work_clothing_events_counter > 0:
            "You get back to work"
        $ rand_choice = WeightedChoice([
        ("work_clothing_events_time", 300),
        ("work_clothing_events_vcommon", 100),
        ("work_clothing_events_common", 20),
        ("work_clothing_events_rare", 5),
        ("work_clothing_events_vrare", 1)
        ])
        jump expression rand_choice
label work_clothing_events_vcommon:
    jump expression renpy.random.choice([
    "work_clothing_events_vcommon_01",
    "work_clothing_events_vcommon_02",
    "work_clothing_events_vcommon_03",
    "work_clothing_events_vcommon_04",
    "work_clothing_events_vcommon_05",
    "work_clothing_events_vcommon_06",
    "work_clothing_events_vcommon_07"
    ])













jump expression renpy.random.choice([
"park_walk_events_vcommon_1",
"park_walk_events_vcommon_2",
"park_walk_events_vcommon_3"
])
label work_clothing_events_common:

    $ rand_choice = WeightedChoice([
    ("work_clothing_events_common_01", 5),
    ("work_clothing_events_common_02", 5),
    ("work_clothing_events_common_03", 5),
    ("work_clothing_events_common_04", 5),
    ("work_clothing_events_common_05", 5),
    ("work_clothing_events_common_06", 5),
    ("work_clothing_events_common_07", 5),
    ("work_clothing_events_common_08", 5),
    ("work_clothing_events_common_09", 5)
    ])
    jump expression rand_choice

label work_clothing_events_rare:
    if work_clothing_naughty_counter < 3:
        jump work_clothing_events_common
    else:

        $ rand_choice = WeightedChoice([
        ("work_clothing_events_rare_01", 5),
        ("work_clothing_events_rare_02", 5),
        ("work_clothing_events_rare_03", 5),
        ("work_clothing_events_rare_04", 5),
        ("work_clothing_events_rare_05", 5),
        ("work_clothing_events_rare_06", 5),
        ("work_clothing_events_rare_07", 5),
        ])
        jump expression rand_choice

label work_clothing_events_vrare:
    if work_clothing_naughty_counter < 3:
        jump work_clothing_events_common
    elif work_clothing_naughty_counter <= 10:
        jump work_clothing_events_rare
    else:

        $ rand_choice = WeightedChoice([
        ("work_clothing_events_vrare_01", 5),
        ("work_clothing_events_vrare_02", 5)

        ])
        jump expression rand_choice




label work_clothing_events_time:
    "Test to show the time passing event is working"
    $ t.minute = 31
    jump work_clothing_weights





label work_clothing_events_vcommon_01:
    "As you are passing through the aisles you notice one of the racks have all the clothes pulled out and laying on the floor."
    $ face = 1
    pc "*Sigh* Why do people do this instead of asking for help."
    "You spend some time cleaning up the mess."
    pc "There we go, all done."
    $ player.add_mood -= 5
    $ work_clothing_events_counter += 1
    $ face = 0
    $ t.minute = 22

    jump work_clothing_weights


label work_clothing_events_vcommon_02:
    "As you are working the cashiers desk, a customer approaches you asking for help."
    $ face = 2
    $ randomnum = renpy.random.randint(1, 30)
    if randomnum == 1:
        pc "For the last time ma'am, this is a toaster and you are in a clothing store. You didn't buy it from here!"
    elif randomnum == 2:
        pc "Sir, shouting at me doesn't help the situation any."
    elif randomnum == 3:
        pc "This coupon is for the burger restaurant, just becase we are in the same mall it doesn't mean you can use it to get a discount here."
    elif randomnum == 4:
        pc "No sir, we do not rent tuxedos, we are a teen clothing shop. Teens tend not to want a tuxedo."
    elif randomnum == 5:
        pc "Ma'am, you bought this 4 years ago, you cannot get a refund because they have worn out..."
    elif randomnum == 6:
        pc "No ma'am, we do not sell a four legged version for your dog..."
    elif randomnum == 7:
        pc "No I will not give you all these items for free in return for a shoutout on your social media."
    elif randomnum == 8:
        pc "No, we do not give discounts for being married to someone in the military. Ask your husband to come and buy it instead."
    elif randomnum == 9:
        pc "It won't fit because you need to put your head in the big hole, not the small ones..."
    elif randomnum == 10:
        pc "If you dont want it to be so revealing, then buy a longer skirt. I will not give a discount because it shows off too much of your leg..."
    elif randomnum == 11:
        pc "Look, if you read the label tey are called *ripped designer jeans*. They are made this way and I will not discount them for being damaged!"
    elif randomnum == 12:
        pc "These are a size 6 ma'am, and you are clearly not. So of course they ripped when you tried to put them on!"
    elif randomnum == 13:
        pc "Sir, it's a dress... We do not carry a male version of dresses. I'm not even sure what a make version of a dress is..."
    elif randomnum == 14:
        pc "Ugh, one moment and I'll get the manager..."
    elif randomnum == 15:
        pc "I'm sorry ma'am but I can't help you. We have a strict *No trying on underpants* policy..."
    elif randomnum == 16:
        pc "Ma'am, you are drunk and I am going to have to ask you to stop harassing other customers and leave the store."
    elif randomnum == 17:
        pc "No we will not be taking part in the anti vax march you have planned next weekend. Now please move aside so I can deal with other customers."
    elif randomnum == 18:
        pc "I'm sorry miss, but once you remove the labels then we no longer accept returns. it's clearly stated on the recipt in your hand."
    elif randomnum == 19:
        pc "You should think yourself lucky I am not calling the police on you for that. Now please leave the store right now!"
    elif randomnum == 20:
        pc "Yes, thats right. The *pretty in pink* collection comes in pink only and no we cannot make you a blue version."
    elif randomnum == 21:
        pc "Yes ma'am, all the mirrors are the same. They are not curved to try and make you look fat."
    elif randomnum == 22:
        pc "If you didn't wear this dress out already, then why is ther wine stains on it?"
    elif randomnum == 23:
        pc "Ma'am, you bought this as a clearance item, we will not be refunding the full price for it."
    elif randomnum == 24:
        pc "...because I saw you swap the labels out. This very expensive dress is quite clealy not a belt as the label says..."
    elif randomnum == 25:
        pc "No we do not eccept returns from other clothing shops."
    elif randomnum == 26:
        pc "Ma'am, I clearly told you that your daughter couldn't wear this to school but you refused to listen..."
    elif randomnum == 27:
        pc "Thats what sheer means. Very thin and almost see through, so of course people could see your nipples through it without a bra..."
    elif randomnum == 28:
        pc "No sir, we do not have viewing rooms behind the mirrors to the changing rooms. Now please leave before I call security."
    elif randomnum == 29:
        pc "No we do not accept nudes as a form of payment."
    else:
        pc "Sir, please keep a social distance of at least 2 meters."

    "After having to deal with that customer, you are ready to pull your hair out!"
    $ face = 0
    $ work_clothing_events_counter += 1
    $ t.minute = 42
    jump work_clothing_weights

label work_clothing_events_vcommon_03:
    "As you are cleaning the store you notice a child running around causing chaos and messing up the selves."
    pc "Ma'am, can you please keep your child from messing up the store..."
    "She pretneds to not hear you."
    pc "Ma'am?"
    $ face = 3
    pc "..."
    pc "Bitch!"
    $ work_clothing_events_counter += 1
    $ face = 0
    $ t.minute = 24
    jump work_clothing_weights

label work_clothing_events_vcommon_04:
    "As you go into the toilets to freshen up you notice a weird smell."
    pc "What is that smell..."
    pc "..."
    $ face = 3
    pc "Ahhhh disgusting. How the hell can that come out of someone..."
    pc "I guess I am the idiot that need to clean this up..."
    $ face = 0
    $ work_clothing_events_counter += 1
    $ t.minute = 26
    jump work_clothing_weights

label work_clothing_events_vcommon_05:
    "The store has been extremly busy for a while now, but looks like it has started to calm down."
    pc "Ah finally a moment to breathe..."
    $ face = 4
    pc "Damn, what the hell happened to this place, looks like a bomb went off in the store."
    "Suzie comments how you both need to clean it up before [marco] sees the place"
    pc "Uff, alright. How the hell can a few customers make such a mess of the place?"
    $ face = 0
    $ work_clothing_events_counter += 1
    $ t.minute = 40
    jump work_clothing_weights

label work_clothing_events_vcommon_06:
    pc "Looks like the shop is empty so I think I can manage a little sit down in the staff room"
    $ work_clothing_events_counter += 1
    $ t.minute = 20
    jump work_clothing_weights

label work_clothing_events_vcommon_07:
    "A very common event where you helped a nice customer so now you feel good"
    $ work_clothing_events_counter += 1
    $ t.minute = 26
    jump work_clothing_weights




label work_clothing_events_common_01:
    "A common event where you are helping the gf of a couple pick out clothing. the bf wants a more sexy look and the girl more conservative. YOur stats determine the advice you can give"
    $ work_clothing_events_counter += 1
    $ t.minute = 45
    jump work_clothing_weights

label work_clothing_events_common_02:
    "A common event where father comes in to buy stuff for his daugther. you can give advice depending on your stat. if your corruption is too high you can suggest inapropriate things."
    $ work_clothing_events_counter += 1
    $ t.minute = 46
    jump work_clothing_weights

label work_clothing_events_common_03:
    "A common event where an old lady comes in to browse. depending on your clothing you are called a slut"
    if pregnant >= 3:
        "She comments it's no wonder you are pregnant and should look forward to being a single mum."
    $ work_clothing_events_counter += 1
    $ t.minute = 26
    jump work_clothing_weights

label work_clothing_events_common_04:
    "A common event where a girl your age comes in to shop. you give advice based on your own clothing and stats"
    $ t.minute = 27
    $ work_clothing_events_counter += 1

label work_clothing_events_common_05:
    "A common event where a fat lady is complaining that the shop doesnt stock her size. she is mad that its discrimination. you call security and have her kicked out"
    fat "Hello, I can't find anything in my size. Go in the back and get me one of these dresses that fits."
    pc "I'm sorry ma'am, size 16 is the largest size the store stocks."
    fat "WHAT!! How can that be. Thats discrimination!"
    pc "I'm sorry, but these sizes aren't big sellers so the stores dont stock them to save space. But if you want I can place a delivery order fo..."
    fat "This is outrageous! Are only skinny people allowed to shop here or something?"
    pc "Ma'am, this is a store aimed at teenagers. There are not many teens that need sizes larger than 16..."
    fat "Screw you! I am going to call your corporate office and have you fired for discrimination."
    pc "Ok... As you wish. Not like I decide what we stock."
    fat "I'll be taking your job from you!!"
    $ work_clothing_events_counter += 1
    $ t.minute = 44
    jump work_clothing_weights

label work_clothing_events_common_06:
    "A common event where an ugly woman is shouting and complaining that this is the problem with todays youth. all are sluts"
    ugly "Miss, hey miss? Where are the clothes that actually cover some skin?"
    pc "Excuse me? What do you mean?"
    ugly "You see, thats the problem!"
    pc "Huh?"
    ugly "Girls your age showing off their bodies like street hookers. Thats the problem with society these days."
    if player.pregnancy >= 2:
        ugly "Not a shock to see a girl your age already with a baby in her belly"
        ugly "Hope you enjoy being a single mum!"
    else:
        ugly "It's only a matter of time before you become a single mother the way you go round flaunting your bodies!"
    ugly "This is a terrible store and I won't be buying any hooker clothes from here. I'll take my money and shop elsewhere!"
    pc "Ok..."
    pc "What did I do to deserve that?"
    $ player.tired -= 2
    $ work_clothing_events_counter += 1
    $ t.minute = 22
    jump work_clothing_weights

label work_clothing_events_common_07:
    "A common event where the power in the shop goes out. you are not allowed to serve any customers during this time and just relax until the power is back on"
    scene bg_black
    $ face = 4
    pc "Huh? What happened to the lights?"
    suzie "looks like the power went out again."
    $ randomnum = renpy.random.randint(1, 3)
    if randomnum == 1:
        $ face = 0
        "hard day"
        pc "Damn, and we have so many customers in the store as well."
        suzie "Mall security won't allow us to serve customers while the power is out so looks like we need to go round and get everyone to leave."
        pc "*Sigh*"
        pcs "Can I have your attention please! Due to a power failure I am asking eveyone to leave right now please!"
        clo_cust1 "What? Can't I just buy these few items..."
        clo_cust2 "But I only need to..."
        clo_cust3 "But I dont have time to come bac..."
        clo_cust4 "What terrible servi..."
        pcs "Please leave in an orderly manner and security will lead you out of the mall!"
        "Eventually you get all the customers to leave"
        scene bg_commercial_area_mall_screen
        $ face = 2
        pc "Great, spend ages getting them all to leave and then the power comes on as soon as the last one is out the door."
        $ face = 0
        $ player.tired -= 2


    elif randomnum == 2:
        $ face = 1
        "easy day"
        pc "Lucky there are no customers in the store. Looks like we can just relax in the back room until the power comes back on."
        suzie "Lucky!"
        "You spend some time relaxing in the dark chatting with [suzie]"
        scene bg_commercial_area_mall_screen
        $ face = 4
        pc "Damn! Suppose that means we have to reopen the store..."
        $ face = 0
        suzie "Yeah..."
        $ player.tired += 1
        $ player.add_mood += 2
    else:

        "Normal day"
        $ face = 0
        suzie "Lucky there are only a couple of customers in the store. I'll go tell them we are closing while you get ready to lock up."
        pc "Ok."
        "You lock up once the last customer has left then spend a bit of time with [suzie]."
        scene bg_commercial_area_mall_screen
        $ face = 4
        suzie "Ah, back on. Well suppose that means we need to open back up."
        $ face = 0

    $ work_clothing_events_counter += 1
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_common_08:
    if pregnant >= 3:
        "As you are arranging clothes on a rack, a customer catches your eye and starts heading towards you."
        pc "Hello ma'am, how can I hel..."
        preg "Slut!"
        $ face = 4
        pc "Whaaa?"
        preg "Girl your age and pregnant already. You slut!"
        pc "Errr... What's your prob..."
        preg "Society going down the toilet with people like you living in it! Thats what my problem is!"
        pc "Ok... If you say so..."
        preg "I do! You should be ashamed of yourself!"
        $ face = 2
        "The lady then marches off and leaes the store leaving you gobsmacked."
        pc "Ok... That was unexpected."
        $ face = 0
        $ player.will -= 5
        $ player.add_mood -= 5
    else:
        jump work_clothing_weights
    $ work_clothing_events_counter += 1
    $ t.minute = 22
    jump work_clothing_weights

label work_clothing_events_common_09:
    if t.hour < 20:
        "The store is pretty quiet and you are spending some time relaxing when you see [marco] heading towards you."
        marco "Hey [name]. Since the store is quiet today I want you to head out and hand out some fliwers on the streets. It should hopefully get more people int the store."
        pc "Sure, no problem."
        "You grab a stack of fliers off [marco] and head outside."
        jump work_fliers
    else:
        jump work_clothing_weights




label work_clothing_events_rare_01:
    "A rare event where some boys from the mall come in to try and chat you up"
    "As you are tidying up some of the shelves, you notice that a couple of young guys keep looking at you"
    if player.looks >= 4:
        "one of them comes"
        "Eventually one of the guys comes over to you."
        pc "Hi, how can I help you?"
        guy1 "Oh I don't need help, I just couldn't leave without coming up and saying Hi to such a beautiful girl."
        menu:

            "Whaaa..." if player.will < 30:
                "You are shcoked"

            "Wow, do you use that line on all the girls?" if player.will >= 30 and player.mood > 30:
                "A rejection from you but the guy will try to recover"

            "Hi to you too." if player.inhibition >= 60 and player.will >= 30 and player.mood > 30:
                "You start flirting with each other"

            "You aren't bad looking yourself" if player.desire >= 80 and player.will >= 30 and player.mood > 30:
                "You start being a bit lewd with each other"

            "Not interested" if player.mood <= 30 and player.will >= 30:
                "Instant rejection"
    elif player.looks >= 8:
        "Both come"
    else:
        "Eventually they head towards the exit and leave the store."
        pc "That was odd. I wonder what they wanted?"
    $ work_clothing_events_counter += 1
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_rare_02:
    $ face = 4
    "As you are cleaning up you notice a couple of guys approach [suzie]. They don't seem the type of be shopping here so maybe they want to talk to her."
    $ face = 0

    $ work_clothing_events_counter += 1
    $ randomnum = renpy.random.randint(1, 10)
    if randomnum <= 6:
        "They try to talk to [suzie] but you can see from her face she isn't interested in talking back"
        "eventually the guys give up and leave the store"
    elif randomnum == 10:
        "They start talking to [suzie] and she seems to be smiling and laughing when talking back to them. After a few minutes the boys leave"
        "Not long after, you notice [suzie] heading towards you."
        suzie "Hey, can you cover the till for me while I go for my break?"
        $ face = 1
        pc "Sure, no problem."
        suzie "Thanks."
        $ randomnum = renpy.random.randint(1, 10)
        if randomnum <= 6:
            "A little while later you notice [suzie] return to the store and get back to work. You notice she didn't have a coat with her so she must not have left the mall."
            pc "I wonder if she had lunch with the guys that were chatting to her."
        elif randomnum == 10:
            "A little while later you notice [suzie] return. Her hair and clothes seem a bit of a mess and she heads straight to the bathroom."
            if player.inhibition >= 70 and player.pregnancy >=2:
                $ face = 4
                pc "Looks like she might also be getting a fat belly soon."
            elif player.inhibition >= 70:
                pc "Looks like she had a fun break with the guys."
            elif player.inhibition <= 30:
                $ face = 2
                "Wow, is she a slut coming back like that after going with those guys?"
            elif player.desire >= 80:
                pc "Someone got some action it seems. Lucky."
                $ player.desire += 5
            elif player.will <= 30:
                pc "Getting fucked on her break, how nice."
            else:
                pc "Wow, seems someone had a good break."
        else:
            "A little while later you notice [suzie] return to the store and get back to work. You notice she didn't have a coat with her so she must not have left the mall."
            pc "She has been smiling the entire time since coming back. Wonder if she met the boys that she was chatting to."
            if player.inhibition >= 80:
                pc "Hope that smile is because she got some action from the boys."
            elif player.desire >= 80 and player.inhibition >= 60:
                pc "Shame It's not boys giving me a smile like that. Making me wet just thinking about what she got up to"
            elif player.desire >= 80 and player.inhibition < 60:
                pc "Getting a smile like that from the boys, I wouldn't mind a kiss as well."
            elif player.desire >= 80 and player.inhibition <= 30:
                pc "Getting a smile like that from the boys, Oooh."
            elif player.will <= 30:
                pc "Leaving to meet some boys and coming back with that smile. I could do with some guys ordering me around as well."
    else:

        "She flirts with the boys for a while and eventually you see [suzie] write something on a piece of paper and hand it to them. Her phone number?"
        "The guys leave and seem to be talking happily with each other. Probably happy they got her number."
    $ face = 0
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_rare_03:
    "You and suzie are gossiping at the counter when a couple of boys come in and flirt with the both of you. The choices here are dependant on you and suzies relationship"
    "If you have witnessed some of suzies slutty behaviour and your own stats. if the stars allign you can end up having a 4some in the back room."
    $ work_clothing_events_counter += 1
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_rare_04:
    "A rare event where some guy wants to buy some clothes for his daugther. he asks you to model them for him and things get progressively more naughty"
    "As you are cleaning up the shop floor, a guy comes up to you."
    guy "Hello miss, I wonder if you could help me?"
    pc "Sure sir, how can I help?"
    guy "Well I am trying to buy some clothes for my daughter but I am honestly at a bit of a loss."
    guy "I want to try to buy something cool, but as you can see I have no idea what young girls might like and I am worried I might buy something too innapropriate."
    pc "Well sure I can help you with that."
    guy "Wonderful, wonderful. Well if you could put these on for me so I can see how they look it would be wonderful."
    menu:
        "Ok, the changing rooms are this way" if player.willpower <=20:
            guy "Wow, Excellent."
            jump work_clothing_events_rare_04_changing

        "Errm, ok, let's go to the changing rooms" if player.willpower <=40 and >20:
            guy "Encellent, thank you."
            jump work_clothing_events_rare_04_changing

        "Wait what? Put them on?" if player.willpower <= 60 and > 40:
            jump work_clothing_events_rare_04_questions

        "Wait, I can give advice but not put them on for you." if player.willpower >= 80 and player.desire <= 20:
            guy "So you won't show me how they look?"
            pc "No, I will not wear them for you."
            jump work_clothing_events_rare_04_rejection

        "Wait, I can give advice but you are asking me to put them on for you?" if player.willpower >= 80 and player.desire > 20 and < 80:
            jump work_clothing_events_rare_04_questions

        "Wait, are you asking for me to be your model?" if player.willpower >= 80 and player.desire >= 80:
            jump work_clothing_events_rare_04_questions

label work_clothing_events_rare_04_questions:
    guy "Well you are about the same size as my daughter so I should be able to get a good idea of how they look if I can see them on you."
    if bra == 0 or pants == 0:
        menu:
            "No I dont think I can do that for you since I am not wearing a bra." if bra == 0 and pants > 0 and player.inhibition >=40:
                jump work_clothing_events_rare_04_rejection

            "Well, I dont have a bra on, is that ok?" if bra == 0 and pants > 0 and player.inhibition <=40:
                guy "Oh thats fine dear, thats fine. Here, lets go to the changing rooms."
                jump work_clothing_events_rare_04_changing

            "No I dont think I can do that for you since I dont have any underwear on." if pants == 0 and player.inhibition >=20:
                jump work_clothing_events_rare_04_rejection

            "Well I'm not wearing any underwear. Are you okay with that?" if pants == 0 and player.inhibition <=20:
                guy "Oh thats fine dear, thats fine. Here, lets go to the changing rooms."
                jump work_clothing_events_rare_04_changing

            "Well, be warned I am only wearing what you can see." if bra == 0 and pants == 0 and player.inhibition <=40 and player.desire >= 80:
                guy "Oh? Thats good, fine I mean. Thats fine..."
                guy "Come, lets head to the changing rooms quickly."
                jump work_clothing_events_rare_04_changing

            "Well, I am not wearing underwear but I think thats fine. The changing rooms are this way." if player.will < 30:
                jump work_clothing_events_rare_04_changing

            "Errm, I am not wearing much underneath and not sure I am comfortable with showing you." if player.will > 30 and < 60:
                guy "I don't mind, it's fine, it's fine."
                menu:
                    "Errm, okay I suppose." if player.will < 45:
                        jump work_clothing_events_rare_04_changing
                    "Errm, no I am not comfortable with this" if player.will >= 45:
                        jump work_clothing_events_rare_04_rejection

            "No, I don't want to be modeling for you, especially when I am not wearing much underneath" if player.will >= 60:
                jump work_clothing_events_rare_04_rejection
    else:

        menu:
            "This could be fun." if player.desire >= 80:
                jump work_clothing_events_rare_04_changing

            "The changing rooms are this way." if player.will < 30:
                jump work_clothing_events_rare_04_changing

            "Errm, I and not sure I am comfortable changing with you." if player.will > 30 and < 60:
                guy "I don't mind, it's fine, it's fine."
                menu:
                    "Errm, okay I suppose." if player.will < 45:
                        jump work_clothing_events_rare_04_changing
                    "Errm, no I am not comfortable with this" if player.will >= 45:
                        jump work_clothing_events_rare_04_rejection

            "No, I don't want to be modeling for you, I am here working." if player.will >= 60:
                jump work_clothing_events_rare_04_rejection


label work_clothing_events_rare_04_rejection:
    guy "Thats a shame."
    guy "Well ok, here you go miss, I dont think I will be purchasing these items after all. Good day to you."
    "They guy hands you the clotes he had in his hands and leaves the store."
    pc "Hmm, some of these clothes are very revealing. Why would he be picking these up for his daughter?"
    $ work_clothing_events_counter += 1
    $ t.minute = 31
    jump work_clothing_weights

label work_clothing_events_rare_04_changing:
    "You lead the guy to the changing rooms and he eagerly follows behind with his pile of clothes."
    pc "Here we are, so what do you have there?"
    guy "Well I have some tops, a skirs and some pants."
    pc "Ok, What would you like to see first?"
    pc "Buying pants for his daughter...?"
    guy "Here you go, try these first."
    "He hands you a full outfit."



    "I will continue this questline later as it's getting really long"





    $ work_clothing_events_counter += 1
    $ t.minute = 35
    jump work_clothing_weights

label work_clothing_events_rare_05:
    "A rare event where a guy comes in and flirts with you, eventually he claims hes a photographer and wants you to model for him"
    "You can agree, disagree or demand money"


    $ work_clothing_events_counter += 1
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_rare_06:
    "A rare event where someone comes in and flirts with you, he invites you to have a coffee."
    "random factor decides if he leaves normally, asks for a kiss or something more"
    $ work_clothing_events_counter += 1
    $ t.minute = 36
    jump work_clothing_weights

label work_clothing_events_rare_07:
    "A rare event where a guy flat out asks you to flash him"
    $ work_clothing_events_counter += 1
    $ t.minute = 22
    jump work_clothing_weights







label work_clothing_events_vrare_01:
    "A very rare event where a guy is asking clothing advice, then asks you to model for him. then offers to pay for sex."
    $ work_clothing_events_counter += 1
    $ t.minute = 55
    jump work_clothing_weights

label work_clothing_events_vrare_02:
    "A very rare event where a guy is asking clothing advice, then asks you to model for him. then offers to pay for sex."
    $ work_clothing_events_counter += 1
    $ t.minute = 55
    jump work_clothing_weights
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
