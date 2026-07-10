

label dance_party_start_firsttime:

    pcm "Ah, the girls are waiting for me."
    rachel.name "Over here [name]!"
    show svet at right1
    show rachel at right2
    show dani at left1
    show anabel at left2
    with dissolve
    $ log.markdone("quest_dancevip_01")
    svet.name "Okay, everyone is here. Let's head up before the party starts."
    anabel.name "Is there somewhere to change? I didn't want to come here in my dance clothes."
    pc "Yeah I didn't wear anything either."
    svet.name "I'm sure there is somewhere. Let's go."
    $ hide_npc([dani, svet, anabel, rachel])
    hide svet
    hide rachel
    with dissolve
    show dani at right2
    show anabel at right1
    with dissolve
    dani.name "..."
    pc "Not heading up?"
    dani.name "Give me a minute."
    anabel.name "You scared too [name]?"
    if player.has_perk([perk_whore, perk_sucu], notif=True):
        pc "Err, what is there to be scared of? Just some party."
    elif player.has_perk([perk_party_girl, perk_slut, perk_bimbo], notif=True):
        pc "Not really, sounds like it might be fun."
    elif player.has_perk([perk_meek, perk_bambi], notif=True):
        pc "Yeah, terrified. But a lot of money and it should be fine."
        pc "I hope..."
    else:
        pc "Err, kind of. No idea what they expect in this place."
    show rachel at left3 with dissolve
    rachel.name "Come on. We are waiting!"
    hide rachel with dissolve
    pc "Oh well..."
    pc "Take your time."
    hide dani
    hide anabel
    with dissolve
    $ walk(loc_revel_backstreet_stairwell)
    $ loc_revel_backstreet_stairwell.locked = False
    $ loc_party_main.locked = False
    pcm "Well, let's see how this goes..."
    pcm "Hopefully not too bad."
    $ unhide_npc([dani, svet, anabel, rachel])
    show rachel at right1 with dissolve
    rachel.name "In here."
    hide rachel with dissolve
    $ walk(loc_party_main)

    pcm "Hmm, looks kind of barren, like no one actually lives here."
    show theo at right1 with dissolve
    if theo.has_met:
        theo.name "Nice to see you again."
        pc "Ah, hi."
        theo.name "Happy to see you decided to join us."
        if "dance_waited_interrupt_toilet" in dani.conversation_topics:
            pc "Yeah I bet. Though let's keep things out of the toilet this time."
            theo.name "For now at least."
        else:
            pc "Ah, well you are paying, why wouldn't I come."
            theo.name "Yup, I definitely like you girls."
    else:
        theo.name "I don't believe we have met."
        pc "We haven't. [name]."
        theo.name "[theo.name]. Nice to meet you."
    pc "Err, so what is it you want from us."

    if "dance_waited_interrupt_toilet" in dani.conversation_topics:
        theo.name "Considering what we did before in the toilet, I think you might know the answer to that question."
        pc "Always good to confirm."
        theo.name "Well, nothing is expected of you."
        pc "Other than show my tits off to the guys?"
        theo.name "No. Well, yes. But no."
        pc "I perfectly understand."
        theo.name "I am having a party. You girls are here to make people have more fun."
        theo.name "How best to do that, I can imagine. But I am not going to demand anything of you just yet."
        pc "Just yet? Planning more parties?"
        theo.name "Sure. Why not?"
        theo.name "You make people here happy, you get more money. If folk are happy they will want more parties."
        pc "More parties mean repeat work."
        theo.name "I have met [svet.name] and had fun with [dani.name]. And you of course. You girls seem to know how to entertain."
        theo.name "So I'll leave everything in your hands."
        pc "Sounds good."
        theo.name "Anyway, glad you are here. Here, take this."
        $ player.add_money(500)
        pc "Payment in advance?"
        theo.name "Who knows what state you girls will be in by the end."
        pc "Ah..."
        theo.name "Have fun."
        pc "Bye."
        hide theo with dissolve
        pcm "So, judging by that, he wants some whores to have fun with the guys."
    else:
        theo.name "To entertain and make people here happy."
        theo.name "Knowing [svet.name] and [dani.name], I trust you all can do that."
        pc "Err, probably."
        theo.name "And the more happy these guys are, the more they will push me to have you around in future parties."
        pc "More work?"
        theo.name "That's right."
        pc "Sounds good to me."
        theo.name "I'll leave it in you girls' capable hands. Here is your payment."
        $ player.add_money(500)
        pc "Payment in advance?"
        theo.name "All this booze flowing, I'd better get it out the way now. Have fun."
        pc "See you."
        hide theo with dissolve
        pcm "So, pretty girls entertaining the guys I guess."
    pcm "Guess I'll look around for the other girls."
    $ walk(loc_party_kitchen, trans=False)
    show svet dance at right1
    show rachel dance at left4
    with dissolve
    show rachel at right2 with dissolve
    rachel.name "Get this [name]. The booze is just here and they don't mind if we drink."
    if player.has_perk(perk_alcoholic, notif=True):
        $ player.face_happy()
        pc "Really? Free booze?"
        svet.name "Ugh. You two..."
        svet.name "You know why they want you to get drunk."
        pc "Don't care. Free booze."
        $ player.add_perk(perk_drinking_beerbottle_2, mins=10)
        $ player.drink()
        rachel.name "Haha!"
        svet.name "Christ you two. You are going to get wrecked before the night is half done."
        pc "Hope so."
        svet.name "Right. Whatever. Just remember to take this stuff out to the people at the actual party."
        hide svet with dissolve
        rachel.name "She is always nagging me."
        pc "Yeah I know."
        rachel.name "Supposed to walk around with the drinks and hand them out when we're not dancing."
    else:
        pc "Oh? I can see where this is going."
        rachel.name "Going good places."
        svet.name "So we are supposed to hand out drinks between dances. Walk around and generally entertain people."
        pc "When are the dances?"
        svet.name "I'll give you all a call when it's time."
        pc "Sounds good."
        hide svet with dissolve
        rachel.name "Free booze!"
        pc "And other stuff by the look of the table."
        rachel.name "Huh?"
    pc "Where did you change?"
    rachel.name "Ah, lemme show you."
    show rachel at left1
    $ walk(loc_party_main)
    $ walk(loc_party_bedroom1)
    rachel.name "Get dressed here."
    pc "Okay."
    hide rachel with dissolve
    $ school_dance_set_clothes()
    $ pc_dress_event("work")
    $ walk(loc_party_main)
    pcm "Seeing more wine glasses than beer. Maybe I should walk around with a wine bottle."
    if player.has_perk(perk_alcoholic):
        pcm "No one will notice if I take swigs from the bottle either."
    if player.has_perk_drinking():
        pcm "Better finish up this drink first."
        $ player.drink_finish()
        pcm "Ooooh..."
    $ walk(loc_party_kitchen)
    pcm "So, a bottle of wine it is."
    $ dance_party_get_wine()
    pcm "See if these folk want anything."

    jump random_event_picker_dance_party_tombola



