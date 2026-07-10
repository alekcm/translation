label random_event_generic_park_wolf_1:
    "Dog" "Awooooooooooo..."
    pcm "Hmmm, odd. I didn't realise dogs were around any more."
    jump travel

label random_event_generic_park_wolf_2:
    "Dog" "Awooooooooooo..."
    pcm "..."
    pcm "Thought all the dogs were eaten or ran away by now."
    jump travel

label random_event_generic_park_wolf_3:
    "Dog" "Awooooooooooo..."
    pcm "Hmm, seems they are hunting for someone."
    jump travel

label random_event_generic_park_wolf_4:
    show wolfman roar at right1 with hpunch
    "Wolfman" "Woof!"
    $ player.face_shock()
    pc "Ah!"
    $ player.face_annoyed()
    pc "Shoo! Shooo!"
    hide wolfman with dissolve
    pc "..."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
