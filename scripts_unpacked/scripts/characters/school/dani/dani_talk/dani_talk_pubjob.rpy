
label pub_askjob_talk_trigger:
    $ add_to_list(dani.list, "asked_pub_work")
    dani.name "How's working at the pub? Debating if I should give it a shot."
    pc "Short skirt and horny men who are also drunk. Worse than the bus."
    dani.name "But what's the pay like?"
    if pub_waitress.sex:
        pc "Depends on if you let the drunks do what they want."
        dani.name "And if you do?"
        pc "Then the pay is pretty good."
    else:
        pc "Mostly tips. Get the guy's to like you and they tip better."
        dani.name "Oh?"
        pc "Mmmm..."
    jump dani_talk_end

label pub_askjob_talk_0:
    $ dani.dict["pub_askjob_talk"] += 1
    dani.name "So how did you get the job in the pub?"
    pc "Just walked in and asked."
    dani.name "Just like that? You didn't know someone who worked there or anything?"
    pc "Na, just asked and they told me to come back later for a shift."
    dani.name "That easy?"
    pc "Well, I guess they struggle to keep people working there."
    jump dani_talk_end

label pub_askjob_talk_1:
    $ dani.dict["pub_askjob_talk"] += 1
    dani.name "Why does the pub have trouble keeping people working there?"
    pc "Girls in short dresses and drunk men everywhere? Have a guess."
    dani.name "They ever, y'know... with you?"
    pc "Of course. It's basically part of the job."
    dani.name "..."
    jump dani_talk_end

label pub_askjob_talk_2:
    $ dani.dict["pub_askjob_talk"] += 1
    dani.name "What happens if you tell the drunks in the pub to stop?"
    pc "They probably don't. Need to walk away for them to stop."
    dani.name "And they don't chase you or anything?"
    pc "No. Most of the time they are well behaved."
    dani.name "Really?"
    pc "Their hands will wander everywhere when you are close to them. But they never try to hit you or anything."
    dani.name "That's... good I suppose?"
    pc "Yeah."
    jump dani_talk_end

label pub_askjob_talk_3:
    $ dani.dict["pub_askjob_talk"] += 1
    $ add_to_list(dani.list, "willwork_pub")
    $ dani.dict["pub_started_working"] = (t.day + 3)
    pc "Anyway, stop asking a hundred questions about the pub and go try it out."
    pc "Work a shift or two and see if it's something you can handle."
    if dani.iswhore:
        pc "Not like you haven't sold yourself before anyway so shouldn't be an issue."
    dani.name "Just walk in there and ask?"
    pc "Sure, if I'm not there just tell [trixie.name] you know me. She will sort you out."
    dani.name "Right..."
    jump dani_talk_end



label dani_gotjob_talk_0:
    $ dani.dict["pub_gotjob_talk"] += 1
    dani.name "So I went to the pub and asked about work."
    if "asked_about_dani" in trixie.list:
        pc "Yeah, [trixie.name] told me you popped by."
    else:
        pc "Oh you did? Good for you."
    pc "The money isn't great but the work isn't too bad either."
    dani.name "I'll see I suppose."
    jump dani_talk_end

label dani_gotjob_talk_1:
    $ dani.dict["pub_gotjob_talk"] += 1
    dani.name "Anything I should know about the place before I start?"
    pc "You just bring drinks to people who flag you down."
    pc "Pretty simple since there aren't many drinks. So you just walk around with a beer until someone wants one from you."
    dani.name "Hmmm..."
    jump dani_talk_end

label dani_gotjob_talk_2:
    $ dani.dict["pub_gotjob_talk"] += 1
    dani.name "What about the... err... perverts in the pub?"
    pc "What about them?"
    dani.name "What do I do about them?"
    pc "Depends how much you want the money."
    dani.name "Really?"
    jump dani_talk_end

label dani_gotjob_talk_3:
    $ dani.dict["pub_gotjob_talk"] += 1
    dani.name "So, like, it's not expected to do that sort of thing in the pub?"
    pc "No, can work there fine without anything weird."
    pc "I mean some guy might try and put his hand up your skirt but it's fine to walk away."
    dani.name "..."
    jump dani_talk_end

