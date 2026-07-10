label random_event_school_normal:
    $ rand_choice = WeightedChoice([
    ("random_event_school_normal_1", 100),
    ("random_event_school_normal_2", If (school_dance_quest_show_count >= 2, 100, 0)),
    ("random_event_school_normal_3", If(not any([shane.dead, marcus.dead]), 100, 0)),
    ("random_event_school_normal_4", 100),
    ("random_event_school_normal_5", 100),
    ("random_event_school_normal_6", 100),
    ("random_event_school_normal_7", 100),
    ("random_event_school_normal_8", 100),
    ("random_event_school_normal_9", 100),
    ])
    jump expression rand_choice

label random_event_school_normal_1:
    girl1 "...as far away from there as possible. Even Security avoids the area unless they are in huge numbers."
    girl2 "Err, ok. But what's so scary about the place?"
    girl1 "It's lawless. Get in trouble and no one will help you. They call it Haven like it's a nice place to be but really what they mean is a free haven to do what you want."
    if main_quest_05.active == 2:
        pcm "Ugh, not wrong there..."
    jump random_event_school_end_picker

label random_event_school_normal_2:
    girl1 "...show that the dance girls did?"
    girl2 "Yeah. Give it a week and you will probably see them all at highway..."
    jump random_event_school_end_picker

label random_event_school_normal_3:
    girl1 "What happened to you?"
    girl2 "..."
    girl1 "Those two arseholes?"
    girl2 "..."
    jump random_event_school_end_picker

label random_event_school_normal_4:
    girl1 "You don't look right."
    girl2 "Yeah, stomach ache... Knew I shouldn't have eaten in the cafeteria..."
    girl1 "Err, have you taken a test?"
    girl2 "What? No..."
    girl1 "You probably should..."
    jump random_event_school_end_picker

label random_event_school_normal_5:
    girl1 "...to find somewhere peaceful to study."
    girl2 "Well, why not the library?"
    girl1 "Yeah right. Not stepping foot in there while those smelly shits hang out there."
    jump random_event_school_end_picker

label random_event_school_normal_6:
    girl1 "...walk all the way here again?"
    girl2 "Yeah, no chance I'm getting the bus again."
    girl1 "*Sigh* I swear there are shits who just spend all day on the bus to harass people..."
    jump random_event_school_end_picker

label random_event_school_normal_7:
    girl1 "...last night near the motel. Didn't even listen to what he wanted and just ran away."
    girl2 "Probably for the best. Can't take the chance."
    jump random_event_school_end_picker

label random_event_school_normal_8:
    girl1 "...not seen her for a while. You know anything?"
    girl2 "No, she didn't say anything to me. My guess is pregnant. She was acting up a bit before she went missing."
    girl1 "No? You think so? How did she manage that? She was smart enough to avoid it."
    girl2 "Who knows. Maybe someone paid more to do it that way..."
    jump random_event_school_end_picker

label random_event_school_normal_9:
    girl1 "...at the lake to relax."
    girl2 "What? I have never been there. Is it safe?"
    girl1 "Well, as safe as anywhere round here can be. Just don't use the lockers to keep your stuff in and keep it in your bag."
    girl2 "Err, ok. Why?"
    girl1 "So if you need to do a runner, you aren't left god knows where with only a bikini."
    girl2 "Ah..."
    jump random_event_school_end_picker



