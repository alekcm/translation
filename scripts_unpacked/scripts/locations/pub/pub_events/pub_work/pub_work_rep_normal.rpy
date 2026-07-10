label pub_waitress_work_normal:
    $ player.face_happy()
    $ pub_tips()
    jump expression renpy.random.choice([
    "pub_waitress_work_normal1",
    "pub_waitress_work_normal2",
    ])

label pub_waitress_work_normal1:
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["pub_serve_clevage", "pub_serve_ass"]))
    with dissolve
    $ dialouge = renpy.random.choice([
    "Here you go chaps, enjoy.",
    "Here you go lads, enjoy.",
    "Two beers here. Enjoy yourselves.",
    "Drinks are up. Have fun guys.",
    ])
    pc "[dialouge]"
    $ player.hands_reset()
    $ dialouge = renpy.random.choice([
    "Cheers love!",
    "Nice one sweetheart.",
    "Ahh my beer angel.",
    "The beer angel has spoken and all must obey!",
    "Ahh nice one sweetheart.",
    "Excellent, cheers darling.",
    "Sweet, drink up lads."
    ])
    patron "[dialouge]"
    if pub_waitress.timesworked > 6 and numgen(0,5) == 0:
        jump pub_waitress_work_grope
    jump pub_waitress_work_cycle1

label pub_waitress_work_normal2:
    $ renpy.scene()
    $ renpy.show(renpy.random.choice(["pub_serve_clevage", "pub_serve_ass"]))
    with dissolve
    $ dialouge = renpy.random.choice([
    "Eeeeyyy! The beer lady has come!",
    "The heartbreaker is here, drink up lads.",
    "Ahh my beer angel is here.",
    "Here she is. Cheers love.",
    "Ahh nice one sweetheart, stick 'em down right here.",
    "Excellent, cheers darling."
    ])
    patron "[dialouge]"
    $ player.hands_reset()
    $ dialouge = renpy.random.choice([
    "Enjoy yourselves boys.",
    "Enjoy and don't be getting up to trouble now.",
    "Enjoy lads. Make sure you can leave here on your own two feet..",
    "Drinks are up. Have fun guys.",
    ])
    pc "[dialouge]"
    if pub_waitress.timesworked > 6 and numgen(0,4) == 0:
        jump pub_waitress_work_grope
    jump pub_waitress_work_cycle1



label pub_waitress_work_grope:
    $ player.face_happy()
    $ pub_tips()
    jump expression renpy.random.choice([
    "pub_waitress_work_grope_grope",
    "pub_waitress_work_grope_spank",
    ])

label pub_waitress_work_grope_grope:
    $ if_showing("pub_serve_clevage", "grope", "pub_serve_ass", "grope", trans=None)
    $ player.grope(hands=False)
    pc "..."
    $ dialouge = renpy.random.choice([
    "Oooh so nice.",
    "Lovely",
    "Mmmmmmm.",
    "Ah so soft."
    ])
    patron "[dialouge]"
    jump pub_waitress_work_cycle1

label pub_waitress_work_grope_spank:
    $ if_showing("pub_serve_clevage", "grope", "pub_serve_ass", "grope", trans=None)
    $ player.spank()
    $ player.add_desire_random(5)
    $ player.face_surprised()
    pc "..."
    $ dialouge = renpy.random.choice([
    "Oooh so nice.",
    "Lovely",
    "Mmmmmmm.",
    "Ah so soft."
    ])
    patron "[dialouge]"
    jump pub_waitress_work_cycle1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
