label main_quest_recap:
    if main_quest_01.active == 1:
        jump main_quest_01_recap
    elif main_quest_02.active == 1:
        jump main_quest_02_recap
    elif main_quest_03.active == 1:
        jump main_quest_03_recap
    elif main_quest_04.active == 1:
        jump main_quest_04_recap
    elif main_quest_05.active == 1:
        jump main_quest_05_recap
    else:
        jump main_quest_endofcontent




label main_quest_none_recap:
    tucker.name "This should never trigger and is just a failsafe. Report it as a bug."
    jump tucker_generic_cont

label main_quest_01_recap:
    tucker.name "Go to the pub in the evening and speak to Simon Banks. Find out why he is trying to squeeze our staff for info."
    tucker.name "Come and see me after you have spoken to him and tell me how it went. Remember, the goal is just to give you practice so don't worry about not finding out what his aims are."
    jump tucker_generic_cont


label main_quest_02_recap:
    if main_quest_02.stage == 2:
        tucker.name "In the evening, go to the pub you met [simon.name] in before and leave a white chalk mark on the door signalling you are ready to meet."
        tucker.name "Then head to the highway and collect the package off him. I'll leave the methods up to you."
        jump tucker_generic_cont
    elif main_quest_02.stage == 1:
        tucker.name "First you need you to meet with [nik.name] and have your appearance altered before your meeting with [simon.fullname]."
        tucker.name "We need you need to pretend to be a woman named [nadianame] to be able to receive the package we want off of [simon.name]."
        tucker.name "Shall we go pay a visit to [nik.name] now?"
        menu:
            "Yes, I am ready for the mission":
                jump main_quest_02_transform
            "No, I will come back later":
                tucker.name "Ok, I will be here when you need me."
                jump tucker_generic_cont
    elif main_quest_02.stage == 0:
        tucker.name "We are still monitoring the reporter and waiting for him to make a move. I will keep you updated if anything changes"
        jump tucker_generic_cont
    elif main_quest_01.missionvar1 == True:
        "The last mission was complete so come back tomorrow and I will have some info for you"
        jump tucker_generic_cont
    else:

        jump main_quest_none_recap

label main_quest_03_recap:
    tucker.name "Go home and think over what we spoke about. Come and speak to me after if you still want to work with us."
    jump tucker_generic_cont

label main_quest_04_recap:
    tucker.name "Go to the highway checkpoint and speak with [miller.name]. He will have more details when you get there."
    $ unlocked_police = True
    jump tucker_generic_cont

label main_quest_05_recap:
    if log.interactive("mq_04_e"):
        tucker.name "Give us some time to recon [haven] and come up with a plan on how to get you inside. Come back in a few days."
        jump tucker_generic_cont

    if log.interactive("mq_05_a"):
        if player.pregnancy > 1 or player.preg_knows:
            tucker.name "We are preparing to send you into [haven] to look for [ant.name] but we can't do that while you are pregnant."
            jump tucker_generic_cont
        elif player.fitness < 20 or player.pregnancy > 0:
            tucker.name "We need you to get in better shape before we can send you into [haven]. So work out a bit and lose that belly then come and speak to me to start things off."
            jump tucker_generic_cont
        else:
            tucker.name "We are waiting on you to give the go ahead before we prepare you to go into [haven]. Are you ready now?"
            menu:
                "Yes, let's get started":
                    $ log.markdone("mq_05_a")
                    jump main_quest_05_preperation
                "Not yet.":
                    tucker.name "Ok, well you know where I am."
                    jump tucker_generic_cont




label main_quest_endofcontent:
    tucker.name "You have reached the end of content for The Institute missions for now."
    jump tucker_generic_cont
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
