




init python:

    class Random_list_generator(object):
        def __init__(self):
            self.random_list_generator_variable = ""
        
        
        
        
        
        @property
        def name_deg(self): 
            name_list = ("sugar tits", "sweet cheeks", "sexy", "babe", "doll", "fluffy")
            return renpy.random.choice(name_list)
        @property
        def name_deg_upper(self):
            name_list = ("sugar tits", "sweet cheeks", "sexy", "babe", "doll", "fluffy")  
            return renpy.random.choice(name_list).capitalize()
        
        @property
        def name_sexy(self): 
            name_list = ("whore", "bitch", "dirty cunt", "slut")
            return renpy.random.choice(name_list)
        @property
        def name_sexy_upper(self):
            name_list = ("whore", "bitch", "dirty girl", "slut")  
            return renpy.random.choice(name_list).capitalize()
        
        @property
        def name_cute(self): 
            name_list = ("baby", "cutie", "sexy", "darling", "sweetheart", "petal", "lovely")
            return renpy.random.choice(name_list)
        @property
        def name_cute_upper(self):
            name_list = ("baby", "cutie", "sexy", "darling", "sweetheart", "petal", "lovely")
            return renpy.random.choice(name_list).capitalize()
        
        @property
        def name_breasts(self): 
            if player.breasts == 1:
                sizelist = ("small", "perky")
            elif player.breasts == 2:
                sizelist = ("pert", "pert")
            else:
                sizelist = ("huge", "big", "massive")
            namelist = ("boobs", "tits", "breasts")
            name1 = renpy.random.choice(sizelist)
            name2 = renpy.random.choice(namelist)
            return (name1 + " " + name2)
        
        @property
        def praise_good(self):
            name_list = ("good girl", "good obedient girl", "good little bunny", "good poppet", "good little flower", "good little pet")
            return renpy.random.choice(name_list)
        @property
        def praise_good_upper(self):
            name_list = ("good girl", "good obedient girl", "good little bunny", "good poppet", "good little flower", "good little pet")
            return renpy.random.choice(name_list).capitalize()
        
        
        
        
        @property
        def scav_search(self): 
            name_list = [
            "Anything here...?", 
            "Is that something?", 
            "Maybe over there?", 
            "Is that something?", 
            "Hmm, what's that?", 
            "Let's see...", 
            "Come on, there has got to be something.",
            "Come on shiny things.", 
            "Give me something interesting...", 
            "Is that something over there?", 
            "What's this? Worth anything?", 
            "Hmmm... Anything?", 
            "Hello! What's this?", 
            "Gimme gimme gimme.",
            ]
            return self.get_entry(name_list)
        
        
        
        
        
        @property
        def singing_dialogue_1(self):
            self.random_list_generator_variable = numgen(0, 11)
            return WeightedChoice([
            ("{font=DejaVuSans.ttf}\u266A{/font} Want you to make me feel, like I'm the only girl in the world. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 0, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Last Friday night, yeah, we danced on tabletops. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 1, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Last Friday night, we went streaking in the park. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 2, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I threw a wish in the well. Don't ask me, I'll never tell. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 3, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Hey, I just met you. And this is crazy. But here's my number. So call me, maybe. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 4, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} There ain't no reason you and me should be alone tonight. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 5, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Making my connection as I enter the room. Everybody's chilling as I set up the groove. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 6, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I've had a little bit too much. All of the people start to rush. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 7, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} When the sun shines, we'll shine together. Told you I'll be here forever. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 8, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Wanna get dirty. It's about time that I came to start the party. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 9, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Like a cat in heat stuck in a moving car. A scary conversation. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 10, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I stay out too late. Got nothing in my brain. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        @property
        def singing_dialogue_2(self):
            return WeightedChoice([
            ("{font=DejaVuSans.ttf}\u266A{/font} Like I'm the only one that you'll ever love. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 0, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} And we took too many shots, think we kissed, but I forgot. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 1, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Skinny dipping in the dark then had a meme a twa. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 2, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I looked to you as it fell. And now you're in my way. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 3, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} It's hard to look right. At you, baby. But here's my number. So call me, maybe. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 4, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} But I got a reason that you should take me home tonight. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 5, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Pumping up the volume with this brand new beat. Everybody's dancing and their dancing for me. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 6, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} A dizzy twister dance. Can't find my drink or man. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 7, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Said I'll always be your friend. Took an oath, I'ma stick it out to the end. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 8, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Sweat dripping over my body. Dancing, getting just a little naughty. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 9, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Shut my eyes, can't find the brake. What if they say that you're a climber? {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 10, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} That's what people say, mm-mm. That's what people say, mm-mm. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        @property
        def singing_dialogue_3(self):
            return WeightedChoice([
            ("{font=DejaVuSans.ttf}\u266A{/font} Like I'm the only one who knows your heart. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 0, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Last Friday night, yeah, we maxed our credit cards. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 1, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Last Friday night, yeah, I think we broke the law. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 2, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I trade my soul for a wish. Pennies and dimes for a kiss. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 3, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Hey, I just met you. And this is crazy. But here's my number. So call me, maybe. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 4, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I need a man that thinks it right when it's so wrong. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 5, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I'm your operator, you can call anytime. I'll be your connection to the party line. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 6, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Where are my keys, I lost my phone. What's going on on the floor? {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 7, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Now that it's raining more than ever. Know that we'll still have each other. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 8, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Wanna get dirty! {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 9, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Naturally I'm worried if I do it alone. Who really cares? 'Cause it's your life. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 10, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I go on too many dates. But I can't make 'em stay. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        @property
        def singing_dialogue_4(self):
            return WeightedChoice([
            ("{font=DejaVuSans.ttf}\u266A{/font} Only girl in the world. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 0, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} And got kicked out of the bar, so we hit the boulevard. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 1, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Always say we're gonna stop-op, oh-woah. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 2, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I wasn't looking for this. But now you're in my way. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 3, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} And all the other boys. Try to chase me. But here's my number. So call me, maybe. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 4, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} Right on the limit's where we know we both belong tonight. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 5, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I'm coming up so you better get this party started! {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 6, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} I love this record baby, but I can't see straight anymore. WHOOO! {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 7, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} You can stand under my umbrella. You can stand under my umbrella, ella, ella. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 8, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} It's about time for my arrival. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 9, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} You never know, it could be great. Take a chance 'cause you might grow. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 10, 1, 0)),
            ("{font=DejaVuSans.ttf}\u266A{/font} At least that's what people say, mm-mm. That's what people say, mm-mm. {font=DejaVuSans.ttf}\u266A{/font}", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        
        
        
        
        @property
        def gagged_dialogue(self):
            name_list = (
            "Mmmfff ug rrrfff unnnnn *gestures to this and that*",
            "Uuugg ah mmffff. Unnn ag mfffff hrmmmmfff.", 
            "Unnggg Hhhaa.", 
            "Mmmmff aaa nnnngggg mmffff hrrmmmffff. *pointing*", 
            "Unnggg mfff mmmmffffff unn.", 
            "Uggg nnngg mfffffmmmm hmmmmmfff, Ugg aah mmmmffff hhrrrmmmmmfff...", 
            "*Gestures here and there* Mmmmfff unnnngggg...")
            return renpy.random.choice(name_list).capitalize()
        
        @property
        def drunk_dialogue(self):
            name_list = (
            "Fuck I am so drunk...",
            "Ugh, I think I drank way too much...", 
            "Think I need to calm down on the booze.", 
            "Woah! Head spinning...", 
            "Oooh been drinking too much I think...", 
            "Starting to really feel the booze.", 
            "Gonna end up blottoed if I don't calm down on the drink.")
            return renpy.random.choice(name_list)
        
        @property
        def horny_dialogue(self):
            name_list = (
            "I am so horny.",
            "Hmm... I wonder if... No! Calm down...", 
            "I am so wet right now.", 
            "Hmmm, I wonder if... \u2665", 
            "I want to go have fun with someone.", 
            "Going to leave a puddle on the floor at this rate...", 
            "I need a cold shower...")
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_dialogue(self):
            name_list = (
            "\u2665",
            "Mmmmmm...", 
            "Feel so good to be full up!", 
            "Fuck me! \u2665", 
            "Oh yes! Like that!", 
            "Keep going!", 
            "Yes! Yes! Oh yes! \u2665")
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_sold_dialogue(self):
            name_list = (
            "Fuck me like a good whore!",
            "Fuck me. Get your money's worth!", 
            "Like fucking a whore do you?", 
            "Fuck me! \u2665", 
            "Just because you are paying me, doesn't mean I can't enjoy it!", 
            "Hope I am worth the money.", 
            "Mmm yes! Fuck me!")
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_sold_regret_dialogue(self):
            name_list = (
            "Can't believe I am resorting to letting people put their dick in me for money.",
            "Letting him put his dick in me just so I can earn some money...", 
            "The things I am forced to do for money...", 
            "I wish I didn't need the money this badly.", 
            "Sex for money...", 
            "Hurry up and do what you paid for.", 
            "Taking a dick for money...")
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_forced_dialogue(self):
            name_list = (
            "Rapist piece of shit!",
            "Cunt! Having to force me to do this.", 
            "*SOB*", 
            "I can't believe this is happening.", 
            "Hurry up you piece of shit.", 
            "...", 
            "What a cunt. Having to force someone...")
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_forced_freeuse_dialogue(self):
            name_list = (
            "I allowed him to have his way but he could at least be gentler.",
            "Don't you see I am not resisting? So at least go easy on me.", 
            "Hurry up you rapist shit. You are pushing my free use to the limits.", 
            "Raping someone who's free use. What an idiot!")
            return renpy.random.choice(name_list)
        
        
        
        
        
        @property
        def whore_start_available(self):
            return WeightedChoice([
            ("I hang around and try to make myself look available.", 1),
            ("I try to strike some sexy poses and show I am available to anyone who sees me.", 1),
            ("I look as easy and available as I can while hanging around.", 1),
            ("I wander around the tables while giving men the eye to show I am available.", If (loc(loc_pub), 1, 0)),
            ])
        
        @property
        def whore_start_waiting(self):
            return WeightedChoice([
            ("C'mon. I don't want to be standing here all day...", 1),
            ("Ugh. No one at all?", 1),
            ("Hmmm, no one?", 1),
            ("All these drunks and no one wants a whore?", If (loc(loc_pub), 1, 0)),
            ("Not even charging you money and you still make me wait?", If (player.has_perk(perk_freeuse), 1, 0)),
            ])
        
        @property
        def whore_start_location_here_is_good(self):
            return WeightedChoice([
            ("Ok, well, this is as good a place as any.", 1),
            ("Right here is fine.", 1),
            ("No one should disturb us here.", 1),
            ("Let's pop into one of the cubicles.", If ("toilet" in loc_cur.name or "locker" in loc_cur.name, 1, 0)),
            ("No one should be able to see us here.", If (loc_cur == loc_bushes, 1, 0)),
            ])
        
        @property
        def whore_start_see_customer(self):
            return WeightedChoice([
            ("I see someone paying more attention to me than normal so I go up to him.", 1),
            ("I seem to have caught the attention of someone so I put on a flirty smile and go to speak to him.", 1),
            ("I see someone looking at me and heading towards me, so I give him a sultry look as he approaches.", 1),
            ("Someone is walking past smiling at me so I decide to go and say hello.", 1),
            ])
        @property
        def whore_start_see_customer_speak(self):
            return WeightedChoice([
            ("Hey sweetie. Looking for some company?", 1),
            ("Hi darling. Want to spend some time together?", 1),
            ("Hey baby. Want someone to warm your bed?", 1),
            ("Like what you see?", 1),
            ])
        @property
        def whore_start_see_customer_speak_reply(self):
            return WeightedChoice([
            ("Fuck sexy. Sure, let's have some fun.", 1),
            ("Hope you are as dirty as you look.", 1),
            ("Girl like you warming my cock? Let's go.", 1),
            ("Fuck so sexy. C'mon then.", 1),
            ])
        
        @property
        def whore_start_location_somewhere_else(self):
            return WeightedChoice([
            ("Let's go somewhere more private.", 1),
            ("Let's go somewhere where we won't be caught.", 1),
            ("Somewhere quiet would be better, follow me.", 1),
            ("Let's go somewhere else so I can have fun with that cock of yours.", If (player.soldprice == 0, 1, 0)),
            ("Not very private here, come with me.", 1),
            ])
        
        @property
        def whore_start_location_somewhere_follow(self):
            return WeightedChoice([
            ("Okay, I'll follow you.", 1),
            ("Sure, lead the way.", 1),
            ("Okay, let's go.", 1),
            ("Sounds good.", If (player.soldprice == 0, 1, 0)),
            ("Okay, I'll follow you.", 1),
            ])
        
        @property
        def whore_start_location_give_money(self):
            return WeightedChoice([
            ("So... money first.", 1),
            ("Ok, hand over the money.", 1),
            ("Money before we do anything more.", 1),
            ("Pay up before we do anything more.", 1),
            ])
        
        @property
        def whore_start_location_give_money_reply(self):
            return WeightedChoice([
            ("Sure, here you go.", 1),
            ("Right... Here we go.", 1),
            ("Ah right. Here you are.", 1),
            ("Sure.", 1),
            ])
        
        
        
        
        
        @property
        def flirt_start_available(self):
            return WeightedChoice([
            ("I hang around and chat to the odd guy who seems interested.", 1),
            ("I chat and flirt with guys passing who look like they are up for some fun.", 1),
            ("I hand around, striking up conversation with guys who look like they might be interested.", 1),
            ("I wander around the tables while chit chatting with some of the guys.", If (loc(loc_pub), 1, 0)),
            ])
        
        @property
        def flirt_start_waiting(self):
            return WeightedChoice([
            ("C'mon. I don't want to be standing here all day...", 1),
            ("Ugh. No one at all?", 1),
            ("Hmmm, no one?", 1),
            ("All these drunks and no one wants to have some fun?", If (loc(loc_pub), 1, 0)),
            ])
        
        @property
        def flirt_guy_start(self):
            return WeightedChoice([
            ("I chat away to the guy and he seems to be showing interest. I act all flirty and make it clear I am up for some fun.", 1),
            ("The guy seems to be hooked, so I brush up against him and show clear interest.", 1),
            ("As I chat to the guy, I am way more touchy feely than usual and show clear interest in some fun.", 1),
            ("I am all over the guy and showing clear interest. The guy also seems happy and receptive.", 1),
            ])
        
        @property
        def flirt_guy_pc_cont(self):
            return WeightedChoice([
            ("...a guy like you. It could be fun...", 1),
            ("...but im sure a good looking guy like you already knows that...", 1),
            ("...always nice to have someone strong next to me, it feels so much...", 1),
            ("...haha, that sounds really nice. It would be fun to...", 1),
            ])
        
        @property
        def flirt_guy_man_cont(self):
            return WeightedChoice([
            ("...such a pretty girl like you, I am sure it...", 1),
            ("...and looking at you, I am not surprised...", 1),
            ("...and then we could go somewhere quiet and alone...", 1),
            ("...for something interesting, it sure would be like that...", 1),
            ])
        
        @property
        def flirt_guy_wrapup(self):
            return WeightedChoice([
            ("We continue chatting away until I am sure we are both on the same page and decide to seal the deal.", 1),
            ("We continue chatting away while I touch him and make it clear what I want from him.", 1),
            ("As I keep flirting with him, it's clear he wants the same thing as me, so I decide to cut to the chase.", 1),
            ("He seems as eager as I am, so I decide to offer what we both want.", 1),
            ])
        
        @property
        def flirt_guy_wrapup_pc(self):
            return WeightedChoice([
            ("So how about we go somewhere more private to chat?", 1),
            ("Mmm, would be nice if we had more privacy. You up for going somewhere more quiet?", 1),
            ("How about we go somewhere more quiet so we have more privacy?.", 1),
            ("Hehe, I think we should maybe go somewhere a bit more quiet for that.", 1),
            ])
        
        
        
        
        
        @property
        def sex_exclaim_like(self):
            return WeightedChoice([
            ("Haa \u2665", 1),
            ("Ooooh!", 1),
            ("Unnngg. \u2665", 1),
            ("Oh yes!", If (player.desire > 80, 1, 0)),
            ("Ah fuck.", If (player.desire > 80, 1, 0)),
            ])
        
        @property
        def sex_exclaim_like_reply(self):
            return WeightedChoice([
            ("Oh you like that?", 1),
            ("Knew a bitch like you would like that.", 1),
            ("Dirty girls always love their ass being beat.", 1),
            ("Knew a dirty slut like you would love that.", If (player.isslut, 1, 0)),
            ("Ah the slut likes being spanked?", If (player.isslut, 1, 0)),
            ("Oh even whores love a good spanking?", If (player.iswhore, 1, 0)),
            ])
        
        @property
        def sex_exclaim_more(self):
            return WeightedChoice([
            ("Yes! Do it again. \u2665", 1),
            ("Ah fuck!", 1),
            ("Mmmmmm.", 1),
            ("\u2665", 1),
            ("More!", 1),
            ])
        
        @property
        def sex_exclaim_negative(self):
            return WeightedChoice([
            ("Ah shit!", 1),
            ("Ah fuck!", 1),
            ("Ah!", 1),
            ("What the...!", 1),
            ("Hey!", 1),
            ])
        
        @property
        def sex_exclaim_wolfman(self):
            return WeightedChoice([
            ("Awoooo!", 1),
            ("You dirty little bitch.", 1),
            ("You're a bad little bitch.", 1),
            ("Woof!", 1),
            ("Take it like a good bitch.", 1),
            ])
        
        @property
        def sex_exclaim_bitch(self):
            return WeightedChoice([
            ("Woof woof!", 1),
            ("\u2665", 1),
            ("Haa \u2665", 1),
            ("Ooooh!", 1),
            ("Unnngg. \u2665", 1),
            ])
        
        @property
        def foreplay_badgirl_comment(self):
            return WeightedChoice([
            ("You dirty girl.", 1),
            ("You dirty little bitch.", 1),
            ("You're a bad little girl.", 1),
            ("Nice big titted bitch.", If (player.breasts == 3, 1,0)),
            ("Ah you're a nice little slut.", If (c.slutty , 1,0)),
            ])
        
        @property
        def foreplay_goodbitch_comment(self):
            return WeightedChoice([
            ("Good girl.", 1),
            ("Whose a good girl?", 1),
            ("Ah you're a nice little bitch.", 1),
            ])
        
        @property
        def foreplay_like_clothes_ask(self):
            return WeightedChoice([
            ("You like when I show off my huge tits in this top? They are almost spilling out", If (c.clevage and player.breasts == 3, 1,0)),
            ("You like when my nipples poke through my clothes like this?", If (c.pokenips, 1,0)),
            ("You like my tits while I am wearing this?", If (c.clevage , 1,0)),
            ("You like looking at my huge milk tits when I wear this?", If (c.clevage and player.pregnancy >= 2 and player.breasts >= 2, 1,0)),
            ("You like my tits like this when I don't wear a bra?", If (c.clevage and c.bra == 0, 1,0)),
            ("You like my ass when I wear something so tight?", If (c.ass , 1,0)),
            ("You like it when I wear clothes that show off my pregnant belly?", If (player.preg_knows and c.belly, 1,0)),
            ("You like it when I wear such revealing clothes?", If (c.slutty , 1,0)),
            ])
        
        @property
        def foreplay_want_undress_ask(self):
            return WeightedChoice([
            ("Hmm... Wonder if you would like to see my bare ass instead?", 1),
            ("Bet you want me to take this off so you can have a look at my tits.", 1),
            ("Want to see me dropping my clothes on the floor?", 1),
            ("Want to see me take my clothes off?", 1),
            ("Shall I do a striptease for you?", 1),
            ("Want me to take this off so you can have a look at these huge tits?", If (player.breasts == 3, 1,0)),
            ])
        
        @property
        def foreplay_like_boobs_ask(self):
            return WeightedChoice([
            ("Like what you see?", 1),
            ("You like having a girl in front of you showing off her tits?", 1),
            ("You like a girl with huge tits like these?", If (player.breasts == 3, 1,0)),
            ("Mmm, just enough to fill both hands don't you think?", If (player.breasts == 2, 1,0)),
            ("Wonder if you are the type that likes a smaller girl.", If (player.breasts == 1, 1,0)),
            ])
        
        @property
        def foreplay_like_ass_ask(self):
            return WeightedChoice([
            ("Like what you see?", 1),
            ("Like having a look at my arse?", 1),
            ("You like having a girl in front of you showing off her bare arse?", 1),
            ])
        
        @property
        def foreplay_nice_cock(self):
            return WeightedChoice([
            ("Oh, not a disappointment at all.", 1),
            ("Already up eh?", 1),
            ("Looks like your friend is happy to see me.", 1),
            ])
        
        @property
        def foreplay_nice_cock_reply(self):
            return WeightedChoice([
            ("Sexy girl like you? Of course it's happy.", 1),
            ("Of course. Been a while since I had a girl on the end of it.", 1),
            ("Not every day a slutty barmaid drags you off somewhere alone.", If(dis(dis_pub) and c.outfit==6, 1, 0)),
            ("Mmm. Getting a chance with a dirty little barmaid makes it stand up pretty quickly.", If(dis(dis_pub) and c.outfit==6, 1, 0)),
            ("Those giant tits of yours had me hard before we even came in here.", If (player.breasts == 3 and not loc_cur.outside, 1, 0)),
            ("A drunken barmaid rushes me off somewhere alone so of course I am ready to go. Can't have you sobering up and changing your mind.", If (player.check_drunk(2) and dis(dis_pub) and c.outfit==6, 1, 0)),
            ("Why else would I pay you to get me off if I wasn't already horny?", If (player.soldprice or player.selling, 1, 0)),  
            ("With a drunk whore like you? Of course!", If (player.check_drunk(2) and (player.soldprice or player.selling), 1, 0)), 
            ])
        
        @property
        def foreplay_preparesex_fours(self):
            return WeightedChoice([
            ("I head over to the bed and get on fours, exposing my ass for him to get behind.", If(loc_cur.loc_type == "room", 1, 0)),
            ("I get on the bed and stick my ass out for him to have fun with.", If(loc_cur.loc_type == "room", 1, 0)),
            ("I get on my fours and look behind me, preparing to be taken.", 1),
            ("I get down into the sand, sticking my ass out and wait for him to mount me.", If(loc_cur.loc_type == "beach", 1, 0)),
            ("The floor isn't too hard so I get down doggy style and teasingly look at the guy.", If(loc_cur.loc_type == "plaster", 1, 0)),
            ])
        
        @property
        def foreplay_preparesex_ontop(self):
            return WeightedChoice([
            ("He lays down and I get on top of him.", 1),
            ("I lay him down then get on top, straddling him with his cock between my legs.", 1),
            ])
        
        @property
        def foreplay_preparesex_wall(self):
            return WeightedChoice([
            ("I lean against the wall, sticking my ass out.", 1),
            ("I press against the wall ready for him to take me from behind.", 1),
            ])
        
        @property
        def foreplay_preparesex_layback(self):
            return WeightedChoice([
            ("I lay down and wait for the guy.", 1),
            ("I head over to the bed and lay down.", If(loc_cur.loc_type == "room", 1, 0)),
            ("I lay down on the bed and look at the guy invitingly, waiting for him to come over.", If(loc_cur.loc_type == "room", 1, 0)),
            ])
        
        
        @property
        def dirtytalk_handob_guy(self):
            return WeightedChoice([
            ("Ah yes! Keep going like that. So nice!", 1),
            ("Fuck! You slutty little barmaid!", If(dis(dis_pub) and c.outfit==6, 1, 0)),
            ("Ah fuck it feels nice. Love a little bitch like you wanking me off.", 1),
            ("Ah yes, like that.", 1),
            ("Fuck, you know what you are doing don't you?", If (player.hsex > 15,1,0)),
            ("Mmm, whores sure know what they are doing down there.", If (player.selling, 1, 0)),
            ("Having a whore grab your cock is great, they know how to treat it well.", If (player.selling, 1, 0)),
            ])
        
        @property
        def dirtytalk_handob_pc(self):
            return WeightedChoice([
            ("Mmm you dirty pervert, you like it when I do this?", 1),
            ("Bet you love it seeing a girl on her knees with your cock in her hand.", 1),
            ("Such a big one as well. Feels so nice and firm in my hand.", 1),
            ])
        
        @property
        def dirtytalk_guywank_pc(self):
            return WeightedChoice([
            ("Mmm, you pervert. Like wanking while looking at me?", 1),
            ("So hot having you wank off to me.", 1),
            ("Dirty boy. Like wanking off to me getting fucked by your friend?", If(any(x in ["vag", "ass"] for x in player.sex_holes), 1, 0)),
            ("Like watching me get fucked you pervert?", If(any(x in ["vag", "ass"] for x in player.sex_holes), 1, 0)),
            ("Like looking at my big tits as you wank yourself off?", If(player.breasts > 2, 1, 0)),
            ])
        
        
        
        
        
        @property
        def wanking_man_cum_action_face(self):
            return WeightedChoice([
            ("Cum suddenly shoots out of his cock and hits me in the face. But I knew this would happen so I close my eyes let more of it cover me and avoid getting it in my eye.", 1),
            ("His cock pulses harder and I point it away from my eyes and his cum shoots out and hits me in the face.", 1),
            ("He groans as he starts to cum and I close my eyes as he wanks himself harder, covering my face in his cum.", 1),
            ("He starts to grunt and points his cock at my face as he starts to cum. Making sure to keep going until his cock is done covering my face in his warm cum.", 1),
            ("He speeds up and starts to cum. Getting it all over my face and lips.", 1),
            ])
        
        @property
        def wanking_man_cum_action_face_reaction(self):
            return WeightedChoice([
            ("Oooh, it's all over my face.", 1),
            ("Mmm, it's dripping down my face and into my mouth.", 1),
            ("Oooh, like the look of my face covered in your cum?", 1),
            ("Oh yeah! Cover my face wit it.", 1),
            ("Mmm, like how I look with your cum all over me?", 1),
            ])
        
        
        
        
        
        @property
        def handjob_expecting_cock(self):
            return WeightedChoice([
            ("Mmm, show me what you have down there.", 1),
            ("Mmm, can't wait to see what you are packing.", 1),
            ("Show me what you got.", 1),
            ("Mmm, wonder what we have down here.", 1),
            ])
        
        @property
        def handjob_touch_cock(self):
            return WeightedChoice([
            ("Mmm, so warm and hard in my hand.", 1),
            ("Ha it feels so nice to have it in my hand.", 1),
            ("Solid as a rock. Been a while has it?", 1),
            ("With a cock like this, not even sure why you are paying me. Could easily get someone to do it for free.", If (player.soldprice or player.selling, 1, 0)),
            ("Always nice when people paying me have nice cocks like this.", If (player.soldprice or player.selling, 1, 0)),
            ])
        
        @property
        def handjob_wank_cock(self):
            return WeightedChoice([
            ("I stroke his cock with a nice rhythm and it seems he's enjoying it by the sounds he is making.", 1),
            ("I grip his warm cock in my hand and stroke it back and forth, slowly picking up the pace as I hear groans of pleasure from his mouth.", 1),
            ("I take his cock in my hand and start working at the shaft, stroking him while he looks at my naked tits.", 1),
            ("It is hardly the first cock I have had in my hand and I start wanking him off with expert skill. The noises he is making letting me know how fast or slow to go.", If (player.hsex > 15,1,0)),
            ("Even though he is paying me to do it, I still try to put in a good performance and make sure he gets as much pleasure out of it as possible.", If (player.soldprice or player.selling, 1, 0)),
            ("Even though he is paying me, his cock in my hand still feels nice so I put in effort to make sure to give him as much pleasure as I can give him.", If (player.soldprice or player.selling, 1, 0)),
            ])
        
        @property
        def handjob_wank_pc_say_man_close(self):
            return WeightedChoice([
            ("Oooh, what was that? I think I can feel it pulsing.", 1),
            ("Wow, getting even harder now. Ready to blow on me are you?", 1),
            ("Enjoying that are you? I can feel your cock throbbing.", 1),
            ("Oh? You're starting to leak. You close?", 1),
            ])
        
        @property
        def handjob_wank_man_say_enjoy(self):
            return WeightedChoice([
            ("Ah fuck yes!", 1),
            ("Ah fuck! Sluts like you know how to work a cock.", 1),
            ("Ah yes, like that.", 1),
            ("Fuck! How many guys have you wanked off? This feels so good!", If (player.hsex > 15,1,0)),
            ("Ah fuck you dirty whore! Keep going.", If (player.selling, 1, 0)),
            ])
        
        @property
        def handjob_blow_offer(self):
            name_list = WeightedChoice([
            ("Bet you would like it more if it were my lips around it instead of my hand.", 1),
            ("Wonder what it tastes like. I'm sure you don't mind if I have a try.", 1),
            ("Looks nice and big in my hand, but think I will try it in my mouth just to be sure.", 1),
            ("Mmm, starting to think it might be better off in my mouth.", 1),
            ("Want your slutty barmaid to suck you off?", If("work" in tab_top and c.outfit == 6, 1, 0)),
            ])
            return name_list
        
        @property
        def handjob_man_cum(self):
            return WeightedChoice([
            ("Oooh, it's coming out.", 1),
            ("Mmm it's throbbing.", 1),
            ("Mmmmm.", 1),
            ("Ooooh.", 1),
            ("Oh its so warm.", 1),
            ("Yeah cum for me!", 1),
            ("Mmmm let it all out!", 1),
            ])
        
        @property
        def handjob_man_cum_yes_dialogue(self):
            return WeightedChoice([
            ("Ah fuck you dirty little slut.", 1),
            ("Ah yes! Keep going.", 1),
            ("Ah you dirty bitch.", 1),
            ("Ah fuck yes. Keep going!", 1),
            ("Ah I am cumming!", 1),
            ("Nng fuck I am cumming.", 1),
            ("Yes, yes!", 1),
            ("You dirty slut. Keep going!", If (player.isslut, 1, 0)),
            ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def handjob_man_cum_action_hand(self):
            return WeightedChoice([
            ("Cum suddenly shoots out of his cock, landing who knows where while more pumps cover my hand as I keep wanking him.", 1),
            ("His cock pulses harder and something shoots out. I keep wanking him to milk everything he has.", 1),
            ("He groans as he starts to cum and I wank him harder getting my hand covered in cum.", 1),
            ("I feel his cock suddenly get rock hard so I go faster as he cums. Making sure to keep going until his cock is done making my hands all sticky.", 1),
            ("I speed up as he starts to cum. Getting it all over my hand and using it as makeshift lube to be more aggressive in wanking him off.", 1),
            ])
        
        @property
        def handjob_man_cum_action_face(self):
            return WeightedChoice([
            ("Cum suddenly shoots out of his cock and hits me in the face. But I knew this would happen so I keep going and let more of it cover me.", 1),
            ("His cock pulses harder and I point it away from my eyes and his cum shoots out and hits me in the face.", 1),
            ("He groans as he starts to cum and I wank him harder, getting my face and hand covered in his cum.", 1),
            ("I feel his cock suddenly get rock hard so I go faster as he cums. Making sure to keep going until his cock is done covering my face in his warm cum.", 1),
            ("I speed up as he starts to cum. Getting it all over my face and hand, using it as makeshift lube to be more aggressive in wanking him off.", 1),
            ])
        @property
        def handjob_man_cum_action_face_man(self):
            return WeightedChoice([
            ("Cum suddenly shoots out of his cock and hits me in the face. But I knew this would happen so I wait until he is done.", 1),
            ("His cock pulses harder and I tilt my face away to avoid getting it in my eyes. His cum shoots out and hits me in the face.", 1),
            ("He groans as he starts to cum all over my face.", 1),
            ("He starts to wank himself off much faster and I can see his cockhead all slick with precum, so it's no surprise when he starts spraying his load all over my face.", 1),
            ("He speeds up as he starts to cum. Getting it all over my face and lips, using it as makeshift lube to be more aggressive in wanking himself off.", 1),
            ])
        
        @property
        def handjob_pc_cum_reaction(self):
            return WeightedChoice([
            ("Looks like someone enjoyed himself.", 1),
            ("Mmm, all sticky...", 1),
            ("Mmmmm. Made a bit of a mess there. \u2665", 1),
            ("Mmm so warm.", 1),
            ("Mmm, my hand is covered in your stuff.", If(player.cum_locations["cum_hand"], 1, 0 )),
            ("Mmm, all over my face.", If(player.cum_locations["cum_face"], 1, 0 )),
            ("Mmm, like my new look?", If(player.cum_locations["cum_face"], 1, 0 )),
            ("Like a girl looking at you with a face covered in cum?", If(player.cum_locations["cum_face"], 1, 0 )),
            ])
        
        
        
        
        
        @property
        def blowjob_muffle(self): 
            return WeightedChoice([
            ("Mmmm \u2665", 1),
            ("Mmmmfff.", 1),
            ("*Slurp* Mmmmm.", 1),
            ("Mmmfff. Soo nice.", 1),
            ("*Slurp*", 1),
            ("*Hyuk* *Hyuk* *Hyuk*", 1),
            ])
        
        @property
        def blowjob_start_suck(self):
            return WeightedChoice([
            ("He relaxes back against the wall as I take his warm cock in my hand and wrap my lips around it. It feels so nice and warm being there.", 1),
            ("I take his cock in my hands and start to stroke him while I put the tip of his cock in my mouth.", 1),
            ("I see his large cock in front of my face and take it in my hands. Then slowly I lick the tip of his penis and slide my lips around his cockhead.", 1),
            ("Seeing his huge cock in front of me fills me with excitement. I take him fully in my mouth while I wrap my fingers around it to stroke his cock.", 1),
            ("Even though I am being paid to suck him off. Seeing his huge cock in front of me still makes me excited and I happily take it in my hands and wrap my lips around it.", If (player.selling, 1, 0)),
            ])
        
        @property
        def blowjob_start_suck_reaction(self):
            return WeightedChoice([
            ("It's clear from his reactions that he's enjoying himself so I continue to work at his cock and swirling my tongue around him inside my mouth.", 1),
            ("His actions make it clear he is having fun. I speed up working his shaft with my hands as I use my tongue to pleasure his cockhead.", 1),
            ("He rubs his fingers through my hair and tries to push his cock deeper into my mouth. I happily accept it and start working his shaft with my hands.", 1),
            ("He starts thrusting into my mouth in time with my head bobbing and eventually he is slowly fucking my mouth. I help him out by stroking his cock in time with his thrusts.", 1),
            ])
        
        @property
        def blowjob_cum_close(self):
            return WeightedChoice([
            ("I can taste him leaking in my mouth so I know he is about to cum very soon.", 1),
            ("I start to feel his cock tensing up and his movements become erratic. I know he is about to cum very soon.", 1),
            ("His groaning lets me know he is not far off cumming so I pick up the pace and blow him even faster than I was before.", 1),
            ("He is gripping onto my head and thrusting quite aggressively now. I know he won't last much longer at this rate so I work his shaft harder with my hands to try and push him over the edge.", 1),
            ])
        
        @property
        def blowjob_cum_mouth_man_dialogue(self):
            return WeightedChoice([
            ("Ah you dirty bitch. Take it in your mouth. Swallow it up.", 1),
            ("Ah fuck I'm gonna put it down your throat.", 1),
            ("Ah yes. Take it.", 1),
            ("Ah I am cumming!", 1),
            ("Nng fuck I am cumming.", 1),
            ("Come here and let me fill your mouth up.", 1),
            ("Yes, yes!", 1),
            ("Ah yes! I am going to fill you up.", 1),
            ("You dirty slut. Take it in your mouth.", If (player.isslut, 1, 0)),
            ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def blowjob_cum_mouth(self):
            return WeightedChoice([
            ("I feel his start to throb and push his cock deep in my mouth. He starts to cum and I feel his warmth squirting from his cock and get a good taste of his cum.", 1),
            ("He starts throbbing in my mouth and I feel the salty warmth from his cock enter my mouth.", 1),
            ("His cock starts to swell until he tenses up and releases his load in my mouth. Its warmth fill it up and I have no choice but to swallow most of it down.", 1),
            ("He throbs in my mouth and I feel the first wave fill me. I quickly swallow it down before another pulse shoots more on my tongue. I eagerly swallow that down as well until it seems he is all out of steam.", 1),
            ])
        
        @property
        def blowjob_cum_mouth_swallow_reaction(self):
            return WeightedChoice([
            ("Ohh, you put a lot in my mouth. Managed to drink it all up though.", 1),
            ("That was a lot. Thought I was going to choke.", 1),
            ("Aww, some of it is leaking down my face.", 1),
            ("Mmmm, tasty.", 1),
            ])
        
        @property
        def blowjob_cum_mouth_swallow_reaction_man(self):
            return WeightedChoice([
            ("You're a nice little cocksucker aren't you?", 1),
            ("You're a good cocksucking whore.", If(player.selling, 1, 0)),
            ("All the schoolgirls know how to suck a cock like you do?", If("school" in tab_top, 1, 0)),
            ("You barmaids sure know how to give a service.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("That's a cleaning service I didn't expect you girls would provide.", If(quest_cleaner.workcycle, 1, 0)),
            ])
        
        @property
        def blowjob_sex_ask(self):
            return WeightedChoice([
            ("Ah so nice. How about you let me fuck you?", 1),
            ("Mmm, come here. Show me that arse of yours so I can fill you with my cock.", 1),
            ("Ah you dirty slut. Come here and let me fuck you.", 1),
            ("Ah you dirty bar bitch. Come here and let me fuck you.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("Such a nice little whore. Come here so I can put my cock in you.", If (player.selling, 1, 0)),
            ])
        
        
        
        
        
        @property
        def having_sex_present_doggy(self):
            return WeightedChoice([
            ("I get on my fours and wiggle my ass, inviting him to come and take me.", 1),
            ("I get down on fours and arch my back, giving him a clear view of my holes.", 1),
            ("I get down on my hands and knees, giving him a clear view of what he will be fucking.", 1),
            ])
        
        @property
        def having_sex_present_standassup(self):
            return WeightedChoice([
            ("I drop my hands to the floor, presenting my ass to be fucked.", 1),
            ("I bend over, pressing my hands to the floor and give a clear view of my holes.", 1),
            ("I bend over and press my hands down, giving a perfect view of where I want to be fucked.", 1),
            ])
        
        @property
        def having_sex_present_onbelly(self):
            return WeightedChoice([
            ("I wiggle my ass, showing him I am prepared to be fucked.", 1),
            ("I poke my ass up off the ground, giving him a clear view of my holes.", 1),
            ("I wiggle my ass and lift my hips up, giving a perfect view of where I want to be fucked.", 1),
            ])
        
        @property
        def having_sex_present_onback(self):
            return WeightedChoice([
            ("I lay on my back, spread my legs and present myself to the guy.", 1),
            ("I get down and spread my legs, giving him a clear view of where he will be fucking me.", 1),
            ("I get down and spread myself, making sure he knows I am eager to be fucked.", 1),
            ])
        
        @property
        def having_sex_told_behind(self):
            return WeightedChoice([
            ("Bend over, I want you from behind.", 1),
            ("Come here. I want to see that sexy ass while I fuck you.", 1),
            ("Turn around, I want to take you like a bitch.", 1),
            ("Ah you dirty bar bitch. Turn around and I'll take you like one.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ])
        
        
        
        
        @property
        def having_sex_tease_vag(self):
            name_list = WeightedChoice([
            ("I feel his cock sliding between my lips as he wanks himself off a bit.", 1),
            ("I can feel him stroking his cock as the tip of his penis slides between my wet folds.", 1),
            ])
            return name_list
        
        @property
        def having_sex_tease_vag_rough(self):
            name_list = WeightedChoice([
            ("I feel his cock pressed between my folds as he wanks himself off.", 1),
            ("He presses his cock against me and starts to furiously wank himself while rubbing it up and down between my folds.", 1),
            ("I feel him slap his cock against me while wanking himself off.", 1),
            ])
            return name_list
        
        @property
        def having_sex_tease_vag_cowgirl(self):
            name_list = WeightedChoice([
            ("I feel his hard cock between my legs whenever I move around on top of him.", 1),
            ("I feel his cock jump whenever I move on top of him and it eventually rests pressing between my ass cheeks.", 1),
            ("I sit on top of his cock and feel it pulsing whenever I move or readjust on top of him.", 1),
            ])
            return name_list
        
        @property
        def having_sex_tease_ass_suprise(self):
            return WeightedChoice([
            ("Thats my arse. \u2665", 1),
            ("*Huff* \u2665 You are poking my arsehole.", 1),
            ("\u2665", 1),
            ("\u2665 Haa, that's my other hole.", 1),
            ("Ah! That's my arse. I've never done anything there before.", If(not player.asex, 10, 0)),
            ])
        
        @property
        def having_sex_penetrate_vag_slow(self):
            return WeightedChoice([
            ("His cock starts to push deeper and I feel him slowly start to stretch my pussy and fill me up inside.", 1),
            ("I feel him start to enter deeper and deeper with each poke until he is deep enough inside me that it's no longer poking but actual fucking.", 1),
            ("He gently starts to press his cock against me and in a very slow thrust, stretches my lips and starts to enter me fully.", 1),
            ])
        
        @property
        def having_sex_penetrate_vag_slow_pull(self):
            return WeightedChoice([
            ("He pulls at my hips and I feel him start to stretch me open as his cock slides inside me.", 1),
            ("I slowly lower myself onto his cock and feel myself opening up as he starts to fill my insides.", 1),
            ("I let him pull me closer and I feel his cock start to enter me until it is inside me all the way.", 1),
            ])
        
        @property
        def having_sex_penetrate_vag_cowgirl(self):
            return WeightedChoice([
            ("I lift my hips up and rock back and forth lining up his hard cock until I feel it poke in the right place. I relax my way down it, feeling it fill my insides.", 1),
            ("I hump him until I feel his cock poke at me, then gently slide myself down until it's filling me all the way.", 1),
            ("I lift my hips up and use my hand to put his cock in the right place, then slowly ease myself onto it.", 1),
            ])
        
        @property
        def having_sex_penetrate_vag_cowgirl_horny(self):
            return WeightedChoice([
            ("I am already soaking wet so when I lift up my hips and point his cock at my pussy, it has little resistance sliding inside me.", 1),
            ("I hump him until I feel his cock poke at me. Since I am soaking wet he slips inside me without me even meaning to do it.", 1),
            ("I lift my hips up and use my hand to put his cock in the right place, then slowly ease myself onto it.", 1),
            ])
        
        @property
        def having_sex_penetrate_vag_forced(self):
            return WeightedChoice([
            ("He starts shoving his cock inside me and I feel it go all the way inside me.", 1),
            ("With little warning, he presses his cock inside me.", 1),
            ("He pokes hard at me and his second attempt is forced inside me.", 1),
            ])
        
        @property
        def having_sex_penetrate_ass_slow(self):
            return WeightedChoice([
            ("He then gently presses it harder against my ass until I feel it easing its way deeper into my arse. Slowly until it is all the way inside me filling me up.", 1),
            ("He wiggles his cock against my asshole as he slowly presses it more firmly against me. It starts to slide inside me until I can feel his pelvis press against my ass checks.", 1),
            ("He gently prods against my asshole, with each prod sliding his cock a little deeper inside me. Eventually the prods turn to thrusting and I realise he has already got it all the way in and is fucking me.", 1),
            ("I gently ease back onto his slick cock and feel him start to enter me. Sliding inside deeper and deeper until he is all the way in.", 1),
            ("He gently puts more pressure on my ass until I feel it stretching open and I finally fell what it is like to have a cock in my arse.", If(player.asex <= 1, 10, 0)),
            ])
        
        @property
        def having_sex_penetrate_ass_slow_pull(self):
            return WeightedChoice([
            ("He pulls at my hips and I feel him start to poke in my ass until I feel him stretching and filling me up inside.", 1),
            ("I gently lower myself on him, feeling his cock put more pressure on my ass until it starts to slide inside me.", 1),
            ("I let him pull me closer and I feel his cock start to enter me until it is inside me all the way.", 1),
            ])
        
        @property
        def having_sex_penetrate_ass_cowgirl(self):
            return WeightedChoice([
            ("I lift my hips up and rub his cock between my lips, lubing it up a bit. Then press it against my asshole and gently lower myself down on top of it.", 1),
            ("I rub his cock between my legs a bit, then press him against my ass and gently bounce on him. Each bounce pressing him inside me slightly deeper until eventually he is all the way inside me.", 1),
            ("I rub his cock on my pussy, making it wet and then press it against my ass. I gently hump him and each time I press more on his cock until eventually he is all the way up my arse.", 1),
            ])
        
        @property
        def having_sex_penetrate_ass_forced(self):
            return WeightedChoice([
            ("He starts shoving his cock inside my arse and I feel it go all the way inside me.", 1),
            ("With little warning, he presses his cock against my arsehole and pushes it inside me.", 1),
            ("He pokes hard at my arse, and with cum still leaking out of me he manages to easily slip it in.", If(player.cum_locations["cum_assin"], 1,0)),
            ("He pokes his cock against my arsehole, struggling to get it in, until he forces it more and I feel it enter me.", If(not player.cum_locations["cum_assin"], 1,0)),
            ])
        
        @property
        def having_sex_vag_to_ass_switch(self):
            name_list = [
            "I feel him slide his cock from my wet vagina and press it against my asshole while masturbating.",
            "He rubs his cock between my legs, making sure it is nice and slick before pressing it against my asshole.",
            "He presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it.",
            "His cock is covered in my juices as he presses it against my asshole, ready to start sliding it inside me.",
            ]
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_ass_poke(self):
            name_list = [
            "I feel his cock poking at me and trying to find it's way into my arsehole.",
            "He rubs his cock between my legs, making sure it is nice and slick before pressing it against my asshole.",
            "He presses his already lubed cock against my ass and he starts to put pressure against it.",
            "His cock is covered in my juices as he presses it against my asshole, ready to start sliding it inside me.",
            ]
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_vag_to_ass(self):
            name_list = [
            "I feel slide his cock out of my wet vagina and press it against my asshole and slide it inside.",
            "He pulls his cock out of my vagina and presses it against my asshole. Already slick with my juices and precum, he is able to easily penetrate me without issue.",
            "He pulls out of my vagina and presses his already lubed cock against my ass and he starts to masturbate while putting pressure against it and gently sliding it inside me.",
            "He pulls out and his cock is covered in my juices as he presses it against my asshole, wasting no time to start sliding it inside me.",
            ]
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_asked_anal_wonder(self):
            return WeightedChoice([
            ("He is starting to poke me instead of switching to my arse...", 1),
            ("His cock should be wet enough already so he should have already put it somewhere else...", 1),
            ("Ah, he is starting to push deeper. If I let this go on he might end up trying to fill my pussy...", 1),
            ("He's poking the wrong place. I don't want to end up having my first time now...", If(player.vvirgin, 10, 0)),
            ])
        
        
        @property
        def having_sex_asked_anal_comment(self):
            
            return WeightedChoice([
            ("That's not my arse you are poking.", 1),
            ("You are poking at the wrong hole.", 1),
            ("Wrong hole, I told you to take me in the bum.", 1),
            ])
        
        @property
        def having_sex_asked_anal_respond(self):
            
            return WeightedChoice([
            ("I know. Just getting lubed up.", 1),
            ("Ah yeah...", 1),
            ("Did you? Okay sure.", 1),
            ("Don't worry, just getting it ready.", 1),
            ("Mmm, I know.", 1),
            ("Uh huh. Just having a bit of fun where it's wet.", 1),
            ("I know. Just have some fun with it.", 1),
            ("Mmm, it's so nice here.", 1),
            ("So warm and wet here.", 1),
            ("You are so wet. Sure you want it in the arse?", 1),
            ])
        
        @property
        def having_sex_asked_anal_ask(self):
            
            return WeightedChoice([
            ("Didn't you want to arse fuck me?", 1),
            ("Thought you wanted to fuck me in the arse?", 1),
            ("That's not my bum you know?", 1),
            ])
        
        @property
        def having_sex_asked_anal_ask_respond(self):
            
            return WeightedChoice([
            ("I know. Just getting lubed up.", 1),
            ("I know.", 1),
            ("One hole is just as warm as the other.", 1),
            ("Mmm, I know.", 1),
            ("Uh huh. Just having a bit of fun where it's wet.", 1),
            ("I know. Just have some fun with it.", 1),
            ("Mmm, it's so nice here.", 1),
            ("So warm and wet here.", 1),
            ])
        
        @property
        def having_sex_thats_not_anal_happy(self):
            return WeightedChoice([
            ("Ahhh. \u2665 That's not my bum...", 1),
            ("*Huff* \u2665 Wrong... Hole...", 1),
            ("\u2665", 1),
            ("\u2665 Thats not where I told you to put it.", 1),
            ])
        
        @property
        def having_sex_thats_not_anal_angry(self):
            return WeightedChoice([
            ("Fuck I told you not inside me. Take it out now!", 1),
            ("You deaf? I told you in my arse. Take it out right fucking now!", 1),
            ("Ah take it out. I told you not to put it in there!", 1),
            ("Ah take it out, now!", 1),
            ])
        
        @property
        def having_sex_mmm(self):
            name_list = (
            "Haaaaa... \u2665",
            "Mmmmm!", 
            "Oh thats nice. \u2665", 
            "Oooh!", 
            "Ahhh keep going~.",
            "Ahhhhh \u2665",
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_yes(self):
            name_list = (
            "Haaaaa... \u2665",
            "Ah fuck!", 
            "Oh yes! YES! \u2665", 
            "Yes! Yes! Yes!", 
            "Keep going! Fuck yes! Fuck me! Fuck me!", 
            "Ahhhhh \u2665 Fuuuuck! \u2665 Take me!", 
            "Yes! Yes! Oh yes! \u2665",
            "Ahhh keep going~.",
            "Ahhhhh \u2665",
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_nng(self):
            name_list = (
            "Nng! That hurts!",
            "Ow fuck!", 
            "Ahhh, a bit more gentle?", 
            "Ah shit!", 
            "Oww!", 
            "Nnnnngg!", 

            "Ahhhhh!",
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_suprise(self):
            name_list = (
            "Oh?",
            "Mmmmm!", 
            "Haaa...", 
            "Oooh!", 
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_man_yes(self):
            name_list = (
            "Ahh fuck yes!",
            "Ah fuck!", 
            "Fuck yes!", 
            "Ahhh yeeessss...", 
            "Fuck fuck fuck!", 
            "Huuuuuu...", 
            "Haa fuck!",
            )
            return renpy.random.choice(name_list)
        @property
        def having_sex_man_keep_going(self):
            return WeightedChoice([
            ("Sexy little slut. Keep going!", 1),
            ("Ah fuck, keep going like that and you will make me cum.", 1),
            ("Ah fuck yes, keep going.", 1),
            ("Yes, fuck! Keep going...", 1),
            ("*Huff* *Huff* *Huffff*", 1),
            ("Haa! Keep going you dirty whore!", If(player.selling,1,0)),
            ("AH keep going you dirty school whore!", If(player.selling and "school" in tab_top,1,0)),
            ])
        
        @property
        def having_sex_take_it_out(self):
            name_list = (
            "Take it out!",
            "Get it out of me.",
            "I told you take it out!",
            "I said take it out of me.",
            )
            return renpy.random.choice(name_list)    
        
        @property
        def having_sex_action(self):
            name_list = [
            "I feel him start to take long and deep thrusts inside me. Pushing his cock balls deep into me before pulling almost all the way out, then pushing it back in again. ",
            "He seems eager and I feel him taking quick and shallow thrusts while gripping onto my hips. He is fucking me like a horny little rabbit.",
            "He takes it slow and rhythmically thrusts in and out of me. My tits bounce back and forth in time with his thrusting and it feels very pleasant and hypnotic.",
            "He thrusts deeply into me before slowly sliding his cock out almost all the way. Then aggressively slams back into me in a quick and hard thrust.",
            "He starts to get into it more and spanks me or reaches round to grope at my tits as he is thrusting deep inside me.",
            "He starts to build momentum and it's not long before I hear his body slapping against my ass with each thrust into me.",
            "He builds up speed as I get used to him inside me and it's not long until he is harshly gripping my sides and pulling me against his thrusting cock.",
            "I am already soaking wet down there and it doesn't take him long to start hammering away at me. Fucking me hard and fast while smacking me on the arse.",
            
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_cowgirl(self):
            name_list = [
            "I rock my hips back and forth riding him while he grips onto me making pleasurable noises.",
            "He seems to enjoy himself as I bounce up and down, taking his length almost to the tip and back down again deep inside me.",
            "I takes it slow and rhythmically strides as I rock back and forth on him. He closes his eyes and just gets lost in the pleasure.",
            "I lift my hips up a bit and sway them back and forth humping him. I am not sure how he is feeling but I am enjoying it.",
            "I bounce up and down on him and he matches my motion. Whenever I descend on his cock he thrusts his hips upwards making sure I take him right to the hilt.",
            "His hands are all over my body as I rock back and forth on him. I am not sure what he's enjoying more, what I am doing to his cock or just the sight of me on top of him.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_cowgirl_rough(self):
            name_list = [
            "I furiously rock my hips back and forth riding him while focusing almost entirely on my own pleasure. That doesn't stop him from making noises that sound like he's enjoying it.",
            "I bounce up and down, taking his length almost to the tip and back down again deep inside me. I pay little attention to his pleasure but he is probably enjoying it.",
            "I dig my fingers into his skin as I hump him like a horny rabbit. Paying little attention to his pleasure and just trying to get myself off using him.",
            "I agressively ride him like he's a human dildo, focusing only on my pleasure. I hear him make some noises or say something, but I dont care and focus only on myself.",
            "I bounce up and down on him and he matches my motion. Whenever I descend on his cock he thrusts his hips upwards making sure I take him right to the hilt.",
            "His hands are all over my body as I rock back and forth on him. I am not sure what he's enjoying more, what I am doing to his cock or just the sight of me on top of him.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_struggle_pretend(self):
            name_list = [
            "I make a token effort to escape, pulling away just enough to make him keep a grip on me and pull me in closer.",
            "I wiggle away and pretend to try to get away, but in reality I end up humping against him even more.",
            "I push back against him pretending it is an effort to escape, but really I am pushing his cock deep inside me.",
            "I struggle and resist. But put no strength or effort behind it, making sure he keeps me close.",
            "I wiggle my ass in a feigned effort to escape.",
            "I wiggle and worm my way out of his grasp, but make no real effort to escape and just make sure the guy needs to put extra effort to keep me close.",
            "I try to pull away from the guy, but only just enough to make sure he keeps a grip on me and pulls me in closer.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_cowgirl_continue(self):
            name_list = [
            "I keep riding him, in and out of me as I rock back and forth. Sometimes I let him touch my tits while other times I lean down and rub them on his chest as I hump him.",
            "I fully take control and keep rocking on top of him, feeling him fill me fully when I press down on him. He is trying to match my motions but I don't pay much attention to that.",
            "I look him in the eyes as I sit on top of him, rocking my hips and feeling his hands explore my body.",
            "He grips my thighs and pushes me down onto his cock so that I take him all the way inside me, then he releases me so I can bring myself up and do it again and again.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_onback(self):
            name_list = [
            "I relax back as he is above me, watching as he thrusts into me.",
            "I lay back and enjoy the pleasure of him on top of me and inside me. ",
            "I takes it slow and rhythmically strides as I rock back and fouth, tits bouncing with each thrust.",
            "I let him take control and his hands are all over my body as he thrusts into me. I can see him looking down at me, eyes roving all over my body as he enjoys me.",
            "He spreads my legs and takes me as deep as he can. He pulls on my thighs as he trusts into me to make sure I get his full length. I just relax back and enjoy.",
            "I look him in the eyes as he holds onto me, pulling at my thighs to get as easy access as possible. On my back with my legs spread makes it very easy for him to give me his full length.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_action_ass(self):
            name_list = [
            "He relentlessly fucks me in the ass while pressing me up against the wall. I feel his hard cock pumping in and out as he roughly grips onto my ass cheeks, spreading them so he can thrust in deeper.",
            "He slowly starts to pick up the pace and places his hands on my arse cheeks, spreading them while also using them as handholds to pull me deeper onto his cock.",
            "He spreads me as he slowly fucks me in the arse. He starts out gentle but starts picking up the pace once he realises I have adjusted to his huge cock filling me up.",
            "He seems to take pleasure in pulling his cock out right to the tip, then grabbing me by the hips and pulling me balls deep back onto his cock. While it is a bit rough, it is not without its pleasure.",
            "He barely waits for me to adjust to him being in my ass before he is pounding away at me with determination. He is gripping onto my hips and thrusting like a madman. While it does hurt a bit, it is far more pleasurable than painful.",
            "He keeps pounding away while groaning or muttering some dirty words. He doesn't make much sense though as he is lost in the pleasure of fucking me in the ass.",
            "He rhythmically fucks my asshole and I get lost in the hypnotic pleasure it brings. My breasts swinging back and forth in time with each thrust.",
            "I hear my ass cheeks clapping against his body as he continuously thrusts in and out of me. I find the rhythms and sound quite exciting and get lost in the pleasure of it all.",
            "He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_enjoy(self):
            name_list = [
            "My mind starts to lose focus as I focus only on the cock thrusting in and out of me. I can feel the pleasure building up inside me.",
            "My mind goes blank as I focus only on the approaching orgasm gripping my body.",
            "My pussy starts to tighten around his cock as he brings me closer and closer to orgasm.",
            "I focus only on the man behind me pounding his nice cock in and out of me. I can barely focus as he brings my dripping pussy to orgasm.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_enjoy_cowgirl(self):
            name_list = [
            "My mind starts to lose focus as I focus only on the cock I am bouncing on. I can feel the pleasure building up inside me.",
            "My mind goes blank as I focus only on the approaching orgasm gripping my body.",
            "My pussy starts to tighten around his cock as he brings me closer and closer to orgasm.",
            "I focus only on the man under me as I slide up and down on his cock. I can barely focus as he brings my dripping pussy to orgasm.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_enjoy_cowgirl_anal(self):
            name_list = [
            "My mind starts to lose focus as I focus only on the cock I am bouncing on. I can feel the pleasure building up inside me.",
            "My mind goes blank as I focus only on the approaching orgasm gripping my body.",
            "I focus only on the man under me as I slide up and down on his cock. I can barely focus as he brings me close orgasm with his cock in my ass.",
            "I focus on the cock in my ass as he brings me closer to cumming.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_enjoy_rough(self):
            name_list = [
            "My mind starts to lose focus as he roughly grips onto me and relentlessly fucks me.",
            "My thoughts are only of him violently thrusting in and out of me while his fingers dig into my skin.",
            "My pussy starts to feel a bit raw as his cock relentlessly thrusts in and out of me.",
            "I focus only on the man behind me pounding his cock in and out of me. I can barely focus as I am caught between liking and disliking what he is doing.",
            ]
            return self.get_entry(name_list)
        
        @property
        def having_sex_man_dirtytalk(self):
            return WeightedChoice([
            ("Ah fuck this is so nice. You are such a dirty girl!", 1),
            ("Ah yes this is so nice. You are gripping onto my cock!", 1),
            ("Ah fuck you are so warm. So nice having my cock in you.", 1),
            ("Damn you are soaked. Sexy girl, you want this more than me.", If (player.check_horny(), 1, 0)),
            ("Ah fuck, yes keep going like that. Fuck you are such a horny bitch.", If (player.check_horny(), 1, 0)),
            ("Ah fuck so nice. You know perfectly how to make a man feel good.", If (player.sex > 10 or player.sold > 10, 1, 0)),
            ("Ah fuck. You bar whores know how to give good service.", If(dis(dis_pub), 1, 0)),
            ("Damn fucking you is great, seems they teach you young girls good things in school.", If ("school" in tab_top, 1, 0)),
            ])
        
        @property
        def having_sex_switch_position(self):
            return WeightedChoice([
            ("He pulls out of me suddenly. I thought he was about to come, but it seems he has other ideas.", 1),
            ("He pulls his cock out of me, and I think he is going to wank himself off. But it seems he wants to carry on.", 1),
            ("He pulls out of me, hits me a few times with his cock then starts pulling me into a different position.", 1),
            ])
        
        
        
        
        
        @property
        def having_sex_man_close(self):
            return WeightedChoice([
            ("His grip on me starts to get stronger and a little painful as he gets more and more excited. His breathing is now getting more ragged with each thrust.", 1),
            ("His grip on my cheeks is now hard enough to leave marks on my skin as his thrusts start to become erratic. He is clearly enjoying this and may not last much longer.", 1),
            ("His hands are all over my body as he starts to put himself over the edge. His breathing becoming heavy and he starts to thrust much more aggressively into me.", 1),
            ("He grips me by the hips and thrusts into me again and again, my ass clapping against his body each time.", 1),
            ])
        
        @property
        def having_sex_pc_close_vag(self):
            return WeightedChoice([
            ("My mind starts to lose focus as I focus only on the cock thrusting in and out of me. I can feel the pleasure building up inside me.", 1),
            ("My mind goes blank as I focus only on the approaching orgasm gripping my body.", 1),
            ("My pussy starts to tighten around his cock as he brings me closer and closer to orgasm.", 1),
            ("I focus only on the man behind me pounding his nice cock in and out of me. I can barely focus as he brings my dripping pussy to orgasm.", If (player.desire > 80, 1, 0)),
            ])
        
        @property
        def having_sex_pc_close_anal(self):
            return WeightedChoice([
            ("He must be close... And so am I, despite his cock being in my ass and not my pussy.", 1),
            ("I can feel myself close to orgasm despite the fact he is fucking me in the ass and not in my vagina.", 1),
            ("My body starts to tense up as I get closer to orgasm. Unexpected as it is my ass he is fucking.", 1),
            ("My body starts to quiver as his ass fucking brings me closer and closer to orgasm.", 1),
            ])
        
        @property
        def having_sex_man_close_dialogue(self):
            name_list = (
            "Ahhh, I'm about to come!",
            "Ah fuck I am close...",
            "Fuck so good. I am not going to last much longer.",
            "Ah yes! I am cumming!",
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_pc_cum_inside_vag_want_dialogue(self):
            return WeightedChoice([
            ("Fuck! I want my first time to end with me being cummed in!", If (player.virgin_pregcheck, 100, 0)),
            ("Ahh! Cum in my virgin pussy!", If (player.virgin_pregcheck, 100, 0)),
            ("Cum inside me.", 1),
            ("You can finish inside me if you want.", 1),
            ("Keep going. Don't stop.", 1),
            ("Yes keep going. \u2665", 1),
            ("I'm close. Don't pull out! \u2665", 1),
            ("Ahh it feels so nice. Don't take it out. \u2665", 1),
            ("Keep going. Yes! Don't stop! \u2665", 1),
            ("Ah yes! \u2665", 1),
            ("I can feel you. Don't you dare pull out!", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Don't pull out. I want to feel you cum inside me! \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Keep going. Cum inside and give me what I want. \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Ahh wait. Ahh fuck yes. Stop! Keep going!", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck yes. Haa, be careful...", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
            ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_inside_vag_want_dialogue_cowgirl(self):
            return WeightedChoice([
            ("Fuck! I want my first time to end with me being cummed in!", If (player.virgin_pregcheck, 100, 0)),
            ("Ahh! Cum in my virgin pussy!", If (player.virgin_pregcheck, 100, 0)),
            ("Cum inside me.", 1),
            ("You can finish inside me if you want.", 1),
            ("Ah fuck yes! Let me feel it inside me.", 1),
            ("Yes cum inside me. \u2665", 1),
            ("I'm close. Fill me up! \u2665", 1),
            ("Ahh it feels so nice. \u2665", 1),
            ("Ah yes! \u2665", 1),
            ("I can feel you. Put it all inside me!", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Fuck, I'm going to make you cum in me! \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Cum inside and give me what I want. \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Ahh wait. Don't cum yet. Let me have my fun!", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck yes. Haa, be careful...", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
            ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_inside_ass_want_dialogue(self):
            return WeightedChoice([
            ("Ah yes. Put it all in my ass!", 1),
            ("Cum inside me.", 1),
            ("You can finish inside me if you want.", 1),
            ("Keep going. Don't stop.", 1),
            ("Yes keep going. \u2665", 1),
            ("I'm close. Don't pull out! \u2665", 1),
            ("Ahh it feels so nice. Don't take it out. \u2665", 1),
            ("Keep going. Yes! Don't stop! \u2665", 1),
            ("Ah yes! \u2665", 1),
            ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
            ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_inside_ass_want_dialogue_cowgirl(self):
            return WeightedChoice([
            ("Cum inside me.", 1),
            ("You can finish inside me if you want.", 1),
            ("Ah fuck yes! Let me feel it inside me.", 1),
            ("Yes cum inside me. \u2665", 1),
            ("I'm close. Fill me up! \u2665", 1),
            ("Ahh it feels so nice. \u2665", 1),
            ("Ah yes! \u2665", 1),
            ("I don't want to touch your shitty cock, so cum in my arse!", 1),
            ("Ah fuck unload in me like a slut!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to brand me like a slut.", If (player.isslut, 1, 0)),
            ("Keep going. I love it when men cum inside me.", If (player.isslut, 1, 0)),
            ("Ah yes! Cum in my whore ass.", If (player.selling, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_pullout_ask(self):
            return WeightedChoice([
            ("Pull out. Don't cum inside me.", 1),
            ("Take it out and cum on my ass.", 1),
            ("*Huff* Take it out and put it on my ass.", 1),
            ("Ah yes, cum on my ass. \u2665", 1),
            ("Ahh! \u2665 Not inside...", 1),
            ("Ahh take it out. Cum over me. \u2665", 1),
            ("Make sure to pull out! \u2665", 1),
            ("Ah yes! Cum over me! \u2665", 1),
            ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
            ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
            ("Don't finish inside me, I don't need to be getting knocked up again.", If (player.preg_amount, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_pullout_ask_front(self):
            return WeightedChoice([
            ("Pull out. Don't cum inside me.", 1),
            ("Take it out and cum on my belly.", 1),
            ("*Huff* Take it out and put it on my belly.", 1),
            ("Ah yes, cum all over me. \u2665", 1),
            ("Ahh! \u2665 Not inside...", 1),
            ("Ahh take it out. Cum over me. \u2665", 1),
            ("Make sure to pull out! \u2665", 1),
            ("Ah yes! Cum over me! \u2665", 1),
            ("Ahh wait. Take it out and cum somewhere else! I am not protected.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Don't finish inside me, I don't have protection.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck unload it on my tits! Cover me in your cum!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
            ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
            ("Don't finish inside me, I don't need to be getting knocked up again.", If (player.preg_amount, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_pullout_ask_cowgirl_anal(self):
            return WeightedChoice([
            ("Ah, Not inside my pussy, let me put it in my arse.", 1),
            ("Ah let me put it up my arse when you cum.", 1),
            ("*Huff* Hold on, cum in my arse.", 1),
            ("Ah fuck, I'm going to put you up my bum. \u2665", 1),
            ("Ahh! \u2665 Not inside... Do it in my ass.", 1),
            ("Ahh wait. Let me put it where I can't get knocked up.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Don't finish inside me, I don't have protection. I'll put it in my arse.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah fuck. Take it out and fuck my arse!", If (player.isslut, 1, 0)),
            ("Ah yes! Hold on and you can stick it up my bum and fill me up.", If (player.isslut, 1, 0)),
            ("Come in my ass. I love it when men fuck both my holes.", If (player.isslut, 1, 0)),
            ("Don't finish inside me, I don't need to be getting knocked up again. Assfuck me instead.", If (player.preg_amount, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_ass_pullout_ask(self):
            return WeightedChoice([
            ("Pull out. Don't cum inside me.", 1),
            ("Take it out and cum on my ass.", 1),
            ("Don't cum in my ass or I'll be leaking.", 1),
            ("*Huff* Take it out and put it on my ass.", 1),
            ("Ah yes, cum on my ass. \u2665", 1),
            ("Ahh! \u2665 Not inside...", 1),
            ("Ahh take it out. Cum over me. \u2665", 1),
            ("Ah yes! Cum over me! \u2665", 1),
            ("Ah fuck unload it on my arse! Cover me in your cum!", If (player.isslut, 1, 0)),
            ("Ah yes! Get ready to cover me like a slut.", If (player.isslut, 1, 0)),
            ("Come on my ass. I love it when men cover me with it.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_pc_cum_pullout_ask_anal_reply(self):
            return WeightedChoice([
            ("Then I'll put it somewhere else warm.", 1),
            ("If not your pussy, then...", 1),
            ("Then take it in your arse!", 1),
            ("Ah then I'm gonna fuck your arse.", 1),
            ("I paid to put it somewhere warm. Then take it in your arse.", If (player.selling, 1, 0)),
            ("Ah you shitty whore. Take it in your arse then.", If (player.selling, 1, 0)),
            ("Ah, then in your arse. Slut like you probably have enough cocks in there for it to be ready.", If (player.isslut, 1, 0)),
            ("Ah pulling out of a slut like you? Na, take it in the arse instead.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_man_cum_inside_vag_dialogue(self):
            return WeightedChoice([
            ("Ah you dirty bitch. Take it inside.", 1),
            ("Ah fuck I'm gonna put it inside you.", 1),
            ("Ah yes. Take it.", 1),
            ("Ah I am cumming!", 1),
            ("Nng fuck I am cumming.", 1),
            ("Come here and let me fill you up.", 1),
            ("Yes, yes!", 1),
            ("Ah yes! I am going to fill you up.", 1),
            ("Ah get ready for carrying my baby!", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Haaa fuck I am going to knock you up!", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Get ready for my baby you bitch.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Ahhh yes take it deep inside. Hope you're feeling lucky.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Better hope you are lucky cos I am going to fill you up!", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
            ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_man_cum_inside_ass_dialogue(self):
            return WeightedChoice([
            ("Ah fuck you dirty little butt slut.", 1),
            ("Ah yes! Take it in your arse.", 1),
            ("Ah you dirty bitch. Take it inside.", 1),
            ("Ah fuck I'm gonna put it inside you.", 1),
            ("Ah yes. Take it.", 1),
            ("Ah I am cumming!", 1),
            ("Nng fuck I am cumming.", 1),
            ("Come here and let me fill your ass up.", 1),
            ("Yes, yes!", 1),
            ("Ah yes! I am going to fill you up.", 1),
            ("You dirty slut. Take me inside you.", If (player.isslut, 1, 0)),
            ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_inside_vag_want_action(self):
            return WeightedChoice([
            ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
            ("His cock pulses inside me, unloading his cum deep inside me.", 1),
            ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
            ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
            ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
            ("I feel his cock pumping me full of cum and hope he is lucky enough to put a baby inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I feel euphoric as he tries to knock me up by pushing his cock balls deep inside me while it throbs and fill me full of his cum.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I feel like a right bitch as I hope he can knock me up while cumming inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I have mixed feelings as I feel his cock throbbing inside me, ready to try and get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("I am caught between euphoria and dread as I orgasm on a cock that is trying to put a child inside me.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
            ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_inside_vag_want_action_cowgirl(self):
            return WeightedChoice([
            ("I start to feel him cum and press my hips down on him making sure his cock is fully inside as he pumps inside me.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
            ("His cock pulses inside me, unloading his cum deep inside me.", 1),
            ("I keep riding him as I hear him groan and his cock pulses inside me, making sure everything goes inside me.", 1),
            ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
            ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
            ("I feel his cock pumping me full of cum and hope he is lucky enough to put a baby inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I feel euphoric as he tries to knock me up by pushing his cock balls deep inside me while it throbs and fill me full of his cum.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I feel like a right bitch as I hope he can knock me up while cumming inside me.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("I have mixed feelings as I feel his cock throbbing inside me, ready to try and get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("I could easily get off his cock to make sure he doesn't knock me up, but instead I keep him inside me and let him fill me with cum.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("I am caught between euphoria and dread as I orgasm on a cock that is trying to put a child inside me.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
            ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_inside_ass_want_action(self):
            return WeightedChoice([
            ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in my arse.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
            ("His cock pulses inside me, unloading his cum deep inside me.", 1),
            ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
            ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
            ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
            ("I feel his cock trobbing inside me, glad I can get filled up and not risk getting pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("I am caught in a euphoric feeling getting filled up and not risking getting knocked up.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
            ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_vag_want(self):
            return WeightedChoice([
            ("Ahhh. I can feel it throbbing in me.", 1),
            ("Mmmmm \u2665 I can feel you pumping it in!", 1),
            ("Ah yes. Fill me up.", If (not player.has_perk(perk_preg_notwant), 0, 1)),
            ("Haaaaaaaa \u2665", 1),
            ("Mmmmmmmmm \u2665", 1),
            ("Ohhh I feel it throbbing. \u2665", 1),
            ("Yes pump it in me! \u2665", If (not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ah yes! \u2665", 1),
            ("Mmmm pump it in. Make me fat.", If (player.has_perk(perk_preg_want), 1, 0)),
            ("You going to make me carry your baby round for the next few seasons? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Mmmm, are you gonna give me huge milk tits? \u2665", If (player.has_perk(perk_preg_want), 1, 0)),
            ("Mmmm I can feel it. But you better not get me pregnant.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Mmmm so nice. Even if there is some risk...", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Mmmm. I never get bored of men filling me up.", If (player.isslut, 1, 0)),
            ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
            ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_inside_vag_notwant_action(self):
            return WeightedChoice([
            ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
            ("His cock pulses inside me, unloading his cum deep inside me.", 1),
            ("I try to move away from him, but his hands grip my thighs and pulls me balls deep on his cock as I feel it throb inside me.", 1),
            ("Lost in the throes of orgasm I am too late to pull away when he starts to cum and I just let him stay there even as I feel him cumming inside me and filling me up.", 1),
            ("Caught between my own orgasm and the feeling of him cumming inside me, I fail to get him to pull out properly and he unloads everything inside me.", 1),
            ("I feel his cock pumping me full of cum and my stomach sinks as I realise that now is a dangerous time to be having a man's cum inside me.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
            ("My orgasm is cut short as I realise that right now is a terrible time of the month to let a man cum inside.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
            ("He grips my hips and pushes his cock deep inside me. I am hit by a wave of terror as I realise right now is the most fertile time of the month.", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
            ("I am caught between orgasm and trying to resist the guys attempts to cum inside but the feeling of his throbbing let's me know I didnt do a good enough job of getting off his cock.", 1),
            ("I feel the arsehole throbbing inside me and am filled with horror as I realise he could be getting me pregnant right now.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ])
        
        @property
        def having_sex_cumming_inside_ass_notwant_action(self):
            return WeightedChoice([
            ("He thrusts deep inside me and keeps his cock buried inside me, making sure he puts everything deep in me.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything inside me.", 1),
            ("His cock pulses inside me, unloading his cum deep inside me.", 1),
            ("I try to move away from him, but his hands grip my thighs and pulls me balls deep on his cock as I feel it throb inside me.", 1),
            ("Lost in the throes of orgasm I am too late to pull away when he starts to cum and I just let him stay there even as I feel him cumming inside me and filling me up.", 1),
            ("Caught between my own orgasm and the feeling of him cumming inside me, I fail to get him to pull out properly and he unloads everything inside me.", 1),
            ("I am caught between orgasm and trying to resist the guys attempts to cum inside but the feeling of his throbbing let's me know I didnt do a good enough job of getting off his cock.", 1),
            ("I feel the arsehole throbbing inside me and although I can't get pregnant in the ass, it's still annoying as I asked him to pull out.", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_vag_notwant_reaction(self):
            return WeightedChoice([
            ("What the hell? I don't want to be ending up with your shitty child in my belly.", 1),
            ("Idiot. I don't want to be carrying your baby around for the next few seasons.", 1),
            ("You do that on purpose or something? I don't want your accident in me.", 1),
            ("You trying to get me pregnant?", 1),
            ("Fuck, \"pull out\" mean nothing to you? I don't want your baby in me.", 1),
            ("It's a bad time of the month and you don't bother to pull out?", If (player.cycle_conditions["stage"] == "ovulate", 1, 0)),
            ("Fucking hell. Gonna give me another baby like this.", If (player.preg_amount, 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_ass_notwant_reaction(self):
            return WeightedChoice([
            ("I told you outside. It's gonna be leaking for the rest of my shift.", If("work" in tab_top, 1, 0)),
            ("You arse. It's going to be leaking while I work.", If("work" in tab_top, 1, 0)),
            ("Ugh, I told you outside.", 1),
            ("...", 1),
            ("Now it's going to get all sticky and leak out my arse...", 1),
            ("*Sigh* It's going to get all sticky and make it hard to walk", 1),
            ("*Sigh* Just cum where you want why don't you?", 1),
            ("Just because you are paying me, doesn't mean you can just ignore me.", If (player.selling, 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_vag_notwant_excuse(self):
            return WeightedChoice([
            ("*Huff* It was too nice being inside you to pull out.", 1),
            ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
            ("Sorry, I thought I could last longer...", 1),
            ("It felt far too nice to stop.", 1),
            ("Ah it was so good in there.", 1),
            ("Since when do whores care if they are came in?", If(player.selling, 1, 0)),
            ("Half you schoolgirls are knocked up anyway so what do you care?", If("school" in tab_top, 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_ass_notwant_excuse(self):
            return WeightedChoice([
            ("*Huff* It was too nice being inside you to pull out.", 1),
            ("Ah I didn't hear you. Was too busy enjoying that pussy of yours.", 1),
            ("Sorry, I thought I could last longer...", 1),
            ("It felt far too nice to stop.", 1),
            ("Ah it was so good in there.", 1),
            ("Not like you can get knocked up in the ass, calm down.", 1),
            ("Not gonna get pregnant from cum up your arse.", 1),
            ("Since when do whores care if they are came in?", If(player.selling, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_pullout_man_dialogue(self):
            return WeightedChoice([
            ("Ahh yes you dirty slut. Take it over you!", 1),
            ("Ah yes! Take it on your arse.", 1),
            ("Ah you dirty bitch. Take it all over you.", 1),
            ("Ah fuck I'm gonna cover you in it.", 1),
            ("Ah yes. Take it over you.", 1),
            ("Ah I am cumming!", 1),
            ("Nng fuck I am cumming.", 1),
            ("Yes, yes!", 1),
            ("Ah yes! I am going to cover you with my cum.", 1),
            ("You dirty slut. Take me over you.", If (player.isslut, 1, 0)),
            ("Ah fuck yes you filthy slut.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_cumming_pullout_action(self):
            return WeightedChoice([
            ("He pulls out and starts to come on my pussy lips and arse.", 1),
            ("He pulls out and I can feel his warm cum hitting my naked arse.", 1),
            ("He pulls his cock out and starts jerking it. I can hear him moaning as he cums all over my bum.", 1),
            ("He pulls out at the last moment and with a loud grunt, I feel him spraying his load all over my arse and pussy.", 1),
            ("He pulls his cock out of me then presses his cockhead against my arsehole. I feel it throbbing as he grunts and then a warm trickle running down my arsehole and pussy.", 1),
            ("He pulls out and furiously masturbates as he starts to groan. He sprays his load all over my ass cheeks and the back of my thighs. He then rubs his cock against my arsehole to get the last bits out.", 1),
            ("He pulls out and masturbates with one hand while gripping my arse cheek with the other. I feel him cumming over my bum and then he uses his hand to rub it all over my cheeks and between my legs.", 1),
            ("He pulls out and humps his cock between my bum cheeks. I can hear him groaning at the same time as I feel a wet warmth on my lower back. He slows as I start to feel the wetness run down to my arse and pussy.", 1),
            ])
        
        @property
        def having_sex_cumming_pullout_reaction(self):
            return WeightedChoice([
            ("Mmmmm \u2665 I can feel it on my arse.", 1),
            ("Mmm. I can feel you have put it all over me.", 1),
            ("Ah yes. Put it all on me!", 1),
            ("Ah yes. Cover me in your cum!", 1),
            ("Ahh. \u2665 Now I am even wetter than when we started.", 1),
            ("Mmmm. I hope it's true that this stuff makes a good skin cream. \u2665", 1),
            ])
        
        @property
        def having_sex_cumming_pullout_poke_action(self):
            return WeightedChoice([
            ("He pulls out and I can feel him poking me while cumming all over my pussy.", 1),
            ("He pulls out but still presses his cock against me as he cums.", 1),
            ("He pulls out as his cock pulses inside me, unloading his cum inside me and all over my lips.", 1),
            ("His cock slips out of me and I can feel his cock spraying it's load over my pussy.", 1),
            ("I feel his cock somewhat still inside me and I can feel him cumming and filling me up.", 1),
            ])
        
        @property
        def having_sex_cumming_pullout_poke_reaction(self):
            return WeightedChoice([
            ("You're too deep, pull out more!", 1),
            ("Idiot. Take it all out!", 1),
            ("*Huff* It's too deep. Take it out.", 1),
            ("Hey, pull it out more.", 1),
            ("Not so deep. Pull it out more!", 1),
            ("It's still inside. Take it out.", 1),
            ])
        
        @property
        def having_sex_cumming_pullout_poke_reaction_followup(self):
            return WeightedChoice([
            ("He finally pulls out all the way and I feel his last drops on my pussy lips and arse.", 1),
            ("He pulls out all the way and I can feel his warm cum hitting my naked arse.", 1),
            ("He pulls his cock out and starts jerking it. I can hear him moaning as he cums all over my bum.", 1),
            ("He eventually pulls out and I feel him spraying his load all over my arse and pussy.", 1),
            ("He pulls his cock out of me then presses his cockhead against my arsehole. I feel it throbbing as he grunts and then a warm trickle running down my arsehole and pussy.", 1),
            ])
        
        @property
        def having_sex_cumming_inside_ass_want_action(self):
            return WeightedChoice([
            ("He spreads my cheeks and pumps his load deep into my ass. Throb after throb unloading more into me.", 1),
            ("I can feel him gripping my hips and pulling me balls deep on his throbbing cock. Unloading everything into my ass.", 1),
            ("His cock pulses inside me, unloading his cum deep in my ass.", 1),
            ("I push back on his cock as it throbs inside me, making sure everything goes inside me.", 1),
            ("Lost in the throes of orgasm I keep bouncing on his cock even as I feel him cumming inside me and filling me up.", 1),
            ("Him cumming inside me does nothing to slow me from humping his cock to get the most pleasure from my own orgasm.", 1),
            ("The familiar feeling of a man fulling my insides full of his cum fills me with excitement.", If (player.isslut, 1, 0)),
            ("Like so many men before, I am filled with euphoria as one of them fills me with their cum.", If (player.isslut, 1, 0)),
            ])
        
        @property
        def having_sex_came_inside_ass_want(self):
            return WeightedChoice([
            ("Ahhh. I can feel it throbbing in me.", 1),
            ("Mmmmm \u2665 I can feel you pumping it in my ass!", 1),
            ("Ah yes. Fill me up.", 1),
            ("Ah yes. Pump my arse full!", 1),
            ("Haaaaaaaa \u2665", 1),
            ("Mmmmmmmmm \u2665", 1),
            ("Ohhh I feel it throbbing. \u2665", 1),
            ("Ah yes! \u2665", 1),
            ("Yes pump it in me! \u2665", If (player.has_perk(perk_preg_notwant), 1, 0)),
            ("Mmmm. I never get bored of men filling me up.", If (player.isslut, 1, 0)),
            ("Ah yes! Brand me like the slut I am.", If (player.isslut, 1, 0)),
            ("Ahhh! No matter how many guys come in me, I love it every time.", If (player.isslut, 1, 0)),
            ])
        
        
        @property
        def having_sex_cum_dialogue(self):
            name_list = (
            "Cumming!!! \u2665",
            "Uhhh fuck yes! Cumming!!!", 
            "Oh yes! YES! \u2665", 
            "I'm close! Keep goinnnnnnnn YESSSS!!!", 
            "Yes! I'm Cumming!!!", 
            "Mmmmmggg yessssss!", 
            "Yes! Yes! Oh yes! \u2665",
            "Yes, yes! \u2665",
            "Ahhhhh!",
            "Yes! Yes! Yes!",
            "Ahhhhh \u2665",
            )
            return renpy.random.choice(name_list)
        
        @property
        def having_sex_came_take_cock_out_vag(self):
            return WeightedChoice([
            ("His cock has gotten a little soft and I feel it slip out of me followed by his cum leaking out.", 1),
            ("He takes his cock out of me and I feel something warm leaking out of me.", 1),
            ("His cock slips out of me along with his cum leaking out.", 1),
            ])
        
        @property
        def having_sex_came_take_cock_out_ass(self):
            return WeightedChoice([
            ("His cock has gotten a little soft and I feel it slip out of me followed by his cum leaking out.", 1),
            ("He takes his cock out of me and I feel something warm leaking out my arse.", 1),
            ("His cock slips out of me along with his cum leaking out.", 1),
            ])
        
        
        @property
        def sex_end_man_tired(self):
            return WeightedChoice([
            ("Phew!", 1),
            ("Haa. That was nice.", 1),
            ("*Huff *Huff*.", 1),
            ])
        
        @property
        def sex_end_compliment(self):
            return WeightedChoice([
            ("Fuck that was nice.", 1),
            ("That was well worth the money. Will have to do it again sometime.", If(player.selling, 1, 0)),
            ("That's why I love this place. Such lovely little sluts working here.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("Fucking you slutty little barmaids is always the highlight of my week", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("Nothing better than coming here for some beers and ending the evening with a little slut on the end of your cock.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("Came here for some beers. But getting a little girl on the end of my cock is the best.", If(dis(dis_pub) and pub_waitress.workcycle, 1, 0)),
            ("So nice to have a schoolgirl to play around with.", If("school" in tab_top, 1, 0)),
            ("Nothing better than a schoolgirl to help you let off some steam.", If("school" in tab_top, 1, 0)),
            ("Ah you whores know how to make a man happy.", If(player.selling, 1, 0)),
            ("You dirty whores know how to please.", If(player.selling, 1, 0)),
            ])
        
        @property
        def sex_end_goodbye(self):
            return WeightedChoice([
            ("Cheers love. I'm gonna head back now." , 1),
            ("I'm going to head back to my drink now. Thanks for the fun.", If(dis(dis_pub) and pub_waitress.workcycle, 100, 0)),
            ("Cheers love. I'll let you get back to work now.", If(dis(dis_pub) and pub_waitress.workcycle,100,0)),
            ("My drink will taste a lot better now after that. Cheers love.", If(dis(dis_pub) and pub_waitress.workcycle,100,0)),
            ("Thanks love. I'd better head off now in case someone sees me with a schoolgirl.", If("school" in tab_top, 100, 0)),
            ("Cheers love, you can see yourself out.", If("loc_lorry" in loc_cur.name or "loc_flat" in loc_cur.name or loc(loc_motel_room2), 100, 0)),
            ])
        
        @property
        def sex_end_pc_goodbye(self):
            return WeightedChoice([
            ("Cheers handsome. I'll head off now." , 1),
            ("Thanks for the fun. I'll be going now." , 1),
            ("See ya round handsome." , 1),
            ])
        
        
        
        
        
        @property
        def having_sex_forced(self):
            name_list = [
            "It hurts! Please stop.",
            "*SOB*",
            "...",
            "Ah fuck. Stop please!",
            ]
            return self.get_entry(name_list)
        
        
        
        
        @property
        def pinkroom_welcome_single(self):
            return WeightedChoice([
            ("Hello darling. Come on in." , 1),
            ("Hi sweetie. Come in and I'll make you feel good.", 1),
            ("Mmm, hi cutie. Come and let's have a nice time", 1),
            ("Hi darling. Ready to have some fun?", 1),
            ("Come on in and make yourself comfortable." , 1),
            ("Relax and take a load off. I'll make you feel good.", 1),
            ])
        
        @property
        def pinkroom_welcome_group(self):
            return WeightedChoice([
            ("Hello guys. Come on in." , 1),
            ("Hi guys. Come in and I'll make you feel good.", 1),
            ("Mmm, so many strapping young men to entertain.", 1),
            ("Come on in guys. Make yourself comfortable.", 1),
            ("Come in lads. Let's have some fun." , 1),
            ("Hello lads, come in.", 1),
            ])
        
        @property
        def pinkroom_welcome_guyask_vanilla(self):
            return WeightedChoice([
            ("Hey, not after anything special and just want a bit of fun." , 1),
            ("You're cute. I'm just after a bit of fun.", 1),
            ("Hi sexy.", 1),
            ("Mmm, gonna have some fun with you.", 1),
            ("Wow, those tits are even bigger than they look from the window" , If(player.breasts == 3, 1, 0)),
            ])
        
        @property
        def pinkroom_welcome_guyask_vag(self):
            return WeightedChoice([
            ("Hey, not after anything special but just wanna fuck you in the pussy." , 1),
            ("You're cute. I'm just looking to pussy fuck you.", 1),
            ("Mmm, gonna have some fun with your wet pussy.", 1),
            ])
        
        @property
        def pinkroom_welcome_guyask_creampie(self):
            return WeightedChoice([
            ("Hey, I want to cum deep inside you." , 1),
            ("I want to cum inside you and try and knock you up.", If(not player.showing, 1, 0)),
            ("Hi fatty, I want to cum deep in your pregnant pussy.", If(player.showing, 1, 0)),
            ("Mmm, I want to leave here with your pussy leaking.", 1),
            ])
        
        @property
        def pinkroom_welcome_guyask_anal(self):
            return WeightedChoice([
            ("Hey, I wanna fuck you in the ass." , 1),
            ("You're cute. I want to have some fun with your arse.", 1),
            ("Hi sexy. Nice arse, let's have some fun with it.", 1),
            ("Mmm, gonna have some fun with your ass.", 1),
            ])
        
        
        
        
        
        @property
        def clean_area_dialogue(self):
            dialogue = []
            if renpy.showing("activity_broom") or renpy.showing("activity_sweep"):
                dialogue = dialogue + [
                "I grab the broom and start giving the floor a good sweep, making sure to collect all the junk in a bag.",
                "I pick up some of the junk, put it in a bin bag then take the broom to give the floor a sweep.",
                "I start sweeping the floor. Fortunately it isn't too bad so I don't need to get down and scrub anything.",
                "I take the broom and start my way around sweeping everything into a little pile then scoop it all up into a bin."
                ]
            elif renpy.showing("sb_table"):
                dialogue = dialogue + [
                "I take a damp rag and start washing down the tables and other surfaces.",
                "I wipe down all of the surfaces with a damp cloth, scooping all the debris into my hand and pouring it into a bin.",
                "I use a wet cloth to clean all the surfaces, making sure to give all the stubborn bits a good scrub until it's all nice and clean.",
                "I use a cloth to dust and mop all the surfaces and clear any junk from on top."
                ]
            else:
                dialogue = dialogue + [
                "I get down and start collecting all the junk and giving the floor a clear, scooping anything useless into a bag.",
                "I get on my knees to give the floor a good clean.",
                "I head around looking for all manner of junk on the floor to give it a good cleanup.",
                "I clear up all the junk and debris from the floor, making sure to put anything worthless into a bag."
                ]
            if renpy.showing("sb_table") and loc(loc_pub):
                dialogue = dialogue + [
                "I collect up all the empty glasses that are scattered all over the tables.",
                "I clear the empty glasses off the tables and wipe away all the spilled beer.",
                "I wipe away all the spilled beer, clean all the junk from the table and collect empty glasses.",
                "I gather up all the empty glasses and mop away all the spilled beer."
                ]
            return renpy.random.choice(dialogue)
        
        
        
        
        @property
        def flyering_area_dialogue(self):
            dialogue = []
            if quest_flyers.missionvar1 == "market":
                dialogue = dialogue + [
                "Old entertainment magazines sold in the market!",
                "Porn mags both new and refurbished!",
                "General good sold in the market!",
                "Books, mags, porn, ciggies! What more do you need?",
                "Books, books and more books available at the market!",
                "All the porn magazines you will ever need available at the market!",
                "Lesbian porn, gay porn, fetish porn, animal porn. All available at the market!",
                "Clothes available at the stalls. Repairs available!",
                "Sell your old books and magazines at the market for good prices!",
                ]
            elif quest_flyers.missionvar1 == "milkmaid":
                dialogue = dialogue + [
                "Fresh milk! Fresh milk!",
                "Come and get milk straight from human cows!",
                "Don't let the lack of cows stop you from enjoying fresh milk!",
                "All milk freshly milked today!",
                "Moooo! Come and buy some fresh milk!",
                "All the milk you will ever need, fresh at Milkmaids!",
                "Milk deliveries daily at Milkmaids!",
                "Moooo! Come and get your fresh milk!"
                ]
            elif quest_flyers.missionvar1 == "needle":
                dialogue = dialogue + [
                "We repair clothes good as new!",
                "Come and shop at the Needle stall!",
                "Need anything fancy? We do custom orders!",
                "Clothes for men and women!"
                ]
            elif quest_flyers.missionvar1 == "funwear":
                dialogue = dialogue + [
                "Men wont be able to resist you with clothes from Funwear!",
                "Funwear clothes! Want to catch everyones eye? Look no further!",
                "We have everything that barely qualifies as clothes at Funwear!",
                "Working the highway? Get your clothes from Funwear!",
                "Want skimpy clothes like I have? Come to Funwear!",
                "Men can't resist you dressed like this. Come to Funwear!",
                "Look like a slut with clothes from Funwear!",
                "Nothing says cheap whore like wearing clothes from Funwear!",
                ]
            elif quest_flyers.missionvar1 == "motel":
                dialogue = dialogue + [
                "Rooms for sleeping in and rooms for having fun in!",
                "Blue rooms available, rented by the night!",
                "There is no better place in the city than our pink rooms!",
                "Come and shop for girls at our pink rooms!",
                "All types of girls available at the pink rooms!",
                "Come and rent a blue room for the night. Rooms are clean and have private showers!",
                "Don't want a pink room? Rent a blue room and bring your own whores!",
                "Why rent a room when you can rent a girl and get the room for free at the motel?!"
                ]
            elif quest_flyers.missionvar1 == "pub":
                dialogue = dialogue + [
                "Cold beer and sexy waitresses!",
                "Booze all night long at the Cock and Goose!",
                "Who wants a cold beer? Come to the pub and get one free with this flyer!",
                "Beer and the best company in town! First beer free!",
                "Cold beers and warm women at the Cock and Goose!",
                "Come for the beers and stay for the entertainment at the Cock and Goose!",
                "Free beer with this flyer at the Cock and Goose!",
                "Drown your sorrows at the Cock and Goose!",
                "Feeling down? The Cock and Goose has everything you need to lave a better man!",
                "Cold beers, short dresses and sometimes no knickers at the Cock and Goose!",
                ]
            elif quest_flyers.missionvar1 == "sandy":
                dialogue = dialogue + [
                "Bikinis and sunglasses at Trinkets!",
                "Sell the junk you find on the beach at Trinkets!",
                "Cold drinks and snacks sold by Sandy!",
                "Need something to wear at the beach? Come to Trinkets for all your beach needs!",
                "Make money digging in the sand. Sell your shells at Trinkets!",
                "Want to look good on the beach? Trinkets sells all you will need!",
                "Swimsuits and bikinis at Trinkets!",
                "Practical swimsuits, modest bikinis and tiny thong bikinis, all available at Trinkets!",
                "Come to Trinkets for all your beach needs!",
                "Find anything interesting in the sand? Come sell it at Trinkets!",
                ]
            else:
                "I have no idea what I am doing, this is a bug!",
                "Handing ou flyers but I dont know what ones. This is a bug!",
            return renpy.random.choice(dialogue)
        
        
        
        
        
        @property
        def dance_party_wine_offer(self):
            return WeightedChoice([
            ("Wine, anyone want wine?" , 1),
            ("Wine. Wine anyone?", 1),
            ("Wine here.", 1),
            ("Anyone for some wine?", 1),
            ("Anyone want a refill?" , 1),
            ("Drink anyone?", 1),
            ("Anyone for a drink?", 1),
            ("Wine for anyone?", 1),
            ])
        
        @property
        def dance_party_wine_offer_accept(self):
            return WeightedChoice([
            ("Over here love." , 1),
            ("Top me up darling.", 1),
            ("Yeah over here.", 1),
            ("I'll have some.", 1),
            ("Here." , 1),
            ("Won't say no to some more.", 1),

            ])
        
        @property
        def dance_party_poledance_anabel(self):
            return WeightedChoice([
            ("Nice one blondie. Let's see some more!" , 1),
            ("Shake those tits luv!", 1),
            ("Get yet tits out darling!", If(not "topless" in anabel.list, 1, 0)),
            ("Show us that fat arse hiding under your skirt!", If(not "nude" in anabel.list, 1, 0)),
            ("Nice tits luv. Shake em for us!", If("topless" in anabel.list, 1, 0)),
            ("Bend over, let us see the goods!", If("nude" in anabel.list, 1, 0)),
            ])
        
        @property
        def dance_party_poledance_dani(self):
            return WeightedChoice([
            ("Come as sit on my lap darling!", 1),
            ("Shake those tits luv!", 1),
            ("Get yet tits out darling!", If(not "topless" in dani.list, 1, 0)),
            ("What you got under that skirt darling?!", If(not "nude" in dani.list, 1, 0)),
            ("C'mere and I'll lick those freckles off yer tits!", If("topless" in dani.list, 1, 0)),
            ("Nice hair you got down there. Give us a closer look!", If("nude" in dani.list, 1, 0)),
            ])
        
        @property
        def dance_party_poledance_rachel(self):
            return WeightedChoice([
            ("Come as sit on my lap darling!", 1),
            ("Shake those tits luv!", 1),
            ("Get yet tits out darling!", If(not "topless" in rachel.list, 1, 0)),
            ("Meet me later and I'll fatten up that skinny body of yours!", If(not rachel.showing, 1, 0)),
            ("Nice little tits you got there!", If("topless" in rachel.list, 1, 0)),
            ("Look at that, the bald bitch is ready for some fun!", If("nude" in rachel.list, 1, 0)),
            ])
        
        @property
        def dance_party_poledance_svet(self):
            return WeightedChoice([
            ("Come as sit on my lap darling!", 1),
            ("Shake those tits luv!", 1),
            ("Get yet tits out darling!", If(not "topless" in svet.list, 1, 0)),
            ("Meet me later and I'll fatten up that skinny body of yours!", If(not svet.showing, 1, 0)),
            ("Nice little tits you got there!", If("topless" in svet.list, 1, 0)),
            ("Look at that, the bald bitch is ready for some fun!", If("nude" in svet.list, 1, 0)),
            ])
        
        
        
        
        
        @property
        def dance_park_start_svet(self):
            return WeightedChoice([
            ("Okay girls. You all know what to do.", 1),
            ("Okay, let's clean up and get ready.", 1),
            ("Let's clean up so we don't trip on our asses.", 1),
            ("We have done this a bunch of time, so you all know what to do.", 1),
            ("Clean, dance, money, home.", 1),
            ])
        
        @property
        def dance_park_start(self):
            return WeightedChoice([
            ("This is something we have all done quite a lot already, so we all get together and dance a nice performance.", 1),
            ("We are used to doing shows here by now, so we all seamlessly switch between dance and collecting money.", 1),
            ("Having done this a lot, we are all confident in our show, not worrying too much about showing our asses off.", 1),
            ("Being experienced at this, we get together and show off to the crowd.", 1),
            ])
        
        @property
        def dance_park_dance_1(self):
            return WeightedChoice([
            ("Short skirts and tiny tops don't seem to matter much to anyone anymore. We dance and show off, trying to earn as much as possible.", 1),
            ("We all have next to nothing, or nothing at all, under our skirts. But this doesn't stop any of us from putting in a good performance.", 1),
            ("Barely wearing anything to cover ourselves doesn't seem to matter, we all start dancing and showing off.", 1),
            ("The guys have come to know that a bunch of barely dressed girls are coming to dance, and are not shy in hiding what they are here for.", 1),
            ])
        
        @property
        def dance_park_dance_2(self):
            return WeightedChoice([
            ("We put in every effort to make sure the guys put their hand in their pockets to put some money in our hats.", 1),
            ("Despite that, we show off and try to encourage everyone to part with their money.", 1),
            ("It's clear what we are here for, and we push every attempt to get people to get their money out.", 1),
            ("The guys know we are here to earn, and wont spend any time with people not willing to give money.", 1),
            ])
        
        @property
        def dance_park_dance_3(self):
            return WeightedChoice([
            ("We all dance and show off, at some points it almost seems like we are putting on more than just a show.", 1),
            ("We all dance and show off, much more comfortable being barely dressed and no problems showing off some skin.", 1),
            ("I look around and notice some aren't even shy about showing off anymore, and in fact seem to do it on purpose.", 1),
            ("We dance around, flaring our skirts and allowing people to get a good look. Some probably even get a look up our tiny tops.", 1),
            ("We dance around and show ourselves off. We got more money the less we dressed so no point in being shy.", 1),
            ("It is pretty clear the way we are dancing that we have little under our skirts and nothing under our tops.", 1),
            ("We show off to the crowd of watching men, not caring that they are getting a good view of what is under our dance uniform.", 1),
            ("We dance and show ourselves off. With the little clothes we are wearing, it is borderline an erotic show we are putting on.", 1),
            ])
        
        @property
        def dance_park_dance_4(self):
            return WeightedChoice([
            ("The watching crowd is pretty much drooling at our performance, and hopefully their pockets will be loosened because of it.", 1),
            ("The people watching clearly enjoy the display we are all putting on, and some are even beckoning us over with coins in their hand.", 1),
            ("The men cheer alond as we dance, particularly when a movement flares one of our skirts or ends up giving a view up our tops.", 1),
            ("The men are clapping along to our performance, clearly entertained. Hopefully this makes them loose with their money.", 1),
            ("By the sounds of it, the men are enjoying. They are hollering along with us dancing and now and then shouting the odd lewd comment.", 1),
            ("Shouts and perverted comments make it clear the men are having fun watching us, particularly when one of us bends over or does a twirl.", 1),
            ("The longer we dance, the rowdier the men get, and it's clear what is exciting them.", 1),
            ("They clap along with the music and cheer whenever one of us ends up losing control of our skirts, which considering how small they are, is quite often.", 1),
            ])
        
        
        
        
        @property
        def dani_sex_comment_breasts(self):
            return WeightedChoice([
            ("I never get tired of seeing your huge boobs naked.", If(player.breasts == 3, 1, 0)),
            ("Mmm, I love seeing what you have under your top.", 1),
            ("Lets see those tits of yours.", 1),
            ("Mmm, I wanna see your milk tits.", If(player.has_perk(perk_lactating), 1, 0)),
            ("Mmmm, huge tits and a fat belly. Love seeing them.", If(player.breasts == 3 and player.showing, 1, 0)),
            ])
        
        @property
        def dani_sex_comment_ass(self):
            return WeightedChoice([
            ("Such a nice ass.", 1),
            ("Seeing that ass, I want to bend you over just as much as all the perverts.", 1),
            ("Sexy ass and your dirty tramp stamp.", If(tattoo.ass, 1, 0)),
            ("I want to feel how wet you are.", 1),
            ("Dirty girl, Lemme see what you have down here.", 1),
            ])
        
        @property
        def dani_sex_comment_generic(self):
            return WeightedChoice([
            ("Fuck, you are so sexy.", 1),
            ("Mmm, it's so nice seeing you like this.", 1),
            ("Mmm, didn't think we would be doing this when we first met.", 1),
            ("Come here you preggo eggo.", If(player.showing, 1, 0)),
            ("Excited are we?", 1),
            ])
        
        @property
        def dani_tied_talk_nonesense(self):
            name_list = [
            "...in the park, we can go and have a nice walk. Ah but no, you will probably...",
            "...the pub, but I dont think I can let you go there, it would be...",
            "...and then I was thinking, why not? It could be okay after all...",
            "...if you were to be a good girl. But I can't trust it. You might try to...",
            "...if only you would stay put. Instead of teasing and having fun with...",
            "...no, I don't think that would be a good idea. I think you would...",
            "...might be nice. You and me... Hmmm...",
            "...but nooooo, you have to go and be all like a whore. I need to keep you safe so that...",
            ]
            return self.get_entry(name_list)
        
        
        
        
        @property
        def pub_drink_relax_action(self):
            return WeightedChoice([
            ("I sit and relax, nursing my beer, but get a fair few looks from the men.", allure_weight()),
            ("I just relax and watch what others are up to. Some drinking away while others trying to attract whores.", 100),
            ("I sit and relax, slowly sipping my beer and get the odd wave hello from guys who recognise me working here.", If(pub_waitress.timesworked > 5, 100, 0)),
            ("I relax in my seat slowly nursing my beer and watching all the people going about their business.", 100),
            ("I sit drinking my beer, avoiding looks from men who notice how I am dressed.", If(player.slutty, allure_weight(), 0)),
            ("I sit and sip at my beer, watching what " + dani.setname + " is getting up to.", If(dani_here() and not dani.hate, 100, 0)),
            ("I relax and have a drink, mostly watching " + trixie.setname + " flirting with the patrons.", 100),
            ("Feeling pretty buzzed, I try to take things a bit slower and pace myself a bit.", If(player.drunk > 70, 100 ,0)),
            ("I sit back and just watch whatever people are up to, drinking away and chatting to each other.", 100),
            ("I sip my drink and try not to spy on other people. I notice a couple of guys chatting away to what looks like a whore.", 100),
            ("It's fairly quiet in here so I enjoy the silence and relax with my drink.", If(t.hour in irange(12,17), 100 ,0)),
            ])
        
        @property
        def pub_drink_relax_thinking(self):
            return WeightedChoice([
            ("After the first beer, it stops tasting so much like piss.", If(player.drunk, 100, 0)),
            ("At least these drinks are cold.", 100),
            ("Maybe I should have dressed a bit better for drinking in the pub. People think I am a whore.", If(player.slutty and not player.iswhore, 100, 0)),
            ("I relax in my seat slowly nursing my beer and watching all the people going about their business.", 100),
            ("I sit drinking my beer, avoiding looks from men who notice how I am dressed.", If(player.slutty, allure_weight(), 0)),
            ("I swear that guy has spent most of my drink staring at my tits...", If(c.clevage and player.breasts > 1, 100, 0)),
            (trixie.setname + " working hard tonight. It's pretty busy.", If(t.hour in irange(12,17), 100, 0)),
            (dani.setname + " seems to have adapted well to working here", If(dani_here(), 100 ,0)),
            ("Ugh, so many people recognise me here, just smile and nod... I wish there was somewhere else to drink.", If(pub_waitress.timesworked > 5, 100, 0)),
            ("Dressed like this I am getting a lot of looks.", allure_weight()),
            ])
        
        @property
        def pub_drink_talk_relax(self):
            return WeightedChoice([
            ("I sit and chat with the guy who is drinking with me, and he makes it mostly clear he is interested in something.", If(player.allure > 300, 100, 0)),
            ("I kick back and relax while chatting to the guy. Although he struggles to look me in the eye most of the time and his gaze keeps lowering.", If(c.clevage and player.breasts > 1, 100, 0)),
            ("I relax and chat with the guy, but I can't help notice his gaze constantly drifts over my body.", If(player.slutty and not player.iswhore, 100, 0)),
            ("We relax, chatting back and forth while drinking our beers.", 100),
            ("We chat away, and he struggles to keep it secret that he is interested in me other than just chatting.", If(player.slutty, allure_weight(), 0)),
            ("We chat away and drink, and the more we drink the lower his gaze gets, until he is looking at my chest more than in my eyes.", If(c.clevage and player.breasts > 1, 100, 0)),
            ("We chat away and share stories while each nursing our beers.", allure_weight()),
            ])
        
        @property
        def pub_drink_talk_man(self):
            self.random_list_generator_variable = numgen(0, 11)
            return WeightedChoice([
            ("...and you would think that would be the end of it, but no.", If(self.random_list_generator_variable == 0, 1, 0)),
            ("...turned to her, talking away like usual, then stopped and asked \"where is my girlfriend?\"", If(self.random_list_generator_variable == 1, 1, 0)),
            ("...the motel and she was trying to get me down some dark alleyway. I ran like crazy.", If(self.random_list_generator_variable == 2, 1, 0)),
            ("...thought it looked suspicious. I turned around and walked the other way. Never did find out what it was.", If(self.random_list_generator_variable == 3, 1, 0)),
            ("...a dead end. So all I could do was turn around and casually walk back. Security was everywhere but didn't realise it was me.", If(self.random_list_generator_variable == 4, 1, 0)),
            ("...avoid the whole area if you can. No one that's there is there by choice.", If(self.random_list_generator_variable == 5, 1, 0)),
            ("...first day in town and it ends up like that?", If(self.random_list_generator_variable == 6, 1, 0)),
            ("...worse. I mean I did some trucking for a bit. One moment everything is okay then sudden chaos.", If(self.random_list_generator_variable == 7, 1, 0)),
            ("...and easy. Maybe the trains or something. Either way it all worked well.", If(self.random_list_generator_variable == 8, 1, 0)),
            ("...think so? I mean I suppose I could see it going that way...", If(self.random_list_generator_variable == 9, 1, 0)),
            ("...then you would think it's all good. But no, some weird guy pretending to be a dog is humping your leg.", If(self.random_list_generator_variable == 10, 1, 0)),
            ("...and only once. I was walking funny for a week or so afterwards.", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        
        @property
        def pub_drink_talk_man_reply(self):
            return WeightedChoice([
            ("So what did he do? Don't tell me he...", If(self.random_list_generator_variable == 0, 1, 0)),
            ("What? He was talking to someone else?", If(self.random_list_generator_variable == 1, 1, 0)),
            ("Ha, good. Probably a bunch of people down there waiting to rob you.", If(self.random_list_generator_variable == 2, 1, 0)),
            ("Lat time that happened to me, it was a rubbish bag blowing in the wind. Looked scary and made a weird noise...", If(self.random_list_generator_variable == 3, 1, 0)),
            ("And they jut let you walk past? Ha, what idiot would just walk through the crowd thats hunting them.", If(self.random_list_generator_variable == 4, 1, 0)),
            ("Don't need to tell me twice. Places like that are...", If(self.random_list_generator_variable == 5, 1, 0)),
            ("Yup, wrapped around a tree. Or maybe it was a lamp post. I didn't catch the name of whatever our car was hugging.", If(self.random_list_generator_variable == 6, 1, 0)),
            ("Yeah I wouldn't know. Only hear bits off of other people.", If(self.random_list_generator_variable == 7, 1, 0)),
            ("Err, yeah... What? Trains? I'm lost...", If(self.random_list_generator_variable == 8, 1, 0)),
            ("Yup, I am sure. Give it a try.", If(self.random_list_generator_variable == 9, 1, 0)),
            ("Probably not even the strangest thing that happens in the park at night...", If(self.random_list_generator_variable == 10, 1, 0)),
            ("Serves you right. Although I bet you wont forget that night.", If(self.random_list_generator_variable == 11, 1, 0)),
            ])
        
        
        
        
        @property
        def pre_game_bf_virgin(self):
            return WeightedChoice([
            ("a guy I was dating when I was a teenager. It was over in less than 10 seconds and I spent the next two weeks praying for my period.", 100),
            ("to a friend's boyfriend. I was super drunk and it was a wild night.", 100),
            ("to someone whose name I never knew. It was a wild drunken night and I spent most of it bent over.", 100),
            ("to one of my sister's friends who she had spent weeks trying to set me up with.", 100),
            ("to a guy in my class who I had a crush on for half a year.", 100),
            ("to a guy I was flirting with online and he flew out to meet me.", 100),
            ("to my long term boyfriend who was sweet and gentle.", 100),
            ("to a one night hookup and he treated my like I was meat.", 100),
            ("to a guy I met on holiday. We couldn't even speak the same language, but that made it more fun.", 100),
            ("in the toilet of a nightclub to some drunken guy.", 100),
            ("to a friends boyfriend. I was super drunk and it was a wild night.", 100),
            ("to a guy I was crushing on hard and I couldn't get my clothes off fast enough.", 100),
            ("to my sister's boyfriend who fucked me while my sister watched.", 100),
            ("to a guy I thought I would only kiss, but I was having too much fun and let it go all the way.", 100),
            ("to my boyfriend who I had been dating for a while.", 100),
            ("to a local celebrity. I thought it was cool to do it with him but I never heard from him afterwards.", 100),
            ("to my boyfriend who promised me only the tip.", 100),
            ("to a close friend who I had been experimenting with for a while.", 100),
            ("to one of my school boyfriends.", 100),
            ("to some guy I met on a dating website. I never saw him again after that.", 100),
            ("to a guy from my friend group. He later spread rumours I was a slut and I was ostracised.", 100),
            ("to some guy who treated me like an easy lay.", 100),
            ("to a guy who I was dating that made me feel really special.", 100),
            ("to a nice looking guy that was boring as a plank. I wanted him just for his looks.", 100),

            

            ("to my father who used to sneak into my bedroom at night.", 5),
            ("to my gym coach that convinced me being a virgin made me a worse player.", 5),
            ("to my boyfriend who wouldn't accept that I wanted to wait.", 5),
            ("to someone who took advantage of me while I was drunkenly puking in the toilet.", 5),
            ("to a bunch of guys who got me way too drunk.", 5),
            ("to someone who must have put something in my drink.", 5),
            ("to a guy much older than me who knew how to seduce me.", 5),
            ])
        
        @property
        def pre_game_bf_preg(self):
            return WeightedChoice([
            ("I am carrying the child of someone I was dating before the world went to shit", 100),
            ("I am carrying the child of a guy I was messing around with before the world went to shit", 100),
            ("I am carrying the child of someone I met in a bar and we didn't have condoms", 100),
            ("I am carrying the child of some guy I had a one night stand with", 100),
            ("I am carrying the child of someone I met at a fetish club", 100),
            ("I am carrying the child of some guy I had fun with in the nightclub toilet", 100),
            ("I am carrying the child of a guy who I let dom me", 100),
            ("I am carrying the child of my long term boyfriend who went missing after the chaos started", 100),
            ("I am carrying the child of a guy I had just started to date when the world went to shit", 100),
            ("I am carrying the child of a guy I was dating who promised to pull out", 100),
            ("I am carrying the child of my friend's boyfriend when we had a little too much drink together", 100),
            ("I am carrying the child of a guy whose name I can't remember", 100),
            ("I am carrying the child of a friend who ended up cumming in me during a game of truth or dare gone too far", 100),
            ("I am carrying the child of a friend who I told I would cure of his virginity", 100),
            ("I am carrying the child of a guy I leglocked just as I was cumming. Turns out so was he", 100),

            

            ("I am carrying the child of someone who must have taken advantage of me when I passed out during a house party", 5),
            ("I am carrying the child of a guy who dragged me into an alleyway on my way home from a bar", 5),
            ("I am carrying the child of a guy who must have put something in my drink", 5),
            ("I am carrying the child of friends boyfriend who pinned me down while I was visited them", 5),
            ])
        
        
        
        
        @property
        def avatar_touch_vag_comment(self):
            return WeightedChoice([
            
            ("Ha fuck. So sensitive.", If(player.check_horny(extreme=True), 1, 0)),
            ("I'm going to go crazy at this rate.", If(player.check_horny(extreme=True), 1, 0)),
            ("Mmmmmm...", If(player.check_horny(extreme=True), 1, 0)),
            ("I need something to calm me down.", If(player.check_horny(extreme=True), 1, 0)),
            ("Fuck I am so excited.", If(player.check_horny(extreme=True), 1, 0)),

            
            ("Ha, that feels nice.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("Oooh?", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("If I keep this up I might do something I'll regret.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("Oooh nice.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),

            
            (self.avatar_react_exclaim_reject, If(not player.check_horny(), 1, 0)),

            
            ("Me poking at it isn't going to make my willy grow back.", If(player.has_perk(perk_male) and not player.check_horny(), 1, 0)),
            ("Nope. Still missing my cock.", If(player.has_perk(perk_male) and not player.check_horny(), 1, 0)),
            
            
            ("Ung, it hurts down there.", If(player.recovering, 1, 0)),
            ("After what happened, it doesn't feel nice down there.", If(player.recovering, 1, 0)),
            ])
        
        @property
        def avatar_touch_breasts_comment(self):
            return WeightedChoice([
            
            (self.avatar_touch_breasts_comment_normal, If(not player.has_perk(perk_lactating), 1, 0)),

            (self.avatar_touch_breasts_comment_lactating, If(player.has_perk(perk_lactating), 1, 0)),
            ])
        
        @property
        def avatar_touch_breasts_comment_normal(self):
            return WeightedChoice([
            
            ("Ha fuck. So sensitive.", If(player.check_horny(extreme=True), 1, 0)),
            ("I'm going to go crazy at this rate.", If(player.check_horny(extreme=True), 1, 0)),
            ("Mmmmmm...", If(player.check_horny(extreme=True), 1, 0)),
            ("I need something to calm me down.", If(player.check_horny(extreme=True), 1, 0)),
            ("Fuck I am so excited.", If(player.check_horny(extreme=True), 1, 0)),

            
            ("Ha, that feels nice.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("Oooh?", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("If I keep this up I might do something I'll regret.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),
            ("Oooh nice.", If(player.check_horny() and not player.check_horny(extreme=True), 1, 0)),

            
            (self.avatar_react_exclaim_reject, If(not player.check_horny(), 1, 0)),

            
            ("Still getting used to having these.", If(player.has_perk(perk_male) and not player.check_horny(), 1, 0)),
            ("These are going to take some time to get used to.", If(player.has_perk(perk_male) and not player.check_horny(), 1, 0)),

            ])
        
        @property
        def avatar_touch_breasts_comment_lactating(self):
            return WeightedChoice([
            
            ("Ugh, I really need to milk myself. They are totally full.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] == 20, 1, 0)),
            ("They are so full they kinda hurt.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] == 20, 1, 0)),
            ("Pretty full. I should probably milk myself soon.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] > 15 and not perk_lactating.dict["milk_amount"] == 20, 1, 0)),
            ("A lot of milk, I should milk myself soon.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] > 15 and not perk_lactating.dict["milk_amount"] == 20, 1, 0)),
            ("Not much milk there.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] < 5, 1, 0)),
            ("Not really much milk, I can wait a while before milking.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] < 5, 1, 0)),
            ("A normal amount of milk. I could milk myself or just wait.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] >= 5 and not perk_lactating.dict["milk_amount"] > 15, 1, 0)),
            ("Have some milk there, but I don't need to hurry and milk myself.", If("milk_amount" in perk_lactating.dict and perk_lactating.dict["milk_amount"] >= 5 and not perk_lactating.dict["milk_amount"] > 15, 1, 0)),
            ])
        
        @property
        def avatar_touch_belly_comment(self):
            return WeightedChoice([
            (self.avatar_touch_belly_comment_fit, If(not player.preg_knows or (player.preg_knows and player.pregnancy == 0), 1, 0)),
            (self.avatar_touch_belly_comment_preg, If(player.preg_knows, 1, 0)),
            ])
        
        @property
        def avatar_touch_belly_comment_fit(self):
            return WeightedChoice([
            
            ("Mmm, I have nice abs.", If(player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("Much nicer when I work out.", If(player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("Working out suits me.", If(player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("Lot of effort to get these abs.", If(player.fitness > 60 and not player.pregnancy, 1, 0)),

            
            ("A little bit soft...", If(player.fitness < 30 and not player.pregnancy, 1, 0)),
            ("Maybe I should work out a little bit more.", If(player.fitness < 30 and not player.pregnancy, 1, 0)),
            ("Not bad, but I could do with working out a bit.", If(player.fitness < 30 and not player.pregnancy, 1, 0)),
            ("Oooh.", If(player.fitness < 30 and not player.pregnancy, 1, 0)),

            
            ("Starting to get more in shape.", If(player.fitness >= 30 and not player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("I am doing well with the fitness.", If(player.fitness >= 30 and not player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("Not too bad.", If(player.fitness >= 30 and not player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("Looking good. But could be better.", If(player.fitness >= 30 and not player.fitness > 60 and not player.pregnancy, 1, 0)),
            ("I should keep this up.", If(player.fitness >= 30 and not player.fitness > 60 and not player.pregnancy, 1, 0)),

            
            ("I really need to do something about this belly.", If(player.pregnancy, 1, 0)),
            ("People are starving and I managed to get a pot belly?", If(player.pregnancy, 1, 0)),
            ("This is a little much. I should work out or something.", If(player.pregnancy, 1, 0)),
            ("Squishy.", If(player.pregnancy, 1, 0)),

            
            ])
        
        @property
        def avatar_touch_belly_comment_preg(self):
            return WeightedChoice([
            
            ("Looks like I have a baby bump.", If(player.pregnancy == 1 and player.preg_knows, 1, 0)),
            
            ("Looks like I have a baby bump.", If(player.pregnancy == 1, 1, 0)),
            ("This is just going to keep getting bigger.", If(player.pregnancy == 1, 1, 0)),
            ("People might start to notice I have a baby bump.", If(player.pregnancy == 1, 1, 0)),
            ("Starting to get bigger.", If(player.pregnancy, 1, 0)),

            
            ("No hiding this now.", If(player.pregnancy == 2, 1, 0)),
            ("Ugh, starting to feel huge.", If(player.pregnancy == 2, 1, 0)),
            ("Pretty big.", If(player.pregnancy == 2, 1, 0)),
            ("No doubt whats in there.", If(player.pregnancy == 2, 1, 0)),

            
            ("Not long left now.", If(player.pregnancy == 3 , 1, 0)),
            ("Won't be long until I pop.", If(player.pregnancy == 3, 1, 0)),
            ("Any day now.", If(player.pregnancy == 3, 1, 0)),
            ("I feel like a truck.", If(player.pregnancy == 3, 1, 0)),

            
            ("Can't believe I let someone put this in me.", If(player.has_perk(perk_unwanted_preg), 1, 0)),
            ("I should have been more careful.", If(player.has_perk(perk_unwanted_preg), 1, 0)),
            ("Ugh, next time I will take it in the bum or something.", If(player.has_perk(perk_unwanted_preg), 1, 0)),
            ("Can't wait until I can get rid of this.", If(player.has_perk(perk_unwanted_preg), 1, 0)),
            ("Can't believe I let someone put this in me.", If(player.has_perk(perk_unwanted_preg), 1, 0)),

            
            ("Got something nice in there.", If(player.has_perk(perk_wanted_preg), 1, 0)),
            ("A nice little one is in there.", If(player.has_perk(perk_wanted_preg), 1, 0)),
            ("Someone left me a gift.", If(player.has_perk(perk_wanted_preg), 1, 0)),

            
            ("Letting someone pay me to put this in me? Ugh...", If(player.soldbaby, 1, 0)),
            ("Deal of the century paying to fuck me and making me carry his baby.", If(player.soldbaby, 1, 0)),
            ("Should have asked for more if I knew he would put this in me.", If(player.soldbaby, 1, 0)),

            
            ("Arsehole forcing this in me.", If(player.rapebaby, 1, 0)),
            ("Fucking shit putting this in me.", If(player.rapebaby, 1, 0)),

            
            ("The first of many.", If(player.has_perk(perk_broodmother) and player.preg_amount == 1, 1, 0)),
            ("Another bun in the oven.", If(player.has_perk(perk_broodmother) and player.preg_amount > 1, 1, 0)),

            
            
            ("I'm such a bitch getting bred like this.", If(player.preg_father_class == wolf, 1, 0)),
            ("I really let some doggie in the park breed me...", If(player.preg_father_class == wolf, 1, 0)),
            ("Knocked up in the gloryhole... Ugh.", If(player.preg_father_class == ghman, 1, 0)),
            ("I really let some glory hole pervet put a baby in me.", If(player.preg_father_class == ghman, 1, 0)),
            ("Getting a baby put in me while riding the bus...", If(player.preg_father_class == busgroper, 1, 0)),
            ("I just wanted to get the bus. Didn't think I would leave with a baby in me.", If(player.preg_father_class == busgroper, 1, 0)),
            ("Knocked up in that dingy motel...", If(player.preg_father_class == motelman, 1, 0)),
            ("Go to the VIP party and end up leaving with a baby in me.", If(player.preg_father_class == partyman, 1, 0)),
            ("Some VIP treatment letting them knock me up.", If(player.preg_father_class == partyman, 1, 0)),
            ("Yeah, great VIP treatment carrying their baby.", If(player.preg_father_class == partyman, 1, 0)),
            ("I really let that bitch invite a bunch of men around to knock me up.", If(player.preg_father_class == tiedman_dani, 1, 0)),
            ("Damn crazy bitch even got them to knock me up.", If(player.preg_father_class == tiedman_dani, 1, 0)),
            ("Gangbanged a baby in me...", If(player.preg_father_class == guy_gangbang, 1, 0)),
            ("Gang raped a baby in me...", If(player.preg_father_class == guy_gangbang_r, 1, 0)),
            ("As if running a train on me wasn't enough, you leave me with a baby.", If(player.preg_father_class in [guy_tiedtrain, pinkroom_tiedtrain], 1, 0)),
            ("Tied up, a train ran on me and now I have someone's baby in me.", If(player.preg_father_class in [guy_tiedtrain, pinkroom_tiedtrain], 1, 0)),
            ("Choo choo. Added an extra passenger in my belly.", If(player.preg_father_class == guy_tiedtrain, 1, 0)),
            ("If I knew he would put a baby in me, I would have demanded more tickets.", If(player.preg_father_class in [pinkroom_man, pinkroom_group], 1, 0)),
            ("Wonder how many tickets I could have got if he knew he was knocking me up?", If(player.preg_father_class in [pinkroom_man, pinkroom_group], 1, 0)),
            ("Carrying his baby just for some pink tickets.", If(player.preg_father_class in [pinkroom_man, pinkroom_group], 1, 0)),
            ("Pub didn't pay me to carry a baby.", If(player.preg_father_class == pubpatron, 1, 0)),
            ("Letting some pub drunk knock me up...", If(player.preg_father_class == pubpatron, 1, 0)),
            ("Go work in the pub, wear a tiny dress, let some guy bend me over and knock me up...", If(player.preg_father_class == pubpatron, 1, 0)),
            ("Fucked in the pub toilets and a baby put in me.", If(player.preg_father_class == pubpatron, 1, 0)),
            
            
            ("Go play football and end up preggo by the boys.", If(player.preg_father_class in [dan, drake, nate], 1, 0)),
            ("A baby in my belly isn't what I expected when I wanted to play with the boys.", If(player.preg_father_class in [dan, drake, nate], 1, 0)),
            ("Damn pervert boys. Putting a baby in me.", If(player.preg_father_class in [dan, drake, nate], 1, 0)),
            ("I only wanted to play football, not get knocked up.", If(player.preg_father_class in [dan, drake, nate], 1, 0)),

            ("Better not report on putting a baby in me.", If(player.preg_father_class == simon, 1, 0)),
            ("Private investigator. Ugh, he investigated my privates and left something behind.", If(player.preg_father_class == simon, 1, 0)),
            ("A few beers and he puts a baby in me.", If(player.preg_father_class == bob, 1, 0)),
            ("Should have taken Bob in the arse after all.", If(player.preg_father_class == bob, 1, 0)),

            ("Pervert teacher put his baby in his student.", If(player.preg_father_class == mason, 1, 0)),
            ("Naked volleyball pervert knocking me up...", If(player.preg_father_class == mason, 1, 0)),
            ("Pervert and his damn mushroom.", If(player.preg_father_class == mason, 1, 0)),

            ("Knocked up by those damn mouth breathers at the academy.", If(player.preg_father_class in [shane, marcus], 1, 0)),
            ("Damn scum of the academy putting this in me.", If(player.preg_father_class in [shane, marcus], 1, 0)),
            ("Left with a damn baby after those idiots got me gang raped.", If(player.preg_father_class == shanewhore, 1, 0)),
            ("Gangraped in the toilets and left with this.", If(player.preg_father_class == shanewhore, 1, 0)),

            ("Should charge that damn landlord rent on my belly.", If(player.preg_father_class == oskar, 1, 0)),
            ("Not sure this was worth the rent money.", If(player.preg_father_class == shanewhore, 1, 0)),
            ("Cheaper rent? Now I have his baby in me.", If(player.preg_father_class == shanewhore, 1, 0)),
            ])
        
        @property
        def hud_desire_press_comment(self):
            return WeightedChoice([
            
            (self.hud_desire_press_comment_recovering, If(player.recovering, 1, 0)),
            (self.hud_desire_press_comment_normal, If(not player.recovering, 1, 0)),

            ])
        
        @property
        def hud_desire_press_comment_recovering(self):
            return WeightedChoice([
            
            ("Ugh, after what happened...", 1),
            ("Not interested in anything like that after...", 1),
            ("It hurts down there and I have no interest in anything funny.", 1),
            ("I'm too sore to be considering something like that.", 1),
            ])
        
        @property
        def hud_desire_press_comment_normal(self):
            return WeightedChoice([
            
            ("I'm not really excited.", If(player.desire < 100, 1, 0)),
            ("Not really in the mood for anything fun like that.", If(player.desire < 100, 1, 0)),
            ("Kinda not in the mood.", If(player.desire < 100, 1, 0)),
            ("Not interested in funny stuff.", If(player.desire < 100, 1, 0)),

            
            ("Starting to feel a little hot.", If(player.desire in irange(100,200), 1, 0)),
            ("Maybe a little excited.", If(player.desire in irange(100,200), 1, 0)),
            ("Starting to feel a bit excited.", If(player.desire in irange(100,200), 1, 0)),
            ("I could be okay with a little fun.", If(player.desire in irange(100,200), 1, 0)),

            
            ("I am feeling quite excited.", If(player.desire in irange(201,400), 1, 0)),
            ("I am feeling kinda horny.", If(player.desire in irange(201,400), 1, 0)),
            ("Mmm, I am feeling kind of nice.", If(player.desire in irange(201,400), 1, 0)),
            ("I am feeling a bit...", If(player.desire in irange(201,400), 1, 0)),

            
            ("I am kinda horny and can feel it as I walk.", If(player.desire in irange(401,600), 1, 0)),
            ("I am feeling quite excited.", If(player.desire in irange(401,600), 1, 0)),
            ("I am pretty horny, I should maybe do something about it.", If(player.desire in irange(401,600), 1, 0)),
            ("I am kinda horny and my pants are pretty wet.", If(player.desire in irange(401,600) and c.pants, 1, 0)),
            ("I'm going to have to replace my underwear if this keeps up.", If(player.desire in irange(401,600) and c.pants, 1, 0)),

            
            ("I am feeling myself dripping down my leg...", If(player.desire in irange(601,1000) and not c.pants, 1, 0)),
            ("I'm going to leave a puddle on the floor at this rate.", If(player.desire in irange(601,1000), 1, 0)),
            ("I am soaking wet.", If(player.desire in irange(601,1000), 1, 0)),
            ("My knickers are soaked.", If(player.desire in irange(601,1000) and c.pants, 1, 0)),
            ])
        
        @property
        def hud_allure_press_comment(self):
            return WeightedChoice([
            
            (self.hud_allure_press_comment_nasty, If(player.allure < 100, 1, 0)),
            (self.hud_allure_press_comment_bra, If(c.cansee_bra and loc_cur.population >= 2, 1, 0)),
            (self.hud_allure_press_comment_pants, If(c.cansee_pants and loc_cur.population >= 2, 1, 0)),
            (self.hud_allure_press_comment_underwear, If(c.cansee_underwear and not c.exposed and loc_cur.population >= 2, 1, 0)),
            (self.hud_allure_press_comment_exposed, If(c.exposed or c.cansee_ass and loc_cur.population >= 2, 1, 0)),

            (self.hud_allure_press_comment_normal, If(player.allure >= 100, 1, 0)),
            ])
        @property
        def hud_allure_press_comment_normal(self):
            return WeightedChoice([
            ("Oooh", 1), 
            
            ("My ass looks nice in this.", If(c.ass, 1, 0)),
            ("Tight clothes showing off my nice ass.", If(c.ass, 1, 0)),

            
            ("Skirts always bring attention.", If(c.skirt, 1, 0)),
            ("Everyone loves looking at a tight skirt.", If(c.skirt and c.ass, 1, 0)),
            ("Tight skirt showing off my ass. Betterbe careful with no underwear though.", If(c.skirt and c.ass and not c.pants, 1, 0)),

            
            ("Nipply wearing this.", If(c.pokenips, 1, 0)),
            ("Easy to see I don't have a bra with my nipplies poking like this.", If(c.pokenips, 1, 0)),

            
            ("Happy valley.", If(c.clevage and player.breasts >= 2, 1, 0)),
            ("I have them, so might as well show them off.", If(c.clevage and player.breasts >= 2, 1, 0)),
            ("People find it hard to look me in the eye with these showing off.", If(c.clevage and player.breasts >= 2, 1, 0)),
            ("People are always sneaking looks at the girls.", If(c.clevage and player.breasts >= 2, 1, 0)),

            
            ("Showing off my belly will bring attention.", If(c.belly and not player.pregnancy, 1, 0)),
            ("I worked hard getting these abs, so I'm going to show them off.", If(c.belly and not player.pregnancy and player.fitness > 60, 1, 0)),
            ("Let everyone see I have a baby in my belly.", If(c.belly and player.pregnancy >= 2, 1, 0)),

            
            ("I look alright, but could be better.", If(player.allure in irange(100,200), 1, 0)),
            ("Not too bad looking, but could be better.", If(player.allure in irange(100,200), 1, 0)),
            ("I could look better than I currently do.", If(player.allure in irange(100,200), 1, 0)),

            ("I'm looking quite nice.", If(player.allure in irange(201,400), 1, 0)),
            ("Dressed like this, I get a fair bit of attention.", If(player.allure in irange(201,400), 1, 0)),
            ("Guys sneak some looks at me.", If(player.allure in irange(201,400), 1, 0)),
            ("Mmmm...", If(player.allure in irange(201,400), 1, 0)),

            ("Looking sexy!", If(player.allure > 400, 1, 0)),
            ("Guys pretty much break their neck trying to look at me.", If(player.allure > 400, 1, 0)),
            ("Leaving the guys drooling", If(player.allure > 400, 1, 0)),
            ("Looking damn good", If(player.allure > 400, 1, 0)),
            ])
        
        @property
        def hud_allure_press_comment_nasty(self):
            return WeightedChoice([
            
            ("I don't look nice.", 1),
            ("I really need to do something about how I look.", 1),

            
            ("I have cum on me.", If(player.cum_visible, 1, 0)),
            ("I am covered in cum.", If(player.cum_visible, 1, 0)),
            ("People are going to think I am nasry with this cum on me.", If(player.cum_visible, 1, 0)),

            
            ("I stink!", If(player.has_perk(perk_dirty), 1, 0)),
            ("I look and smell nasty.", If(player.has_perk(perk_dirty), 1, 0)),
            ("I need to shower.", If(player.has_perk(perk_dirty), 1, 0)),
            ("People probably think I am homeless with the way I smell.", If(player.has_perk(perk_dirty), 1, 0)),
            ])
        
        @property
        def hud_allure_press_comment_bra(self):
            return WeightedChoice([
            ("With no top on, of course people are looking.", 1),
            ("Only my bra on so I am getting looks.", 1),
            ])
        
        @property
        def hud_allure_press_comment_pants(self):
            return WeightedChoice([
            ("Walking around with my pants on like this is attracting attention.", 1),
            ("Walking around with just knickers is getting me some looks.", 1),
            ("Walking around with my arse out is getting me looks.", If(c.thong, 1 ,0)),
            ("Just my thong on, so of course people are looking.", If(c.thong, 1 ,0)),
            ])
        
        @property
        def hud_allure_press_comment_underwear(self):
            return WeightedChoice([
            ("Of course just wearing underwear will get me looks.", 1),
            ("Only in my underwear so I am attracting attention.", 1),
            ])
        
        @property
        def hud_allure_press_comment_exposed(self):
            return WeightedChoice([
            ("Walking around with my tits out.", If(c.cansee_breasts, 1, 0)),
            ("Showing off my tits is of course getting attention.", If(c.cansee_breasts, 1, 0)),
            ("These things are hard enough to hide even with clothes on.", If(c.cansee_breasts and player.breasts == 3, 1, 0)),
            ("I know they aren't big, but walking with them out still draws attention.", If(c.cansee_breasts and player.breasts == 1, 1, 0)),
            ("Showing my tit's off to everyone.", If(c.cansee_breasts, 1, 0)),

            ("My ass on full display.", If(c.cansee_ass, 1, 0)),
            ("Underwear doesn't hide much if it's a thong.", If(c.cansee_ass and c.thong, 1, 0)),
            ("Walking around with my ass out for everyone to see.", If(c.cansee_ass, 1, 0)),

            ("I should at least put some pants on.", If(c.cansee_vagina, 1, 0)),

            ("Everything on full display.", If(c.nude, 1, 0)),
            ("Walking around totally nude is going to draw attention.", If(c.nude, 1, 0)),
            ("Maybe I should put something on.", If(c.nude, 1, 0)),
            
            ])
        
        @property
        def hud_tired_press_comment(self):
            return WeightedChoice([
            
            (self.hud_tired_press_comment_wakeup, If(player.has_perk(perk_wakeup), 1, 0)),
            (self.hud_tired_press_comment_wakeup_comedown, If(player.has_perk(perk_wakeup_comedown), 1, 0)),
            
            (self.hud_tired_press_comment_drunk, If(player.tired < 30 and player.drunk > 50, 1, 0)),
            
            (self.hud_tired_press_comment_normal, If(not player.has_perk([perk_wakeup, perk_wakeup_comedown]), 1, 0)),

            ])
        
        @property
        def hud_tired_press_comment_wakeup(self):
            return WeightedChoice([
            
            ("Whooooo!", 1),
            ("I feel wild! This wakeup is great.", 1),
            ("On wakeup, nothing will keep be down.", 1),
            ])
        
        @property
        def hud_tired_press_comment_wakeup_comedown(self):
            return WeightedChoice([
            
            ("Ugh fuck, it's wearing off...", 1),
            ("I'm starting to crash now the wakeup is wearing off.", 1),
            ("Feels like my energy is being drained now the wakeup is wearing off.", 1),
            ])
        
        @property
        def hud_tired_press_comment_drunk(self):
            return WeightedChoice([
            
            ("Pretty tired, but the booze is keeping me on my feet.", 1),
            ("This booze is the only thing keeping me standing... For now.", 1),
            ("Drink more or go to sleep.", 1),
            ])
        
        @property
        def hud_tired_press_comment_normal(self):
            return WeightedChoice([
            
            ("I am well rested and full of energy.", If(player.tired >= 80, 1, 0)),
            ("I had a good sleep and am ready to face the world.", If(player.tired >= 80, 1, 0)),
            ("I had a good rest.", If(player.tired >= 80, 1, 0)),
            ("I've not long woke up and full of energy.", If(player.tired >= 80, 1, 0)),
            ("I'm feeling well rested.", If(player.tired >= 80, 1, 0)),

            ("I'm not really tired.", If(player.tired in irange(60,79), 1, 0)),
            ("I'm felling good.", If(player.tired in irange(60,79), 1, 0)),
            ("I slept not long ago and feeling okay.", If(player.tired in irange(60,79), 1, 0)),

            ("I can feel the day's fatigue creeping up on me.", If(player.tired in irange(40, 59), 1, 0)),
            ("Been awake for a bit and starting to feel it.", If(player.tired in irange(40, 59), 1, 0)),
            ("Not sleepy, but not full of energy either.", If(player.tired in irange(40, 59), 1, 0)),
            ("I'm feeling okay.", If(player.tired in irange(40, 59), 1, 0)),

            ("I'm kinda tired, should look to go to sleep soon.", If(player.tired in irange(20, 39), 1, 0)),
            ("Should probably look to finish what I am doing and go to bed.", If(player.tired in irange(20, 39), 1, 0)),
            ("Wont be long until I am ready to hit the hay.", If(player.tired in irange(20, 39), 1, 0)),
            ("Should be looking to get some sleep soon.", If(player.tired in irange(20, 39), 1, 0)),

            ("I feel like a zombie.", If(player.tired < 20, 1, 0)),
            ("I am about ready to pass out on my feet.", If(player.tired < 20, 1, 0)),
            ("I'm exhausted.", If(player.tired < 20, 1, 0)),
            ("I wanna go to bed.", If(player.tired < 20, 1, 0)),
            ("Sooooooo tired.", If(player.tired < 20, 1, 0)),

            ])
        
        @property
        def hud_mood_press_comment(self):
            return WeightedChoice([
            
            (self.hud_mood_press_comment_joy, If(player.has_perk(perk_joy), 1, 0)),
            (self.hud_mood_press_comment_desp, If(player.has_perk(perk_despondent), 1, 0)),
            (self.hud_mood_press_comment_normal, If(not player.has_perk([perk_joy, perk_despondent]), 1, 0)),
            ])
        
        @property
        def hud_mood_press_comment_joy(self):
            return WeightedChoice([
            ("Joy makes me feel so wonderful!", 1),
            ("The world is at my feet.", 1),
            ("Whoever invested Joy deserves a peace prize.", 1),
            ("Joy is amazing.", 1),
            ("If it wasn't so expensive, I could live my whole life on Joy.", 1),
            ])
        
        @property
        def hud_mood_press_comment_desp(self):
            return WeightedChoice([
            ("Life is shit.", 1),
            ("Please, anything to cheer me up.", 1),
            ("Fuck this place.", 1),
            ("Ugh, I feel like total shit.", 1),
            ("Anything to feel better.", 1),
            ])
        
        @property
        def hud_mood_press_comment_normal(self):
            return WeightedChoice([
            ("Life is wonderful.", If(player.mood > 80, 1, 0)),
            ("I feel great.", If(player.mood > 80, 1, 0)),
            ("Things are looking up and I feel wonderful.", If(player.mood > 80, 1, 0)),
            ("Everything is so colourful and wonderful.", If(player.mood > 80, 1, 0)),
            ("Cos I'm happy!", If(player.mood > 80, 1, 0)),
            (self.singing_dialogue_1, If(player.mood > 80, 2, 0)),
            
            ("Things are quite nice.", If(player.mood in irange(60,80), 1, 0)),
            ("I'm going quite well, all things considered.", If(player.mood in irange(60,80), 1, 0)),
            ("Not too bad.", If(player.mood in irange(60,80), 1, 0)),
            (self.singing_dialogue_1, If(player.mood in irange(60,80), 1, 0)),

            ("Could be better.", If(player.mood in irange(30, 59), 1, 0)),
            ("Doing okay I guess.", If(player.mood in irange(30, 59), 1, 0)),
            ("Doing alright. Wouldn't mind a beer or something though.", If(player.mood in irange(30, 59), 1, 0)),
            ("Meh.", If(player.mood in irange(30, 59), 1, 0)),

            ("Doing kinda shitty. I should do something fun.", If(player.mood < 30, 1, 0)),
            ("Wouldn't mind doing something to cheer me up.", If(player.mood < 30, 1, 0)),
            ("Feeling a bit blue right now...", If(player.mood < 30, 1, 0)),
            ("Maybe I can do something fun?", If(player.mood < 30, 1, 0)),
            ("Ugh, feeling kinda lame...", If(player.mood < 30, 1, 0)),
            ])
        
        @property
        def hud_conf_press_comment(self):
            return WeightedChoice([
            (self.hud_conf_press_comment_normal, If(player.confidence >= 20, 1, 0)),
            (self.hud_conf_press_comment_perks, If(player.confidence >= 20, 1, 0)),
            (self.hud_conf_press_comment_low, If(player.confidence < 20 or player.has_perk(perk_broken), 1, 0)),
            ])
        
        @property
        def hud_conf_press_comment_normal(self):
            return WeightedChoice([
            ("Life is wonderful.", If(player.confidence > 80, 1, 0)),
            ("I am amazing.", If(player.confidence > 80, 1, 0)),
            ("I am, without doubt, the absoloute best.", If(player.confidence > 80, 1, 0)),
            ("All worship my feet.", If(player.confidence > 80, 1, 0)),
            ("Worship me.", If(player.confidence > 80, 1, 0)),

            ("I am feeling pretty good about myself.", If(player.confidence in irange(41,80), 1, 0)),
            ("I don't need no man!", If(player.confidence in irange(41,80), 1, 0)),
            ("I am pretty good.", If(player.confidence in irange(41,80), 1, 0)),
            ("Things are wonderful and I feel good about myself.", If(player.confidence in irange(41,80), 1, 0)),
            ("Life is good and so am I.", If(player.confidence in irange(41,80), 1, 0)),

            ("Ehhh, I kinda feel okay... Maybe...", If(player.confidence in irange(20,40), 1, 0)),
            ("Do I feel good? Dunno.", If(player.confidence in irange(20,40), 1, 0)),
            ("I can stand up for myself... Maybe.", If(player.confidence in irange(20,40), 1, 0)),
            ("Kinda okay.", If(player.confidence in irange(20,40), 1, 0)),
            ("Could be more confident I guess.", If(player.confidence in irange(20,40), 1, 0)), 
            ])
        
        @property
        def hud_conf_press_comment_perks(self):
            return WeightedChoice([
            ("I am new to life and feeling better about things.", If(player.has_perk(perk_fresh), 1, 0)),
            ("I just woke up from my old life, I will make good on this one.", If(player.has_perk(perk_fresh), 1, 0)),

            ("I have remained pure after all this time and feeling good about it.", If(player.has_perk(perk_pure_virgin), 1, 0)),
            ("Keeping myself pure shows how good I am.", If(player.has_perk(perk_pure_virgin), 1, 0)),
            ("A virgin in this shitty world? Ha, I am awesome.", If(player.has_perk(perk_pure_virgin), 1, 0)),

            ("I got broken in and used. I feel shitty about that.", If(player.has_perk(perk_broken_virgin), 1, 0)),
            ("Fuckers finally used my body and took my virginity.", If(player.has_perk(perk_broken_virgin), 1, 0)),
            ("Lost my virginity and feel kinda shit about it.", If(player.has_perk(perk_broken_virgin), 1, 0)),

            ("Being a whore has taught me a lot about life.", If(player.has_perk(perk_whore), 1, 0)),
            ("Yes, I am a whore. No, I am not ashamed of it.", If(player.has_perk(perk_whore), 1, 0)),
            ("Need to be pretty confidence to whore about like I do.", If(player.has_perk(perk_whore), 1, 0)),

            ("Everyone love a slut like me, and it shows.", If(player.has_perk(perk_slut), 1, 0)),
            ("I'm a slut, and people love me for it.", If(player.has_perk(perk_slut), 1, 0)),
            ("Takes a lot of confidence to be a slut in this town.", If(player.has_perk(perk_slut), 1, 0)),

            ("Ha, I have to take dick to stay awake. That takes confidence.", If(player.has_perk(perk_sucu), 1, 0)),
            ("I am awesome, and anyone who disagrees... Well, I'll suck their cock.", If(player.has_perk(perk_sucu), 1, 0)),
            ("I will drain the men and feel good about it.", If(player.has_perk(perk_sucu), 1, 0)),

            ("I am free use, and love it.", If(player.has_perk(perk_freeuse), 1, 0)),
            ("I have the confidence to let any guy who want to, to fuck me senseless.", If(player.has_perk(perk_freeuse), 1, 0)),
            ("I never say no, but unlike those slave girls, I own it.", If(player.has_perk(perk_freeuse), 1, 0)),
            ("I'm so awesome I am turn down money and still live happy.", If(player.has_perk(perk_freeuse), 1, 0)),

            ("Feeling kinda shitty because of te pain between my legs.", If(player.has_perk(perk_recovering), 1, 0)),
            ("I'm still recovering from what happened, so feeling a little self conscious.", If(player.has_perk(perk_recovering), 1, 0)),

            ("No underwear and owning it.", If(player.has_perk(perk_commando) and not c.pants, 1, 0)),
            ("Totally commando under this skirt makes me feel awesome.", If(player.has_perk(perk_commando) and not c.pants and c.skirt, 1, 0)),

            ("The booze is making me feel better about myself.", If(player.has_perk([perk_drunk, perk_tipsy, perk_wasted, perk_blackout]), 1, 0)),
            ("Always feeling good while drunk.", If(player.has_perk([perk_drunk, perk_tipsy, perk_wasted, perk_blackout]), 1, 0)),

            ("Dressed like a slut makes me feel good about myself.", If(player.has_perk(perk_slutty), 1, 0)),
            ("The looks I get dressed like this makes me feel really confident.", If(player.has_perk(perk_slutty), 1, 0)),
            ("Yeah, I am awesome and look even better.", If(player.has_perk(perk_slutty), 1, 0)),

            ("Woof.", If(player.has_perk(perk_bitch), 1, 0)),

            ("Having nice make up always fills me with confidence.", If(player.has_perk(perk_makeup), 1, 0)),
            ("I have nice makeup.", If(player.has_perk(perk_makeup), 1, 0)),

            ("Like, I feel great.", If(player.has_perk(perk_bimbo), 1, 0)),

            ("Feeling very self conscious in this new body.", If(player.has_perk(perk_male), 1, 0)),
            ("This new body really makes me feel vulnerable.", If(player.has_perk(perk_male), 1, 0)),

            ])
        
        @property
        def hud_conf_press_comment_low(self):
            return WeightedChoice([
            ("Ah, scary.", If(player.confidence < 20, 1, 0)),
            ("I kinda just do what people say.", If(player.confidence < 20, 1, 0)),
            ("I... Don't really have any faith in myself.", If(player.confidence < 20, 1, 0)),
            ("People tell me what to do.", If(player.confidence < 20, 1, 0)),
            ("I just, kinda, do what I am told.", If(player.confidence < 20, 1, 0)),

            ("Doesn't matter, I'm going to do what I am told anyway.", If(player.has_perk(perk_broken), 1, 0)),
            ("They trained me too well. I just do as I am told.", If(player.has_perk(perk_broken), 1, 0)),
            ("Who cares? I just do as I am told.", If(player.has_perk(perk_broken), 1, 0)),
            ("I'm just a toy to play with anyway, so what does it matter?", If(player.has_perk(perk_broken), 1, 0)),
            ])
        
        @property
        def hud_conf_press_comment_fitness(self):
            return WeightedChoice([
            (self.avatar_touch_belly_comment, 1),

            ])
        
        @property
        def hud_int_press_comment(self):
            return WeightedChoice([
            (self.hud_int_press_comment_bimbo, If(player.has_perk([perk_bimbo, perk_princess]), 1, 0)),
            (self.hud_int_press_comment_normal, If(not player.has_perk([perk_bimbo, perk_princess]), 1, 0)),
            ])
        
        @property
        def hud_int_press_comment_bimbo(self):
            return WeightedChoice([
            ("Who cares about that kind of thing?", 1),
            ("That is just silly booksmart stuff. I don't need that.", 1),
            ("S M R T!", 1),
            ("Whatever...", 1),
            ("Yeah, like, I don't care.", 1),
            ("Nothing I need to care about.", 1),
            (self.singing_dialogue_1, If(player.mood > 80, 2, 0)), 
            ])
        
        @property
        def hud_int_press_comment_normal(self):
            return WeightedChoice([
            ("I really should pay more attention in the academy or something.", If(player.int < 20, 1, 0)),
            ("I'm not really that dumb, am I?", If(player.int < 20, 1, 0)),
            ("Errm, maybe I should... Dunno, go to a brain gym.", If(player.int < 20, 1, 0)),
            ("Should I try and read some books or something?", If(player.int < 20, 1, 0)),
            ("It's a good job I am pretty.", If(player.int < 20, 1, 0)),

            ("I am the smartest in the room usually.", If(player.int > 60, 1, 0)),
            ("I'm not just a pretty face. I also have a pretty brain.", If(player.int > 60, 1, 0)),
            ("I have been doing a good job of keeping my min sharp.", If(player.int > 60, 1, 0)),
            ("The worst part about being smart is you realise how dumb everyone else is.", If(player.int > 60, 1, 0)),
            ("Yeah I am smart, but it doesn't stop me from doing dumb shit.", If(player.int > 60, 1, 0)),

            ("Not doing too bad, I try to keep my mind sharp.", If(player.int in irange(20,60), 1, 0)),
            ("I read when I can and pay attention in the academy.", If(player.int in irange(20,60), 1, 0)),
            ("I can generally keep on top of things.", If(player.int in irange(20,60), 1, 0)),
            ("I am smart enough to get by without problems.", If(player.int in irange(20,60), 1, 0)),

            ])
        
        @property
        def hud_cycle_press_comment(self):
            return WeightedChoice([
            (self.avatar_touch_belly_comment_preg, If(player.preg_knows, 1, 0)),
            (self.hud_cycle_press_comment_late, If(player.has_perk(perk_period_late), 1, 0)),
            (self.hud_cycle_press_comment_ovulating, If(player.has_perk(perk_ovulating), 1, 0)),
            (self.hud_cycle_press_comment_normal, If(player.cycle_conditions["stage"] in ["lut", "foll"], 1, 0)),
            (self.hud_cycle_press_comment_period, If(player.has_perk(perk_period), 1, 0)),
            (self.hud_cycle_press_comment_insem, If(player.has_perk(perk_inseminated), 1, 0)),
            (self.hud_cycle_press_comment_nocycle, If(player.cycle_conditions["stage"] == "no_cycle", 1, 0)),
            ])
        
        @property
        def hud_cycle_press_comment_period(self):
            return WeightedChoice([
            ("Ugh, I hate being on my period.", 1),
            ("You think your last one just ended and then suddenly it comes again.", 1),
            ("Damn period.", 1),
            ("I feel kinda shitty since I am on my period.", 1),
            ("At least I cant get pregnant on my period.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ])
        
        @property
        def hud_cycle_press_comment_nocycle(self):
            return WeightedChoice([
            ("My cycle hasn't started again yet.", 1),
            ("I haven't started my periods again.", 1),
            ("Still waiting on my period after...", 1),
            ])
        
        @property
        def hud_cycle_press_comment_late(self):
            return WeightedChoice([
            ("I should be on my period, but it isn't coming.", 1),
            ("My period is late...", 1),
            ("Still no period...", 1),
            ("My period isn't usually this late.", 1),

            ("Period is late. Hopefully it means I am pregnant.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Still no period... Exciting.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Maybe I am pregnant.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Still waiting to know if I am pregnant.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ])
        
        @property
        def hud_cycle_press_comment_ovulating(self):
            return WeightedChoice([
            ("I am ovulating now, so dangerous time to have sex.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Dangerous time to let a man inside me.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Pretty dangerous time of the season.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Now would be a dangerous time for sex.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Risky time of the month.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),

            ("Better take it in the bum or something if it comes to that.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Now would be a terrible time to play it risky.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Better avoid men for now or I will end up with something inside me.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("No having fun at this time of the season.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Ovulating. Perfect time for anal.", If(not player.has_perk(perk_preg_notwant), 1, 0)),

            ("Perfect time to have sex.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Now is the perfect time to meet a guy and get pregnant.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("I need to find someone to put a baby in me.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Dangerous sex time, I should find someone.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ])
        
        @property
        def hud_cycle_press_comment_normal(self):
            return WeightedChoice([
            ("It should be fine at this time of the season... Should be...", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Not dangerous, but not safe either.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Shouldn't end up pregnant at this time of the season.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Should be fine, but still better to play it safe.", If(not player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),

            ("Still kind of a risky time.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("I don't want to get knocked up, so better play it safe.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Not impossible, so best take it in the bum or something.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Might not happen, but I shouldn't take the risk.", If(not player.has_perk(perk_preg_notwant), 1, 0)),
            ("Better keep my legs closed.", If(not player.has_perk(perk_preg_notwant), 1, 0)),

            ("I can still get pregnant, so no reason to say no.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("Not the best time for getting pregnant, but no harm in trying.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("I can still get pregnant, maybe I should find someone to help me.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ("It can still happen.", If(player.has_perk([perk_preg_want, perk_broodmother]), 1, 0)),
            ])
        
        @property
        def hud_cycle_press_comment_insem(self):
            return WeightedChoice([
            ("I let someone cum in me, it could be dangerous.", 1),
            ("After having risky sex, I could end up pregnant if I don't do something about it.", 1),
            ("Probably have some guy still inside me trying to knock me up.", 1),
            ("I let him finish inside me...", 1),
            ("I had risky sex.", 1),
            ])
        
        
        
        
        @property
        def avatar_comments_general_sandbox(self):
            
            
            return WeightedChoice([
            (self.singing_dialogue_1, 1), 

            
            
            
            
            
            ("A nice day today.", If(weather_var == 1 and t.timeofday == "day" and loc_cur.outside, 10, 0)),
            ("Nice to walk around in this weather.", If(weather_var == 1 and t.timeofday == "day" and loc_cur.outside, 10, 0)),
            
            ("So grey and dull today.", If(weather_var == 2 and t.timeofday == "day" and loc_cur.outside, 10, 0)),
            ("Hopefully there will be some sun tomorrow.", If(weather_var == 2 and t.timeofday == "day" and loc_cur.outside, 10, 0)),
            
            ("Ugh, pissing down outside.", If(weather_var == 3 and not loc_cur.outside, 10, 0)),
            ("Good to get out of the rain.", If(weather_var == 3 and not loc_cur.outside and loc_from.outside, 10, 0)),
            ("Glad to be dry in here. Raining so hard outside.", If(weather_var == 3 and not loc_cur.outside, 10, 0)),
            
            ("Brrr. So cold.", If(weather_var == 4 and loc_cur.outside, 10, 0)),
            ("Glad to be in the warm. So cold outside.", If(weather_var == 4 and not loc_cur.outside, 10, 0)),
            ("Good to get away from the snow.", If(weather_var == 4 and not loc_cur.outside and loc_from.outside, 10, 0)),
   
            
            ("Kinda dark. Maybe I should go home.", If(t.timeofday == "night" and player.confidence < 40 and loc_cur.outside, 20, 0)),
            ("Probably shouldn't be out at night.", If(t.timeofday == "night" and player.confidence < 40 and loc_cur.outside, 20, 0)),
            ("It's dangerous at night. Maybe I should go home.", If(t.timeofday == "night" and player.confidence < 40, 20, 0)),

            
            
            
            ("Ah, " + robin.setname + " is here.", If(robin_here() and not dis(dis_home), 100, 0)),
            ("I can see " + robin.setname + ".", If(robin_here() and not dis(dis_home), 100, 0)),

            (dani.setname + " hanging out here as usual.", If(dani_here() and loc(loc_stairwell), 100, 0)),
            ("Freezing out here and " + dani.setname + " is still hanging out.", If(dani_here() and loc(loc_stairwell) and weather_var == 4, 100, 0)),

            ("Looks like " + cass.setname + " is working tonight.", If(cass_here() and dis(dis_truckstop), 100, 0)),
            (cass.setname + " is hard at work.", If(cass_here() and dis(dis_truckstop), 100, 0)),
            ("I wonder if " + cass.setname + " manged to find out anything.", If(cass_here() and dis(dis_truckstop) and quest_mira_missing.isactive(), 100, 0)),
            (cass.setname + " working hard to find " + mira.setname, If(cass_here() and dis(dis_truckstop) and quest_mira_missing.isactive(), 100, 0)),
            
            (mira.setname + " putting her ass to work.", If(mira_here() and dis(dis_truckstop), 100, 0)),
            (mira.setname + " is here. Looks like she is working.", If(mira_here() and dis(dis_truckstop), 100, 0)),

            
            
            
            
            ("A nice walk in the park.", If(dis(dis_park) and loc_cur.outside, 100, 0)),
            ("The town might be kinda shit. But at least it's nice in the park.", If(dis(dis_park) and loc_cur.outside, 100, 0)),
            ("Nice to live so close to the park.", If(dis(dis_park) and loc_cur.outside and not loc_kitchen.locked, 100, 0)),

            
            ("Busy in here tonight as usual.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (18,19,20,21,22,23,0,1), 100, 0)),
            ("Quite the crowd as usual.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (18,19,20,21,22,23,0,1), 100, 0)),
            ("Lot's of guys in here drinking their sorrows away.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (18,19,20,21,22,23,0,1),100, 0)),

            ("People are starting to head home.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (1,2,3,4), 100, 0)),
            ("Most people are going home now.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (1,2,3,4), 100, 0)),

            ("Not very busy in here yet.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (14,15,16,17), 100, 0)),
            ("Still waiting for things to pick up.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (14,15,16,17), 100, 0)),
            ("Pretty quiet in here for now.", If(loc(loc_pub) and pub_waitress.isactive() and t.hour in (14,15,16,17), 100, 0)),
            
            ("Oh? " + robin.setname + " is here looking to get laid.", If(loc(loc_pub) and robin_here(), 100, 0)),
            ("Looks like " + robin.setname + " is here looking to drag some guy off.", If(loc(loc_pub) and robin_here(), 100, 0)),
            ("The dirty slut " + robin.setname + " is here.", If(loc(loc_pub) and robin_here(), 100, 0)),
            ("That slut!" + robin.setname + " is here looking to get fucked.", If(loc(loc_pub) and robin_here(), 100, 0)),

            ("Looks like " + dani.setname + " is working tonight.", If(loc(loc_pub) and dani_here() and not dani.hate, 100, 0)),
            (dani.setname + " is picking up a shift tonight.", If(loc(loc_pub) and dani_here() and not dani.hate, 100, 0)),
            ("I can see " + dani.setname + " over there working.", If(loc(loc_pub) and dani_here() and not dani.hate, 100, 0)),
            
            
            ("A lot of people drinking and hanging out outside the pub.", If(loc(loc_revel) and t.hour in (18,19,20,21,22,23,0,1), 100, 0)),
            ("Still pretty busy around here. Lot of drunks.", If(loc(loc_revel) and t.hour in (18,19,20,21,22,23,0,1), 100, 0)),
            ("Lot of drunks staggering home.", If(loc(loc_pub) and t.hour in (1,2,3,4), 100, 0)),
            ("Looks like people are heading home from the pub.", If(loc(loc_pub) and t.hour in (1,2,3,4), 100, 0)),
            
            
            ("Maybe I can do a bit of shopping.", If(loc(loc_market) and t.hour in workhours, 100, 0)),
            ("I wonder if I can find something nice?", If(loc(loc_market) and t.hour in workhours, 100, 0)),
            ("More clothes!", If(loc(loc_market) and t.hour in workhours, 100, 0)),
            
            ("Market is closed.", If(loc(loc_market) and not t.hour in workhours, 100, 0)),
            ("Aww, market is closed.", If(loc(loc_market) and not t.hour in workhours, 100, 0)),

            
            ("Good job I got out of here alive.", If(dis(dis_hospital), 100, 0)),

            
            ("Lot of girls with their bums out.", If(loc([loc_boardwalk, loc_beach_gym]) and t.timeofday == "day", 100, 0)),
            ("Would have liked this view when I was still a guy.", If(loc([loc_boardwalk, loc_beach_gym]) and player.has_perk(perk_male) and t.timeofday == "day", 100, 0)),
            ("Splish splash.", If(loc(loc_beach_water), 100, 0)),
            ("I wonder if these damaged boats were sunk?", If(loc(loc_beach_rocks), 100, 0)),
            ("You would think with all these damaged boats, people would stop trying to get across.", If(loc(loc_beach_rocks), 100, 0)),
            ("Maybe I should join the girls and play.", If(loc(loc_beach_gym) and t.timeofday == "day", 100, 0)),
            ("A good place to play and get some exercise.", If(loc(loc_beach_gym), 100, 0)),

            

            
            ("Whores everywhere.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and not player.iswhore, 100, 0)),
            ("Perverts everywhere looking at the whores.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and not player.iswhore, 100, 0)),
            ("So sad that these girls need to do this.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and not player.iswhore, 100, 0)),
            ("Hope I don't end up like these whores.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and not player.iswhore, 100, 0)),
            ("Motel looking as seedy as always.", If(loc(loc_motel) and not player.iswhore, 100, 0)),
            ("Shady as hell down here.", If(loc(loc_highway_slum_street) and not player.iswhore, 100, 0)),

            
            ("Lots of girls working.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and player.iswhore, 100, 0)),
            ("Lots of perverts looking for some fun.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and player.iswhore, 100, 0)),
            ("Earning a bit of cash.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and player.iswhore, 100, 0)),
            ("Bend over and get fucked. Easy money.", If(loc([loc_truckstop, loc_motel, loc_highway, loc_highway_slum]) and player.iswhore, 100, 0)),
            ("I wonder if I should work a pink room?", If(loc(loc_motel) and player.iswhore, 100, 0)),
            ("Maybe I should earn some pink tickets?", If(loc(loc_motel) and player.iswhore, 100, 0)),
            
            
            
            

            
            ("Home sweet home.", If(dis(dis_home) and not loc_from in dis_home.locs, 100, 0)),
            ("Good to be back home.", If(dis(dis_home) and not loc_from in dis_home.locs, 100, 0)),

            
            ("Living the good life...", If(loc(loc_highway_slum_home), 100, 0)),
            ("Stinks in here as usual.", If(loc(loc_highway_slum_home), 100, 0)),
            ("Got to remember to lock the door.", If(loc(loc_highway_slum_home), 100, 0)),

            ("Sounds like my neighbour has a customer.", If(loc(loc_highway_slum_home) and neighbour_here() and "sex" in neighbour.list, 100, 0)),
            ("Can hear her moaning through the shitty wall.", If(loc(loc_highway_slum_home) and neighbour_here() and "sex" in neighbour.list, 100, 0)),
            ("Neighbour sounds like she is entertaining someone.", If(loc(loc_highway_slum_home) and neighbour_here() and "sex" in neighbour.list, 100, 0)),
            
            
            ("Looks like " + jaylee.setname + " is home.", If(loc(loc_junk_trailer) and loc_from.outside and jaylee_here(), 100, 0)),
            ("Small, but at least it's safe.", If(loc(loc_junk_trailer) and loc_from.outside and loc_junk_trailer.home_location, 100, 0)),
            
            
            ("Staying in a dingy motel room...", If(loc(loc_motel_room), 100, 0)),
            ("Staying in a place surrounded by whores and customers...", If(loc(loc_motel_room), 100, 0)),

            
            
            

            
            ("I am really showing my ass off here.", If(c.cansee_ass and player.covering, 100, 0)),
            ("Everyone behind me can see my ass.", If(c.cansee_ass and player.covering, 100, 0)),
            ("Really giving everyone a view of my ass here.", If(c.cansee_ass and player.covering, 100, 0)),
            ("This skirt does nothing to hide my ass.", If(c.cansee_ass and player.covering and c.skirt, 100, 0)),

            ("Pretty much showing my gash to everyone here.", If(c.cansee_vagina and player.covering, 100, 0)),
            ("This skirt does nothing to hide the fact I am showing everything off.", If(c.cansee_vagina and player.covering and c.skirt, 100, 0)),
            ("Everyone can see me...", If(c.cansee_vagina and player.covering, 100, 0)),
            ("I need to wear something that doesn't show off between my legs.", If(c.cansee_vagina and player.covering, 100, 0)),
            
            ("Everyone can see my tits.", If(c.cansee_breasts and player.covering, 100, 0)),
            ("Showing my tits off to everyone here.", If(c.cansee_breasts and player.covering, 100, 0)),
            ("Ugh, I am pretty much showing my tits off to everyone.", If(c.cansee_breasts and player.covering, 100, 0)),
            ("My tits are pretty much on display here.", If(c.cansee_breasts and player.covering, 100, 0)),

            
            
            

            
            
            ("I really let some guy buy my first time?", If(player.has_perk(perk_cherry_sold), 100, 0)),
            ("Taking money for my first time was a bit much wasn't it?", If(player.has_perk(perk_cherry_sold), 100, 0)),
            ("Damn, I took money for my virginity.", If(player.has_perk(perk_cherry_sold), 100, 0)),
            ("First time having sex and it was as a whore.", If(player.has_perk(perk_cherry_sold), 100, 0)),
            ("Taking money to get fucked for my first time...", If(player.has_perk(perk_cherry_sold), 100, 0)),
            
            ("My first time and it was me being raped...", If(player.has_perk(perk_cherry_taken), 100, 0)),
            ("Can't believe my first time was someone raping me.", If(player.has_perk(perk_cherry_taken), 100, 0)),
            ("My first time and it was like that...", If(player.has_perk(perk_cherry_taken), 100, 0)),
            
            
            
            ("Little swimmers inside me doing work I hope.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_want), 10, 0)),
            ("Got little swimmers inside me trying to knock me up.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_want), 10, 0)),
            ("I wonder if these little swimmers inside me will do a good job.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_want), 10, 0)),
            ("Wonder if I will get pregnant.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_want), 10, 0)),
            
            ("I had better do something about getting cummed in.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_notwant), 10, 0)),
            ("I have cum in me. I need to do something so I don't get knocked up.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_notwant), 10, 0)),
            ("Hope I don't get knocked up.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_notwant), 10, 0)),
            ("I better not end up pregnant with these swimmers inside me.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_notwant), 10, 0)),
            ("Hope I dont end up pregnant.", If(player.has_perk(perk_inseminated) and player.has_perk(perk_preg_notwant), 10, 0)),
            
            ("I have swimmers inside me.", If(player.has_perk(perk_inseminated), 10, 0)),
            ("Dangerous. Might end up pregnant at this rate.", If(player.has_perk(perk_inseminated), 10, 0)),

            
            
            

            
            ("I am pretty tired.", If(player.tired < 30, 100, 0)),
            ("Kinda tired. I should sleep soon.", If(player.tired < 30, 100, 0)),
            ("Passing out on my feet here.", If(player.tired < 15, 100, 0)),
            ("Ugh, going to pass out if I keep this up.", If(player.tired < 15, 100, 0)),

            
            
            ("Fuck, I am horny as shit. I need to fuck someone.", If(player.desire > 1000, 100, 0)),
            ("If this keeps up, I'm gonna just fuck some random guy.", If(player.desire > 1000, 100, 0)),
            ("Hmmm, maybe I should just grab some guy for fun.", If(player.desire > 1000, 100, 0)),
            
            ("I want to have some fun.", If(player.desire > 600, 100, 0)),
            ("Feeling kinda horny here.", If(player.desire > 600, 100, 0)),

            
            ("Ugh, I stink.", If(player.hygiene < 20, 100, 0)),
            ("I need a shower.", If(player.hygiene < 20, 100, 0)),
            ("I need to wash up somewhere. I stink.", If(player.hygiene < 20, 100, 0)),

            
            ("I wouldn't mind something to eat right now.", If(player.hunger < 20, 40, 0)),
            ("I'm kinda hungry. I wonder if I can find somewhere to eat?", If(player.hunger < 20, 40, 0)),

            
            
            

            ("Nice to relax and have a ciggie now and then.", If(player.smoking, 100, 0)),

            ("A drink a day keeps the doctor at bay.", If(player.drinking, 100, 0)),
            ("Doesn't taste vry nice, but gets me drunk so thats good enough.", If(player.drinking, 100, 0)),
            ("Mmm, not too bad having a drink now and then.", If(player.drinking, 100, 0)),

            ("Exciting to walk around with a plug in my ass.", If(player.plugged, 100, 0)),
            ("Kind of a naughty secret going around with a buttplug inside me.", If(player.plugged, 100, 0)),

            ("I can't see a damn thing with this on.", If(player.blind, 100, 0)),
            ("I can't see anything.", If(player.blind, 100, 0)),
            ("Walking around blind is going to get me into trouble.", If(player.blind, 100, 0)),

            ("So naughty having this gag on.", If(player.gagged, 100, 0)),
            ("Ugh, I am drooling all over myself because of this gag.", If(player.gagged, 100, 0)),

            
            
            

            
            ("I have cum all over my face.", If(player.cum_locations["cum_face"], 20, 0)),
            ("People can see that I have cum on my face.", If(player.cum_locations["cum_face"] and loc_cur.population, 20, 0)),
            ("I should clean the cum from my face.", If(player.cum_locations["cum_face"], 20, 0)),
            
            ("I have cum all around my mouth.", If(player.cum_locations["cum_mouth"], 20, 0)),
            ("Ugh, I can feel the cum dripping from my chin.", If(player.cum_locations["cum_mouth"], 20, 0)),
            
            ("This top doesn't hide that I have cum over my tits.", If(player.cum_locations["cum_chest"] and c.clevage, 20, 0)),
            ("People can see the cum on my tits.", If(player.cum_locations["cum_chest"] and c.clevage and loc_cur.population, 20, 0)),
            
            ("Ugh, no knickers and I can feel the cum leaking out of me.", If(player.cum_locations["cum_vagin"] and not c.pants and c.skirt, 20, 0)),
            ("Ugh, the cum leaking out my ass is making it difficult to walk.", If(player.cum_locations["cum_assin"] and not c.pants and c.skirt, 20, 0)),
            
            
            
            

            ("So difficult to walk around with this giant belly.", If(player.pregnancy >= 2, 100, 0)),
            ("Ugh, walking like a penguin.", If(player.pregnancy >= 2, 100, 0)),
            ("Phew. Getting around is hard with a giant belly.", If(player.pregnancy >= 2, 100, 0)),

            
            
            

            ("Probably about time I milked myself.", If(player.milky, 100, 0)),
            ("I can feel pressure in my boobs. I should milk myself soon.", If(player.milky, 100, 0)),
            ("Mooooo!", If(player.milky, 100, 0)),

            
            
            

            (self.hud_cycle_press_comment_period, If(player.has_perk(perk_period), 50, 0)),
            (self.hud_allure_press_comment_normal, 20),
            (self.avatar_touch_belly_comment_preg, If(player.preg_knows, 50, 0)),
            
            
            ])
        
        @property
        def avatar_react_exclaim_negative(self):
            return WeightedChoice([
            ("Ah shit!", 1),
            ("Ah fuck!", 1),
            ("Ah!", 1),
            ("What the...!", 1),
            ("Hey!", 1),
            ])
        
        @property
        def avatar_react_exclaim_pain(self):
            return WeightedChoice([
            ("Nng! That hurts!", 1),
            ("Ow fuck!", 1),
            ("Ah shit!", 1),
            ("Oww!", 1),
            ("Nnnnngg!", 1),
            ("Ahhhhh!", 1),
            ])
        
        @property
        def avatar_react_exclaim_suprise(self):
            return WeightedChoice([
            ("Huh?", 1),
            ("What the?", 1),
            ("Ummm...", 1),
            ("Errr, what are you...", 1),
            ("Hey!", 1),
            ])
        
        @property
        def avatar_react_exclaim_accept(self):
            return WeightedChoice([
            ("Oh?", 1),
            ("Mmmmm!", 1),
            ("Haaa...", 1),
            ("Oooh!", 1),

            ])
        
        @property
        def avatar_react_exclaim_shock(self):
            return WeightedChoice([
            ("Aiieee!", 1),
            ("Ahh!", 1),
            ("Waaa?", 1),
            ("Oooh!", 1),
            ])
        
        @property
        def avatar_react_exclaim_reject(self):
            return WeightedChoice([
            ("Hey!", 1),
            ("Oi!", 1),
            ("Stop that!", 1),
            ("What are you doing?!", 1),
            ("Stop it!!", 1),
            ])
        
        
        def get_entry(self, alist):
            new_list = alist
            if self.random_list_generator_variable in new_list:
                remove_from_list(new_list, self.random_list_generator_variable)
            self.random_list_generator_variable = renpy.random.choice(new_list)
            return self.random_list_generator_variable
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
