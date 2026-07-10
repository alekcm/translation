label random_event_picker_homeless_start_tombola:
    jump expression WeightedChoice([
    ("start_homeless_postsearch", If(log.interactive("quest_homeless_start_01") and all([loc_motel.visited, loc_truckstop.visited, loc_highway.visited, loc_highway_slum.visited]), 10000, 0)), 

    ("start_homeless_comment_1", 50), 
    ("start_homeless_comment_2", 50), 
    ("start_homeless_comment_3", 50), 

    ("travel_dis", 300), 
    ])

label start_homeless_intro:
    show screen blackout(100, _layer="master") with Dissolve(2)
    $ renpy.scene()
    $ block_walk_music = True
    $ loc_cur = loc_homeless_start_5
    $ diary_list = []
    $ emile.add_love(1500)
    if temp_var_1:
        $ npc_race_picker()
        $ player.generate_pre_game_stats(pre_bf, amount=numgen(0,300), children=False, fertility=0.05)

    $ t._monthnames = t.month_order("Winter")
    $ t.hour = numgen(1,2)
    $ t.minute = numgen(5,55)
    $ t.day = numgen(14,25)

    play music music_intro
    $ weather_var = 1


    $ dis_residential.locked = True
    $ dis_school.locked = True
    $ loc_kitchen.locked = True
    $ loc_hospital_entrance.locked = True

    $ player.hair_fringe = numgen(1, 6)
    $ player._hair_length = 1
    $ player.hair_colour = random(hair_colours_custom_list)
    $ player.eye_colour = random(eye_colours_custom_list)
    $ player.breasts = numgen(1, 3)


    $ player.perk_list = []
    $ player.add_perk(perk_survivor, origin=True)
    $ player.add_perk(perk_smoker)
    $ player.cycle_gamestart_randomiser()


    $ inv.take(item_cigs, 42)
    $ inv.take(item_preg_test)
    $ inv.take(item_energyfood)
    $ inv.take(item_scrap_cloth, 2)
    $ inv.take(item_scrap_junk)



    $ player._fitness = (numgen(22,30))
    $ player._confidence = (numgen(22,30))
    $ player._int = (numgen(22,30))
    $ player._mood = (numgen(2,15))
    $ player._tired = (numgen(25, 40))



    $ bruise.harm("face", numgen(1,3))
    $ bruise.harm("chest", numgen(1,3))
    $ bruise.harm("belly", numgen(1,3))
    $ bruise.bruise_ass()


    $ player.hygiene = 0


    $ wardrobe.take(item_coat_4, dress=True)
    $ wardrobe.take(item_top_25, dress=True)
    $ wardrobe.take(item_pants_5, dress=True)
    $ wardrobe.take(item_bottom_18, dress=True)


    $ daily.bottom_primary_colour = "custom5"
    $ daily.bottom_secondary_colour = "custom3"
    $ daily.top_primary_colour = "custom1"
    $ daily.top_secondary_colour = "custom1"
    $ daily.coat_primary_colour = "custom1"
    $ daily.coat_secondary_colour = "custom2"
    $ daily.pants_primary_colour = "custom10"
    $ daily.pants_secondary_colour = "custom10"

    $ party.bottom_primary_colour = "custom5"
    $ party.bottom_secondary_colour = "custom3"
    $ party.top_primary_colour = "custom1"
    $ party.top_secondary_colour = "custom1"
    $ party.coat_primary_colour = "custom1"
    $ party.coat_secondary_colour = "custom2"
    $ party.pants_primary_colour = "custom10"
    $ party.pants_secondary_colour = "custom10"

    $ home.top_primary_colour = "custom1"
    $ home.top_secondary_colour = "custom1"
    $ home.pants_primary_colour = "custom10"
    $ home.pants_secondary_colour = "custom10"

    $ party.top = 25
    $ party.pants = 5
    $ party.bottom = 18

    $ home.pants = 5
    $ home.top = 25

    $ player.brow = 3
    $ player.mouth = 8
    $ player.uncover()
    if player.vsex == 0:
        $ player.add_perk(perk_virgin)

    show screen background_scene(_layer="bg_screen")
    show screen pc_avatar(_layer="pc_avatar")
    show screen foreground_scene(_layer="fg_bg_screen")
    show screen right_menu
    $ clean_screen()
    show screen blackout(number=0, _layer="master") with dissolve
    $ renpy.hide_screen("blackout", layer="master")
    pc "Ugn!"
    $ walk(loc_checkpoint)
    $ player.face_shock()
    pcm "Fuck fuck. Need to run!"
    $ walk(loc_homeless_start_1)
    $ player.face_worried()
    pcm "I can still hear people shouting!"
    $ c.coat = 0
    $ wardrobe.drop(item_coat_4)
    $ walk(loc_homeless_start_2, trans=hpunch)
    $ blood.face = 5
    $ player.face_pain()
    pc "Ugn!"
    pc "Err..."
    pcm "No time. Gotta run!"
    $ walk(loc_homeless_start_3)
    $ player.face_shock()
    pc "*HUFF* *HUFF* *HUFF*"
    pcm "Did I lose them?"
    pcm "..."
    pcm "I can't hear anything."
    pcm "..."
    $ player.face_worried()
    pcm "What in the hell happened?"
    pcm "I was just running from some lunatics and ended up running straight into some checkpoint with police looking people."
    pcm "Good job they were far more interested in the lunatics following me otherwise I would never have got past them."
    pc "*Huff*"
    $ player.force_cover_breasts = True
    pcm "Fuck it's freezing!"
    pcm "Should I go back and get my coat?"
    if player.pregnancy >= 2:
        pcm "Ugh, I am not waddling back there. They would catch me."
        pcm "No idea how I managed to even get away. Not like I can run fast with this belly."
    else:
        pcm "No chance. I'd probably get caught."
    pcm "Hmm, but where am I?"
    pcm "Pretty sure I can hear voices further in..."
    pcm "..."
    $ walk(loc_homeless_start_4)
    pcm "Hmmm, quite a few people..."
    pcm "Most of them are women. They are dressed kinda..."
    pcm "Yeah, pretty sure I can guess."
    pcm "Means no one will notice me."
    pcm "I hope..."
    $ walk(loc_truckstop)
    pcm "Yeah, pretty busy. I need to just blend in."
    pcm "But what happened to [emile.name]? She was right behind me then she wasn't."
    pcm "Maybe I should have a look around."
    pcm "Hmmm..."
    $ loc_truckstop.visited = True
    $ log.assign("Lost and alone")
    $ log.qvar = log._findquest(qid="Lost and alone")
    $ block_walk_music = False
    $ diary_people_list = []
    $ add_to_list(diary_people_list, emile)
    $ diary_list = []
    $ diary_first_day = Diary_Class("New town, new life", "I have no idea what is going on. My sister and I were just driving to a place we had heard was a bit of a safe haven, when somehow my sister crashed the car we were driving.\n\nBefore I knew it, people were shouting and coming after us. " + If(player.pregnancy >= 2, "We just ran! Not an easy task considering I am carrying a giant belly with me. I must have looked like an elephant crashing through the tress.", "We just ran!") + " I managed to somehow get past the checkpoint in the confusion but when I looked back I realised I was alone. " + If(player.pregnancy >= 2, If(emile.showing, "She is pregnant too, so must have been just as hard for her to run as it was for me.", "How in the hell did my fat arse manage to outrun her?"), "") + "\n\nI need to find my sister.")
    $ emile.bio_text = "She is my sister. \nAfter getting into a car crash on the way to Blaston, we ended up separated. I hope she is okay and we can manage to meet up again soon."

    if player.showing:
        $ add_to_list(quest_homeless_start.list, "pc_preg")
    if emile.showing:
        $ add_to_list(quest_homeless_start.list, "emile_preg")
    jump loc_truckstop_visit

