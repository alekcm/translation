label school_field_soccer_hangout:
    $ walk(loc_school_field_back)
    if not school_soccer_hangingout():
        jump travel








    if not "soccer_hangout_conv" in mira.dict:
        $ mira.dict["soccer_hangout_conv"] = 0


    if not "rachel_nude" in rachel.dict:
        $ rachel.dict["rachel_nude"] = 0
    if not "free_use_topic" in loc_school_field_back.dict:
        $ loc_school_field_back.dict["free_use_topic"] = 0


    if not loc_cur == loc_school_field_back:
        pc "Hey guys."
    if player.has_perk(perk_exhibitionist) and not "exhibitionist_asked" in school_soccer_quest.conversation_topics and (sum([drake.love, nate.love, dan.love]) > 70 or all([drake.naked, nate.naked, dan.naked])) and t.timeofday == "night":
        jump school_field_soccer_hangout_conv_exhibitionist
    if "exhibitionist_asked" in school_soccer_quest.conversation_topics and not c.nude and t.timeofday == "night":
        $ pc_striptease(True)
        $ pc_set_temp_outfit()
        if robin_here() and not "soccer_exhibition_seen" in robin.list:
            $ add_to_list(robin.list, "soccer_exhibition_seen")
            robin.name "Here as well? In front of the boys?"
            pc "I asked and they don't mind."
            robin.name "Of course they don't..."

    if "has_photos" in school_soccer_quest.conversation_topics and not "has_photos_know" in school_soccer_quest.conversation_topics and not nate.last_spoke_to == t.day:
        jump school_field_soccer_hangout_conv_photos

    if school_soccer_dare_should_undress():
        nate.name "Aren't you a bit overdressed [name]?"
        pc "Ugh."
        if school_soccer_dare_should_undress() == "nude":
            $ pc_striptease(temp=True)
        elif school_soccer_dare_should_undress() == "topless":
            $ pc_strip_upper(slow=True, temp=True)
        elif school_soccer_dare_should_undress() == "under":
            $ pc_strip_tops(slow=True, temp=True)
        pc "Happy?"
        nate.name "Yup."


    if school_soccer_love_check(35) and not school_soccer_quest_backentrance["shown"] and not loc_school_secret_entrance.visited:
        jump school_field_soccer_hangout_backentrance_show
    elif school_soccer_quest_backentrance["used"] and not school_soccer_quest_backentrance["talk"] and not school_open_hours():
        jump school_field_soccer_hangout_backentrance_used
    elif school_soccer_quest_hangout_conv == 1:
        jump school_field_soccer_hangout_conv_1

    elif robin_here() and rachel_here() and "soccerboys_can_sex" in robin.list and renpy.has_label("school_field_soccer_hangout_conv_freeuse_" + str(loc_school_field_back.dict["free_use_topic"])):
        jump expression "school_field_soccer_hangout_conv_freeuse_" + str(loc_school_field_back.dict["free_use_topic"])


    elif school_soccer_isfather() and player.preg_knows and not "told_pregnant" in player.preg_father_class.conversation_topics and player.preg_father_class.preg <= 1:
        jump school_field_soccer_hangout_conv_preg_boysintro
    elif not school_soccer_isfather() and player.pregnancy >= 2 and not "preg1" in school_soccer_quest.list and player.preg_amount == 0:
        jump school_field_soccer_hangout_conv_preg1_notboys
    elif not school_soccer_isfather() and player.pregnancy >= 2 and not "preg2" in school_soccer_quest.list and player.preg_amount > 1:
        jump school_field_soccer_hangout_conv_preg2_notboys


    elif school_bully_quest_bully_event_stage >= 6 and not school_soccer_quest_bully_remove["asked1"] and school_soccer_love_check(50) and not (school_bully_quest_bully_soccer_boys_remove or school_bully_quest_bully_cass_target) and not shane.dead:
        jump school_field_soccer_hangout_bully_ask_remove1
    elif school_bully_quest_bully_event_stage >= 6 and not school_soccer_quest_bully_remove["asked2"] and school_soccer_love_check(70) and not (school_bully_quest_bully_soccer_boys_remove or school_bully_quest_bully_cass_target) and not shane.dead:
        jump school_field_soccer_hangout_bully_ask_remove2
    elif school_bully_quest_bully_event_stage >= 6 and school_soccer_quest_bully_remove["asked2"] and school_soccer_love_check(100) and not (school_bully_quest_bully_soccer_boys_remove or school_bully_quest_bully_cass_target) and not shane.dead:
        jump school_field_soccer_hangout_bully_ask_remove3
    elif school_soccer_quest_bully_remove["vanished"] and t.day > school_soccer_quest_bully_remove["vanished_date"] + 3 and not school_soccer_quest_bully_remove["vanished_return"] and school_soccer_quest_bully_remove["vanished_field"]:
        jump school_field_soccer_hangout_bully_ask_remove_return


    elif not school_soccer_quest_boys_know["sis_home"] and main_quest_05.active == 2 and school_soccer_quest_hangout_conv > 5:
        jump school_field_soccer_hangout_sis_home
    elif not school_soccer_quest_boys_know["pub_work"] and pub_waitress.timesworked > 5 and school_soccer_quest_hangout_conv >= 8:
        jump school_field_soccer_hangout_pubwork


    elif t.day in weekend and school_soccer_quest_talk_topics["weekend"]:
        jump school_field_soccer_hangout_conv_weekend
    elif not school_soccer_quest_talk_topics["rain"] and weather_var == 3:
        jump school_field_soccer_hangout_conv_rain
    elif not school_soccer_quest_talk_topics["snow"] and weather_var == 4:
        jump school_field_soccer_hangout_conv_snow
    elif not school_soccer_quest_talk_topics["beer"] and school_soccer_love_check(40):
        jump school_field_soccer_hangout_conv_beer
    else:

        jump school_field_soccer_hangout_picker





label school_field_soccer_hangout_conv:
    jump expression "school_field_soccer_hangout_conv_" + str(school_soccer_quest_hangout_conv)

label school_field_soccer_hangout_conv_1:
    $ school_soccer_quest_hangout_conv += 1
    drake.name "So what brings you round these parts anyway?"
    pc "Huh? Beer and football. Not much else to do here."
    drake.name "I mean [town]. Doesn't sound like you were from this area before."
    pc "Ah, no I wasn't. I wound up here trying to find somewhere safe to escape the riots."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_2:
    $ school_soccer_quest_hangout_conv += 1
    drake.name "So trying to escape the riots? Still doesn't explain how you ended up here. This place isn't what I would call safe."
    pc "Me and my sister were just trying to find somewhere safe to hide. But ended up run off he road and almost died."
    drake.name "Fuck! Really?"
    if quest_homeless_start.active:
        pc "Ended up wandering into the slums and stayed there for a bit."
    else:
        pc "Yeah, my sister was fine but I was a wreck. Spent ages in hospital. While I was there, [emile.name] set up a life while I recovered."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_3:
    $ school_soccer_quest_hangout_conv += 1
    if quest_homeless_start.active:
        dan.name "The slums?"
        pc "Yeah, bit of a shithole but found a free place to stay."
        pc "Bumped into my sister though when wandering the city. So all good now."
    else:
        drake.name "How did you wind up in the hospital after getting run off the road? Thought they would just leave you there."
        if main_quest_04.active == 2:
            pc "Well, I found out later it was one of the hospital's trucks that knocked us off the road. Guess they felt they owed me or something."
            drake.name "Hmm, lucky break I guess all things considered."
            pc "Mmm."
        else:
            pc "Yeah, not sure why myself. But I wasn't about to start asking questions."
            drake.name "Yeah I suppose."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_4:
    $ school_soccer_quest_hangout_conv += 1
    if quest_homeless_start.active:
        drake.name "What was your sister doing while you were slumming it?"
        pc "She managed to find a nice place and a job. Spent time looking for me."
        pc "She wasn't even sure I was alive. But luckily we found each other."
    else:
        drake.name "And your sister was fine after the crash?"
        pc "Yeah, seatbelts it seems do in fact save lives. While I was recovering, she was setting up a life."
        pc "After getting out the hospital I didn't really ask any questions and just went along with things. So seems I am living here now."
        nate.name "Good luck with that."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_5:
    $ school_soccer_quest_hangout_conv += 1
    nate.name "You sister live with you or what?"
    if main_quest_05.active == 2:
        $ school_soccer_quest_boys_know["sis_home"] = True
        pc "Yeah, we live together in a tiny room not too far from here."
        dan.name "Oh? Sharing the same room? Share the same bed as well?"
        pc "Err, yeah. No space for another bed."
        nate.name "Wow! Nice!"
        dan.name "Oh shit. Wonder if..."
        pc "Shush! Leave your fantasies to yourself."
    else:
        pc "Na, no idea where she lives actually. She set stuff up for me then vanished."
        nate.name "Oh..."
        pc "Not to worry, she will turn up eventually. Probably..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_6:
    $ school_soccer_quest_hangout_conv += 1
    dan.name "Why did you decide to come to this shithole?"
    pc "Didn't have much of a choice. I was signed up before I even left the hospital. Before I knew it I was here."
    dan.name "Well, for the best. Better coming here than working out there."
    pc "What do you mean? Not like they pay us to come here. Still have to work anyway so all this place does is eat up time."
    dan.name "Hmm, true."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_7:
    $ school_soccer_quest_hangout_conv += 1
    drake.name "What you doing for work anyway. Rent can't be easy."
    if pub_waitress.timesworked > 5:
        $ school_soccer_quest_boys_know["pub_work"] = True
        pc "Whatever pays. Been working at the pub on Revel. It gives some decent money I suppose."
        nate.name "Been there a few times but not recently. Might have to pop by knowing you are working there."
    elif quest_cleaner.timesworked >= 5:
        pc "Been doing some cleaning. Not great money but it helps me get by."
    elif quest_flyers.timesworked >= 5:
        pc "Been handing out flyers. Not great money but it helps me get by."
    else:
        pc "Not much. Work is not easy to find here... Not if you want to keep your dignity anyway."
        drake.name "Not a lot of that left in these parts any more."
    $ school_soccer_quest_hangout_conv_robin += 1
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_robin_1:
    $ add_to_list(robin.list, "soccer_hangout")
    $ school_soccer_quest_hangout_conv_robin = 2
    robin.name "Hey guys."
    drake.name "Hey [robin.name]. Decided to join us in the end?"
    robin.name "Yeah, not exactly beach weather and saw [name] hanging out with you lot."
    dan.name "Beer?"
    robin.name "Err, sure?"
    dan.name "Here."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_2:
    $ school_soccer_quest_hangout_conv_robin += 1
    nate.name "So what changed your mind?"
    robin.name "Eh, saw [name] hanging out with you ugly lot so you can't be all that bad."
    drake.name "Maybe [name] has bad decision making skills."
    pc "Thanks..."
    robin.name "She probably does."
    pc "Oh thanks!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_3:
    $ school_soccer_quest_hangout_conv_robin += 1
    nate.name "No matter how you look at it. You hanging out at the beach in a bikini is way more shady than with us [robin.name]."
    pc "Speaking from experience?"
    nate.name "Gotta be perverts everywhere round there."
    pc "Errr..."
    robin.name "Did he just say that?"
    nate.name "What?"
    drake.name "Idiot!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_4:
    $ school_soccer_quest_hangout_conv_robin += 1
    robin.name "So you okay hanging out with this lot?"
    pc "Yeah. They aren't too bad."
    pc "Except [nate.name]."
    nate.name "What did I do?"
    pc "You spend so much time staring at my tits I'm not sure you even know what colour my hair is."
    nate.name "Pfft. Like you mind."
    if player.has_perk([perk_slut, perk_whore, perk_bimbo, perk_exhibitionist]):
        pc "Well, no. But that's besides the point."
    else:
        nate.name "Well... They are nice..."
        robin.name "Pervert."
        drake.name "Haha!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_5:
    $ school_soccer_quest_hangout_conv_robin += 1
    drake.name "So what's your story [robin.name]?"
    robin.name "Huh? Just killing time."
    drake.name "Not from [town]?"
    robin.name "No. Ended up here when all the killing was going on."
    robin.name "Just stumbled on some goons, got beaten up, jabbed then ended up in some medical tent with hundreds of other folk."
    dan.name "Ah, then..."
    robin.name "Mmmm."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_6:
    $ school_soccer_quest_hangout_conv_robin += 1
    drake.name "So sticking around?"
    robin.name "Nowhere else to go. For some reason they let me come here so thought why the hell not?"
    robin.name "Not like I got much else going for me."
    drake.name "No family I assume?"
    robin.name "Orphan. Not cos of the plague. Was before all this."
    drake.name "Oh..."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_robin_sex_0:
    $ school_soccer_quest_hangout_conv_robin_sex += 1
    pc "So guys. What do you think of [robin.name]?"
    drake.name "Better at football than you are."
    pc "Wanna fuck her?"
    if rachel_here():
        rachel.name "Ooooh..."
    drake.name "Err..."
    nate.name "Don't answer. It's a trap."
    dan.name "Yup."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_sex_1:
    $ school_soccer_quest_hangout_conv_robin_sex += 1
    pc "About [robin.name]..."
    nate.name "Uh oh..."
    drake.name "This isn't going to cause problems is it?"
    pc "She knows what we have been getting up to and asked me to tell you she wants to have fun as well."
    nate.name "What? Seriously?"
    if rachel_here():
        rachel.name "Wow guys. You get all the fun."
    pc "Yeah."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_sex_2:
    $ school_soccer_quest_hangout_conv_robin_sex += 1
    nate.name "You sure about [robin.name] [name]? Not like I haven't offered."
    pc "Yeah, we had a chat about it after she found out we were having fun."
    nate.name "And she wants to as well?"
    pc "Yeah. But she's a bit shy about the whole thing and it's not an easy topic to raise."
    if rachel_here():
        rachel.name "No need to be shy. We can all have fun together."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_sex_3:
    $ school_soccer_quest_hangout_conv_robin_sex += 1
    $ add_to_list(robin.list, "soccerboys_told_sex")
    drake.name "You okay with [robin.name] joining in on the fun?"
    pc "Sure. We are friends so why not?"
    drake.name "Dunno. Just making sure."
    if rachel_here():
        pc "You are already fucking [rachel.name] and it's all good."
        rachel.name "Yup! The more the merrier."
    else:
        pc "Yeah, go for it."
        pc "Ah, but I was supposed to be discreet about the whole thing. So go easy on her at first."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_mira_arrival_0:
    $ mira.dict["soccer_hangout_conv"] += 1
    $ add_to_list(mira.list, "soccer_hangout")
    pc "Ah [mira.name]! You came to join us?"
    mira.name "Yeah, [dan.name] suggested I should hang out here before heading off to work."
    pc "Ah, yeah probably not a bad idea."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_mira_arrival_1:
    $ mira.dict["soccer_hangout_conv"] += 1
    pc "Why didn't you hang out with us before [mira.name]?"
    mira.name "No one knew what I did for work, so I kept things hidden."
    pc "Hmm, doubt anyone would have cared. Not these days anyway."
    mira.name "Maybe not. But I didn't know that."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_mira_arrival_2:
    $ mira.dict["soccer_hangout_conv"] += 1
    mira.name "It was probably all the secrecy that ended up getting me into trouble."
    pc "You think so?"
    mira.name "How long was it before anyone even thought to ask about me?"
    mira.name "If friends knew, they might have looked for me the moment I didn't come home."
    pc "Hmmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_mira_arrival_3:
    $ mira.dict["soccer_hangout_conv"] += 1
    pc "You think it could have stopped what happened?"
    mira.name "Not sure. Maybe. I'm not the only girl from here that works the highway."
    mira.name "If I didn't keep it all secret, I might have had people to hang out with."
    pc "[cass.name] hangs with you now doesn't she?"
    mira.name "Yeah."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_weekend:
    pc "Here even on the weekend?"
    drake.name "Yeah. Where else we gonna go?"
    pc "No idea. Don't you have other stuff to do? Work?"
    nate.name "Heh, yeah... Work."
    dan.name "Tussle with the urchins to get work sweeping some warehouse for barely enough to eat?"
    nate.name "That's assuming whoever hires us doesn't want to just bum fuck us instead."
    $ school_soccer_quest_talk_topics["weekend"] = True
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rain:
    pc "Here even in the rain?"
    dan.name "Nicer in the rain."
    pc "Huh?"
    dan.name "The rain sends everyone home so it's peaceful out here."
    $ school_soccer_quest_talk_topics["rain"] = True
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_snow:
    pc "It's freezing. What are you lot doing here still?"
    drake.name "Nothing better to do. Could ask you the same question."
    pc "..."
    pc "Yeah, nothing better to do."
    $ school_soccer_quest_talk_topics["snow"] = True
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_beer:
    pc "How have you lot always got beer?"
    drake.name "What do you mean? We buy it."
    pc "Yeah, with what money? None of you work."
    drake.name "We work. Just enough anyway. Not like we are here drinking stuff made from before. All this homebrew is pretty cheap."
    pc "Yeah?"
    $ school_soccer_quest_talk_topics["beer"] = True
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_bully_ask_remove1:
    $ school_soccer_quest_bully_remove["asked1"] = True
    drake.name "You having trouble with the filth?"
    $ player.face_conf()
    pc "Huh?"
    drake.name "Those two mouth breathers who give everyone some trouble. They seem to have taken a liking to you."
    if player.check_nowill():
        $ player.face_meek()
    else:
        $ player.face_angry()
    pc "Ah, them..."
    drake.name "They are just bottom feeders. [dan.name] here is looking for an excuse. Would get them off your back."
    $ player.face_surprised()
    pcm "Those cunts might wind up messing about with others if [dan.name] scares them off. Might even go after [cass.nname]..."
    menu:
        "Yes, get the bullies off my back":
            $ player.face_meek()
            pc "..."
            $ player.face_neutral()
            pc "I wouldn't say no..."
            drake.name "Mmm, no worries."
            $ school_bully_quest_bully_cass_target = True
        "No, better me than someone else":
            $ player.face_sad()
            pc "Unless they end up in a shallow grave it's better not to."
            dan.name "Why?"
            pc "I can handle it... Mostly."
            pc "Scare them off me and they will just push someone else around."
            dan.name "And?"
            pc "And that other person might wind up cutting their wrists because of it."
            dan.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_bully_ask_remove2:
    $ school_soccer_quest_bully_remove["asked2"] = True
    dan.name "Sure you don't want those shits off your back?"
    $ player.face_conf()
    pc "Ah, them?"
    menu:
        "Yes, get rid of them":
            $ player.face_meek()
            pc "*Sigh* Probably."
            dan.name "Ok."
            $ player.face_neutral()
            pc "Sorry..."
            dan.name "It's fine. They could do with a kicking anyway."
            $ school_bully_quest_bully_cass_target = True
        "No, they will just push someone else around":
            $ player.face_sad()
            pc "It's fine..."
            dan.name "..."
            dan.name "If you say so..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_bully_ask_remove3:







    $ school_soccer_quest_bully_remove["vanished"] = True
    $ school_soccer_quest_bully_remove["vanished_date"] = t.day + 1
    $ school_bully_quest_bully_soccer_boys_remove = True
    jump school_field_soccer_hangout