label random_event_school_desire:
    $ rand_choice = WeightedChoice([
    ("random_event_school_desire_1", If (player.vvirgin, 100, 0)),
    ("random_event_school_desire_2", 100),
    ("random_event_school_desire_3", If (drake.has_met, 100, 0)),
    ("random_event_school_desire_4", 100),
    ("random_event_school_desire_5", player.check_horny(extreme=True)),
    ("random_event_school_exhibitionist_1", If(player.has_perk(perk_exhibitionist),50,0)),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_desire_1:
    $ player.face_shy()
    pcm "Phew. I need to go and wash my face or something. Cold shower..."
    $ player.face_normal()
    jump random_event_school_end_picker

label random_event_school_desire_2:
    $ player.face_shy()
    pcm "Could accidentally walk into the boys' changing rooms..."
    pcm "No... That would just make me feel hotter."
    pcm "..."
    pcm "Unless they decide to do something about it for me..."
    $ player.face_normal()
    jump random_event_school_end_picker

label random_event_school_desire_3:
    $ player.face_shy()
    pcm "Maybe I should go and play football with the boys out there. Pretty sure they will help cool me down..."
    $ player.face_normal()
    jump random_event_school_end_picker

label random_event_school_desire_4:
    $ player.face_shy()
    pcm "..."
    $ player.eye = 6
    pause 0.5
    $ player.eye = 5
    pause 0.5
    $ player.eye = 1
    pcm "Hmmm..."
    $ walk(loc_school_locker_girls)
    pcm "..."
    pcm "No one here..."
    $ pc_striptease()
    show sb_pose_lookback with dissolve
    pcm "I'm in here naked all alone..."
    pcm "Anyone...?"
    pcm "..."
    hide sb_pose_lookback with dissolve
    $ player.face_worried()
    pcm "*Sigh* Just makes me hotter..."
    $ pc_dress_slow()
    $ player.face_normal()
    jump random_event_school_end_picker

label random_event_school_desire_5:
    pcm "..."
    pcm "I really could do with someone helping me out..."
    if not loc_cur == loc_school_hallway:
        $ walk(loc_school_hallway)
    pcm "Hmmm, should I ask someone to \"help\" me out?"
    if player.check_sex_agree(3):

        menu:
            "Find someone to go somewhere private with":
                pcm "Hmm, who could I ask..."
                pcm "He is alone and looks alright I guess."
                pc "Errm, hey."
                guy "Err, hi?"
                pc "You interested in heading off somewhere alone together?"
                $ randomnum = renpy.random.randint(1, 8)
                if randomnum == 1:
                    guy "Yeah right. So your friends can jump me when I am alone and rob me?"
                    guy "Go fuck yourself."
                    "He gives me a dirty look as he walks away."
                elif randomnum == 2:
                    guy "Whaa, errr, what?"
                    pc "We can go somewher..."
                    "He turns around and immediately starts walking away"
                elif randomnum == 3:
                    guy "Heh, no idea what your game is but no chance am I going anywhere alone with you."
                    "Before I can get another word in, he turns and walks away."
                elif randomnum == 4:
                    "He doesn't even say a word and just walks away from me."
                elif randomnum == 5:
                    guy "Yeah right. As if I can afford that."
                    "Before I can get another word in, he turns and walks away."
                elif randomnum == 6:
                    guy "Fuck, go and do that shit at the highway and leave this place alone."
                    "Before I can get another word in, he turns and walks away."
                else:
                    guy "You serious? To do what I think you mean?"
                    pc "Yes."
                    guy "Err, sure?"
                    jump school_rep_sex

                $ player.face_worried()
                pcm "Not the response I was expecting..."
                jump random_event_school_end_picker
            "No, don't bother":

                $ NullAction()
    pcm "Ugh, better not. Probably more trouble than it's worth."
    jump random_event_school_end_picker
label random_event_school_allure:
    $ rand_choice = WeightedChoice([
    ("random_event_school_allure_1", 100),
    ("random_event_school_allure_2", 100),
    ("random_event_school_allure_3", 30),
    ("random_event_school_allure_4", 30),
    
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_allure_1:
    $ dialogue = WeightedChoice([
    ("Nice ass.", If (c.ass,1,0)),
    ("Nice tits.", If (c.clevage,1,0)),
    ("Nice tits, look at 'em bounce!", If (c.clevage and c.bra == 0,1,0)),
    ("Ohh, nice pokies.", If (c.clevage and c.bra == 0 and outside, 1, 0)),
    ("Fuck, sexy girl!", If (c.slutty,1,0)),
    ("Damn, looking good girl.", 1),
    ])
    guy "[dialogue]"

    if player.isslut:
        $ player.face_happy()
        $ player.add_mood(5)
        $ player.add_desire(5)
        pc "Thanks."
    else:
        $ player.face_shy()
        pc "..."
    jump random_event_school_end_picker

label random_event_school_allure_2:
    girl "*COUGH* Whore!"
    $ player.add_mood(-5)
    $ player.face_worried()
    pc "..."
    jump random_event_school_end_picker

label random_event_school_allure_3:
    guy "Hey... So..."
    pc "Huh?"
    $ player.set_whore_price(0)
    guy "£[player.soldprice] to wank me off?"
    $ player.soldrequest = "hand"
    if player.check_whore_agree_choice():
        jump school_rep_sex
    else:
        if player.check_whore(notif=False):
            pc "Sorry, you are on your own."
            guy "Ah, ok..."
        else:
            pc "*Tsk* No."
        jump random_event_school_end_picker














label random_event_school_allure_4:
    guy "Hey... So..."
    pc "Huh?"
    $ player.set_whore_price(0)
    guy "£[player.soldprice] to suck me off?"
    pc "Oh?"
    if player.check_whore_agree_choice(request="oral"):
        $ tempname = schoolguy
        $ quest_temp = None
        $ male_npc_create()
        jump whore_street_customer_pick_location_tombola
    else:

        pc "Sorry, you are on your own."
        guy "Ah, ok..."
    jump random_event_school_end_picker

label random_event_school_allure_5:
    guy "Damn, fucking sexy."
    if player.isslut or player.iswhore:
        $ player.face_happy()
        $ player.add_mood(3)
        pc "Thanks."
    elif not player.check_nowill():
        pc "Err, thanks I guess."
    else:
        $ player.face_worried()
        pc "..."
    $ randomnum = renpy.random.randint(1, 8)
    if randomnum == 1:
        guy "So, wanna go somewhere alone? I can pay."
        if player.iswhore or player.check_whore():
            pc "..."
            pc "How much?"
            $ player.set_whore_price(0)
            guy "£[player.soldprice]?"
            pc "Hmm..."
            if player.check_whore_agree_choice(request="oral"):
                jump school_rep_sex
            else:
                pc "Sorry mate, you are on your own."
                guy "Ah, ok..."
                jump random_event_school_end_picker
        else:
            $ player.face_annoyed()
            pc "*Tsk* No."
            "I walk off without giving him a chance to protest."
            jump random_event_school_end_picker
    guy "How about we go somewhere alone for some fun?"
    if player.check_drunk(4) and player.sex_agree(2):
        pc "Sure, whatever."
        jump school_rep_sex
    elif player.sex_agree(4):
        pc "Bold aren't you?"
        pc "Sure, why not..."
        jump school_rep_sex
    elif player.sex_agree(2):
        pc "Eh, another time maybe."
        guy "Ah thought I would ask anyway."
        pc "Sure."
        jump random_event_school_end_picker
    else:
        $ player.face_annoyed()
        pc "*Tsk* No."
        "I walk off without giving him a chance to protest."
        jump random_event_school_end_picker

label random_event_school_allure_6:
    $ walk(loc_school_toilet_boys)
    with vpunch
    $ player.face_shock()
    pc "Ah fuck. What are you doing?"
    guy "Gonna have some fun with you. Dressed like that I couldn't resist."
    $ player.face_worried()
    pc "Whaa, fuck off. Get out of the way."
    $ player.punch()
    guy "Shut! The! Fuck! Up!"
    $ player.sex_forced(schoolguy)
    jump school_rep_sex

label random_event_school_highconf:
    $ rand_choice = WeightedChoice([
    ("random_event_school_highconf_1", 30),
    ("random_event_school_highconf_2", 100),
    ("random_event_school_exhibitionist_1", If(player.has_perk(perk_exhibitionist),30,0)),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_highconf_1:
    pcm "Guess this place isn't -such- a shithole..."
    pcm "Could have ended up in worse places after my accident."
    jump random_event_school_end_picker

label random_event_school_highconf_2:
    girl "Hey [name]."
    pc "Hey."
    pcm "..."
    pcm "No idea who that was."
    jump random_event_school_end_picker

label random_event_school_lowconf:
    $ rand_choice = WeightedChoice([
    ("random_event_school_lowconf_1", If(t.day > 30, 5, 0)),
    ("random_event_school_lowconf_2", 100),
    ("random_event_school_lowconf_3", 100),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_lowconf_1:
    guy "Hey, you. Come with me."
    $ player.face_confused()
    pc "Err, what for?"
    guy "I just need some help, come on."
    if player.check_nowill():
        pc "Errm..."
        guy "Come on, hurry."
        $ player.face_worried()
        pc "But..."
        guy "Quick, come, just in here..."
        $ walk(loc_school_toilet_boys)
        $ player.face_worried()
        pc "Err, what? Why in here?"
        $ player.sex_forced(schoolguy)
        jump school_rep_sex
    else:
        pc "Err, No I don't think so."
        guy "Come on, just..."
        $ player.face_normal()
        "I walk away from him paying him no more mind."
        jump random_event_school_end_picker

label random_event_school_lowconf_2:
    guy "Hey."
    if player.check_nowill():
        pc "..."
    else:
        pc "Hi."
    jump random_event_school_end_picker

label random_event_school_lowconf_3:

    $ c.bottom = 0
    $ c.outfit = 0
    $ player.face_shock()
    with vpunch
    pc "Whaaa what the fuck!"
    pc "..."
    if player.has_perk(perk_exhibitionist):
        $ player.face_shy()
        "I pretend to fumble with my clothes and give a good showing to the gawkers."
        pc "C'mon, ahh. Sorry sorry."
        "I pretend to be humiliated but in fact I find this really exciting."
        $ pc_dress()
        pc "Finally."
        $ player.face_annoyed()
        pc "Shoo! Show's over!"
        $ player.add_mood(10)
        $ player.add_conf(2)
        $ player.add_desire_random(20)
    else:
        $ pc_dress()
        $ player.face_angry()
        pc "What kind of creep rushes up to someone and pulls their clothes down?"
        pc "Damn, some right weirdos out in the world."
        $ player.add_mood(-10)
    jump random_event_school_end_picker

label random_event_school_lowconf_4:
    $ c.bottom = 0
    $ c.outfit = 0
    $ player.face_shock()
    pc "Ahh!"
    guy "Heh, let's see..."
    $ grope_crotch = True
    pc "Ah what the..."
    $ grope_crotch = False
    with hpunch
    guy "Haha, got her guys!"
    $ pc_dress()
    $ player.face_angry()
    pcm "What the fuck. The hell kind of freak does something like that?"
    pcm "Damn, some right weirdos out in the world."
    $ player.add_mood(-10)
    jump random_event_school_end_picker

label random_event_school_int:
    "This is an int event. If you have high int you may make comments about not needing to attend school and your time would be better spent elsewhere. May also have events where you are asked to join clubs."
    jump random_event_school_end_picker

label random_event_school_fitness:
    $ rand_choice = WeightedChoice([
    ("random_event_school_fitness_1", 100),
    ("random_event_school_fitness_2", 100),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_fitness_1:
    guy "*Whistles* Nice ass darlin'"
    if player.confidence < 20:
        pc "Ugh."
    elif player.confidence < 45:
        pc "You should be so lucky."
    else:
        pc "I know, I worked hard on it."
    $ player.add_mood(3)
    $ player.add_conf(1)
    jump random_event_school_end_picker

label random_event_school_fitness_2:
    guy "Wow fuck, you are looking good. Working out suits you."
    $ player.spank()
    pc "Ung!"
    $ player.add_mood(3)
    $ player.add_conf(1)
    pcm "Idiot..."
    jump random_event_school_end_picker

label random_event_school_fat:
    $ rand_choice = WeightedChoice([
    ("random_event_school_fat_1", 100),
    ("random_event_school_fat_2", 100),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_fat_1:
    girl "How the hell you wind up a fatarse round here? Who you been eating to put that kind of beef on?"
    $ player.face_worried()
    $ player.add_mood(-5)
    pc "..."
    jump random_event_school_end_picker

label random_event_school_fat_2:
    guy "Christ where did you find this one? Living in famine and someone manages to be a gutlord."
    $ player.face_worried()
    $ player.add_mood(-5)
    pc "..."
    jump random_event_school_end_picker

label random_event_school_lowmood:
    $ rand_choice = WeightedChoice([
    ("random_event_school_lowmood_1", 100),
    ("random_event_school_lowmood_2", 100),
    ("random_event_school_lowmood_3", 100),
    ("random_event_school_lowmood_4", If(school_soccer_quest_hangout_prompt,100,0)),
    ("random_event_school_exhibitionist_1", If(player.has_perk(perk_exhibitionist),100,0)),
    
    
    ])
    jump expression rand_choice

label random_event_school_lowmood_1:
    $ player.face_worried()
    pcm "Ugh, really could do with a beer or something. Feeling so shitty."
    jump random_event_school_end_picker

label random_event_school_lowmood_2:
    $ player.face_worried()
    pcm "Does no one have anything to drink or have fun with in this place?"
    jump random_event_school_end_picker

label random_event_school_lowmood_3:
    $ player.face_worried()
    pc "..."
    $ walk(loc_school_toilet_girls)
    $ player.face_cry()
    pc "*SOB*"
    pc "*Sniff*"
    $ player.face_wail()
    pc "Waaaaaaah!"
    $ player.face_cry()
    pc "*SOB*"
    $ player.add_mood(5)
    jump random_event_school_end_picker

label random_event_school_lowmood_4:
    $ player.face_worried()
    pc "..."
    pcm "Fuck it! I want a drink."
    $ walk(loc_school_field)
    if school_soccer_hangingout():
        pcm "There they are."
        $ walk(loc_school_field_back)
        pc "Beeeeeeer!"
        dan.name "One of those days?"
        pc "Mmmm."
        $ player.beer()
        pcm "Something to enjoy at least."
        $ relax(10)
        jump school_field_soccer_hangout_conv_end
    elif school_soccer_playing():
        pcm "They are playing."
        pc "Hey [dan.name]."
        show dan at right1
        pc "Hey [name]. You joining us?"
        pc "Maybe. You mind if I raid your stash?"
        dan.name "One of those days? Well, you know where it is."
        pc "Thanks."
        dan.name "Mmmm."
        hide dan
    else:
        pcm "The boy's aren't around, but I'm sure [dan.name] won't mind..."

    $ walk(loc_school_field_back)
    pcm "Let's see here. Ah, there we go."
    pcm "Something to cheer me up."
    $ player.beer()
    $ relax(10)
    pcm "Mmmmmm."
    if renpy.random.randint(0, 1) == 1:
        if school_soccer_hangingout():
            jump school_field_soccer_hangout_conv_end
        else:
            jump travel
    pc "..."
    pcm "Another I think."
    $ player.beer()
    $ relax(10)
    pc "Phew..."
    pcm "That hit the spot."
    if renpy.random.randint(0, 1) == 1:
        if school_soccer_hangingout():
            jump school_field_soccer_hangout_conv_end
        else:
            jump travel
    pc "Hmmm..."
    pcm "Sure. Why not?"
    $ player.beer()
    $ relax(10)
    pc "Phew!"
    if school_soccer_hangingout():
        jump school_field_soccer_hangout_conv_end
    else:
        jump travel

label random_event_school_highmood:
    "This is a good mood event. Sammy will make generally plesant comments."
    jump random_event_school_end_picker

label random_event_school_weather:
    $ rand_choice = WeightedChoice([
    ("random_event_school_weather_1", If(player.mood < 30, 1, 0)),
    ("random_event_school_weather_2", If(player.mood >= 30, 1, 0)),
    ])
    jump expression rand_choice

label random_event_school_weather_1:
    if weather_var == 1:
        $ player.face_angry()
        pcm "Ugh! Damn sun getting in my eyes..."
    elif weather_var == 2:
        $ player.face_angry()
        pcm "Ugh! So grey and ugly out here..."
    elif weather_var == 3:
        $ player.face_angry()
        pcm "Ugh! Damn rain..."
    else:
        $ player.face_angry()
        pcm "Brr. Freezing cold..."
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_weather_2:
    if weather_var == 1:
        $ player.face_happy()
        pcm "Phew, quite a nice day out today."
    elif weather_var == 2:
        $ player.face_happy()
        pcm "Not very sunny but glad it's not raining."
    elif weather_var == 3:
        $ player.face_happy()
        pcm "Raining. Well, is kind of romantic."
    else:
        $ player.face_happy()
        pcm "Ah the snow is so beautiful."
    $ player.add_mood(5)
    jump random_event_school_end_picker

label random_event_school_rushhour:
    $ rand_choice = WeightedChoice([
    ("random_event_school_rushhour_1", 100),
    ("random_event_school_rushhour_2", 100),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_rushhour_1:
    with hpunch
    $ player.face_angry()
    with vpunch
    pc "Ugh. Say sorry why don't you?"
    pc "Arsehole!"
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_rushhour_2:
    $ player.face_shock()
    $ player.grope()
    pc "Ah!"
    $ player.grope_end()
    with hpunch
    $ player.face_angry()
    pc "Get off!"
    pc "Pervert!"
    jump random_event_school_end_picker


label random_event_school_night:
    "This is the night time event. This one will probably not have anything unique to the school. Late night general shadyness. Robbery, beaten, cooerced, propositioned or raped."
    jump travel

label random_event_school_hungry:
    $ rand_choice = WeightedChoice([
    ("random_event_school_hungry_1", If (player.cash <= 10, 100,0)),
    ("random_event_school_hungry_2", If (player.cash > 10, 100,0)),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_hungry_1:
    $ player.face_worried()
    pcm "Dammnit. So hungry but don't have any money to buy some food..."
    pcm "Ugh!"
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_hungry_2:
    pcm "So hungry, think I will pick something up from the cafeteria."
    $ walk(loc_school_cafe)
    pcm "Hmmm... Everything looks as disgusting as each other..."
    pcm "This looks at least edible..."
    $ player.add_money(-5)
    "I find somewhere to sit and eat what I bought."
    pcm "..."
    $ player.eat()
    pcm "Not as horrible as it looked. Still pretty bad though."
    jump random_event_school_end_picker

label random_event_school_dirty:
    $ rand_choice = WeightedChoice([
    ("random_event_school_dirty_1", 100),
    ("random_event_school_dirty_2", 100),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_dirty_1:
    $ player.face_worried()
    pcm "Ugh, I am starting to stink. I really should clean up."
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_dirty_2:
    $ player.face_worried()
    girl1 "Ugh, you smell her?"
    girl2 "Yeah, disgusting..."
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_drunk:
    $ rand_choice = WeightedChoice([
    ("random_event_school_drunk_1", 100),
    ("random_event_school_drunk_2", 100),
    ("random_event_school_drunk_3", 100),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_drunk_1:
    with hpunch
    with vpunch
    guy "Watch it!"
    pc "Sorry..."
    jump random_event_school_end_picker

label random_event_school_drunk_2:
    with hpunch
    pc "Woah, sorry."
    guy "No worries..."
    guy "Been drinking have you?"
    pc "Yeah~"
    jump random_event_school_end_picker

label random_event_school_drunk_3:
    pcm "Huh?"
    $ player.grope_breasts()
    pc "Ah hey, what are you doing?"
    guy "Just havin' a bit of fun. Smells like you have been enjoying yourself as well."
    guy "Had a little to drink have we?"
    pc "Only a little~"
    guy "Hows about we go somewhere and I cheer you up some more?"
    if (player.check_drunk(3) and player.check_sex_agree(2)) or player.check_sex_agree(4):
        pc "Eh, sure why not~"
        $ player.grope_end()
        jump school_rep_sex
    elif player.check_sex_agree(2):
        menu:
            "Agree":
                pc "Eh, sure why not~"
                $ player.grope_end()
                jump school_rep_sex
            "Refuse":
                $ NullAction()

    pc "Sorry, you are on your own. Have fun though~"
    $ player.grope_end()
    guy "Ah, ok..."
    jump random_event_school_end_picker

label random_event_school_drunk_4:
    "Offer to go somewhere for more drinks"
    if player.check_drunk(3):
        "You agree"
    else:
        "You refused"
        jump travel
    $ walk(loc_school_locker_boys)
    "He has more booze in his locker."
    pc "Thanks."
    "He gropes you as you drink"
    $ player.grope()
    if player.check_sex_agree(2):
        "You dont protest much though"
    else:

        "You protest and get out of there."
        $ walk(loc_school_hallway)
        jump travel
    $ player.grope()
    $ player.beer()
    "You have a drink while his hands are all over you"
    pc "Mmmmm"
    "He offers you some more."
    if player.check_drunk(4):
        "You agree"
    else:
        "You know where this is heading. Do you agree?"
        menu:
            "Agree":
                $ NullAction()
            "Refuse":
                "THings are getting a bit too dangerous"
                $ walk(loc_school_hallway)
                jump travel
    "Here you go."
    $ player.beer()
    "As you have been drinking, you have been losing clothes"
    $ pc_strip_upper()
    "He offers something nicer to put in your mouth."
    $ player.grope_end()
    $ tempname = schoolguy
    jump whore_street_sex_blowjob

label random_event_school_pregnant:
    $ rand_choice = WeightedChoice([
    ("random_event_school_pregnant_1", 100),
    ("random_event_school_pregnant_2", 100),
    
    
    
    
    ])
    jump expression rand_choice

label random_event_school_pregnant_1:
    guy1 "Look, another whore with a fat belly round here."
    $ player.face_worried()
    guy2 "Huh? What are you so shocked about? Like half the girls round here are like that."
    jump random_event_school_end_picker

label random_event_school_pregnant_2:
    girl "Ugh, you not been listening in class? Learn to take it in the bum or something."
    $ player.face_worried()
    girl "Well, too late now..."
    jump random_event_school_end_picker

label random_event_school_cum:
    $ rand_choice = WeightedChoice([
    ("random_event_school_cum_1", 100),
    ("random_event_school_cum_2", 100),
    ("random_event_school_cum_3", 100),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_cum_1:
    $ player.face_worried()
    girl "Ugh fuck! Disgusting! Go and wash up or something you dirty bitch!"
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_cum_2:
    $ player.face_worried()
    girl "Fucking hell! Can't you leave your whoring to the highway you filthy cunt!"
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_cum_3:
    $ player.face_worried()
    guy "Wow look at the cumslut! The other bitches round here should learn from you."
    $ player.add_mood(-5)
    jump random_event_school_end_picker

label random_event_school_whore:
    $ rand_choice = WeightedChoice([
    ("random_event_school_whore_1", 100),
    ("random_event_school_whore_2", 100),
    ("random_event_school_whore_3", 100),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_whore_1:
    guy "Err, don't take this the wrong way. But..."
    $ player.face_worried()
    pc "Err, what?"
    guy "You are... A whore right?"
    $ player.face_confused()
    pc "Why?"
    $ player.set_whore_price(0)
    guy "£[player.soldprice]?"
    $ player.face_normal()
    pc "Ah, ok."
    if player.check_whore_agree_choice():
        $ tempname = schoolguy
        $ quest_temp = None
        $ male_npc_create()
        jump whore_street_customer_pick_location_tombola
    else:
        pc "Sorry, not now."
        guy "Ah, ok..."
        jump random_event_school_end_picker

label random_event_school_whore_2:
    $ player.set_whore_price(0)
    guy "Oi whore! £[player.soldprice] to pound your pussy?"
    $ player.face_normal()
    pc "*Sigh*"

    if player.check_whore_agree_choice(request="vag"):
        $ tempname = schoolguy
        $ quest_temp = None
        $ male_npc_create()
        jump whore_street_customer_pick_location_tombola
    else:
        pc "No."
        "I walk away ignoring the rude idiot."
        jump random_event_school_end_picker

label random_event_school_whore_3:
    $ player.set_whore_price(0)
    guy "Wanna earn some cash?"
    pc "Sure, how much?"
    guy "£[player.soldprice]?"

    if player.check_whore_agree_choice(request="vag"):
        $ tempname = schoolguy
        $ quest_temp = None
        $ male_npc_create()
        jump whore_street_customer_pick_location_tombola
    else:
        pc "No thanks."
        guy "Ah, ok..."
        jump random_event_school_end_picker



label random_event_school_broken:
    $ rand_choice = WeightedChoice([
    ("random_event_school_broken_1", If (player.mood < 20, 100,0)),
    ("random_event_school_broken_2", 100),
    ("random_event_school_broken_3", 100),
    
    
    
    ])
    jump expression rand_choice

label random_event_school_broken_1:
    $ tempname = streetguy
    $ quest_temp = None
    $ player.face_meek()
    pc "..."
    $ player.face_normal()
    pcm "Maybe..."
    $ walk(loc_school_locker_boys)
    guy "Hey, what are you..."
    $ c.top = 0
    $ c.outfit = 0
    pause 0.2
    if c.bra > 0:
        $ c.bra = 0
        pause 0.2
    $ player.face_meek()
    pc "I feel like shit. Anyone want to cheer me up?"
    guy "Wow! Ok... Sure, come here."
    $ player.face_happy()
    pc "Really?"
    guy "Damn right!"
    jump whore_sex_start

label random_event_school_broken_2:
    $ tempname = streetguy
    $ quest_temp = None
    guy "Hey, how about some fun?"
    pc "Err..."
    guy "C'mon. Come with me."
    pc "..."
    jump whore_street_customer_pick_location_tombola

label random_event_school_broken_3:
    $ tempname = streetguy
    $ quest_temp = None
    guy "Ah, you're that girl."
    pc "Huh?"
    $ walk(loc_school_locker_boys)
    "He takes me by the arm and leads me off somewhere."
    pc "What are you doing?"
    guy "having some fun."
    pc "Oh..."
    jump whore_sex_start

label random_event_school_bully:
    jump school_bully_event_picker

label random_event_school_photo:
    $ rand_choice = WeightedChoice([
    ("random_event_school_photo_1", 100),
    ("random_event_school_photo_2", 100),
    ("random_event_school_photo_3", If("tasteful" in school_photo_quest.list,100,0)),
    ("random_event_school_photo_4", If("breasts" in school_photo_quest.list,100,0)),
    ("random_event_school_photo_5", If("nude" in school_photo_quest.list,100,0)),
    ("random_event_school_photo_6", If("sex" in school_photo_quest.list,100,0)),

    ])
    jump expression rand_choice

label random_event_school_photo_1:
    girl1 "That's the girl in the gazette."
    girl2 "It is isn't it?"
    jump random_event_school_end_picker

label random_event_school_photo_2:
    guy1 "Look who it is."
    guy2 "That the girl flashing her arse in the gazette?"
    guy1 "Yeah."
    jump random_event_school_end_picker

label random_event_school_photo_3:
    guy1 "Fuck, it's her."
    guy2 "Who?"
    guy1 "I have photos of her showing off."
    guy2 "What? Naked ones?"
    guy1 "Yeah, but she doesn't show anything off. Dunno if there are others."
    jump random_event_school_end_picker

label random_event_school_photo_4:
    guy1 "Oh shit. It's that girl. I have photos of her with her tits out."
    guy2 "What? Really? I gotta see those. She's hot!"
    jump random_event_school_end_picker

label random_event_school_photo_5:
    guy1 "Shit. I got pictures of that girl starkers."
    guy2 "What? Her? Naked?"
    guy1 "Yeah, everything on show."
    guy2 "Damn! Show me."
    jump random_event_school_end_picker

label random_event_school_photo_6:
    guy1 "Wow. That's the whore that got fucked in those photos I showed you."
    guy2 "You sure? Looks kind of different."
    guy1 "I'm sure it's her."
    jump random_event_school_end_picker

label random_event_school_exhibitionist_1:
    if player.mood < 20:
        pcm "Ugh, I feel like shit."
    else:
        pc "Maybe I should have some fun."
    pcm "I know!"
    $ walk(loc_cur.isolate_loc)
    $ pc_striptease()
    $ player.face_laugh()
    $ walk(loc_school_hallway, trans=False)
    $ player.face_laugh()
    with dissolve
    $ walk(loc_school_field, trans=False)
    $ player.face_laugh()
    with dissolve
    $ walk(loc_school_cafe, trans=False)
    $ player.face_laugh()
    with dissolve
    $ walk(loc_school_gym, trans=False)
    $ player.face_laugh()
    with dissolve
    $ walk(loc_school_locker_girls)
    pcm "*PHEW*"
    pc "Haha!"
    $ pc_dress_slow()
    $ player.add_mood(30)
    $ player.add_desire_random(30)
    jump random_event_school_end_picker

label random_event_school_end_picker:
    if renpy.has_label(school_random_event_returner):
        $ temp_var_1 = school_random_event_returner
        $ school_random_event_returner = False
        jump expression temp_var_1
    elif school_random_event_returner:
        $ school_random_event_returner = False
        return
    else:
        jump travel

label random_event_school_exterior_late_for_school:
    $ player.face_worried()
    pc "I am really late for school. I had better hurry."
    $ player.face_normal()
    jump travel

label random_event_school_exterior_leave_school_early:
    $ player.face_worried()
    pc "Still classes going on right now. If I leave I may be locked out until classes are over."
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
