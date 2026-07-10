label random_event_generic_rent:
    jump expression WeightedChoice([
    ("random_event_generic_rent_1", 100),
    ("random_event_generic_rent_2", If (player.cash >= rent_total_owed(), 100, 0)),
    ("random_event_generic_rent_3", If (player.cash < rent_total_owed(), 100, 0)),
    ("random_event_generic_rent_4", If (quest_rent.sold and player.cash < rent_total_owed(), 100, 0)),
    ("random_event_generic_rent_5", 100),
    ])

label random_event_generic_rent_1:
    pcm "I should probably see [oskar.name] at some point to pay the rent."
    jump travel

label random_event_generic_rent_2:
    pcm "I have money to pay the rent, I should see [oskar.name] about it at some point."
    jump travel

label random_event_generic_rent_3:
    pcm "Rent needs to be paid and I don't have enough. I really need to get some cash."
    jump travel

label random_event_generic_rent_4:
    pcm "Unless I plan on paying with my arse again, I really should get some money to pay [oskar.name]."
    jump travel

label random_event_generic_rent_5:
    pcm "Ugh, I need to pay the rent at some point."
    jump travel

label random_event_generic_newhome:
    jump expression WeightedChoice([
    ("random_event_generic_newhome_1", 100),
    ("random_event_generic_newhome_2", 100),
    ("random_event_generic_newhome_3", 100),
    ("random_event_generic_newhome_4", 100),
    ("random_event_generic_newhome_5", 100),
    ])

label random_event_generic_newhome_1:
    pcm "I don't have anywhere to stay any more..."
    pcm "People always talk about going to live at the highway. Maybe I should take a look."
    jump travel

label random_event_generic_newhome_2:
    pcm "Couldn't keep up payments for rent. Maybe I should check out the slum for something cheap."
    jump travel

label random_event_generic_newhome_3:
    pcm "Living in the slum would be better than being homeless. I should check the place out."
    jump travel

label random_event_generic_newhome_4:
    pcm "Ugh, I really should look for somewhere to stay."
    pcm "Since I couldn't afford anywhere good, maybe I should check out the slums."
    jump travel

label random_event_generic_newhome_5:
    pcm "I could stay at the motel for now. But I really need somewhere more permanent."
    pcm "I wonder if there is somewhere like that nearby the motel area?"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
