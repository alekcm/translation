label main_quest_02_briefing:

    $ cosmetic_surgery_tutorial = True
    $ main_quest_02.stage = 1

    $ walk(loc_hospital_office, trans=False)
    show tucker at right1 with dissolve
    if t.hour in morning:
        tucker.name "Good morning, [name]. I am glad you are here."
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [name]. I am glad you are here."
    else:
        tucker.name "Good to see you, [name]. I am glad you are here."
    pc "Well, you asked me to come."
    tucker.name "I did. We finally have something for you to do. We have been keeping an eye on [simon.fullname] and we think we have a way to find out what he is up to."
    pc "Ah, that's good."
    tucker.name "Indeed. As we expected, finding out that The Institute is looking into him has shaken him up a bit. In response he has contacted a professional contact of his, [nadianame]."
    tucker.name "He seems to think he might be in danger. So he wants to hand over a copy of all of his documents and papers to her in case he suddenly goes missing."
    pc "So she can release the incriminating evidence?"
    tucker.name "That's the conclusion we came to."
    tucker.name "We need you to pretend to be her, meet with [simon.name] and take possession of the package."
    pc "What? I see so many problems with that plan I don't even know where to start. Main ones being that I look nothing like the woman in the picture and he knows who I am already."
    show tucker smile
    tucker.name "And that is my cue to call [nik.name] here to tell you something that is frankly quite amazing."
    show nikolas at right3 with dissolve
    if t.hour in morning:
        tucker.name "Good morning [nik.name]."
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [nik.name]."
    else:
        tucker.name "Good to see you [nik.name]."

    nik.name "Ah [tucker.name]. Good to see you too. And Miss [sname], what a wonderful sight. I am so happy to see you up and about."
    nik.name "My turn to do some explaining?"
    tucker.name "If you would, please."
    nik.name "So, a question for you Miss [sname]. Did you happen to notice that your hair colour, skin colour and even eyes are the same as they were before you died?"
    pc "Errrm... I can't say I even thought about it."
    nik.name "No, I imagine not. Well, it wasn't a coincidence that it turned out that way. We felt you might adjust better if you looked closer to how you used to look."
    pc "Ok, how does that help us now?"
    nik.name "It helps us because we can just change it without any issue."
    nik.name "I won't bother with the science behind it, but put simply your body has no natural colours being that it was grown in a lab. It didn't develop any way to know what pigments to produce."
    nik.name "So we instead \"told\" your body what to produce. And we can do it again."
    if player.int >= 20:
        pc "So you mean to say you can give me dark skin and hair like the woman in the photo."
        nik.name "That's right!"
    else:
        pc "And that means?"
        nik.name "Someone hasn't been putting her brain to work since she left here. It means we can change your skin colour"
    nik.name "So we make a few adjustments to make you look like her. And it shouldn't be an issue to pretend you are her."
    pc "Ok, so that solves the first two issues. There are still plenty of other problems. They know each other and I can't pretend to..."
    tucker.name "They don't know each other. They are professional contacts that have never actually met. Through shared connections they often pass work each other's way but have never really spoken and have never met in person."
    pc "Ok... But they must know some stuff about each other."
    tucker.name "That's where the rest of your training begins. Get the package however you feel you can. The more contact you have with [simon.name] the more chances of things going wrong."
    pc "But what about the real [nadia]?"
    tucker.name "We have already given her a dead drop with useless \"evidence\" in the package. As far as she is concerned the exchange has already been completed and contact has been cut."
    pc "So what you are saying is I am screwed?"
    tucker.name "Not at all. If I didn't have confidence in you I wouldn't assign you these tasks."
    pc "..."
    pc "When is the meeting?"
    tucker.name "That's up to you. As you know, [simon.name] spends most of his evenings in the pub. If you put a chalk marking on the door of the pub it will signal [simon.name] that you are ready for a meeting."
    tucker.name "From there the meeting place isn't far from the pub. So after you leave the chalk mark, head there and wait for him to show up. Take possession of the package and move on."
    tucker.name "Should be simple enough."
    pc "Yeah, you say that while nice and comfortable in the office."
    tucker.name "Of course I do. It's why we need skilled people like you in the field. So people like me can stay comfortable."
    tucker.name "But first of all, tell me when you are willing to undergo the change."
    pc "Will I be able to change it back?"
    nik.name "Of course you can. Get this mission done and the clinic will be open to you to do as you wish."
    pc "Hmmmm."

    menu:
        "Change my appearance":
            jump main_quest_02_transform
        "I'll come back another time":

            tucker.name "Ok, well when you are ready come and see me."
            hide tucker
            hide nikolas
            $ walk(loc_hospital_lobby)
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
