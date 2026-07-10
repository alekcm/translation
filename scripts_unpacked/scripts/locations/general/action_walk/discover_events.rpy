



label loc_walk_rails_discover:
    pcm "It looks like things go down further past those trains..."
    pcm "I wonder what's back there? Might be able to get more junk to sell."
    $ loc_walk_junk_rails.locked=False
    jump travel

label loc_walk_junk_rails_visit:
    pcm "Hmmm, the rails are blocked ahead but looks like people travel through this pipe..."
    pcm "Fuck. I'm gonna get murdered if I go down there. Or fall and break my head."
    pc "Ugh!"
    $ loc_walk_slum_pipe.locked=False
    jump travel

label loc_walk_slum_pipe_visit:
    pcm "Oh, I can see ahead. It comes out into the slums."
    pcm "Well, that's good I guess."
    pcm "Other than the slums being a shithole..."
    jump travel





label loc_walk_park_forest_discover:
    pcm "I think there is some kind of dirt path down there..."
    pcm "Looks like people walk there. I wonder where it goes?"
    $ loc_walk_park_forest.locked=False
    jump travel

label loc_walk_park_forest_visit:
    pcm "Hmm, it is a path of some kind. Seems to go on for a while."
    pcm "I wonder where it goes?"
    $ loc_walk_school_forest.locked=False
    jump travel

label loc_walk_school_forest_visit:
    pcm "Ah, this is near the school. I can see it from here."
    $ loc_school_secret_entrance.locked=False
    jump travel

label loc_school_secret_entrance_visit:
    $ loc_school_secret_entrance.visited = True
    $ loc_school_field.opening_hours = []
    $ loc_school_field_back.opening_hours = []
    $ loc_school_locker_old.opening_hours = []
    if school_soccer_quest_backentrance["shown"]:
        $ school_soccer_quest_backentrance["used"] = True
        pcm "Hmm, in the bushes there is a hole..."
        pcm "Let's see..."
        $ player.face_happy()
        pcm "Ah, yes! There we go."
        $ player.face_worried()
        pcm "Err..."
        pcm "That's a pretty small hole."
    else:

        pcm "There is the school. The field is just on the other side of these bushes."
        pcm "Hmmm, looks like someone has made a hole in the fence."
        pcm "I can probably climb through there and get inside the school when it's closed."
        $ player.face_worried()
        pcm "It is pretty small though..."

    if havenvent.vsex > 0:
        show haven_vent shortsoff giveup tears man at right2 with dissolve
        pcm "..."
        $ player.face_angry()
        hide haven_vent with dissolve
        pcm "I swear, if something like that happens again I am going to make it my life's work to chop off and collect as many penises as possible!"
        pc "*Sigh*"

    $ player.face_neutral()
    pcm "Well, might as well give it a go."
    pc "Hup!"
    with vpunch
    $ player.face_pain()
    pc "Ung!"
    with vpunch
    $ walk(loc_school_field, trans=hpunch)
    if c.skirt and c.bottom:
        $ c.bottom = 0
        $ player.face_confused()
        pcm "There we..."
        $ player.face_annoyed()
        pc "Ah fuck!"
        pcm "Snagged on the fence."
        $ pc_dress()
        pc "*Sigh*"
        $ player.face_neutral()
    jump travel





label loc_walk_park_lake_discover:
    pcm "Hmm, is there some path back there?"
    pcm "Looks like lots of bushes, but some way between them all."
    $ loc_walk_park_shrubs.locked=False
    jump travel

label loc_walk_park_shrubs_visit:
    pcm "Looks like people hang out here. I wonder what's ahead."
    $ loc_walk_lake_shrubs.locked=False
    jump travel

label loc_walk_lake_shrubs_visit:
    pcm "Ah, Looks like this heads to the lake. I can hear the water."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
