label pinkroom_customer_event_spanking:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "Mmmm, you have a sexy ass. I want to leave here with it all purple."
    pc "Purple?"
    tempname.name "Yup. I'm gonna spank you 'til you scream."
    pc "Okay."
    $ inv.take(item_pinkticket, 4)
    tempname.name "Come here, bend over bitch."
    $ renpy.show(renpy.random.choice(["sb_onfours", "sb_doggy1", "sb_doggy2"]))
    with dissolve
    pc "Like this?"
    tempname.name "So sexy."
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    pc "Ah, starting already?"
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    tempname.name "Shut up!"
    pc "..."
    tempname.name "That's better."
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    pc "Nnng!"
    tempname.name "Nothing better than a bitch with a red arse."
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    tempname.name "And I know whores like you love it."
    pc "Do we?"
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    tempname.name "I said shut up!"
    if player.check_nowill():
        pc "..."
        tempname.name "Good girl."
    else:

        pc "Don't like a girl who talks?"
        $ player.spank()
        $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
        tempname.name "You are asking for something worse!"
        pc "I'm just here bent over."
        $ player.spank()
        $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
        pc "Nnng!"
        pc "Can you even afford to do worse?"
        $ player.spank()
        $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
        if numgen():
            tempname.name "I can. Keep talking and I will!"
            $ player.spank()
            $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
            pc "Ah!"
            menu:
                "Keep talking":
                    pc "Can't even get a whore to do what you..."
                    tempname.name "Right, you asked for it."
                    $ renpy.scene()
                    with dissolve
                    $ inv.take(item_pinkticket, 2)
                    "He throws some tickets on the floor."

                    jump pinkroom_customer_event_forced_sex
                "Keep quiet":
                    pc "..."
                    tempname.name "Good. Know your place!"
        else:
            tempname.name "Oh? That's your game bitch?"
            pc "No idea what you are talking about."

    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    tempname.name "All you bitches round here could do with this."
    tempname.name "Walking around with your ass red is so fucking sexy."
    $ player.spank()
    $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
    if numgen():
        jump whore_street_sex_floor_anal
    else:
        tempname.name "Dirty little girl!"
        $ player.spank()
        $ if_showing("sb_onfours", "noman", "sb_doggy1", "noman", "sb_doggy2", "noman", trans=None)
        pc "Nnng!"
        pc "..."
        pc "... ..."
        pc "Did you stop?"
        if numgen():
            pc "Err, where did you go?"
            pcm "Did he just leave?"
            pcm "Oh well..."
        else:
            tempname.name "Cheers you dirty girl."
            pc "Okay, had your fun?"
            tempname.name "Sure did. I'll leave you and your bright ass to it."
            pc "C'ya."



    jump whore_street_sex_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
