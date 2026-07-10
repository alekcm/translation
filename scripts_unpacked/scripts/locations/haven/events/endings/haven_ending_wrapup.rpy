label haven_ending_wrapup:

    $ time_sleep(300)
    if player.mood < 30:
        $ player.set_mood(30)
    show emile suitvest at right1
    $ player.eye = 3
    pause 0.5
    show screen blackout(50) with dissolve
    emile.name "...sleep but you should get up."
    emile.name "Wake up!"
    $ player.eye = 2

    pc "[emile.name]?"
    emile.name "Yup, come on. Wake up."
    hide screen blackout with dissolve
    $ player.face_normal()
    pc "Ugh. What's going on?"
    emile.name "[nik.name] is preparing to give you a check up but I thought I would come and see how you're doing while he gets ready."
    pc "Doing ok..."
    emile.name "You sure?"
    pc "Need a shower."
    emile.name "Ok, well plenty of time for that. Hope [haven] wasn't too messy."
    if main_quest_05.rape > 0:
        $ player.face_meek()
        pc "Pretty sure messy was expected when I was sent in there."
    else:
        pc "Mostly ok."
    $ player.face_normal()
    emile.name "Hmmm. Well if you want to talk, I am here. [tucker.name] has also insisted you speak to [psy.name] after you get checked out."
    pc "Ok. I just want to get back to normal."
    emile.name "Well won't be long."
    nik.name "Ok, we are mostly ready. [emile.name], if you would give us some privacy."
    emile.name "Sure. See you in a bit [name]."
    pc "Yeah."
    hide emile with dissolve
    show nikolas at right3
    show nurse at right1
    with dissolve
    nik.name "Okay Miss [sname]. Let's see what we are dealing with here."
    nik.name "First, need to get you cleaned up and remove those tattoos. In the meantime we will give you a quick check up and make sure everything is ok."
    if main_quest_05.rape > 0:
        pc "Okay would be about the best I could expect all things considered."
    else:
        pc "Should be fine. I didn't really have much issue in there."
    nurse.name "Well, let's get you cleaned up and see."
    pc "Sure."
    show screen blackout(100) with dissolve
    $ t.hour = 2
    $ player.shower()
    $ acc.makeup_on = False
    $ tattoo.chest = 0
    $ tattoo.ass = 0
    $ pc_strip()
    $ acc_strip()
    $ player.eye_liner = 1
    $ c.outfit = 1
    hide nikolas
    hide nurse
    pause 0.5

