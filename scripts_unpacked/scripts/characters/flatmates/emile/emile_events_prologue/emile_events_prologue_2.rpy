init python:
    def emile_prologue_event_2_check_swimwear():
        top = False
        bottom = False
        outfit = False
        for i in item_clothes_list:
            if wardrobe.qty(i) and i.type == "top" and "swim" in i.outfit:
                top = True
            elif wardrobe.qty(i) and i.type == "bottom" and "swim" in i.outfit:
                bottom = True
            elif wardrobe.qty(i) and i.type == "outfit" and "swim" in i.outfit:
                outfit = True
        if (top and bottom) or outfit:
            return True
        return False

    def emile_prologue_event_2_set_swimwear():
        if player.has_perk(perk_male) and player.body_conf >= -140:
            pc_set_clothing(work, "top", 1, trans_pri="trans_trans")
            pc_set_clothing(work, "bottom", 1, trans_pri="trans_trans")
            wardrobe.take(item_top_1)
            wardrobe.take(item_bottom_1)
        elif player.has_perk(perk_exhibitionist):
            pc_set_clothing(work, "bottom", 3, trans_pri="trans_sheer")
            wardrobe.take(item_bottom_3)
        elif player.has_perk(perk_bimbo):
            pc_set_clothing(work, "top", 3, colour_pri="hotpink")
            pc_set_clothing(work, "bottom", 3, colour_pri="hotpink")
            wardrobe.take(item_top_3)
            wardrobe.take(item_bottom_3)
        else:
            pc_set_clothing(work, "top", 2,)
            pc_set_clothing(work, "bottom", 2)
            wardrobe.take(item_top_2)
            wardrobe.take(item_bottom_2)

label emile_prologue_event_2:
    emile.name "Ready to head out somewhere?"
    pc "What did you have in mind?"
    emile.name "I thought since the weather is nice, we could head to the lake."
    if loc_lake.visited and player.has_perk(perk_male):
        pc "Hold on, I checked that place out already. The lake is a beach."
        emile.name "Yeah."
        pc "A beach. I'll need to wear a bikini..."
        emile.name "Yeah. And?"
        pc "..."
        pc "I woke not long ago without my cock and now you want to parade by arse about in a bikini?"
        emile.name "Ah..."
        emile.name "Well, it's something you need to get used to anyway. So suck it up."
        emile.name "We going?"
    menu:
        "Sure, let's go to the lake":
            pc "Okay, sounds good."
            jump emile_prologue_event_2_start
        "No, think I would prefer to go alone":

            emile.name "You sure? I won't be around for long so won't really get another chance."
            menu:
                "Actually, yeah let's go out":
                    jump emile_prologue_event_2_start
                "Yeah I'm sure.":
                    emile.name "Ok, but don't wander around too late and be home before dark."
                    pc "Right. Okay."
                    jump travel

label emile_prologue_event_2_start:
    $ emile.dict["prologue_event"] += 1
    if "home" in tab_top:
        pc "Let me change first though."
        $ pc_dress_event("daily", loc_bedroom)
        show emile at right1 with dissolve
        $ walk(loc_kitchen)
        pc "Ready."
    show emile at right1
    $ walk(loc_stairwell)
    if loc_lake.visited:
        pc "Checked the lake out before. It seems... Nice?"
        emile.name "You don't sound so sure."
        pc "Well, a lot has changed. A year ago I wouldn't have had issue with the place, but now..."
        if player.has_perk(perk_male):
            pc "And let's not forget I'm not a guy any more. The beach is going to feel totally different than before."
    else:
        pc "So, the lake? It a nice place?"
        emile.name "About as nice a place as any round here."
        pc "Seems to be a running theme."
        emile.name "Yeah..."
    $ walk(loc_residential)
    emile.name "So we'll get the bus there. They run all day and night and go through all the major areas in [town]."
    $ walk(loc_busstop_residential)
    pc "Yay. The only thing worse than public transport is public transport during the collapse of society..."
    emile.name "Yup! Let's go."
    hide emile with dissolve
    $ walk(loc_bus_interior)
    pc "..."
    show emile at right6 with hpunch
    $ player.grope_ass()
    emile.name "Don't get too close to anyone."
    $ player.face_annoyed()
    pc "Or they will start feeling up my arse? Too late."
    $ player.face_angry()
    $ player.grope_end()
    with hpunch
    pc "Ung! Go away..."
    emile.name "Better?"
    $ player.face_neutral()
    pc "Yeah."
    if loc_school.visited and t.day < 3:
        pc "Decided to pop by the academy place and check it out."
        emile.name "Oh?"
        pc "Looks a bit old and run down, but an okay place I suppose."
        emile.name "Not been there myself. You go inside?"
        pc "No, Thought I would wait til it's open properly first."
    elif robin.has_met:
        pc "Met one of my flatmates, you see her too?"
        emile.name "[robin.name]? Yeah she came and said hello. Seems nice."
        pc "Mmm, seems she just moved in so good to have another stranger around."
        emile.name "Yeah."
    elif loc_pub.visited:
        pc "Went down to revel and checked out a pub that was there."
        emile.name "Oh Drinking your woes away already?"
        pc "Was out and about looking for a job."
    else:
        pc "That park seemed like a nice place."
        emile.name "It is. One of the few nice things around this place. It's pretty huge and covers most of the places where people live."
        pc "Mmm."
    emile.name "We are close. Let's go."
    hide emile with dissolve
    $ walk(loc_lake, trans=False)
    show emile at right1 with dissolve
    emile.name "Changing room over there that leads to the beach and some kiosks over on the boardwalk."
    if loc_beach_hangout.visited or loc_boardwalk.visited:
        pc "Yeah, check this place out already remember?"
        emile.name "Ah yeah."
    else:
        pc "Hmm, ok."
    emile.name "I assume you don't have anything beach worthy? Wait here and I'll pick something up for you."
    if player.has_perk(perk_male, notif=True):
        jump emile_prologue_event_2_male
    else:
        jump emile_prologue_event_2_female

