
label cass_mira_talk_photos_chain_0:
    $ mira.dict["photos_talk"] += 1
    mira.name "So, porn star [name]."
    cass.name "What? Porn star?"
    mira.name "Didn't you see?"
    cass.name "See what?"
    mira.name "[name] got a new job."
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_1:
    $ mira.dict["photos_talk"] += 1
    cass.name "I want a new job. What job does she have?"
    mira.name "I told you, a porn star."
    cass.name "Okay, now a serious answer?"
    pc "She is serious."
    cass.name "What???"
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_2:
    $ mira.dict["photos_talk"] += 1
    cass.name "Porn star? How do you even manage that with no videos or anything."
    pc "[mira.name] is messing with you. It's just some pictures for a magazine."
    cass.name "Oh? That's not so bad. It pay well?"
    pc "Yeah actually."
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_3:
    $ mira.dict["photos_talk"] += 1
    cass.name "Can I get photos?"
    mira.name "[cass.fullname] ginger gangbang!"
    cass.name "[mira.name]!"
    mira.name "Haha!"
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_4:
    $ mira.dict["photos_talk"] += 1
    cass.name "Okay, so photos?"
    pc "Someone is making a magazine to do promotions of this place."
    cass.name "Oh? Sounds easy."
    mira.name "Becoming a pimp as well [name]?"
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_5:
    $ mira.dict["photos_talk"] += 1
    pc "I can probably get you both in the pictures."
    cass.name "Really?"
    mira.name "[cass.name]..."
    cass.name "What?"
    mira.name "Have you seen the pictures?"
    cass.name "No. Why?"
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_6:
    $ mira.dict["photos_talk"] += 1
    mira.name "You wouldn't even recognise [name] since there are so few pictures of her face."
    cass.name "Isn't that better? No weirdos recognising you."
    mira.name "Well, yeah I guess so."
    mira.name "I can now tell you how many moles [name] has on her arse."
    pc "Really? Now many?"
    mira.name "Errr... Actually, none that I saw..."
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_7:
    $ mira.dict["photos_talk"] += 1
    pc "[mira.name] is a pervert."
    cass.name "She showed me the magazine!"
    pc "Oh?"
    cass.name "You trying to get me to show off my arse as well?"
    pc "Not at all!"
    pc "With you it would be the tits."
    mira.name "Hahaha!"
    jump cass_mira_talk_end

label cass_mira_talk_photos_chain_8:
    $ mira.dict["photos_talk"] += 1
    pc "But you two will be fine for the magazine."
    cass.name "She really is pimping!"
    mira.name "Yeah, bad [name]!"
    pc "Sure sure. Come to me alone and I'll set you up."
    $ add_to_list(felix.list, "cass_mira_photos")
    jump cass_mira_talk_end





label cass_mira_talk_kidnap_explain_0:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    pc "When me and [cass.nname] started working here, the girls all mentioned to look out for each other."
    mira.name "Yeah, need to, otherwise... Well, y'know."
    pc "Yeah. Did they catch you off guard or something?"
    mira.name "..."
    mira.name "Something like that..."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_1:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "It was some regular guy, I knew him quite well so didn't think there would be a problem."
    mira.name "But I don't know, he fell in love or something. Crazy weirdo."
    pc "..."
    mira.name "I ended up bumping into him on my way home. Don't even remember much after that but woke in his basement."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_2:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "Seems like he specifically targeted me."
    pc "..."
    mira.name "Sorry. You probably don't want to hear this."
    pc "Me? It's fine. I just don't want to push you or something."
    mira.name "Na it's okay. That [psy.name] says it's good to talk with my friends about it."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_3:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "Actually [psy.name] hinted that you would be good to speak to about this stuff but wouldn't say why."
    mira.name "Did... something like this happen with you?"
    if log.completed("Slave"):
        pc "Yeah..."
        pc "Something pretty bad."
        $ add_to_list(mira.list, "haven_slave")
    elif log.completed("Haven"):
        pc "Yeah, sort of. Not as bad as you but ended up in a pretty shitty place for some time."
    else:
        pc "I speak to her as well. I kind of have to..."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_4:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "So I just woke in his basement. I thought it was some game at first."
    cass.name "A game?"
    mira.name "Yeah. Like some kinky play or something. So I wasn't even too worried at first."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_5:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "But then things kept going on. He wouldn't let me go..."
    mira.name "When I started getting angry and demanding to be let out, he got violent."
    mira.name "Started professing his love for me or some crazy stuff. Telling me how I would learn to love him eventually."
    mira.name "Kind of at that point I knew I just had to hold out and hope for some way to escape."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_6:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "Didn't expect security to come kicking the door down though."
    cass.name "They came in useful for once."
    mira.name "Heh. They just marched in and beat the shit out of him. Not even sure if he came out of the house alive."
    pc "Yeah I haven't heard about what happened to him. I was told not to ask."
    cass.name "Good. Only a shame he didn't suffer for long."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_7:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    mira.name "When I heard it was thanks to you two though... I couldn't believe it."
    pc "It was all [cass.nname]'s fault. She ruined your romantic getaway."
    cass.name "Me?"
    mira.name "Thanks guys."
    jump cass_mira_talk_end

label cass_mira_talk_kidnap_explain_8:
    $ mira.dict["whore_post_kidnap_talk"] += 1
    pc "We were just having fun in the highway. Pure coincidence we found you."
    mira.name "Yeah sure. They did tell me what happened."
    pc "All lies!"
    cass.name "Err. [name] is all shy it seems."
    jump cass_mira_talk_end






