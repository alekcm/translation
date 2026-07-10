default main_quest_01_qs = 0
default main_quest_01_passed = False


label main_quest_01_briefing:

    $ main_quest_01.activate()
    $ diary_main_quest_01 = Diary_Class("My first mission", "I finally bit the bullet and visited The Institute today and had a chat with [tucker.name].\nHe gave me a rough idea of what they expect of me. Or I guess hope they can get from me.\nI have been asked to go to the pub and get some information off of someone who is poking their nose in their business.\nOr something...\nNot entirely sure what is going on, But I suppose I should go and see what I can do.")
    $ walk(loc_hospital_office)
    show tucker smile at right1 with dissolve
    if t.day == 0:
        tucker.name "Hello Miss [sname]. You came here a lot quicker than I expected. I thought you would have wanted more time to adjust to your situation."
    elif t.day <= 7:
        tucker.name "It's good to see you again Miss [sname]. I hope you have been adjusting well."
    elif t.day > 15:
        tucker.name "Hello Miss [sname]. It's been a while. I was starting to think you might not come to visit me. I hope you have been adjusting well."
    else:
        tucker.name "It's good to see you again Miss [sname]. How has returning to school been? I hope you are adjusting well."

    if name == fname:
        pc "It's [name], and it's a lot easier to adjust when you have all the info on what's going on."
    else:
        pc "It's [fname]. Or better yet, [name]. And it's a lot easier to adjust when you have all the info on what's going on."
    tucker.name "Well, I won't argue with you there. But there is nothing to stress about."
    $ player.face_frown()
    pc "Hmmm, the world has gone in the toilet so I think I will keep some scepticism."
    tucker.name "Mmm, rightly so. But I will at least promise you we have nothing sinister planned for you. We just need someone we can rely on. And that's where you come in."
    pc "What makes you think you can rely on me?"
    if quest_homeless_start.active:
        tucker.name "Coming into [town] with only the clothes on your back and still managing to get through it all paints you in a good light."
        pc "Pretty sure half the whores in the slum can say the same thing."
        tucker.name "Maybe, but none of them has [emile.name] to vouch for them."
        pc "Ah, so a bit of nepotism then."
        tucker.name "Call it what you will. Are you ready to do something for us? Your first mission so to speak."
    else:
        tucker.name "Well, as I explained before. With your situation it would be highly destructive to yourself if you were to divulge anything that goes on here."
        $ player.face_suspicious()
        pc "Chopped up on a lab table for the secrets of a new body? Why is this not something you want for me?"
        $ player.face_frown()
        tucker.name "Well why would we need to? We already have the secrets. What we need now is data. Are there side effects? How do you mentally recover? That sort of thing."
        tucker.name "Using you to complete sensitive tasks for us is just an added benefit. And on that topic, are you ready to do something for us? Your first mission so to speak."
    pc "Well, I can certainly listen."
    tucker.name "Good enough. Well ok..."
    tucker.name "We have had reports of someone trying to get info from our staff members. We aren't entirely sure what his goals are or what he might know about us. So we want you to find out."
    tucker.name "His name is [simon.fullname] and is a self-proclaimed reporter. Here is a photo of him."
    $ player.face_surprised()
    pc "A reporter?"
    tucker.name "Emphasis on the \"Self-proclaimed\". You might not be aware but news these days is highly curated. Propaganda basically. So actual reporters no longer exist."
    tucker.name "Most likely he is someone aiming to find something he can use to blackmail The Institute or its staff. We can't let that happen. But how we deal with him depends on what he knows."
    $ player.face_shock()
    pc "Deal with him? Like kill him."
    tucker.name "No, that would bring even more attention if we did something so rash. No, we would use much more tactful methods."
    $ player.face_frown()
    pc "Should I ask what methods?"
    tucker.name "Depends on the situation. Anything from just giving the info if it's mundane enough, to bribery or threats."
    pc "Ok..."
    tucker.name "Unfortunately against people who want to bring us harm, there is often little choice."
    pc "And what makes you think I am capable of getting the info you want from him?"
    tucker.name "We don't think you are capable. This is a task that we do not expect you to succeed. Our aim is to see how you deal with such work. Basically, to allow you to practice in a safe environment."
    pc "You expect me to fail? Won't that cause you trouble?"
    tucker.name "Probably not. The so-called reporter probably hasn't got a clue about anything that goes on here."
    pc "That makes the two of us..."
    tucker.name "Heh, in time you will find out more. Ordinarily we would just ignore him. But he makes a good target for you to practice on."
    pc "And if I refuse?"
    if quest_homeless_start.active:
        tucker.name "Then nothing. You go home and I find someone else to do the work I need."
        tucker.name "But being that you have no history in [town], no loyalties or ties. You make a good candidate."
    else:
        tucker.name "Nothing. I will reiterate my promise that we have nothing sinister planned for you. Our goal with you is just research data and having you perform tasks is just a bonus we hope will both bear fruit and aid in your recovery."
    tucker.name "And for a little motivation, the pay is probably better than anything else you would be capable of earning."
    pc "Ok, so what do you want from me?"
    tucker.name "The so-called reporter, [simon.fullname], is in the pub almost every night in the hope of eavesdropping on conversations from Institute staff members."
    tucker.name "We want you to somehow find out what he knows or what his aims are. Strike up a conversation with him and try and get the info."
    pc "Not break into his flat or pickpocket him or something?"
    tucker.name "Are you even capable of either of those?"
    tucker.name "No, as I mentioned before, we expect you to fail. You have zero training in such things so to expect anything else is unreasonable."
    tucker.name "The real goal is to spook him. This will either scare him away or have him lead us to any co-conspirators."
    tucker.name "The final result really doesn't matter. Getting you on board and getting practice is our ultimate goal. So give it a go with no pressure."
    pc "Speak to the reporter, [simon.fullname], in the pub and find out what he knows? Ok. I will think about it."
    tucker.name "No problem. Think it over and come and see me once you have made your choice."
    $ player.face_normal()
    $ main_quest_01.stage = 1
    $ log.markdone("mq_01_a")
    jump tucker_generic_cont
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