label emile_prologue_event_2_female:
    hide emile with dissolve
    if emile_prologue_event_2_check_swimwear():
        pcm "Err, run off before I can answer. I do have something I can wear..."
    elif player.has_perk(perk_exhibitionist):
        pcm "Err, run off before I can answer. I don't need to wear anything on the beach."
    else:
        pcm "Right then, just run off leaving me all alone here..."
    pcm "Whatever..."
    show emile at right1 with dissolve
    emile.name "Right, here you go. Let's change."
    hide emile with dissolve
    pcm "Okay then..."
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_locker_girls_stall)
    pcm "Right then..."
    $ pc_strip_work()
    $ pc_striptease()
    $ tab_top = "work"
    $ emile_prologue_event_2_set_swimwear()
    pcm "Let's see..."
    if player.has_perk(perk_exhibitionist, notif=True):
        pcm "Right... That's why she was so quick to just run off..."
        pcm "Damn bitch knows me too well..."
    elif player.has_perk(perk_bimbo, notif=True):
        pcm "Damn [emile.name] knows me too well..."
    $ pc_dress_slow()
    pc "Okay then..."
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_hangout)
    pcm "Hmm, looks nicer than I thought it would."
    show emile swim at right1
    emile.name "All good?"
    pc "Yeah"
    "*** NOTE *** THIS EVENT IS CURRENTLY INCOMPLETE SO ENDING HERE."
    jump travel

label emile_prologue_event_2_male:
    if ((swim.bottom and swim.top) or swim.outfit) and swim.appropriate:
        pc "Actually I do have something to wear."
        emile.name "Oh? Been here before?"
        if loc_beach_hangout.visited:
            pc "Yeah, I checked the beach out already."
            emile.name "Great, go get changed then and I'll meet you on the beach."
        else:
            pc "No, I just saw something and picked it up."
            emile.name "Ok, well whatever. Go get changed and I'll meet you on the beach."
        pc "Okay."
        hide emile with dissolve
        jump emile_prologue_event_2_male_change_own

    if loc_beach_hangout.visited:
        hide emile with dissolve
        if emile_prologue_event_2_check_swimwear():
            pcm "Err, run off before I can answer. I do have something I can wear..."
        elif player.has_perk(perk_exhibitionist):
            pcm "Err, run off before I can answer. I don't need to wear anything on the beach."
        else:
            pcm "Right then, just run off leaving me all alone here..."
    else:
        $ player.face_shock()
        pc "Wait what? Beach worthy?"
        if emile_prologue_event_2_check_swimwear():
            pc "I do have something but you want me to parade round the beach near naked?"
        else:
            pc "What do you mean by \"beach worthy\"? You want me to parade around in a bikini?"
        emile.name "Well, yes? You can't really go in your clothes. Will get soaked going through the showers and end up with sand everywhere."
        $ player.face_worried()
        pc "Ugh... Not sure I am comfortable walking around like that."
        emile.name "Well it's that or we go home. Come on, this is your life now."
        pc "..."
        hide emile with dissolve
        $ player.face_neutral()
        pcm "Right then, just run off leaving me all alone here..."
    show emile at right1 with dissolve
    emile.name "Here you go. Let's change."
    hide emile with dissolve
    pcm "Okay then..."
    hide emile with dissolve
    jump emile_prologue_event_2_male_change_emile

label emile_prologue_event_2_male_change_own:
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_locker_girls_stall)
    $ pc_striptease()
    pcm "Even though I got my own stuff, hanging out on the beach dressed near naked is still a bit daunting..."
    $ tab_top = "swim"
    $ pc_dress_slow()
    show sb_pose_upvag with dissolve
    if c.slutty:
        pcm "Okay then..."
        if c.thong:
            pcm "Swimwear that rides right up my arse and going out in public with it. People are going to get a good look."
        else:
            pcm "These things are tiny and I am out in public wearing them. People are going to get a good look."
        pcm "Why did I buy these in the first place? Do I want people to look?"
        pcm "Ugh..."
    else:
        pcm "Right... Arse still hanging out but that's normal I suppose..."
        pcm "Didn't pay much attention before but these things are tiny even in the more modest ones."
        pcm "Skin tight and right up my arse."
    hide sb_pose_upvag with dissolve
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_hangout)
    $ player.face_worried()
    jump emile_prologue_event_2_male_beach_arrive

label emile_prologue_event_2_male_change_emile:
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_locker_girls_stall)
    pcm "Right then..."
    $ pc_strip_work()
    $ pc_striptease()
    $ tab_top = "work"
    $ emile_prologue_event_2_set_swimwear()
    pcm "Let's see..."
    $ pc_dress_slow()
    show sb_pose_upvag with dissolve
    if loc_beach_hangout.visited:
        pcm "Well, not like I haven't hung out on the beach before in my swimwear..."
        if c.slutty:
            pcm "Did she have to get me something so small though? It barely covers my arse."
            pcm "And aren't bikinis supposed to hide things? This is already see through and it isn't even wet yet..."
            pcm "Damn [emile.name]!"
    elif c.slutty:
        $ player.face_worried()
        pcm "What the hell..."
        pcm "These are tiny!"
        pcm "And it's not even wet and it's already see through!"
        pcm "Fucking [emile.name]!"
        pcm "She did this on purpose..."
    else:
        pcm "Well... I suppose as far as beachwear goes, it's not too bad..."
        pcm "Still basically showing off my tits and arse though."
        if player.breasts == 1:
            pcm "At least they aren't so big to attract attention."
        elif player.breasts == 3:
            pcm "These things are basically spilling out of the top. Going to get all manner of attention."
    pcm "*Sigh*"
    hide sb_pose_upvag with dissolve
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_hangout)
    $ player.face_worried()
    jump emile_prologue_event_2_male_beach_arrive

