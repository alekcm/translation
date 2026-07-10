label main_quest_02_transform:
    $ main_quest_02.stage = 2

    $ walk(loc_hospital_ward)
    show tucker at right1 with dissolve
    show nikolas at right3 with dissolve
    nik.name "So, ready for the changes?"
    pc "As ready as I'll ever be..."
    nik.name "Don't worry, it's a simple procedure."
    nik.name "First I need you to undress. Need to make sure you can be seen fully to be sure there are no issues."
    if not player.has_perk([perk_exhibitionist, perk_whore, perk_slut, perk_commando]) or player.check_nowill(notif=False):
        pc "Errm..."
        nik.name "I helped create this body. I have seen more of it than you can imagine. Don't worry."
        pcm "Well, still feels a bit uncomfortable."
        pcm "Suppose he's right. He's probably seen parts of this body I never will..."
    pc "Ok..."
    $ player.uncover()
    $ pc_striptease()
    nik.name "Lets see here, lets start with the skin..."
    $ player.skin_colour = "4_0_base"
    $ player.nip_colour = main_quest_02.race
    $ refresh_avatar()
    nik.name "Wonderful..."
    tucker.name "Hmmmm. Impressive."
    nik.name "Now, your hair..."
    $ player.hair_colour = main_quest_02.hair_colour
    $ refresh_avatar()
    nik.name "Ok... Now the eyes."
    $ player.eye_colour = main_quest_02.eye_colour
    $ refresh_avatar()
    pc "Wow. You can do this much?"
    if player.breasts == 1:
        nik.name "We can do more than this. Can make physical changes like your breast size. But I think what we have here is close enough."
    else:
        nik.name "That's not the end of it. You are a bit more busty than in the photo so..."
        $ player.breasts = 1
    nik.name "And there we go."
    tucker.name "Her hair is a bit different than in the photo, but women change their hair constantly so I don't think it will be a huge issue."
    pc "Can I put my clothes back on?"
    nik.name "Yes of course, we are done here for now. Come see me after the mission and I will revert you back to how you were. Or if you feel like it, I can change you into something more to your liking."
    $ pc_dress_under()
    tucker.name "One step at a time. Thank you [nik.name]."
    $ pc_dress()
    nik.name "You are welcome, goodbye Miss [sname]."
    hide nikolas
    $ walk(loc_hospital_office)
    show tucker at right1
    tucker.name "Ok, now about the mission. Go to the pub in the evening and leave a chalk marking on the door. Then head to the old highway and wait for [simon.name] to arrive."
    tucker.name "Get the package off him and job done. Either drop it off at reception or come and see me once it's done."
    pc "Ok, any advice?"
    tucker.name "It's him that contacted you so he is desperate. He should be quick to hand over the package, but if he has his suspicions then you have two choices."
    tucker.name "Push and bully him. He is already pulling you into his troubles so to further inconvenience you at this meeting is unacceptable."
    tucker.name "Or play nice and calm his fears and worries."
    tucker.name "And once his package is in your hands, leave. There is no need to hang around at all."
    pc "Even if I just run away from him? Won't he then be suspicious?"
    tucker.name "At that point, who cares? [nadia]'s job is done so just go. While it is preferable to preserve a cover, it's fine to burn your cover to escape."
    pc "..."
    tucker.name "But I am saying all this just for your knowledge. The reality is, this exchange will be a simple affair. [simon.name] is not a dangerous person or even a particularly smart person."
    tucker.name "If I were in your shoes, I would go for a direct approach, ask for the package with your hand out expectantly. Take it and walk off without another word."
    pc "Ok, well I hope it all goes as easy as you expect."
    tucker.name "Well, you can tell me about it once it's done. Have fun [fname]."
    pc "Err. I'll try..."
    $ log.markdone("mq_02_b")
    hide tucker
    $ main_quest_02.stagedesc = "Go to the pub in the evening and leave a chalk marking on the door to signal to [simon.fullname] that you want to meet."

    $ walk(loc_hospital_lobby)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
