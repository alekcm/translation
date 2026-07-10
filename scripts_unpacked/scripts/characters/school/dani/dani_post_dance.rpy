label dani_postdance_company_conv:
    if player.iswhore:
        pc "So~"
        pc "How did your private audience go?"
        dani.name "Huh?"
        pc "The guy you kept company after the dance. Hope he paid well."
        show dani worried
        dani.name "Ah..."
        dani.name "Let's talk about that another time..."
        pc "Sure. If you say so."
    elif player.isslut:
        pc "So~"
        pc "Did you entertain your new admirer?"
        show dani worried
        dani.name "Ah. You heard about that?"
        pc "No, I just assumed that's what it was."
        dani.name "Let's talk about that another time..."
        pc "Sure. If you say so."
    else:
        pc "Everything okay with you heading off early after the dance?"
        dani.name "Err, I guess..."
        pc "You guess?"
        dani.name "Yeah..."
        dani.name "Mind if we talk about this another time?"
        pc "Sure. Up to you."
    $ remove_from_list(dani.conversation_topics, "dance_went_alone")
    $ add_to_list(dani.conversation_topics, "dance_went_alone_followup")
    return

label dani_postdance_company_conv_chat:
    if player.iswhore:
        pc "So~"
        pc "How did your private audience go?"
        dani.name "Huh?"
        pc "The guy you kept company after the dance. Hope he paid well."
        show dani worried
        dani.name "Ah..."
        dani.name "Let's talk about that another time..."
        pc "Sure. If you say so."
    elif player.isslut:
        pc "So~"
        pc "Did you entertain your new admirer?"
        show dani worried
        dani.name "Ah. You heard about that?"
        pc "No, I just assumed that's what it was."
        dani.name "Let's talk about that another time..."
        pc "Sure. If you say so."
    else:
        pc "Everything okay with you heading off early after the dance?"
        dani.name "Err, I guess..."
        pc "You guess?"
        dani.name "Yeah..."
        dani.name "Mind if we talk about this another time?"
        pc "Sure. Up to you."
    $ remove_from_list(dani.conversation_topics, "dance_went_alone")
    $ add_to_list(dani.conversation_topics, "dance_went_alone_followup")
    jump dani_talk_end

label dani_postdance_company_conv_chat_alone:
    if player.iswhore:
        pc "So~"
        pc "How did your private audience go?"
        dani.name "Huh?"
        pc "The guy you kept company after the dance. Hope he paid well."
        show dani worried
        dani.name "Ah..."
    elif player.isslut:
        pc "So~"
        pc "Did you entertain your new admirer?"
        show dani worried
        dani.name "Ah. You heard about that?"
    else:
        pc "Everything okay with you heading off early after the dance?"
        dani.name "Err, I guess..."
        pc "You guess?"
        dani.name "Yeah..."
    $ remove_from_list(dani.conversation_topics, "dance_went_alone")
    $ add_to_list(dani.conversation_topics, "dance_went_alone_followup")
    jump dani_postdance_company_conv_followup_catcher

label dani_postdance_company_conv_followup:
    show dani school at right1 with dissolve
    dani.name "Hey [name]. Got a bit to chat?"
    pc "Sure. What's up. Is this about..."
    dani.name "Yeah..."
    if dis(dis_school):
        dani.name "Can we go somewhere else?"
        pc "Sure? Quiet I assume?"
        if school_soccer_quest_hangout_prompt:
            pc "I know somewhere quiet."
            $ walk(loc_school_field)
            $ walk(loc_school_locker_old)
            pc "Here we go. No one ever comes in here so can talk freely."
            dani.name "Oh? What is this place?"
            pc "This place had more locker rooms than the one we use. But too much water so they closed these ones down."
            pc "Me and the boy's sometimes use to after playing."
            dani.name "Oooh."
        else:
            pc "Hmm, not many places round here that are too quiet. The locker rooms maybe?"
            dani.name "Sure. I guess so."
            $ walk(loc_school_hallway)
            pause 0.5
            $ walk(loc_school_locker_girls)
    jump dani_postdance_company_conv_followup_catcher