label emile_prologue_event_2_male_beach_arrive:
    pc "..."
    pcm "At least this place seems alright. Expected a lot worse when I heard there was a beach but it's all relatively normal here."
    pcm "Normal still means there will be guy's staring at the girls though..."
    show emile at right1 with dissolve
    if "swim" in tab_top:
        if c.thong or c.slutty:
            emile.name "Wow, when you said you had your own swimwear I didn't expect you to come out like this!"
            pc "It's swimwear isn't it?"
            emile.name "Yeah, for someone who wants to be taken off by some beach hunk."
            emile.name "Err... Do you want to be taken off by some beach hunk?"
            $ player.face_annoyed()
            pc "Shut up!"
            emile.name "Haha. Well don't need you getting pregnant right after getting out the hospital. So be careful."
            pc "Ugh..."
        elif c.outfit:
            emile.name "Err, more for swimming and not so much for the beach. But I guess it works."
            pc "What? Whats wrong with this?"
            emile.name "Nothing. It gets the job done."
            $ player.face_sus()
            pc "You just want to parade my arse around the beach."
            emile.name "Well, you are doing that regardless. So might as well wear something that doesn't leave tan lines."
            pc "I am okay with this."
        else:
            emile.name "Looking good. I thought you would come out with a knee length one piece or something."
            emile.name "Or maybe the other direction. A C string bikini or something."
            pc "The hell is a C string?"
            emile.name "A woman's worst enemy. About one step away from butt plug underwear."
            $ player.face_shock()
            pc "Wait what? They do such things?"
            emile.name "Err... Probably? Perverts come up with all manner of craziness."
            $ player.face_sus()
            pc "Does yours have a butt plug?"
            emile.name "No! Shut up!"
            pc "Riiight..."
    else:
        emile.name "All good?"
        if c.slutty:
            $ player.face_annoyed()
            pc "If you consider the bikini up the crack of my arse \"all good\", then yes."
            pc "Looks the same as your one but I notice I'm the only one wearing something that's see through."
            emile.name "Well, you seemed to be adjusting well to this new situation so I thought I would get you something daring."
            show emile happy
            emile.name "Plus it was cheaper."
            pc "Daring? If I bend over, people will see my arsehole!"
            show emile neutral
            emile.name "Then don't bend over unless you want them to see it."
            pc "Ugh!"
        else:
            pc "Can't say walking around the beach dressed like this is \"all good\", but it is what it is I suppose."
            emile.name "Yup. You might feel strange now but you'll get used to it."
            pc "And get used to guy's eyeing up my arse like the guys behind you?"
            emile.name "Yup. Normal."
    emile.name "Come on. Let's find somewhere to relax."
    $ player.face_neutral()
    pc "Sure..."
    $ walk(loc_beach_gym)
    emile.name "I like to hang out here and watch people play."
    pc "Mmm, you ever joined them?"
    emile.name "A couple of times. But it's not quite my thing."
    emile.name "Here is good."
    show activity_beach_lay emile
    hide emile
    with dissolve
    if player.breasts == 3:
        pc "Uff. Laying down on my stomach is a bit more difficult with these huge new additions."
        emile.name "Haha yeah. I was going to ask what the hell they were thinking giving you ones that big. But we already know what they were thinking."
        pc "Or what was doing the thinking..."
        emile.name "Haha!"
    if c.slutty:
        pc "Hope we are not giving a good view to all the perverts round here."
        emile.name "Probably are. But who cares."
        pc "Err... I do?"
        emile.name "No you don't. Your just a bit self conscious. It'll pass."
        pc "You get used to showing off your arse to all the men on the beach?"
        emile.name "If you want to enjoy being here, yes."
    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        pc "Bet it's good to get off your feet with that belly of yours."
        emile.name "Damn right. The sand between my toes also feels nice."
        pc "Better not have smelly feet. I have to live with you."
        emile.name "Oh shush!"

    pc "They let anyone join in?"
    emile.name "The volleyball? Yeah. Mostly just messing about and having fun in the sun. Not like it's a competition or anything."
    pc "And the guys there. They just there to look at the girls or they play as well?"
    emile.name "Usually ogle, but they join sometimes when players are short."
    pc "And the girls don't mind?"
    emile.name "Ogling is something you get everywhere. And at least they don't do anything."
    if c.thong or c.slutty:
        if c.thong:
            emile.name "Although with you and that thong up your arse, they might come and say hello to you."
        else:
            emile.name "Although with you showing off in that, they might come and say hello to you."
        pc "Not gonna let this go are you?"
        emile.name "Of course not. Why not take your top off as well and give everyone a show?"
        menu:
            "I think I will":
                $ add_to_list(emile.list, "prologue_beach_topless")
                pc "Just to annoy you, I think I will!"
                emile.name "Yeah right!"
                $ c.top = 0
                emile.name "Oh wow. You actually did!"
                emile.name "Err... Right then... I'm sittin' here with a pervert"
                pc "Going to do the same?"
                emile.name "Really? You expect me to as well?"
                pc "Well, don't need to if you don't want to. I mean it was only you making fun of me and now your scared and all."
                emile.name "Haha. Okay then."
                show activity_beach_lay emile_nude with dissolve
                emile.name "Satisfied?"
                pc "Actually surprised you did it."
                emile.name "Can't have my former brother showing me up."
                menu:
                    "Take off bottoms as well":
                        $ add_to_list(emile.list, "prologue_beach_nude")
                        $ c.bottom = 0
                        emile.name "Err... What are you doing?"
                        pc "Showing you up?"
                        emile.name "Right... Bit far isn't it?"
                        pc "Get used to it. Isn't that what you keep telling me?"
                        emile.name "Haha, I suppose."
                        emile.name "Ok, there. We are both stark naked. Happy?"
                        pc "Nothing more to take off..."
                        $ player.add_perk(perk_exhibitionist, notif=True)
                    "Stay like this":
                        pc "Eh. Maybe not. Tits on a beach is kinda normal but think that's a bit far."
            "I don't think so":

                pc "Why don't you? It's you who seems used to all this attention."
                emile.name "Na, it can be seen as an invite. Plus not gonna sit here naked on my own."
                pc "Oh? Would do it if I did?"
                emile.name "Naa, probably not."
    else:
        emile.name "Sometimes they come to chat, but are quick to go away when you tell them to."
        pc "You seem to know a lot about them."
        emile.name "Yeah, I come here now and than. Chatted to a few people. A girl sitting here alone tends to attract attention."
        pc "You don't sound upset."
        emile.name "Why should I be?"
        pc "Guys coming up and trying to flirt with you doesn't annoy you?"
        emile.name "Happens everywhere you go. And at least the people here are sober and not handsy cretins."
        emile.name "Gets boring alone so sometimes having someone to chat to can be nice. Helps kill the time at least."
    if "prologue_beach_topless" in emile.list:
        pc "Nice boobs by the way."
        emile.name "Thanks. All natural unlike yours."
        pc "Mine are natural... I think... No silicone anyway."
        emile.name "Not sure created in a lab counts."
        emile.name "Err... Hold on..."
        pc "What?"
        emile.name "Why are you looking at my tits?"
        pc "Well, they are right in front of me."
        emile.name "I almost forgot. You better not be getting hard looking at them!"
        pc "Yeah, doubt anything is making me hard any time soon."
        emile.name "Pervert. I got all caught up in seeing how far you would go and I probably just got tricked into undressing for my brother."
        pc "Hey. It was you that mentioned it. Maybe my lesbo sister is trying to get a look at my tits!"
        if emile.days_pregnant > (global_pregnancy_length * 0.3):
            emile.name "Haha. Some lesbo I am. Sitting here pregnant."
            pc "Well, let's not make common sense get in the way of making fun of you."
            emile.name "Haha!"
        else:
            emile.name "Oh yeah. Lesbian [emile.name] trying to get some action off my bro-sis days after they come out a coma."
            emile.name "Better be careful. I know where you sleep."
            pc "Oh no! Better find some beach pervert to distract your naked arse while I do a runner."
            emile.name "A runner while also showing off your arse?"
            pc "Haha!"
    emile.name "I wonder if it's guys you are into now in the new body? How much is hormones and how much is yourself?"
    pc "Not even sure what colour or food I like right now."
    emile.name "Well, I can answer the food question. None. It's all shit now."
    pc "Ah fuck. Really?"
    emile.name "Yeah... Food is pretty scarce so not a lot of options."
    pc "Scarce? Doesn't look to me like people are going hungry. The women are thin but the guys are pretty buff."
    emile.name "Oh? Admiring the buff guys eh? Should I call some of them over for you?"
    pc "\"Some\"? Just out the hospital and you are trying to set a bunch of guys on me? Not sure this body could handle it."
    emile.name "Could find out."
    emile.name "Hey buff guys! My sister wants to see if she likes dick!"
    pc "Haha fuck you!"
    emile.name "Scarce is the wrong word anyway. Plenty of food but most of it as simple as it comes."
    emile.name "Get used to cabbage. It grows quick in shit weather and is easy to deal with. Or so I hear. It's bloody everywhere."
    emile.name "Most of the meat you will get these days is that pink paste stuff."
    pc "Most?"
    emile.name "If it's not pink paste, then it's probably pigeon, fox, dog... Rat maybe..."
    pc "Ugh. So better stick to the pink paste."
    emile.name "Yup. It will have all of those in there."
    pc "Ah fuck!"
    emile.name "Haha!"
    if c.slutty or c.exposed:
        jump emile_prologue_event_2_male_beach_men_join
    else:
        jump emile_prologue_event_2_male_beach_cont

