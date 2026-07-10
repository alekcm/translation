




label mira_whore_discover_talk_0:
    $ mira.dict["whore_discover_talk"] += 1
    $ player.face_worried()
    pc "Hey, so... Err..."
    mira.name "Yes, it is what it looks like."
    pc "Right. Okay."
    mira.name "..."
    jump mira_talk_end

label mira_whore_discover_talk_1:
    $ mira.dict["whore_discover_talk"] += 1
    pc "So how did that come about? The highway I mean?"
    mira.name "Ugh. That's not a good story."
    pc "Yeah. Probably not. Sorry, I shouldn't have asked."
    jump mira_talk_end

label mira_whore_discover_talk_2:
    $ mira.dict["whore_discover_talk"] += 1
    mira.name "When everything turned to shit. I had nothing. Parents died and no food in the house."
    mira.name "So I went to live with an uncle. He didn't have much but was alive at least."
    pc "I think I can already see where this is going."
    mira.name "Pretty much."
    jump mira_talk_end

label mira_whore_discover_talk_3:
    $ mira.dict["whore_discover_talk"] += 1
    pc "So let me guess. Uncle wanted you to earn your food. But no jobs. But happens to have a friend who has money."
    mira.name "Wasn't quite as bad as that. We were starving and money was useless. Everyone needed food."
    mira.name "If you can't pay for food, then how else do you get it?"
    mira.name "It was me that made the offer to the hoarders. Uncle didn't know about it."
    jump mira_talk_end

label mira_whore_discover_talk_4:
    $ mira.dict["whore_discover_talk"] += 1
    pc "Uncle must have guessed how you got it though. Food doesn't just appear like that."
    mira.name "He knew, but what could he say? It was this or die of starvation."
    pc "You still live with him?"
    mira.name "No. This was before I came to [town]. When things were kind of at their worst."
    pc "Ah."
    jump mira_talk_end

label mira_whore_discover_talk_5:
    $ mira.dict["whore_discover_talk"] += 1
    pc "So where is your uncle now?"
    mira.name "No idea. One day he went out and I never saw him again."
    pc "Oh... And this was when things were pretty bad?"
    mira.name "Yeah... I like to think he abandoned me for something better..."
    pc "..."
    jump mira_talk_end

label mira_whore_discover_talk_6:
    $ mira.dict["whore_discover_talk"] += 1
    pc "How did you end up here then?"
    mira.name "The place I was living, well the whole building, went up in flames one day."
    mira.name "I had to get out. No home any more so I just followed a main road and kept walking."
    mira.name "After a few days of sleeping in the dirt and eating grass, I ended up here. Compared to out there this place was a paradise."
    pc "I spent most of those days dying. So never saw how it was."
    jump mira_talk_end

label mira_whore_discover_talk_7:
    $ mira.dict["whore_discover_talk"] += 1
    mira.name "Believe it or not, things are a lot better now than when I arrived. It's quite safe now in comparison."
    pc "Only dragged in the bushes, beaten and raped once a week now?"
    mira.name "Haha. At least now they don't kill you to turn you into dried meat to sell."
    pc "Well... I guess that is better."
    jump mira_talk_end

label mira_whore_discover_talk_8:
    $ mira.dict["whore_discover_talk"] += 1
    pc "So why all this now that things are better?"
    mira.name "It's what I know how to do."
    pc "Could get another job now though. There are places that are doing okay and need people to work there."
    mira.name "And in every place people want to fuck. So might as well cut to the chase and bend over from the start."
    jump mira_talk_end

label mira_whore_discover_talk_9:
    $ mira.dict["whore_discover_talk"] += 1
    pc "Why do you even go to the academy?"
    mira.name "Why not? Nothing saying whores can't go. Look around you, a bunch of people here go there."
    pc "Err, really?"
    mira.name "It's fairly safe and free food. Better than waiting to get raped in the slum."
    jump mira_talk_end

label mira_whore_discover_talk_10:
    $ mira.dict["whore_discover_talk"] += 1
    pc "Going to be honest. If I had to put money on you or [cass.nname] working the highway, my money would have went on [cass.nname]."
    mira.name "Not sure if I should be upset at that or not."
    pc "Just didn't think you were the type when I met you."
    jump mira_talk_end

label mira_whore_discover_talk_11:
    $ mira.dict["whore_discover_talk"] += 1
    mira.name "Probably I would have put my money on [cass.nname] as well."
    mira.name "Red head, large... Yeah..."
    pc "Take her here for a job trial."
    mira.name "No way! She will put me out of a job!"
    mira.name "And, she's my friend or something."
    pc "Haha!"
    jump mira_talk_end

