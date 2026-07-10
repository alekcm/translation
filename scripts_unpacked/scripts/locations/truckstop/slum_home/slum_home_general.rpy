label slum_home_find:
    pcm "Hmm, some shithole places here. I wonder if there is somewhere to stay..."
    pcm "Suppose I should have a look around and see if I can see anything."
    pcm "Hmm, I suppose I could look up there... Seems pretty high. Might be something."
    pcm "No idea how to get up there though. Guess I will look around."
    $ walk(loc_highway_slum_street)
    pcm "Anything around here?"
    if loc_highway_slum_still.visited:
        pcm "Got the booze place in there so no point going in there to check."
    else:
        pcm "Quite a few doors, this place has a sign on the front advertising booze, so probably occupied."
    pcm "Doors... Doors... A window..."
    pcm "Hmm, this door is open."
    $ walk(loc_highway_slum_home)
    pc "Err, hello."
    pc "Anyone here?"
    pcm "Looks empty. Lot's of dust everywhere."
    pcm "Doesn't look like people would bother to clean a place like this. But the dust has settled for quite some time."
    pcm "So don't think anyone has been here for ages."
    $ walk(loc_highway_slum_street)
    pcm "Hmm, maybe I should ask around."

    if loc_highway_slum_still.visited and loc_highway_slum_still.open():

        pcm "Maybe should ask the booze guy."
        $ walk(loc_highway_slum_still)
        pc "Err, hey. Can I ask something."
        show haven_viktor at right1 with dissolve
        havenvik.name "Yes we wash all the bottles. Usually with soap."
        pc "Err, good to know. I'm looking for somewhere to stay and saw and empty place over there."
        havenvik.name "The one across from here?"
        pc "Yeah."
        havenvik.name "Last girl living there took too much and left a corpse. Place is free."
        pc "Oh, good. Well, not good. Yeah..."
        pc "So is there something I should know? Like is there someone who runs the place or something?"
        havenvik.name "You think we live in the fancy part?"
        havenvik.name "Place is free, go live there. Lock your door if you can."
        havenvik.name "Pretty girl like you will get visitors if you don't keep your head down."
        havenvik.name "Best not to fight. Only ones who turn into a corpse are the ones who fight."
        pc "Right..."
        pc "Thanks."
        hide haven_viktor with dissolve
        $ walk(loc_highway_slum_street)
        pcm "Shithole like this, I guess that's to be expected."
        pcm "Fuck..."
    elif t.hour in irange(8,20):

        $ walk(loc_highway_slum)
        pcm "That is one of the slum gang guards. Maybe I can ask him."
        pc "Err hey. Do you know anything about the houses here?"
        show haven_guard1 at right1 with dissolve
        havengateguard.name "What you wanna know?"
        pc "I saw an empty place over there and I need somewhere to stay. I was wondering how things work."
        havengateguard.name "They don't work. Place is empty and you want it, it's yours now."
        pc "Just like that?"
        havengateguard.name "Until a punter kills you and it's empty again. Or someone stronger than you wants it, yes."
        pc "Right..."
        pc "Thanks."
        hide haven_guard1 with dissolve
        pcm "So it's like that is it?"
        $ walk(loc_highway_slum_street)
        pcm "Better be careful. Lock the door if I can."
    else:

        $ walk(loc_highway_slum)
        pcm "That is one of the slum gang guards. Maybe I can ask him."
        pc "Err hey. Do you know anything about the houses here?"
        show haven_guard2 at right1 with dissolve
        havenmeanguard.name "What?"
        pc "Err, I am looking for a place to stay and I saw an empty place."
        havenmeanguard.name "So? If it's empty, it's yours now."
        pc "Just like that?"
        havenmeanguard.name "Until someone comes and fucks you dead and we gotta drag your whore arse out of it, yes."
        pc "Right... Thanks."
        hide haven_guard2 with dissolve
        pcm "So it's like that is it?"
        $ walk(loc_highway_slum_street)
        pcm "Better be careful. Lock the door if I can."

    $ walk(loc_highway_slum_home)
    pcm "Well then. Home sweet home I guess..."
    $ loc_highway_slum_home.locked = False
    if log.interactive("quest_homeless_start_02"):
        $ log.markdone("quest_homeless_start_02")
    if log.interactive("quest_homeless_01"):
        $ log.markdone("quest_homeless_01")
    jump travel



label bed_sleep_slum_wake_1:
    $ player.add_mood(-10)
    $ player.inhib_sleep()
    $ player.face_shock()
    hide screen blackout with hpunch
    pcm "What the fuck?"
    pcm "Was that the door?"
    $ player.face_annoyed()
    with vpunch
    pc "Fuck off! Occupied!"
    pc "..."
    pcm "Ugh, idiots."
    jump travel

label bed_sleep_slum_wake_2:
    $ player.add_mood(-10)
    $ player.inhib_sleep()
    $ player.face_shock()
    hide screen blackout with hpunch
    pcm "What the fuck?"
    "Neighbour" "Yes fuck me! Ahh yes!"
    $ player.face_annoyed()
    pcm "Ugh..."
    jump travel

label bed_sleep_slum_wake_3:
    $ player.add_mood(-10)
    $ player.inhib_sleep()
    $ player.face_shock()
    hide screen blackout with hpunch
    pcm "Huh? What was that?"
    $ player.face_annoyed()
    pcm "..."
    pcm "Hopefully nothing..."
    jump travel

label bed_sleep_slum_wake_4:
    $ player.add_mood(-10)
    $ player.inhib_sleep()
    $ player.face_shock()
    hide screen blackout with hpunch
    pcm "Huh? What was that?"
    "Voice" "You taking customers?"
    $ player.face_annoyed()
    if not player.iswhore:
        pc "No! Wrong place!"
        pcm "..."
        jump travel

    pcm "Ugh, can't even sleep properly..."
    menu:
        "Let him in":
            "I head over to the door and open it."
            $ male_npc_create_all()
            $ tempname = punter
            $ player.set_whore_price(0)
            pc "Come in."
            show male_generic at right5 with dissolve
            tempname.name "Cheers luv."
            jump whore_sex_start
        "Send him away":

            pc "No! Wrong place!"
            pcm "..."
            jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