label emile_prologue_event_2_male_beach_cont:
    hide activity_beach_lay
    show sb_onbelly
    with dissolve
    pc "Well, at least this place doesn't seem as dire as the rest of the places."
    emile.name "The beach?"
    pc "Yeah. Would have thought it more a swamp or something since no one looking after it."
    emile.name "So you had a look around at other places in [town]?"
    if loc_park.visited:
        pc "The park over the road seems alright. I mean, it's just a park. But at least it's not on fire."
        emile.name "Yeah, just avoid at night. Weird people hang out there."
    if loc_revel.visited:
        pc "Went to Revel street. Bit run down but people still go about their lives. And there is a pub there."
        emile.name "Oh, the pub is alright."
        if loc_pub.visited:
            pc "It is? Didn't see a single girl in there. Just drunk guys."
        else:
            pc "It is? Would have thought with all that's going on it would be a place to avoid."
        emile.name "One of the few places to get a drink around here. So you get used to it."
        pc "Used to it again? Seems I need to do a lot of that."
        if loc_market.explored:
            pc "Also had a wander round the market stalls. Guess there are no megastores anymore."
            emile.name "Nope. Looted from what I hear. Now got to go round the stalls like some medieval town and look for deals."
            pc "Ugh..."
    if loc_checkpoint.visited:
        pc "Got the bus and ended up at the checkpoint out of [town]. That place was grim..."
        emile.name "Yeah. Drives home all the shit that's going on round here."
        if loc_junk_entrance.visited:
            if loc_junk_entrance.explored:
                pc "Did checkout the nearby junkyard as well and met some nice scavver girl. Also kind of got told about work."
            else:
                pc "Did checkout the nearby junkyard as well but didn't have much time to look around."
            emile.name "Oh? I checked that place out ages ago. It... Was bad..."
            pc "Seemed alright when I was there."
            if loc_junk_entrance.explored:
                emile.name "What kind of work?"
                pc "Collecting junk like electronics or whatever and selling it off to them. Not a proper job."
            emile.name "Not been there since the first time. But looked like the kind of place where you are lucky if you are just gangraped."
            emile.name "I imagine most people end up with the neck cut open afterwards..."
            pc "Shit..."
    if loc_truckstop.visited:
        pc "Thought I would check out the diner you mentioned. Not sure what to make of that area."
        emile.name "No? Thought the hoards of junkie whores would have clued you in."
        pc "Well, there also seems to be decent stuff going on. Diner, truckers hanging out."
        pc "It's like you have normal innocent life going on around open depravity and desperation. Would be funny if it wasn't so depressing."
        if loc_highway.visited:
            pc "And went to the highway..."
            emile.name "Oh? Need cream for your arsehole?"
            pc "Huh?"
            emile.name "Only people that go there are people who bend over for money. Or for less reputable things."
            pc "Less reputable than whoring?"
            emile.name "Desperate times..."
    hide sb_onbelly
    show activity_beach_lay emile
    with dissolve
    emile.name "You watch the girls shake their arse while playing and keep an eye on our stuff."
    pc "What you doing?"
    emile.name "Last time I was here there was some kiosk over there selling drinks."
    pc "Ah ok."
    emile.name "Back in a bit."
    show activity_beach_lay alone with dissolve
    pcm "Should have asked her to get me something..."
    pcm "Wonder if it's booze or water? Doubt anyone is selling any cola these days."
    pcm "Bit early to get drunk..."
    $ relax(10)
    "I sit and watch the group playing volleyball but what gets my attention more is the actual lake."
    pcm "Water is pretty calm. Sun and sand makes it look like a proper beach but it's not. I wonder what is on the other side?"
    pcm "Only see trees and some hills. Are there people living there I wonder..."
    $ relax(10)
    "I sit and watch over the lake for a while to see if I can see any movement or signs of life over there."
    pcm "..."
    pcm "Isn't she taking her time?"
    pcm "Ah, here she comes... Who is that with her?"

    $ renpy.scene()
    show emile at left1
    show mateo at right1
    with dissolve
    pc "Took your time."
    emile.name "Sorry. Got caught up with something."
    guy "Hi."
    pc "Hey."
    guy "Well, I'm gonna head back to playing. Nice meeting you."
    emile.name "Bye"
    hide mateo
    with dissolve
    pc "Who was that?"
    show emile at right6 with dissolve
    emile.name "Someone I bumped into looking for the stand."
    pc "Did you find it?"
    emile.name "Ah no. He told me the guy isn't here."
    pc "Oh? You were gone for ages. Thought there was a queue or something."
    emile.name "Na, just took a while to realise I was wasting my time looking."
    pc "Right..."
    emile.name "Anyway, been here a while as well. Probably time for us to head off."
    pc "Yeah alright. Had enough of showing my arse off for one day."
    emile.name "Ready? Got all your stuff?"
    pc "Yeah."
    $ walk(loc_beach_hangout)
    jump emile_prologue_event_2_male_beach_redress

