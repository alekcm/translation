init python:
    def wolfgang_can_play():
        if player.has_perk(perk_bitch) and wolfgang_play_location():
            return True
        else:
            return False

    def wolfgang_play_location():
        if dis(dis_park) or loc([loc_walk_park_forest, loc_walk_school_forest, loc_walk_park_shrubs, loc_walk_lake_shrubs]):
            return True
        else:
            return False

    def wolfgang_play_trigger():
        
        
        number = 0
        if t.timeofday == "night":
            number = 85
        elif t.timeofday == "day":
            number = 20
        else:
            number = 50
        return weightgen(number, (100 - number))

    def wolfgang_run_away_location():
        locations = [loc_park, loc_park_toilet, loc_park_path, loc_park_gazebo, loc_park_field]
        remove_from_list(locations, loc_cur)
        walk(random(locations))

label wolfgang_cheat:
    if not wardrobe.qty(item_choker_6):
        "Giving you the choker. Go wear it then go to the park."
        $ wardrobe.take(item_choker_6, all_notif=True)
    else:
        "You already have the choker. Wear it and go to the park."
    jump travel



label wolfgang_action_howl:
    $ player.face_howl()
    pc "Awooooooo!"
    jump random_event_wolfgang_picker

label wolfgang_action_dress_and_leave:
    $ pc_dress_event(tab_top_backup, loc_park_toilet_girls ,loc_residential)
    jump travel

label wolfgang_trigger_intro:
    $ player.face_shock()
    show wolfman roar at right1 with hpunch
    wolf.name "RWAAAAAA!!!"
    pc "Ahhh fuck fuck fuck!"
    show wolfman roar at right5 with hpunch
    "I try to run away from the pervert but trip over my own feet and he gets close to me."
    show wolfman stand with dissolve
    wolf.name "You are new."
    if inv.qty(item_pepperspray):
        "I fumble with the pepper spray I have and prepare to spray him."
    else:
        "I kick at the guy and prepare to run away."
    with vpunch
    wolf.name "Woah. I'm just playing. Calm down please."
    show wolfman at right1 with dissolve
    "He steps back and gives me space."
    wolf.name "You have the collar on. I though you were playing?"
    $ player.face_worried()
    pc "Collar?"
    wolf.name "Yeah, the thing round your neck. You don't know what it is?"
    pc "It looked nice so I wore it."
    wolf.name "Ah. Then good job I got to you first."
    pc "Fuck you weirdo!"
    wolf.name "Haha. Well, yeah. Weirdo is right."
    wolf.name "But see I have the same collar on."
    pc "Errr, yeah. And?"
    wolf.name "Round here we play a game. And that collar shows everyone you are playing."
    pc "Game? What kind?"
    wolf.name "The kind where people like me will chase after you and grab you."
    pc "Then what?"
    wolf.name "Well, make you our bitch."
    pc "Huh?"
    wolf.name "Drag you into the bushes and fuck you."
    pc "Ah, shooo!"
    wolf.name "The collar shows you are part of the game. Don't want to get dragged off then take the collar off."
    wolf.name "Up to you."
    hide wolfman with dissolve
    pcm "Wow. That was weird."
    pcm "This place has some very strange people."
    $ log.assign("Wolfgang bitch")
    $ log.activate("quest_wolfgang_02")
    pcm "I'd better take this thing off or some other weirdo will grab me."
    $ acc.choker = 0
    pcm "There we go."
    jump travel

label wolfgang_first_park_enter_warning:
    if not (player.has_perk([perk_sucu, perk_slut, perk_broken]) or player.check_sex_agree(5)):
        pcm "I am not going in there with this collar on."
        jump travel

    $ add_to_list(quest_wolfgang.list, "warned_pc")
    $ player.face_worried()
    if not quest_wolfgang.active:
        "DEV NOTE It looks like you cheated to get the collar you are wearing."
        "Activating the quest now. There may be bugs for not doing things properly."
        $ log.assign("Wolfgang bitch")
        $ log.activate("quest_wolfgang_02")
    pcm "If I go in there with this collar on, I am agreeing to play their game."
    pcm "I won't have any control over what happens. And it's pretty obvious what will happen."
    pcm "Me getting jumped on and fucked by who knows how many people..."
    jump travel

label random_event_wolfgang_picker:
    if not quest_wolfgang.active:
        if loc(loc_park):

            jump travel
        else:
            jump wolfgang_trigger_intro



    if loc(loc_park_toilet_girls):
        pcm "Phew, think I am safe in here..."
        jump travel

    if wolfgang_play_trigger():
        if c.nude:
            jump random_event_wolfgang_play_tombola
        else:
            if not tab_top == "temp_outfit":
                $ pc_set_temp_outfit()
            jump random_event_wolfgang_strip_tombola
    else:
        jump random_event_wolfgang_safe_tombola


