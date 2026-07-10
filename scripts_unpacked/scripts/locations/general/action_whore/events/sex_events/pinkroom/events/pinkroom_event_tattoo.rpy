init python:
    def pinkroom_customer_event_tattoo_picker():
        space = []
        if not tattoo.chest:
            space.append("chest")
        if not tattoo.ass:
            space.append("ass")
        if space:
            if random(space) == "chest":
                tattoo.chest = 1
            else:
                tattoo.ass = 1
        else:
            writing.add_writing_random("tattoo")

label pinkroom_customer_event_tattoo:
    pc "[rlist.pinkroom_welcome_single]"
    tempname.name "Hey darling, I'm looking for someone to practice my skills on. Up for a free tat?"
    pc "Err, okay..."
    $ inv.take(item_pinkticket, 2)
    tempname.name "Great, lay down and I'll get my stuff ready."
    show sb_onback relaxed pout with dissolve
    "I lay back watching the guy prepare, when he is ready he comes over to me."
    "I relax as he does his thing. Normally I might be totally opposed to this, but I can fortunately get them removed if I want to so its worth the tickets."
    $ relax(15)
    $ pinkroom_customer_event_tattoo_picker()
    show sb_onback with dissolve
    "It takes him a bit, but finally it looks like he is finishing up."
    tempname.name "There we go! Cheers love."
    "He quickly packs his stuff away and heads out the door."
    pcm "Why is he in such a hurry?"
    hide sb_onback with dissolve
    pcm "Well, at least it doesn't hurt..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