label haven_ending_wrapup_beaten_catcher:

    if player.mood < 30:
        $ player.set_mood(30)
    hide screen blackout with dissolve
    show nurse at right1 with dissolve
    nurse.name "Ok, everything is looking good. No scarring with the tattoo removal. The piercings were also fine..."
    nurse.name "The hair we will let you deal with and style how you wish..."
    nurse.name "I also have your test and blood results back. Let's see here..."
    if main_quest_05.rape >= 10:
        $ player.face_worried()
        nurse.name "Oh dear..."
        nurse.name "I..."
        nurse.name "Sorry. It must have been a nightmare in there..."
    elif main_quest_05.rape > 1:
        $ player.face_worried()
        nurse.name "Oh dear. Looks like this mission was..."
        nurse.name "No, never mind."
    elif "jumped_window" in main_quest_05.list:
        nurse.name "Other than injuries from the fall, everything seems fine."
    else:
        nurse.name "Other than some bumps and scrapes, no physical damage which is good."
    if player.preg_test():
        $ player.face_shock()
        nurse.name "Looking at the bloodwork, it looks like you are expecting. Though considering the circumstances I am not sure if I should congratulate you."
        if player.has_perk(perk_wanted_preg):
            if player.rapebaby:
                pc "You should. I don't care if it was forced in me. It is still a blessing."
            elif player.soldbaby:
                pc "You should. I don't care if someone paid to put it there. It is still a blessing."
            else:
                pc "You should. It is still a blessing regardless of the situation."
            nurse.name "Err, ok. Congratulations."
        else:
            pc "..."
    $ player.face_normal()
    $ player.mouth = 8

    nurse.name "[nik.name] will prepare things so you can adjust your appearance back to how you want it. In the meantime I think it is a good idea if you have a chat with [psy.name]."
    pc "Ok, now?"
    nurse.name "Yes, she is waiting for you. You can head there now."
    pc "Ok..."
    hide nurse with dissolve
    pc "*Sigh*"
    pc "Hup."
    pause 0.5
    $ walk(loc_hospital_psy)
    $ player.face_normal()
    $ player.mouth = 8
    pause 0.5
    pc "Err, [psy.name]?"
    psy.name "[fname]. I'll be with you in a second, come in."
    pc "Ok..."
    show brooker at right1 with dissolve
    psy.name "I have been reading over what I have although the picture isn't entirely clear."
    psy.name "We felt it was a good idea if you and I had a talk before you go and debrief [tucker.name]."
    pc "Ok. Why?"
    psy.name "Because we understand that [haven] might not have been a very pleasant place and this is a better environment to discuss such things instead of with [tucker.name]."
    psy.name "Also, anything you say in here will only be heard by me and seen by [tucker.name] so he can get the full picture. No one else will know about what you say in here."
    pc "You are talking about [emile.name]?"
    psy.name "Yes, and anyone else you might have to work with in future."
    pc "..."
    psy.name "So is there anything you would like to talk about?"
    if main_quest_05.rape >= 10:
        pc "*Sigh*"
        pc "..."
        pc "I knew going in there would be trouble. But I thought I was prepared for it."
        pc "But I don't think I was..."
        psy.name "Did something happen while you were in there?"
        pc "Something? Many somethings..."
        pc "Seemed like I couldn't turn a corner without someone looking to abuse me."
    elif main_quest_05.rape == 1:
        pc "*Sigh*"
        pc "..."
        pc "I knew going in there would be trouble."
        pc "Suppose it was to be expected that someone would force themselves on me."
    elif main_quest_05.rape > 1:
        pc "*Sigh*"
        pc "..."
        pc "I knew going in there would be trouble. But I thought I was prepared for it."
        pc "But I don't think I was..."
        psy.name "Did something happen while you were in there?"
        pc "Something? Many somethings..."
    else:
        pc "*Sigh*"
        pc "..."
        pc "I knew going in there would be trouble."
        pc "But either I was lucky or just had the wrong idea. But I managed to get through it all mostly unscathed."
    $ temp_var_1 = 0
    if havenvent.vsex > 0:
        $ temp_var_1 += 1
        pc "Was gangraped while I was looking for someone's stash to trade with in a small vent space. Someone spotted idiot me with my arse hanging out and him and his friends spent some time raping me over and over..."
    if havenblackmail.vsex > 0:
        $ temp_var_1 += 1
        pc "Was blackmailed into fucking some guy who caught me looking through peoples belongings to see if there was anything I could use for the mission..."
    if havenpsleeper.vsex > 0 or havenpsleepergang.vsex > 0 or havenpsleeperforce.vsex > 0:
        $ temp_var_1 += 1
        pc "Couldn't even sleep in that place without someone wanting to join and fuck me..."
    if havenvik.vsex > 0 and temp_var_1 > 0:
        $ temp_var_1 += 1
        pc "After that happening, I was feeling like complete shit so ended up fucking the booze dealer for something to drink since my body was the only way I could pay..."
    elif havenvik.vsex > 0:
        pc "Felt like utter shit in that place so turned to booze to help me get through it. But in a place like that with no money, there is only one way someone like me could pay for it..."
    if havenpeeper.vsex > 0:
        $ temp_var_1 += 1
        pc "Oh, fucked some pervert who made a hole in the showers to spy on the girls. I was using it to eavesdrop on conversations but he would come now and then and grope me."
        pc "Which eventually lead to sex..."
    if havenman.vsex and temp_var_1 > 0:
        pc "Of course there was just the other random people as well who..."
    if temp_var_1 > 0:
        pc "Well..."
        pc "You get the idea."
        pc "..."
    pc "But I suppose you don't go into a place like [haven] expecting it to be all warm and friendly."
    pc "..."
    psy.name "Do you want to talk about how you managed to complete the mission?"
    if "pregnant_exit" in main_quest_05.list:
        jump haven_ending_wrapup_pregnant
    elif "burnt_building" in main_quest_05.list:
        jump haven_ending_wrapup_burnt_building
    elif "set_fire" in main_quest_05.list:
        jump haven_ending_wrapup_set_fire
    elif "flooded" in main_quest_05.list:
        jump haven_ending_wrapup_flooded
    elif "gate_pry" in main_quest_05.list:
        jump haven_ending_wrapup_pry
    elif havengateguard.vsex:
        jump haven_ending_wrapup_guard_vsex
    elif "gangbanged" in main_quest_05.list:
        jump haven_ending_wrapup_gangbanged
    elif "got_intel" in main_quest_05.list:
        jump haven_ending_wrapup_got_intel
    else:
        "This is an error. If you completed haven in a legit way and you are seeing this, please report it as a bug."
        "This message is only here to catch endings where I use console commands and did not play the mission properly."
        "I will now trigger the conclusion of the psychology session."
        jump haven_ending_wrapup_conclusion

