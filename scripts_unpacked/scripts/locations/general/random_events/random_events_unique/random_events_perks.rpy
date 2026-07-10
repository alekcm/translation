label random_event_perk_bimbo:
    $ player.face_worried()
    pcm "I haven't really been studying or working on my brain at all recently have I?"
    pcm "Bah, who needs to?"
    $ player.face_happy()
    pcm "Just as long as I am happy, I don't need smarts."
    $ player.add_mood(30)
    $ player.add_perk(perk_bimbo, notif=True)
    jump travel

label random_event_perk_commando:
    $ player.face_worried()
    pcm "Been spending most of my time without any underwear. Is that such a bad thing?"
    pcm "..."
    pcm "No. No it's not. I like the freedom and bras are annoying."
    $ player.add_mood(30)
    $ player.add_perk(perk_commando, notif=True)
    jump travel

label random_event_perk_loose_commando:
    pcm "Kinda getting used to wearing underwear now."
    pcm "I guess it's not so bad."
    $ player.remove_perk(perk_commando, notif=True)
    jump travel

label random_event_commando_underwear:
    $ player.face_annoyed()
    $ dialogue = WeightedChoice([
    ("Ugh, do I really need to be wearing underwear?", 1),
    ("*Tsk* My pant's are getting all twisted around...", 1),
    ("Why do I need to be wearing pants like these?", 1),
    ("Ugh, these pants are getting stuck in places they shouldn't.", 1),
    ])
    pcm "[dialogue]"
    $ player.add_mood(-3)
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
