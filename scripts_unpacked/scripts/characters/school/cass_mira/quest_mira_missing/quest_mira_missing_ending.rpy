label quest_mira_missing_intel_complete:
    if not renpy.showing("cass"):
        show cass at right1 with dissolve
    pc "I think we have enough to piece together what happened to [mira.name]."
    cass.name "Looks to me like this guy took too much of a liking to her."
    pc "Seemed to be stalking her by the sounds of things."
    cass.name "He was doing it to some other girl ages ago, then she vanished and he wasn't seen for a while."
    pc "So you think the same as me? This cunt kidnapped her and is holding her somewhere?"
    cass.name "It... It looks that way to me..."
    cass.name "But what do we do about it? We don't even know where he lives. And even if we did..."
    pc "If we go chasing him down, then he will add us to his collection..."
    cass.name "Yeah."
    pc "Erm... Leave this with me. I have a contact I can use that might set things right."
    cass.name "How? One person won't be able to help us."
    pc "The person I am thinking of can help for sure. If he agrees then [mira.name] will be rescued in no time."
    cass.name "\"If he agrees\"."
    pc "Yeah. \"If\". But I am pretty sure he will."
    cass.name "I hope you are right."
    pc "So do I..."
    hide cass with dissolve
    pcm "So, I think at this point I need to go to [tucker.name] and ask for his help."
    pcm "Supposed to be me helping him so not sure if he will stick his neck out for me..."
    pcm "Can only ask though."
    $ add_to_list(quest_mira_missing.list, "told_cass_all_intel")
    jump travel

label quest_mira_missing_security_intel_complete:
    pc "So a friend of mine went missing, and I found out where she is."
    paige.name "Ah. Okay. Err... That's good?"
    pc "Yeah, but I need help getting her. She has been kidnapped and I can't do anything about it."
    paige.name "Normally we... Y'know? Wouldn't care."
    pc "What?"
    paige.name "Normally. Normally! But why are you asking me? Your boss would be better."
    pc "[tucker.sname]?"
    paige.name "Who else?"
    pc "Right..."
    $ add_to_list(quest_mira_missing.list, "asked_security")
    paige.name "Good luck."
    hide paige with dissolve
    pcm "So they won't do anything."
    pcm "No choice but to go to [tucker.sname]."
    jump travel

