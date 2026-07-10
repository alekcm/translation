label flatmate_cheat:
    "***Huge spoilers***"
    "This cheat will move your location and change the time of day. It may break your game if you are somewhere like Haven."
    "Last chance to roll back."
    show charlie at right1
    show jason at right3
    show robin at right5
    with dissolve
    "These are the current flatmates. Charlie on the right and Robin on the left and Jason in the middle"
    show emile at right4 with dissolve
    "And you should all know Emile."
    "And we have the landlord..."
    show oskar at right2 with dissolve
    "More about these two later"
    hide emile
    hide oskar
    with dissolve
    "They will be met mostly in your flat..."
    $ walk(loc_common)
    "And most of the interaction will be here with them."
    "You will see them hanging around and be able to talk to them while at home."
    $ walk(loc_school_hallway)
    $ time_advance_to(10,0)
    if not t.wkday in weekdays:
        $ t.day = 2
    "But you will also be able to interact with them in school."
    $ walk(loc_park, time_amount=360)
    "Rarely you might see them out and about..."
    "Notice the change of clothes, this is a new system for NPCs I am testing out where clothes are based on the location."
    "As well as the weather..."
    $ weather_var = 1
    "Sunny"
    $ weather_var = 3
    "Rain"
    $ walk(loc_stairwell)
    "Inside."
    $ walk(loc_common)
    "At home during the day"
    $ time_advance_to(22,0)
    "Home at night..."
    $ walk(loc_beach_rocks, time_amount=600, outfit_block=True)
    "The beach..."
    "(Note, if nothing changed for that area or weather, just means I haven't added it yet or there is no need such as emile's lacking a school uniform.)"
    $ walk(loc_common)
    "Personality stuff."
    hide charlie
    hide robin
    hide jason
    with dissolve
    show emile with dissolve
    "We already know a lot about Emile since she has been in since the start of the game. So I won't speak more about her."
    hide emile
    show robin at right3
    with dissolve
    "Robin is a tomboy. That does not mean she is a cross dresser, wants to be a man or is a reverse trap."
    show robin happy
    robin.name "Hi!"
    "She is someone who is entirely female but lacks many of the things many would consider female attributes."
    show robin neutral
    "She is very sporty and will probably end up friendly with the soccer boys or end up at the beach playing volleyball."
    "While she is not lesbian, this is a porn game and most players will want to be able to have sex with her, so romance will be possible."
    show robin nude with dissolve
    "And yes, she is female."
    hide robin
    show charlie at right3
    with dissolve
    "This is Charlie. He will mostly be a somewhat cheerful and friendly, but also a reserved flatmate. You will later find out why..."
    show charlie dress with dissolve
    "Given his features and the state of the world, he has taken to dressing up and entertaining men for money."
    "He is not trans, gender dysmorphic or other such things. Just a guy using what he has to earn a living in the world."
    "Doesn't mean he doesn't have fun with his female persona though..."
    show charlie nude with dissolve
    "And yes, is a guy."
    hide charlie with dissolve
    show jason with dissolve
    "This is Jason. He will be very reserved and seemingly anti social. It will be quite hard to get to know him as there won't be many opportunities to talk to him"
    $ walk(loc_school_library)
    "But you can probably meet with him after school in the library."
    "Depending on how things go, he might be here with a couple of equally anti social friends. We will so if I have time to add them in though."
    hide jason with dissolve
    $ walk(loc_common)
    show oskar with dissolve
    "And finally, the landlord."
    "Sammy and the other flatmates will need to pay him rent every week or face consequences."
    "There is planned to be a job available much like the pub job but much more lewd that sammy, robin or emile can work if they are behind on rent"
    "It will not be a very pleasant job for them so will only be worked if you are a bit desperate for money or cant pay rent"
    $ walk(loc_bedroom)
    $ pc_strip()
    "This job will come in a slightly later update (jobs update) though, so for the next update it will likely just be sex tasks."
    $ renpy.scene()
    with dissolve
    "** EVEN BIGGER SPOILERS AHEAD **"
    menu:
        "See the spoilers":
            $ NullAction()
        "Dont see the spoilers":

            jump travel
    show robin at right1 with dissolve
    "Robin has had some of her story already written and it is somewhat playable at the time of writing."
    "As you talk to her more, she will inadvertently reveal more info about her deviant sexual preferences."
    "She will eventually ask you to ask the soccer boys to have sex with her."
    "She will reveal that she kind of got off on being touched on the bus and will eventually go out on journeys alone or with Sammy."
    show robin_bus_grope_behind grope with dissolve
    "..."
    hide robin_bus_grope_behind
    show robin_bus_grope_front
    with dissolve
    "..."
    hide robin_bus_grope_front
    show robin_bus_sex
    with dissolve
    "She has a lot of fun on the bus."
    hide robin_bus_sex
    with dissolve
    "She will also turn up to the bar where you work because she gets off watching Sammy \"entertain\" people in the pub."
    "Seems she likes watching people have fun..."
    "Later on she will want to join in on the fun."
    show robin bimbo with dissolve
    "..."
    show robin slut with dissolve
    "She also asks you to dress her up to look \"fuckable\". Sammy makes an attempt but kind of overdoes it. Robin seems happy though."
    show robin_bimbo_pose_front with dissolve
    "..."
    show robin_bimbo_pose_front slut with dissolve
    "..."
    hide robin_bimbo_pose_front
    show robin_bimbo_pose_back with dissolve
    "..."
    show robin_bimbo_pose_back slut with dissolve
    "There will be events where Sammy and slutty robin head out and hunt for men together."
    $ renpy.scene()
    show charlie at right with dissolve
    "Charlies story is somewhat planned but may go in a few different directions. I am not sold on the idea yet and will decide as I am writing."
    show charlie dress with dissolve
    "His starting story will be about him being a whore and coming to terms with it. This will bring Sammy and him closer together."
    show jason at right2 with dissolve
    "Running parallel will be the Jason storyline. He will be presented as a typical outcast type. Incel vibes and probably a yandere."
    "Sammy can react in a couple of ways but most first time players will probably be fairly hostile towards him due to the way he will be introduced and presented."
    "Eventually you and charlie will talk about how he is stealing your underwear and doing other creepy as shit things."
    "The story will start to get a bit hostile and take a turn in bad directions."
    "Here is where things may go differently depending on how I am feeling as I am writing, but my current pencilled in draft is..."
    "It is finally discovered that charlie is the crazy yandere and is totally in love with Sammy. This will culminate into the kidnapping of Sammy."
    "Weird outcast flatmate Jason actually had no idea what was going on due to his complete social ineptitude. He might help save Sammy or something, I am not sure yet."
    "We will see how this goes."
    $ renpy.scene()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
