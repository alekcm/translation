label loc_office_pi_closed:
    pcm "Closed. Sign says [loc_office_pi.opening_hours_display]."
    jump travel

label loc_office_pi_discover:
    $ add_to_list(loc_office_pi.list, "intro")
    pcm "[simon.fullname] Private Investigator?"
    pcm "This place was right here and [tucker.name] still called him a \"so called reporter\"?"
    pcm "Couldn't they have just looked out the window or something and found out who he was?"
    pcm "Guess this is why they have me doing all their running around."
    $ loc_revel_backstreet_stairwell.locked = False
    jump travel

label loc_office_pi_enter_firsttime:
    $ walk(loc_revel_backstreet_stairwell)
    $ loc_revel_backstreet_stairwell.locked = False
    $ walk(loc_office_pi)
    $ loc_office_pi.visited = True
    pc "Helloooooooo..."
    show simon at right1 with dissolve
    simon.name "Welcome. [simon.fullname] at your service. How can I help?"
    if simon.creamvag:
        pc "Hi. I'm here to collect child support for the baby you left inside me."
        simon.name "What?? A baby... What???"
        pc "Yup. We had fun in the pub and I ended up getting pregnant."
        simon.name "You? From the..."
        simon.name "Err... Hold on..."
        hide simon with dissolve
        "[simon.name] rushes past me and out the main door."
        pc "YOU KNOW THIS IS YOUR OFFICE!"
        pc "I can wait all day."
        pcm "..."
        pcm "... ..."
        show simon at right1 with dissolve
        simon.name "*Sigh*"
        simon.name "What is it you want?"
        $ player.face_laugh()
        pc "Mostly to wind you up."
        simon.name "What??"
        pc "Haha. Running out the door!"
        simon.name "..."
        $ player.face_neutral()
        if player.showing:
            simon.name "So... Your belly? It's not mine?"
            if player.preg_father_class == simon:
                pc "Oh it is yours."
                simon.name "Fuck!"
                pc "\"Fuck\" is how I got this."
                simon.name "..."
                simon.name "So what do you want?"
                pc "Err. Give me money."
                simon.name "Really?"
                pc "Err, yes and no. Actually I just came here because I saw the sign on the wall."
                pc "Couldn't resist teasing you at the same time."
                pc "But I'll take your money."
            elif simon.preg:
                pc "This one? No. But you did get me pregnant."
                simon.name "Err... Fuck..."
                pc "Yup. You one and this one because of \"fuck\"."
                simon.name "So what do you want?"
                pc "Err. Give me money."
                simon.name "Really?"
                pc "Err, yes and no. Actually I just came here because I saw the sign on the wall."
                pc "Couldn't resist teasing you at the same time."
                pc "But I'll take your money."
            else:
                pc "No, it's not. But I couldn't resist teasing you."
                simon.name "..."
                pc "I'll take money if you are offering though."
        else:
            simon.name "So you aren't pregnant?"
            if player.preg_knows and player.preg_father_class == simon:
                pc "Oh I am. Not showing yet though."
                simon.name "And it's mine?"
                pc "Yup."
                pc "\"Fuck\" is how I got this."
                simon.name "..."
                simon.name "So what do you want?"
                pc "Err. Give me money."
                simon.name "Really?"
                pc "Err, yes and no. Actually I just came here because I saw the sign on the wall."
                pc "Couldn't resist teasing you at the same time."
                pc "But I'll take your money."
            elif player.preg_knows:
                pc "Oh I am. Not yours though."
                simon.name "Thank fuck!"
            else:
                if player.has_perk(perk_preg_notwant):
                    pc "I bloody hope not. I just couldn't resist the joke."
                else:
                    pc "Don't think so. I just couldn't resist the joke."
                simon.name "..."

    elif main_quest_01.missionvar1:
        pc "I just saw your name on the door and thought I would pop by."
        simon.name "Err... Do I know you?"
        if bob.naughty:
            pc "Well, you have photos around here somewhere of me and [bob.name] so I thought you would remember me."
            simon.name "Ah! It's you! That was a good job. Nice and easy."
            if bob.asex:
                pc "Was a pain in the arse for me."

        elif simon.sex:
            pc "Maybe I should take my clothes off to remind you. We did spend most of our time naked after all."
            simon.name "You a whore?"
            pc "No. I met you in the pub while working on something."
            simon.name "Ah! I remember now!"
        elif "intimidate_branch_pass_intimidate" in main_quest_01.list:
            pc "I met you in the pub. Though I was being a but more mean than I am now."
            simon.name "The pub?"
            simon.name "..."
            simon.name "Ooooh shit."
            pc "Yup."
            simon.name "I gave you what I knew."
            pc "I know. I'm not here for that."
        elif "waitress_branch" in main_quest_01.list:
            pc "I was working the pub and helped you out with something you needed help with."
            simon.name "Err... Okay... If you say so..."
        else:
            pc "Clothes for a question in the pub alleyway ring a bell?"
            simon.name "Ooooh? Yes it does. That was fun."
    else:

        pc "I just saw the name on the door and thought I would pop in."
        simon.name "Do I know you?"
        pc "Sort of. Last time we met you found out who I work for and avoided me."
        simon.name "Ah... Yes... So you are following me here?"
        pc "Nothing like that. We found out what you were after and my bosses decided they didn't care."
        simon.name "Are you serious?"
        pc "Yup."
        simon.name "So you aren't here to shake me down?"
        pc "No."

    simon.name "Well, what are you here for anyway?"
    pc "I just saw the sign and saw a familiar name, so thought I would pop in."
    simon.name "You... Err... Still working for them?"
    pc "Doubt there will be a time where I am not working for them."
    simon.name "Err... Okay. I know well enough not to pry."
    pc "For the best."
    simon.name "Well, if you are looking to freelance, I could always use someone like you."
    simon.name "Or if you need help on one of your... dealings... with them. Then I can help out for a price."
    simon.name "Help each other out and get more money flowing."
    pc "I do like money."
    simon.name "Don't we all."
    simon.name "[name], wasn't it?"
    pc "That's right."
    simon.name "Hope we can work together in future [name]."
    hide simon
    $ walk(loc_revel_backstreet)
    pcm "Well, that was interesting. Wonder if I will be able to get work with him?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