label school_field_soccer_hangout_bully_ask_remove_where:
    pcm "Hmm, the boys are not here today..."
    pcm "Those lazy bastards finally doing some work?"
    $ school_soccer_quest_bully_remove["vanished_field"] = True
    $ shane.kill()
    $ marcus.kill()
    $ shane.dead_location = "Seem's to have vanished. Good!"
    $ marcus.dead_location = "Somewhere far from here hopefully."
    $ shane.dead_message = "Hopefully found his way into a shallow grave."
    $ marcus.dead_message = "Face down in the same grave as the other cuntface!"
    jump travel

label school_field_soccer_hangout_bully_ask_remove_return:
    pc "Where did you lot vanish to?"
    drake.name "Had some work to do."
    pc "Really? I didn't think you lot had it in you."
    dan.name "I am offended!"
    pc "Yeah yeah. Well, glad to see you. Seems others went missing as well and was worried."
    drake.name "Who went missing?"
    pc "No one anyone will miss."
    $ school_soccer_quest_bully_remove["vanished_return"] = True
    $ shane.kill()
    $ marcus.kill()
    $ shane.dead_location = "Seem's to have vanished. Good!"
    $ marcus.dead_location = "Somewhere far from here hopefully."
    $ shane.dead_message = "Hopefully found his way into a shallow grave."
    $ marcus.dead_message = "Face down in the same grave as the other cuntface!"
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_sis_home:
    $ school_soccer_quest_boys_know["sis_home"] = True
    pc "So my sister came to live with me..."
    drake.name "Oh? That's good right?"
    pc "Yeah, though I have a tiny place so not much room."
    dan.name "Oh? Sharing the same room? Share the same bed as well?"
    pc "Err, yeah. No space for another bed."
    nate.name "Wow! Nice!"
    dan.name "Oh shit. Wonder if..."
    pc "Shush! Leave your fantasies to yourself."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_pubwork:
    pc "Started working at that pub on Revel street to get a bit of extra cash."
    nate.name "Oh, I've been there. Interesting place."
    dan.name "How's the pay?"
    pc "No pay, just tips."
    dan.name "Shit, that's rough."
    pc "Mmm..."
    $ school_soccer_quest_boys_know["pub_work"] = True
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_backentrance_show:
    drake.name "Hey, how come you never come hang out with us at night? You working or something?"
    pc "Huh, at night? Where do you lot hang out?"
    drake.name "Here. Where else?"
    pc "Err, the school closes at night. Don't they kick you out while they are locking up?"
    drake.name "Ah, didn't we tell you? We made a hole in the fence over there by the pitch. Doesn't get you into the school but can hang out here at night."
    if loc_school_secret_entrance.visited:
        pc "Ah, I found that when wandering around. It was you guys that made it?"
        drake.name "Yeah, it's quiet here at night, only us most of the time so a good place to hang out."
    else:
        pc "Ah, no. No one mentioned it. I'll keep that in mind."
        drake.name "Yeah you should. Never anyone but us here at night so no chance of anyone giving you trouble. Can chill out here and drink some beers without issue."
    pc "Good to know."
    $ school_soccer_quest_backentrance["shown"] = True
    $ loc_school_secret_entrance.locked = False
    jump school_field_soccer_hangout_end

label school_field_soccer_hangout_backentrance_used:
    $ player.face_neutral()
    $ school_soccer_quest_backentrance["talk"] = True
    drake.name "Found the back entrance did you?"
    $ player.face_worried()
    pc "Yeah, was a bit of a squeeze though."
    drake.name "Nothing happen I hope. I saw the movies back when there was internet."
    if havenvent.vsex > 0:
        $ player.face_meek()
        pc "Yeah... Never letting that happen again."
        drake.name "Err..."
        drake.name "Again?"
        $ player.face_worried()
        drake.name "Make a habit of sticking your bum out for people to have fun or something?"
        if player.check_nowill():
            $ player.face_meek()
            pc "..."
            drake.name "Err, ok. Touchy subject."
            pc "..."
            drake.name "Right..."
            drake.name "Anyway, nice to see you joining us..."
        else:
            $ school_soccer_quest_boys_know["raped"] = True
            $ player.face_angry()
            pc "*Tsk* I thought I was being sneaky and getting my hands on a hidden stash."
            if havenvent.vsex > 1:
                $ dialouge = "One gang raping "
            else:
                $ dialouge = "One raping "
            if havenvent.preg:
                $ dialouge = dialouge + "and a baby in my belly "
            $ dialouge = dialouge + "later"
            pc "[dialouge] and I realised it wasn't such a smart idea after all..."
            drake.name "Oh, hey... Sorry. I was just messing about. Didn't realise it was a touchy subject."
            $ player.face_sad()
            if player.rape > havenvent.vsex:
                pc "It's fine. Not like getting raped round these parts is anything new."
            else:
                pc "It's fine. These things happen."
            drake.name "Err..."
            drake.name "..."
            drake.name "Beer?"
            $ player.face_happy()
            pc "Yup!"
    else:
        pc "Yeah, was thinking the same when I sneaked through. But no worries. Made it through with my dignity."
        if c.skirt:
            $ player.face_worried()
            pc "Well, mostly anyway. Should probably avoid climbing in tight places with a skirt on in future."
    $ player.face_neutral()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_exhibitionist:
    $ add_to_list(school_soccer_quest.conversation_topics, "exhibitionist_asked")
    pc "So, you guys probably already realised by now. But I like to show off."
    if robin_here():
        robin.name "Oh no..."
    nate.name "Mmm, yeah can tell."
    $ player.face_shy()
    pc "Mind if I hang out naked with you all?"
    drake.name "*COUGH*"
    nate.name "What!?"
    if robin_here():
        robin.name "Ugh..."
    pc "..."
    drake.name "Really?"
    pc "Yeah, I like it."
    nate.name "Not going to complain."
    pc "I know you aren't going to. I am asking the less perverted ones of the group."
    drake.name "No complaints."
    dan.name "None."
    nate.name "Can we... Err, look?"
    pc "I'd be upset if you didn't."
    nate.name "Win!"
    $ pc_striptease(temp=True)
    show sb_pose_lookback smile with dissolve
    pc "Get it out of your system."
    drake.name "Fuck!"
    nate.name "Ooooh!"
    show sb_pose_lookback normal with dissolve
    $ player.spank()
    pc "Ah!"
    pc "No touching!"
    show sb_pose_lookback tounge with dissolve
    pc "Unless I ask."
    nate.name "Right."
    hide sb_pose_lookback with dissolve
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photos:
    $ add_to_list(school_soccer_quest.conversation_topics, "has_photos_know")
    nate.name "Fucking hell. Look here!"
    drake.name "Wow!"
    pc "What are those idiots up to?"
    dan.name "[nate.name] managed to buy some of your photos off of [felix.name]. They're looking through them now."
    pc "Ah. Okay then... Should probably leave them alone."
    nate.name "Fuck. Look here!"
    drake.name "Shit!"
    pc "Or maybe they should go somewhere alone..."
    dan.name "Probably."
    pc "HEY GUYS!"
    nate.name "..."
    drake.name "Errr..."
    nate.name "{color=#b3b3b3}Hide them!{/color}"
    drake.name "{color=#b3b3b3}I'm trying!{/color}"
    pc "I know what you have there."
    nate.name "Errr..."
    pc "Enjoy them."
    drake.name "...Thanks?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_picker:


    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_conv_drunk", If(player.drunk>100, player.drunk - 100, 0)),
    ("school_field_soccer_hangout_conv_" + str(school_soccer_quest_hangout_conv), If(renpy.has_label("school_field_soccer_hangout_conv_" + str(school_soccer_quest_hangout_conv)),1000,0)),

    
    ("school_field_soccer_hangout_conv_robin_1", If(t.day > 15 and robin.love > 50 and not t.timeofday == "night" and not robin_here(dis_beach.locs) and not "soccer_hangout" in robin.list, 100, 0)),
    ("school_field_soccer_hangout_conv_robin_" + str(school_soccer_quest_hangout_conv_robin), If(robin_here() and renpy.has_label("school_field_soccer_hangout_conv_robin_" + str(school_soccer_quest_hangout_conv_robin)),100,0)),
    ("school_field_soccer_hangout_conv_robin_sex_" + str(school_soccer_quest_hangout_conv_robin_sex), If("soccerboys_asked_sex" in robin.list and not robin_here() and renpy.has_label("school_field_soccer_hangout_conv_robin_sex_" + str(school_soccer_quest_hangout_conv_robin_sex)),1000,0)),

    
    

    ("school_field_soccer_hangout_mira_arrival_0", If(not "soccer_hangout" in mira.list and t.wkday in weekdays and t.hour in (16,17, 18, 19) and school_soccer_hangingout() and "rescued" in mira.list and not "hospitalised" in mira.list ,100, 0)),
    ("school_field_soccer_hangout_mira_arrival_" + str(mira.dict["soccer_hangout_conv"]), If(mira_here() and renpy.has_label("school_field_soccer_hangout_mira_arrival_" + str(mira.dict["soccer_hangout_conv"])) and "soccer_hangout" in mira.list and t.wkday in weekdays and t.hour in (16,17, 18, 19) and school_soccer_hangingout() and "rescued" in mira.list and not "hospitalised" in mira.list ,100, 0)),

    
    ("school_field_soccer_hangout_dare_intro", If (not school_soccer_quest_betmatch["intro"], 30,0)),
    ("school_field_soccer_hangout_dare_offer", If (school_soccer_quest_betmatch["intro"] and t.timeofday =="night", 10,0)),

    
    ("school_field_soccer_hangout_conv_rachel_nudeask", If (rachel_here() and not c.nude and t.timeofday == "night", 100,0)),
    ("school_field_soccer_hangout_conv_rachel_nudetalk_" + str(rachel.dict["rachel_nude"]), If (renpy.has_label("school_field_soccer_hangout_conv_rachel_nudetalk_" + str(rachel.dict["rachel_nude"])) and rachel_here() and robin_here() and not any(["naked_for_boys" in robin.list, "will_get_naked_boys" in robin.list]) and not t.timeofday == "day", 100, 0)),
    
    
    ("school_field_soccer_hangout_conv_subject", 100),
    ])
    jump expression rand_choice

label school_field_soccer_hangout_conv_drunk:
    $ player.face_puke()
    pc "I'll be back..."
    pause 0.2
    $ randomnum = renpy.random.randint(0, 1)
    if randomnum == 1 or weather_var >= 2:
        $ walk(loc_school_locker_old)
    else:
        $ walk(loc_bushes)

    $ player.face_puke()
    pc "Ubbb!"

    pause 0.5
    $ player.inhib_puke()
    $ player.face_puke2()
    pc "Bleeehh!!!"
    show screen blackout(25) with dissolve
    hide screen blackout with dissolve
    show screen blackout(50) with dissolve
    $ relax(5)
    $ player.face_sad()
    hide screen blackout with dissolve
    pc "Owaaaa..."

    $ rand_choice = WeightedChoice([
    ("school_field_soccer_hangout_conv_drunk1", 100),
    ("school_field_soccer_hangout_conv_drunk2", 30),
    
    
    ])
    jump expression rand_choice

label school_field_soccer_hangout_conv_drunk1:
    pcm "Ugh..."
    pcm "Might have had a bit much..."
    $ walk(loc_from)
    $ player.face_worried()
    pc "Uhhh."
    drake.name "Have fun?"
    pc "Just making room for more..."
    drake.name "Sure..."
    jump travel

label school_field_soccer_hangout_conv_drunk2:
    pcm "Ugh..."
    pcm "Just... Sit for a bit..."
    $ player.face_sleep()
    pause 0.1
    show screen blackout(100) with dissolve
    $ randomnum = renpy.random.randint(20,150)
    $ relax(randomnum)
    pause 0.5
    $ player.face_sleep()
    hide screen blackout with Dissolve(0.2)
    pcm "Ugghhh..."
    $ player.face_worried()
    $ player.eye = 2
    pcm "Where am..."
    pcm "Ah fuck. Drunk too much..."
    $ player.face_worried()
    pcm "Ugh..."
    jump travel

label school_field_soccer_hangout_gloryhole_ask:
    $ quest_gloryhole_create.activate()
    nate.name "We were talking earlier on about glory holes."
    pc "Of course you were..."
    if robin_here():
        robin.name "Ugh..."
    nate.name "Think one in the school would work?"
    pc "Huh?"
    nate.name "Was thinking about making a hole in the men's toilets through to the girls and seeing if it takes off."
    pc "Right. Good for you."
    nate.name "Think you can get hold of something to make a hole in the wall for us?"
    pc "Me? What makes you think I can get hold of the tools?"
    if player.has_perk(perk_gamine):
        nate.name "Well, you know how to get around so though you might be able to get hold of something."
    elif player.has_perk([perk_slut, perk_whore]):
        nate.name "Well, you meet with your fair share of men. Maybe you can get something off them?"
    else:
        nate.name "Well, the only other option is getting [dan.name] to ask around [haven]. Better to ask you before dealing with that lot."
    pc "Right..."
    pc "Whatever. I'll tell you if I come across anything."
    $ log.assign("Making a glory hole")
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_chis:
    pc "So I got hold of a chisel you can probably use for making a glory hole."
    nate.name "Nice one [name]!"
    if log.interactive("quest_gloryhole_a"):
        $ log.markdone("quest_gloryhole_a")
    $ log.markdone("quest_gloryhole_b_chis")
    $ inv.drop(item_chis)
    $ nate.inv.take(item_chis)
    if nate.inv.qty(item_chis) and nate.inv.qty(item_saw):
        jump school_field_soccer_hangout_gloryhole_saw_chis
    else:
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_saw:
    pc "So I got hold of a saw you can probably use for making a glory hole."
    nate.name "Nice one [name]!"
    if log.interactive("quest_gloryhole_a"):
        $ log.markdone("quest_gloryhole_a")
    $ log.markdone("quest_gloryhole_b_saw")
    $ inv.drop(item_saw)
    $ nate.inv.take(item_saw)
    if nate.inv.qty(item_chis) and nate.inv.qty(item_saw):
        jump school_field_soccer_hangout_gloryhole_saw_chis
    else:
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_saw_chis:
    pc "So you should be able to make a hole now shouldn't you?"
    drake.name "Won't a hole like that just tear your cock apart?"
    nate.name "Hmm, yeah. Using that saw is going to make a pretty rough hole."
    drake.name "Probably why the movies put tape all around the hole."
    nate.name "Yeah. Wonder where we can get some..."
    $ log.activate("quest_gloryhole_b_tape")
    if inv.qty(item_tape):
        pc "Actually I picked some tape up as well. This ok?"
        jump school_field_soccer_hangout_gloryhole_tape_cont
    else:
        pc "*Sigh* I'll keep a look out..."
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_tape:
    pc "So I got my hands on some tape for your glory hole project."
    jump school_field_soccer_hangout_gloryhole_tape_cont

