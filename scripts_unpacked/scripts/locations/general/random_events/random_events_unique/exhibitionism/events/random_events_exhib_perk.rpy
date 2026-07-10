

label random_event_generic_exhib_perk_1:

    $ c.pants = 0
    jump travel

label random_event_generic_exhib_perk_2:

    $ c.bra = 0
    jump travel

label random_event_generic_exhib_perk_3:
    $ c.top = 0
    $ player.face_happy()
    $ player.uncover()
    pc "Haha!"
    pc "Oops..."
    $ pc_dress()
    jump travel

label random_event_generic_exhib_perk_4:
    $ c.bottom = 0
    $ player.face_happy()
    $ player.uncover()
    pc "Haha!"
    pc "Oops..."
    $ pc_dress()
    jump travel

label random_event_generic_exhib_perk_5:
    if pc_remove_clothes_exhibitionist():
        $ player.face_happy()
        $ player.uncover()
        pc "Oops..."
        pc "How did that happen?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
