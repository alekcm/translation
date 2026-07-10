define replace = Character('New friend', color="#ffffff")

define school_newfriend_quest_reject_drink = 0
define school_newfriend_quest_blackmail_material = False
define school_newfriend_quest_blackmailing = False
define school_newfriend_quest_refusedsex = 0
define school_newfriend_quest_refusedblackmail = 0
define school_newfriend_quest_shownpics = False

label school_newfriend_intro:
    $ school_newfriend_quest.stage += 1
    $ school_newfriend_quest.activate()
    "NOTE *** The dialogue is short and to the point here. It will be expanded on later."
    replace "Hey, your a new face right?"
    pc "Err, yeah...?"
    replace "Hey, names [replace]. How you settling in?"
    pc "Um, fine I suppose."
    replace "Well, better than most then. You got to grips with the place yet? I can show you around if you want."
    pc "What? No that's fine. Don't wanna put you out."
    replace "It's no problem. I usually show new people around but things are pretty busy right now with all the new people joining so must have missed you."
    pc "Ah really?"
    replace "Yeah, so how about it?"
    menu:
        "Okay sure, show me around":
            jump school_newfriend_showaround
        "No thanks, another time":

            replace "No worries."
            jump random_event_school_end_picker
    jump random_event_school_end_picker

label school_newfriend_showaround:
    "He will show you around. I don't want to write it just yet as there are some new locations I will be adding soon and they will be included."
    "Generally everything is nice and you will have a friendly chat while being shown around. The guy is nice and seems to know a lot."
    jump random_event_school_end_picker

label school_newfriend_event_picker:
    if school_newfriend_quest.stage in (1,2,3):
        jump expression "school_newfriend_chat_" + str(school_newfriend_quest.stage)
    elif school_newfriend_quest_blackmail_material == False:
        jump school_newfriend_invite
    else:
        jump school_newfriend_sex




label school_newfriend_chat_1:
    $ school_newfriend_quest.stage += 1
    "Chat with new friend event 1"
    jump random_event_school_end_picker
label school_newfriend_chat_2:
    $ school_newfriend_quest.stage += 1
    "Chat with new friend event 2"
    jump random_event_school_end_picker
label school_newfriend_chat_3:
    $ school_newfriend_quest.stage += 1
    "Chat with new friend event 3"
    jump random_event_school_end_picker

label school_newfriend_invite:
    "The new friend will invite you to have some drinks with him. Do you agree or not?"
    menu:
        "Agree":
            "You go and have some drinks with him. It is generally a pleasant time and you have a little much to drink."
            "Do you let him touch you and proceed to a blowjob?"
            menu:
                "Blowjob":
                    "Sammy gives him a blowjob."
                    $ school_newfriend_quest_blackmail_material = True
                "Refuse blowjob":

                    "You say goodbye and go about our day."

            jump random_event_school_end_picker
        "Don't agree":

            $ school_newfriend_quest_reject_drink += 1
            "You rejected having a drink with him."
            if school_newfriend_quest_reject_drink >= 3:
                "This is the third time you have rejected him. This quest chain will now close and he will not ask you anymore."
            jump random_event_school_end_picker

label school_newfriend_sex:
    if school_newfriend_quest_blackmailing == True:
        jump school_newfriend_sex_blackmail
    else:
        jump school_newfriend_sex_offer

label school_newfriend_sex_offer:
    "You new friend approaches you and offers some fun in the toilets or somewhere else. Do you agree?"
    menu:
        "Agree":
            "You go off to somewhere private and have sex with him."
            jump random_event_school_end_picker
        "Refuse":

            $ school_newfriend_quest_refusedsex += 1
            if school_newfriend_quest_refusedsex >= 3:
                $ school_newfriend_quest_blackmailing = True
                "You refused sex too many times. He will now show you he has pics of you doing naughty things with him."
                "If you don't do as he asks he will spread them around the school."
                "Do you agree to have sex with him now?"
                if player.check_nowill():
                    "You failed a will check so you dont get the choice to refuse him."
                    "You have sex with him again and this time he takes pics of you in the open and not so hidden."
                    jump random_event_school_end_picker
                else:
                    "You passed a will check. You get the choice to tell him to fuck off or not."
                    menu:
                        "Tell him no!":
                            $ school_newfriend_quest_refusedblackmail += 1
                            if school_newfriend_quest_refusedblackmail == 1:
                                "This is the first time you refused. He will not show the pics yet but threaten next time he will."
                                jump random_event_school_end_picker
                            else:
                                "This is the second time you refused. He tells you he will not be so kind this time and will show the pics around."
                                $ school_newfriend_quest_shownpics = True
                                jump random_event_school_end_picker
                        "Agree to sex anyway":

                            "You have sex with him and he will take more pics of you."
                            jump random_event_school_end_picker
            else:

                "He seems disappointed but goes away"
                jump random_event_school_end_picker

label school_newfriend_sex_blackmail:
    "Blackmail sex event. he will demand you go with him."
    if player.check_nowill():
        "you failed a will check so you do with him and do as he demands."
        "You have sex or whatever and then carry on your day."
        jump random_event_school_end_picker
    else:
        "You passed a will check. You get the choice to tell him to fuck off or not."
        menu:
            "Tell him no!":
                $ school_newfriend_quest_refusedblackmail += 1
                if school_newfriend_quest_refusedblackmail == 1:
                    "This is the first time you refused. He will not show the pics yet but threaten next time he will."
                else:
                    "This is the second time you refused. He tells you he will not be so kind this time and will show the pics around."
                    $ school_newfriend_quest_shownpics = True

                jump random_event_school_end_picker
            "Agree to sex anyway":

                "You have sex with him and he will take more pics of you."
                jump random_event_school_end_picker
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
