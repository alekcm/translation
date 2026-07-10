label main_quest_02_debrief:

    $ walk(loc_hospital_office)
    show tucker at right1 with dissolve
    $ log.markdone("mq_02_d")
    if t.hour in morning:
        tucker.name "Good morning, [fname]. I am glad you are here."
    elif t.hour in afternoon:
        tucker.name "Good afternoon, [fname]. I am glad you are here."
    else:
        tucker.name "Good to see you, [fname]. I am glad you are here."

    tucker.name "By the look on your face you meet with [simon.name]. How did it go?"
    $ player.face_worried()
    pc "I stood around some shady alley trying not to look like a prostitute for hours. Eventually [simon.name] popped out the dark near scaring me to death."
    pc "He shoved this in my arms and pretty much ran away. So I suppose it went well."
    $ inv.drop(item_simon_satchel, notif_message="Gave Simon's satchel")
    tucker.name "What did I tell you? Nothing to worry about."
    pc "Yeah. Apart from the shady guys hanging around in the dark looking at me like prey."
    tucker.name "Don't worry. We will eventually make it so you will eat them without trouble."
    $ player.face_neutral()
    pc "Yeah, I was thinking about that while waiting. Shouldn't I have some kind of defence training or something?"
    tucker.name "We considered that, but came to the conclusion it wouldn't do you any good. Your body wasn't built at all with combat in mind."
    pc "What was in mind when it was built?"
    tucker.name "Hmmm. I'm not sure you want to know that."
    pc "..."
    $ player.face_sus()
    pc "That's not for you to decide."
    tucker.name "No it's not, but think it over for some time before asking again. Then if you really want to know, then I will tell you. For now though, let's go see [nik.name] and return you back to how you were."
    pc "..."
    $ player.face_frown()
    pc "Ok"
    $ walk(loc_hospital_ward)
    show tucker at right1
    show nikolas at right3 with dissolve
    nik.name "Welcome back Miss [sname]. I trust your mission went well?"
    pc "It did. A bit anticlimactic, but fine."
    nik.name "That's good. So am I to guess you are here to return back to how you were before?"
    menu:
        "Yes please.":
            nik.name "Ok, please strip and let's get this done."
            pc "..."
            $ pc_striptease()
            nik.name "Ok, So you can pick what you like now. No need to go back to how you were before if you don't want to"
            call screen surgery_screen()
        "Can I stay like this?":
            nik.name "Sure you can."
    $ cosmetic_surgery_tutorial = False
    nik.name "And now that you are a fully fledged fixer, my services are always open to you. But unless it's for a mission then you need to pay for the materials used yourself."
    pc "Fixer?"
    tucker.name "We haven't got to that part yet. First I need you to meet someone."
    pc "Ok, who?"
    tucker.name "A psychologist, [psy.name]. She will be looking after your mental stability from now on. I need you to have a talk with her before we can wrap things up and pay you."
    $ player.face_worried()
    pc "A psychologist? Do I have to?"
    tucker.name "Protocol I'm afraid."
    pc "..."
    nik.name "Goodbye Miss [sname]."
    tucker.name "Follow me [fname]."
    hide nikolas
    jump main_quest_02_psychologist
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