label cass_mira_talk_havenslave_explain_0:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    mira.name "So what happened to you that had [psy.name] all worked up."
    pc "..."
    pc "Not sure you want to hear about that."
    mira.name "Probably not. But I guess this talking stuff helps."
    pc "..."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_1:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "I had to go deep into the slums to find someone. Ended up in a bit of trouble there."
    cass.name "Find who?"
    pc "Doesn't matter. But I ended up making some people mad at me."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_2:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "They ended up beating me up and selling me to some place."
    cass.name "What? Selling you?"
    pc "Yeah... Much like [mira.name] I ended up waking up in some prison cell place stark naked."
    mira.name "I at least had a basement. Not a cell."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_3:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "I was confused as shit. 4 tiny walls, a bed, toilet and shower. No windows or daylight."
    mira.name "Wow..."
    pc "After being in there for some time, someone unlocked the door, beat me up a bit, raped me and left."
    cass.name "Fuck..."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_4:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "This happened for a while to \"train\" me."
    pc "Eventually they let customers in as well."
    mira.name "Shit. That's way worse than I had to suffer..."
    pc "..."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_5:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "Sometimes you would hear screaming from other rooms. It was a proper cell so I guess it was a police station or prison in the past or something."
    pc "Probably had a bunch of us all in their own cells."
    cass.name "..."
    pc "So I just did what they told me to do. No was could I escape and I doubted anyone would come to help."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_6:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "I was in that place so long I pretty much forgot my name..."
    cass.name "How long was it?"
    pc "At the time it felt like a lifetime. I found out after it was about half a year."
    mira.name "What? Fuck that is a long time."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_7:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "Security eventually raided the place and I got free. I assume the other prisoners as well but didn't actually see them."
    mira.name "..."
    pc "Spend more time in hospital recovering and also had to speak to [psy.name]."
    pc "Then they let me go and here we are..."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_8:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    cass.name "Is this kind of stuff common or something?"
    mira.name "Huh?"
    cass.name "I mean should I expect to be carted off as a sex prisoner or something?"
    cass.name "Happened to both of you. So, is this like, our life now?"
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_9:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    cass.name "\"Hey [cass.nname], where ya been?\" \"Ah t'know, got caught and lived in a sex dungeon for a bit, the usual.\""
    mira.name "Haha."
    cass.name "\"Food was terrible, had 4 babies and got my eye stabbed out. No biggie.\""
    pc "They should put that in the tourism guide."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_10:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    pc "We will miss you though [cass.nname]."
    cass.name "Miss me?"
    pc "Yeah, you are next on the sex slave list. See you in a year or so."
    mira.name "Can I sell your clothes while you are away? You won't be needing them."
    cass.name "Funny..."
    jump cass_mira_talk_end

label cass_mira_talk_havenslave_explain_11:
    $ mira.dict["whore_post_havenslave_talk"] += 1
    cass.name "You two better save my ass when I get dragged away."
    pc "Yeah, but after we sell your stuff and spend it on booze."
    mira.name "How long of a party do you think her stuff will get us?"
    pc "Eh... I think we need to whore her out some more. It's basically our savings."
    $ add_to_list(cass.list, "kidnap_jokes")
    jump cass_mira_talk_end





label cass_mira_talk_postwhore_0:
    $ mira.dict["whore_post_rescue_talk"] += 1
    pc "You two are here?"
    cass.name "Yeah. Keep each other company."
    pc "Would have thought after all that happened that I wouldn't see you here again."
    mira.name "Yeah... I thought about it. But how else will I get money."
    jump cass_mira_talk_end

label cass_mira_talk_postwhore_1:
    $ mira.dict["whore_post_rescue_talk"] += 1
    cass.name "Safer with the two of us always sticking together."
    pc "Yeah I bet. And you have the other girls around as well."
    mira.name "Yeah, you should stay with us as well if you are going to keep working."
    pc "Mmmm."
    jump cass_mira_talk_end

label cass_mira_talk_postwhore_2:
    $ mira.dict["whore_post_rescue_talk"] += 1
    pc "How's the other girls reacting to hearing about what happened?"
    mira.name "It's the same as always. Just need to make sure to keep an eye out for each other."
    pc "More security around here or anything like that?"
    mira.name "Of course not. They don't lift a finger for anything."
    jump cass_mira_talk_end

label cass_mira_talk_postwhore_3:
    $ mira.dict["whore_post_rescue_talk"] += 1
    mira.name "It's better there are no security around here anyway. They end up causing more problems than they solve."
    mira.name "And they end up scaring off the real customers while demanding free service."
    pc "Yeah, from what I have seen of them, probably safer to be with the weirdos."
    jump cass_mira_talk_end

label cass_mira_talk_postwhore_4:
    $ mira.dict["whore_post_rescue_talk"] += 1
    mira.name "No idea how you managed to get those lazy idiots off their arse to come and get me."
    pc "They wouldn't have if I didn't make use of a connection I have."
    mira.name "Oh? So if I need something done, I should come to you in future."
    pc "Call me Mistress [name]!"
    jump cass_mira_talk_end

label cass_mira_talk_postwhore_5:
    $ mira.dict["whore_post_rescue_talk"] += 1
    mira.name "[cass.nname]! Mistress [name] is here!"
    cass.name "Hide the booze!"
    pc "No! Give me the booze."
    mira.name "Run [cass.nname]! I'll hold her off!"
    jump cass_mira_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