label haven_ending_wrapup_pregnant:
    pc "Ugh..."
    pc "I noticed I was getting bigger the more time I spent in there."
    psy.name "Bigger?"
    pc "Bigger, fatter... Growing a giant belly..."
    pc "Up the fluff, bun in the oven, eating for..."
    psy.name "I get it."
    pc "That place is bad enough as it is. I didn't want to be staying there any longer in such a state."
    pc "So I decided to push my luck and put on a sob story to convince the guard to let me speak to [alex.fname] [alex.sname]..."
    psy.name "And it worked?"
    pc "I mean, I guess..."
    psy.name "But?"
    if "pregnant_exit_nice_guard" in main_quest_05.list:
        pc "I asked the guard if he could let me up. He seemed nice enough and I knew I could convince him."
        pc "But he wasn't going to risk his neck for some random girl in that shithole, so he offered to bring me up as a whore."
        psy.name "Oh?"
        pc "Problem was. It wasn't just him. I was treated like a cheap whore for the rest of the night..."
    else:
        pc "I asked the guard if he could let me up. He was a complete cunt and didn't care what I had to say."
        pc "But was more than happy to take advantage of a desperate girl with a bay in her belly..."
        pc "Demanded I entertain him and his friends first. I didn't really have much choice but to agree."
        pc "Was pretty much used like a cheap whore for most of the night..."
    pc "..."
    pc "Eventually I was left alone for long enough to sneak out and into [alex.fname] [alex.sname]'s office."
    pc "Lucky it was dark in his room and he couldn't see what a mess I was. Could hardly stand up..."
    pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
    jump haven_ending_wrapup_left

label haven_ending_wrapup_burnt_building:
    pc "Not sure..."
    psy.name "I heard there was a fire. Did that have something to do with you?"
    pc "..."
    pc "I..."
    pc "I wanted to just cause a commotion..."
    pc "I didn't expect the fire to go on for so long that it would take hold of the building."
    pc "I just wanted to get the guards to come running so I could sneak past the security gate they had..."
    pc "..."
    pc "I didn't intend to hurt anyone."
    pc "How..."
    pc "How were things after I left?"
    psy.name "We are not sure. The fire was somewhat dealt with so the building is still standing. Since security was watching the building, they helped out and took some of the more heavily injured here for medical treatment."
    psy.name "But it is expected there might be people who never managed to make it here."
    pc "You mean dead?"
    psy.name "Probably. Hard to tell without taking an active role in the recovery and repair."
    pc "..."
    pc "It was not at all how I planned for things to go."
    if main_quest_05.rape >= 10:
        pc "Though hard to feel sorry for the people living in a place where I was constantly raped."
    if "intel_done" in main_quest_05.list:
        pc "I could have just left. I had overheard people talking enough to already paint a picture of what happened to [ant.name] but for some reason I decided to stay anyway and try to sneak to [alex.fname] [alex.sname]..."
        pc "I don't know why I did that..."
    jump haven_ending_wrapup_conclusion