label quest_mira_missing_tucker_ending:
    $ player.face_happy()
    pc "Y'know. I've always thought you looked pretty snazzy in that suit."
    show tucker frown
    tucker.name "..."
    pc "Giving off the gruff professional vibe."
    tucker.name "What do you need?"
    pc "I bet the girls in the office are swooning when you walk by."
    $ player.face_neutral()
    tucker.name "We have work to do if you need money."
    pc "I might need a little more help than money."
    tucker.name "So..."
    $ player.face_frown()
    pc "I made a friend in the academy."
    tucker.name "Oh? Well the eggheads will be glad to hear you are capable of making friends. But I fail to see why you are trying to butter me up."
    pc "She has been kidnapped."
    tucker.name "Hmmm. That would normally be a job I would send you on to deal with."
    pc "Ah, I dealt with it already. I investigated and found out what happened to her. I know roughly where she is."
    tucker.name "So. Problem solved."
    pc "Almost. I am a tiny little girl who is all weak and fragile and need big strong men to beat people up."
    tucker.name "Get to the point."
    pc "I need you to get the goons to kick a few doors in and rescue my friend."
    tucker.name "Hmmm..."
    pc "Please?"
    tucker.name "You say you investigated it yourself?"
    pc "Yeah. Well me and another friend."
    tucker.name "This is the first I am hearing about it."
    pc "Well, it's my friend. Nothing to do with this place. I was worried you wouldn't like me sticking my nose in places I shouldn't."
    tucker.name "Well, I do pay you to stick your nose in places you shouldn't."
    pc "Well, yeah. But that's for you. Or The Institute. Whatever."
    tucker.name "I have a condition."
    pc "Well, this is a hospital. You can get it checked out easy enough. Have you been visiting suspicious ladies?"
    tucker.name "I want you to give a full debrief on everything you did and what happened."
    pc "Ugh!"
    pc "It's not a pretty story."
    tucker.name "All the more reason to hear it. It's not easy to track down a missing girl in [town]. People go missing all the time."
    pc "It wasn't..."
    tucker.name "I will arrange for you to speak to [psy.name] and go over things with her in detail. In the mean time I will speak to [miller.name]."
    $ player.face_worried()
    pc "Ugh... Okay..."
    hide tucker with dissolve
    pcm "Well, this is good I guess. [mira.name] will hopefully be saved so I guess I can go through all this stuff with [psy.name]."
    pcm "Hope she is okay..."
    pcm "Been a while since she was taken."
    pcm "Ugh."
    show brooker at right1 with dissolve
    psy.name "Hello [fname]."
    pc "Hi."
    psy.name "[tucker.name] has filled me on what little details he has. Would you like to come to my office?"
    pc "Not really."
    psy.name "Great. Come on. Let's walk together."
    pc "..."
    hide brooker with dissolve
    $ walk(loc_hospital_lobby)
    pcm "Going to have to tell everything aren't I?"
    show brooker at right1
    $ walk(loc_hospital_psy)
    psy.name "So, from what I hear you have been doing some investigating yourself."
    pc "Something like that."
    psy.name "From what I understand, a friend of yours went missing and you managed to track her down?"
    psy.name "That is not an easy thing to do and must have taken considerable effort."
    pc "Yeah, you could say that."
    psy.name "So, want to start from the beginning?"
    pc "Not really. But no choice I suppose."


    pc "So I have been going to the academy that [tucker.sname] set me up in. Made some friends there. [cass.nname] and [mira.name] on my first days."
    pc "Been chatting and hanging out with them since."


    if "met_whore_mira_as_whore" in quest_whore.list:
        pc "So, errm..."
        pc "I have kinda ben doing work up the highway area and bumped into [mira.name] doing the same."
        pc "So when [cass.nname] came to me some time later telling me [mira.name] had vanished, I suspected right away it was something to do with that."
        psy.name "Why would the work have something to do with it?"
        pc "Because it's the highway."
        psy.name "I don't follow."
        pc "Whoring."
        psy.name "Oh? Okay, I understand."
    elif "met_whore_mira" in mira.list:
        pc "One day I bumped into [mira.name] hanging around the highway area and had a bit of an awkward conversation."
        psy.name "Why awkward?"
        pc "Because she was whoring there."
        psy.name "Oh."
        pc "So when [cass.nname] came to me some time later telling me [mira.name] had vanished, I suspected right away it was something to do with that."
        psy.name "[cass.nname] wasn't aware?"
        pc "No. Not the kind of thing you announce to everyone."
    else:
        pc "So [cass.nname] comes to me one day asking if I have seen [mira.name]. She has been missing for a while and she is worried."
        pc "People don't just vanish so I asked friends if they had seen her."
        pc "One of the boys I drink with at night came up to me and told me he had seen her working the highway at night. So obviously that was the best place to start."
        psy.name "Why \"obviously\"?"
        pc "People who work the highway are whores. Hanging around the streets with strange men at the dead of night."
        psy.name "Right."




    if "investigate_whore_route" in quest_mira_missing.list:
        pc "So me and [cass.name] went to the highway to ask around. But it's not like anyone would have seen anything otherwise there would already be an uproar."
        pc "So kinda had to figure things out ourselves. But [cass.nname] was insistent that she helps. But no one round there will speak to you if you are not a whore."
        pc "So didn't manage to find anything out."
        psy.name "Why didn't you ask around?"
        pc "I offered. But [mira.name] was [cass.nname]'s best and i think only friend until I came along. So she insisted on doing things herself."
    elif "investigate_nowhore_route" in quest_mira_missing.list:
        pc "So one evening me and [cass.nname] went to the highway to ask around. Was mostly told to fuck off."
        psy.name "Why is that?"
        pc "Didn't know at the time. So we left."





    if "investigate_whore_route" in quest_mira_missing.list:
        pc "[cass.nname] ended up asking me to meet her later at Revel street."
        pc "I suspected what she might be getting at, and when I met her there it was confirmed."
        psy.name "What was?"
        pc "She had just came out a shop known for selling whore clothes looking like a whore herself."
        pc "I ended up taking her to the highway and introducing her to some of the girls I knew."
        pc "Ended up finding her a customer to go off with."
        psy.name "Why would you do that?"
        pc "The only way to be in with the whore crowd is to be a whore."
        pc "So she had to either be a whore or leave it to me."
        pc "I honestly thought the idea would scare her off. But she went along with it and kept returning the next days."
        psy.name "That's some dedication. Did the plan work?"
        pc "I'm here while [tucker.sname]'s goons go save [mira.name]. So yes."
        psy.name "That is good to hear. But I feel you are cutting part of the story short."
        pc "Of course I am."
        psy.name "Well, it would be better if you didn't."
    else:
        pc "So in the end I asked around to see what I could do."
        if "investigate_asked_security" in quest_mira_missing.list:
            pc "I went to security to see if they could help. No luck there but was told that whores only speak to whores."
        elif "investigate_asked_simon" in quest_mira_missing.list:
            pc "I went and paid a visit to [simon.fullname] and asked his advice."
            psy.name "[simon.fullname]? That name rings a bell."
            pc "Yeah, he was the guy [tucker.sname] had me investigate."
            psy.name "Wow. Making use of your contacts there. I am impressed."
            pc "He had already tried with the whores before. Told me they only speak with other whores."

        pc "When I went back to [cass.nname] with this info, she eventually asked me to meet her near one of the shops round Revel."
        psy.name "How would that help?"
        pc "To dress us as whores and go to the highway to ask around."
        psy.name "Oh? Did it work?"
        pc "I'm here while [tucker.sname]'s goons go save her. So yes."
        psy.name "That is good to hear. But I feel you are cutting part of the story short."
        pc "Of course I am."
        psy.name "Well, it would be better if you didn't."

    if quest_mira_missing.sold:
        pc "What? You want to hear about how I had to hang out the streets near naked and sell myself to men?"
    else:
        pc "What? You want to hear how I hung out round the highway near naked with strange men almost every night?"

    psy.name "If that's what you had to do, yes."
    pc "Ugh!"
    pc "Well yes. That's what I had to do."
    pc "..."
    psy.name "Go on..."
    pc "Really?"
    psy.name "Yes, everything you say will be helpful."
    pc "Ugh."
    pc "Me and [cass.name] had to go to the highway most nights and whore."
    pc "It's the only way we could make friends round there. With the other girls and with the punters."
    pc "Constantly asking around and piecing together what might have happened from all the little bits we found out."
    psy.name "So you weren't just told what happened?"
    pc "Of course not. Rumour of a shady guy here, suspicions of a missing girl there. Took ages to find out."
    psy.name "That is quite incredible."
    if quest_mira_missing.asex:
        pc "Yeah. Easy for you to say. I had to let men assfuck me to find this stuff out."
    elif quest_mira_missing.sex:
        pc "Yeah. Easy for you to say. I had to let men fuck me to find this stuff out."
    elif quest_mira_missing.osex:
        pc "Yeah. Say that next time you need to suck dicks to get what you want."
    else:
        pc "Yeah, say that to yourself next time you have to play the whore to get what you need."
    psy.name "Well, you pretty much had an impossible task. I don't think it quite matters how you did it. Only that you did."
    pc "..."
    psy.name "From what I am piecing together, [mira.name] may well be alive and safe because of what you did for her."
    psy.name "You did what you needed to do to save her. If the end result is her being alive, then you achieved everything you set out to do."
    pc "..."
    "*KNOCK KNOCK*"
    psy.name "Busy!"
    tucker.name "It's me. I have news."
    pc "[tucker.sname]!?"
    show tucker at right2 with dissolve
    pc "Did you find her?"
    tucker.name "They did. And she is alive."
    pc "Thank fuck!"
    tucker.name "But she is not in a good state. I am having security bring her here for medical treatment."
    pc "How bad?"
    tucker.name "We have no medics with her now to say anything definitive. But she is responsive and able to move."
    pc "So she won't go dying on her way here?"
    tucker.name "No. But she will need medical treatment for some time."
    tucker.name "Can I see you outside [psy.name]?"
    psy.name "Sure. One moment Miss [sname]."
    pc "..."
    hide tucker
    hide brooker
    with dissolve
    pcm "She is alive and can move. That's good news."
    pcm "Kidnapped all this time though. She will be a wreck no doubt."
    pcm "Who knows what she has been through..."
    show brooker at right1 with dissolve
    pc "Everything okay?"
    psy.name "It is. But you should go home now."
    pc "I want to see [mira.name]."
    psy.name "She will be in no condition to see anyone when she gets here. You would only be in the way."
    psy.name "Go and speak to your friend [cass.nname] and tell her the good news. Come back tomorrow and we might have more information."
    pc "..."
    psy.name "You have done your part Miss [sname]. Now let the doctors do their part."
    pc "Right..."
    pc "Tomorrow?"
    psy.name "Yes."
    pc "Okay..."
    hide brooker
    $ walk(loc_hospital_lobby)
    pcm "..."
    pcm "So [mira.name] is alive. That's good..."
    pcm "Better tell [cass.nname] and see tomorrow how [mira.name] is."
    $ mira.dict["rescue_date"] = t.day
    $ add_to_list(mira.list, "hospitalised")
    $ add_to_list(mira.list, "pc_knows_whore")


    $ add_to_list(mira.list, "rescued")
    $ log.markdone("mira_missing_09")
    $ mira.preg_abort()
    jump travel