label mira_whore_discover_talk_12:
    $ mira.dict["whore_discover_talk"] += 1
    $ add_to_list(mira.list, "offered_whore_training")
    mira.name "Not that I would encourage it. But you any interest in doing this?"
    if quest_whore.active:
        pc "Err, I already asked around and found out how things work."
        mira.name "Oh? I didn't know. Well we can hang out together if you want. Keep each other safe."
        pc "Sure."
    elif player.has_perk(perk_whore):
        pc "Maybe. Not like I haven't made money this way already. Just not here."
        mira.name "Well, I can show you around if you want."
        pc "I'll think about it."
    else:
        pc "Seems dangerous."
        mira.name "Can be. Need to look out for each other."
        pc "I would imagine so."
        mira.name "Well, speak to me about it if you want."
    jump mira_talk_end





label mira_whore_pc_whore_0:
    $ mira.dict["whore_whore_talk"] += 1
    mira.name "[cass.nname] know you are a whore?"
    pc "Nope. She is better not knowing."
    mira.name "Yeah, It's why I don't tell her either."
    pc "Yeah..."
    jump mira_talk_end

label mira_whore_pc_whore_1:
    mira.name "What made you start whoring round here?"
    if player.has_perk(perk_gamine):
        pc "I used to do it before all this shit. So just started doing it again."
        mira.name "Really? Not many girls round here usd to be whores before."
        pc "Pretty different now though. No pimps."
        mira.name "Haha, yeah. The girls ended up killing the last ones that tried. No idea how they managed that."
    else:
        pc "No doubt the same as anyone else here. Need money and people are offering."
        mira.name "Yeah. Same story everywhere. Get fucked or starve."
        pc "Well, even normal jobs need you to get fucked if you want to earn."
    jump mira_talk_end

label mira_whore_pc_whore_2:
    $ mira.dict["whore_whore_talk"] += 1
    mira.name "So been keeping safe round here?"
    pc "Safe as can be. The girls stick together mostly so not dead yet."
    mira.name "Well, keep your guard up. Corpses are still found now and then."
    pc "Yeah, I know..."
    jump mira_talk_end

label mira_whore_pc_whore_3:
    $ mira.dict["whore_whore_talk"] += 1
    mira.name "It's expensive, but should get some pepper spray if you can."
    if inv.qty(item_pepperspray):
        pc "Yup. Got some here."
        mira.name "Good."
    else:
        pc "Yeah. Hard to get and expensive."
        mira.name "Think [havenvik.name] sells some. Or there is some guy on the beach selling it."
        if lake_dealer.sex or lake_dealer.osex:
            pc "Yeah, met him. He gives a discount if you fuck him."
        elif lake_dealer.has_met:
            pc "Yeah met the lake guy before."
        else:
            pc "Will have to check them out and see what they have."
    jump mira_talk_end

label mira_whore_pc_whore_4:
    $ mira.dict["whore_whore_talk"] += 1
    mira.name "Decided if you will take pills or not?"
    pc "What do you mean?"
    mira.name "Guys round here can get a bit shitty if you tell 'em what to do. Gonna end up knocked up at some point."
    pc "Ah, those pills."
    jump mira_talk_end

label mira_whore_pc_whore_5:
    $ mira.dict["whore_whore_talk"] += 1
    mira.name "Some of the girls round here take pills all the time. But ends up costing a fortune."
    mira.name "Just getting preggo is cheaper, but..."
    pc "But then you are pregnant."
    mira.name "Yeah..."
    if mira.showing:
        pc "I see you go the preggo route."
        if mira.heavy_preg:
            mira.name "Not really. Pills are expensive and it ended up a bit too late."
        else:
            mira.name "Not really... But at this point I need to use the expensive pills to get rid of it."
    jump mira_talk_end





label mira_whore_pre_academy_0:
    $ mira.dict["whore_pre_aca_talk"] += 1
    pc "So... I am assuming I should keep quiet about the whole highway thing."
    mira.name "Obviously."
    pc "I mean't from [cass.nname]. You are friends so maybe she knows."
    mira.name "Yeah, she doesn't know. And I don't want her to."
    pc "No problem."
    jump mira_talk_end

label mira_whore_pre_academy_1:
    $ mira.dict["whore_pre_aca_talk"] += 1
    pc "You don't think [cass.nname] will understand?"
    mira.name "Maybe she would. I still don't want her to know."
    mira.name "She is my friend, but I don't really want her to know those parts of life."
    pc "Who knows. Maybe she get's up to worse."
    mira.name "Haha, sure."
    jump mira_talk_end

