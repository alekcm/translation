init python:
    def robin_sexobject_dress_bimbo():
        work.pants = 7
        work.outfit = 11
        work.outfit_primary_colour = "black"
        work.pants_primary_colour = "pink"
        work.pants_secondary_colour = "black"

    def robin_sexobject_dress_slut():
        work.pants = 7
        work.top = 22
        work.bottom = 15
        work.top_primary_colour = "blue"
        work.bottom_primary_colour = "black"
        work.bottom_secondary_colour = "white"
        work.pants_primary_colour = "pink"
        work.pants_secondary_colour = "black"

label robin_talk_sexobject_offer_outing_start:
    if not "robin_talk_sexobject_outing_times" in robin.dict:
        $ robin.dict["robin_talk_sexobject_outing_times"] = 0
    $ robin.dict["robin_talk_sexobject_outing_times"] += 1













    show robin at right1 with dissolve
    $ add_to_list(robin.list, "slut_outing")
    if robin.dict["robin_talk_sexobject_outing_times"] == 1:
        pc "Hey, I was thinking of heading out for some fun, you interested?"
        robin.name "Err, the kind of fun like last time?"
        pc "Yeah, but let's go to the pub or something."
        robin.name "Could hang out in the park couldn't we?"
        pc "I guess, if the weather is okay."
        robin.name "Well, just wondering if it's some drinking and party you are after, or like..."
        pc "Wouldn't need to invite you if that was the plan."
        robin.name "Ah, good. So you want to meet a guy?"
        pc "Guy?"
        robin.name "Guys?"
        pc "That's better."
        robin.name "Ha, you slut!"
        pc "Yup, and you too. Go and put some slutwear on then and we can go out."
        robin.name "Okay."
    else:
        pc "So, want to go out somewhere and have some fun?"
        robin.name "Oooh? Yeah would love to."
        robin.name "I'll go get changed. Meet you outside?"
    hide robin with dissolve
    if numgen():
        $ robin.dict["robin_talk_sexobject_outing_clothes"] = "slut"
    else:
        $ robin.dict["robin_talk_sexobject_outing_clothes"] = "bimbo"
    if not "party" in tab_top:
        $ pc_dress_event("party", loc_bedroom, loc_stairwell)
    else:
        $ walk(loc_stairwell)
        pcm "Should be fun."
    show robin outing happy at right6 with dissolve
    if robin.dict["robin_talk_sexobject_outing_times"] == 1:
        pc "No pink hair this time?"
        robin.name "Na, I don't think it matters much."
        pc "Not really, not when your tit's and arse are hanging out of your clothes."
    robin.name "Ready?"
    pc "Yup!"
    show robin outing at left1 with dissolve

    jump expression WeightedChoice([
    ("robin_talk_sexobject_offer_outing_pub", 100),
    ])

label robin_talk_sexobject_offer_outing_pub:
    $ walk(loc_busstop_residential)
    robin.name "The pub yeah?"
    pc "Yeah, nice and safe there."
    $ walk(loc_bus_interior)
    pc "Don't be fucking someone on the bus and wearing yourself out now."
    robin.name "Haha. No promises."
    pc "It's not far anyway."
    robin.name "Mmm..."
    "We hang around for our stop chatting away."
    robin.name "Come on."
    $ walk(loc_revel)
    $ walk(loc_pub)
    robin.name "You get us some drinks and I'll find somewhere to sit."
    pc "Okay."
    hide robin with dissolve
    pause 0.3
    show trixie at right1 with dissolve
    pc "Hey [trixie.name]. Couple of beers please."
    trixie.name "Sure hon. You and your friend looking for some fun tonight?"
    pc "Yeah, just letting our hair down a bit."
    trixie.name "Have fun. Here you go."
    $ player.add_perk(perk_drinking_beer_2, mins=10)
    $ player.right_hand = "beer"
    pc "Thanks."
    hide trixie with dissolve
    pcm "Where did [robin.name] go?"
    pcm "Ah, there you are."
    show robin outing happy at right6 with dissolve
    "I have a seat with [robin.name] and hand her a beer."
    pc "Here you go."
    $ player.right_hand = ""
    robin.name "Thanks."
    jump robin_talk_sexobject_offer_outing_pub_talk_picker

label robin_talk_sexobject_offer_outing_pub_talk_picker:
    jump expression WeightedChoice([
    ("robin_talk_sexobject_offer_outing_pub_talk_1", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_2", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_3", If(player.slutty, 100, 0)),
    ("robin_talk_sexobject_offer_outing_pub_talk_4", If(pub_waitress.timesworked > 5, 100, 0)),
    ("robin_talk_sexobject_offer_outing_pub_talk_5", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_6", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_7", If(player.iswhore, 100, 0)),
    ])