label haven_ending_wrapup_set_fire:
    pc "Well, I needed to cause a commotion in the hopes of having the guards running to deal with it. Then I could slip in behind them and up to the top floor."
    pc "I had come across a lighter and some accelerant, so thought a fire might do the trick."
    if "caught_settingfire" in main_quest_05.list:
        pc "But I ended up getting spotted while trying to set the fire..."
        jump haven_ending_wrapup_beaten
    else:
        pc "As planned, the guards came running and I managed to get upstairs."
        jump haven_ending_wrapup_upstairs

label haven_ending_wrapup_flooded:
    pc "Well, I needed to cause a commotion in the hopes of having the guards running to deal with it. Then I could slip in behind them and up to the top floor."
    pc "I had come across a crowbar while searching around and thought that if I broke one of the water pipes in the showers, it would do the trick."
    if "caught_destroying" in main_quest_05.list:
        pc "But I ended up getting spotted after I managed to break one of the pipes..."
        jump haven_ending_wrapup_beaten
    else:
        pc "As planned, the guards came running. But I didn't have time to grab my clothes on the way out of the room so ended up having to rush upstairs totally naked."
        jump haven_ending_wrapup_upstairs

label haven_ending_wrapup_pry:
    pc "I had been having chats now and then with the guard keeping an eye on the gate and at some point I gave him a lighter I had come across. So he started taking smoke breaks now and then."
    pc "I had also found a crowbar so decided to use that to pry the gate open while he was gone. I eventually managed to pry it out of it's lock and sneak upstairs."
    jump haven_ending_wrapup_upstairs

label haven_ending_wrapup_gangbanged:
    pc "I decided it would be a good idea to chat with the guard at the gate. He was talkative and friendly enough so I had hoped to maybe sweet talk him into letting me past or something."
    pc "At some point he had offered me to \"warm his bed\" for him..."
    pc "I agreed..."
    pc "Problem was. It wasn't just him. I was treated like a cheap whore for the rest of the night..."
    pc "..."
    pc "Eventually I was left alone for long enough to sneak out and into [alex.fname] [alex.sname]'s office."
    pc "Lucky it was dark in his room and he couldn't see what a mess I was. Could hardly stand up..."
    pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
    jump haven_ending_wrapup_left

label haven_ending_wrapup_guard_sex:
    pc "I decided it would be a good idea to chat with the guard at the gate. He was talkative and friendly enough so I had hoped to maybe sweet talk him into letting me past or something."
    pc "At some point he had offered me to \"warm his bed\" for him..."
    pc "I agreed..."
    pc "Problem was. It seems his friends wanted in on the fun as well..."
    pc "..."
    pc "Eventually I was left alone for long enough to sneak out and into [alex.fname] [alex.sname]'s office."
    pc "Lucky it was dark in his room and he couldn't see what a mess I was."
    pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
    jump haven_ending_wrapup_left

label haven_ending_wrapup_guard_vsex:
    pc "I decided it would be a good idea to chat with the guard at the gate. He was talkative and friendly enough so I had hoped to maybe sweet talk him into letting me past or something."
    pc "At some point after we had been chatting for a while, he kind of made a move on me. Offered me to stay with him upstairs."
    pc "He seemed nice enough and I didn't really look forward to staying in [haven] any longer. So I accepted his offer."
    pc "He was... Nice to me..."
    if "gangbanged" in main_quest_05.list:
        pc "But he had to go back to his post and left..."
        pc "This... Left me at the mercy of all the others that were staying there."
        if player.isslut:
            pc "So to kill time until night time I... Entertained them, lets say."
        else:
            pc "I needed to wait until night time so I had to keep them company for a while."
    pc "But I couldn't stay there all night so eventually I sneaked out and into [alex.fname] [alex.sname]'s office."
    if "beaten" in main_quest_05.list:
        pc "But I guess he didn't take too kindly to that."
        jump haven_ending_wrapup_beaten



    pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
    jump haven_ending_wrapup_left