label random_event_wolfgang_safe_tombola:
    jump expression WeightedChoice([
    ("random_event_wolfgang_safe_event_1", 100),
    ("random_event_wolfgang_safe_event_2", 100),
    ("random_event_wolfgang_safe_event_3", 100),
    ("random_event_wolfgang_safe_event_4", 100),
    ])

label random_event_wolfgang_safe_event_1:
    $ player.face_worried()
    pcm "Hmm, no one..."
    jump travel

label random_event_wolfgang_safe_event_2:
    $ player.face_worried()
    distvoice "AWOOOOOOOOOOO!!!!"
    pcm "..."
    jump travel

label random_event_wolfgang_safe_event_3:
    $ player.face_worried()
    pcm "Can't really see, is that someone in the bushes?"
    jump travel

label random_event_wolfgang_safe_event_4:
    pcm "..."
    pcm "Looks like no one is here..."
    jump travel



label random_event_wolfgang_strip_tombola:
    jump expression WeightedChoice([
    ("random_event_wolfgang_strip_event_1", 100),
    ("random_event_wolfgang_strip_event_2", 100),
    ])

label random_event_wolfgang_strip_event_1:
    $ player.grope(strip=True)
    $ player.face_shock()
    pc "Ah!"
    wolf.name "Gotcha!"
    $ player.grope_end()
    pc "Fuck!"
    jump travel

label random_event_wolfgang_strip_event_2:
    $ player.grope(strip=True)
    $ player.face_shock()
    pc "Ah!"
    $ player.spank()
    wolf.name "Haha!"
    $ player.grope(strip=True)
    pc "Aiee!"
    $ player.grope_end()
    pc "Fuck!"
    jump travel

label random_event_wolfgang_play_tombola:
    jump expression WeightedChoice([
    ("random_event_wolfgang_play_event_1", 100),
    ("random_event_wolfgang_play_event_2", 100),
    ("random_event_wolfgang_play_event_3", 100),
    ("random_event_wolfgang_play_event_4", 100),
    ("random_event_wolfgang_play_robin_event_1", If(robin_here(loc_park), 20, 0)),
    ("random_event_wolfgang_play_robin_event_2", If(robin_here(loc_park), 20, 0)),
    ("random_event_wolfgang_play_rachel_event_1", If(rachel_here(loc_park), 20, 0)),
    ("random_event_wolfgang_play_rachel_event_2", If(rachel_here(loc_park), 20, 0)),
    ])

label random_event_wolfgang_play_event_1:
    $ player.grope()
    $ player.face_shock()
    wolf.name "Aha! Got ya!"
    pc "Aie!"
    $ player.grope()
    wolf.name "Good girl."
    wolf.name "Keep running ya bitch!"
    $ player.grope_end()
    with hpunch
    "He shoves me away and gives me a chance to run away."
    $ wolfgang_run_away_location()
    jump travel

label random_event_wolfgang_play_event_2:
    $ player.face_shock()
    show wolfman roar at right4 with vpunch
    wolf.name "Wraaaaa!!"
    hide wolfman
    $ wolfgang_run_away_location()
    "I run away quickly before I can be grabbed."
    jump travel

label random_event_wolfgang_play_event_3:
    $ player.face_worried()
    pcm "Fuck, I can see them sneaking around in the bushes."
    jump travel

label random_event_wolfgang_play_event_4:
    jump action_wolfpack_grabbed

label random_event_wolfgang_play_robin_event_1:
    show robin happy at right1 with hpunch
    robin.name "Run away!!"
    hide robin with vpunch
    jump travel

label random_event_wolfgang_play_robin_event_2:
    pcm "Ah, is that [robin.name]?"
    show robin_bitching_1 with dissolve
    pcm "Looks like she got caught."
    pcm "Have fun."
    hide robin_bitching_1 with dissolve
    jump travel

label random_event_wolfgang_play_rachel_event_1:
    show rachel evil at right1 with hpunch
    rachel.name "Where are you naked bastards?!"
    show rachel happy
    rachel.name "Oh, hi [name]!"
    hide rachel with vpunch
    pcm "Okay..."
    jump travel

label random_event_wolfgang_play_rachel_event_2:
    rachel.name "Ah!"
    pc "Huh?"
    show rachel_bitching_1 with dissolve
    pcm "Looks like she got caught."
    pcm "Have fun."
    hide rachel_bitching_1 with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
