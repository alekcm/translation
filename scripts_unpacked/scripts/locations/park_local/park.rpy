label loc_park_visit:
    pcm "Not a bad place. Thought it would be a shithole..."
    jump travel_arrival

label loc_park_explore:
    pcm "This place seems fairly big and looks like an okay place."
    "I take a walk around the park to see if there is anything of interest."
    pcm "Could probably go for a run around the park if I had my sports clothes on. The place is big enough that I wouldn't bother anyone."
    pcm "No more dogs shitting everywhere so can relax on the grass if the weather is nice."
    $ stroll(20)
    jump travel_arrival

label loc_park_path_visit:
    pcm "Hmm, pretty dark down there. Wonder where it goes?"
    jump travel_arrival

label loc_park_gazebo_visit:
    pcm "Ohhh. This place looks nice."
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