label dance_party_first_event_chain_0:
    $ quest_dancevip.dict["intro_chain"] += 1
    show anabel worried at right1 with dissolve
    anabel.name "Everyone here are men."
    pc "Err, yeah. Did you expect different?"
    anabel.name "I thought it would be more normal. Don't girls normally go to parties like this?"
    pc "Not really."
    anabel.name "I have passed places and there are women in there."
    pc "Yeah, whores looking for customers. Not many women would go to a place like this."
    anabel.name "..."
    show anabel neutral
    jump random_event_picker_dance_party_talk_anabel_end

label dance_party_first_event_chain_1:
    $ quest_dancevip.dict["intro_chain"] += 1
    show dani worried at right1 with dissolve
    dani.name "You okay with this place [name]?"
    if dani.hate:
        $ player.face_annoyed()
        pc "*Tsk*"
        hide dani
        $ walk(loc_from)
        pcm "Crazy bitch."
        jump travel
    pc "Sure, seems fine. Why?"
    dani.name "It seems a bit, y'know."
    if player.has_perk([perk_whore, perk_sucu]):
        pc "Did you expect anything else? You know the guy that hired us."
        dani.name "Well, yeah..."
    elif player.has_perk(perk_alcoholic):
        pc "Free booze is good enough for me."
    elif player.has_perk([perk_slut, perk_bimbo]):
        pc "It's a party. Lot's of guys having fun. No reason we cant have fun."
        dani.name "..."
    elif player.has_perk([perk_broken, perk_meek]):
        pc "Guys pay us to do stuff, we do it."
        dani.name "..."
    else:
        pc "Everyone here needs money. Let's see how that goes."
        show dani neutral
    jump random_event_picker_dance_party_talk_dani_end

