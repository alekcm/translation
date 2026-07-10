label main_quest_01_debrief:
    $ walk(loc_hospital_office)

    show tucker at right1
    if main_quest_01.missionvar1 == True:
        jump main_quest_01_debrief_passed
    else:
        jump main_quest_01_debrief_failed


label main_quest_01_debrief_failed:
    $ main_quest_01_fail = Diary_Class("Reporting my failure.", "Well, it was to be expected. I have no idea what I am doing so all I could do is report that I failed the mission. [tucker.name] didn't seem too concerned though and it was pretty much expected I would fail. Still, doesn't feel good.\nI am supposed to wait now to see if [simon.fullname] slips up.")
    if t.hour in morning:
        tucker.name "Good morning, [name]. How can I help you?"
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [name]. How can I help you?"
    else:
        tucker.name "Good to see you, [name]. How can I help you?"
    pc "Well, I spoke to [simon.name]."
    show tucker smile
    tucker.name "Ah you did? How did it go?"
    pc "Can't say it went too well. He clocked me the moment I entered the pub."
    tucker.name "Well that was mostly expected. For now we will keep an eye on him and see what he does."
    tucker.name "Hopefully he will get in touch with contacts and we can find out who they are. Might even be able to figure out what he is after based on who he's talking to."
    pc "Hmm. So that's good? I don't need to worry because I failed?"
    tucker.name "Failed? Not at all. I have told you plenty of times but this was the plan. Shake him up and have him run to any co-conspirators."
    tucker.name "So for now it's just a waiting game. We will keep an eye on him and see what he gets up to. So you should come back in a few days for an update."
    pc "Ok..."
    pc "What should I do until then?"
    tucker.name "Enjoy your life. Have fun in school. Dance some maybe."
    pc "Uff. Ok. I'll come back in a few days time."
    tucker.name "I look forward to it. Goodbye [fname]."

    hide tucker at right1
    $ main_quest_01.missionvar2 = t.day
    $ main_quest_01.complete()
    $ main_quest_02.activate()
    $ log.markdone("mq_01_c")
    $ log.assign("Tracking down Simon Banks")
    $ walk(loc_hospital_lobby)
    jump travel

label main_quest_01_debrief_passed:

    if t.hour in morning:
        tucker.name "Good morning, [name]. How can I help you?"
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [name]. How can I help you?"
    else:
        tucker.name "Good to see you, [name]. How can I help you?"
    pc "Well, I spoke to [simon.name]."
    show tucker smile
    tucker.name "Ah you did? How did it go?"

    if main_quest_01.vvirgin:
        pc "Well... Let's just say it cost me something I will never get back."
    elif simon.sold:
        pc "Well, I offered him something in exchange and he was happy to go along with it."
    elif main_quest_01.sex:
        if quest_homeless_start.active:
            pc "Well, I put myself to use and got what you wanted."
        else:
            pc "Well. This new body you gave me got put to use to get what you wanted."
    elif main_quest_01.osex:
        pc "Left a pretty bad taste in my mouth... But I got what you wanted."
    elif main_quest_01.hsex:
        pc "Well, offering a helping hand seems to go a long way and managed to get what you asked for."
    elif simon.naughty:
        pc "I helped him let off some steam and then he was a lot more receptive."
    elif simon.naked:

        pc "I showed him something worth giving the info for. He was more than happy to give it up afterwards."
    else:
        if "intimidate_branch" in main_quest_01.list:
            pc "No problem. I just put the screws to him and he spilled pretty quickly."
        elif "waitress_branch" in main_quest_01.list:
            pc "No problem. I just dressed as a barmaid and talked the info out of him."
        else:
            pc "No problem. We played a bit of a drinking game and he lost. So he gave me everything I wanted to know"
    tucker.name "Err... Ok. Well honestly I am shocked. This was just supposed to be an outing to get you used to speaking to random strangers in unusual situations."
    tucker.name "But to return with the info we asked for is quite surprising."
    if main_quest_01.preg and player.preg_knows:
        pc "Well, something inside me tells me it was an experience I won't forget."
    elif simon.vvirgin == True:

        pc "Well, it was certainly an experience that's for sure. One that [simon.name] made sure I will never forget."
    else:

        pc "Well, it was certainly an experience that's for sure."
    tucker.name "I am glad to hear it. Very glad. This is a lot more than we ever expected."
    tucker.name "Sorry. I am at a loss for words. It was a bit of a risk expecting you to take on such a task which you have no training for. But to have you come out of it successfully..."
    tucker.name "Well. It fills me with confidence at how you will progress going forward."
    pc "Thanks I suppose."
    tucker.name "You are welcome. So, tell me. Why was [simon.name] snooping around The Institute?"
    pc "Well, he wasn't."
    tucker.name "He wasn't? Are you sure about that?"
    pc "Yes. He is investigating another guy who drinks in the pub called [bob.name]. It seems his wife wants dirt on him so she can use it as an excuse to kick him out and claim his stuff."
    tucker.name "..."
    tucker.name "Wow... Okay then. So nothing that we need to be concerned about."
    pc "Well, other than [bob.name]."
    tucker.name "That's nothing for us to worry about. It's a personal problem between [bob.name] and his wife. And [bob.name] doesn't hold a position where he has knowledge that could harm The Institute."
    tucker.name "So we will just leave it alone."
    pc "Hmm. That's disappointing."
    tucker.name "It is?"
    pc "Yeah. I went to all that trouble for nothing."
    tucker.name "No. Not nothing. You came back with info that lets us make an informed decision on how to move forward from here. Just because that decision is to do nothing doesn't make it any less important."
    tucker.name "It allows us to allocate resources in the right areas and no longer waste time on [simon.name]. Frankly the fact that what [simon.name] was doing was so mundane is excellent news to me."
    tucker.name "It also allows us to put you to better use."
    pc "So you already have something else for me to do?"
    tucker.name "As long as The Institute exists, there will never be a lack of things we will need from someone such as yourself."
    tucker.name "But one step at a time. For now I need you to come back tomorrow and speak to a couple of people before we can move forward."
    pc "Err. Should I be worried?"
    if quest_homeless_start.active:
        tucker.name "Quite the opposite. This is for your benefit. You will speak to [nik.name] about some interesting developments we have been making here."
    else:
        tucker.name "Quite the opposite. This is for your benefit. You will speak to [nik.name] about your body. He has some interesting developments to share with you."
    if not nik.has_met:
        pc "Err, no idea who that is."
        tucker.name "Well, you will meet him tomorrow them."
    tucker.name "And [psy.name]. She's a psychologist that will be looking out for your mental health. You can discuss with her anything relating to your missions as well as anything going on in your personal life. I hope you will make use of her."
    pc "Ugh. A psychologist?"
    tucker.name "That's right. Speak to her tomorrow for an initial chat. After that it will be up to you if you continue to see her."
    if nik.has_met:
        pc "Hmm, I suppose. And [nik.name]?"
        tucker.name "You have already met him. He was the one who woke you up. He is the head researcher on the Body project. But I will let him tell you what he has to say. I won't spoil the surprise."
    pc "Ok... Well, I'll come back tomorrow then."
    tucker.name "I look forward to it. Goodbye [fname]."

    hide tucker at right1
    $ main_quest_01.missionvar2 = t.day
    $ log.markdone("mq_01_c")
    $ log.assign("Cosmetic what...?")
    $ diary_main_quest_01_pass_func()
    $ main_quest_01.complete()
    $ main_quest_02.activate()
    $ walk(loc_hospital_lobby)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