label dani_gotjob_talk_4:
    $ dani.dict["pub_gotjob_talk"] += 1
    dani.name "And what if you don't walk away in the pub when they touch you?"
    pc "Then make sure you get paid for the touching."
    dani.name "You won't get fired for letting it happen?"
    pc "Ha! No."
    pc "Do as much or as little as you want. Just make sure it's worth it."
    pc "Also there is spare underwear in the lockers in case you sell yours."
    jump dani_talk_end

label dani_gotjob_talk_5:
    $ dani.dict["pub_gotjob_talk"] += 1
    $ dani_yan_max_add(20)
    dani.name "Wait, sell your underwear?"
    pc "Yeah, some weirdos will buy anything."
    dani.name "Wow."
    pc "Just make sure you make more than you have to buy them for."
    pc "And be careful if you sold them. Bending over in that skirt will show everything."
    dani.name "..."
    pc "Or, y'know. Bend over more?"
    show dani happy
    dani.name "[name]!"
    jump dani_talk_end



label dani_talk_workingpub_chain_0:
    $ dani.dict["talk_workingpub_chain"] += 1
    pc "So how you finding the pub now you have worked there a bit?"
    dani.name "Not as bad as I thought it would be."
    pc "Really?"
    dani.name "It's only really a short dress."
    pc "And a room full of horny drunks."
    dani.name "Yeah, that's not far off being like anywhere else."
    jump dani_talk_end

label dani_talk_workingpub_chain_1:
    $ dani.dict["talk_workingpub_chain"] += 1
    dani.name "The job is mostly fine."
    pc "Honestly I thought you would have quit on your first day."
    pc "Or been fired for hitting someone."
    show dani angry
    dani.name "If I were going to hit someone, [oskar.name] is first on my list."
    dani.name "Until he never gets up again."
    pc "I would pay to see that."
    dani.name "..."
    show dani neutral
    jump dani_talk_end

label dani_talk_workingpub_chain_2:
    $ dani.dict["talk_workingpub_chain"] += 1
    dani.name "The job does kind of piss me off. But..."
    dani.name "The perverts at the pub are kind of okay."
    pc "Wow, really?"
    dani.name "They aren't forcing me to do something I don't want."
    dani.name "They drink and look. If they want more then they offer to pay for more."
    pc "I guess so. They rarely push for more than you are willing."
    jump dani_talk_end

label dani_talk_workingpub_chain_3:
    $ dani.dict["talk_workingpub_chain"] += 1
    pc "They do try to get you shit drunk in the pub though."
    dani.name "Yeah. Not entirely a bad thing."
    pc "Not really. Even if their motives are not pure."
    dani.name "Don't think ours are either."
    pc "No?"
    dani.name "Flashing our arses to bleed them of money they can barely afford?"
    dani.name "Yeah, they are probably just as screwed as we are."
    jump dani_talk_end