label dance_party_first_event_chain_2:
    $ quest_dancevip.dict["intro_chain"] += 1
    show rachel happy at right1 with dissolve
    rachel.name "Booze booze booze!"
    pc "Having fun?"
    rachel.name "Loads!"
    pc "Ha, good for you."
    rachel.name "You know [name]..."
    rachel.name "There are empty bedrooms here."
    rachel.name "More fun."
    pc "I suppose."
    jump random_event_picker_dance_party_talk_rachel_end

label dance_party_first_event_chain_3:
    $ quest_dancevip.dict["intro_chain"] += 1
    show svet at right1 with dissolve
    svet.name "So, looks like this place is pretty much what I expected."
    if player.has_perk([perk_whore, perk_sucu]):
        pc "Bunch of drunk guys looking to fuck easy girls?"
        svet.name "Okay, so you are aware."
        pc "Was aware before we even came here."
    elif player.has_perk(perk_alcoholic):
        pc "Giving us all free booze."
        svet.name "Yeah, but you know why?"
        if player.has_perk(perk_bimbo) or not player.check_int():
            pc "Err, dunno. Fun?"
            svet.name "Ugh, you and [rachel.name] are just the same."
        else:
            pc "Get us drunk enough to fuck us in the corner. I'm drunk, not stupid."
            svet.name "Okay, just making sure."
    elif player.has_perk([perk_slut, perk_bimbo]):
        pc "Bunch of guys inviting a bunch of girls somewhere. Is there some secret I am missing?"
        svet.name "Probably not."
    elif player.has_perk([perk_broken, perk_meek]):
        pc "Yeah..."
        svet.name "..."
    else:
        pc "The same as almost anywhere."
        svet.name "I suppose. Be careful."
        pc "You too."
    jump random_event_picker_dance_party_talk_svet_end

label dance_party_first_event_chain_4:
    $ quest_dancevip.dict["intro_chain"] += 1
    show theo at right1 with dissolve
    theo.name "Enjoying yourself?"
    pc "Not as much as these guys I imagine."
    theo.name "Good to hear. Hope you are all entertaining them."
    pc "Party is young, we will find out later I suppose."
    theo.name "The blonde girl, she seems a bit..."
    theo.name "Aloof?"
    pc "Yeah no need to find weird words to use. I know what you mean."
    theo.name "Is she okay?"
    pc "Probably not."
    theo.name "Right..."
    theo.name "Don't really want her scaring people off."
    pc "Yeah, I'll see what I can do."
    theo.name "Thanks. Well, I'll leave it to you."
    hide theo with dissolve
    pcm "Hmmm, He's right. This really isn't the type of place [anabel.name] should be."
    pcm "Knowing her, she might cause trouble with one of the guys."
    if player.has_perk([perk_party_girl, perk_alcoholic, perk_addict, perk_joy_addict, perk_wasted, perk_blackout], notif=True) or player.check_drunk(3, notif=True):
        pcm "I should fill her up with booze. That might make her more cheerful around here."
        if inv.qty(item_joy):
            pcm "Have some joy I might be able to give as well."
        elif inv.qty(item_lebo):
            pcm "Have some lebo on me as well. But getting her to take that is kind of fucked up."
        $ add_to_list(quest_dancevip.list, "anabel_harm")
    elif player.has_perk([perk_sucu, perk_bimbo], notif=True):
        pcm "Maybe it's about time she tried to enjoy herself."
        pcm "Hmmm..."
        pcm "Maybe I can stick some booze in her and she will let someone stick something else in her."
        pcm "Might loosen her up."
        $ add_to_list(quest_dancevip.list, "anabel_harm")
    elif player.has_perk([perk_meek, perk_broken, perk_deadinside], notif=True):
        pcm "Whatever, I guess that's on her. None of my business really."
        $ add_to_list(quest_dancevip.list, "anabel_neutral")
    elif player.vvirgin or player.has_perk([perk_bambi]):
        pcm "Doubt she want's to end up in one of the bedrooms and lose her virginity that way. I know I don't want to."
        pcm "Pretty sure she is a virgin anyway, the way she hates men."
        pcm "Maybe I should try to keep her out of trouble."
        $ add_to_list(quest_dancevip.list, "anabel_help")
    else:
        pcm "Not sure it's my business to worry about what happens with her."
        pcm "I guess I could help her out and make sure she stays out of trouble."
        pcm "Could also help her get into more trouble..."
        menu:
            "Get her drunk and into trouble":
                $ add_to_list(quest_dancevip.list, "anabel_harm")
                pcm "Heh, okay, I'll get her to loosen up."
            "Leave her to deal with it herself":
                $ add_to_list(quest_dancevip.list, "anabel_neutral")
                pcm "Yeah, she's a grown woman. She can deal with her own issues."
            "Help her out and keep her safe":
                $ add_to_list(quest_dancevip.list, "anabel_help")
                pcm "Ugh, probably going to cost me as well. But I should look out for her."
    jump travel