label school_field_soccer_hangout_gloryhole_tape_cont:
    $ inv.drop(item_tape)
    $ nate.inv.take(item_tape)
    $ log.markdone("quest_gloryhole_b_tape")
    $ log.activate("quest_gloryhole_c")
    nate.name "Fucking great [name]!"
    pc "So that should be everything?"
    if not t.timeofday == "day":
        jump school_field_soccer_hangout_gloryhole_create
    else:
        nate.name "That should be it. Now we just wait until it gets dark and everyone is gone."
        jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_create:
    nate.name "Ok, let's sneak inside and give this a go. You guys coming?"
    drake.name "Na. I'll let you do the work for your perverted game."
    dan.name "I'll be here drinking."
    if robin_here():
        robin.name "You're on your own [name]."
    nate.name "Right..."
    nate.name "Let's go [name]!"
    pc "Wait. How come they get to stay and you are dragging me along?"
    nate.name "I need someone on the girls' side to help out."
    if c.nude:
        if player.has_perk(perk_exhibitionist):
            pc "And want to parade me around the school stark naked?"
            nate.name "Like you care you dirty bitch."
        else:
            pc "I'm stark naked and you want to drag me through the school?"
            nate.name "No one is there. Plus I get to see your arse in a better light."
    elif c.cansee_ass:
        pc "Got my bare arse out and you wanna drag me through the school?"
        nate.name "No one is there. Plus I get to see your arse in a better light."
    elif c.cansee_breasts:
        pc "You want to drag me through the school with my tits out?"
        nate.name "Sure. And I get to look at them in a better light."
    elif c.exposed:
        pc "Not exactly dressed for trapsing through the school."
        nate.name "Your problem, not mine."
    elif robin_here():
        pc "Could ask [robin.name] for help."
        nate.name "Doesn't seem like she is up for it."
        pc "Nor am I!"
        nate.name "C'mon [name]. Don't be a spoilsport."
    pc "*Sigh*"
    pc "Come on then."
    show nate at left1
    $ walk(loc_school_field)
    pc "How we getting into the school?"
    nate.name "They usually don't lock the side doors, only the front."
    $ walk(loc_school_hallway)
    nate.name "See?"
    $ walk(loc_school_toilet)
    show nate with dissolve:
        xzoom 1
    nate.name "Right, so you wait in the girls near the wall and I'll get to work making a hole."
    pc "This is vandalism you know? They might not like you breaking their walls."
    nate.name "Hopefully no one tells."
    hide nate with dissolve
    pcm "Yeah. Nothing like trying to pee and someone sticks their dick through the wall..."
    pcm "Whatever..."
    $ walk(loc_school_toilet_girls)
    $ walk(loc_school_toilet_girls_stall)

    if loc_cur.has_gloryhole:
        pc "Errm... [nate.name]?"
        nate.name "Yeah, I see it."
        nate.name "Wow, okay. Seems there are other smart people coming here."
        pc "Yeah, looks like you were out perverted."
        nate.name "Mayb we should test it?"
        $ walk(loc_school_toilet_girls)
        pcm "Idiot."
        $ walk(loc_school_hallway)
        pcm "..."
        pcm "He's probaby standing there with his dick in the hole."
        $ add_to_list(nate.list, "no_location")
        $ walk(loc_school_field)
        $ walk(loc_school_field_back)
        if drake_here():

            drake.name "That was quick."
            pc "Yeah, [nate.name] isn't the genius he thinks he is."
            drake.name "Yeah, we all know that."
        elif dan_here():
            dan.name "You just left and you are back already?"
            pc "Yeah, [nate.name] isn't the genius he thinks he is."
            dan.name "Yeah..."
        $ remove_from_list(nate.list, "no_location")
        nate.name "Leaving me with my dick out like that?"
        pc "Yeah, it was funny."
        nate.name "Someone else made a hole!"
        if dan_here():
            dan.name "So that's what [name] was talking about?"
        elif drake_here():
            drake.name "So you were too slow?"
        else:
            nate.name "Wait, where is everyone?"
        pc "Well, at least you got your hole for afternoon fun in the toilet."
        nate.name "Yeah, I should try it during lunch."
        $ log.markdone("quest_gloryhole_c")
        jump school_field_soccer_hangout_conv_end

    pcm "Right then..."
    $ relax(10)
    "I hang out in the stall waiting to see if [nate.name] makes any progress."
    pcm "I could go round to the other side and help him..."
    pcm "Na..."
    $ relax(5)
    "I can hear him bashing away and making some progress. And it's not long before he manages to make it though to my side."
    pc "Oh, you made it?"
    nate.name "Yeah, now just to make it bigger."
    $ relax(5)
    "I stand there watching as he uses the saw to make the the hole bigger and more of a circle. He actually doesn't do a bad job of it."
    pcm "Why am I here again? He could have done all this without me."
    nate.name "Right [name]. The hole is done so help me smooth it out with the tape."
    pc "Ok."
    "He passes strips of tape through the hole and I stick them wherever it looks like there is a rough exposed bit."
    $ loc_school_toilet_girls.has_gloryhole = True
    $ loc_school_toilet_boys.has_gloryhole = True
    $ loc_school_toilet_girls_stall.has_gloryhole = True
    $ loc_school_toilet_boys_stall.has_gloryhole = True
    pc "Looks like it should be fine from here."
    nate.name "Same here."
    $ log.markdone("quest_gloryhole_c")
    show gh_blow_behind no_man_hole with dissolve
    pc "Not a bad job. Looks like it should be fine."
    pc "Assuming someone doesn't block it up in the morning."
    nate.name "Hopefully not."
    pc "So we done?"
    nate.name "Hold on..."
    pc "..."
    $ npc_race_picker(nate)
    show gh_blow_behind man_hole with dissolve
    $ player.face_happy()
    pc "Fucking hell [nate.name]."
    pc "Damn pervert"
    nate.name "Well. You gonna try it out?"

    if player.check_sex_agree(3):
        menu:
            "Sure, why not?":
                jump school_field_soccer_hangout_gloryhole_create_suck
            "You are on your own":
                jump school_field_soccer_hangout_gloryhole_create_suck_reject
    else:
        jump school_field_soccer_hangout_gloryhole_create_suck_reject

label school_field_soccer_hangout_gloryhole_create_suck:
    pc "Pervert!"
    hide gh_blow_behind
    show gh_blow_close
    with dissolve
    pc "Hold on, shouldn't you put money on it?"
    nate.name "Hmm, wonder how much I should write..."
    pc "Heh."
    pc "Try 200 and see how that goes."
    nate.name "Ok."
    $ player.sex_oral(nate, quest_gloryhole_create)
    show gh_blow_close lick with dissolve
    pc "Don't expect me to do this on a regular basis."
    if nate.sex:
        nate.name "It's fine, I'll just fuck you out back again."
    elif nate.osex > 1:
        nate.name "Why not? This isn't the first time you are sucking my cock."
    else:
        nate.name "Don't worry. You won't know if it's me the next time you come here."
    pc "Ha. Assuming it will be me here again?"
    if player.has_perk(perk_whore):
        nate.name "Sure. Easy way for you to earn."
    else:
        nate.name "I will imagine it is you whenever I am here."
    pc "Yeah yeah..."
    show gh_blow_close suck with dissolve
    nate.name "Oh fuck!"
    nate.name "Ah yes. Like that! All the way."
    nate.name "Fuck this is pretty hot."
    pc "Mmmmf?"
    nate.name "Be nicer though if my face wasn't pressed against this nasty wall..."
    pc "*Hyuk*"
    show gh_blow_close cum with dissolve
    pc "Fucking hell [nate.name]. Don't make me laugh with your cock in my mouth."
    nate.name "I should put some photos on the wall."
    if "has_photos_know" in school_soccer_quest.conversation_topics:
        nate.name "Stick some of those picutes [felix.name] took of you up here."
        nate.name "Everyone will be imagining it's you."
    pc "You do that..."
    show gh_blow_close suck with dissolve
    nate.name "Haaaa."
    nate.name "Keep going!"
    pcm "This is kinda fun."
    pcm "I know it's [nate.name] on the other side. But being anonymous like this could be exciting."
    nate.name "Ah yeah like that!"
    pcm "Mmmm."
    $ player.sex_cum(nate, "mouth", quest_gloryhole_create)
    nate.name "Ahhhhhh!"
    pc "Ubbbbb!"
    show gh_blow_close cum with dissolve
    pc "Shum warging ext ime."
    nate.name "Haa. Sorry. Next time."
    show gh_blow_close no_pc with dissolve
    show gh_blow_close no_man_hole with dissolve
    hide gh_blow_close with dissolve
    pc "Ubb..."
    pcm "Right then..."
    $ walk(loc_school_toilet_girls)
    $ walk(loc_school_hallway)
    $ walk(loc_school_field)
    show nate at right1 with dissolve
    nate.name "Same again tomorrow morning?"
    pc "Sure."
    hide nate with dissolve
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout_gloryhole_create_wrapup

label school_field_soccer_hangout_gloryhole_create_suck_reject:
    pc "You're on your own mate"
    hide gh_blow_behind
    $ walk(loc_school_toilet_girls)
    $ walk(loc_school_hallway)
    $ walk(loc_school_field)
    show nate at right1 with dissolve
    nate.name "Leaving me behind with my cock hanging out?"
    pc "Heh."
    hide nate with dissolve
    $ walk(loc_school_field_back)
    jump school_field_soccer_hangout_gloryhole_create_wrapup

