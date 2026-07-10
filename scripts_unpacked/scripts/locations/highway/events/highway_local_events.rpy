label highway_local_event_tombola:




label highway_local_event_passout:

    pc "I really need to have a lay down, I am almost falling alseep on my feet"
    scene bg_highway_local
    if unlocked_highway_homeless == True:
        "You go under the bridge where the local homeless sleep and look for a spot to lay down"
    else:
        "You go and lay down in one of the ditches just off the highway."

    scene bg_black with dissolve
    hide screen pc_avatar with dissolve
    pause 1
    $ t.hour = 3
    $ randomnum = renpy.random.randint(10, 40)
    $ t.minute = randomnum
    $ player.add_mood -= 40
    $ player.add_tired(30)
    scene bg_highway_local with dissolve
    show screen pc_avatar with dissolve
    "You wake up in the alley you fell asleep in. You might find yourself robbed, raped oe kidnapped."
    pc "Ugh! Lets not do that again please."
    $ outside = True
    $ loc_fromfrom = loc_from
    $ loc_from = loc_to
    $ walk(loc_highway)
    $ go_sleep_prompt = False
    jump highway_local_screen

label highway_local_event_meet_homeless:
    $ unlocked_highway_homeless = True
    scene bg_highway_local
    "As you arrive near the highway, you notice the light of a fire under the overpass."
    pc "I wonder what that is? It doesn't look like an out of control fire."
    "As you start getting closer to the highway it becomes easier to see what is happening."
    pc "Ahh, homeless people. This must be where the local homeless are forced to live and they are huddling by a small fire to keep warm."
    jump highway_local_screen

label highway_local_event_meet_hookers:
    $ unlocked_highway_hookers = True
    if loc_to == "highway_local":
        scene bg_highway_local
        "As you arrive to the highway, you notice some women talking to one of the truck drivers across the road."
        pc "Hmm, pretty sure they are prostitutes."
        if player.inhibition <70:
            pc "Good place for them to look for customers I suppose. It's near a truck stop and close to a motel so they probably dont have much trouble finding customers."
            if player.inhibition < 50:
                pc "I wonder what kind of money they make."
            jump highway_local_screen
        else:
            pc "Better stay away else the truckers might think I am a hooker as well."
            jump highway_local_screen
    elif loc_to == "highway_local_motel":
        scene bg_highway_local_motel
        "As you arrive to the motel, you notice a middle aged man heading into a room with a woman who is dressed like a hooker."
        if player.inhibition < 70:
            pc "So there are prostitutes that work here. I knew this place was a rat hole but I should make sure if I stay here I should avoid touching anything."
            jump highway_local_motel_screen
        else:
            pc "That girl was way too young to be his girlfriend..."
            jump highway_local_motel_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