label dance_party_ending_goodbye_first:
    if "goodnight_event_first_played" in quest_dancevip.list:
        if svet_here():
            show svet at right1 with dissolve
            svet.name "Head home and sober up. We will talk about this at the academy."
            pc "Right."
            hide svet with dissolve
        elif anabel_here():
            show anabel at right1 with dissolve
            anabel.name "Too drunk, go home and we can talk on Monday or something."
            pc "Okay."
            hide anabel with dissolve
        elif dani_here():
            show dani at right1 with dissolve
            dani.name "Shoild go home [name]. Think things over."
            pc "Okay."
            hide dani with dissolve
        else:
            show rachel at right1 with dissolve
            rachel.name "Whoo. Good night [name]. See you on Monday!"
            pc "See you [rachel.name]."
            hide rachel with dissolve
        jump travel


    $ add_to_list(quest_dancevip.list, "goodnight_event_first_played")
    if svet_here():
        show svet at right1 with dissolve
        pc "Phew. That's finally over."
        svet.name "Yeah. Head home and sober up. We can talk about how it went another day."
        if all([rachel_here(), dani_here(), anabel_here()]):
            pc "Okay, looks like everyone is here safe and sound. I'll be heading home then."
            svet.name "Travel safe."
        elif any([rachel_here(), dani_here(), anabel_here()]):
            pc "Okay, looks like we are missing people. You going to wait around?"
            svet.name "Yeah, I'll stick around and see who turns up."
            pc "Okay, bit dangerous around here. Be safe."
        else:
            pc "Only you and me made it out? You sticking around to see if anyone else emerges?"
            svet.name "For a bit. Doubt I need to though. I'm sure they can look after themselves."
            pc "Okay, bit dangerous around here. Be safe."
        hide svet with dissolve

    elif dani_here():
        show dani at right1 with dissolve
        pc "Phew. That was some party."
        dani.name "Yeah, pretty intense."
        pc "You heading home?"
        dani.name "In a bit. I just want to get a bit of fresh air first."
        if not all([rachel_here(), svet_here(), anabel_here()]):
            pc "Doesn't look like everyone is here. Maybe should talk about the night at the academy."
            dani.name "Yeah probably. Goodnight [name]."
            pc "Night [dani.nname]."
        else:
            pc "Been a bit too much booze flowing. So probably chat about tonight once we sober up."
            dani.name "Yeah probably. Goodnight [name]."
            pc "Night [dani.nname]."
        hide dani with dissolve
    elif anabel_name():
        show anabel at right1 with dissolve
        anabel.name "Good to see you safe [name]."
        if not all([rachel_here(), svet_here(), dani_here()]):
            pc "You too. Not everyone here though."
            anabel.name "Nope."
            pc "Sticking around and waiting for them?"
            anabel.name "A little. But mostly getting some air. I will go home soon."
            pc "Be safe [anabel.nname]."
        else:
            pc "Looks like everyone else is here as well. So I'll be heading home."
            anabel.name "Goodnight [name]."
        hide anabel with dissolve
    else:
        show rachel at right1 with dissolve
        rachel.name "Whoo. That was fun."
        pc "Yeah, why are you waiting here?"
        rachel.name "[svet.nname] the dirty slut is always telling me off, but she is still up there."
        rachel.name "I'm gonna tell her off!"
        pc "Right, well don't get dragged off while waiting. I'm going to head home."
        rachel.name "See ya [name]."
        hide rachel with dissolve
    jump travel


