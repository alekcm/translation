label random_event_generic_exhib_academy:
    $ exhib_stat_changes()

    jump expression WeightedChoice([
    ("random_event_generic_exhib_academy_1", 100),
    ("random_event_generic_exhib_academy_2", 100),
    ("random_event_generic_exhib_academy_3", If(shane.alive and not school_bully_quest_bully_cass_target, 100, 0)),
    ])

label random_event_generic_exhib_academy_1:
    $ player.cover()
    $ player.face_worried()
    pcm "Shit, I can't be walking around the academy like this."
    jump travel

label random_event_generic_exhib_academy_2:
    $ player.cover()
    $ player.face_worried()
    pcm "There are so many people here, I can't be walking around here like this."
    jump travel

label random_event_generic_exhib_academy_3:
    $ player.cover()
    $ player.face_worried()
    call school_bully_bully_event_isolate from _call_school_bully_bully_event_isolate_13

    $ tempname = school_pick_bully_lust()

    call school_bully_bully_event_force_strip from _call_school_bully_bully_event_force_strip_5

    jump school_bully_sex_forced_blow
    jump travel

label random_event_generic_exhib_park:
    $ exhib_stat_changes()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_park_1", 100),
    ("random_event_generic_exhib_park_2", 100),
    ])

label random_event_generic_exhib_park_1:
    $ player.uncover()
    pcm "Kinda fun to run around the park like this. No one can see me."
    jump travel

label random_event_generic_exhib_park_2:
    $ player.uncover()
    pcm "Easier here to have some naked fun. If anyone comes I can hide in the bushes."
    jump travel

label random_event_generic_exhib_highway:
    $ exhib_stat_changes()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_highway_1", 100),
    ("random_event_generic_exhib_highway_2", 100),
    ])

label random_event_generic_exhib_highway_1:
    $ player.uncover()
    pcm "No one really cares I am naked around here since I just look like a whore."
    jump travel

label random_event_generic_exhib_highway_2:
    $ player.uncover()
    pcm "With the whores everywhere, it doesn't really stand out being naked or showing off around here."
    jump travel

label random_event_generic_exhib_pub:
    $ exhib_stat_changes()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_pub_1", 100),
    ("random_event_generic_exhib_pub_2", 100),
    ])

label random_event_generic_exhib_pub_1:
    pcm "Showing off in the pub with all these drunk perverts is going to get me into trouble."
    jump travel

label random_event_generic_exhib_pub_2:
    pcm "In the pub like this? I'm sure the drunks are enjoying but it wont be long until one of them goes to far."
    jump travel

label random_event_generic_exhib_hospital:
    pc "I shouldn't hang out here too much like this. Someone important might see me."
    jump travel

label random_event_generic_exhib_junk:
    $ exhib_stat_changes()
    jump expression WeightedChoice([
    ("random_event_generic_exhib_junk_1", 100),
    ("random_event_generic_exhib_junk_2", 100),
    ("random_event_generic_exhib_junk_3", If(c.nude, 100, 0)),
    ])

label random_event_generic_exhib_junk_1:
    pcm "Hmm, I bet [jaylee.name] wouldn't mind seeing me like this."
    jump travel

label random_event_generic_exhib_junk_2:
    pcm "[jaylee.name]'s eyes might pop out her skull if she comes across me like this."
    jump travel

label random_event_generic_exhib_junk_3:
    pcm "Butt naked in the junk yard. Perfect recipe for [jaylee.name] to find my raped corpse."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