label quest_mira_missing_cass_conv:
    show cass at right1 with dissolve
    pc "So I spoke to my contact, got help from them and [mira.name] is safe."
    show cass laugh
    cass.name "Really? Really really???"
    pc "Yeah, she is in the hospital now. She is a bit hurt but otherwise okay."
    cass.name "The hospital? I'll go there."
    if mira.dict["rescue_date"] == t.day:
        pc "She needs time to rest and recover. So give it a bit."
        cass.name "But."
        pc "Tomorrow. We can head there tomorrow and see how she is."
        cass.name "Okay. Speak after school and let's go there."
        pc "Okay."
    else:
        pc "Okay. We can go together."
        cass.name "Okay. Meet after school and let's go."
        pc "Okay."
    $ log.markdone("mira_missing_10")
    hide cass with dissolve
    jump travel

label quest_mira_missing_cass_visit:
    show cass at right1 with dissolve
    cass.name "Want to go visit [mira.name]?"
    menu:
        "Sure, lets go":
            $ NullAction()
        "Not right now":

            cass.name "Okay, well we should see her soon."

    $ add_to_list(mira.list, "visited_hospital")
    pc "We can get the bus there and see her."
    $ walk(loc_busstop_school)
    cass.name "Hope she is okay."
    pc "She is alive."
    cass.name "Yeah."
    hide cass with dissolve
    show cass at left1
    $ walk(loc_bus_interior)
    pc "They told me she would be in there for a while. She might be in a bad state."
    cass.name "I know."
    pc "I mean, just don't be upset when you see her."
    cass.name "Upset? I am happy."
    pc "She might not be though. She has been through a lot."
    $ walk(loc_revel)
    cass.name "I know."
    $ walk(loc_hospital_entrance)
    $ walk(loc_hospital_lobby)
    show receptionist at right1 with dissolve
    pc "Hi, we are here to see [mira.name]."
    receptionist.name "Miss [sname]? One moment and I'll call for [nurse.name]."
    pc "Thanks."
    hide receptionist with dissolve
    pc "..."
    show nurse at right1 with dissolve
    nurse.name "Good to see you again Miss [sname]. And who might you be?"
    cass.name "[cass.name]. [mira.name]'s friend."
    nurse.name "Follow me."
    $ walk(loc_hospital_ward)
    $ player.face_neutral()
    nurse.name "Miss [mira.sname]. Your friends are here to see you."
    hide nurse with dissolve
    show mira worried at right1 with dissolve
    cass.name "[mira.name]! I'm so happy to see you!"
    mira.name "[cass.nname]! [name]!"
    pc "Good to see you up and about."
    show cass worried
    mira.name "Yeah... Looks like I will be here for a while."
    cass.name "Is your eye... Okay?"
    mira.name "It's still there. Just a bit beaten up."
    cass.name "..."
    mira.name "I heard about what happened... About what you guys did..."
    mira.name "Thank you."
    cass.name "Ah. Yeah..."
    pc "Made some new friends, a bit of money on the side. No big deal."
    cass.name "Ha. Sure."
    pc "A pain in the ass sometimes though."
    show cass neutral
    cass.name "[name]!"
    mira.name "Haha."
    cass.name "..."
    cass.name "How long are you here for?"
    mira.name "Not sure. But it should be okay afterwards."
    mira.name "They have been asking me a lot of questions about how this all started."
    cass.name "Yeah..."
    tucker.name "Miss [sname]. Can I see you in my office?"
    pc "Err, sure. I'll be right back."
    pc "Good to see things are okay [mira.name]."
    hide mira
    hide cass
    $ walk(loc_hospital_lobby)
    show tucker at right1
    $ walk(loc_hospital_office)
    pc "She seems to be somewhat okay."
    tucker.name "I am having her talk to [psy.name] about her situation. It might do some good."
    pc "What happened to her?"
    tucker.name "That's not for me to tell. But I think you can probably guess yourself."
    pc "Yeah..."
    tucker.name "You did a good job in finding out where she was. You should be proud of yourself."
    pc "Yeah sure."
    tucker.name "I am serious. You saved a friend from a terrible fate. Who knows what would have happened had you not."
    pc "I think we can guess."
    pc "Why did you call me in here anyway?"
    tucker.name "To tell you that once we let [mira.name] out of here, she will need people like you around her to aid in her recovery."
    tucker.name "And to make sure that you didn't reveal anything unnecessary about The Institute during your investigation."
    pc "Don't worry. Your sex doll project is still a secret."
    tucker.name "Good. And if you feel the need, [psy.name] is always available to you."
    pc "What happened to the guy that took her?"
    tucker.name "He won't be anyone's concern any more."
    pc "Ah. Okay..."
    pc "Did you read the report from [psy.name]?"
    tucker.name "I did."
    pc "And?"
    tucker.name "And what?"
    pc "Err... I had to do things to find out what happened."
    tucker.name "That is not my concern. You did what was needed."
    pc "Right..."
    tucker.name "Keep up the good work [fname]."
    pc "Yeah..."
    hide tucker
    $ walk(loc_hospital_lobby)
    pcm "What was that about?"
    show cass at left1
    show mira worried at right1
    $ walk(loc_hospital_ward)
    cass.name "You're back?"
    pc "Yeah. Everything okay here?"
    cass.name "Yeah. The nurse is waiting for you to come back to shoo us away."
    pc "Ah? Already?"
    mira.name "Thanks for coming to see me. It means a lot."
    pc "Of course."
    mira.name "I'll be back to normal in no time."
    show nurse at left4 with dissolve
    nurse.name "Okay, let's get you back to bed."
    cass.name "Bye [mira.name]."
    hide mira
    hide nurse
    $ walk(loc_hospital_lobby)
    show cass at right6 with dissolve
    cass.name "Well, that's good. She seems alright."
    pc "Yeah, though she will still need time. Couldn't have been easy whatever happened to her while she was with that monster."
    cass.name "Thanks for coming with me [name]."
    pc "No problem."
    hide cass with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