label start_homeless_postsearch:
    pcm "Hmm, I have looked around the local area and can't find [emile.name]..."
    pcm "Hope she is okay."
    pcm "Can't imagine what would happen if those people caught her."
    pcm "..."
    pcm "Well, I can't stand around here freezing my ass off. I need to find somewhere to sleep."
    pcm "Guess I will look around for a place to stay. Can look for [emile.name] at the same time."
    $ log.markdone("quest_homeless_start_01")
    jump travel

label start_homeless_comment_1:
    pcm "Can't see [emile.name] anywhere. I should look around some more."
    jump travel
label start_homeless_comment_2:
    pcm "So cold now. Gotta find [emile.name] then try and find somewhere warm."
    jump travel
label start_homeless_comment_3:
    pcm "Ung. I'm gonna be feeling that car crash for a while."
    jump travel

label start_homeless_meet_sister:
    "Voice" "[name]?! Is that you??"
    $ player.face_worried()
    pcm "Huh?"
    "I look around and see someone running towards me."
    $ player.face_shock()
    pc "[emile.name]?"
    show emile worried at right1 with dissolve
    emile.name "[name]! *Huff* *Huff*"
    emile.name "I finally found you."
    $ player.face_happy()
    pc "Yeah, I've been looking all over for you."
    emile.name "Let me... Catch my breath... *Huff*"
    pc "What happened to you? I ran and you were gone."
    emile.name "*Huff*"
    emile.name "Yeah... I got caught by security."
    show emile neutral
    pc "Ugh, shit. But you are free now?"
    emile.name "Yeah, they didn't much care about me. They were more interested in the people attacking."
    pc "Attacking? Those lunatics that chased us?"
    emile.name "Well yeah. Turns out they weren't chasing us."
    pc "Looked that way to me."
    emile.name "They were setting up an ambush or something, and when we crashed they got spooked and attacked."
    pc "Wow... Okay..."
    $ player.face_neutral()
    emile.name "Whatever, doesn't matter."
    emile.name "You are alive! I was starting to worry."
    pc "Yeah so was I..."
    if "emile_preg" in quest_homeless_start.list:
        pc "I was worried with your belly you couldn't run and got caught or something."
        emile.name "I did get caught. Just not by the lunatics."
        emile.name "Security stopped me but realised I wasn't one of those guys so pretty much just left me alone."
        emile.name "So what have you been doing? Been safe?"
        pc "Ugh, when I arrived I managed to find a tin shack to stay in."
    if "pc_preg" in quest_homeless_start.list:
        emile.name "How did you get away?"
        pc "No idea. I just waddled my arse through some bushes and kept going until I was ready to collapse."
        emile.name "Haha, I bet that was a sight to see."
        pc "Yeah, not a pretty one."
        emile.name "So what have you been doing? Been safe?"
        pc "Ugh, when I arrived I managed to find a tin shack to stay in."
    elif player.showing and not "pc_preg" in quest_homeless_start.list:
        emile.name "So... You have gotten bigger since I last saw you."
        if player.preg_father_class == pre_bf:
            pc "Yeah... Seems I brought this to [town] with us but I didn't know at the time."
            emile.name "Oh? Wow... Okay... Congratulations?"
            pc "Ha yeah right. Don't see him the entire time this chaos starts but he leaves this with me."
            pc "Ugh."
            emile.name "So what have you been doing? Been safe?"
            pc "Ugh, when I arrived I managed to find a tin shack to stay in."
        elif player.soldbaby:
            pc "Ugh yeah..."
            pc "Ended up with this trying to earn some money to get by."
            emile.name "Ah fuck. It's been that bad has it?"
            pc "Wouldn't call it good. Ended up living in a tin hut with the junkies and whores."
            pc "Not much else to do to earn in a place like that."
        elif player.rapebaby:
            pc "Yeah..."
            pc "This wasn't something that got here by choice."
            emile.name "Oh..."
            pc "The tin shack I am living in isn't exactly a safe place to live."
        else:
            pc "Yeah, not like I can get my hands on any protection, so kinda ended up with this..."
            emile.name "Oh? Wow... Okay... Congratulations?"
            pc "Yeah right. My tin shack with junkies and whores all around is the perfect place to get big and fat."
    elif player.sold > 10 and player.slutty:
        emile.name "You look... Errr..."
        pc "Like a cheap whore?"
        emile.name "Your words, not mine."
        pc "Ugh. It's because I am. Not easy to make money when you arrive in some shithole with only a tin shack to sleep in."
        emile.name "Oh..."
    else:
        emile.name "So what have you been doing? Been safe?"
        pc "Ugh, when I arrived I managed to find a tin shack to stay in."
    emile.name "A tin shack?"
    pc "Yeah, some place in the slums that whores or junkies stay in. Not really much else on offer so I have been living there."
    emile.name "Damn..."
    pc "You been managing any better? I've been keeping a lookout for new people wandering in looking for a place hoping to find you."
    emile.name "Yeah, actually after getting caught by security I ended up in contact with some people."
    emile.name "Long story short, I got a place to stay and some work. Been spending my free time looking around for you."
    pc "Oh nice. Your place better than a tin shack?"
    emile.name "Yeah it is. Actually considering your shithole, maybe you should stay with me."
    $ player.face_annoyed()
    pc "Hey! My place is not a shithole!"
    $ player.face_neutral()
    pc "I would have to do a lot of renovating to elevate it to shithole standards."
    pc "And get rid of my junkie whore neighbour that keeps me awake from all the fucking."
    pc "And a proper lock on my door so drunks don't try and join me in bed in the middle of the night."
    pc "Mmm, a shithole would be good living."
    emile.name "I am not sure if you are joking or not..."
    emile.name "But come to the hospital on Revel, ask for me and we can chat some more. Maybe move you in with me."
    pc "Okay."
    emile.name "I have to go and speak to someone and get things sorted. Come by soon."
    pc "Sure. Glad to see you are okay."
    emile.name "So am I."
    hide emile with dissolve
    pcm "Hospital on Revel street? Did she get herself a fancy job there or something?"
    $ loc_hospital_entrance.locked = False
    $ log.markdone("quest_homeless_start_03")
    jump travel

