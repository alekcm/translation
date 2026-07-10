label loc_highway_visit:
    pcm "Nothing of much interest here. Long road that is mostly blocked off..."
    pcm "Under the overpass... What is that?"
    pcm "A shanty town of sorts. Fuck, should be careful round here."
    if log.interactive("quest_homeless_start_01"):
        pcm "I don't see [emile.name] around. Most of the girls here are barely dressed so would be easy to spot her."
    jump travel

label loc_highway_slum_visit:
    $ player.face_worried()
    pcm "Err..."
    pcm "This place is worse up close..."
    pcm "I can't imagine this place is very safe. I need to be careful."
    if log.interactive("quest_homeless_start_01"):
        pcm "Might be a good place for [emile.name] to hide though."



    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