label mira_whore_pre_academy_2:
    $ mira.dict["whore_pre_aca_talk"] += 1
    mira.name "Knowing her, if she knew she might even ask to come with me."
    pc "Ugh... That wouldn't end well for her."
    pc "Doesn't end well for anyone I suppose..."
    mira.name "Just got to get out early enough."
    jump mira_talk_end





label mira_talk_general_whore_slut_0:
    $ mira.dict["whore_slut_talk"] += 1
    pc "So, ever enjoy this stuff?"
    mira.name "Being an object for men?"
    pc "Having lots of hot men after you."
    mira.name "It's not as exciting as you seem to think."
    jump mira_talk_end

label mira_talk_general_whore_slut_1:
    $ mira.dict["whore_slut_talk"] += 1
    pc "Sounds exciting though."
    mira.name "What? Being a highway whore?"
    pc "Mmm, lots of fun with men, sore legs, having..."
    mira.name "I think you might need to buy some magazines and spend time alone at home."
    jump mira_talk_end

label mira_talk_general_whore_slut_2:
    $ mira.dict["whore_slut_talk"] += 1
    pc "Why buy a magazine when I can hear sexy stories from you?"
    mira.name "Because my stories are not sexy."
    pc "C'mon, I bet you have done lots of exciting things."
    mira.name "You think hanging out here in the cold until some guy pays you to go to his room is exciting?"
    pc "Of course!"
    jump mira_talk_end

label mira_talk_general_whore_slut_3:
    $ mira.dict["whore_slut_talk"] += 1
    pc "Why buy a magazine when I can hear sexy stories from you?"
    mira.name "Because my stories are not sexy."
    pc "C'mon, I bet you have done lots of exciting things."
    mira.name "You think hanging out here in the cold until some guy pays you to go to his room is exciting?"
    pc "Of course!"
    jump mira_talk_end

label mira_talk_general_whore_slut_4:
    $ mira.dict["whore_slut_talk"] += 1
    mira.name "If you have such a dirty fantasy, why don't you try it out?"
    pc "I might. Probably will. But still fun to hear what you have to say."
    mira.name "It's not all the excitement you seem to think it is."
    pc "Or maybe you take it too seriously."
    jump mira_talk_end

label mira_talk_general_whore_slut_5:
    $ mira.dict["whore_slut_talk"] += 1
    mira.name "Going to send one of my customers to you next time, see how it makes you feel."
    pc "Hmm, don't want to be stealing your money."
    mira.name "Steal my money? I'll get him to pay me and send you off to make him happy."
    pc "Ah, sounds dirty!"
    jump mira_talk_end

label mira_talk_general_whore_slut_6:
    $ mira.dict["whore_slut_talk"] += 1
    pc "You also have those rooms I hear about."
    mira.name "Yeah, I would avoid..."
    $ male_npc_create_all()
    $ tempname = punter
    $ quest_temp = None
    show male_generic at left4 with dissolve
    tempname.name "Up for some fun?"
    mira.name "Sure, or you can have fun with my friend here. She is new."
    pcm "Fuck!"
    tempname.name "Doesn't matter to me."
    mira.name "You up for it?"
    if player.check_sex_agree():
        menu:
            "Go with the man":
                $ add_to_list(mira.list, "slut_customer_agreed")
                pc "Err... Okay..."
                mira.name "Have fun."
                $ player.set_whore_price(1)
                hide mira
                show male_generic at right1
                with dissolve
                jump whore_street_customer_pick_location_tombola
            "Back out of it":


                $ NullAction()
    $ add_to_list(mira.list, "slut_customer_refused")
    pc "Err, no thanks. I think I'll leave that to you."
    mira.name "Suit yourself."
    $ add_to_list(mira.list, "whore_having_sex")
    hide mira
    hide male_generic
    with dissolve
    "I watch as [mira.name] walks off with the guy."
    jump travel

label mira_talk_general_whore_slut_7:
    $ mira.dict["whore_slut_talk"] += 1
    if "slut_customer_agreed" in mira.list:
        mira.name "So have fun with your customer?"
        pc "I guess. Not much different from most guys."
        mira.name "Then I guess you got a good one."
        pc "Or the average guys are just so shitty."
        mira.name "Haha."
    else:
        mira.name "So asking about all the fun then getting scared when I offer you a guy?"
        pc "Well yeah, not quite sure I'm ready to be a back alley whore."
        mira.name "Don't think anyone is ever ready. Most of us are forced into it."
    jump mira_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