label emile_prologue_event_2_male_beach_men_join:
    hide activity_beach_lay
    if "prologue_beach_nude" in emile.list:
        show emile nude at left1
    elif "prologue_beach_topless" in emile.list:
        show emile swim_topless at left1
    else:
        show emile at left1
    show kaan at right1
    show mateo at right2
    with dissolve
    mateo.name "Hey, not want to join in?"
    $ player.face_worried()
    pc "Err, what?"
    mateo.name "Think they are short a player."
    if emile.showing:
        emile.name "Doubt I'll be doing much running around with this belly. Just here to relax. Why aren't one of you guys joining?"
    else:
        emile.name "Na, just here to relax. Why aren't one of you guys joining?"
    mateo.name "Was playing earlier but sun is out and just wanna relax now."
    pc "Why would they need an extra if they aren't playing a match?"
    mateo.name "Need even numbers. Someone has to drop out if they don't."
    pc "Ah."
    mateo.name "Interested?"
    pc "No, think I just want to hang out."
    pcm "Fuck, I'm standing here with my tit's out and these guys are chatting away like normal."
    pcm "Shoo them away [emile.name]!"
    emile.name "Is that guy selling drinks still around these days?"
    mateo.name "Yeah, over the way there. Want something?"
    emile.name "Yeah, can you show me?"
    pcm "What?!"
    mateo.name "Sure."
    emile.name "[name], keep an eye on our stuff."
    pc "Err..."
    pcm "Fuck!"
    hide emile
    hide mateo
    with dissolve
    pc "I..."
    kaan.name "Gone and left you behind."
    pc "Yeah..."
    kaan.name "Names [kaan.name]."
    pc "Like the tiger?"
    kaan.name "Close enough."
    hide kaan
    show activity_beach_lay kaan
    with dissolve
    if player.has_perk([perk_exhibitionist, perk_slut]):
        pcm "Fuck, I am laying here giving him a good eyeful. Naked in front of some guy I just met..."
        $ player.add_desire_random(50)
    elif "prologue_beach_nude" in emile.list:
        pcm "This would be a lot less awkward if I didn't have my arse on full display..."
    elif "prologue_beach_topless" in emile.list:
        pcm "This would be a lot less awkward if I didn't have my tits out..."
    else:
        pcm "Sitting here all normal while wearing such tiny clothes..."
    pcm "Pretend I don't care. I am not the only one near nude on the beach. It's normal. It's normal!"
    if player.has_perk([perk_exhibitionist, perk_slut]):
        pcm "I do care though... This is kinda hot..."
        pcm "Fuck, don't betray me new body. What the hell are you doing?"
    else:
        pcm "Hope he can't see much..."
    hide activity_beach_lay
    show sb_onbelly worried
    with dissolve
    if player.has_perk([perk_exhibitionist, perk_slut]):
        pcm "Yup, all on display..."
    else:
        pcm "Ah who am I kidding. He can see everything..."
    kaan.name "...on the way there."
    show sb_onbelly back slant
    pc "Err, what?"
    kaan.name "The girl."
    pc "Huh?"
    kaan.name "Haha, too busy eyeing the goods and not listening?"
    pc "Yeah, sorry. I was thinking about something. What girl?"
    kaan.name "The one you were with."
    pc "Ah. [emile.name]. My sister."
    kaan.name "Ah sisters? That will be fun."
    pc "It will?"
    kaan.name "Yeah, maybe can swap afterwards and mess about."
    show sb_onbelly worried
    pc "Err, sure?"
    show sb_onbelly up
    pcm "Share what?"
    pc "Err..."
    $ npc_race_picker(kaan)
    show sb_onbelly back kaan oh with dissolve
    pcm "What's going on?"
    show sb_onbelly rub with dissolve
    kaan.name "...you relaxed a bit."
    pc "Ah?"
    if not c.bottom:
        pcm "Fuck, from back there with no bikini he can see everything."
    else:
        pcm "Shit, wearing this doesn't hide anything and he can probably see."
    pcm "Wait..."
    pcm "He's coming onto me?!?!"
    pcm "Of fucking course he is. Sitting here with my tits out while chatting away. He thinks I am some beach slut."
    pcm "The hell am I supposed to do?"
    pc "Err, there are people around..."
    kaan.name "Not something they haven't seen or done before. Don't worry."
    pc "[emile.name] will be back soon."
    kaan.name "Doubt it. She probably has my friends shorts off by now and having her own fun."
    pc "Don't be silly, she won't get up to that sort of thing."
    if "prologue_beach_nude" in emile.list:
        kaan.name "Running off naked with him. What else is she going to be doing?"
    elif "prologue_beach_topless" in emile.list:
        kaan.name "Running off alone with him while flashing her tits. What else is she going to be doing?"
    else:
        kaan.name "Running off alone with him shaking her ass. What else is she going to be doing?"
    if "prologue_beach_topless" in emile.list:
        pc "She took her bikini with her."
        kaan.name "Wasn't wearing it though."
    pcm "Fuck, would she do that?"
    if emile.showing:
        pcm "Well, she is pregnant with no boyfriend. Did she get it from messing about?"
    pcm "I know I am new to this body, but is this normal for girls?"
    show sb_onbelly grope with dissolve
    pcm "Never really spoke about sex with her. I think... Did I? Don't think it's something a sister would tell her brother."
    pcm "But she has teased me more than once about trying to get me with a man or about a cock between my legs."
    show sb_onbelly noman with dissolve
    $ temp_var_1 = False
    if c.bottom:
        $ temp_var_1 = True
        $ c.bottom = 0
        pause 0.3
    show sb_onbelly assjob grope with dissolve
    pc "Ah hey. What you doing there?"
    kaan.name "Just getting more comfortable."
    if temp_var_1:
        pc "And what part of that means taking my bikini off?"
        kaan.name "Hard to do anything with it on."
    show sb_onbelly down neutral straight
    pcm "Is this why [emile.name] ran off? Trying to leave me alone with him?"
    pcm "I swear she better not have planned this."
    show sb_onbelly up worried with dissolve
    pcm "Wait. If she did plan this then she isn't coming back..."
    pcm "Then what the hell is she doing. Is this guy right?"
    show sb_onbelly rub with dissolve
    show sb_onbelly back straight with dissolve
    pc "Err, what are you up to back there?"
    pcm "Wait! Why am I even letting him touch me back there?"
    kaan.name "Want me to go further?"
    pc "Further?"
    pcm "Wait. He wants to... Err, shit..."
    if player.check_sex_agree(4, notif=True):
        pcm "He wants to have sex..."
        pcm "Definitely starting to look like [emile.name] has set me up here."
        pcm "Is it a problem though? I mean men and women have sex all the time. Pretty sure I would want to have sex with me when I was in my old body."
        pcm "Err... Would I though? Maybe I was gay..."
        pcm "Either way. Not like doing this is some horrible act. Less so if he is right and [emile.name] is off having her own fun."
        if player.has_perk(perk_virgin):
            pcm "Would be my first time doing this though. Do I really want it on a beach in public?"
        elif player.has_perk(perk_tech_virgin):
            pcm "I already had someone in my arse. That would be much \"worse\" than what he wants to do."
            pcm "Unless he wants to assfuck me as well..."
        else:
            pcm "Don't suppose any of that matters. Not like this would be my first time anyway so who cares really? Maybe I am just hung up on [emile.name] seeing and making fun of me."
        menu:
            "Let him carry on":
                jump emile_prologue_event_2_male_beach_men_sex_start
            "Put a stop to it":

                $ NullAction()
    jump emile_prologue_event_2_male_beach_men_sex_reject

