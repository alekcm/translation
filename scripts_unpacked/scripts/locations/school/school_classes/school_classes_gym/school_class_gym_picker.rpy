



label school_class_gym_picker:
    $ walk(loc_school_gym)

    if school_day == 0:
        if t.day == 3:
            jump school_class_gym_first_day
        else:
            jump school_class_gym_first_day_missed

    if t.wkday in ("Tuesday", "Thursday") and not school_dance_intro:

        if t.day == 4:
            jump school_class_gym_dance_intro
        else:
            jump school_class_gym_dance_intro_missed

    elif player.pregnancy >= 2:







        if t.wkday in ("Monday", "Wednesday") and not school_gym_preg:
            jump school_class_gym_preg_kicked
        else:

            jump school_class_preg

    elif t.wkday in ("Tuesday", "Thursday") and school_dance_quest_preg == True:



        $ school_dance_quest_preg = False
        jump school_class_gym_dance_preg_rejoin
    else:

        if school_gym_preg == True:

            $ school_gym_preg == False

        if t.wkday in ("Tuesday", "Thursday"):
            jump school_class_gym_dance
        elif t.wkday == "Monday":
            jump school_class_gym_run
        elif t.wkday == "Wednesday":
            jump school_class_gym_vball
        elif t.wkday == "Friday":
            jump school_class_gym_dance






label school_class_gym_dance_intro:


    $ walk(loc_school_gym)
    show svet at right1 with dissolve
    svet.name "Okay girls, gather round. I am [svet.name] your club leader. As you might have guessed, I am not a teacher here but a student like everyone else."
    svet.name "I created this club because I love to dance, and I am sure you are all here for the same reason."
    svet.name "Now, I have a few rules here. Rule 1. We are all girls here and I expect you all to support each other and not bring each other down."
    svet.name "Rule 2. There will be no shame here. If you dance like a three legged donkey but have fun, then go wild. Anyone mocking the donkey will be removed from the team."
    svet.name "Now, with that out of the way, we have classes on Tuesdays and Thursdays and the [dancet] will be here on weekends practicing, feel free to join."
    svet.name "I expect good things from you all and most of all, have fun! We will start our first class on Thursday so for now you can all go home."
    hide svet with dissolve
    pcm "Well, that all sounds good. Hopefully I can enjoy myself here. Didn't realise it would be all girls though. Did [tucker.name] know this when he signed me up?"
    pcm "I wonder if that is part of his plan to get me more socially adjusted. Ah well, doesn't really matter. Suppose I will go home then."
    $ school_dance_intro = True
    $ school_day += 1
    $ stroll(60)
    jump travel

label school_class_gym_dance_intro_missed:
    show svet at right1
    $ walk(loc_school_gym)
    svet.name "[fname] [sname]? Over here, lets have a chat."
    pc "Ok."
    svet.name "You missed the intro class so I will go over a few things quickly with you. Dance is on Tuesdays and Thursdays."
    svet.name "And basically, have fun. Don't tease anyone or you will be punished. And have fun, it's important."
    if not player.showing:
        svet.name "Now go and get changed, you are already late for the class."
    else:
        svet.name "But I can't have you here with that belly. So go to your preggo classes and come back when it's gone."
    pc "Ok."
    hide svet
    if svet.showing:
        pcm "She has a belly like mine but still shoos me away?"
    $ school_dance_intro = True
    jump school_class_gym_picker

label school_class_gym_dance_jointeam:
    show svet at right1 with dissolve
    svet.name "Hey [name], you have been making great progress, how about you join the [dancet]?"
    pc "What? Really? I would love to."
    svet.name "Well before you decide, we have an extra event on Tuesday and Thursday."
    pc "Yes, where you go and do an event or something."
    svet.name "Yeah something like that. The school usually arranges some exhibition with local officials or businesses."
    svet.name "Our next one is a small dance event in the park. Just dance to some music on the stage and interact with people in the park."
    svet.name "So you up for it?"
    pc "Yes of course."
    svet.name "Great. Good having you aboard."
    pc "Thanks, see you."
    hide svet with dissolve
    pc "..."
    pc "So looks like I really am making progress with my body if I am being asked to join the [dancet]."
    $ player.eye = 3
    $ player.mouth = 6
    pc "Heh"
    $ player.face_normal()
    pc "Should probably tell [tucker.name] at some point. I'm sure he will be glad to hear of my progress."
    $ log.assign("The Sweet Girls")
    $ school_dance_quest_on_team = True
    return



label school_class_gym_dance_preg_kicked:


    show svet at right1 with dissolve
    svet.name "Aww [name]... [name]... Ugh"
    svet.name "How do you expect to dance now with that fat belly?"
    pc "I can still dance."
    svet.name "Today and tomorrow sure. But your gonna become a fat cow in no time and I am not wasting my time on someone who is just going to get fatter and worse at dancing."
    svet.name "Sorry [fname] but you are going to have to take classes elsewhere. Come back when you aren't carrying a child and I might let you back."
    pc "..."
    svet.name "Oh and [name]..."
    svet.name "You dumb fuck! Why did you let some guy do this to you? Haven't you been listening in class about how fucked up things are right now for girls like us who get knocked up?"
    svet.name "And you let some guy stick a baby in you? I just don't know what to say..."
    pc "..."
    svet.name "*Sigh* See you round [name]."
    pc "Yeah..."
    hide svet with dissolve
    pc "..."
    pc "Suppose It's swimming class for me then."
    $ school_dance_quest_preg = True
    jump school_class_gym_picker

label school_class_gym_dance_preg_rejoin:


    show svet at right1 with dissolve
    pc "Hey [svet.name]."
    svet.name "[fname]. You aren't as fat as the last time I saw you. Everything go well?"
    pc "As well as things can go..."
    svet.name "Yeah..."
    pc "I was hoping I can re-join the group."
    if school_dance_quest_on_team == True:
        if player.isfat == True:
            svet.name "Well sure. But there is no way I am letting your fat arse back into [dancet]. You can re-join the normal classes."
            $ school_dance_quest_on_team = False
        elif player.fitness >= 30:
            svet.name "Looks like somehow you managed to keep up your fitness during all that so I suppose you can re-join [dancet]."
        else:
            svet.name "Well sure. But you haven't managed to keep up your fitness so I can't let you re-join [dancet] until you work it back up. For now you will have to re-join the normal classes."
            $ school_dance_quest_on_team = False
    else:
        svet.name "Sure, you can re-join the classes like before. Would be good for you to get back into shape after your pregnancy. Can't imagine it was easy to keep fit with a baby in your belly."
    pc "Thanks [svet.name]."
    if school_dance_quest_on_team == True:
        pc "I won't let you down!"
        svet.name "See that you don't."
        hide svet
    jump school_class_gym_picker





label school_class_gym_end:
    $ renpy.scene()
    with dissolve
    $ walk(loc_school_locker_girls)
    $ player.face_normal()
    $ school_gym()
    $ dialouge = renpy.random.choice([
    "I head to the locker room to shower and change.",
    "After class I head to the locker room to shower and change my clothes.",
    "I head off to shower and change in the locker room.",
    "With class over, I go to the locker room for a shower and a change of clothes."
    ])
    "[dialouge]"
    $ school_day += 1

    if school_dance_event_active():
        jump school_dance_show_ask

    jump shower_event
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