label haven_ending_wrapup_upstairs:
    psy.name "How did it go up there?"
    if "caught_upstairs" in main_quest_05.list:
        pc "Not good. I didn't know the layout too well and ended up getting spotted by one of the guards."
        jump haven_ending_wrapup_beaten
    elif "alex_spoketo" in main_quest_05.list:
        pc "I decided to take the direct approach and speak to [alex.fname] [alex.sname] right away to try and find out what he knew."
        if "beaten" in main_quest_05.list:
            pc "But I guess he didn't take too kindly to that."
            jump haven_ending_wrapup_beaten
        else:
            pc "We had a talk. It seems at some point he realised I was neither a threat or some [haven] rat, and since he isn't too happy with [ant.name], he was okay telling me what he knew."
            pc "No point letting trouble come to you over someone you hate, So better direct it at [ant.name]."
            jump haven_ending_wrapup_left

    elif "gangbanged" in main_quest_05.list:
        pc "..."
        pc "I ended up bumbling my way into the guard room."
        pc "There wasn't a lot I could do..."
        pc "..."
        pc "I pretended to be a whore who was sent to make them happy."
        pc "I think you can imagine the rest."
        jump haven_ending_wrapup_sneaked
    elif "beaten" in main_quest_05.list:
        pc "I... ended up getting myself caught..."
        jump haven_ending_wrapup_beaten
    else:
        pc "I managed to hole up until night. I had hoped that I could sneak into [alex.fname] [alex.sname]'s room while he was asleep."
        pc "Although I was a wreck from the waiting, it seems [alex.fname] [alex.sname] was spooked by my arrival. I guess he didn't expect someone to just be able to come up to him in his sleep."
        pc "Lucky it was dark in his room and he couldn't see what a mess I was."
        if "flooded" in main_quest_05.list:
            pc "Especially considering I was naked. I don't think he would have been so scared of me if he realised I was just a short, naked girl who was ready to pass out on her feet."
        pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
        jump haven_ending_wrapup_left

label haven_ending_wrapup_sneaked:

    pc "Lucky it was dark in his room and he couldn't see what a mess I was."
    if "flooded" in main_quest_05.list:
        pc "Especially considering I was naked. I don't think he would have been so scared of me if he realised I was just a short, naked girl who was ready to pass out on her feet."
    pc "After he realised I didn't mean to kill him, he seemed okay to tell me what I wanted to know to get rid of me. He doesn't have any love for [ant.name] so saw no point in protecting him."
    jump haven_ending_wrapup_left


label haven_ending_wrapup_left:
    if "flooded" in main_quest_05.list:
        pc "From there I just left. The gate guard was a bit shocked to see some random naked girl coming down but he opened the gate without much commented regardless."
        pc "Had to head back to the showers to get my clothes. It seemed they had fixed the damage I caused as everything seemed back to normal."
        pc "After leaving the building I couldn't find anyone from Security. So instead of hanging around the highway area like a whore, I came here."
    else:
        pc "From there, I just walked out the building. Couldn't find anyone from Security so instead of hanging around the highway area like a whore, I came here."
    jump haven_ending_wrapup_conclusion

label haven_ending_wrapup_beaten:
    pc "I can only guess I was hit over the head or something. Not entirely sure but I woke up in [alex.fname] [alex.sname]'s office with a splitting headache."
    pc "He wasn't too pleased that someone had been causing trouble in his building, and even less pleased it was because of [ant.name]."
    pc "I am not entirely sure what was going to happen, but they wanted to take me somewhere. Kill me I guess."
    pc "No doubt whatever they wanted would have been bad. And I had no plans on leaving my life in the hands of the people [miller.name] had watching the building."
    psy.name "And you thought going through the window was your best option?"
    if "survive_fall" in main_quest_05.list:
        pc "I had looked out the holes in the walls before. I was somewhat confident I could survive."
    else:
        pc "It was that or go back the way I came through a bunch of guards and a locked gate."
    pc "So I took a chance and jumped out the window. Tried to make sure I landed on my legs, but honestly don't much remember..."
    pc "You probably know more about that part than I do."
    jump haven_ending_wrapup_conclusion