label emile_prologue_event_2_male_beach_men_sex_reject:
    show sb_onbelly worried
    pc "Err, I think I had better see where [emile.name] went."
    kaan.name "Don't worry, my friend will be keeping her company."
    pc "Can you get off me please?"
    kaan.name "Err, ok..."
    show sb_onbelly noman with dissolve
    hide sb_onbelly
    show kaan at right1
    with dissolve
    pc "I want to make sure my crazy sister is ok."
    kaan.name "No problem. I'll be here."
    pc "Err, yeah. Ok."
    hide kaan with dissolve
    $ walk(loc_beach_hangout, outfit_block=True)
    pcm "I saw her walk this way. Where did she go though. Drinks stand?"
    $ walk(loc_beach_fire, outfit_block=True)
    pcm "Hmm, drinks stand thingy is here. But no sign of [emile.name]..."
    pcm "The pier is over there but can't see anyone there..."
    $ walk(loc_beach_hangout, outfit_block=True)
    pcm "Ah fuck. Where the hell are you?"
    $ walk(loc_beach_gym, outfit_block=True)
    pcm "..."
    show kaan at right1 with dissolve
    kaan.name "Wrong way. Saw her go off that way after coming back from the stand."
    pc "That way? Why did she go over there?"
    kaan.name "More secluded."
    pc "No... She isn't is she?"
    kaan.name "Of course she is."
    pc "She isn't like that..."
    pc "I think..."
    hide kaan
    $ walk(loc_beach_rocks, outfit_block=True)
    pcm "Hmmm. Where are..."
    pcm "Fuck!"
    show emile_sex_beach with dissolve
    $ add_to_list(emile.list, "prologue_beach_sex_seen")
    pcm "She is..."
    pcm "Damn [emile.name] set me up to get fucked by some guy while she hides to chomp on her knickers..."
    $ player.add_desire_random(100)
    pcm "Bitch!"
    hide emile_sex_beach
    show kaan at right1
    $ walk(loc_beach_gym)
    kaan.name "Find her?"
    $ player.face_annoyed()
    pc "Yeah..."
    kaan.name "And?"
    pc "And nothing. Shush!"
    kaan.name "That bad? Or good I suppose."
    pc "Don't want to hear it."
    hide kaan
    show activity_beach_lay
    with dissolve
    pc "Hrmf! That bitch."
    show activity_beach_lay kaan with dissolve
    kaan.name "Nothing wrong with having a bit of fun."
    pc "That's not what I am mad at."
    kaan.name "Then what?"
    pc "She set me up with you to get stuck like a pig while she is off having her own fun."
    kaan.name "Err... Nothing wrong with that?"
    $ player.face_neutral()
    pc "Why not?"
    kaan.name "Not like you can't make your own choices. Squeal like a piggy or sit here chatting. What difference does it make?"
    pc "She's supposed to look out for me."
    kaan.name "Can't look out for yourself?"
    pc "I am new to this stuff. I don't know... Things... It's all new to me."
    kaan.name "Ah, new to [town]? Right. Now I get it."
    pc "Err... Yeah... Sure..."
    kaan.name "Hmmm, well whatever. I'd fuck ya or just happy to sit here and wait while looking at your tits."
    hide activity_beach_lay
    show sb_onbelly back
    with dissolve
    pc "Ha, thanks!"
    kaan.name "How about we pick up where we left off?"
    pc "What? With your cock between my ass cheeks?"
    kaan.name "Sure. Sisters having fun together."
    show sb_onbelly down
    pc "*Sigh*"
    if player.check_sex_agree(4):
        menu:
            "Come on then":
                jump emile_prologue_event_2_male_beach_men_sex_start
            "No thanks":
                $ NullAction()
    show sb_onbelly back
    pc "Think I'll just sit here and think of ways to murder my sister."
    kaan.name "Don't do that. Then she can't come visit again."
    show sb_onbelly happy
    pc "Bah, choking on your dick might be a good way. You get your fun and she dies. Win win."
    kaan.name "Haha. No, I am gentle."
    pc "Yeah yeah."
    show sb_onbelly neutral
    pc "What goes on around here anyway? It common to get someone coming here looking to be dragged off and her swimwear shoved in her mouth?"
    kaan.name "Oh, they were in her mouth? Ha!"
    pc "Yeah, on her back, legs spread and moaning into her bikini."
    kaan.name "Damn. Lucky [mateo.name]!"
    kaan.name "But common enough. Play some volleyball, drink by the fire, fuck in the bushes and go home. Not much else better to do round this shithole."
    show sb_onbelly down
    pcm "Actually sounds like it would be fun if it wasn't me the one being fucked."
    pcm "Well, kinda sounds fun anyway..."
    pcm "Err... No. I used to have a cock. Don't need a new one from someone else."
    pcm "..."
    pcm "No, I... Shit..."
    kaan.name "...poke her head round."
    show sb_onbelly back
    pc "Huh?"
    kaan.name "I said it's too late to be staring at my cock now. I just saw your sister making sure the coast is clear."
    pc "Staring at your... Err..."
    show sb_onbelly up
    pcm "Shit. I get lost in thought and was staring at his cock..."
    jump emile_prologue_event_2_male_beach_men_sex_emile_return

