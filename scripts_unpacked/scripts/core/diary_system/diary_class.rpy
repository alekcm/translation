init python:

    class Diary_Class(object):
        def __init__(self, name='no name', description='no description', left_pic=None, right_pic=None):
            
            self.name = name
            self.description = description 
            self.left_pic = left_pic
            self.right_pic = right_pic
            self.date = self.get_date() 
            self.day = self.get_day_added() 
            add_to_list(diary_list, self)
            
            self.set_new_entry()
        
        def get_date(self):
            return t.wkday + " " + str(t.daym) + " " + t.month 
        
        def get_day_added(self):
            return t.day
        
        def set_new_entry(self):
            global new_diary_diary_entry
            new_diary_diary_entry = True
            show_notif_popup("Diary entry " + self.name + " added")

    def diary_check_today_entry():
        
        for i in diary_list: 
            if i.day == t.day or (i.day == t.day - 1):
                return True
        return False

    def diary_check_entry(title):
        
        for i in diary_list:
            if title == i.name:
                return True
        return False


    def diary_virginity_haven_func():
        global diary_virginity
        desc = "I had hoped that it wouldn't come to this. But you don't go into a shithole like [haven] and expect to come out smelling like flowers.\n"
        if player.selling:
            desc = desc + "I agreed to give up my first time at a cost...\nDoes that make me any different to the other whores around here? Selling my body for a profit.\n"
            desc = desc + "This place is such a fucking shithole that you need some kind of pick me up to get though it..."
        elif player.beingraped:
            desc = desc + "I had at least hoped it would have been by choice...\n"
            desc = desc + "I ended up raped while on this damn mission. And by the look of this shithole it won't be the last time.\nFuck!"
        else:
            desc = desc + "I ended up agreeing to have sex today...\nIn this [haven] shithole.\n"
            if player.check_drunk(2, notif=False):
                desc = desc + "I was pretty drunk at the time but that is not a good reason."
            elif player.check_drunk(5, notif=False):
                desc = desc + "I was totally wasted when I agreed to have sex. Well, being wasted in [haven] is pretty much the norm."
            desc = desc + "Would have at least hoped it would be more romantic and not in a dumping ground for the homeless...\n"
            desc = desc + "\nFuck who am I kidding? I knew it would come to this while on the mission. I should just be glad I had the choice."
        diary_virginity = Diary_Class("Haven taking my virginity", desc) 

    def diary_virginity_func(person, quest): 
        global diary_virginity
        if quest == main_quest_05:
            diary_virginity_haven_func()
            return
        elif player.selling == True:
            desc = "Today someone offered me £ " + str(player.soldprice) + " to have sex with them "
            if player.check_poor(notif=False):
                desc = desc + "and since I pretty much had no money in my purse so I decided to accept their offer. "
            else:
                desc = desc + "and despite not being so desperate for money, I decided to take them up on their offer. "
            diary_virginity = Diary_Class("Selling my virginity", desc)
            return
        elif player.beingraped:
            desc = "It was horrible..."
            if person == busgroper:
                desc = desc + "\n\nOn the bus of all places. A shitty fucking bus! Some pervert started groping me and before I knew it he was inside me. I didn't know what to do..."
            
            elif player.check_drunk(5):
                desc = desc + "\n\nI was totally blackout drunk and somehow ended up in a shitty situation where I was raped."
            elif player.check_drunk(2):
                desc = desc + "\n\nI was a bit drunk, but there still no reason for him to do what he did. Cunt!"
            else:
                desc = desc + "\n\nNot sure what I could have done to stop it...\n\nWhat a cunt!"
            diary_virginity = Diary_Class("My virginity was stolen...", desc)
            return
        else:
            if any([person == nate, person == drake, person == dan]):
                desc = "So, I had my first time today. I mean I guess it was bound to happen while hanging out with the boys like that. Drinking beer and generally having fun. It's not like they made much secret of being attracted to me.\n\nWell, finally it happened with " + person.name.name + ". It was fun, the boys are nice so playing around with them and having my first time like that is probably the best I could have hoped for."
                diary_virginity = Diary_Class("Giving it up for the boys", desc) 
                return
            elif person == busgroper:
                desc = "So, I was kind of a dumbass today. I got on the bus with my virginity and left without it. I had heard bus rides can get like that, and I did nothing to stop it. But it's not like he forced me or anything...\n\nI dunno, I just didn't do anything to stop it. I was kind of excited and just rolled with it all."
                diary_virginity = Diary_Class("Bumping on the bus", desc) 
                return
            elif person == ghman:
                desc = "Might have been a stupid choice to make, but today I visited a glory hole and decided to have my first time with the cock sticking through the hole.\n\nIt wasn't too bad. I got to control everything this way and do it all the way I wanted. The cock sticking out of the wall was mine to do with as I wanted, so no need to care about what the guy inside me wanted or if he even had fun.\n\nIt was all about what pleased me and nothing else."
                diary_virginity = Diary_Class("My glorious hole", desc) 
                return
            else:
                desc = "I had sex today for the first time.\n"
                if person.virginname == "some random":
                    desc = "I ended up having sex with some random " + str(person.fullname)
                else:
                    desc = "I ended up having sex with " + str(person.fullname) + " for my first time"
                if player.check_drunk(2, notif=False):
                    desc = desc + " while I was pretty drunk."
                elif player.check_drunk(5, notif=False):
                    desc = desc + " while I was totally wasted."
                else:
                    desc = desc + "." 
        
        if quest:
            if quest.faction == "Institute":
                if player.beingraped:
                    desc = desc + "\n\nIt was kind of expected that this sort of thing might happen on a mission. But my first time?\nFuck..."
                else:
                    desc = desc + "\n\nDamn [tucker.sname] better be happy with how the mission went considering what I did for it."
        
        diary_virginity = Diary_Class("Losing my virginity", desc) 

    def diary_preg_first_func(): 
        global pregnant_first
        desc = ""
        if player.vvirgin:
            pregnant_first = Diary_Class("Immaculate conception", "What the fuck?!?!?\n I am pregnant!\n HOW????\n I have never had sex and still a virgin. I have no idea what is going on...")
            return
        if player.virginbaby:
            desc = desc + "Well, not being able to get pregnant your first time is a complete lie. Because I am pregnant... "
        else:
            if player.rapebaby:
                desc = desc + "FUCK! "
            elif player.has_perk(perk_preg_want):
                desc = desc + "Wow! Good news! I just found out today that I am pregnant. "
            elif player.has_perk(perk_preg_notwant):
                desc = desc + "Fuck... I am pregnant... "
            else:
                desc = desc + "I just found out today that I am pregnant. "
        
        if player.selling == True:
            if player.preg_father_class.is_unique:
                desc = desc + player.preg_father_class.setname + " got the deal of the century when he paid to have sex with me. Not only did he get to fuck me and cum inside, now I am carrying around his baby."
            else:
                desc = desc + "My \"customer\" got the deal of the century when he paid to have sex with me. Not only did he get to fuck me and cum inside, now I am carrying around his baby."
        
        elif player.rapebaby:
            if player.virginbaby:
                desc = desc + "Not only did that shit take my virginity when he raped me. He also left behind his baby. This couldn't get any worse!"
            else:
                desc = desc + "Shit, not only did that fuck force himself on me. Now I have to suffer even more by carrying his baby..."
        
        else:
            if player.preg_father_class.is_unique:
                if player.preg_father_class.vsex > 5:
                    desc = desc + "I guess it shouldn't come as a surprise though considering how often we have fooled around. So now I am pregnant with " + player.preg_father_class.setname + "'s child."
                else:
                    desc = desc + "We didn't fool around too much, but I guess it only takes one time. So now I am pregnant with " + player.preg_father_class.setname + "'s child."
            else:
                desc = desc + "I guess it shouldn't come as a surprise if I am going to have unprotected sex with strangers, then this is going to happen."
        pregnant_first = Diary_Class("Knocked up", desc)

    def diary_preg_again_func(): 
        
        desc = ""
        
        if player.rapebaby:
            desc = desc + "FUCK! "
        elif player.has_perk(perk_preg_want):
            desc = desc + "Wow! Good news! I just found out today that I am pregnant again. "
        elif player.has_perk(perk_preg_notwant):
            desc = desc + "Fuck... I am pregnant... Again... "
        else:
            desc = desc + "I just found out today that I am pregnant again. "
        
        if player.selling == True:
            if player.preg_father_class.is_unique:
                desc = desc + player.preg_father_class.setname + " got the deal of the century when he paid to have sex with me. Not only did he get to fuck me and cum inside, now I am carrying around his baby."
            else:
                desc = desc + "My \"customer\" got the deal of the century when he paid to have sex with me. Not only did he get to fuck me and cum inside, now I am carrying around his baby."
        
        elif player.rapebaby:
            desc = desc + "Shit, not only did that fuck force himself on me. Now I have to suffer even more by carrying his baby..."
        
        else:
            if player.preg_father_class.is_unique:
                if player.preg_father_class.vsex > 5:
                    desc = desc + "I guess it shouldn't come as a surprise though considering how often we have fooled around. So now I am pregnant with " + player.preg_father_class.setname + "'s child."
                else:
                    desc = desc + "We didn't fool around too much, but I guess it only takes one time. So now I am pregnant with " + player.preg_father_class.setname + "'s child."
            else:
                desc = desc + "I guess it shouldn't come as a surprise if I am going to have unprotected sex with strangers, then this is going to happen."
        
        diary_title = random(["Pregnant again", "Another bun in the oven", "Knocked up... Again", "Another baby in my belly"])
        pregnant_again = Diary_Class(diary_title, desc)

    def diary_preg_abort_func(): 
        
        
        desc = ""
        
        if player.rapebaby:
            desc = desc + "I couldn't keep it. I know it didn't do anything wrong, but that fucker forced it inside me so I had to get rid of it."
        
        
        elif player.soldbaby:
            desc = desc + "I couldn't keep it. I know it didn't do anything wrong, bringing to term a baby from someone who paid to fuck me just didn't fell right."
        elif player.has_perk(perk_preg_notwant):
            desc = desc + "I couldn't keep it. I didn't want to be pregnant in the first place and can't take any precautions these days, so I got rid of it."
        else:
            desc = desc + "I didn't want to keep it. Not like I can keep the thing anyway and it just gets handed off to who knows where. So I got rid of it."
        
        desc = desc + "\n\nFortunately I can just take a little pill and it was gone. Can't go to the hospital or anything to get it done, so hav to rely on some shady backstreet dealer. Luckily I managed to get my hands on one. Made me feel like shit after taking it and my body was all in pain. And the less that is said about what leaked out of me after the better.\n\nOh well... Hopefully I can avoid it happening again."
        
        diary_title = random(["Abortion", "No more baby", "Not pregnant any more", "I got rid of it"])
        diary_abortion = Diary_Class(diary_title, desc)

    def diary_preg_birth_func(): 
        desc = ""
        if player.has_perk(perk_unwanted_preg):
            if player.rapebaby:
                desc = desc + "I didn't get pregnant by choice, or even have sex with the father by choice, but it is out of me now. "
            elif player.soldbaby:
                desc = desc + "It wasn't part of the plan to get pregnant when I was selling myself, but I did get pregnant so here it is. "
            else:
                desc = desc + "Cant say it was planned, but I didn't do a lot to prevent it either. It got in my belly, so I brought it to term and gave it life. "
            desc = desc + "Probably should have got rid of the thing the day I found out about it. Not sure why I didn't. I let the thing grow in me all this time for some reason. Ugh."
        elif player.has_perk(perk_wanted_preg):
            if player.rapebaby:
                desc = desc + "I gave birth! Regardless of the guy raping me while putting it in me, I am happy. Or was happy I guess. Now it's gone. "
            elif player.soldbaby:
                desc = desc + "I just had a baby! And I am glad. Being paid to have sex doesn't change that I was happy to carry their child and bring it to term. "
            else:
                desc = desc + "I had a baby! I happily carried it around with me all this time, and now it's born and off to whatever life it will lead. "
            desc = desc + "I wonder if I will have another? Probably. I mean even if I didn't want to, it's not like I can protect from it these days. Hopefully I will be just as happy with my next one as I was with this one."
        
        else:
            if player.rapebaby:
                desc = desc + "I didn't agree to have a baby in me since the fucker forced himself on me. But it is what happened and I just gave birth. Maybe I should have done something about it when I found out I was pregnant. Not sure why I didn't. "
            elif player.soldbaby:
                desc = desc + "Ended up giving birth to a baby who's father was a customer. Paid to have sex but ended up carrying his child. Should I have kept it? Not really sure. "
            else:
                desc = desc + "So I had a baby finally. Carrying this around all that time wasn't an easy task. But it got inside me so that's what I did. "
            desc = desc + "No matter. It is out now and I can live life without a giant belly."
        
        desc = desc + "\n\nThe baby will now it will be handed off to whoever looks after the babies we have. Hopefully it has a good life, but I will never know."
        
        diary_title = random(["Water broke", "Giving birth", "I had the baby", "I'm a mother"])
        diary_abortion = Diary_Class(diary_title, desc)


    def diary_main_quest_01_pass_func():
        global diary_main_quest_01_pass
        desc = "Well, I got the job done and [tucker.setname] seemed pretty shocked.\n"
        if main_quest_01.vvirgin:
            if simon.rape:
                desc = desc + "Getting this mission complete ended up costing me my first time against my will, so [tucker.setname] better bloody be appreciative. It is not really something I want to repeat again."
            else:
                desc = desc + "Ended up making use of the new body they gave me and had sex for the first time to get this mission completed."
        elif main_quest_01.sex:
            desc = desc +  "He didn't seem to react much to the fact that I used sex to get the mission done. Maybe he expected it. I don't really know."
        elif simon.naughty:
            desc = desc +  "He didn't seem to react much to finding out I used my body to get the mission done. Maybe he expected it. I don't really know."
        else:
            if "intimidate_branch" in main_quest_01.list:
                desc = desc +  "[tucker.setname] didn't seem too upset when I told him I used The Institutes name to put the fear into [simon.fname]. Maybe he really means it when he says I am free to ge the job done however I see fit."
            elif "waitress_branch" in main_quest_01.list:
                desc = desc +  "Since I had already worked in the pub before, it made sense t dress up as a barmaid and try to talk the info out of him. Not sure if [tucker.name] expected some other way since I doubt he knew I had been working there."
            else:
                desc = desc +  "I did't go into much details about how I ended up with my arse hanging out after playing [simon.fname]'s game. Doubt [tucker.name] would actually care much come to think of it."
        
        desc = desc + "\nWhatever, the job was done and everyone is happy. I get paid and can see what is next."
        diary_main_quest_01_pass = Diary_Class("Reporting my first mission complete", desc)


    def diary_jobs_scavving_func():
        desc = "I was wandering around and stumbled on a giant junkyard today. While nosing about, I bumped into a girl that works there and she explained that I can earn a bit of cash digging up trash and selling on anything useful. Not entirely sure I want to be diving into piles of rubbish to earn a bit of money, but it sure beats some of the alternatives."
        if robin.love > 20:
            desc = desc + "\n\nMaybe I should mention this to Robin. She is looking to earn a bit of cash as well. Although she will probably dislike it as much as I would. Whatever pays the rent I guess."
        diary_jobs_scavving = Diary_Class("Working as a scavver", desc, right_pic = "diary_sideimage_jobs_scav")

    def diary_jobs_flyers_func(who=""):
        pic = "diary_sideimage_jobs_flyers"
        if who == "sandy":
            desc = "I was wandering around the lake area today and ended up checking out one of the kiosks "
            if sandy.showing:
                desc = desc + "and ended up chatting to this pregnant girl in a tiny bikini. "
            else:
                desc = desc + "and ended up chatting to some girl in a tiny bikini. "
            desc = desc + "Seems she runs a kiosk selling bikinis and for some reason buying up seashells. Buying shells on the beach? Seems odd... Whatever. Not important.\n\nWhat is important is she offered me a job to hand out flyers. Pay is okay I think. Although I do need to wear a bikini for her while doing the job."
            pic = "diary_sideimage_jobs_flyers_sandy"
        elif who == "market":
            desc = "I ended up at the market again today and got chatting with a girl who was there. She was handing out flyers so I asked her about it. Seems fairly simple. She pointed me in the direction of a stall who regularly hire people so hand them out. Seems easy enough.\n\nSounded like the job was fairly common as well, so it looks like I should keep my eye out for other places looking for this kind of work. Hopefully easy money."
        elif who == "motel":
            desc = "I was working today in that shitty whore motel near the highway today. Yeah yeah, the job is terrible. Need to mind my ass while working there or someone will take it. Anyway, not why I am writing this. "
            if motel_recep.showing:
                desc = desc + "The moody girl who works the counter, who looking at her belly ended up getting taken around back one too many times, "
            else:
                desc = desc + "The moody girl who works at the counter "
            desc = desc + "stopped me before finishing up work and told me I could also hand out flyers for the motel. Advertise their whores and the clean rooms. Cant be that clean if it's me cleaning them...\n\nNot important. What is, is I have more paying work. And I have seen girls handing out flyers while wandering around town. So maybe it's work I can pick up off others as well."
        diary_jobs_flyers = Diary_Class("Handing out flyers", desc, right_pic = pic)

    def diary_jobs_pub_func():
        desc = "Went into the pub today. Honestly not sure what I expected. "
        if player.male_origin:
            desc = desc + "Been to the pub plenty of times before, but of course that's when I were a guy. Wasn't too many women in the pub even back before the world went to shit. And the few that would go out would be swarmed by guys hoping to get lucky. "
        else:
            desc = desc + "Was never big into pubs before the world went to shit. Dingy places with perverted old men and your eyes watering from the amount of cigarette smoke in the air. Better to just clear a bottle of vodka at home with friends. "
        desc = desc + "\n\nI guess the place I ended up inside is fairly similar to how it used to be. The cigarette smoke is back since no one bothers with smoking bans any more. I spoke to the lady that works there, "
        if trixie.showing:
            desc = desc + "a blondie looking like she is spilling out the top of her dress and a giant baby bump to go with her upper bumps. "
        else:
            desc = desc + "a blondie looking like she is spilling out the top of her dress. "
        desc = desc + "\n\nI asked her about work and seems she needs people. No salary though and only tips. I guess that explains her dress. I suppose it's probably what I will have to wear as well."
        if player.breasts == 1:
            desc = desc + " Unlike her though, I don't have much up top to have spilling out for the customers."
        desc = desc + "\n\nI wonder if the name of the pub \"The cock and goose\" was the original name of the place. Or is the name trying to tell something?"
        diary_jobs_pub = Diary_Class("Blaston barmaid", desc, right_pic = "diary_sideimage_jobs_pub")


    def diary_people_meet_robin_func():
        if c.exposed:
            desc = "I was walking around my flat today, not entirely dressed properly since I thought I was alone. And of course this is when I bump into my flatmate. She got a bit blustered and rushed off. I guess I should probably go and have a chat with her and let her know I'm not a pervert..."
        else:
            desc = "I bumped into one of my new flatmates today. She seems nice enough. Kind of a tomboy look."
            if robin.showing:
                desc = desc + " Big fat belly though. Clearly pregnant and doesn't seem to hide it considering the clothes she is wearing doesn't hide her stomach."
            else:
                desc = desc + " I wonder if she likes to do sport and stuff, might be good to play with her or something."
            desc = desc + " Well, it looks like we will be living together for the future so I should probably go and have a chat with her and get to know her."
        
        diary_people_meet_robin = Diary_Class("My tomboy flatmate", desc, left_pic = "diary_sideimage_people_robin")





    def diary_filler_entry_func():
        
        
        if diary_check_today_entry(): 
            
            
            return
        elif not numgen(0,14) and not t.hour in irange(0,12):
            
            
            
            return
        
        elif all([loc_park.visited, loc_park_gazebo.visited, loc_park_field.visited]) and not diary_check_entry("The local neighbourhood"):
            diary_explore_park_func()
        elif loc_market.visited and not diary_check_entry("Shopping around"):
            diary_explore_market_func()
        elif loc_shop_funwear.visited and not diary_check_entry("The shop of whores"):
            diary_explore_funwear_func()
        elif all([loc_truckstop.visited, loc_highway.visited]) and not diary_check_entry("Highway whores"):
            diary_explore_highway_func()
        elif loc_checkpoint.visited and not diary_check_entry("Trapped like rats"):
            diary_explore_wall_func()
        elif jaylee.has_met and ashon.has_met and not diary_check_entry("A big pile of junk"):
            diary_explore_junk_func()
        elif loc_highway_slum_still.visited and not diary_check_entry("Booze in the slum"):
            diary_explore_slumstill_func()
        elif loc_lake.visited and loc_beach_hangout.visited and not diary_check_entry("Beach bikini bums"):
            diary_explore_lake_func()
        
        
        elif robin.love > 90 and not diary_check_entry("The terrible tomboy"):
            diary_people_robin_func()
        elif dani.love > 90 and not diary_check_entry("My courtyard buddy"):
            diary_people_dani_func()
        elif cass.iswhore and cass.sold > 10 and not diary_check_entry("Gingersnap"):
            diary_people_gingersnap_func()


    def diary_explore_park_func():
        global diary_explore_park
        desc = "I decided to look around my local area and the park near where I live. Doesn't seem that bad. It looks like I could do some exercise there to keep a little fit."
        if quest_scav.active:
            desc = desc + "\n\nI wonder if I could scav around and find anything interesting. Better be careful at night though."
        diary_explore_park = Diary_Class("The local neighbourhood", desc)

    def diary_explore_market_func():
        global diary_explore_market
        desc = "I visited that market again, the one where I went after leaving the hospital.\nIt seems nice, they have a large variety of clothes there but I have to spend ages searching all the damn stalls for something that interests me.\n\nThey also have some sellers that sell bits n bobs. Oh, and the odd bootleg booze stall."
        if quest_flyers.active:
            desc = desc + "\n\nI also spoke to one of the girls handing out flyers, I can do that I guess. Not very appealing though. "
        if hucow.has_met:
            desc = desc + "\nAh, I also met some crazy cow lady selling milk. People milk themselves these days and sell if on. Maybe I should have just stayed wrapped around the lamp post. Waking up in a world where we are the cows..."
        diary_explore_market = Diary_Class("Shopping around", desc)

    def diary_explore_funwear_func():
        global diary_explore_funwear
        desc = "I totally forgot. I went to a shop on Revel and it was... Weird.\nMost of the clothes were barely scraps of cloth. They didn't even try to pretend it was anything other than a place for the sluttiest clothes around. In fact they seemed proud of it."
        if player.iswhore:
            desc = desc + "\n\nI guess it might be a good place for me to buy my clothes. A whore shopping at a whore clothes shop."
        elif player.isslut:
            desc = desc + "\n\nMaybe I can find something interesting there :)"
        diary_explore_funwear = Diary_Class("The shop of whores", desc)

    def diary_explore_highway_func():
        global diary_explore_highway
        desc = "I ended up at the highway the other day. It was eye opening.\n\nI knew the world had gone to shit, but that whole area really hammers home how bad. The entire area had girls everywhere you look, barely dressed in anything, trying to attract customers.\nI think the worst part of it all was how casual it was. Hmm, is casual the right word? Normalised I think...\n\nThe girls were all there barely dressed and you still have normal people going about their normal day. Men and non whore women. The girls hanging around selling their body was just such an ordinary thing for most people to see that it barely got a second look."
        diary_explore_highway = Diary_Class("Highway whores", desc)

    def diary_explore_wall_func():
        global diary_explore_wall
        desc = "Headed to the edge of town to see what was going on. There is a giant wall blocking everything off. The security station has some checkpoints to let the trucks in, but other than that it's entirely walled off.\n\nCould probably climb over with a bit of help or a ladder, so not entirely sure what it is for. Blocking vehicles? Maybe it's meant to be guarded with people as well, but the lazy shits here don't care.\n\nOr maybe it's just to stop curious people like me from exploring and getting killed because we went too far out."
        diary_explore_wall = Diary_Class("Trapped like rats", desc)

    def diary_explore_junk_func():
        global diary_explore_junk
        desc = "Ended up in the junkyard at the edge of town the other day. Looks like they go outside the town and collect up whatever they can find and haul it back for people to sort.\n\nPeople like me...\n\nThe girl who works there told me I can sort through the junk and sell anything worth selling to them. Well, to her brother. Seems they both operate the junkyard. He does all the management stuff while she directs the people working there."
        diary_explore_junk = Diary_Class("A big pile of junk", desc)

    def diary_explore_slumstill_func():
        global diary_explore_slumstill
        if loc_highway_slum_home.unlocked:
            desc = "Right next to my shitty tin hut of a house in the slum, "
        else:
            desc = "Against my better judgement, I wound up in the slums the other day. "
        desc = desc + "I found some ramshackle hut type place with a shop sign. Probably lucky it wasn't a trick to lure idiots like me into the place to be murdered or something.\n\nWell I went in and wasn't murdered. The guy there sells a mountain of booze. Some in actual bottles and some in jars that look like someone pissed in it. Maybe they did...\n\nThe piss jars are cheap though and pack a punch!"
        diary_explore_slumstill = Diary_Class("Booze in the slum", desc)

    def diary_explore_lake_func():
        global diary_explore_lake
        desc = "I headed to the lake recently. Not entirely sure what I expected to be honest. It was oddly nice. Almost nice enough to make you think we were living in the old world. It was... Pretty much like it would have been like before. "
        if player.male_origin:
            desc = desc + "\n\nNot entirely sure what to make of things now I am a girl. Obviously walking around in a bikini is... Well, it makes me feel vulnerable. Even ones that cover a lot are still pretty tiny. And that's ones that cover a lot. There are ones that are barely dental floss and cover almost nothing."
        else:
            desc = desc + "\n\nI was a bit wary to wear a bikini. Nothing I haven't done before of course, but the world has changed a lot since then. But other people seemed to be wearing them so I decided to as well. And it was all just very normal."
        if "beach_vball_asked" in loc_beach_gym.list:
            desc = desc + "\n\nMet some girls playing volleyball there. They seemed nice enough. Maybe I should join them and play at some point. "
            if robin.has_met:
                desc = desc + "And I'm pretty sure Robin might enjoy playing here, assuming she isn't already. Seems her kind of thing. Although... Her in a bikini? That will be an interesting sight." 
        if lake_dealer.has_met:
            desc = desc + "\n\nOh, I also ran into some shady guy. Thought he was a pervert flashing me at first, but then realised he is selling stuff. Things that it didn't look like he would be allowed to sell. Pills to make babies go away and some stuff I think were meant to be weapons. Need a better bikini if I am going to hide something like that." 
        diary_explore_lake = Diary_Class("Beach bikini bums", desc, left_pic="diary_sideimage_activities_beachvball")



    def diary_people_robin_func():
        global diary_people_robin
        desc = "I have been getting to know my flatmate a bit more these days. I thought at first she was a typical sporty tomboy, and I suppose she still is. But getting to know her a little more I realise there is a little more of a... Hmmm, I think I had better not say.\n\n"
        if robin.isslut:
            desc = desc + "I seems she is breaking out of her shell a bit though. Or maybe just exploring a repressed side of herself? Either way, she wants to break away from her tomboy style and go full party girl. Go out there dressed in something that would make a whore blush, meet some guys and wake up the next morning walking funny.\n\nGood for her discovering a new side of herself."
        elif "pc_know_want_bussex" in robin.list:
            desc = desc + "She really is having a bit of deviant fun on the bus though. I had heard some girls use the bus for harmless fun but didn't entirely believe it. I thought the perverts on the bus were no different to rapists. But if what I am seeing is true, maybe they do this because there are plenty of girls who welcome their attention. This crazy tomboy pretty much targets the perverts and offers herself up to them like a juicy steak."
        diary_people_robin = Diary_Class("The terrible tomboy", desc)

    def diary_people_dani_func():
        global diary_people_dani
        desc = "I have been hanging out with the girl who lives across from our courtyard. She goes to the academy with me and I used to bump into her in the courtyard on the way home.\n\nLike pretty much all of us, she is having a shitty time in this new world I woke up to.\n\n"
        if "knows_dani_sex_oskar" in dani.list:
            desc = desc + "Chatting to her a bit more, I found out she is fucking the landlord for cheaper rent. Or free rent? I never did find out.\n\nAlthough I say fucking him, it sounds more like he is abusing his position. She does not seem happy in the slightest about it all and is looking for almost any alternative she can to get him off her back. Or her ass I guess.\n\n"
            if "working_pub" in dani.list:
                desc = desc + "I did set her up with a job in the pub. It should help her with a bit more cash. Unfortuantly for her, it means more people on her ass than just the landlord. Instead of one sleezy landlord fucking her, she is going to have 20 pub drunks sticking their dick in her so she can pay off the one landlord.\n\nAnd probably still end up fucking the landlord anyway...\n\n"
        if dani_yan_value() > 50:
            desc = desc + "I think I need to keep an eye on her. I have noticed some changes with her. It might be my imagination but sometimes it looks like the light behind her eyes has vanished. This glazed over look for a bit. And I swear those cuts... Are they...? Ugh...\n\n"
        if quest_daniwine.active:
            desc = desc + "She did invite me for some wine round her place. Well, I say invite. I have to bring the wine since she can't even afford... Well, yeah... Anyway, getting her piss drunk might help her forget we live inthis world for a moment."
        diary_people_dani = Diary_Class("My courtyard buddy", desc)

    def diary_people_gingersnap_func():
        global diary_people_gingersnap
        desc = "So, I guess she is a whore now... Not much of a choice I guess. Well, there would have been a choice, but then her friend would die."
        if "kidnapped" in mira.list and not "rescued" in mira.list:
            desc = desc + "\n\nI guess she may still die. Not managed to find her yet. But at least this way she might be able to find her still. I hope so anyway."
        else:
            desc = desc + "\n\nAnd I guess it's probably what saved her life in the end. Going out there and doing this kind of job to find out about her friend is a pretty big step."
        desc = desc + "\n\nBut at the end of the day, I helped someone become a whore. Took her to the highway and helped her get fucked by some pervert for money. While there was a very good reason for it, it's still something that will ear your soul."
        diary_people_gingersnap = Diary_Class("Gingersnap", desc, right_pic="diary_sideimage_people_gingersnap")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