label dance_party_end_first_party:
    if not "party_sex" in anabel.list and "anabel_help" in quest_dancevip.list:
        if not anabel_here():
            pcm "Suppose I should check and see if [anabel.name] is doing okay."
            $ walk(anabel_here(class_loc=True))
            show anabel at right1 with dissolve
            pc "Survived the party?"
            anabel.name "Yeah..."
            if "topeless" in anabel.list or "nude" in anabel.list:
                pc "Should probably grab the clothes you lost. Be heading out soon."
            else:
                pc "Be heading out soon. I'll check on the others."
            anabel.name "Right..."
            hide anabel with dissolve
    if dance_someone_having_sex():
        if dance_everyone_having_sex():
            $ walk(loc_party_hall)
            pcm "..."
            $ walk(loc_party_main)
            pcm "Really?"
            pcm "Everyone has gone without me?"
            pcm "Probably not, no way [rachel.name] would leave. She is probably in one of the bedrooms."
        elif dance_someone_having_sex():
            $ walk(loc_party_hall)
            pcm "..."
            $ walk(loc_party_main)
            pcm "Not everyone is here..."
            pcm "They can't have just left alone. At least I hope not."
            pcm "One of these pervs probably took them off into one of the rooms."

        pcm "Suppose I should check..."

        if "party_sex" in svet.list:
            $ walk(svet_here(class_loc=True), trans=False)
            show dance_svet_buk
            with dissolve
            $ player.face_worried()
            pc "Err..."
            pc "Okay..."
            pc "..."
            $ walk(loc_party_main, trans=False)
            hide dance_svet_buk
            with dissolve
            pcm "Right then. [svet.name] is having a bunch of men on her face..."
            if not svet.showing:
                pcm "Probably for the best. Won't leave here with a baby."

        if "party_sex" in rachel.list:
            $ walk(rachel_here(class_loc=True), trans=False)
            show dance_rachel_dp
            with dissolve
            if player.has_perk([perk_slut, perk_bimbo, perk_sucu]):
                $ player.face_happy()
            else:
                $ player.face_worried()
            rachel.name "Ahhh fuck yes!"
            pc "Ah!"
            show dance_rachel_dp look
            rachel.name "Ah [name]! Ahhhh fuck! You here for fun?"
            pc "Err... No, just checking everyone is alive."
            rachel.name "Ha fuck. This guy put it in my arse. Nasty bastard."
            pc "Err, yeah, I guess no where else to put it."
            show dance_rachel_dp ag
            rachel.name "Haaaa fuck yes!"
            $ walk(loc_party_main, trans=False)
            hide dance_rachel_dp
            with dissolve
            pcm "Well, seems she is fine."
            pcm "Mostly."
        if "party_sex" in dani.list:
            $ walk(dani_here(class_loc=True), trans=False)
            show dance_dani_group lookup
            with dissolve
            dani.name "Mmmmf!"
            $ player.face_worried()
            pc "Err..."
            show dance_dani_group lookback
            pc "All good?"
            dani.name "Mmmmfff gug."
            pc "I'll take that as a yes."
            show dance_dani_group lookup
            pc "Err, well have fun. I'm heading home."
            $ walk(loc_party_main, trans=False)
            hide dance_dani_group
            with dissolve
        if "party_sex" in anabel.list:
            $ walk(anabel_here(class_loc=True), trans=False)
            show dance_anabel_behind
            with dissolve
            $ player.face_shock()
            "Man" "Ah yes you fat fucking whore!"
            anabel.name "Ahhhh!"
            "Man" "Take it you slut!"
            anabel.name "Uhhh nyy goooood..."
            pcm "Right, didn't expect [anabel.name] to be going for that."
            pcm "Right then..."
            $ walk(loc_party_main, trans=False)
            hide dance_anabel_behind
            with dissolve

        if not dance_everyone_having_sex() and dance_someone_having_sex():
            pcm "Guess I'll round up whoever is left and head off together."
        elif dance_everyone_having_sex():
            pcm "Guess I'll head off alone then."

        show theo at right1 with dissolve

        theo.name "Ah you girls were a good choice to manage this party."
        if dance_everyone_having_sex():
            pc "Err, yeah I suppose. I'm the only one not bent over in a bedroom. So I guess the guys are having fun."
        else:
            pc "Err, yeah I suppose. Some of us got dragged off into a bedroom so I guess the guys are having fun."
        theo.name "I'm sure they are."
        theo.name "So, same time next week?"
        pc "Err, you are doing this every week?"
        theo.name "We will if I can get you girls entertaining."
        pc "Whoring you mean."
        theo.name "Same thing at the end of the day."
        pc "..."
        pc "I guess we will have to have a talk about it."
        theo.name "I would expect so."
        theo.name "[svet.name] and [dani.name] knows how to get in touch."
        theo.name "You can stay here for the night if you want. It's late."
        pc "Err, thanks for the offer. What's the chances of me waking up with some guy in my bed?"
        theo.name "Err... High? There aren't any locks on the door."
        pc "Right."
        theo.name "Well, I hope to be seeing you again [name]."
        pc "Sure. Good night."
        hide theo with dissolve
    else:


        $ walk(loc_party_hall)
        pcm "..."
        $ walk(loc_party_main)
        pcm "Looks like everyone is here."
    $ pc_dress_event("daily", loc_party_bedroom1)
    $ school_dance_leave_party()
    $ walk(loc_party_main)
    $ walk(loc_revel_backstreet)
    pcm "That was..."
    pcm "Something..."
    pcm "Suppose I should meet with the girls and see their thoughts on how this night went."
    if partyman.name in anabel.sex_who and not "anabel_harm" in quest_dancevip.list:
        pcm "Kinda shocked at [anabel.name] going off with guys like that."
        pcm "Hope she had fun."
    elif partyman.name in anabel.sex_who:
        pcm "Also managed to get [anabel.name] to let off some steam."
        pcm "Seemed those guys were giving her a good time."
        $ player.face_evil()
        pcm "She will thank me later."



    $ log.markdone("quest_dancevip_02")
    jump travel