label emile_prologue_event_2_male_beach_men_sex_start:
    $ npc_race_picker(kaan)
    pc "We are in public here. Someone might see us."
    kaan.name "Not if I hide it."
    pc "Hide it?"
    show sb_onbelly happy pokemast grope with dissolve
    show sb_onbelly poke with dissolve
    pc "Ah?"
    pc "Think that is going to stop anyone from noticing?"
    kaan.name "Dunno. But will make both of us feel good anyway."
    pc "Yeah, that is the worst excuse I have ever heard."
    kaan.name "You're supposed to pretend to believe it."
    pc "Ah, right. It's like that?"
    kaan.name "Yup, you girls like to pretend it's not what you wanted from the start."
    "Before I can respond, I feel him using his hands to spread me open and press deeper into me. He doesn't find much resistance and slowly I feel myself getting fuller."
    $ player.sex_vag(kaan)
    show sb_onbelly sex up ag worried with dissolve
    pcm "Mmmmmmmmm..."
    "He manages to \"hide\" his thing all the way inside me. Still pretending to be discreet he gently humps while groping my ass."
    show sb_onbelly happy back with dissolve
    pc "*Huff* Good job, no one will see what's going on now."
    kaan.name "Right!"
    show sb_onbelly happy down with dissolve
    "I lay on my stomach and rock back and fourth to his gentle rhythm. He doesn't get much thrusting in but the fullness and gentle rocking has me feeling good regardless."
    "I think I can hear him saying something, but don't really pay attention. I am enjoying myself and just forget my surroundings and focus on the pleasure."
    pc "Mmmm, keep going..."
    "I continue to enjoy the rocking while being full up. While he is not able to trust much, he is deep inside me and the motions alone are enough to bring me close to the edge."
    pc "Ooohh..."
    kaan.name "I am close."
    show sb_onbelly back
    pc "Huuu so am I."
    pc "Mmmmmm..."
    kaan.name "Unnng!"
    show sb_onbelly down ag
    if emile.showing:
        $ player.sex_cum(kaan, "inside")
    else:
        show sb_onbelly happy pokemast with dissolve
        $ player.sex_cum(kaan, "pullout")
    pc "Ha fuck yes."
    kaan.name "Nnnng."
    show sb_onbelly neutral
    kaan.name "That was nice..."
    pc "Mmmm."
    show sb_onbelly back
    if emile.showing:
        pc "Hold on, you are still inside me."
        kaan.name "Mmm?"
        pc "Ugh. Hope nothing bad comes of it."
        kaan.name "Not want to join your sister?"
        pc "Knocked up on a beach. No thanks."
        kaan.name "She got knocked up here?"
        pc "Ah, not sure how she got it. Won't tell me so maybe."
    else:
        pc "Ohh. It's warm."
        show sb_onbelly poke with dissolve
        kaan.name "What? Thought it would come out refrigerated?"
        pc "Of course not. Just never... No matter."
    pc "Anyway, get off in case [emile.name] comes back and sees us."
    if emile.showing:
        pc "Don't want her showing up and you having to take your thing out while she is here."
        show sb_onbelly poke with dissolve
        "I feel him slide out of me and a trickle of something warm following him."
    show sb_onbelly noman up with dissolve
    pc "Think I need to jump in the water and wash away your mess. Keep an eye on our stuff?"
    kaan.name "Sure. I'll be here."
    hide sb_onbelly with dissolve
    $ walk(loc_beach_water)
    pc "..."
    pcm "I really did that. Out in the open on the beach..."
    if kaan.vvirgin:
        pcm "Not even a week in this body and lost my virginity on the beach to some random guy..."
    pcm "Ugh... Whatever. Was fun anyway."
    $ walk(loc_beach_gym)
    show activity_beach_lay kaan with dissolve
    kaan.name "All good?"
    pc "Yeah..."
    kaan.name "Good, because I think I see your sister coming."
    jump emile_prologue_event_2_male_beach_men_sex_emile_return

