label random_event_generic_comments:
    jump expression WeightedChoice([
    ("random_event_generic_comments_cherrypop_taken", If(player.has_perk(perk_cherry_taken), 100, 0)),
    ("random_event_generic_comments_cherrypop_sold", If(player.has_perk(perk_cherry_sold), 100, 0)),

    ("random_event_generic_comments_buttplug", If(player.has_perk(perk_buttplug), 100, 0)),
    ("random_event_generic_comments_slutty", If(player.has_perk(perk_slutty), 100, 0)),

    ("random_event_picker_generic_tombola", 1),
    ])


label random_event_generic_comments_cherrypop_taken:
    pcm "I can't believe my first time was be being forced like that..."
    jump travel

label random_event_generic_comments_cherrypop_sold:
    pcm "I really sold my virginity so easily like that?"
    jump travel

label random_event_generic_comments_buttplug:
    pcm "This plug in my ass is making me hot."
    jump travel

label random_event_generic_comments_slutty:
    pcm "People really can't keep their eyes off me the way I am dressed."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