label school_field_soccer_hangout_gloryhole_create_wrapup:
    drake.name "How'd it go?"
    pc "Yeah, he managed to make something that won't destroy your cock."
    if player.cum_locations["cum_mouth"]:
        drake.name "Yeah, by the look of your face it worked out well."
        pc "Shit..."
        pc "Better wash it down with a beer."
        if robin_here():
            $ add_to_list(robin.list, "soccerboys_seen_gloryhole_cum")
            $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_gloryhole_give_tools:
    nate.name "You need this stuff back [name]?"
    pc "What stuff?"
    nate.name "The tools to make the hole."
    pc "Ah."
    pcm "Can't hurt to have them back."
    pc "Yeah."
    nate.name "Sure."
    $ inv.take(item_chis)
    $ inv.take(item_saw)
    $ nate.inv.drop(item_chis)
    $ nate.inv.drop(item_saw)
    nate.name "Tape got used up when making the hole."
    pc "Thanks."
    pcm "Hmm, now that I have these tools. I can probably make holes elsewhere."
    pcm "Why would I want to though?"
    pcm "Hmmm..."
    $ log.assign("Glory holes")
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_subject:


    $ rand_choice = WeightedChoice([

    ("school_field_soccer_hangout_conv_general1", 100),
    ("school_field_soccer_hangout_conv_general2", 100),
    ("school_field_soccer_hangout_conv_general3", 100),
    ("school_field_soccer_hangout_conv_general4", If(c.pokenips, 100, 0)),
    ("school_field_soccer_hangout_conv_general5", 100),

    ("school_field_soccer_hangout_conv_pub1", If(school_soccer_quest_boys_know["pub_work"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub2", If(school_soccer_quest_boys_know["pub_work"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub3", If(school_soccer_quest_boys_know["pub_work"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub4", If(school_soccer_quest_boys_know["pub_work"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub5", If(school_soccer_quest_boys_know["pub_work"] and not school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub7", If(school_soccer_quest_boys_know["pub_work"] and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub8", If(school_soccer_quest_boys_know["pub_work"] and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub9", If(school_soccer_quest_boys_know["pub_work"] and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_pub10", If(school_soccer_quest_boys_know["pub_work"] and school_soccer_quest_boys_know["whore"], 100, 0)),

    

    ("school_field_soccer_hangout_conv_sisjoke1", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke2", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke3", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke4", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke5", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke6", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),
    ("school_field_soccer_hangout_conv_sisjoke7", If(school_soccer_quest_boys_know["sis_home"], 100, 0)),

    ("school_field_soccer_hangout_conv_dance1", If(school_dance_quest_on_team, 100, 0)),
    ("school_field_soccer_hangout_conv_dance2", If(school_dance_quest_on_team, 100, 0)),
    ("school_field_soccer_hangout_conv_dance3", If(school_dance_quest_on_team, 100, 0)),
    ("school_field_soccer_hangout_conv_dance4", If(school_dance_quest_on_team and school_dance_quest_show_count >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_dance5", If(school_dance_quest_on_team and school_dance_quest_show_count >= 5, 100, 0)),
    ("school_field_soccer_hangout_conv_dance6", If(school_dance_quest_on_team and school_dance_quest_show_count >= 5, 100, 0)),
    ("school_field_soccer_hangout_conv_dance7", If(school_dance_quest_on_team and school_dance_quest_show_count >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_dance8", If(school_dance_quest_on_team and school_dance_quest_show_count >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_dance9", If(school_dance_quest_on_team and school_dance_quest_show_count >= 2 and not "soccerboys_hangout" in rachel.list, 100, 0)),
    ("school_field_soccer_hangout_conv_dance10", If(school_dance_quest_on_team and school_dance_quest_show_count >= 8 and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_dance11", If(rachel.fname in drake.conversation_topics and not "told_sex_" + rachel._original_name in drake.conversation_topics, 300, 0)),
    ("school_field_soccer_hangout_conv_dance12", If(rachel.fname in nate.conversation_topics and not "told_sex_" + rachel._original_name in nate.conversation_topics, 300, 0)),
    ("school_field_soccer_hangout_conv_dance13", If(rachel.fname in dan.conversation_topics and not "told_sex_" + rachel._original_name in dan.conversation_topics, 300, 0)),
    ("school_field_soccer_hangout_conv_dance14", If(any([rachel.sex_who.has_key(drake.fname), rachel.sex_who.has_key(nate._original_name), rachel.sex_who.has_key(dan._original_name)]) and not robin_here(), 100, 0)),
    ("school_field_soccer_hangout_conv_dance15", If(all([rachel.sex_who.has_key(drake.fname), rachel.sex_who.has_key(nate._original_name), rachel.sex_who.has_key(dan._original_name)]) and not robin_here(), 100, 0)),
    ("school_field_soccer_hangout_conv_dance16", If("pregnant_" + rachel._original_name in rachel.pregnant_who.conversation_topics, 1000, 0)),

    ("school_field_soccer_hangout_conv_preg1", If(player.showing >= 2 and not school_soccer_isfather(), 100, 0)),
    ("school_field_soccer_hangout_conv_preg2", If(player.showing >= 2 and not school_soccer_isfather(), 100, 0)),
    ("school_field_soccer_hangout_conv_preg3", If(player.showing >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_preg4", If(player.showing >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_preg5", If(player.showing >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_preg6", If(robin_here() and not robin.preg and player.showing >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_preg7", If(robin_here() and robin.pregbabies and player.showing >= 2 and not player.pregbabies, 100, 0)),
    ("school_field_soccer_hangout_conv_preg8", If(robin_here() and player.pregnancy >= 3, 100, 0)),

    ("school_field_soccer_hangout_conv_preg_robin1", If(robin_here() and robin.showing, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_robin2", If(robin_here() and robin.showing, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_robin3", If(robin_here() and robin.showing, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_robin4", If(robin_here() and robin.showing, 100, 0)),

    ("school_field_soccer_hangout_conv_preg_robin_pc1", If(robin_here() and robin.showing and player.pregnancy >= 2, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_robin_pc2", If(robin_here() and robin.showing and player.pregnancy >= 2 and player.preg_father_class in (nate, drake, dan) and robin.pregnant_who in (drake, nate, dan), 100, 0)),

    ("school_field_soccer_hangout_conv_preg_drake_1", If(drake.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_drake_2", If(drake.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_drake_3", If(drake.preg_knows, 100, 0)),

    ("school_field_soccer_hangout_conv_preg_nate_1", If(nate.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_nate_2", If(nate.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_nate_3", If(nate.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_nate_4", If(nate.preg_knows, 100, 0)),

    ("school_field_soccer_hangout_conv_preg_dan_1", If(dan.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_dan_2", If(dan.preg_knows, 100, 0)),
    ("school_field_soccer_hangout_conv_preg_dan_3", If(dan.preg_knows, 100, 0)),

    ("school_field_soccer_hangout_conv_allure1", nate.lust),
    ("school_field_soccer_hangout_conv_allure2", If(c.clevage and not c.bra and not c.cansee_breasts, nate.lust, 0)),  
    ("school_field_soccer_hangout_conv_allure3", If(c.ass, nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure4", If(c.skirt and not c.pants, nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure5", If(c.slutty and player.has_perk(perk_whore), nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure6", If(c.clothed, nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure7", If(c.clothed, nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure8", nate.lust),
    ("school_field_soccer_hangout_conv_allure9", If(c.clothed, nate.lust, 0)),
    ("school_field_soccer_hangout_conv_allure10", nate.lust),
    ("school_field_soccer_hangout_conv_allure11", nate.lust),

    ("school_field_soccer_hangout_conv_haven0" , If(not school_soccer_quest_boys_know["haven"], 50, 0)),
    ("school_field_soccer_hangout_conv_haven" + str(school_soccer_quest_boys_know["haven"]), If(school_soccer_love_check(school_soccer_quest_boys_know["haven"] * 10 + 20) and renpy.has_label("school_field_soccer_hangout_conv_haven" + str(school_soccer_quest_boys_know["haven"])), 100, 0)),
    ("school_field_soccer_hangout_conv_slave" + str(school_soccer_quest_boys_know["slave"]), If(school_soccer_quest_boys_know["slave"] and renpy.has_label("school_field_soccer_hangout_conv_slave" + str(school_soccer_quest_boys_know["slave"])), 100, 0)),

    ("school_field_soccer_hangout_conv_whore1", If(school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore2", If(school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore3", If(school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore4", If(school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore5", If(school_soccer_quest_boys_know["whore"] and player.pregnancy >= 2, 100, 0)),

    ("school_field_soccer_hangout_conv_whore_robin1", If(robin_here() and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore_robin2", If(robin_here() and school_soccer_quest_boys_know["whore"], 100, 0)),
    ("school_field_soccer_hangout_conv_whore_robin3", If(robin_here() and school_soccer_quest_boys_know["whore"], 100, 0)),
    

    ("school_field_soccer_hangout_conv_bully1", If(school_soccer_quest_bully_remove["asked1"] and not (school_soccer_quest_bully_remove["accepted"] or shane.dead), 200, 0)),
    ("school_field_soccer_hangout_conv_bully2", If(school_soccer_quest_bully_remove["asked1"] and not (school_soccer_quest_bully_remove["accepted"] or shane.dead), 200, 0)),

    
    ("school_field_soccer_hangout_conv_photo1", If(school_photo_intro_quest_stage >= 4 and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo2", If("dance_modest" in school_photo_quest.list and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo3", If("dance_sexy" in school_photo_quest.list and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo4", If("witch" in school_photo_quest.list and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo5", If("catgirl" in school_photo_quest.list and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo6", If("santa" in school_photo_quest.list and not "has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo7", If("has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo8", If("has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo9", If("has_photos" in school_soccer_quest.conversation_topics, 100, 0)),
    ("school_field_soccer_hangout_conv_photo10", If("has_dani_photos" in school_soccer_quest.conversation_topics and not "dani_photos_pc_knows" in school_photo_quest.conversation_topics, 100, 0)),

    
    ("school_field_soccer_hangout_gloryhole_ask", If (nate.love > 45 and not quest_gloryhole_create.active, 5000,0)),
    ("school_field_soccer_hangout_gloryhole_chis", If (log.interactive("quest_gloryhole_b_chis") and not nate.inv.qty(item_chis) and inv.qty(item_chis), 5000,0)),
    ("school_field_soccer_hangout_gloryhole_saw", If (log.interactive("quest_gloryhole_b_saw") and not nate.inv.qty(item_saw) and inv.qty(item_saw), 5000,0)),
    ("school_field_soccer_hangout_gloryhole_tape", If (log.interactive("quest_gloryhole_b_tape") and not nate.inv.qty(item_tape) and inv.qty(item_tape), 5000,0)),
    ("school_field_soccer_hangout_gloryhole_create", If (log.interactive("quest_gloryhole_c") and nate.inv.qty(item_chis) and nate.inv.qty(item_saw) and nate.inv.qty(item_tape) and not t.timeofday == "day", 5000,0)),
    ("school_field_soccer_hangout_gloryhole_give_tools", If (quest_gloryhole_create.iscomplete() and nate.inv.qty(item_chis), 5000,0)),

    
    ("school_field_soccer_hangout_conv_robin_general1", If (robin_here(), 100,0)),
    ("school_field_soccer_hangout_conv_robin_general2", If (robin_here(), 100,0)),
    ("school_field_soccer_hangout_conv_robin_general3", If (robin_here() and pub_waitress.timesworked > 2, 100,0)),
    ("school_field_soccer_hangout_conv_robin_general4", If (robin_here(), 100,0)),
    ("school_field_soccer_hangout_conv_robin_general5", If (robin_here(), 100,0)),
    ("school_field_soccer_hangout_conv_robin_general6", If (robin_here(), 100,0)),
    ("school_field_soccer_hangout_conv_robin_general7", If (robin_here() and "exhibitionist_asked" in school_soccer_quest.conversation_topics and c.nude and not "naked_for_boys" in robin.list, 100,0)),

    
    ("school_field_soccer_hangout_conv_rachel_nudeask", If (rachel_here() and not c.nude and not t.timeofday == "day", 1000,0)),

    ("school_field_soccer_hangout_conv_rachel_nudetalk_" + str(rachel.dict["rachel_nude"]), If (renpy.has_label("school_field_soccer_hangout_conv_rachel_nudetalk_" + str(rachel.dict["rachel_nude"])) and rachel_here() and robin_here() and not any(["naked_for_boys" in robin.list, "will_get_naked_boys" in robin.list]) and not t.timeofday == "day", 800,0)),
    ("school_field_soccer_hangout_conv_robin_strip", If (rachel_here() and robin_here() and "will_get_naked_boys" in robin.list, 1000,0)),
    
    ("quest_mira_missing_soccer_hangout_mira_ask", If (log.interactive("mira_missing_01") and not "asked_about_mira" in dan.list, 5000,0)),
    

    
    ("school_field_soccer_hangout_conv_group_sex_ask", If ((rachel_here() and "soccer_sex_rachel" in rachel.list) or (robin_here() and "soccer_sex_robin" in robin.list), 100,0)),
    ("school_field_soccer_sex_robin_spy", If (robin_here() and "soccer_sex_robin" in robin.list and player.check_horny(), 100,0)),
    ])
    jump expression rand_choice





label school_field_soccer_hangout_conv_general1:
    nate.name "Is getting the bus as bad as they say?"
    if robin_here() and numgen():
        robin.name "Those fuckers can't keep their hands off my arse."
        nate.name "That bad?"
        robin.name "Well, not really. Men trying to put their finger up my bum is pretty normal."
        nate.name "I know I wouldn't mind."
    elif player.preg_father_class == busgroper and player.preg_knows:
        pc "Ask the baby in my belly. Riding the bus is how it got there"
        nate.name "Oh wow..."
    elif player.isbroken:
        pc "Men using girls to get off?"
        nate.name "Err, do they?"
        pc "No different to anywhere else."
        pc "Men put their cock in me no matter where I am. Why would the bus be any different?"
        nate.name "..."
        if c.skirt and not c.pants:
            pc "I guess wearing a skirt with no pants kind of invites them though..."
            nate.name "Err... Great?"
    elif not player.check_nowill:
        pc "..."
        pc "Don't ask."
        nate.name "Right. Ok."
    elif player.has_perk(perk_slut):
        pc "Depends on what you mean by \"bad\"."
        nate.name "Well I hear..."
        pc "I know what you mean, but you are talking to me here."
        if numgen():
            nate.name "Err, and?"
            pc "Bad for some girls is good for me. I don't mind the hands."
            nate.name "Oh?"
            pc "Some entertainment for a boring journey."
            if rachel_here():
                rachel.name "They like to have a lot of fun with us. It's nice."
                if robin_here():
                    if "pc_know_want_bussex" in robin.list:
                        robin.name "You like it as well?"
                        nate.name "As well?"
                        robin.name "Errr, shush!"
                    else:
                        robin.name "Nice? You like it?"
                        rachel.name "Sure. You should see peoples face when you bend over for them"
                    pc "Maybe we should all go for a ride. Maybe the bus happy."
                    rachel.name "Haha right!"
        else:
            nate.name "Ah, so for you it's good?"
            pc "Better than just standing there suffering the smell."
            nate.name "Heh."
    elif player.check_sex_agree(3):
        pc "Hands everywhere? Might lose clothes?"
        nate.name "Err, so yes?"
        pc "That is just a normal ride. Sometimes it can get more pokey."
        if c.slutty and c.skirt and not c.pants:
            nate.name "And wearing something like that with no knickers?"
            pc "What about it?"
            nate.name "Err... Aren't you making it easy for poking to turn to... Err, poked?"
            pc "..."
            pc "I guess so."
        else:
            nate.name "Sounds like fun."
            pc "Yeah, say that next time when someone tries to put something up your arse."
    else:
        pc "It can be."
        nate.name "Oh?"
        pc "No \"oh\" you pervert. Get your kicks elsewhere."
        nate.name "Right."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_general2:
    drake.name "You ever hang out in the park?"
    if not loc_park.visited:
        pc "Not yet. Keep meaning to since it's not far from my house but never get round to it."
        drake.name "Ah."
        jump school_field_soccer_hangout_conv_end
    pc "Yeah. It's not far from my house. Why?"
    drake.name "Just wondering what it's like there."
    pc "You haven't been?"
    drake.name "I have, but hang out here almost all the time so not really seen what other places are like."
    pc "It's okay I guess. Though much safer to hang out here at night."
    drake.name "Oh?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_general3:
    drake.name "You been to the lake before?"
    pc "Why? Want to see me in my bikini?"
    if drake.sex:
        drake.name "Seen you in a lot less. Though wouldn't say no to the bikini."
    else:
        drake.name "Wouldn't say no."
    if not loc_beach_hangout.visited:
        pc "Well too bad anyway. Not really been there."
        drake.name "Ah."
    else:
        pc "Yeah I've been there. It's kinda nice to hang out there even if there are perverts everywhere."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_general4:
    nate.name "Happy to see us [name]?"
    pc "Err. Sure? What are you getting at?"
    nate.name "The twins there are looking at me."
    $ player.eye = 6
    pc "Ah? Didn't notice."
    $ player.face_neutral()
    nate.name "If you say so."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_general5:
    drake.name "Not that I am complaining. But kind of unusual to meet a girl these days who likes having fun."
    if robin_here() and numgen():
        if robin.isslut:
            robin.name "Got to get something fun out of life. And i like being bent over as much as the men bending me over."
            drake.name "Right..."
        elif "soccerboys_can_sex" in robin.list:
            robin.name "Think yourselves lucky. You lot are just hiding back here and the girls come to you."
            pc "I come for the beer."
            robin.name "Yeah, sure..."
        else:
            robin.name "I just play football. Nothing wrong with that."
            drake.name "And the tiny shorts that ride up your arse?"
            robin.name "What? They are easy to play in. And not like I have a wardrobe like [name] has."
    if player.isbroken:
        pc "It makes people happy. Not a lot else to enjoy these days. Why not do what people want from me?"
        drake.name "..."
    elif player.has_perk([perk_slut, perk_bimbo]):
        pc "Not much else to enjoy these days. Why not have a bit of fun."
        drake.name "Hmm, usually it's the guys that want to chase after everyone they see."
        pc "Yeah... Don't be so sure about that."
        if school_dance_quest_show_count > 3:
            pc "I'm guessing you haven't met [rachel.name] yet. She puts me to shame."
        drake.name "Oh?"
    elif all([drake.sex,nate.sex,dan.sex]):
        pc "Not a lot else to enjoy these days. Why not have some fun with you lot?"
        drake.name "Hmm, I guess I expected most girls to be less... Forward with the idea."
        pc "What can I say? Not like I am fucking you behind each others backs."
        if robin_here():
            robin.name "That would be fun to see you try and manage that."
    elif any([drake.sex,nate.sex,dan.sex]):
        pc "Drinking beer and a little extra? Nothing wrong with that."
        drake.name "Didn't say there was."
    else:
        pc "You lot are just perverts. All we do is play football. Not my fault you can't take your eyes off my arse."
        if robin_here():
            robin.name "So not just me then?"
            drake.name "Well, you both have nice arses."
        else:
            drake.name "Well, it is a nice arse."
        nate.name "Tits as well."
        pc "See? Perverts."
    jump school_field_soccer_hangout_conv_end








label school_field_soccer_hangout_conv_pub1:
    nate.name "So how's work at the pub?"
    if pub_waitress.timesworked < 5:
        pc "Seems ok, not worked many shifts there so who knows, but seems fine so far."
        nate.name "Give it time. When I was there it didn't seem like such an upstanding place."
        pc "Same could be said of anywhere in this city..."
        nate.name "True..."
    elif player.check_nowill():
        pc "Eh, let's not talk about that shithole..."
        nate.name "Hmm, sure..."
    elif pub_waitress.timesworked > 20:
        pc "Same as always. Full of perverts with wandering hands who tip more if you hang out with them."
        nate.name "Yeah, seemed pretty much like that when I was there. Waitresses tangled up with the customers for the tips."
        pc "Yeah, bet you liked that."
        nate.name "Think I have the money to keep one of them hanging around me?"
        pc "Hah, no chance."
    else:
        pc "Alright I guess. People there getting a bit handsy but need the tips so can't really say much."
        nate.name "More tips the more their hands wander?"
        pc "Pretty much..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub2:
    nate.name "So you wear one of those sexy dresses when you work at the pub?"
    pc "Of course. It's the uniform."
    drake.name "Sexy dresses?"
    nate.name "Yeah, low at the chest and high at the waist. All boobs and ass."
    drake.name "Oh nice. Wouldn't mind seeing that."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub3:
    if not c.outfit == 6:
        nate.name "So when you gonna flash your arse for us in your pub dress?"
        pc "Come to the pub to see that. Get you out of here at least."
        nate.name "No thanks. I'm happy here."
    else:
        nate.name "That the dress you wear at the pub?"
        pc "Yeah."
        nate.name "I can see why they ask you to wear it."
        pc "Yeah, I think we all know why."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub4:
    nate.name "When I was at your pub, there was one of the girls walking around with her tiny dress."
    pc "Yeah, it's the uniform I have to wear."
    nate.name "Is the underwear optional?"
    pc "Huh?"
    nate.name "The girl I was watching had nothing on underneath."
    pc "Ah, probably sold them to some pervert."
    nate.name "Oh... Really? Nice!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub5:
    nate.name "So..."
    pc "Hmmm?"
    nate.name "Do the girls in the pub charge for extra services?"
    if player.isbroken or player.has_perk(perk_whore, notif=True) or (school_soccer_love_check(40) and not player.check_nowill()):
        pc "It happens."
        nate.name "Oh?"
        nate.name "And you?"
        if player.isbroken or player.has_perk(perk_whore) or (school_soccer_love_check(60) and not player.check_nowill()):
            if pubpatron.sold == 1:
                pc "I gave it a go. Money wasn't bad but not sure..."
                $ school_soccer_quest_boys_know["whore"] = True
            elif pubpatron.sold:
                pc "Sure, there are worse ways to earn money. The pub is at least a safe place."
                $ school_soccer_quest_boys_know["whore"] = True
            elif not pubpatron.sold and (pubpatron.vsex or pubpatron.asex or pubpatron.hsex or pubpatron.osex):
                pc "For money? No. For fun though sure."
                if player.isslut:
                    $ school_soccer_quest_boys_know["slut"] = True
            elif pubpatron.rape:
                pc "Last time I was alone with one of those shits I ended up raped. Not in any hurry to spend more time with them."
                $ school_soccer_quest_boys_know["raped"] = True
            else:
                pc "Na, I can see the other girls doing that but it's not for me."
        else:
            drake.name "Oi!"
            pc "..."
            nate.name "Right... Sorry."
    else:
        pc "No idea what you are talking about."
        nate.name "I mean if..."
        pc "Haven't a clue."
        nate.name "Ah... Ok..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub6:
    nate.name "So, was thinking about popping by the pub at some point."
    pc "Ok. You don't need my permission."
    nate.name "Was wondering how much it would cost me to have you suck my cock."
    if not player.check_sex_agree(2):
        $ player.face_annoyed()
        pc "*Tsk* Idiot."
    elif nate.osex:
        pc "If we are talking money, how about you pay me for the last time I sucked your cock?"
        nate.name "Err..."
    else:
        pc "Like you could afford it."
        nate.name "How much?"
        pc "More than you will ever have."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub7:
    nate.name "So [name]. Would I get a friends discount at the pub?"
    pc "Maybe, I could probably sneak some free beer your way."
    nate.name "What about with one of the barmaids?"
    if all([drake.sex, nate.sex, dan.sex]):
        pc "Well, you are already fucking me for free. But if you want one of the other girls then it will cost you."
        if robin_here() and not "soccerboys_knows_pc_sex" in robin.list:
            robin.name "Wait what? Hold on, did I hear what I thought I did."
            pc "Ah..."
            robin.name "Oh wow."
            $ add_to_list(robin.list, "soccerboys_knows_pc_sex")
        elif drake.preg_knows or nate.preg_knows or dan.preg_knows:
            pc "Just be careful about sticking a baby into one of them. They might not be as accepting of it as I have."
    else:
        pc "Ah. On your own there I'm afraid."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub8:
    nate.name "So anyone ever paid you to do something with one of the other bargirls?"
    pc "..."
    nate.name "I know I wouldn't mind seeing it so others would as well."
    pc "What's with you lot and lesbians?"
    nate.name "It's HOT!"
    drake.name "Mmmmm..."
    dan.name "Yup."
    pc "*Sigh*"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub9:
    nate.name "So is it really worth it taking guys from the pub into the back room?"
    pc "Got any other ideas on how to buy food?"
    nate.name "Well, there are jobs out there that doesn't need you to?"
    pc "Yeah? Name one."
    $ randomnum = renpy.random.randint(0, 2)
    if randomnum == 1:
        nate.name "I have seen girls handing out fliers on the street."
        pc "Yeah, and how many guys are going to demand to see my tits before they accept a flier?"
    elif randomnum == 2:
        nate.name "The motel down the road has cleaners."
        pc "Yeah, until the boss makes me clean his room naked."
    else:
        nate.name "You got those folk who take odd jobs by the station."
        pc "That place? Think anyone is going to hire me for labour? Just asking to be raped and put in a shallow grave."
    nate.name "..."
    drake.name "Really is like that isn't it...?"
    pc "The pub is warm, safe and I get free booze so not too much to complain about."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_pub10:
    nate.name "So you and the other bargirls, have..."
    pc "Lesbians again?"
    nate.name "Yup."
    pc "Can you kiss one of those two for me?"
    nate.name "What?"
    pc "Go on. I want to see. A big old manly kiss on the lips! *MWAH*"
    nate.name "Ugh..."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_sis1:
    "Personal questions about you and emile. THis is mostly to give lore and background info and comments about your relationship with her."
    "There will probably be some info about what happened as you were coming to blaston or even about before the chaos"
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_sisjoke1:
    nate.name "So, your sister never going to join us for drinks?"
    pc "Probably not. Not sure hanging out with a bunch of guys in the bushes is quite her thing."
    nate.name "She would prefer to snuggle with her little sister instead eh?"
    pc "Ugh!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke2:
    nate.name "So, your sister cute?"
    pc "Cute? How old you think she is? Beautiful, yes. Not cute."
    nate.name "Whose tits are bigger? Yours or hers?"
    pc "Ugh!"
    if not numgen(0,10):
        if not player.breasts == 1:
            pc "Mine are..."
            nate.name "Oh?"
        else:
            pc "Hers..."
            nate.name "Oh?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke3:
    nate.name "So..."
    pc "Huh?"
    nate.name "What does she wear in bed with you?"
    pc "Pervert."
    nate.name "Well, yes. But that doesn't answer the question."
    pc "We sleep naked and spooning all night."
    nate.name "Really?"
    pc "No."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke4:
    nate.name "So..."
    nate.name "Ever fantasise about your sister?"
    pc "What kind of question is that?"
    nate.name "Well, same bed. Have a nice dream and she is just there. Maybe you want some help \"calming down\"."
    pc "I think you need to calm down somewhere."
    nate.name "Sure. Going to help me?"
    if player.check_sex_agree(5):
        if weather_var > 2:
            pc "In this weather, no thanks. Better the locker room."
            nate.name "Huh? Really?"
            nate.name "Ok, let's go!"
        else:
            pc "If you are so eager, I can."
            nate.name "Huh?"
            pc "..."
            nate.name "Err, okay let's go."
        menu:
            "Go with him":
                $ tempname = nate
                pause 0.5
                if weather_var >= 2:
                    $ walk(loc_school_locker_old)
                else:
                    $ walk(loc_bushes)
                jump school_field_soccer_sex_offer_cont_knees
            "Back out":
                $ player.face_happy()
                pc "Just messing with you. You are on your own."
                nate.name "Ugh!"
                jump school_field_soccer_hangout_conv_end
    pc "You should ask one of the guys. They might help you out."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke5:
    nate.name "Ever see you sister naked?"
    pc "Ugh. Yes I have and no I wasn't having sex with her at the time."
    nate.name "You like what you saw?"
    pc "Yes, she is very pretty."
    nate.name "Did you..."
    pc "No, I didn't want to fuck her."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke6:
    nate.name "Your sister into guys?"
    pc "Huh?"
    nate.name "Well, she sleeps with you. She ever invite someone round?"
    pc "Not sure actually. She has never really said."
    nate.name "Invite her to hang with us and we will find out."
    pc "Sure... Next time..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_sisjoke7:
    nate.name "Maybe she really is into girls."
    pc "Who?"
    nate.name "Your sister."
    pc "Considering the selection of men these days, it's more surprising to find out someone is into guys."
    nate.name "..."
    nate.name "True..."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_dance1:
    dan.name "How's dance?"
    if player.pregnancy >= 2:
        if drake.preg_knows or nate.preg_knows or dan.preg_knows:
            pc "It was nice. But since [player.preg_father_class.name] knocked me up I can't go anymore."
            dan.name "Ah..."
            jump school_field_soccer_hangout_conv_end
        else:
            pc "It was nice. But since I wound up pregnant I can't go anymore."
            dan.name "Ah..."
            jump school_field_soccer_hangout_conv_end
    else:
        pc "Quite fun actually. Didn't expect to like it but it's much more enjoyable than I thought it would be."
        dan.name "So you didn't dance before coming here?"
        pc "No, well... Outside of flailing around on a club dancefloor, no."
        dan.name "Heh, would have loved to see that."
        pc "Wasn't a good sight."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance2:
    dan.name "How's the girls in your dance group?"
    pc "They are nice. It's fun hanging out with a bunch of girls instead of you smelly lot."
    dan.name "If you have a problem with how I smell, how about you clean me up?"
    pc "Yeah, I am not your mother."
    dan.name "I don't remember my mother doing that for me."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance3:
    dan.name "You gonna invite any of your dance girls to hang out with us?"
    if drake.preg_knows or nate.preg_knows or dan.preg_knows:
        pc "One of us being pregnant is enough thank you."
        dan.name "I didn't mean..."
        pc "Yes you did."
        dan.name "Well. Not pregnant, just some flirting."
        pc "Yeah, that's how it started with me."
    else:
        pc "Why would I?"
        dan.name "So we can get to know them?"
        pc "If you want to go flirting on new girls then that's up to you to invite them."
        dan.name "Yeah, but you are already in with them. So easier if you do."
        pc "We will see..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance4:
    dan.name "Love the outfit you girls are dancing in?"
    pc "Yeah, you and every guy who sees it."
    dan.name "So you know?"
    pc "Know what?"
    dan.name "How revealing it is?"
    pc "You don't even need to look up the skirt to see my arse while I have it on. Of course I know."
    $ randomnum = renpy.random.randint(0, 10)
    if randomnum == 0:
        pc "It's basically the point..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance5:
    dan.name "How's dancing in the park?"
    if player.preg_knows and player.pregnancy >= 2:
        pc "Well, not been for a while since I am pregnant. But it was fine."
    else:
        pc "It's fine. Gets us some money."
    dan.name "Not worried about being out there in those clothes?"
    pc "Well, not really. There are a bunch of us so can't see anything bad happening."
    pc "Going home afterwards is a bit of a problem though..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance6:
    dan.name "Ever get trouble dancing in the park?"
    pc "Outside of wandering hands, not really. Most people behave."
    dan.name "Wandering hands common?"
    pc "Far too common."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance7:
    nate.name "That dance friend of yours, [dani.name]. She is sexy."
    pc "Ok. Good for her."
    if rachel_here() and robin_here() and all([nate.name in rachel.sex_who, nate.name in robin.sex_who]) and nate.sex:
        robin.name "Three girls here you are fucking and you are asking about more?"
        rachel.name "Can make it four girls."
        nate.name "Sure. I can still look and ask."
        pc "Pervert."
    elif rachel_here():
        rachel.name "Oooh, wanna fuck [dani.nname]?"
        nate.name "Err..."
        pc "It's [nate.name]. Is there anyone he doesn't want to fuck?"
        rachel.name "Haha!"
    else:
        nate.name "She single?"
        pc "All girls are single these days."
        nate.name "What do you mean?"
        pc "You seen the state of men since everything went to shit?"
        nate.name "Don't pay much attention to the men."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance8:
    nate.name "What about the \"big\" girl?"
    dan.name "Yeah, but she has a bitch face."
    nate.name "Would that matter when your face is pressed between her tits?"
    pc "Who you talking about?"
    nate.name "Your friend with the huge tits."
    pc "Cass?"
    nate.name "No, he blondie you dance with."
    pc "Ah, [anabel.name]. I would stay away from her if you want to keep your cock."
    nate.name "Oh?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance9:
    nate.name "That energetic girl you dance with. She the full ticket?"
    pc "I think so. She is just very optimistic."
    nate.name "If that's what you want to call it."
    pc "Why do you ask?"
    nate.name "Was thinking of talking to her."
    pc "Ah, well, good for you."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance10:
    nate.name "The other dance girls. They ever fuck for money as well?"
    pc "Why, looking to get some action?"
    nate.name "Yeah, like I can afford it. Just curious."
    pc "Well, that's up to you to find out from them."
    nate.name "Can't just go up to someone and ask them. Well, what if they say yes and I can't pay?"
    pc "Your problem, not mine."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance11:
    drake.name "So... That friend of yours you dance with."
    if "told_sex_" + drake.setname in rachel.conversation_topics:
        pc "[rachel.name]?"
        drake.name "Err, yea that one."
        pc "Hmmmm?"
        drake.name "Errmm..."
        drake.name "She told you?"
        pc "Of course."
        nate.name "Told what?"
        pc "[drake.name] got some action."
        nate.name "Oh nice!"
    else:
        pc "What one?"
        drake.name "[rachel.name]."
        pc "Ok. What about her?"
        drake.name "I fucked her."
        if player.isslut:
            pc "Ooh, about time I guess. She likes to mess about."
            drake.name "Mmm, that she does."
        else:
            pc "What? Really?"
            drake.name "Yeah. She..."
            pc "You can skip the details."
            if drake.sex:
                drake.name "You not mad?"
                pc "Why? Because you are fucking me too? No, it's fine."
                drake.name "Sure?"
                pc "I assumed you guys were fucking other girls anyway. And [rachel.name] is a bit of a slut so it's not unexpected."
    $ remove_from_list(drake.conversation_topics,rachel.setname)
    $ add_to_list(drake.conversation_topics, "told_sex_" + rachel._original_name)
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance12:
    nate.name "[name]!"
    pc "Yeah?"
    nate.name "I chatted to that slut friend of yours and I managed to fuck her."
    if "told_sex_" + nate.setname in rachel.conversation_topics:
        pc "Yeah she told me."
        nate.name "Oh?"
        pc "Girls also talk you know."
        nate.name "Right..."
        drake.name "Suprised you didn't scare her off."
        nate.name "Not sure it's possible to scare that one off."
    else:
        pc "Oh? Someone you didn't manage to scare off? Who was it?"
        nate.name "[rachel.name]. You have other slut friends?"
        if player.isslut:
            pc "Slutty girls stick together."
        else:
            pc "Wouldn't you like to know."
            nate.name "Well, yeah I would."
    $ remove_from_list(nate.conversation_topics,rachel._original_name)
    $ add_to_list(nate.conversation_topics, "told_sex_" + rachel._original_name)
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance13:
    dan.name "That dance friend of yours."
    if "told_sex_" + dan._original_name in rachel.conversation_topics:
        pc "I already know."
        dan.name "Oh? We ok?"
        pc "Yeah no worries. Have fun."
    else:
        if "told_sex_" + rachel._original_name in drake.conversation_topics or "told_sex_" + rachel._original_name in nate.conversation_topics:
            pc "You as well?"
            dan.name "Why so suprised?"
            pc "Didn't think you would put the effort into chasing her as well."
            dan.name "Well, I didn't. She came up to me."
            pc "Ah."
        else:
            pc "What one?"
            dan.name "[rachel.name]. She came up to me and was kind of flirting."
            pc "You fuck her?"
            dan.name "Huh?"
            pc "Don't be coy. I know what she's like."
            dan.name "Well, yeah. We had sex."
            pc "Good for you."
    $ remove_from_list(dan.conversation_topics,rachel._original_name)
    $ add_to_list(dan.conversation_topics, "told_sex_" + rachel.set_original_namename)
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance14:
    nate.name "Maybe we should invite [rachel.name] to hang out with us."
    drake.name "Mmm, would be fun."
    if all([drake.sex,nate.sex,dan.sex]):
        pc "Getting tired to fucking me already?"
        drake.name "No. But two girls are better than one."
        nate.name "Might see some lesbian stuff as well."
        drake.name "Oh right? That would be good to see."
    elif any([drake.sex,nate.sex,dan.sex]):
        pc "Already looking at other girls are you?"
        drake.name "Well, no harm in looking is there?"
        pc "Perverts."
    else:
        pc "Perverts. Not getting any action with me so want to invite other girls?"
        drake.name "Well, she offers something you don't."
        pc "Ugh..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance15:
    nate.name "That slut friend of [name]'s. We should have fun with her together."
    drake.name "Think she would go for that?"
    nate.name "Maybe. She is fucking everyone here already. Why not at the same time?"
    pc "Ugh, do you really need to talk about this with me here?"
    if all([drake.sex,nate.sex,dan.sex]):
        nate.name "Hmm, true. Everyone here has also fucked you. Should we be trying to gangbang you?"
        if player.isslut:
            pc "..."
            pc "I wouldn't complain if you tried..."
            nate.name "Oh?"
            drake.name "What?"
        else:
            pc "Ok, keep talking about [rachel.name]..."
            nate.name "Shame."
    else:
        nate.name "Well, ok."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_dance16:
    if player.preg_knows and player.preg_father_class == rachel.pregnant_who:
        $ player.face_angry()
        pc "[rachel.pregnant_who.name] you utter cunt. First you knock me up and now I hear [rachel.name] is pregnant from you as well."
        if not player.preg_father_class.preg_knows:
            rachel.pregnant_who.name "WHAT!?"
            rachel.pregnant_who.name "You and her? I didn't know either of you were pregnant."
            pc "Well, now you do. Knocked us both up."
            rachel.pregnant_who.name "Fuck! I need a beer."
            pc "You and me both!"
        else:
            rachel.pregnant_who.name "Err..."
            rachel.pregnant_who.name "Fuck..."
            pc "Don't fuck me. It's how we are in this mess to begin with!"
            rachel.pregnant_who.name "..."
            rachel.pregnant_who.name "I need a beer..."
            pc "You and me both!"
    else:
        pc "So [rachel.pregnant_who.name]~~"
        rachel.pregnant_who.name "Yeah? What's with that tone?"
        pc "Has someone been playing risky games?"
        if rachel.pregnant_who.sex:
            if not player.preg_knows:
                rachel.pregnant_who.name "Your pregnant?"
                pc "Not me. You managed to knock [rachel.name] up."
            else:
                rachel.pregnant_who.name "That's not mine is it?"
                pc "This one? No. But you managed to put one in [rachel.name]."
            rachel.pregnant_who.name "Oh? Shit!"
            pc "Heh. Have a beer."
        else:
            rachel.pregnant_who.name "Err..."
            pc "Hmmm?"
            rachel.pregnant_who.name "What have I done?"
            pc "You managed to knock up [rachel.name]. She didn't know how to tell you so asked for my help."
            rachel.pregnant_who.name "Fuck..."
    $ remove_from_list(rachel.pregnant_who.conversation_topics, "pregnant_" + rachel._original_name)
    jump school_field_soccer_hangout_conv_end







label school_field_soccer_hangout_conv_preg1:
    drake.name "Don't you girls have some kind of class that helps you protect against this sort of thing?"
    pc "What sort of thing?"
    drake.name "That fat belly of yours."
    pc "Ah."
    if player.rapebaby:
        pc "Rapists don't tend to use protecton..."
        drake.name "Oh..."
    else:
        pc "Well, hard to protect against this sort of thing when actual protection is forbidden."
        drake.name "Hmmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg2:
    nate.name "So how did you manage to get knocked up anyway?"
    if player.rapebaby:
        pc "Wasn't by choice. Let's leave it at that."
        nate.name "Oh..."
    else:
        pc "Well, you see."
        pc "When a girl touches a boys pee pee, it becomes hard."
        nate.name "Smartarse!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg3:
    nate.name "Is it me or have your tits gotten massive since you got knocked up?"
    drake.name "*COUGH*"
    if c.clevage:
        nate.name "Well look at 'em. Hard to miss with that top she's wearing. They are pretty much bursting out."
    elif not c.bra:
        nate.name "Well look at 'em. She's not wearing a bra and the things are bouncing around all over the place."
    else:
        nate.name "C'mon. Hard to miss 'em. They are almost as big as her head."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg4:
    drake.name "Surprised you managed to waddle your way over here."
    pc "Took 3 breaks on my perilous journey to get here. Was moments when I thought I wouldn't make it."
    drake.name "Har har!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg5:
    drake.name "You okay to be drinking some beer?"
    pc "Why not?"
    drake.name "Isn't it bad for the baby?"
    pc "That's someone else's problem."
    drake.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg6:
    robin.name "How's it feel [name]?"
    pc "Huh? What feel?"
    robin.name "Being pregnant."
    pc "Like I ate a horse. Bloated and can barely move properly."
    pc "Why? You're not pregnant are you?"
    robin.name "No. But is probably just a matter of time..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg7:
    robin.name "That your first one [name]?"
    pc "Yeah..."
    robin.name "It gets easier."
    pc "It does? Could have fooled me."
    robin.name "Well, it doesn't. You just get more used to it."
    pc "It's the part where I get rid of it that I'm worried about."
    robin.name "Yeah, it's rough..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg8:
    pc "Ugh. The beast in my belly is about overstaying it's welcome."
    robin.name "Hah, I can imagine."
    pc "I swear it's doing king-fu in there."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin1:
    nate.name "So how'd you wind up with that in your belly?"
    if robin.pregnant_who in [nate, drake, dan]:
        robin.name "One of you lot probably. The timing seems about right."
        nate.name "Oh? Someone didn't pull out?"
        robin.name "Guess so..."
        if player.preg_father_class in [nate, drake, dan] and player.preg_knows:
            pc "Not happy knocking me up, you get her as well?"
            robin.name "Should poison their beer in revenge."
    elif robin.pregnant_who == lover:
        robin.name "Guess someone I had a bit too much fun with managed to put it there."
        nate.name "Lucky him."
        robin.name "Yeah. Still me who has to carry it round with me though."
    elif robin.pregnant_who == rapist:
        robin.name "Some fuckhead forced me. Let's not talk about it."
    elif robin.pregnant_who == punter:
        robin.name "Some customer probably. Not sure..."
        nate.name "Oh. Thought you would avoid that sort of thing?"
        robin.name "How? No prtection anymore. No one would use it anyway. Guess it was only a matter of time."
    elif robin.pregnant_who == highpayer:
        robin.name "Some people have way more money than sense."
        nate.name "Oh?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin2:
    drake.name "So no more running round with that in your belly I guess?"
    robin.name "It's the worst part. Can't even play anymore."
    nate.name "Bet the guys at the beach are disappointed you aren't showing your arse off round there anymore."
    robin.name "I still go there to hang out when the weather's nice. Just can't play volleyball anymore."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin3:
    nate.name "Aren't you supposed to avoid getting a belly like that?"
    robin.name "Only so much trying you can do when not allowed to use protection."
    nate.name "Take it in the arse?"
    if robin.pregnant_who == rapist:
        robin.name "I doubt the guy who raped me would have listened even if I asked."
        nate.name "Oh..."
    else:
        robin.name "Not as fun. Plus hard to keep the right mind in the heat of the moment."
        nate.name "Mmm, tell me about it."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin4:
    nate.name "Trying to decide if you are hotter with or without the big belly."
    robin.name "And why are you telling me that?"
    nate.name "No reason."
    dan.name "With."
    pc "Oh? Something to tell us?"
    dan.name "Nope."
    pc "Mmmm... Perverts the lot of you."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin_pc1:
    nate.name "I swear almost all the girls round here are preggo."
    pc "It happens."
    nate.name "No it doesn't. It doesn't just jump on you."
    robin.name "Expect everyone round here to just lock up at home with their legs closed?"
    pc "Life is shit enough. Got to find some entertainment to make things better."
    nate.name "Even if that means both of you standing here with fat bellies."
    robin.name "At least we don't have to look after them afterwards. Can't imagine myself being a single mother."
    pc "Hah!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_robin_pc2:
    nate.name "Gotta say. It's kinda hot that you are both standing there with one of our babies in each of you."
    pc "You know. With [robin.name] here, it would be so much easier to hide your body."
    robin.name "And it will be fun doing the murder as well."
    drake.name "You two fatties couldn't hide the body even if you had a week."
    pc "Uhhh..."
    robin.name "Coming from [nate.name]'s mouth I expect, but from you?"
    drake.name "Is kinda hot though."
    robin.name "Ugh. Your lucky there beer here is free."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_boysintro:
    $ add_to_list(player.preg_father_class.conversation_topics, "told_pregnant")
    pc "So..."
    if player.pregnancy >= 2:
        pc "As you can probably guess, I am pregnant"
    else:
        pc "I took a test and I am pregnant."
    pc "Care to guess who the father is [player.preg_father_class.name]?"
    if player.preg_father_class.name == drake.name:
        drake.name "Why are you asking... Fuck..."
        drake.name "Really?"
        pc "Yup."
        drake.name "..."
    elif player.preg_father_class.name == dan.name:
        dan.name "Wait what? Me?"
        pc "Yes, you."
        dan.name "..."
    else:
        nate.name "Me have a guess?"
        if school_soccer_quest_boys_know["whore"]:
            nate.name "How am I supposed to know? Some guy paid you to take it in you?"
            nate.name "An accident with one of them?"
            nate.name "An orgy maybe?"
            pc "Idiot. It was you."
            nate.name "Me what? I never paid you."
            pc "No you didn't. But you still fucked me and came inside. Now I am carrying your baby."
            nate.name "Oh it was me?"
        elif school_soccer_quest_boys_know["slut"]:
            nate.name "How am I supposed to know? You have fucked pretty much any guy who looked your way."
            nate.name "Could be almost anyone."
            pc "*Sigh* And I also fucked you."
            nate.name "Yeah, so almost anyone."
            pc "Except it was you."
            nate.name "Me what?"
            pc "Ugh you idiot. It was you who got me pregnant!"
            pc "Dumbarse."
            nate.name "Wait what? Me. I am the father?"
        else:
            nate.name "Dunno. I don't follow you around checking who you fucked."
            pc "Maybe not. But there is someone you do know who I fucked."
            $ dialouge = "Well, I've fucked you"
            if drake.vsex and dan.vsex:
                $ dialouge = dialouge + " and those two have also had a go on you."
            elif drake.vsex:
                $ dialouge = dialouge + " and [drake.name] has also had a go on you."
            elif dan.vsex:
                $ dialouge = dialouge + " and [dan.name] has also had a go on you."
            else:
                $ dialouge = dialouge + " but no idea who else you might have had a go with."
            nate.name "[dialouge]"
            pc "And when you fucked me, did you pull out?"
            nate.name "Dunno, don't remember."
            pc "You fucking idiot [nate.name]. It was you who knocked me up!"
            nate.name "Me???"
        pc "Yes, you."
        nate.name "Oh wow. I knocked you up. Ha."
        pc "\"Ha\"?"
        nate.name "Well, yeah. Means I'll at least have some kid of mine running around somewhere."
        pc "Yeah, after I carry it around for 3 seasons for you."
        if school_soccer_quest_boys_know["whore"]:
            nate.name "Well, you are a whore so someone was going to knock you up. Better it's me than one 'o those people."
            drake.name "Fuck [nate.name]. That's out of order."
            pc "It's fine. He's right. Was going to happen anyway and better someone I like than some random shit."
        elif school_soccer_quest_boys_know["slut"]:
            nate.name "Well, you are a slut so someone was going to knock you up. Better it's me than one 'o those people."
            drake.name "Fuck [nate.name]. That's out of order."
            pc "It's fine. He's right. Was going to happen anyway and better someone I like than some one nighter."
        else:
            nate.name "Well, sorry. But still happy it's mine and not someone else's."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_drake_1:
    drake.name "So, is there anything I can do?"
    pc "Huh, more beer if you're offering."
    drake.name "I mean with the... Y'know."
    pc "The baby growing inside me?"
    drake.name "Yeah."
    pc "You could un fuck me. Might work."
    drake.name "Hmm, not sure I can do that."
    drake.name "On the plus side, I can fuck you normally without making things worse."
    pc "Wow. Coming from [nate.name] I wouldn't bat an eye. But you saying that?"
    drake.name "Yeah, that was a very [nate.name] think to say."
    pc "You arse."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_drake_2:
    drake.name "So, are we good?"
    pc "Huh, where did that come from? Why wouldn't we be?"
    drake.name "Because of the... Situation."
    pc "Since when were you all coy? We had sex and I got pregnant. Not like you forced me or anything so it happens."
    drake.name "Yeah, but. Dunno. I feel a bit guilty."
    pc "Chocolates and beer will solve everything."
    drake.name "Chocolate? Yeah fucking right. I'm gonna have to knock you up another ten times before I hand out chocolate."
    drake.name "Not seen that stuff for ages."
    pc "Then beer it is."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_drake_3:
    drake.name "Everything ok?"
    if player.pregnancy == 3:
        pc "Yeah, not far off being ready to pop. Be glad when it's all over."
    elif player.pregnancy == 2:
        pc "Yeah, getting all bloated but otherwise everything is ok."
    else:
        pc "Yeah I am fine. Still a while to go before I get all huge."
    drake.name "Hmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_nate_1:
    drake.name "So, knocked up by [nate.name]?"
    pc "Yeah..."
    if nate.vvirgin:
        pc "Wouldn't be so bad if he hadn't also been my first."
        nate.name "Double whammy!"
        pc "Ugh..."
    elif player.iswhore:
        pc "Not so bad though. I guess someone who was paying me would get the job done instead."
        pc "Better [nate.name] than some random punter."
    elif player.isslut:
        pc "Though to be fair, been with a decent amount of guys so was probably going to happen anyway."
        pc "[nate.name] might be an arse, but he's alright."
    else:
        pc "Of all things for him to actually get right he does this..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_nate_2:
    nate.name "So, how's ma boy doing?"
    pc "Your boy?"
    nate.name "The little one in your belly."
    if player.drunk > 60:
        pc "Probably drunk as shit and partying right now."
        nate.name "Party on!"
    else:
        pc "Probably fine. What does it matter. Neither of us are gonna see him."
        nate.name "Maybe not. But he exists."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_nate_3:
    nate.name "So, when that one pops out, wanna go for another one?"
    pc "Yeah fucking right!"
    nate.name "C'mon, we can keep poppin' them out."
    pc "You hit your head or something? Why would I want that?"
    nate.name "Why stop now?"
    pc "Ugh!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_nate_4:
    dan.name "Just to let you know."
    pc "Huh?"
    dan.name "If suddenly you \"find\" [nate.name]'s corpse, I'll help bury it no questions asked."
    nate.name "Thanks a lot!"
    pc "Good to know."
    pc "Better be careful [nate.name]!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_dan_1:
    dan.name "..."
    pc "What? That's the third time you have tried to say something to be but stopped."
    dan.name "I should probably say something about the pregnancy but I haven't a clue what to say."
    pc "So don't say anything and just go get me a beer."
    dan.name "Hmmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_dan_2:
    pc "Ugh, do I need to be comforting you or something? You have been all sullen for a while."
    dan.name "..."
    pc "Look, it happens. Do I need to send you to women's class or something?"
    pc "When a boy and a girl do the naked tango, sometimes pregnancy can occur."
    dan.name "..."
    pc "Don't make me kick you in the ass. It's me who's going to get all fat and milky."
    dan.name "What? Milky?"
    pc "Oh yes. These things in front of me are not just \"boingy boingies\". They carry milk as well."
    dan.name "Wha... I know that."
    pc "Although without a baby to suckle on them, they won't start producing."
    dan.name "Err..."
    pc "They will still hurt a bit though..."
    dan.name "Okay ok. This is the opposite of comforting."
    pc "I know. But it's more fun to tease you."
    dan.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg_dan_3:
    dan.name "Is there something... I dunno. That I can do."
    pc "Err, get me beer? Foot massage? Hitman to kill the person who knocked me up? Chocolate?"
    dan.name "Errm..."
    pc "Maybe forget the Chocolate."
    dan.name "I can do the beer."
    pc "No hitman? Ok, beer will do until I find one."
    dan.name "Right..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg1_notboys:
    $ add_to_list(school_soccer_quest.list, "preg1")
    nate.name "So who was the lucky guy?"
    pc "Huh?"
    nate.name "Who got to put a baby in your belly?"
    if player.preg_father_class in [shane, marcus]:
        pc "Ugh, those shitty cretins did it..."
        nate.name "Oh..."
    elif player.rapebaby:
        pc "Ugh, some shit forced himself on me and left it behind. Rather not talk about it."
        nate.name "Oh..."
    elif player.preg_father_class == pubpatron:
        pc "Ah, someone at the pub did this."
        nate.name "Oh? That a service the pub provides."
        if "shit drunk" in player.father:
            pc "When you get your server shit drunk, it can happen."
            nate.name "Oh? I'll have to remember that."
        elif "it cost him" in player.father:
            pc "Depends how much you pay."
            nate.name "Oh. And how much did he have to pay to have you carry that?"
            pc "Don't ask..."
        else:
            pc "Well, here I stand as big as a cow. So I guess so."
    elif player.soldbaby:
        pc "Ah, I was stupid and let some customer leave it behind..."
        nate.name "Oh? Providing extra services there."
        pc "Yeah. Pro whore and all..."
    else:
        pc "Ah. Well... I think I got a bit carried away."
        nate.name "Or just doing a good job."
        pc "A good job?"
        nate.name "Yeah, everyone seems to want to stick their kids in some girl these days."
        pc "Ah, yeah. Told us about that in class."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_preg2_notboys:
    $ add_to_list(school_soccer_quest.list, "preg2")
    nate.name "Preggo again. Starting to make it a habit."
    pc "Yeah, can't stop spitting them out."
    nate.name "Looks that way."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_allure1:
    nate.name "I'm surprised with the way you dress."
    pc "Got a problem with it?"
    nate.name "Not at all. Just would have thought with the types of people going round these days, you wouldn't want to draw attention to yourself."
    if player.has_perk(perk_exhibitionist):
        if all([drake.seen_all, nate.seen_all, dan.seen_all]):
            pc "You guys know me, I like to show off. No matter if it's you perverts or some other deviants out there."
        else:
            pc "I like showing off so I don't care. Let them look."
    elif player.isbroken:
        pc "Had worse happen than they could ever do. So I just wear what makes me happy."
        nate.name "Err, ok..."
    elif player.iswhore or player.isslut:
        pc "I like the attention. Even if some of it is from the wrong type of people."
        nate.name "Oh?"
    elif player.check_sex_agree(3):
        pc "I don't mind. Not going to change what I like because there are shitty people out there."
        nate.name "Ok, well. Good I suppose."
    elif player.rape:
        pc "Yeah, had run ins with those types before and it didn't end well. But I don't want to change what I like because of shitty people."
        nate.name "Oh..."
        $ school_soccer_quest_boys_know["raped"]
    else:
        pc "Yeah have to be careful. But this is what makes me happy and I am not going to change that."
        nate.name "Ok."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure2:
    nate.name "So, you jiggle those tits for all the boys or are we just special?"
    pc "What you talking about you pervert?"
    nate.name "Low cut top and no bra so they bounce around. I would complain they are distracting but I don't mind looking."
    if player.check_sex_agree(3) and player.check_horny() and not numgen(0,10):
        pc "..."
        $ pc_strip_upper(temp=True)
        pc "I don't mind ♥"
        nate.name "Fuck!"
        drake.name "Damn!"
        dan.name "Wow..."
        $ pc_dress()
    else:
        pc "Then keep to looking and less talking."
        nate.name "No problem there jiggle tits."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure3:
    nate.name "You have a nice ass [name]."
    if c.cansee_ass:
        pc "Pervert."
        nate.name "You're the one flashing your arse about."
    elif player.check_sex_agree(2):
        pc "Err, thanks?"
        nate.name "Nice tits too, but with what you are wearing it's nicer to looks at your arse."
        pc "Ok, if you say so."
    else:
        pc "What kind of way to start a conversation is that?"
        nate.name "A bad way probably. But with what you are wearing it is hard to think of much else."
        pc "*Sigh*"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure4:
    nate.name "So [name]. You lose your knickers on the way here or something?"
    drake.name "*COUGH* What?"
    nate.name "She doesn't have any underwear on."
    pc "And how would you know that?"
    nate.name "I... Saw..."
    pc "Pervert!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure5:
    nate.name "Not that I am judging, but aren't you dressed a bit... Whore like?"
    if player.check_sex_agree(4):
        if player.iswhore and school_soccer_love_check(60):
            pc "Yup, and?"
            nate.name "You don't see a problem in that?"
            pc "In what? A whore looking like a whore?"
            nate.name "*COUGH*"
            $ school_soccer_quest_boys_know["whore"] = True
        else:
            pc "And?"
            nate.name "And..."
            pc "Mmmm?"

        nate.name "Errr..."
        drake.name "Dug your own grave here mate."
        nate.name "Err, drink?"
    else:
        pc "Someone here is looking more punchable like."
        nate.name "Yup, sorry."
        nate.name "Here, beer."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure6:
    nate.name "I like what you are wearing [name]. It's very..."
    pc "Choose your next words carefully."
    nate.name "Err, I was just going to say it makes you look attractive."
    pc "Mmm, thank you."
    drake.name "Idiot."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure7:
    nate.name "I like what you are wearing [name]. It's very..."
    pc "Yes..."
    nate.name "You look nice. I wasn't thinking anything weird."
    if c.clevage:
        pc "I might be convinced of that if you could take your eyes off my chest."
    elif c.ass:
        pc "I might be convinced of that if you wasn't looking at my arse every chance you get."
    else:
        pc "Wipe the drool off your mouth before you give yourself away even more."
    nate.name "Err..."
    drake.name "Idiot."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure8:
    nate.name "You are looking good [name]."
    pc "Ok, I'll take the compliment."
    pc "You're still an idiot though."
    nate.name "What? Why?"
    pc "Because you are a pervert."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure9:
    pc "What are you looking at?"
    nate.name "Err, you? I like what you are wearing."
    pc "Yes?"
    nate.name "..."
    nate.name "I..."
    nate.name "Yeah, I got nothing that won't be digging my grave any deeper."
    pc "Silence, good choice."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure10:
    nate.name "[name]."
    pc "Yeah?"
    nate.name "I..."
    nate.name "Want to take you in the bushes and make you scream..."
    pc "..."
    if player.check_sex_agree(5):
        if weather_var > 2:
            pc "In this weather, no thanks. Better the locker room."
            nate.name "Huh? Really?"
            nate.name "Ok, let's go!"
        else:

            pc "Ok, so what's stopping you?"
            nate.name "Huh?"
            pc "..."
            nate.name "Err, okay let's go."
        menu:
            "Go with him":
                $ tempname = nate
                $ npc_race_picker(nate)
                pause 0.5
                if weather_var >= 2:
                    $ walk(loc_school_locker_old)
                else:
                    $ walk(loc_bushes)
                jump school_field_soccer_sex_offer_cont_knees
            "Back out":
                $ player.face_happy()
                pc "Just messing with you. You are on your own."
                nate.name "Ugh!"
                jump school_field_soccer_hangout_conv_end
    drake.name "Err..."
    dan.name "Ha!"
    nate.name "Beer?"
    if player.isslut:
        pc "Sure. But you are going to the bushes alone."
    else:
        pc "Idiot!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_allure11:
    nate.name "You are looking nice [name]."
    pc "..."
    pc "Not sure if I should accept the compliment or call you an idiot."
    drake.name "Idiot."
    dan.name "Definitely."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_whore1:
    dan.name "Is selling yourself worth it?"
    pc "Depends on what you mean by \"worth it\". Not like I am going to get much work any other way round here."
    dan.name "No? I see a lot of girls working and doesn't seem like they are doing that."
    pc "Doesn't \"seem\"."
    pc "There are no nightclub hookups, tinder, or any of the other ways people met before. Guys are desperate and horny. Doesn't matter what job you work now, someone will ask to fuck you for money."
    dan.name "Really?"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore2:
    nate.name "When you sell yourself, do you enjoy it?"
    pc "Depends on the guy I guess."
    if player.isbroken:
        pc "Some people are gentle and some beat you. Just have to deal with whatever comes."
        pc "All that matters is the guy fucking me enjoys it."
    elif player.has_perk(perk_slut):
        pc "But I like money and I like sex. So if the guy is okay then sure."
    else:
        pc "Not like it's something I entirely want to do. But the money is better than most other things I can do."
    nate.name "Hmmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore3:
    nate.name "What got you into selling yourself?"
    pc "I am pretty sure I can answer for every girl, and boy for that matter. Money."
    nate.name "Well, sure. But not like everyone is capable of doing it."
    pc "Everywhere you go, guys offer you money for it regardless of if you are a whore or not. And considering most people struggle to even eat..."
    pc "At some point you just think \"What's the harm this one time? I need the money\"."
    pc "Gets easier each time after that until you just don't think about it anymore."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore4:
    dan.name "Is it dangerous to sell yourself?"
    pc "Oddly enough, no."
    pc "Men are docile when you are pleasuring them. And after they are done, they are like puppies."
    pc "The ones to be careful of are those who can't afford to pay. They might try and take by force..."
    pc "But that can happen to anyone and not just whores. Every girl has to be careful of these shits."
    dan.name "Oh..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore5:
    dan.name "Do people still pay to have fun with you even when pregnant?"
    pc "Of course. Most are willing to pay more."
    dan.name "Really? Why would they pay more?"
    pc "Because \"I am a dumb slut who was stupid enough to go raw and get pregnant\"."
    dan.name "Huh?"
    pc "If I let a guy knock me up, they think I am okay with anything."
    pc "Either that or they have a pregnancy fetish."
    dan.name "Ok..."
    dan.name "I'll take your word for it."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_whore_robin1:
    nate.name "You ever make money on the side as well [robin.name]?"
    robin.name "What do you mean \"on the side\"?"
    nate.name "You know... The way girls can these days..."
    if not robin.sold:
        robin.name "Ugh. Money is hard to come by, but not done that yet."
        nate.name "Yet?"
        robin.name "..."
        drake.name "Anyway... How work been [name]?"
        pc "Good. Very good!"
    elif robin.sold == 1:
        robin.name "Ugh... Don't remind me."
        nate.name "Oh?"
        robin.name "I'm broke and some pervert just threw a load of money at me..."
        robin.name "Can't really say no when it pays rent for a few weeks..."
    else:
        robin.name "Rather that than homeless..."
        robin.name "Not like people are lining up to give me a job."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore_robin2:
    robin.name "It worth it making money like that [name]?"
    pc "Interested?"
    robin.name "Not really. Just curious about it."
    pc "It's worth it probably. Dignity doesn't pay the rent."
    pc "And I suppose once you get used to it, you can actually have fun with it all."
    robin.name "Really?"
    pc "Mmm. The people willing to pay for it aren't going to kick your arse in an alleyway. No need when money does the job."
    robin.name "Right..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_whore_robin3:
    nate.name "So when we gonna see you two down the highway?"
    pc "Like you could afford us."
    nate.name "Well, yeah. Still sounds like fun though."
    pc "Me and [robin.name] selling ourselves sounds like fun to you?"
    nate.name "Well, yeah?"
    robin.name "Pervert!"
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_haven0:
    dan.name "I had to go past that shithole the other day."
    drake.name "What? [haven]?"
    dan.name "Yeah. I do not like going past that way."
    drake.name "Tough guy like you and that place is scaring you off."
    dan.name "Don't joke, that place is a mess."
    if main_quest_05.active == 2:
        pc "Yup, best avoid it if you can."
        dan.name "You know the place?"
        pc "Yeah... Lived there for a bit..."
        dan.name "Oh..."
        pc "Yeah..."
        $ school_soccer_quest_boys_know["haven"] = 1
    else:
        drake.name "Ok... If you say so."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_haven1:
    $ school_soccer_quest_boys_know["haven"] += 1
    dan.name "Why were you in [haven] anyway [name]?"
    pc "Ugh, I had to go there... For reasons..."
    dan.name "Ok..."
    pc "Not really my choice."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_haven2:
    $ school_soccer_quest_boys_know["haven"] += 1
    dan.name "You meet [havenvik.name] while you were in there?"
    if havenvik.has_met:
        pc "The beer guy? Yeah."
        dan.name "He is who we get most of this knock off booze from."
        pc "Really? I remember his stuff being a lot strong than this."
        dan.name "Yeah, that stuff is for [haven]. The ones we get are what he sells outside of [haven]. A bit smoother and we water it down to get rid of that nasty kick."
        pc "Can still feel that kick even now..."
    else:
        pc "Doesn't ring a bell. I wasn't in there that long so didn't really meet many of the locals."
        dan.name "Ah ok. Not staying long is for the best."
        pc "Yeah."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_haven3:
    $ school_soccer_quest_boys_know["haven"] += 1
    dan.name "Did you sleep in [haven] or did you find somewhere else to bed down?"
    pc "Slept there..."
    dan.name "Ugh. Sleep with a shank?"
    pc "No, I didn't have anything like that. I just tried to bed down when the other girls were there so nothing would happen."
    if havenpsleeper.vsex or havenpsleepergang.vsex or havenpsleeperforce.vsex:
        $ player.face_meek()
        pc "Didn't always work though..."
        dan.name "Oh..."
        $ school_soccer_quest_boys_know["raped"] = True
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_haven4:
    $ school_soccer_quest_boys_know["haven"] += 1
    dan.name "It true they have a communal shower in [haven]?"
    pc "Yeah. Some little alcoves but most are in the open so not much privacy."
    dan.name "Wondered why those lot never really stunk as much as you would expect them to."
    pc "Yeah, seems hygiene is pretty important there."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_haven5:
    $ school_soccer_quest_boys_know["haven"] += 1
    nate.name "So is [haven] really as bad as [dan.name] makes it out to be [name]?"
    pc "..."
    if player.isbroken:
        $ school_soccer_quest_boys_know["raped"] = True
        $ school_soccer_quest_boys_know["slave"] = 1
        pc "I was beaten to shit, kidnapped, sold as a sex slave and raped daily for 2 seasons because of that place."
        pc "It sound like a good place to be to you?"
        nate.name "Shit... Sorry. I didn't know..."
        pc "..."
        pc "I know. It's fine."
    elif "jumped_window" in main_quest_05.list:
        pc "I left that place with more of my blood on the outside of me than on the inside."
        pc "You be the judge of if that sounds like a nice place."
        nate.name "Fuck. Ouch. That hospital must love you."
        pc "Yeah, they can't get rid of me."
    elif main_quest_05.rape >= 10:
        $ school_soccer_quest_boys_know["raped"] = True
        pc "Can't count the amount of times someone forced themselves on me, so you decide if that sounds like fun."
    elif main_quest_05.rape:
        $ school_soccer_quest_boys_know["raped"] = True
        pc "If getting raped sounds like a nice time to you, then go right ahead and check the place out."
    else:
        pc "I wasn't there for too long and tried to keep my head down. But the place is a fucking dangerous shithole."
        pc "It is worse than what [dan.name] is making it out to be."

    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_slave1:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "So how are you feeling?"
    pc "Huh. Odd question out of the blue."
    drake.name "I mean after your time... You know... In that place..."
    pc "You can say it you know. My time as a sex slave."
    drake.name "Sorry. I just don't want to hit a sensitive spot or something."
    pc "It's ok. It's in the past and it's over. You don't ever get over such things but of you confront them at least they can't hurt you anymore."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_slave2:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "So everything is okay about... Being a slave... Nothing we should be aware of?"
    pc "What would there be to be aware of?"
    drake.name "No idea. It's why I am asking."
    pc "No, it's fine. I'm not going to suddenly murder you because you said the wrong word."
    $ player.eye = 2
    pc "[nate.name] on the other hand. Any excuse will do..."
    nate.name "Oi!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_slave3:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "How did you manage to get out of being a slave?"
    pc "There is no \"getting out of\" it. I would have been there until some punter beat me to death or something."
    pc "I don't remember it because I was completely out of it. But there was a raid and I was freed."
    pc "Only really found out about what happened while recovering in the hospital."
    drake.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_slave4:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "So everything is okay now after your rescue?"
    pc "Not in the slightest. But no choice but to make do."
    drake.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_slave5:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "Did you see anyone after you were freed?"
    pc "See anyone?"
    drake.name "Yeah, to talk to I mean."
    pc "Ah yeah. I was kept in the hospital for a while. I was out of it and heavily pregnant so they wouldn't let me out since they thought I would jump in the lake or something."
    pc "Had to see their therapist daily. [emile.name] also visited a lot and checked in on me."
    drake.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_slave6:
    $ school_soccer_quest_boys_know["slave"] += 1
    drake.name "The therapist help you get through things?"
    pc "I guess. Or [emile.name]... Maybe just being out of that place."
    pc "Either way, yeah. Let me get my mind back in the real world and not in that cell. Not gonna be jumping in the lake any time soon anyway."
    pc "Well, that's not true. The lake is nice to swim in."
    nate.name "You have a bikini?"
    $ player.eye = 2
    pc "Way to add class to the conversation [nate.name]."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_bully1:
    drake.name "No idea why you let those shits mess with you."
    pc "Then who else are they going to push around."
    drake.name "What do you care?"
    pc "..."
    pc "Dunno. Maybe I shouldn't."
    drake.name "Giving a shit will put you in more trouble than it's worth."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_bully2:
    nate.name "Saw those shits messing with one of the girls earlier."
    drake.name "Those two mouth breathers?"
    nate.name "Yeah."
    drake.name "They ever make you do things to them [name]?"
    $ player.face_worried()
    $ dialouge = WeightedChoice([
    ("Luckily no. They just call me names when they pass or say other mean things. Maybe hit me now and then...", 1),
    ("Like forcing me somewhere alone and wanking them off?", If(any([shane.hsex,marcus.hsex]),10,0)),
    ("Like dragging me off somewhere isolated and making me suck them off?", If(any([shane.osex,marcus.osex]),10,0)),
    ("Yeah... The shit's caught me alone and make me fuck them...", If(any([shane.vsex,marcus.vsex]),50,0)),
    ("*Tsk* Ended up getting ass fucked...", If(any([shane.asex,marcus.asex]),50,0)),
    ("Wound up losing my viginity cos of those shits...", If(any([shane.vvirgin,marcus.vvirgin]),100,0)),
    ("Most of the school has heard already... Forced me alone and they got a bunch of guys to fuck me...", If(shanewhore.sex,150,0)),
    ("You mean like rape and get me pregnant?", If(any([shane.preg, marcus.preg]),100,0)),
    ("This belly I have is because of them. Raped me and put this in me...", If(any([shane.preg_current, marcus.preg_current]),300,0)),
    ])
    pc "[dialouge]"
    if rachel_here():
        rachel.name "I can't walk anywhere with them around without them wanthing to do things."
        nate.name "Things?"
        rachel.name "Usually I suck their dick. But sometimes they fuck me or have friends fuck me."
    drake.name "Ugh..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo1:
    nate.name "Saw you on a flier trying to get people to come here."
    pc "Ah, you saw that?"
    nate.name "Yeah. What's the deal with it?"
    pc "The head trying to attract more young people to come here instead of hanging out on the streets."
    nate.name "But why you?"
    if player.isslut or player.iswhore:
        pc "Tempt in the perverts I guess."
    else:
        pc "A smiling girl will attract more people I guess."
    nate.name "Oh?"
    jump school_field_soccer_hangout_conv_end



label school_field_soccer_hangout_conv_photo2:
    nate.name "So. Taking pictures of you in your dance gear. Flashing in the park not enough?"
    pc "They both pay and not like I have to choose one or the other."
    nate.name "Not afraid of getting a reputation?"
    $ dialouge = WeightedChoice([
    ("Prefer to not starve. Plus not like most people round here are all pure.", 1),
    ("Like being a whore hasn't already gave me enough of a reputation?", If(player.iswhore,100,0)),
    ("Like I don't already have one of those. Everyone here already thinks I am a slut.", If(player.isslut,100,0)),
    ("If it makes men happy, what do I care?", If(player.isbroken,100,0)),
    ])
    pc "[dialouge]"
    nate.name "Hmmm..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo3:
    drake.name "You seem to be losing more and more of that dance outfit you have."
    pc "What do you mean?"
    drake.name "Saw the recent pictures. Pretty serious underboob and tiny pants on."
    nate.name "Yeah, they were great. Be good to see you without the pants though."
    if nate.sex:
        pc "You have seen me enough without my pants already."
        nate.name "Yeah, but I can't take a photo of you and wank over it at night."
    $ school_soccer_tell_photos()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo4:
    nate.name "You see our little witch in the gazatte?"
    drake.name "Yeah. Right up her skirt."
    pc "I can hear you you know?"
    nate.name "Think it was on purpose?"
    drake.name "How can you miss it? Of course it was."
    pc "..."
    nate.name "Shame she was wearing the pants."
    drake.name "Mmmm."
    $ school_soccer_tell_photos()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo5:
    nate.name "Fucking catgirl!"
    pc "Ah you saw that one did you?"
    dan.name "[nate.name] the dirty fuck is first in line when a new issue is out."
    pc "Pfft. Of course he is. Should have known."
    nate.name "That little window in the top. Perfect."
    if nate.seen_breasts:
        pc "You have seen my tits before. Whats with the drooling over the pics?"
        nate.name "Your tits arent keeping me company at night."
    else:
        pc "Pervert."
        nate.name "Got to take what I can get."
    $ school_soccer_tell_photos()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo6:
    nate.name "Christmas ass cheeks!"
    drake.name "Fuck. I know!"
    pc "What you talking about?"
    nate.name "You and your sweet cheeks for the winter gazette."
    pc "Ah. Bit much was it?"
    nate.name "Nope!"
    drake.name "Not at all."
    dan.name "Was good."
    pc "You oafs."
    $ school_soccer_tell_photos()
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo_private:
    $ add_to_list(school_soccer_quest.conversation_topics, "want_photos")
    pc "So you haven't seen the private topless photos I have?"
    nate.name "Huh?"
    pc "Or the nude ones?"
    nate.name "Ah fuck now you are just messing with us."
    pc "Am I? Go see [felix.name] if you think you can afford the private collection."
    nate.name "What? Really? You two hearing this?"
    drake.name "Yeah..."
    nate.name "They expensive?"
    pc "Speak to my agent."
    nate.name "Fuck!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo7:
    nate.name "Those photos you took have kept me company for quite a few nights."
    if player.isslut:
        pc "Oh. Getting good use out of them then?"
        nate.name "Oh believe me I am."
        pc "You'll wear them out if you keep it up. Can you afford more?"
        nate.name "Err, not sure. Better take good care of them."
        pc "Might be a new collection available when you wear the old ones out~"
        $ dialogue = WeightedChoice([
        ("New ones? Fuck! Didn't think of that. I got the dance stuff you did with your tits out.", If("dance_topless" in school_photo_quest.list,1,0)),
        ("New ones? Fuck! Didn't think of that. I got the catgirl ones with you showing off.", If("catgirl_topless" in school_photo_quest.list,1,0)),
        ("New ones? Fuck! Didn't think of that. I got the witch stuff with that nice little peek between your legs.", If("witch_topless" in school_photo_quest.list,1,0)),
        ("New ones? Fuck! Didn't think of that. I got Santa set with you showing off your arse.", If("santa_tasteful" in school_photo_quest.list,1,0)),
        ("New ones? Fuck! Didn't think of that. I got that elf set you did. Can't quite see between the legs though...", If("elf_tasteful" in school_photo_quest.list,1,0)),
        ])
        nate.name "[dialogue]"
        nate.name "You telling me there are others?"
        pc "Wouldn't you like to know."
    else:
        pc "Err. Good to hear?"
        dan.name "Pervert has had a smile on his face ever since he got hold of them."
        if nate.sex:
            pc "No idea why. Not like he hasn't had the real thing."
            nate.name "Come keep me warm at night and I'll get rid of my collection."
            pc "Err, keep your collection."
        else:
            pc "Don't act like you don't have a private stash under your pillow."
            dan.name "Err..."
            nate.name "Hahaha!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo8:
    drake.name "How come you took those naughty pictures anyway?"
    pc "Huh? Oh. Those..."
    pc "People were aking for them. We did normal shots at first but after a few issues of the gazzete people kept contacting [felix.name] for some of the off market shots."
    pc "Make more money from the private collection than the main pictures. So the gazette now is pretty much an advertisment for the naughty photos."
    drake.name "Oh? You don't mind?"
    if player.iswhore:
        pc "People have paid to fuck me. What do I care about some pictures?"
        drake.name "Hmmm..."
    else:
        pc "If I did, I wouldn't have taken them. Easy way to make money without \"other\" things happening."
        if "bukkake" in school_photo_quest.list:
            drake.name "Other things like having a bunch of guys cum over your face?"
            pc "Err... Well..."
            pc "Shush!"
        elif "sex" in school_photo_quest.list:
            drake.name "Oh? I thought you did do \"other\" things."
            pc "Well, yes..."
            pc "Bit different in a studio though."
            drake.name "If you say so."
        else:
            drake.name "I guess..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo9:
    drake.name "Isn't it a bit dangerous to have your photos out there like that? Don't people harass you on the street or something?"
    pc "Hmm, I guess it can happen. But with the outfits and makeup, most people don't recognise me."
    drake.name "Well, most people round here know it's you."
    pc "Well yeah, I guess."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_photo10:
    nate.name "Hey [name]. Did you know your friend was also taking photos?"
    pc "Huh? What one?"
    nate.name "The cute dark skinned one you dance with. [dani.name] isn't it?"
    pc "Yeah [dani.name]. What do you mean \"taking photos\"?"
    nate.name "Well, I was speaking to [felix.name] to see if he had any new sets of yours. But I noticed in his album he had another girl so I asked to see the sample of those as well."
    nate.name "And it was of her."
    pc "Oh? Nice photos?"
    if "dani_nude" in school_photo_quest.list:
        nate.name "Stark naked!"
        drake.name "Yeah?"
        nate.name "She's fucking hot!"
        pc "Naked?"
        nate.name "Yup!"
    elif "dani_topless" in school_photo_quest.list:
        nate.name "Yeah. Tits out and everything!"
        drake.name "Yeah?"
        nate.name "She's fucking hot!"
    elif "dani_tasteful" in school_photo_quest.list:
        nate.name "Yeah. Nude but hiding her bits. Won't be long 'til I can get some of her naked."
        nate.name "Fuck she is so hot!"
    else:
        nate.name "Yeah. Though she doesn't have ones as nice as yours. She keeps her clothes on."
        pc "For now."
        nate.name "What? You think..."
        pc "Nothing. Nothing..."
    pc "You have the phoos with you?"
    nate.name "What? You want to see?"
    pc "Of course. She's my friend. Hope she has some lovely pictures."
    nate.name "Ah. Well not with me anyway. They are in my collection."
    pc "Ah. No worries. I'll speak to [dani.name] or [felix.name] and try and get a look."
    nate.name "You girls should do a lesbo set together."
    drake.name "Damn that would be hot!"
    if any(item in ["told_sex" + drake.name, "told_sex" + nate.name, "told_sex" + dan.name] for item in rachel.conversation_topics):
        nate.name "Get that slut friend of yours to join as well."
        pc "[rachel.name]?"
        if all(item in ["told_sex" + drake.name, "told_sex" + nate.name, "told_sex" + dan.name] for item in rachel.conversation_topics) and all([nate.sex,drake.sex,dan.sex]):
            nate.name "Everyone here has fucked [rachel.name] and [name] so could get an orgy going. Just need to get to fucking [dani.name]."
            drake.name "Well, she's friends with [name] and [rachel.name], so..."
            $ player.face_annoyed()
            pc "So what?"
            nate.name "Don't play coy [name]. Your both sluts and I have naughy pictures of [dani.name] who's your friend so she's probably a slut too."
            pc "Ugh..."
        else:
            nate.name "Yeah. Would love to see the three of you together."
            pc "I bet."
    else:
        nate.name "Right!"
    $ add_to_list(school_photo_quest.conversation_topics, "dani_photos_pc_knows")
    jump school_field_soccer_hangout_conv_end


label school_field_soccer_hangout_conv_freeuse_0:
    $ loc_school_field_back.dict["free_use_topic"] += 1
    rachel.name "Why do you run away and hide to have fun?"
    robin.name "Huh?"
    rachel.name "Hiding in the back and doing your funny stuff."
    robin.name "Err, why wouldn't I?"
    rachel.name "More fun for us to watch."
    pc "Yeah [robin.name]. Running off to hide!"
    robin.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_freeuse_1:
    $ loc_school_field_back.dict["free_use_topic"] += 1
    pc "[robin.name] likes watching others but hides herself."
    robin.name "Wait, who said I like..."
    rachel.name "Oooh? Really?"
    robin.name "[name]!"
    rachel.name "It's fun!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_freeuse_2:
    $ loc_school_field_back.dict["free_use_topic"] += 1
    rachel.name "Come on, which one of you perverts wants to give [robin.name] a show?"
    nate.name "I'm not gonna say no to that."
    rachel.name "Come on then."
    $ add_to_list(rachel.list, "soccer_free_use")
    $ add_to_list(rachel.list, "soccer_sex_rachel")
    $ add_to_list(nate.list, "soccer_sex_rachel")
    "[nate.name] wastes no time in coming over to [rachel.name] and we all just stand there watching them have fun."
    robin.name "Oh wow..."
    pc "Yeah."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_freeuse_3:
    $ loc_school_field_back.dict["free_use_topic"] += 1
    rachel.name "So come on [robin.name], you turn now."
    drake.name "Let's go!"
    robin.name "Ugh, you guys are going to kill me one day..."
    $ add_to_list(robin.list, "soccer_free_use")
    $ add_to_list(robin.list, "soccer_sex_robin")
    $ add_to_list(drake.list, "soccer_sex_robin")
    "[drake.name] wastes no time in coming over to [robin.name] and we all just stand there watching them have fun."
    rachel.name "Go go go!!"
    pc "Have fun."
    jump school_field_soccer_hangout_conv_end





label school_field_soccer_hangout_conv_robin_general1:
    drake.name "So, volleyball at the beach then?"
    robin.name "Yeah. It's fun."
    drake.name "No troubles there?"
    robin.name "Troubles everywhere."
    drake.name "Thought with the beach there would be more. Bikinis and all that."
    robin.name "Not really. I mean yeah, but doesn't matter where we go. Arseholes are there."
    pc "Fuckers are all over the place. It's either hide at home all day with the doors locked or just deal with it."
    drake.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general2:
    nate.name "Wouldn't mind seeing you in your bikini though."
    robin.name "Then come to the beach and play with us. Room for you lot to join."
    nate.name "No thanks. Prefer it here where I can pretend the shithole world out there doesn't exsist."
    robin.name "Mmm. Not a bad plan."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general3:
    drake.name "So what you doing for work. You working the bar with [name]?"
    robin.name "No. Me and dresses don't get along. Always forget I am wearing one and end up showing off too much."
    pc "That would be a bonus at the pub."
    robin.name "Hah, I bet."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general4:
    nate.name "Let's go [robin.name]. You and me in the bushes."
    robin.name "Pervert."
    nate.name "That wasn't a no."
    if "soccerboys_can_sex" in robin.list:
        robin.name "No, it wasn't."
        nate.name "Let's go then."
        pc "Have fun."
        $ add_to_list(robin.list, "soccer_sex_robin")
        $ add_to_list(nate.list, "soccer_sex_robin")
    else:
        robin.name "Wasn't a yes either."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general5:
    robin.name "You ever check out the junkyard at the end of town?"
    if jaylee.has_met:
        pc "Yeah, had a look around. Can sell stuff to them over there."
        robin.name "Yeah, been scraping by doing a bit of that."
        if sandy.has_met:
            pc "You hang out at the beach a lot. [sandy.name] is always looking for stuff to make jewelery with."
            robin.name "Yeah, I do that too."
    else:
        pc "The junkyard. No, why?"
        robin.name "The guy there buys up junk you can find around the street."
        pc "Junk?"
        robin.name "Electronic crap, cans, metal stuff. Junk mostly but they fix it up. Can make some decent money."
        pc "I'll keep that in mind."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general6:
    robin.name "Think you're good on rent?"
    if player.check_poor():
        pc "Doubt it. Will see. Probably need to scrape some money together before the time comes."
        robin.name "Better do. Don't wanna end up short."
        pc "Yeah..."
    else:
        pc "Should be okay for this week. Fuck, it eats up most of what I make."
        robin.name "Tell me about it..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_general7:
    nate.name "So you not interested in showing off like [name] here?"
    robin.name "Err, no thanks. Rather not invite you lot to drag me into the bushes."
    nate.name "You'd probably like it."
    robin.name "Could be. But I'll keep my clothes on just to spite you."
    nate.name "Hmm. I'll try my best to get them off you then."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_normal:
    $ dialouge = renpy.random.choice([
    "...see that earlier on...",
    "...and I was standing there while...",
    "...then he started to shout down the road...",
    "...I couldn't believe it. At that time of the day as...",
    ])
    $ school_soccer_pick_boy()
    tempname.name "[dialouge]"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_robin_strip:
    robin.name "Since you lot wont shut up about it..."
    $ add_to_list(robin.list, "no_location")
    $ add_to_list(robin.list, "naked_for_boys")
    $ remove_from_list(robin.list, "will_get_naked_boys")
    pc "Uh oh. Did you guys piss her off?"
    nate.name "I hope not."
    pc "Ugh, I'll check if shes ok when I see her at home."
    $ remove_from_list(robin.list, "no_location")
    robin.name "Happy?"
    nate.name "Oh wow! Very happy."
    drake.name "Fuck, didn't expect you would do it."
    rachel.name "Go [robin.name]. Naked sisters!"
    if mira_here():
        rachel.name "Now just to get [mira.name] to do it."
        if t.hour >= 16:
            mira.name "I'm already standing here dressed as a whore."
        else:
            mira.name "If you have the money, then just pay me to get naked."
        rachel.name "Haha!"
    jump school_field_soccer_hangout_conv_end



label school_field_soccer_hangout_conv_rachel_nudeask:
    rachel.name "Why am I the only one naked [name]?"
    pc "Ah..."
    $ pc_strip(True)
    pc "Happy?"
    rachel.name "Yup."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_0:
    $ rachel.dict["rachel_nude"] += 1
    robin.name "So what's with all the nakedness?"
    rachel.name "It's fun! You should try it."
    robin.name "Err, no thanks."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_1:
    $ rachel.dict["rachel_nude"] += 1
    robin.name "But what made you do it?"
    rachel.name "I wanted to get fucked in the bushes."
    robin.name "Err, what?"
    rachel.name "Saw some girl getting dragged off in the park an it looked like fun."
    robin.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_2:
    $ rachel.dict["rachel_nude"] += 1
    robin.name "Okay, but why be naked here?"
    rachel.name "Fun."
    robin.name "You know you are surrounded by perverts?"
    rachel.name "Thats why it's fun."
    robin.name "Right..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_3:
    $ rachel.dict["rachel_nude"] += 1
    if "can_bitch" in rachel.list and "can_bitch" in robin.list:
        robin.name "I'm guessing with the collar on, you got dragged off into the bushes eventually?"
        rachel.name "Yeah! It was great!"
        nate.name "The collar?"
        robin.name "Private conversation!"
        nate.name "We are right in front of you."
    else:
        robin.name "So, did you get dragged off in the bushes?"
        if "can_bitch" in rachel.list:
            rachel.name "Yeah, ended up fighting off a bunch of weirdos."
            robin.name "Oh?"
            rachel.name "They kinda left me alone after I started biting though."
            robin.name "Good to know."
        else:
            rachel.name "Not yet. One day."
            robin.name "Why would you want it?"
            rachel.name "The girl who was running away looked like she was having a great time."
            robin.name "..."
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_4:
    $ rachel.dict["rachel_nude"] += 1
    rachel.name "You should try it. The boys will like it."
    robin.name "I'm sure they will..."
    if all([drake.name in robin.sex_who, nate.name in robin.sex_who, dan.name in robin.sex_who]):
        nate.name "You talk like everyone hasn't already seen you naked round back."
        nate.name "Even better round back since we also fuck you."
        robin.name "Ugh!"
        $ add_to_list(robin.list, "will_get_naked_boys")
    else:
        nate.name "Yeah, we would love it. Listen to [rachel.name]."
        robin.name "Shoo!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_5:
    $ rachel.dict["rachel_nude"] += 1
    rachel.name "Even [name] is naked."
    pc "Hey, don't bring me into this."
    nate.name "Yeah [robin.name], you are the odd one out."
    robin.name "Shush!"
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_conv_rachel_nudetalk_6:


    rachel.name "Boo! No naked people!"
    if not c.nude:
        pc "Ah!"
        $ pc_strip(True)
    robin.name "Shush!"
    if all([drake.name in robin.sex_who, nate.name in robin.sex_who, dan.name in robin.sex_who]):
        nate.name "You talk like everyone hasn't already seen you naked round back."
        nate.name "Even better round back since we also fuck you."
        robin.name "Ugh!"
        $ add_to_list(robin.list, "will_get_naked_boys")

    elif not numgen(0, 15):
        $ add_to_list(robin.list, "will_get_naked_boys")
    jump school_field_soccer_hangout_conv_end



label school_field_soccer_hangout_conv_group_sex_ask:
    $ tempname = school_soccer_npc_nosex_boy_who()
    tempname.name "Since they are having fun [name], why don't we?"
    pc "Hmmm..."
    if player.check_sex_agree_choice(0, "Sure, why not?", "No thanks, I just want to watch"):
        jump school_field_soccer_sex_group_start

label school_field_soccer_hangout_dare_intro:
    $ school_soccer_quest_betmatch["intro"] = True
    nate.name "£100?"
    drake.name "Best out of 5?"
    nate.name "Uh huh."
    drake.name "Ok, let's go."
    $ drake.active = False
    $ nate.active = False
    pc "Who you think will win?"
    dan.name "Whoever drank the least beer today."
    pc "Hmmm."
    "I watch as the two of them play a match against each other for money. Both have had a fair bit to drink and it is pitch black out there so neither of them are putting in a good performance."
    pc "I could probably beat those drunken clowns."
    dan.name "It's all just for fun. Doubt either of them really care about winning."
    nate.name "FUCK!"
    pc "..."
    pc "You sure about that?"
    dan.name "Mostly..."
    $ drake.active = True
    $ nate.active = True
    jump school_field_soccer_hangout_conv_end

label school_field_soccer_hangout_dare_offer:
    $ school_soccer_pick_boy()
    tempname.name "So who's up for a match?"
    menu:
        "Play a bet match with [tempname.name]":
            pc "Sure, I'm game."
            jump school_field_soccer_darematch_picker
        "Don't play":

            pcm "Not really up for playing."
            if not tempname == nate:
                nate.name "Sure, I'm game."
            else:
                dan.name "Sure, let's go."
            tempname.name "Great."
            "I hang around for a bit watching the boys playing a game until one of them wins."
            jump school_field_soccer_hangout_conv_end

label school_field_soccer_drinking_toggle:
    if "stop_drinking" in loc_school_field_back.list:
        $ remove_from_list(loc_school_field_back.list, "stop_drinking")
        pcm "I can handle some more beers I think."
    else:
        $ add_to_list(loc_school_field_back.list, "stop_drinking")
        pcm "I should probably hold off on the beers."
    jump travel

label school_field_soccer_hangout_conv_end:
    if robin_here():
        $ add_to_list(robin.list, "soccer_hanging_out")
        $ loiter_love(who=robin)
    if rachel_here():
        $ add_to_list(rachel.list, "soccer_hanging_out")
        $ loiter_love(who=rachel)
    if mira_here():
        $ add_to_list(mira.list, "soccer_hanging_out")
        $ loiter_love(who=mira)
    if not player.drunk >= 100:
        if not "stop_drinking" in loc_school_field_back.list:
            $ player.beer()
        $ player.face_neutral()
        if player.cum_visible:
            "I hang out some more while chatting away and drinking a beer, though the boys find it a bit hard to focus being that I am covered in cum."
        elif c.exposed:
            "I hang out some more while chatting away and drinking a beer, but the boys seem a bit distracted..."
        elif c.inappropriate:
            "I hang out some more while chatting away and drinking a beer while the boys fail to keep their eyes off me."
        else:
            "I hang out some more while chatting away and drinking a beer."
    else:
        $ player.face_neutral()
        if player.cum_visible:
            "I hang out some more while chatting away while holding off on beer, though the boys find it a bit hard to focus being that I am covered in cum."
        elif c.exposed:
            "I hang out some more while chatting away while holding off on beer but the boys seem a bit distracted..."
        elif c.inappropriate:
            "I hang out some more while chatting away while holding off on beer while the boys fail to keep their eyes off me."
        else:
            "I hang out some more while chatting away while holding off on beer."
    $ school_soccer_npc_sex_robin_end()
    $ loiter(who=[drake, nate, dan])
    if not robin_here([loc_school_field_back, loc_school_field_back_isolate, loc_school_locker_old]) and "soccer_hanging_out" in robin.list:
        if "naked_for_boys" in robin.list:
            show robin nude at right1 with dissolve
        else:
            show robin at right1 with dissolve
        $ remove_from_list(robin.list, "soccer_hanging_out")
        robin.name "I'm heading off [name]. You coming with?"
        menu:
            "Sure, let's go home.":
                pc "See you round guys."
                robin.name "See you!"
                jump robin_goto_home
            "No. You go ahead without me.":

                if player.has_perk([perk_blackout, perk_drunk]):
                    robin.name "You are pretty drunk so look after yourself getting home."
                else:
                    robin.name "Ok, see you guys!"
                hide robin with dissolve

    if not rachel_here([loc_school_field_back, loc_school_field_back_isolate, loc_school_locker_old]) and "soccer_hanging_out" in rachel.list:
        if "Bitching at the park." in rachel_here(where=True):
            rachel.name "Cya guys. I'm gonna get fucked by some wolfies in the park."
        elif rachel_here(where=True) == loc_beach_gym:
            rachel.name "I'm going guys. Gonna play some naked volleyball."
        else:
            rachel.name "Cya guys, I'm going."
        pc "Cya later."
    if not mira_here([loc_school_field_back, loc_school_field_back_isolate, loc_school_locker_old]) and "soccer_hanging_out" in mira.list:
        mira.name "C'ya guys. I'm going to work."
        pc "Be safe."
    if not school_soccer_hangingout():
        drake.name "Getting late [name]. We are gonna head off home."
        pc "Ok, see you round."
    $ remove_from_list(robin.list, "soccer_hanging_out")
    $ remove_from_list(rachel.list, "soccer_hanging_out")
    $ remove_from_list(mira.list, "soccer_hanging_out")
    jump travel_arrival

label school_field_soccer_hangout_end:
    $ relax(30)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