label dance_party_academy_meetup_start:
    $ add_to_list(dani.list, "no_location")
    $ add_to_list(svet.list, "no_location")
    $ add_to_list(rachel.list, "no_location")
    show svet sport at right1
    show rachel sport happy at left4
    with dissolve
    rachel.name "...my ass the entire time."
    rachel.name "He was saying some rubbish like \"make it so you cant walk outta here\"."
    rachel.name "Whatever. Idiots always saying things."
    svet.name "So how did you end up, y'know."
    rachel.name "Ah! So he is going at it for ages. Dirty little bunny. In my ass for aaaages. It was kinda fun."
    svet.name "Right, so...?"
    rachel.name "He doesn't last. He makes my ass sticky and it's late, so I laugh at him. \"Haha I can walk. You can't make me weak.\""
    rachel.name "But he must have fucked my asshole too much. I was laughing at him and then shit myself."
    show svet worried
    $ player.face_shock()
    svet.name "What the fuck [rachel.name]!"
    rachel.name "He just looked at me, laughed and shut the door."
    rachel.name "I am ass naked with it leaking all down my legs."
    svet.name "Fucking hell. [rachel.name], what...?"
    rachel.name "I grabbed my skirt and ran out the door barefoot."
    pc "And tits out?"
    rachel.name "Arse out as well. I didn't wear the skirt. It made good toilet paper."
    rachel.name "Ah yeah. I need a new skirt."
    svet.name "God [rachel.name]. How can you..."
    svet.name "I don't even know anymore... [name], help me out here."
    pc "Err..."
    $ player.face_happy()
    pc "So the guy fucked the shit out of you then?"
    svet.name "[name]!"
    show rachel at right2 with dissolve
    rachel.name "Ha, yeah he did."
    show dani sport at left1 with dissolve
    dani.name "Hey guys."
    show svet neutral
    svet.name "Oh thank fuck."
    dani.name "Everything okay."
    svet.name "No, not even close."
    dani.name "Why not?"
    svet.name "Don't listen to [rachel.name]."
    dani.name "Okay..."
    if "bad_end" in anabel.list:
        jump dance_party_academy_meetup_bad_end
    else:
        jump dance_party_academy_meetup_good_end

