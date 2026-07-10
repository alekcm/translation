label main_quest_04_intro:
    $ main_quest_04.stage = 1
    $ unlocked_police = True
    $ walk(loc_hospital_office)
    show tucker at right1 with dissolve
    $ log.markdone("mq_03_c")
    tucker.name "Good to see you back here [fname]."
    $ player.face_surprised()
    pc "Actually I was just looking for the toilets. This place is a maze."
    $ player.face_normal()
    tucker.name "Have a seat."
    $ player.face_worried()
    pc "That serious?"
    tucker.name "Again with the doom and gloom. No, what I have next for you is easy."
    $ player.face_normal()
    pc "Oh?"
    tucker.name "Go to what is currently acting as the [town] Police station at the Highway checkpoint and introduce yourself to [miller.fullname]."
    pc "And?"
    tucker.name "He should have some paperwork prepared for you. I need you to find out information about someone."
    if not main_quest_01.missionvar1:
        pc "Why is everything with you so anti climactic?"
        tucker.name "*COUGH*"
        tucker.name "What were you expecting? Infiltrate a crime ring and take down the boss?"
        pc "..."
        $ player.face_happy()
        pc "Yes?"
        pc "..."

    $ player.face_neutral()
    pc "Ok, who am I digging into?"
    tucker.name "An old Institute employee. [ant.fullname]."
    pc "Ok... I am guessing he left on bad terms if you are digging into him."
    tucker.name "That is an understatement."
    tucker.name "[ant.name] was one of the researchers involved in the project to make the artificial bodies. Unfortunately, at some point his demeanour completely changed."
    tucker.name "In hindsight, we believe he was diagnosed with some kind of fatal illness. While we are not entirely sure if that's the case, it does explain his actions."
    if quest_homeless_start.active:
        tucker.name "Some time ago, he... Caused some problems."
        pc "Ok... Such as?"
        tucker.name "The body we salvaged to use for you was a woman's body. We had a male counterpart as well."
        if player.int <= 20:
            pc "Ok, but it sounds like you don't have it any more."
            tucker.name "No, [ant.name] had taken it just before you arrived."
        else:
            pc "And not any more since he took it?"
        pc "And I am assuming he \"took\" it took it. As in left his old one behind?"
        tucker.name "Yes."
    else:
        tucker.name "Then a few days before you were admitted here, he... Caused some problems."
        pc "Ok... Such as?"
        tucker.name "The body you are in wasn't the only one. We had a male counterpart as well."
        if player.int <= 20:
            if player.male_origin:
                pc "Ok... So why couldn't I have been given that one?"
                tucker.name "Because we no longer had it at that point. [ant.name] took it."
            else:
                pc "Ok, but it sounds like you don't have it any more."
                tucker.name "No, [ant.name] had taken it just before you arrived."
        else:
            if player.male_origin:
                pc "Ah, and you didn't have one for me. So it means he took it before I arrived."
                tucker.name "Correct."
            else:
                pc "And not any more since he took it?"
        pc "And I am assuming he \"took\" it took it. As in left his old one behind?"
        tucker.name "Yes."
        if player.int >= 40:
            pc "Does him doing this have something to do with why I am still alive? Not to sound ungrateful but The Institute doesn't strike me as a group who would put me in the body out of the kindness of their hearts."
            tucker.name "..."
            tucker.name "Yes, you are right. In his hasty attempt to swap bodies, he damaged a lot of our equipment."
            tucker.name "To put it simply. He broke the fridge and we were forced to drink the milk or it would spoil."
            tucker.name "Hence why you are in this body and not one of our own people."
            pc "Not sure I follow. Couldn't you still have used one of your own?"
            tucker.name "Yes and no. We hadn't managed to do any tests at that point yet. And considering the mess the lab was left in, it was judged too risky."
            tucker.name "We were already accepting that \"the milk would spoil\", but then you arrived."
            pc "Why not try on someone who is dead anyway?"
            tucker.name "Indeed."
    pc "Ok, so [ant.name] ran off with your body, and you want me to track him down?"
    tucker.name "Yes, but it won't be as easy as that. He will no doubt have a new identity so I need you to find out as much about him as possible. Any contacts he would turn to for help."
    $ player.face_confused()
    if quest_homeless_start.active:
        pc "Hold on. He ran away before I even wandered into town. That was ages ago. Won't he be long gone by now?"
    else:
        pc "Hold on. He ran away before I arrived. I was in hospital for half a year. Won't he be long gone by now?"
    tucker.name "Possibly, but I believe not. Have you already been to the security checkpoint?"
    $ player.face_frown()
    if quest_homeless_start.active:
        pc "Err, you know that's how I arrived here. Somehow blundered my way through the checkpoint."
        tucker.name "Yes, but that was under extreme circumstances. Have you been there since?"
    if loc_checkpoint.visited:
        pc "Yes, a depressing place. Looks like a prison camp."
    else:
        pc "No I haven't."
        tucker.name "Well, you will see it on your way to meet [miller.name]. But it is fairly high security with everyone entering and leaving being checked. And a large wall surrounding the city."
    tucker.name "Most cities that are still operational have such security measures. You can't just come and go."
    tucker.name "While it's not terribly hard to leave a city if you have contacts or the know-how, gaining entrance to another one would be quite hard without help from inside the city."
    if quest_homeless_start.active:
        if "pc_preg" in quest_homeless_start.list:
            pc "Unless you waddle in like a fat penguin."
            tucker.name "Yes, apparently security measures don't apply to pregnant women..."
            pc "They probably couldn't believe their eyes. Turns out I am a master of distraction."
            tucker.name "Yes... Well..."
        else:
            pc "Unless you charge in screaming at the top of your lungs."
            tucker.name "Yes, how you managed it is beyond belief. Something else worth looking into."
    else:
        pc "Ok... I am not familiar with how this stuff works."
    tucker.name "Ask [miller.name]. He will explain far better than I can. But for now just know it wouldn't be easy to find somewhere else to settle. And certainly not quickly."
    tucker.name "We are not talking about a master of the criminal underworld here, he is... was, a doctor. So I doubt he would have the kind of connections needed to enter another city."
    tucker.name "Much less the mental fortitude to do so. Outside of these walls is not a pleasant place. A doctor who is used to a mostly pampered lifestyle wouldn't be able to cut it out there."
    pc "Have you checked his mother's basement?"
    tucker.name "Yes we have. The main problem is we have to be discreet."
    tucker.name "If we send security to kick over every rock, he will get desperate and do something stupid. We still need to hide what we were up to here."
    tucker.name "Since we haven't been chasing him down and keeping him on the run, I personally believe he has settled into a mostly routine life."
    tucker.name "While he will be keeping a low profile, he still needs to eat and sleep."
    pc "So will need to earn money. He can't make use of his doctoring abilities with a new identity to get work, so he probably works simple jobs."
    tucker.name "My thoughts as well. So I am hoping that while you are looking for him, he is going about his normal daily life."
    pc "Easier to catch him when he isn't running."
    tucker.name "Mmm."
    tucker.name "[miller.name] has prepared all the paperwork you might need, so dig around and see what you can come up with."
    pc "Ok, I will see what I can find."
    tucker.name "Good luck."
    $ log.assign("Tracking a Curse")
    $ loc_checkpoint_lobby.locked = False
    hide tucker
    $ walk(loc_hospital_lobby)
    with dissolve
    pcm "Okaaay..."
    pcm "Go to the security checkpoint and speak to [miller.name]. He has prepared paperwork for me to help track down [ant.name]."
    pcm "Sounds easy enough."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