label robin_talk_sexobject_offer_outing_pub_talk_morebeer:
    $ player.drink_finish()
    pc "Time for more beer."
    "I grab a couple of beers from [trixie.name] as she is passing."
    $ player.add_perk(perk_drinking_beer_2, mins=10)
    pc "Here we go."
    jump robin_talk_sexobject_offer_outing_pub_talk_picker


label robin_talk_sexobject_offer_outing_pub_talk_1:
    pc "Barely in here and I can already see the guys drooling over you."
    robin.name "Or you."
    if not player.slutty:
        pc "Doubt it, I don't looks like a slut in this."
        robin.name "Yeah, why don't you?"
        pc "I just put on what I had ready."
        robin.name "Next time we go out, you should also have your arse hanging out."
    else:
        pc "Two sluts in the pub isn't that unusual."
        robin.name "Maybe not. But the perverts here probably want to fuck everyone."
        pc "Yeah, wouldn't even matter how we are dressed."
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_2:
    pc "How yu feeling hanging out here with all your bits out?"
    robin.name "It's kinda fun. I know everyone is trying to get a look."
    pc "Not just a look, I can see people outright staring at your arse."
    pc "They don't even notice I am looking at them because of where their eyes are glued."
    robin.name "Maybe I should bend over a bit then."
    pc "You should. Probably give a heart attack to half the men in here."
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_3:
    robin.name "Good to see you slutting it up as well."
    pc "Isn't that the point of coming here?"
    robin.name "Well yeah, but it's still nice to have someone on the same level."
    pc "I guess. Can't say there is anyone else I go out with like this."
    robin.name "You mean your other friends don't want to go out, get piss drunk and have a bunch of guys use them like a sex doll?"
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_4:
    robin.name "You not worried that since you work here, people might recognise you?"
    pc "Not really. I doubt half the men here even know what my face looks like."
    if player.breasts >= 3:
        robin.name "They might recognise those giant tits though. Not many people around with ones that big."
        pc "[trixie.name] isn't exactly small. She spills out of her dress just like I do."
        robin.name "Yeah, but yours are kind of extra."
        pc "Well, whatever, then they might get to suck on them for free instead of offering to pay."
    elif player.slutty and c.skirt:
        robin.name "Not really hiding your ass in those clothes either though."
        pc "What has my arse got to do with it?"
        robin.name "Well, they might not know what your face looks like since they spend all their time look up your skirt."
        robin.name "Now you come here flashing your arse again."
        pc "Ah, well let them look. If they are bold enough they might get some alone time with it."
    else:
        robin.name "Hmm yeah. The dress you work in doesn't give much reason to look you in the eye."
        robin.name "Especially if you don't wear your knickers."
        pc "Didn't think I would have you perving on me as well."
        robin.name "Nothing else worth looking at in thi dreary place."
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_5:
    robin.name "Kinda surprised you agree to come here with me."
    pc "Why?"
    robin.name "\"Hey, let's go out, get piss drunk and fuck a bunch of guys\" isn't something most agree to."
    pc "Because you don't sell it well enough."
    robin.name "That sounds like a perfect sales pitch to me."
    pc "Hmm, well you are a bus pervert so I guess so."
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_6:
    pc "I wonder what it is about getting to fuck a tomboy?"
    robin.name "No idea, guys seem to go kinda wild about it. I think they would prefer me in my hoodie than with my arse out like this."
    pc "Many would, yeah."
    robin.name "I think it might be a lesbian thing."
    pc "Huh?"
    robin.name "Well, normal guys would call me a slut or whore, you know, normal sexy insults."
    robin.name "Guys who are into the tomboy thing end up calling me a dyke, rug muncher or other weird shit when we are messing about."
    pc "Ah, weird."
    jump robin_talk_sexobject_offer_outing_pub_talk_cont

label robin_talk_sexobject_offer_outing_pub_talk_7:
    robin.name "So, you are a whore but coming here for free sex?"
    pc "Yeah, and?"
    robin.name "Seems weird to give it away for free."
    pc "Well, I'm also here to have drinks and fun with you. And it's not like I don't enjoy sex any more."
    pc "Most of the time I whore is because it seems like it would be fun anyway. And just earn a bit of extra."
    robin.name "Ha, not sure I would want to do that."
    pc "What, never fucked a guy for cash before?"
    if robin.sold:
        robin.name "I have, but that was just for the money. Wouldn't have fucked him for free."
    else:
        robin.name "Not saying I wouldn't if the price was good, but no, I haven't."

    jump robin_talk_sexobject_offer_outing_pub_talk_cont



