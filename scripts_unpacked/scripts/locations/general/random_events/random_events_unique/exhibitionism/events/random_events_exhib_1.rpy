label random_event_generic_exhib_1_1:
    pcm "I should probably look for something to cover up."
    jump travel

label random_event_generic_exhib_1_2:
    pcm "Naked again? I should probably try and find some clothes."
    jump travel

label random_event_generic_exhib_1_3:
    $ player.face_shy()
    pcm "People can probably see me if I go around naked like this."
    jump travel

label random_event_generic_exhib_1_4:
    $ player.face_shy()
    pcm "Maybe hiding somewhere until it's dark is a good idea?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