label dani_talk_whoreingpub_chain_0:
    $ dani.dict["talk_whoringpub_chain"] += 1
    show dani worried
    dani.name "So..."
    pc "Hmm?"
    dani.name "I ended up agreeing to into the back room with a customer."
    pc "Oh...?"
    pc "Not too bad I hope."
    if pub_waitress.sold:
        dani.name "Pretty much what I expected after seeing you and [trixie.name] do it."
    else:
        dani.name "Pretty much what I expected after seeing [trixie.name] do it."
    if quest_daniwine.active:
        dani.name "Wouldn't mind if you could get some wine and come over."
        if inv.qty(item_winebottle):
            pc "Sure, I have some with me so I'll pop by later."
        else:
            pc "Sure, I'll pick some up and come over."
        if not log.interactive("quest_daniwine_02"):
            $ log.set_notdone("quest_daniwine_02")
    else:

        dani.name "Would kill for something nice to take my mind off it."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_1:
    $ dani.dict["talk_whoringpub_chain"] += 1
    pc "But everything okay with going into the back room with a drunk?"
    dani.name "Ugh, yeah it was fine."
    dani.name "I got paid. And that's all that really matters."
    pc "Yeah I guess so."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_2:
    $ dani.dict["talk_whoringpub_chain"] += 1
    pc "Going to keep doing it with the drunks."
    dani.name "You ask like you don't know the answer."
    pc "..."
    dani.name "We both knew this is where things were going working there."
    pc "I suppose."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_3:
    $ dani.dict["talk_whoringpub_chain"] += 1
    dani.name "At the end of the day, the pub is a whorehouse."
    pc "I wouldn't call it that."
    show dani angry
    dani.name "Whores like us whore there. What else would you call it?"
    pc "A pub with extra services?"
    dani.name "Yeah right. And who comes with no intention to get extra services?"
    pc "..."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_4:
    $ dani.dict["talk_whoringpub_chain"] += 1
    pc "I take it you haven't been to the highway?"
    dani.name "No. Well, I have. But I don't stick around. Why?"
    pc "If you had been there and looked around, you wouldn't call the pub a whorehouse."
    pc "Homeless whores everywhere selling themselves."
    dani.name "So the only difference is we aren't homeless?"
    pc "Yet."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_5:
    $ dani.dict["talk_whoringpub_chain"] += 1
    pc "That's not the only difference though."
    pc "We serve beers and people offer to fuck us. Highway girls are sticking their ass out with a price tag written on it."
    pc "For however many guys [trixie.name] fucks in the bar, you can add an extra zero for the highway girls."
    dani.name "Still the same thing though..."
    if log.interactive("quest_whore_02"):
        pc "The motel even has a room with a girl in it. She shows off by the window and guys go inside and fuck her."
        pc "Some literally live in the room and fuck fifty guys a night."
        dani.name "..."
    jump dani_talk_end

label dani_talk_whoreingpub_chain_6:
    $ dani.dict["talk_whoringpub_chain"] += 1
    pc "I guess I am just trying to say there is still a lot further to fall."
    pc "So, I dunno. Don't feel too bad or something."
    dani.name "..."
    pc "Booze helps."
    jump dani_talk_end



label dani_talk_gloryholepub_chain_0:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "Some strange hole appeared in the pub toilets."
    pc "Oh?"
    dani.name "Yeah."
    pc "Strange."
    jump dani_talk_end

label dani_talk_gloryholepub_chain_1:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "I wonder how the hole appeared there."
    pc "Aliens?"
    dani.name "..."
    pc "..."
    jump dani_talk_end

label dani_talk_gloryholepub_chain_2:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "Pretty sure a hole like that appeared in the academy as well."
    pc "Why would people commit such vandalism like that?"
    dani.name "Yeah, I wonder."
    pc "..."
    jump dani_talk_end

label dani_talk_gloryholepub_chain_3:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "I wonder what the hole in the bathroom is for."
    pc "Damn peeping toms!"
    dani.name "Yeah, sure. Peeping."
    pc "..."
    jump dani_talk_end

label dani_talk_gloryholepub_chain_4:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "Why did you make a hole in the toilet?"
    pc "Me? Why do you accuse me of doing it?"
    dani.name "Because you did it."
    pc "I am offended!"
    jump dani_talk_end

label dani_talk_gloryholepub_chain_5:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "So, why did you make it?"
    pc "Honestly, no idea. Mostly because I could."
    dani.name "I don't see any random holes anywhere else."
    pc "Want me to put one in your room?"
    dani.name "I will kick you!"
    pc "Haha!"
    jump dani_talk_end

label dani_talk_gloryholepub_chain_6:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    pc "Maybe people want to make use of the hole."
    dani.name "As if people make a secret of just wanting to fuck us."
    pc "Well yeah, but easier to keep control when the pervert is on the other side of the wall."
    dani.name "Assuming they stay there."
    jump dani_talk_end

label dani_talk_gloryholepub_chain_7:
    $ dani.dict["talk_gloryholepub_chain"] += 1
    dani.name "And it's not like they don't know who is there."
    pc "They might not. Some whores come in the pub as well."
    dani.name "Yeah, but those whores are usually paid for. I doubt they are taking a break in the toilet to suck someone off."
    pc "Who knows. Get paid while you are getting paid."
    dani.name "Poor punter who paid for her."
    pc "Who cares about him."
    jump dani_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