label dance_party_academy_meetup_bad_end:
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    $ remove_from_list(rachel.list, "no_location")
    svet.name "Most of us are here now. Where is [anabel.name]?"
    dani.name "Not seen her since the party."
    svet.name "She did make it home okay didn't she?"
    dani.name "I didn't check..."
    if "anabel_harm" in quest_dancevip.list:
        pc "I checked the bedrooms before leaving. [anabel.name] was enjoying her booze with some guys."
        svet.name "Err, that doesn't sound like her."
        pc "She had a good go with the free wine and went off with some people."
        pc "Popped my head in and some guy had her bent over."
    elif "anabel_help" in quest_dancevip.list:
        pc "I was trying to keep an eye on her at the party. But at some point I lost track of her."
        svet.name "So no one saw her after?"
        pc "I checked the rooms before I left. I think some guys might have got hold of her..."
    else:
        pc "I noticed she went missing at some point, went off with someone I think."
        pc "Was checking rooms before I left and she was naked with someone. I didn't inturrupt."
    svet.name "Fuck. That's the last thing she would have..."
    anabel.name "You fucking sluts!"
    $ player.face_worried()
    show dani worried
    show svet worried at left3
    show rachel happy at left2
    show anabel uni angry at right1
    with dissolve
    anabel.name "I trusted you all. And you take me to a fucking whore party!"
    dani.name "[anabel.nname], we..."
    anabel.name "I don't fucking care. Especially you [dani.nname]! After all we went through, you bring us back to that shit!"
    anabel.name "You deserve to be murdered in an alley by these fucks!"
    dani.name "[anabel.name]..."
    anabel.name "None of you ever fucking speak to me again!"
    hide anabel with dissolve

    svet.name "Fuck..."
    show svet at right1
    show rachel at right2
    with dissolve
    svet.name "I knew we shouldn't have pushed her..."
    dani.name "..."
    hide dani with dissolve
    rachel.name "Sounded like she had fun to me."
    svet.name "..."
    rachel.name "So are you going next week as well?"
    svet.name "[rachel.name] do you not understand what we just did?"
    rachel.name "Had a great party?"
    svet.name "Ugh..."
    svet.name "Yeah, next week if you want to..."
    rachel.name "Great!"
    hide rachel with dissolve
    svet.name "Nothing to say [name]?"
    if "anabel_harm" in quest_dancevip.list:
        pc "She needed to let off steam. Having some fun should have done her good."
        svet.name "Obviously it didn't."
        pc "Yeah, seems so."
    else:
        pc "Guess we can't always be her babysitter. Hopefully she comes around."
        svet.name "Yeah, I don' see that happening."
    hide svet with dissolve
    pcm "Hmm, maybe I should try and talk to her."
    if "anabel_harm" in quest_dancevip.list:
        pcm "Considering I was the one pumping her full of booze though, not sure I should..."
    elif "anabel_help" in quest_dancevip.list:
        pcm "I did at least try to help. Not that it did much good."
    else:
        pcm "Seemed pretty upset though..."
    $ dani_yan_max_add(50)
    $ dani_yan_add(50)
    $ log.markdone("quest_dancevip_03")
    $ remove_from_list(anabel.list, "bad_end")
    $ anabel.hate = True
    if "anabel_harm" in quest_dancevip.list:
        $ anabel.hate_message = "She utterly hates me after I got her piss drunk at the VIP party and she was dragged off by a bunch of guys."
    else:
        $ anabel.hate_message = "She utterly hates me after we did a VIP party together and she ended up getting drunk and taken advantage of by a bunch of men."
    jump travel

