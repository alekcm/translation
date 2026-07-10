label random_event_bus_normal:
    jump expression WeightedChoice([
    ("random_event_bus_normal_1", 100),
    ("random_event_bus_normal_2", 100),
    ("random_event_bus_normal_3", 100),
    ])

label random_event_bus_normal_1:
    "I stand there holding the bar as the bus rocks back and forth."
    jump bus_travel_end

label random_event_bus_normal_2:
    "I look out the window as the town passes me by."
    jump bus_travel_end

label random_event_bus_normal_3:
    "I pick a spot on the bus and just stare at it, making sure to avoid eye contact and not draw any unwanted attention."
    jump bus_travel_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
