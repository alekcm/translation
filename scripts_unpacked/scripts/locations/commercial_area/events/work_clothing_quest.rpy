






label work_clothing_fasion_quest_hub:

    if work_clothing_fasion_quest == 0:
        jump work_clothing_fasion_quest_intro1

    elif work_clothing_fasion_quest == 1:
        jump work_clothing_fasion_quest_intro2

    elif work_clothing_fasion_quest_under == True and work_clothing_var_perv == False:
        jump work_clothing_fasion_quest_perv1
    else:

        "As you are preparing to leave, [marco] comes up to you."
        marco "hey [name], [suzie], there is another show tonight for some of our retailers. Are you interested in some extra work showing the clothes off?"
        suzie "Sounds good to me. I could so with the extra money. How about you [name]?"
        menu:
            "Yes.":





                $ randomnum = renpy.random.randint(1, 5)
                if randomnum == 1:
                    jump work_clothing_fasion_quest_show1
                elif randomnum == 2:
                    jump work_clothing_fasion_quest_show2
                elif randomnum == 3:
                    jump work_clothing_fasion_quest_show3
                elif randomnum == 4:
                    jump work_clothing_fasion_quest_show4
                else:
                    jump work_clothing_fasion_quest_show5
            "No.":

                jump work_clothing_fasion_quest_reject





label work_clothing_fasion_quest_intro1:

    "At the end of the day, you are getting ready to leave the store when your boss [marco] comes up to you and [suzie]"
    marco "Hey girls, we have some people from our retailers in town tonight and they want to see what we are offering for next years winter line."
    marco "Are you interested in some extra work modelling the clothes for them?"
    suzie "Im in."
    pc "Is it paid?"
    marco "Of course it is. You will get your days wage doubled and a 1% commision fee from all orders placed at the end of the show."
    suzie "Don't worry [name]. I've done this a few times. Most of them already know what they are ordering and come just for the free wine and dont even care you are there."
    suzie "Easy money. You should do it."

    menu:
        "Ok, lets do it.":
            jump work_clothing_fasion_quest_intro3
        "No, I think I'll pass.":

            $ work_clothing_fasion_quest = 1
            $ work_clothing_workdays += 1

            pc "Sorry [marco], I don't feel comfortable doing a modelling show. Next time maybe."
            marco "Okay no problem. Here is your days pay. Lets go [suzie]."
            suzie "See ya [name]."

            $ player.cash += work_clothing_salary

            jump commercial_area_mall_screen


label work_clothing_fasion_quest_intro2:

    "At the end of the day, you are getting ready to leave the store when your boss [marco] comes up to you and [suzie]"
    marco "Hey girls, we have some more people from our retailers in town tonight and they want to see what we are offering."
    suzie "Count me in."
    marco "Great, and how about you [name]? Same as before, Double your days pay plus commision."

    menu:
        "Ok, lets do it.":
            jump work_clothing_fasion_quest_intro3
        "No, I think I'll pass.":

            $ work_clothing_fasion_quest = 1
            $ work_clothing_workdays += 1


            pc "Sorry [marco], I don't feel comfortable doing a modelling show. Next time maybe."
            marco "Okay no problem. Here is your days pay. Lets go [suzie]."
            suzie "See ya [name]."

            $ player.cash += work_clothing_salary

            jump commercial_area_mall_screen

label work_clothing_fasion_quest_intro3:

    "You do a fasion show displaying the winter line of clothing"


    $ randomnum = renpy.random.randint(1, 10)
    if randomnum >= 6:
        "You are paid normally"
    elif randomnum == 10:
        "You are paid very well"
    else:
        "You are paid well"

    $ work_clothing_fasion_quest = 2
    $ work_clothing_fasion_var_shows += 1
    $ work_clothing_workdays += 1
    $ player.cash += work_clothing_salary
    "[marco] comes and thanks you for doing the show. Tells you that he will have more in future and hopes he can count on you in future"
    "You comment on the show and leave to go home"
    jump commercial_area_mall_screen






label work_clothing_fasion_quest_show1:
    "You do a fasion show displaying the winter line of clothing"


    if work_clothing_fasion_quest == 2:
        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 3:
            $ work_clothing_fasion_quest = 3

    jump work_clothing_fasion_quest_show_end



label work_clothing_fasion_quest_show2:

    if work_clothing_fasion_quest <= 2:
        jump work_clothing_fasion_quest_show1
    if work_clothing_var_spring == 0:
        $ work_clothing_var_spring = 1
    "You do a fasion show displaying the spring line of clothing"


    if work_clothing_fasion_quest == 3:
        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 3:
            $ work_clothing_fasion_quest = 4

    jump work_clothing_fasion_quest_show_end



label work_clothing_fasion_quest_show3:

    if work_clothing_fasion_quest <= 3:
        jump work_clothing_fasion_quest_show2
    if work_clothing_var_summer == 0:
        $ work_clothing_var_summer = 1
    "You do a fasion show displaying the summer line of clothing"


    if work_clothing_fasion_quest == 4:
        $ randomnum = renpy.random.randint(1, 2)
        if randomnum == 2:
            $ work_clothing_fasion_quest = 5

    jump work_clothing_fasion_quest_show_end