label dance_party_academy_meetup_good_end:
    $ player.face_neutral()
    $ remove_from_list(dani.list, "no_location")
    $ remove_from_list(svet.list, "no_location")
    $ remove_from_list(rachel.list, "no_location")
    $ dani_yan_max_add(20)
    svet.name "Most of us are here now. Where is [anabel.name]?"
    dani.name "Not sure, should be here."
    svet.name "She did make it home okay didn't she?"
    dani.name "She left the party with us so I think so."
    show anabel at left2 with dissolve
    anabel.name "I'm here."
    svet.name "Ah good. So that's everyone. So I think we should talk about what happened at the party."
    rachel.name "It was fun. Free booze all night."
    if dani.iswhore:
        dani.name "It was... Ugh. Pretty much what was expected I suppose."
    else:
        dani.name "It was... Ugh, they wanted us there for more than just dancing."
    svet.name "Yes, I thought as much but it became obvious pretty quickly."
    anabel.name "Why are we talking about this?"
    svet.name "Because the guy offered us to go there on a regular basis."
    dani.name "Oh...?"
    anabel.name "I'm not interested."
    svet.name "Okay, that's fine. What about the rest of you?"
    rachel.name "I had fun. I wanna go again."
    if dani.iswhore:
        dani.name "It paid really well. As much as I don't really want to, I can't turn down that kind of pay."
    else:
        dani.name "I... I need the money so I can't say no..."

    if player.has_perk(perk_whore):
        pc "Yeah it payed quite well so I am happy to head there on a regular basis."
    elif player.has_perk([perk_party_girl, perk_bimbo]):
        pc "I also had a lot of fun there. Free party and fun times."
    elif player.has_perk([perk_slut, perk_sucu]):
        pc "Bunch of nice looking guys all in one place? Yeah sign me up."
    elif player.has_perk(perk_alcoholic):
        pc "Place has all the free booze I could drink. Might even go if they wern't paying just to get piss drunk."
    elif player.has_perk(perk_broken):
        pc "Entertaining a bunch of guys is pretty much all I am good at, so sure."
    elif player.has_perk([perk_meek, perk_bambi]):
        pc "That place was kinda scary. I felt like a baby deer in a lions cage."
    else:
        pc "I don't see a lot of reason to refuse. It's a paying job."

    svet.name "Well, this isn't really something we need to decide as a group I suppose."
    anabel.name "You're right. I don't care what the group decides. I am not going back there."
    svet.name "Mmm. They will keep doing the parties. You know the time and place. If you are interested then turn up."
    pc "Sounds good to me."
    dani.name "What about the park?"
    svet.name "I don't see a reason to stop, assuming everyone else still wants to."
    anabel.name "I don't think I will. I still want to dance here with you all, but these events have been pushing things too much for me."
    show dani worried
    dani.name "Aww [anabel.nname]..."
    show anabel at left2 with dissolve:
        xzoom -1
    anabel.name "I went along with it because of the group. But every time we do something, we get more perverts and less clothes involved."
    anabel.name "I don't care about any of that."
    show dani neutral
    show anabel at left2 with dissolve:
        xzoom 1
    dani.name "..."
    svet.name "Things have heated up a lot more than expected. No one should be doing anything they are not comfortable with."
    svet.name "You are still welcome to train with us [anabel.name]. Don't be pressured into doing something you will regret."
    anabel.name "Thanks..."
    svet.name "Well, okay then. I think that's everything."
    hide rachel with dissolve
    $ player.face_happy()
    pc "Don't worry [dani.nname], [rachel.name] is sure to keep you company at the parties."
    show dani happy at left1 with dissolve:
        xzoom - 1
    dani.name "Ha, yeah right. She will vanish five minutes in."
    pc "Err, I guess so."
    hide dani
    hide svet
    if "anabel_help" in quest_dancevip.list:
        hide dani
        hide svet
        show anabel at right1
        with dissolve
        anabel.name "Thanks for making sure I didn't drink too much and do something stupid."
        pc "No problem. Glad you made it home okay."
        hide anabel with dissolve
    else:
        hide dani
        hide svet
        hide anabel
        with dissolve
    $ log.markdone("quest_dancevip_03")
    $ add_to_list(anabel.list, "dance_event_refuse")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
