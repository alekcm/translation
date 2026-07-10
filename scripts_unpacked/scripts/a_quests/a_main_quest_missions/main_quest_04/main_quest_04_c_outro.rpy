label main_quest_04_outro:
    $ walk(loc_hospital_office, trans=False)
    show tucker at right1 with dissolve
    $ player.face_neutral()
    $ log.markdone("mq_04_d")
    tucker.name "Good to see you [fname]. Judging by the phone call I got from [miller.name], it seems you made some progress tracking down [ant.fullname]."
    pc "Maybe. Might not lead to anything but it is worth checking out."
    tucker.name "That's more than we started with, so it's good news."
    pc "Here are the detailed documents on a man named [alex.fname] [alex.sname]."
    tucker.name "And he is?"
    pc "He is somewhat connected to [ant.name]. His wife's sister's first husband."
    tucker.name "Ok, what makes someone so distantly connected to [ant.name] worth looking into."
    pc "Because he is capable of hiding [ant.name]. He is well known by security to house the destitute and desperate."
    pc "It seems he is some kind of leader that controls an old abandoned building in [town] that they call [haven]. While Security can't pin any criminal activity on him, he seems to have quite a bit of power and influence."
    pc "According to those documents, the lower floors in that building is where many urchins, whores and other strays live. Some kind of homeless shelter."
    pc "Since he seems to lord over these people, security suspects he has some kind of hold over them. Drugs, protection money, they don't know. But it's clear he is some kind of leader there."
    pc "They even go so far as to refer to him as \"[alex.nname]\"."
    tucker.name "Hmmm, sounds like a perfect place for [ant.name] to be hiding out."
    pc "It does, that's why I chose to focus on this."
    show tucker smile
    tucker.name "Great work [fname]. Really great work. I honestly didn't expect a lot with this expedition and was using it mostly to introduce you to some of the people we work with."

    if main_quest_01.missionvar1 == True:
        tucker.name "First I sent you to [simon.fullname] and you returned with everything we wanted to know, and now you return from the security offices with a very solid lead. Very well done."
        $ player.face_shy()
        if main_quest_01.rape:
            pcm "And no one raped me in a smelly alleyway in the process, so that's a step up."
        elif main_quest_01.sold:
            pcm "And I didn't sell myself to get the lead. Making progress."
        elif main_quest_01.vsex > 0:
            pcm "And didn't have to fuck anyone to get this lead, so it's an improvement."
        elif main_quest_01.osex > 0:
            pcm "And didn't have to suck anyone's cock this time, so it's an improvement."
        elif main_quest_01.hsex > 0:
            pcm "And no one wanted me to wank them off. Looks like I am getting better."
        else:
            pcm "And I managed it without taking my clothes off. We are making progress."
        $ player.face_normal()
    else:
        tucker.name "But you not only managed to squeeze a lead out of this, you managed to get something quite solid and promising."

    pc "So, how should we proceed?"
    tucker.name "Well, as you already know, it will probably be you checking things out. But how, I will have to think about."
    tucker.name "Give me some time to look over these documents in detail and find out anything our own people might know. I will come up with something for you."
    pc "Ok, then I'll wait to hear from you."
    show tucker frown
    tucker.name "On another topic, seems you caused some waves at the station."
    $ player.face_shy()
    pc "..."
    pc "I might have been a bit mean to [miller.name]."
    $ player.face_neutral()
    tucker.name "Might I ask why?"
    pc "Mostly to see how they reacted. But he treated me like a little girl. I thought I had better correct that attitude."
    tucker.name "The call I got from him was very interesting."
    if main_quest_04.missionvar2:
        tucker.name "But not as interesting as the one I got from [cam.name]."
        pc "Ah..."
        $ player.face_shy()
        pc "Yes, I was considerably more mean to him..."
        tucker.name "\"Little monster bitch\" I believe he is now calling you."
        $ player.face_angry()
        pc "Him calling me little is what made me be mean with him."
        $ player.face_neutral()
        tucker.name "Well don't worry too much. After their initial shock, it seems that they understand that you are not a little girl I sent, but my agent."

    pc "You don't sound too upset with how I handled things."
    tucker.name "I'm not. You need to use all your skills to get things done. Sometimes that is honey, other times vinegar. I will trust your judgement on what best to use."
    pc "They asked me to help out with some of their internal issues. They told me it was your suggestion."
    tucker.name "That's right. As you no doubt discovered, they are not exactly an elite force over there. They have their fair share of internal problems that you are perfectly suited to deal with."
    tucker.name "The smoother things are running over there, the better things are for everyone. So give them a helping hand."
    pc "Ok, [cam.name] asked me to pay him a visit at the train station. Think I'll go see what he wants."
    tucker.name "Great, I look forward to more phone calls."
    hide tucker
    $ walk(loc_hospital_lobby)
    pc "..."
    pcm "Well that was something. I thought he might be upset that I was mean to them but he didn't care in the slightest..."
    pcm "Anyway, I should wait a few days until [tucker.name] manages to get a plan together on how to deal with [haven]."
    pcm "In the meantime I can probably help out [miller.name] at the security checkpoint or [cam.name] at the train station."
    "NOTE*** THESE QUESTS ARE NOT IN YET SO YOU CANNOT VISIT THE TRAIN OR POLICE STATION."
    $ main_quest_05.activate()
    $ main_quest_04.complete()

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