label emile_prologue_event_2_male_beach_men_sex_emile_return:
    $ renpy.scene()
    if "prologue_beach_nude" in emile.list:
        show emile nude at left1
    elif "prologue_beach_topless" in emile.list:
        show emile swim_topless at left1
    else:
        show emile at left1
    show kaan at right1
    show mateo at right2
    with dissolve
    pc "Took your time."
    emile.name "Sorry. Got caught up with something."
    if "prologue_beach_sex_seen" in emile.list:
        pcm "Yeah. Caught alright."
    mateo.name "The girls are still short a player. Think I will jump in. Nice meeting you both."
    emile.name "See you."
    pc "Bye."
    hide kaan
    hide mateo
    with dissolve
    show emile at right6 with dissolve
    if not "prologue_beach_nude" in emile.list and c.nude:
        emile.name "Lose your bikini?"
        $ player.face_worried()
        pcm "Fuck! Forgot to dress back up."
        pc "Ah, I jumped in the water and let it dry off."
        emile.name "Right... Like showing off your body to hunky men?"
        $ player.face_annoyed()
        pc "Shush!"
    $ player.face_neutral()
    emile.name "Anyway, been here a while as well. Probably time for us to head off."
    pc "Yeah alright. Had enough of showing my arse off to horny men for one day."
    emile.name "How was that guy you were with?"
    pcm "She asking if he fucked me?"
    pc "Fine, decent enough guy."
    if not "prologue_beach_nude" in emile.list and c.nude:
        emile.name "Let's hope so. Don't need you having something growing inside you a couple of days after getting out the hospital."
        $ player.face_shock()
        pc "What?"
        $ player.face_worried()
    else:
        emile.name "Right..."
    if "prologue_beach_nude" in emile.list:
        show emile swim_topless
        pause 0.2
    $ pc_dress_slow()
    show emile swim
    emile.name "Ready?"
    pc "Yeah."
    show emile at left1
    $ walk(loc_beach_hangout)
    jump emile_prologue_event_2_male_beach_redress

label emile_prologue_event_2_male_beach_redress:
    emile.name "Meet you on the boardwalk?"
    pc "Sure."
    hide emile with dissolve
    $ walk(loc_beach_locker_girls)
    $ walk(loc_beach_locker_girls_stall)
    pcm "Right then..."
    $ pc_striptease()
    $ tab_top = "daily"
    $ pc_dress_slow()
    $ walk(loc_beach_locker_girls)
    $ walk(loc_lake)
    pc "Hmmm..."
    show emile at left4
    show sandy at right1
    $ walk(loc_boardwalk)
    if sandy.has_met:
        pcm "Ah, [emile.name] knows [sandy.name]?"
        pc "Hey."
        sandy.name "Ah, [name] is your sister?"
        show emile at right3 with dissolve
        emile.name "Oh? You know each other."
        sandy.name "Yeah, she came by and we chatted."
        emile.name "She try to get you to sell her shells?"
        pc "Yeah."
    else:
        pcm "Who is that she is speaking to?"
        pc "Hey."
        sandy.name "Ah, your sister?"
        pc "Yeah."
        show emile at right3 with dissolve
        sandy.name "Nice to meet you. [sandy.name]. I run this shack. Sell beach stuff and buy seashells and other trinkets you can scavenge up."
        emile.name "Always with the sales pitch."
        sandy.name "Of course. I gotta earn."
        emile.name "Ready to head off?"
        pc "Yeah."
    sandy.name "Speak to you later [emile.name]. Come by one night."
    emile.name "Sure."
    hide sandy
    show emile at left1
    with dissolve
    $ walk(loc_lake)
    pc "She a friend of yours?"
    emile.name "Not really. She's always at the beach and is nice. So we chat a bit when I come by."
    pc "Ah."
    emile.name "She's not into girls in case you were wondering."
    pc "Actually I wasn't."
    emile.name "No? Pretty girl like her? Maybe you are into guys instead."
    pc "Shush!"
    $ walk(loc_busstop_lake)
    pc "What's with you trying to push guys onto me anyway?"
    emile.name "Just having some fun."
    hide emile with dissolve
    $ walk(loc_bus_interior)
    show emile at right6 with dissolve
    if emile.showing:
        pc "Yeah, I think I would prefer not to have a belly like yours."
    else:
        pc "Not sure we have the same idea of fun."
        if kaan.sex:
            pcm "Hmm, though I did just have some of [emile.name]'s idea of fun on the beach..."
    emile.name "Just trying to get you to relax. Hard enough to adjust to this new life without having your bits chopped off."
    pc "They weren't chopped off."
    show emile happy
    emile.name "Haha. Where are they then?"
    pc "Dunno. Fed to the dogs maybe."
    emile.name "Ha!"
    emile.name "But I am serious. Just trying to make things a bit easier on you. Friends, booze, sex. Whatever stops you from walking into the lake and not coming back."
    pc "Err, yeah. Can't see that happening. Might not have chose this but it's not entirely a bad deal."
    emile.name "You think?"
    pc "Dead or a brand new younger body? Easy choice to make. Might have even agreed without the death alternative."
    emile.name "Even without your bits?"
    pc "Half the world has no bits. You have no bits. Not what I was used to but not like it's some horrific affliction either."
    pc "Already lived most of a life with bits. Now I get a reset without them. Why jump in the lake?"
    emile.name "You remember more about life previously?"
    pc "Not really. Some parts. It's like most of it is washed away and too faded to see."
    emile.name "You haven't asked me anything about it."
    pc "Not sure I want to know. Better to look forward than backwards."
    emile.name "Maybe for the best."
    hide emile with dissolve
    show emile at right1
    $ walk(loc_busstop_residential)
    emile.name "Maybe something again tomorrow?"
    pc "Sounds good."
    emile.name "Ok."
    hide emile with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