label start_homeless_meet_sister_institute:
    $ walk(loc_hospital_office, trans=False)
    show tucker at right1 with dissolve
    tucker.name "Hello Miss [sname]."
    $ player.face_worried()
    pc "Err, I was looking for [emile.name]."
    tucker.name "You are in the right place."
    $ player.face_neutral()
    pc "Oh? Sorry [emile.name]. I didn't recognise you in that snazzy new suit."
    tucker.name "Have a seat Miss [sname]."
    pc "Err, strange guy in an office asking me to sit on his sofa? Is there a camera set up somewhere?"
    tucker.name "You should know as much as anyone there are no cameras any more."
    pc "Oh, so this is just your perverted role play then?"
    tucker.name "..."
    show emile suitvest happy at right3 with dissolve
    emile.name "[name]!"
    $ player.face_shock()
    pc "There are two [emile.name]'s!"
    show emile neutral
    emile.name "What?"
    pc "And you are both wearing suits."
    emile.name "Err, yeah..."
    $ player.face_neutral()
    pc "Well okay, as long as the pay is good."
    emile.name "What the hell are you talking about?"
    emile.name "Whatever. This is [tucker.fullname]. He is the head of the hospital."
    tucker.name "Hello Miss [sname], It's good to meet you."
    pc "Hi, [name]. Did [emile.name] sit on your sofa?"
    if emile.showing and not "emile_preg" in quest_homeless_start.list:
        pc "She wasn't pregnant when we arrived here, so I guess congratulations..."
    show emile angry
    emile.name "Is it too late to just kick her back out?"
    tucker.name "Probably."
    tucker.name "[emile.name] has told me a lot about you Miss [sname]. I hope we can work well together."
    $ player.face_worried()
    pc "Work? [emile.name] just told me to come here because she has a nicer place to live than my junkie den."
    show emile neutral
    emile.name "Well yeah. But then [tucker.name] decided we might be able to put you to work."
    if player.sold > 5:
        pc "Hopefully better than the work I have been doing since I arrived."
        emile.name "How have you been making money?"
        pc "I live in the slum. Take a guess."
        emile.name "I've don't think I have been to the slum before."
        pc "Everyone who lives there is a junkie or a whore. Usually both. Until they turn into a corpse..."
        emile.name "Oh..."
    else:
        pc "Well always looking for work that doesn't involve me taking some guy back to my tin hut."
        pc "Not a lot of work that doesn't involve someone wanting to bend me over. Been trying to avoid that."
        pc "I'm assuming [tucker.sname] doesn't want to bend me over?"
        emile.name "I don't think so..."
        emile.name "Although it is weird he has the sofa in here."
        pc "Yeah."
        tucker.name "..."

    tucker.name "Well first, why don't you help Miss [sname] settle into her new home. We can discuss the details later."
    emile.name "Okay."
    $ player.face_neutral()
    pc "[name]."
    tucker.name "Come and see me once you have your bearings Miss [sname]."
    pc "Right..."
    hide tucker
    hide emile
    $ walk(loc_hospital_lobby)
    $ walk(loc_hospital_entrance)
    show emile suitvest at right1 with dissolve
    pc "So a nice new place?"
    emile.name "Well wouldn't call it that nice. Or even new. But much better than the slums."
    pc "Yeah almost anything would be better."
    $ walk(loc_revel)
    emile.name "Not too far. We can walk and catch up."
    "We walk and talk about what we have been up to since we got separated."
    "I can't help but get the feeling [emile.name] is being a bit evasive."
    $ walk(loc_residential)
    "But I can't really blame her, it's not like I am telling the whole truth either."
    "Living in the slums means you want to leave a lot of the details out of the story."
    emile.name "Just around here."
    pc "Oooh, nice part of town."
    $ walk(loc_stairwell)
    pc "Fancy."
    $ walk(loc_kitchen)
    pc "Even has separate rooms?"
    $ walk(loc_bedroom)
    $ player.face_neutral()
    emile.name "And here we are."
    pc "Looks nice."
    emile.name "There are some clothes already in the wardrobe. Some stuff for the academy you have been signed up for."
    pc "Academy?"
    emile.name "Yeah, lot's of folk our age go there. Helps get us adjusted to the town and life here."
    pc "Errr, pretty sure I am as adjusted as I can be."
    emile.name "Probably. But you have been signed up anyway. Go or don't go. Up to you."
    emile.name "A new flatmate moved in recently, she also attends."
    pc "Oh?"
    emile.name "I'm sure you will bump into her soon enough."
    pc "Right."
    emile.name "Anyway, I'll leave you to it. I don't think you need me to hold your hand."
    pc "Yeah, see you round."
    emile.name "Oh by the way, this place is nicer but you have to pay."
    $ player.face_shock()
    pc "What? My shithole was free."
    emile.name "Landlords office is in the courtyard. [oskar.name], bit of a cunt. Go see him."
    pc "Right."
    hide emile with dissolve
    pc "Right then..."
    $ log.markdone("quest_homeless_start_04")
    $ log.assign("Introduction to The Institute")

    $ rent_pay(rent_total_owed(), cash=False, notif=False)
    $ wardrobe.take(item_top_12)
    $ wardrobe.take(item_bottom_5)
    $ wardrobe.take(item_socks_3)
    $ wardrobe.take(item_top_8)
    $ wardrobe.take(item_bottom_8)

    $ dis_residential.locked = False
    $ dis_school.locked = False
    $ loc_kitchen.locked = False
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