label dani_postdance_company_conv_followup_catcher:
    pc "Hmm, so everything ok?"
    dani.name "Yeah... Well, no..."
    pc "..."
    show dani worried
    dani.name "What would you have done?"
    if player.has_perk([perk_broken, perk_bambi], notif=True):
        pc "..."
        pc "Probably let him do what he wanted."
        pc "Did he pay you?"
        dani.name "Some... Yeah..."
        pc "I suppose then you just need to worry about getting pregnant."
        dani.name "What? We didn't have sex."
        pc "No? Then no problem."
        dani.name "Wait. You thought we had sex?"
        pc "Yeah."
        dani.name "And you were fine with that?"
        pc "Yeah. Why wouldn't I be?"
        dani.name "Err... Isn't that too much?"
        pc "No."
        dani.name "..."
        dani.name "No...?"
        pc "Why would it be?"
        dani.name "Isn't it wrong?"
        pc "Why?"
        dani.name "..."
        dani.name "Because..."
        pc "Do what you need to so you can be happy."
        dani.name "..."
        dani.name "Even prostitution?"
        pc "Of course. Whoring yourself makes better money than other ways. Plus it can be fun."
        dani.name "Fun? Wait... Have you?"
        pc "Of course."
        dani.name "..."
        dani.name "Thanks [name]..."
        hide dani with dissolve
        pcm "Hmmm..."

    elif player.has_perk(perk_whore, notif=True):
        pc "Did he pay you?"
        dani.name "..."
        dani.name "Some... Yeah."
        pc "Then no problem."
        show dani happy
        dani.name "Really?"
        pc "Sure. These perverts will pay for almost anything and we need money. So why not?"
        dani.name "What? As simple as that?"
        pc "Pretty much."
        dani.name "Err... Have you done it before?"
        pc "Obviously. More times than I can count."
        dani.name "Really?"
        dani.name "Doesn't it... Make you feel dirty?"
        pc "Did at first. Not any more."
        show dani worried
        dani.name "..."
        pc "*Sigh*"
        pc "World is shit out there and people are going to fuck us one way or the other."
        pc "Either they bully us because we are poor and can't afford to lose our job or they hit us over the head and rape us in a piss smelling alleyway."
        pc "So better to take control of the situation and let them fuck us on our terms. And let it cost them instead of us."
        show dani neutral
        dani.name "Is it really like that?"
        pc "You speak as if you never had some shit pull you in the bushes at night or something."
        if not rapist.fname in dani.sex_who:
            dani.name "Err. I haven't. No one's did anything like that."
            pc "Then you are one of the rare ones."
            pc "Then think of the bus..."
        else:
            dani.name "..."
        pc "These shit's will take from you. So take from them first."
        dani.name "..."
        pc "Well. It's what I think anyway..."
        dani.name "..."
        dani.name "Thanks [name]..."
        hide dani with dissolve
        pcm "Hmmm..."
        pcm "Maybe I was a bit too cynical..."

    elif player.has_perk([perk_slut, perk_bimbo, perk_exhibitionist], notif=True):
        pc "Who knows. If it seemed like it would be fun then I would have went along with it."
        dani.name "Really?"
        pc "Sure. Why not? Hard to keep yourself happy these days so I just go along with these things."
        dani.name "And what? You don't feel guilty or dirty?"
        pc "Guilty? No idea what there is to feel guilty about."
        dani.name "Isn't it wrong to take money for this sort of thing?"
        pc "Says who?"
        dani.name "Err..."
        dani.name "Dunno. People?"
        pc "Yeah, fuck people. Do what you want or need to do to get by."
        pc "Don't think about what those shit's care about. Look after yourself."
        dani.name "Is it that easy though?"
        pc "Is when you ignore the shits. People will abuse you for every reason they can. So just look out for yourself."
        dani.name "..."
        dani.name "Thanks [name]..."
        hide dani with dissolve
    else:

        pc "Guess it depends on what he wanted."
        dani.name "..."
        dani.name "He asked me to sit on his lap and keep him company."
        $ player.face_happy()
        pc "That's all?"
        show dani neutral
        dani.name "What?"
        $ player.face_neutral()
        pc "I thought you fucked the guy in the bushes or something. Sitting on his lap is nothing."
        pc "Hell, worse getting on the bus and those fuckers don't even pay."
        pc "Those bastards at the end of the dance show also tried to put their finger in me while I am begging a few coins off them."
        pc "Sitting on someone's lap would be a nice break."
        dani.name "Okay ok..."
        pc "He offer you a margarita as well?"
        show dani happy
        dani.name "Very funny..."
        pc "Next time invite me. Could do with somewhere to relax."
        dani.name "Right..."
        dani.name "Thanks [name]..."
        hide dani with dissolve
    $ remove_from_list(dani.conversation_topics, "dance_went_alone_followup")
    $ add_to_list(dani.conversation_topics, "dance_went_alone_had_conversation")
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
