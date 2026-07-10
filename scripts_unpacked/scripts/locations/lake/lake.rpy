label loc_lake_visit:
    if t.month == "Winter":
        pc "Looks like it would be lovely in the Summer. I had better stay out the water for now though unless I want my tits getting frozen off."
    else:
        pc "This place looks lovely. Looks like I can sunbathe or play in the water."
    jump travel_arrival

label loc_boardwalk_visit:
    pcm "Wow, there is actually stuff here. Thought it would be abandoned."
    pcm "Some kiosks and other bits. I should see what they do."
    jump travel_arrival

label loc_beach_gym_visit:
    if people_beach_vball():
        pcm "Oooh, girls are playing volleyball. Wonder if I can join."
        if mateo_here() or kaan_here():
            $ player.face_annoyed()
            if mateo.has_met or kaan.has_met:
                pcm "Those two just watching, what a shocker..."
            else:
                pcm "Some guys perving on them though..."
    else:
        pcm "Oooh, a volleyball net. Wonder if people play."
    jump travel_arrival

label loc_beach_rocks_visit:
    pcm "Pretty secluded here."
    pcm "Wonder why there are all these boats. Don't tell me people try to get across the water from here."
    $ player.face_worried()
    pcm "Probably even more at the bottom of the lake..."
    jump travel_arrival

label loc_beach_bikinicheck:
    if not "swim" in tab_top:
        pcm "I should change into my beachwear or I'll get sand everywhere."
        jump travel
    else:
        $ travel_walk(loc_beach, 2, True)

label loc_boardwalk_game_kiosk:
    "Here there will be some kind of game kiosk. a pay for mood boost button basically."
    $ player.add_mood(15)
    $ player.add_money(-200)
    $ working(30)
    jump travel_arrival

label loc_pier_relax:
    "I sit at the edge of the pier and just stare out into the water and the waves coming in and out."
    $ dialouge = renpy.random.choice([
    "Hmmm, I wonder if there are people living over there. Can only see trees and hills but maybe people live in the forest.",
    "The lake surrounds half of the city. I wonder if that was one of the reasons this place managed to wall itself off? A lot of natural barriers.",
    "World has turned to shit, but nature always manages to look beautiful. I could sit all day just looking at the rippling water.",
    "So blue and clean. Nothing like the river in the city which is basically sewage water. Was it always this clean or did everyone dying stop the pollution?",
    "The hills over the lake look lovely. Wonder what's over there? I don't really know anything about the area outside of the city.",
    "Ooh, there are fish? The water is so clear that it's easy to see them. Shame they are far too small to eat.",
    "Strange to see something so lovely in this shithole... Probably because it's got nothing to do with people and is natures beauty.",
    "Actually wonder why this pier hasn't been torn apart for firewood by now. Glad it hasn't since it's nice to relax here."
    ])
    pcm "[dialouge]"
    $ loiter()
    $ show_activity_image("relax")
    "I decide to get up and go about my day."
    jump travel_arrival

label loc_beach_relax:
    $ renpy.show(renpy.random.choice(["activity_beach_lay", "sb_onbelly up"]))
    with dissolve
    "I go and sit in the sand and just relax while looking around."
    $ dialouge = renpy.random.choice([
    "Can almost believe the world hasn't gone to shit while sitting here and watching people relaxing and enjoying the beach.",
    "The lake surrounds half of the city. I wonder if that was one of the reasons this place managed to wall itself off? A lot of natural barriers.",
    "World has turned to shit, but nature always manages to look beautiful. I could sit all day just looking at the rippling water.",
    "People still run around here like life is all normal. I guess it's a better escape than drowning in a bottle.",
    "The hills over the lake look lovely. Wonder what's over there? I don't really know anything about the area outside of the city.",
    "Kinda surprised at the girls walking around in tiny bikinis. Almost makes it easy to ignore that there are shitty fucks looking to rape us the moment we are alone.",
    "Strange to see something so lovely in this shithole... Probably because it's got nothing to do with people and is natures beauty.",
    "Nice to see people acting all happy. Good way to think for a moment that the world is actually normal."
    ])
    pcm "[dialouge]"
    $ loiter()
    $ show_activity_image("sunbathe")
    $ renpy.scene()
    with dissolve
    "I get off, brush the sand off my ass and go about my day."
    jump travel_arrival

label loc_vball_relax:
    "I hang around and just watch the girls playing volleyball to kill some time."
    $ dialouge = renpy.random.choice([
    "They are actually quite good. Wonder if they used to play before everything went to shit?",
    "Oooh, that was close. Almost lost but that one managed to save her team.",
    "Oh wow, they are really going at each other. They are all quite good at this.",
    "Oh! Great save!",
    "Ooh, even the perverts stopped looking at their asses to watch that rally. Fuck it was close.",
    "Yes! Ooh no! Saved! Fuck this is intense!",
    ])
    pcm "[dialouge]"
    $ loiter()
    $ show_activity_image("relax")
    "The match comes to a close so I carry on with my day."
    jump travel_arrival

label loc_fire_relax:
    if t.hour_from_to(20,3):
        "I sit down by the fire and relax with others doing the same."
    elif t.hour_from_to(17,3):
        "I sit down in the firepit with the others and relax."
    else:
        "I relax around the firepit to kill some time."
    $ dialouge = renpy.random.choice([
    "I wonder who dug this out?",
    "Be nice to relax here with some beers.",
    "Pretty nice here. Wonder if it ever gets flooded?",
    "Good to just sit and take my mind off things for a while.",
    "Mmm, might have to come here with some beers or something next time.",
    ])
    pcm "[dialouge]"
    $ loiter()
    $ show_activity_image("relax")
    "Eventually I hop out of the firepit and go about my day."
    jump travel_arrival








label loc_beach_workout:
    "If no one is playing vball, you can practice on your own."
    $ exercise(60)
    jump travel_arrival

label loc_pier_jetty_jump:
    if not ("swim" in tab_top or c.nude or c.underwear):
        pcm "Not a good idea to jump in these clothes. Should undress or wear my swimsuit."
        if player.has_perk(perk_exhibitionist, notif=True):
            menu:
                "Strip off here":
                    pcm "Well, why not?"
                    $ pc_striptease(True)
                "Better not":

                    pcm "Maybe another time..."
                    jump travel
        else:
            jump travel

    elif player.check_nowill():
        pcm "Err, no way! Too scary..."
        jump travel
    $ player.face_happy()
    pcm "Here goes..."
    with hpunch
    show screen blackout() with Dissolve(0.1)
    $ walk(loc_beach_water, trans=False)
    $ loc_from = loc_beach_pier
    $ player.add_mood(25)
    if c.nude and player.has_perk(perk_exhibitionist):
        $ player.add_mood(15)
    $ player.face_excited()
    hide screen blackout with Dissolve(0.1)
    pc "Haaaa Whoooo!"
    $ player.face_happy()
    pc "Phew..."
    pc "That was scary."
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
