label pinkroom_customer_event_beating:
    "The guy marches in and dumps a bunch of tickets on the bed. They are quite a lot and considering how angry he looks, I think I can guess what he wants..."
    $ player.face_worried()
    pc "Have some restraint..."
    $ inv.take(item_pinkticket, 8)
    "I pick up the tickets and put them away when..."
    $ player.punch(True)
    pc "Ah!"
    $ player.punch(True)
    pc "Nnnng!"
    pcm "Fuck it hurts!"
    $ player.punch(True)
    tempname.name "Fucking bitch!"
    tempname.name "Fuck you for talking to me like that!"
    $ player.punch(True)
    tempname.name "If you ever do it again, I'll make you regret it!"
    pcm "Lunatic!"
    $ player.punch(True)
    tempname.name "Are you sorry?"
    pc "Yes, I am sorry!"
    tempname.name "Good you fucking cunt!"
    $ player.punch(True)
    "He punches me one last time, then marches out the door."
    pcm "..."
    pcm "Fuck that hurt."
    pcm "Damn weirdos..."
    pcm "Ugh... Am I bleeding?"
    pc "*Sigh*"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