label robin_talk_sexobject_offer_outing_pub_talk_cont:
    $ relax(5)
    "Me and [robin.name] relax a bit and drink our beers, chatting away with each other."
    "Eyes are all on us as we drink and have fun together."
    $ relax(5)
    "And it's not long until some of the guys come to chat with us."

    $ male_npc_create_all()
    $ tempname = robinpubmotel
    $ tempname2 = robinpubmotel2
    $ tempname3 = robinpubmotel3
    $ quest_temp = None

    jump expression WeightedChoice([
    ("robin_talk_sexobject_offer_outing_pub_talk_men_1", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_men_2", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_men_3", 100),
    ("robin_talk_sexobject_offer_outing_pub_talk_men_4", 100),
    ])



label robin_talk_sexobject_offer_outing_pub_talk_men_1:
    show male_generic at right1
    show male2_generic at right2
    with dissolve
    tempname.name "You lovely ladies want some company to drink with?"
    show robin at left1 with dissolve
    robin.name "Oh? Look at this [name], a bunch of guys looking to ply us with booze?"
    pc "Looks like it."
    tempname.name "Err, you make it sound..."
    robin.name "It's fine, bring on the booze."
    tempname.name "Err, okay then."
    pc "More booze!"
    jump robin_talk_sexobject_offer_outing_pub_flirt

label robin_talk_sexobject_offer_outing_pub_talk_men_2:
    $ player.grope_ass()
    pc "Ah!"
    $ player.grope_end()
    show male_generic at right1
    show male2_generic at right2
    with dissolve
    tempname.name "Hey sexy girls, let's have a drink."
    show robin at left1 with dissolve
    robin.name "Oh? Look..."
    $ player.face_annoyed()
    pc "Go away."
    tempname.name "C'mon [rlist.name_deg], we are all here for the same thing."
    pc "Maybe so, but not with you. Piss off."
    tempname.name "Cunts!"
    hide male_generic at right1
    hide male2_generic at right2
    with dissolve
    show robin at right6 with dissolve
    robin.name "Why did you shoo them away?"
    pc "Grabbed my arse before even saying hello."
    robin.name "Ah."
    jump robin_talk_sexobject_offer_outing_pub_talk_morebeer

label robin_talk_sexobject_offer_outing_pub_talk_men_3:
    show male_generic at right1
    show male2_generic at right2
    tempname.name "Hey girls, how's you night treating you?"
    show robin at left1 with dissolve
    robin.name "Good so far, how about you boys?"
    tempname.name "Better with company like you pretty girls."
    robin.name "Oh, they are trying to flatter us?"
    pc "Sounds like they are."
    robin.name "Keep going."
    tempname.name "Haha, I knew you girls looked like fun."
    jump robin_talk_sexobject_offer_outing_pub_flirt

label robin_talk_sexobject_offer_outing_pub_talk_men_4:
    show male_generic at right1 with dissolve
    tempname.name "Looking good girls."
    show robin at left1 with dissolve
    robin.name "Thanks, you too."
    tempname.name "I'm just heading off, but you girls looked too nice to just walk past."
    pc "Ohh, guy is trying to flatter us."
    robin.name "Mmm, sounds like it. Keep it up."
    tempname.name "Haha, well I would, but I should be off."
    pc "Okay, have a good night."
    tempname.name "You too, keep safe."
    hide male_generic with dissolve
    show robin at right6 with dissolve
    jump robin_talk_sexobject_offer_outing_pub_talk_morebeer


label robin_talk_sexobject_offer_outing_pub_flirt:
    "Me and [robin.name] chat away with the guys, making the odd suggestive comment."
    "The guys jump on such comments and go with it."
    $ relax(20)
    tempname.name "More drinks please barmaid."
    $ player.add_perk(perk_drinking_beer_2, mins=10)
    "We make it fairly clear we are looking for some fun, letting the guys get close and put their hands on us."
    "[robin.name] is way more overt than me with the comments she is making."
    $ relax(20)
    tempname.name "[rlist.pub_drink_talk_man]"
    pc "[rlist.pub_drink_talk_man_reply]"
    $ player.add_perk(perk_drinking_beer_2, mins=10)
    "Beer flows and the guys get more bold, making very suggestive comments."
    robin.name "So guys, it's getting a little late. Got anywhere interesting to head off to?"
    tempname.name "Could have a little after party over the motel."
    robin.name "Oh? That sounds like fun."
    tempname.name "Yeah, well finish up your drinks and we can head off."
    show robin at right6 with dissolve
    robin.name "Finish up that beer [name]."
    pc "Right."
    $ player.drink_finish()
    pc "Ubbb."
    pc "There we go."
    show robin at left1 with dissolve
    robin.name "Lead the way guys."
    hide male2_generic with dissolve
    hide robin
    hide male_generic
    with dissolve
    $ walk(loc_revel)
    show male_generic at right5 with dissolve
    tempname.name "This way darling."
    pc "Right behind you."
    show screen blackout() with dissolve
    jump robin_talk_pub_leave_motel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
