label school_dance_show_3:
    $ school_dance_quest_show_count += 1
    $ walk(loc_school_gym, trans=False)
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    show svet dance happy at right1
    with dissolve
    svet.name "Great, all here. So finally girls. We have a show!"
    dani.name "Ah and doe..."
    svet.name "Yes it pays [dani.name]. It's a proper show where we need to dance to attract people towards a shop."
    show dani happy
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(anabel.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ add_to_list(rachel.list, "no_location")
    svet.name "It's a little less formal than in our practice sessions. Get out there, dance and smile at the people and if they ask what we are doing, we guide them to our client's place."
    anabel.name "Where is it?"
    svet.name "It's up by the market. We can jump on the bus to get there and our client will be waiting for us."
    svet.name "So come on, we need to head off if we want to arrive with some time to spare."
    anabel.name "The bus? Like this?"
    svet.name "Unless you wanna be changing in the bushes, yes. Come on."
    hide svet
    hide rachel
    with dissolve
    anabel.name "People will see us..."
    dani.name "Come on, this one is paid. Finally we get some actual work out of this."
    hide dani with dissolve
    anabel.name "But..."
    anabel.name "*Sigh*"
    hide anabel with dissolve
    pause 0.5
    pcm "Ok... Just leave me behind..."
    $ walk(loc_school, trans=False)
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(anabel.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    $ remove_from_list(rachel.list, "no_location")
    show dani dance at right6 with dissolve
    dani.name "You live in [oskar.name]'s block as well don't you?"
    pc "Yeah."
    dani.name "How are you making rent?"
    if pub_waitress.timesworked >= 5:
        if "pub_started_working" in dani.dict and dani.dict["pub_started_working"] <= t.day and "pub_first_talk" in dani.list:
            pc "Same as you, working the pub at night. Why?"
            dani.name "Need more money..."
            pc "Hmmm..."
            if quest_whore.sex >= 10 and dani.love >= 60:
                pc "Doubt you will be interested in some of the other ways I make some money."
                dani.name "No? What do you do?"
                pc "Go to the highway and bend over for some punter in a smelly alleyway."
                dani.name "Ah... Yeah I don't think so..."
                dani.name "It pay well at least?"
                pc "Better than starving."
            else:

                if pubpatron.name in dani.sex_who:
                    pc "Bend over for the drunks some more?"
                    dani.name "Ugh..."
                else:
                    pc "Might need to start bending over for the drunks if you are that desperate."
                    dani.name "Probably..."

        elif "asked_pub_work" in dani.list:
            pc "Been working at the pub on Revel in the evenings. You spoke to [trixie.name] about working there yet?"
            dani.name "Yeah, but tips only makes it sound like I wont be earning much."
            pc "Well, depends on how you play the drunks."
            dani.name "Huh?"
            if player.has_perk([perk_slut, perk_whore, perk_sucu, perk_bimbo], notif=True):
                pc "Let their hands go where they want and they will tip more."
            elif player.has_perk([perk_meek, perk_broken], notif=True):
                pc "Make them happy and they will tip a lot more."
            else:
                pc "It... Depends on what work you do there."
            dani.name "Ah, right."
        else:

            $ add_to_list(dani.list, "asked_pub_work")
            pc "Been working at the pub on Revel in the evenings."
            dani.name "Ah really? Think I could get a job there?"
            pc "Probably. If you are fine with wearing a short dress and drunks trying to put their hand up it."
            dani.name "Oh..."
            dani.name "Ermm."
            dani.name "Does it pay well?"
            if player.has_perk([perk_slut, perk_whore, perk_sucu, perk_bimbo], notif=True):
                pc "If you don't make them remove their hand, yes."
            elif player.has_perk([perk_meek, perk_broken], notif=True):
                pc "Depends how much you charge the guys to go to the bathroom with them."
            else:
                pc "It... Depends on what work you do there."
            dani.name "Err, I don't understand."
            pc "Go and give it a go, they are always looking for staff so their will take you on the same day probably."
            dani.name "Ok, I'll give it a think."

    elif quest_flyers.timesworked >= 5:
        pc "Been handing out flyers. Pay is terrible but it still pays."
        dani.name "I gave that a try. Pay is pretty bad."
    elif quest_cleaner.timesworked >= 5:
        pc "Ugh, been cleaning other peoples mess."
        dani.name "Ah, yeah I do that sometimes."
    else:
        pc "Whatever work I can find. Not a lot to do out there that... Hmmm..."
        dani.name "Yeah I know..."
    $ walk(loc_busstop_school)
    dani.name "I've been having to try to find work around the market and the station. But... People expect too much."
    pc "Mmmm."
    show anabel dance at right5 with dissolve
    anabel.name "Bus is coming. Let's go."
    hide anabel
    hide dani
    with dissolve
    $ walk(loc_bus_interior)
    pcm "Ugh, pretty busy here. Should have expected that considering the time."
    show rachel dance happy at right6 with dissolve
    rachel.name "Bit tight in here."
    pc "Yeah."
    rachel.name "Excited?"
    pc "Nervous."
    rachel.name "It'll be fine. Just smile like [svet.name] says. Smile and attract people."
    pc "Mmmm."
    rachel.name "Here we go. Come on."
    hide rachel with dissolve
    $ walk(loc_revel)
    pause 0.5
    $ walk(loc_market, trans=False)
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    show svet dance happy at right1
    with dissolve
    svet.name "I'll go speak to the boss and make sure everything is ok. You guys set up here and I'll be back in a bit."
    hide svet with dissolve
    show rachel at right2
    show dani at right1
    with dissolve
    rachel.name "Ok, I'll set up the tapes on the player, you guys clear a space."
    rachel.name "Let's make this awesome so we have the boss wanting us back all the time."
    hide rachel with dissolve
    dani.name "Ok. I guess we should get to it."
    anabel.name "Mmm."
    hide dani
    hide anabel
    with dissolve
    "I spend a few minutes with the girls cleaning up the dance area so we don't kick some random junk in someone's face while dancing."
    show dani dance at right1 with dissolve
    dani.name "Not exactly a proper show here. Just dancing on the street for this shop guy."
    pc "What else can you expect? We aren't exactly top talent who everyone wants to book."
    pc "The fact we are being paid actual money instead of some tins of expired beans is probably more than we can expect."
    dani.name "Wouldn't say no to the beans either."
    $ player.face_happy()
    pc "Nor would I!"
    $ player.face_neutral()
    show dani at left1
    show svet dance at right1
    with dissolve
    if weather_var >= 3:
        svet.name "Okay girls. We are good to go. Weather is a bit shit but we will have to do this without our brollies, so let's get ready and give them a show!"
        $ player.prop = ""
    else:
        svet.name "Okay girls. We are good to go. Let's give them a show!"
    hide svet
    hide dani
    with dissolve
    $ show_dance_image()

    "Me and the girls put on a bit of a show. It is less a structured routine and more of a sirens call to tempt people over to us so we can direct people to the client."
    "There is a fair amount of hollering and whistling as we dance. And quite a few people come up to me asking what we are doing."
    $ show_dance_image()
    "It's clear most of the people approaching us have no interest in the shop, or even what we say to them, and are just looking for an excuse to get close to us."
    "While some of the guys that approach me or the girls far outstay their welcome, [svet.name] does a good job of corralling and ushering them off towards the client's shop."
    $ show_dance_image()
    "Some guys just quietly watch us for some time, neither approaching nor making any attempt to go towards the shop we are promoting."
    $ exercise(180)
    $ player.add_mood(20)
    if player.tired <= 21:
        $ player.add_tired(21 - player.tired)
    $ player.face_neutral()
    "Time passes and we are all quite exhausted. But it looks like the later in the evening it got, the more attention we attracted. Eventually we all smile and wave goodbye to the crowd that gathered."
    $ renpy.scene()
    with dissolve
    pc "Phew..."

    show svet dance happy at right1
    with dissolve
    svet.name "Okay girls, gather round."
    show anabel dance at left1
    show dani dance at left2
    show rachel dance at left3
    with dissolve
    svet.name "Good job, good job! We kept them all entertained and drew in quite a crowd."
    anabel.name "Not sure many of them made their way over to the shop though."
    svet.name "Doesn't matter. We did what we were paid to do, the rest was up to the client to deal with. We got the crowd and it's his job to sell."
    dani.name "So when do we get paid?"
    svet.name "Now. Here is your share of the money. Split evenly 5 ways."
    $ player.add_money(100)
    show dani happy
    $ player.face_happy()
    dani.name "YES!!!"
    dani.name "Finally!"
    svet.name "I'll go finish up with the client, you guys can just head off home now I guess."
    $ player.face_neutral()
    rachel.name "I'll join you. I want to see how you speak to him."
    hide rachel
    hide svet
    with dissolve
    show anabel at right1
    show dani at right2
    with dissolve
    dani.name "Finally some proper pay! Hope this keeps up."
    anabel.name "Yeah.."
    dani.name "You wanted more? What they gave us is quite good already."
    anabel.name "No the pay is fine. I just don't feel so comfortable dancing for these perverts."
    show dani worried
    dani.name "Ah..."
    dani.name "Yeah. They were a bit... Vocal..."
    anabel.name "That's putting it politely."
    show dani happy
    dani.name "Well, you do have a big arse."
    show anabel angry
    dani.name "And big..."
    anabel.name "Yeah yeah, that's enough."
    show anabel neutral
    anabel.name "Wearing this skirt doesn't feel much different to being naked. Especially when dancing and it rises up."
    dani.name "Yeah..."
    dani.name "Does feel a bit much."
    dani.name "But whatever, we got paid. Now I might actually be able to pay my rent on time and not have to deal with [oskar.name]."
    dani.name "But I'm gonna go home. You coming [anabel.name]?"
    anabel.name "Yeah, see you [name]."
    pc "See you."
    hide dani
    hide anabel
    with dissolve
    $ player.face_worried()
    pcm "..."
    show sb_pose_upskirt with dissolve
    pcm "Gotta walk home alone stinking and flashing my arse?"
    pcm "Should have probably went with them..."
    hide sb_pose_upskirt with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
