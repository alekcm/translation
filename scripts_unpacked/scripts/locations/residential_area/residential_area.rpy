label loc_residential_visit:
    pcm "Hmmm..."
    pcm "Everything is run down but that's to be expected I suppose."
    pcm "Doesn't seem too bad otherwise. Seen people living in worse places before the outbreak."
    pcm "Ah, I can see the park [emile.name] was talking about. Not too far from here."
    jump travel_arrival

label loc_office_ll_visit:
    jump oskar_talk_meet_office

label loc_office_ll_closed:
    pcm "Need to come back during the day."
    if loc([loc_office_ll, loc_office_ll_back]):
        $ walk(loc_stairwell)
    jump travel

label loc_shop_corner_arrive:
    if loc_shop_corner.closed():
        pcm "Closed. Sign says \"Open 8 'til 8\"."
        jump travel
    $ walk(loc_shop_corner)
    call screen inventory_itemshop_screen(shop_corner)
    $ walk(loc_residential)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