label haven_ending_wrapup_got_intel:
    pc "Not a lot to say. I just listened to everyone when I could and managed to hear enough to piece together what happened with [ant.name]."
    pc "I didn't see the need to speak to [alex.fname] [alex.sname] after that so I just left."
    jump haven_ending_wrapup_conclusion

label haven_ending_wrapup_conclusion:
    pc "And here I am. Still alive and mostly healthy so I suppose that's good..."
    psy.name "It is. You managed to complete the mission assigned to you and make it home alive. Despite the hardships you have suffered, this is considered a success."
    pc "I didn't expect such cold words to come from you."
    psy.name "I am here to support you through what will be terrible situations. Coddling you while you will be expected to do more things like this in future will not be productive for your mental health."
    psy.name "I need to make sure you are strong enough to weather such harsh conditions and that you can push through the trauma. But we both know you might be asked to do it again..."
    pc "Mmm. Probably..."
    if player.preg_test():
        psy.name "I saw from your bloodwork that you are pregnant."
        pc "Apparently so."
        psy.name "How does that make you feel?"
        if player.has_perk(perk_wanted_preg):
            pc "Good. At least something nice can come out of spending time in [haven]."
            psy.name "You are not upset?"
            pc "Of this, no."
        elif main_quest_05.rape >= 10:
            pc "Guess it's to be expected when you get raped as much as I was..."
            psy.name "..."
        elif player.has_perk(perk_unwanted_preg):
            pc "Pretty shitty. Not something I would have like to happen."
        else:
            pc "Not sure. I suppose it's to be expected after..."
        psy.name "Well, as I am sure you already know. You can expect the best medical treatment we can offer."
    psy.name "I have also asked [emile.name] to stay with you for the foreseeable future."
    pc "You have? Why?"
    psy.name "I believe it will now help you come to terms with... Everything that is happening around you."
    pc "Now help me? What do you mean \"Now\"?"
    psy.name "When you woke from your coma, it was felt that having [emile.name] around you would end up hampering your development and make your adjustment period harder to cope with."
    pc "Why?"
    psy.name "We felt that in a situation where literally everything is new and unfamiliar, you would cling too tightly to what small familiarity you do have. Cling to [emile.name]."
    psy.name "This we felt would end up making you dependent on her and not develop yourself."
    psy.name "We no longer feel that is the case. Now we believe you would do better to have your sister nearby."
    psy.name "She can also keep an eye on your mental stability and inform us if anything happens."
    pc "..."
    pc "If you say so."
    psy.name "I do. We do."
    pc "So you are the reason she never came to visit after she left?"
    psy.name "Yes, not me directly but the decision was made to give you time alone."
    pc "..."
    pc "Ok..."
    psy.name "But I think now is a good time to speak to [tucker.name]. [emile.name] has been preparing clothes and other items so once you are done there, you should be able to head straight home."
    pc "*Sigh*"
    pc "If you say so."
    psy.name "I hope you will pay me another visit soon."
    pc "Mmmm. Goodbye."
    hide brooker with dissolve
    $ walk(loc_hospital_lobby)
    pause 0.5
    if temp_var_1 > 0:
        pc "Good job [emile.name] won't know any of that. Not sure how she would handle hearing about what happened in [haven]."
    else:
        pc "Not a lot happened in [haven] but probably for the best that [emile.name] doesn't hear about it regardless."
    pc "Anyway, let's inform [tucker.name] what is going on with [ant.name]."
    $ walk(loc_hospital_office)
    pc "[tucker.name], can I come in?"
    show tucker at right1 with dissolve
    tucker.name "Of course. I have been waiting for you. Coffee?"
    pc "Sure."
    tucker.name "First of all. I would like to say I am happy to see you here safe and sound. I can't imagine what it might have been like in [haven] and I won't even ask. I am just glad you are here."
    pc "Mmm."
    tucker.name "Here."
    $ player.right_hand = "coffee"
    pc "Thanks."
    tucker.name "So, was the trip there at least fruitful?"
    pc "It was and it wasn't. [ant.name] won't be returning to [haven] any time soon, if at all."
    tucker.name "Oh?"
    pc "It seems he and [alex.fname] [alex.sname] had a disagreement. It looks like [ant.name] wanted to use the residents of [haven] as research subjects for some kind of drug."
    pc "[alex.fname] was under the impression it was a narcotic, but considering this is [ant.name], there is probably more to the story than even [alex.fname] was aware of."
    pc "Anyway, [alex.fname] was having none of it and expelled [ant.name] from [haven]."
    tucker.name "Hmmm, this is odd..."
    pc "Well, I expected you might know why he might want something like that so I didn't push for more details."
    tucker.name "No, I don't know. But I will speak to people on the body project and see if they know what he might be after. I can't think of any other reason he might want research on some kind of drug other than for his body."
    tucker.name "Anyway, do we know where he might be now?"
    $ player.right_hand = ""
    pc "Maybe. It seems he might have turned to \"The Twins\". The way it was spoken made it sound like it was the name of two people. But I am not entirely sure on that. No one really went into much detail about it."
    pc "But it seems The Twins has something to do with the manufacturing of drugs. It was never specified if it was narcotics but it's a fair guess based on the way people spoke."
    if "intel_mid" in main_quest_05.list:
        pc "But there is something I noticed that was a bit strange."
        tucker.name "How so?"
        pc "It seems [ant.name] offered his medical services to people in [haven]. But listening to the things they had to say about him does not paint a pretty picture."
        pc "Other than him claiming to be a doctor, it doesn't sound like he was able to even help anyone. It doesn't sound like he had any medical skills at all."
        tucker.name "Hmm, that is strange. While he is not a specialised diagnostician, he should have been able to easily diagnose the kind of issues people in [haven] would have."
        tucker.name "Most of those would be sexually transmitted infection and issues relating to alcohol and drug abuse. Fairly simple conditions to spot and deal with."
        pc "Well, from the things people were saying, he was quickly judged to be someone to avoid."
        tucker.name "Hmmm..."
    tucker.name "Well, I will get to work looking into what you have told me. I will deal with getting information from the lab techs on why he would want to research drugs. I will also speak to [miller.name] about anything relating to \"The Twins\"."
    tucker.name "For now, go home and spend some time with [emile.name]. And if you still agree to work for us, come and see me in a few days."
    tucker.name "And here is your pay for a job well done and what you left behind before you left."

    $ player.add_money((main_quest_05.reward * (t.day - main_quest_05.dict["day_entrance"])) + main_quest_05.reward_counter + 4000)
    $ inv_transfer(inv_backup, inv)
    $ inv.drop([item_haven_crowbar, item_haven_intel, item_haven_lighter, item_haven_fluid], 50)


    pc "Sure."
    tucker.name "Thank you [fname]."
    pc "Mmmm."
    hide tucker with dissolve
    $ walk(loc_hospital_lobby)
    pause 0.5
    pc "Hmm, wonder where [emile.name] might be?"
    pc "Probably waiting near my bed. Suppose I'll go check."
    pause 0.5
    $ walk(loc_hospital_ward)
    show nikolas at right1 with dissolve
    nik.name "Hope all was well in your meetings. Are you ready to be put back to normal again?"
    pc "Ah [nik.name]. Was actually looking for [emile.name]."
    nik.name "She is just dealing with some last minute things. She left some clothes for you there and will be back in a bit to take you home."
    pc "Ah ok."
    nik.name "So are you ready for your change?"
    pc "Sure I suppose."
    nik.name "Right, then undress please."
    pause 0.5
    $ pc_strip()
    pause 0.5
    nik.name "Ok, let's see here."
    $ player.hair_style = "loose"
    $ player.hair_fringe = 1
    $ player._hair_length = 10
    $ tab_top_acc = "makeup"
    $ refresh_avatar()
    call screen surgery_screen()

    $ pc_strip()
    $ t.hour = 1
    nik.name "Wonderful, everything seems fine. I will leave you to get yourself ready to go home."
    nik.name "And it is good to see you're well."
    pc "Thanks."
    hide nikolas with dissolve

    pc "Hmm, wonder what [emile.name] is up to..."
    pc "Suppose I will change while I wait for her."
    $ pc_strip()
    pause 0.5
    $ pc_set_outfit("daily")
    $ pc_dress_slow()
    pcm "Feels good to have some clothes on that I haven't been sleeping in."
    show emile suitvest at right1 with dissolve
    emile.name "Ah, here you are?"
    pc "Yeah, thanks for the clothes."
    emile.name "No problem. You ready to head home?"
    pc "Yeah."
    emile.name "Great, let's head out."
    $ walk(loc_hospital_lobby)
    pause 0.5
    $ walk(loc_hospital_entrance)
    pause 0.5
    pc "Hmmm."
    emile.name "What?"
    pc "Just remembering the last time we left the hospital together."
    emile.name "Ah."
    if c.pants:
        pc "At least this time I have some underwear on."
    else:
        pc "No knickers on this time either."
    show emile happy
    emile.name "Ha! That's the part you choose to remember?"
    show emile neutral
    $ walk(loc_revel)
    emile.name "I guess you spoke to [psy.name] about us staying together?"
    pc "Yeah."
    pc "Hope you don't snore."
    if not player.male_origin:
        emile.name "We have slept together before so you know I don't snore. But with you in the new body, it's me who should be worried about that."
        pc "Oh?"
    else:
        emile.name "And what about you? Might be you who snores the roof down."
    pc "Didn't think of that..."
    emile.name "I'll just stick a pillow over your face if it becomes a problem."
    pc "This the stuff I left behind when I went to [haven]?"
    emile.name "Yeah, I didn't know what to bring you so just settled for this."
    pc "Trying to make me feel right at home in my old stuff?"
    emile.name "Heh, not really."
    pause 0.5
    $ walk(loc_residential)
    pause 0.5
    emile.name "Well, here we are. Want to just head straight up or..."
    pc "Yeah, I am tired after the day I have had. Let's go inside."
    emile.name "Ok."
    $ walk(loc_stairwell)
    pause 0.5
    $ walk(loc_bedroom)
    pause 0.5
    emile.name "..."
    emile.name "I hope you are okay with us bunking together."
    pc "Not much choice really. Not unless you want to sleep with one of the guys."
    emile.name "No thanks..."
    pc "You sure? I don't mind."
    emile.name "Yeah I bet. How about you do that and I get the bed all to myself?"
    pc "Hey, was mine first."
    emile.name "No it wasn't. I was here while you were in the hospital. If you wanna play by those rules then the bed is mine."
    pc "Alright, whatever. Just don't be wetting the bed or anything."
    emile.name "Hey! I was still a child!"
    pc "Yeah yeah."
    emile.name "Pfft! Well anyway. If you wanna do something together I'll be around for a chat."
    pc "You still working with The Institute even when I am not hanging out with the homeless?"
    emile.name "Yeah. And no doubt I will have a mountain of things to do with you coming back from [haven]. Not heard what you told [tucker.name] but no doubt it will be all hands on deck when I next go in."
    emile.name "But normally I have weekends off, so if you want to hang out together then it's good. Or after work."
    pc "Sounds good."
    emile.name "Well anyway, I'll unpack some stuff."
    pc "Ok, speak later."
    $ haven_complete_questlog()
    hide emile with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