label work_clothing_fasion_quest_show4:

    if work_clothing_fasion_quest <= 4:
        jump work_clothing_fasion_quest_show3
    if work_clothing_var_swim == 0:
        $ work_clothing_var_swim = 1
    "You do a fasion show displaying the swimwear line of clothing"


    if work_clothing_fasion_quest == 5:
        $ randomnum = renpy.random.randint(1, 3)
        if randomnum <= 2:
            $ work_clothing_fasion_quest = 6

    jump work_clothing_fasion_quest_show_end



label work_clothing_fasion_quest_show5:

    if work_clothing_fasion_quest <= 5:
        jump work_clothing_fasion_quest_show4
    if work_clothing_var_under == 0:
        $ work_clothing_var_under = 1
    "You do a fasion show displaying the underwear line of clothing"



label work_clothing_fasion_quest_show_end:

    if work_clothing_var_spring == 1:
        $ work_clothing_var_spring = 2
        "Make a comment about working this job for the first time"

    elif work_clothing_var_summer == 1:
        $ work_clothing_var_summer = 2
        "Make a comment about working this job for the first time"

    elif work_clothing_var_swim == 1:
        $ work_clothing_var_swim = 2
        "Make a comment about working this job for the first time"

    elif work_clothing_var_under == 1:
        $ work_clothing_var_under = 2
        "Make a comment about working this job for the first time"
    else:

        $ randomnum = renpy.random.randint(1, 10)
        if randomnum == 1:
            "generic comment 1"
        elif randomnum == 2:
            "generic comment 2"
        elif randomnum == 3:
            "generic comment 3"
        elif randomnum == 4:
            "generic comment 4"
        elif randomnum == 5:
            "generic comment 5"
        elif randomnum == 6:
            "generic comment 6"
        elif randomnum == 7:
            "generic comment 7"
        elif randomnum == 8:
            "generic comment 8"
        elif randomnum == 9:
            "generic comment 9"
        else:
            "generic comment 10"



    $ randomnum = renpy.random.randint(1, 10)
    if randomnum >= 6:
        "You are paid normally"
    elif randomnum == 10:
        "You are paid very well"
    else:
        "You are paid well"

    $ work_clothing_fasion_var_shows += 1
    $ work_clothing_workdays += 1
    $ player.cash += work_clothing_salary

    if randomnum >= 9:
        "as you are about to leave, [suzie] tells you that some of the fasion guys have invited you all out for drinks."
        menu:
            "Go for drinks with them":
                jump work_clothing_fasion_quest_show_drinks
            "Say you dont want to":

                "You get your things and prepare to head home"
                jump commercial_area

    "leave to go home"
    jump commercial_area







label work_clothing_fasion_quest_show_drinks:
    "you have drinks with [suzie] and some of the guys. There might be multiple version of this quest. most of them quite lewd"
    "Here you will find out for sure that [suzie] is a slut and takes money off tese guys for sex on a regular basis"
    "She encourages you to do the same"





label work_clothing_fasion_quest_perv_intro:

    "At the end of the day, you are getting ready to leave the store when your boss [marco] comes up to you and [suzie]"
    "He explains that some more clients are coming to see some of their clothing lines"
    "Suzie can't do it today so you do it alone"

    menu:
        "Yes I agree":
            jump work_clothing_fasion_quest_intro3
        "No I refuse":

            $ work_clothing_workdays += 1
            $ player.cash += work_clothing_salary

            "You explain you dont have time tonight and say sorry"
            "You will get paid for the normal days work"

            jump work_clothing_fasion_quest_perv1



label work_clothing_fasion_quest_perv1:

    "You do a fasion show displaying the underwear line of clothing"
    "midway through the show marco leaves to the back of the shop with one of the clients"
    "The viewers of the clothes ask you to come slower so they can see the fit of the underwear"
    "One of them start to grope you. depending on your stats you can resist or oblige"
    "They say some crude things about you, your sexy ass and the like"

    "eventually marco returns and things calm down and the show eventually ends"



    $ randomnum = renpy.random.randint(1, 10)
    if randomnum >= 6:
        "You are paid normally"
    elif randomnum == 10:
        "You are paid very well"
    else:
        "You are paid well"

    $ work_clothing_fasion_var_shows += 1
    $ work_clothing_workdays += 1
    $ player.cash += work_clothing_salary
    if work_clothing_var_under == False:

        "make some comments on it being the first time doing the swimwear collection"
        "As you are getting ready to leave, one of the clients comes to have a chat with you"
        "He says you handles yourself well given the situation and would like you offer you a job serving private clients during dinner/drinking events"
        "He needs someone like you, someone sexy who can charm the men, but won't cause a fuss if things get a little out of hand"
        "he holds an event every friday and saturday evening. if you are interested then you should give him a call and he will put you on the books"
        $ work_clothing_var_perv = True
        jump commercial_area_mall_screen
    "You comment on the show and leave to go home"
    jump commercial_area_mall_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
