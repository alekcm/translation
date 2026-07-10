label loc_park_loiter:
    if weather_var == 3:
        "It's pissing rain so I just hide under a tree to stay dry while killing some time."
        jump loc_park_loiter_walk_end
    show activity_walk with dissolve
    if numgen() and not weather_var > 1:
        $ dialouge = renpy.random.choice([
        "I decide to take it easy in the park for a bit.",
        "I look for a nice spot on the grass to sit down.",
        "I look for an empty bench to sit down on.",
        "I look for a quiet spot in the park to relax."
        ])
        "[dialouge]"
        $ rand_choice = WeightedChoice([
        ("loc_park_loiter_relax_normal", 300),
        ("loc_park_loiter_relax_desire", player.check_horny()),
        ("loc_park_loiter_relax_allure", player.allure), 
        ("loc_park_loiter_hunger", If(player.hunger < 30, 500, 0)), 
        ])
    else:
        $ dialouge = renpy.random.choice([
        "I decide to kill some time by walking around the park.",
        "I hang around in the park to kill some time.",
        "I go for a stroll around the park",
        "I decide to have a stroll around the park."
        ])
        "[dialouge]"
        $ rand_choice = WeightedChoice([
        ("loc_park_loiter_normal", 300),
        ("loc_park_loiter_desire", player.check_horny()),
        ("loc_park_loiter_allure", player.allure), 
        ("loc_park_loiter_hunger", If(player.hunger < 30, 500, 0)), 
        ])
    jump expression rand_choice





label loc_park_loiter_normal:
    jump expression WeightedChoice([
    ("loc_park_loiter_normal_1", 100),
    ("loc_park_loiter_normal_2", 100),
    ("loc_park_loiter_normal_3", 100),
    ("loc_park_loiter_normal_4", 100),
    ("loc_park_loiter_normal_5", 100),
    ("loc_park_loiter_normal_6", 100),
    ("loc_park_loiter_normal_7", 100),
    ("loc_park_loiter_normal_8", 100),
    ("loc_park_loiter_normal_9", 100),
    ("loc_park_loiter_normal_10", 100),
    ("loc_park_loiter_normal_11", 100),
    ("loc_park_loiter_normal_12", 100),
    ])

label loc_park_loiter_normal_1:
    if t.day in weekends:
        pcm "Busy today. I guess people are enjoying the weekend."
    else:
        if t.hour in workhours:
            pcm "Fairly quiet today, I guess most people are working."
        elif t.hour in afternoon:
            pcm "So busy now that everyone is heading home from work."
        else:
            pcm "Fair amount of people enjoying the park today."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_2:
    if t.day in weekends:
        pcm "So lovely to relax in the park on the weekend."
    else:
        pcm "So lovely to relax in the park during my free time."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_3:
    "I pass an old couple who are holding hands."
    pcm "So nice they can still be happy after so many years."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_4:
    "I pass a teen couple who are struggling to keep their hands off each other."
    $ player.face_shy()
    pcm "Aww, young love."
    if player.check_sex_agree(3):
        pcm "Or is it lust? Probably lust... Horny teens."
        $ player.add_desire(3)
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_5:
    "On my walk, I am approached by some dirty guy begging for money."
    guy "Spare any change darlin'?"
    $ player.face_worried
    $ player.add_desire(-5)
    if player.cash >= 10:
        menu:
            "Give £ 10":
                $ player.remove_money(10)
                jump loc_park_loiter_walk_end
            "Go away!":
                $ NullAction()
    $ player.face_angry()
    pc "Ugh, leave me alone!"
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_6:
    "On my walk, I notice a large group of men drinking and blocking the path."
    pcm "Ugh, looks like I'll take a different path. Damn wastemen!"
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_7:
    "During my walk, I cross paths with a cute guy who smiles at me as I pass."
    if player.check_nowill():
        pc "..."
    else:
        $ player.face_shy()
        pc "Heh."
        $ player.add_desire(3)
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_8:
    pcm "Not much going on. Nice and peaceful."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_9:
    pcm "Ahh, nice and quiet. If only life was always this peaceful..."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_10:
    "I pass a couple while on my walk. They are clearly having a heated argument but are trying to keep it discreet."
    $ player.face_worried()
    pcm "Aaaawkward."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_11:
    "I pass a girl who is dressed very provocatively."
    $ player.brow = 3
    if player.slutty:
        pcm "Hmm, do I stand out like she does?"
    elif not player.check_sex_agree(2):
        pcm "Hmm, that's far too much..."
    else:
        pcm "Hmmmm."
    jump loc_park_loiter_walk_end

label loc_park_loiter_normal_12:
    stranger "Hey darlin'. You would look nicer if you smiled more."
    $ player.face_angry()
    pc "Piss off!"
    stranger "What? I was just being nice."
    jump loc_park_loiter_walk_end






label loc_park_loiter_desire:
    jump expression WeightedChoice([
    ("loc_park_loiter_desire_1", 100),
    ("loc_park_loiter_desire_2", 100),
    ("loc_park_loiter_desire_3", 100),
    ("loc_park_loiter_desire_4", 100),
    ])


label loc_park_loiter_desire_1:
    "During my walk I see a cute guy walking in the opposite direction towards me."
    $ player.mouth = 3
    pc "Hey cutie."
    if t.hour in morning:
        cuteguy "Err, g'mornin'."
    elif t.hour in afternoon:
        cuteguy "Err, gud afternoon."
    elif t.hour in evening:
        cuteguy "Err, good evenin'."
    else:
        cuteguy "Err, Hey."
    $ player.eye = 3
    pc "Heh."
    jump loc_park_loiter_walk_end

label loc_park_loiter_desire_2:
    "During my walk, I see a handsome older guy walking in the opposite direction towards me."
    $ player.mouth = 3
    pc "Hey handsome."
    if t.hour in morning:
        handsomeguy "Good morning miss."
    elif t.hour in afternoon:
        handsomeguy "Good afternoon miss."
    elif t.hour in evening:
        handsomeguy "Good evening young lady."
    else:
        handsomeguy "Hello young lady"
    $ player.eye = 3
    pc "Heh."
    jump loc_park_loiter_walk_end

label loc_park_loiter_desire_3:
    "During my walk, I see a boy that probably goes to school with me."
    $ player.mouth = 3
    pc "Hey."
    cuteboy "Eeeh. H-hello."
    $ player.eye = 3
    pc "Haha, so shy."
    $ player.add_mood(5)
    $ player.add_desire(4)
    jump loc_park_loiter_walk_end

label loc_park_loiter_desire_4:
    if player.check_sex_agree(5):
        pc "Damn, I'm so wet and this walk is doing nothing to calm me down..."
        $ player.eye = 2
        pc "..."
        $ player.face_shy()
        $ randomnum = renpy.random.randint(1, 3)
        if randomnum == 1:
            $ c.bottom = 0
            $ c.outfit = 0
        elif randomnum == 2:
            $ c.top = 0
            $ c.outfit = 0
        $ player.mouth = 3
        pc "Maybe this will cool me down."
        pc "..."
        $ player.mouth = 1
        pc "Nope, made it worse."
        pc "Kinda fun though..."
        $ pc_dress()
        $ player.add_mood(10)
        $ player.add_desire(10)
    else:
        pc "Damn, I'm so wet and this walk is doing nothing to calm me down."
        $ player.add_mood(8)
    jump loc_park_loiter_walk_end






label loc_park_loiter_allure:
    jump expression WeightedChoice([
    ("loc_park_loiter_allure_1", 100),
    ("loc_park_loiter_allure_2", 100),
    ("loc_park_loiter_allure_3", 100),
    ("loc_park_loiter_allure_4", 100),
    ("loc_park_loiter_allure_5", 100),
    ("loc_park_loiter_allure_6", 100),
    ("loc_park_loiter_allure_7", If(c.ass, 100, 0)),
    ("loc_park_loiter_allure_8", If(c.ass, 100, 0)),
    ])

label loc_park_loiter_allure_1:
    "While walking around the park, I catch at the corner of my eye a couple of teenagers following me and whispering to each other."
    if player.check_nowill():
        pcm "Perverts."
        "I stop near a bench so they are forced to pass me by before I go on my way."
    elif player.check_sex_agree(3):
        pcm "Pfft, shy guys only able to look and not come and say hello? They won't get anywhere with that tactic. Should I show them what they are missing."
        menu:
            "Show them.":
                if c.outfit > 0:
                    "I make sure to put more sway to my hips while walking."
                    with grope_trans
                    "Eventually, I stop suddenly and bend over to \"tie my laces\". One of the boys almost runs right into me and probably got a good feel of my ass as he struggled to pass me."
                else:

                    if c.skirt:
                        pcm "I'll hitch my skirt up and give them something nice to look at."
                    else:
                        pcm "I'll pull my trousers down and let them get a good view."
                    $ c.bottom = 0
                    "I hear the boys gasping as I keep walking while flashing them."
                    $ pc_dress()
                    pcm "That should be enough."
                $ player.add_mood(8)
                $ player.add_desire(10)
    else:
        pcm "Pfft, shy guys only able to look and not come and say hello? They won't get anywhere with that tactic. No harm in letting them look though."
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_2:
    "While walking around the park, I notice I am attracting a lot of sneaky looks from the guys I pass."
    pcm "Well, suppose that means the hard work I've been putting into looking good is working."
    $ player.add_desire(2)
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_3:
    cuteboy "Hey, my friend asked me to tell you he fancies you."
    if player.check_sex_agree(1):
        pc "What good is that if he's way over there."
        cuteboy "He's too shy to tell you himself."
        pc "Too bad. He will never get a girl if he can't talk to them."
        $ player.add_mood(8)
        $ player.add_desire(2)
    else:
        "I just walk away ignoring them."
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_4:
    "As I am walking, I pass an elderly man who doesn't take his eyes off me for a moment."
    $ player.face_worried()
    pc "Ugh, thats too creepy old man."
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_5:
    "As I am walking, I notice a girl walking with a guy giving me a dirty look."
    $ player.face_worried()
    pcm "Keep an eye on your man, not on me..."
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_6:
    "While walking, I notice a middle aged woman giving me the stink eye."
    $ player.face_worried()
    pcm "What's her problem?"
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_7:
    stranger "*Whistles* Nice ass darlin'"
    if player.check_nowill():
        pc "Ugh."
    elif player.check_sex_agree(3):
        pc "You should be so lucky."
    else:
        pc "I know, I worked hard on it."
    jump loc_park_loiter_walk_end

label loc_park_loiter_allure_8:
    stranger "Ohh baby, you shit with that ass?"
    $ player.face_annoyed()
    pc "What the fu... Is that supposed to be a chat up line or something. Just plain creepy."
    jump loc_park_loiter_walk_end





label loc_park_loiter_hunger:
    if player.cash >= 10:
        jump expression renpy.random.choice([
        "loc_park_loiter_hunger_1",
        "loc_park_loiter_hunger_2",
        "loc_park_loiter_hunger_3",
        ])
    else:
        "I head around the park eyeing up he food stands."
        pcm "Damn, I am starving but too broke to buy anything from here."
        $ player.add_mood(-3)
        jump loc_park_loiter_walk_end

label loc_park_loiter_hunger_1:
    "During my walk, I decide to stop off at a food stand and get something to eat."
    pc "Mmmm. I know this greasy food isn't good for my figure, but it's tasty at least."
    $ player.eat()
    $ player.remove_money(10)
    jump loc_park_loiter_walk_end

label loc_park_loiter_hunger_2:
    "During my walk, I decide to pop to a sweets stand and get something to snack on."
    pc "Lets stick to a healthier option today. Now where is the butter and salt?"
    $ player.eat()
    $ player.remove_money(10)
    jump loc_park_loiter_walk_end

label loc_park_loiter_hunger_3:
    "Hunger gets the better of me during my walk so I decide to grab a few meal bars from one of the vendors."
    pc "Sometimes, I wonder if these things are worse than just starving."
    $ player.eat()
    $ player.remove_money(10)
    jump loc_park_loiter_walk_end











label loc_park_loiter_relax_normal:
    jump expression WeightedChoice([
    ("loc_park_loiter_relax_normal_1", 100),
    ("loc_park_loiter_relax_normal_2", If(weather_var == 1, 100, 0)),
    ("loc_park_loiter_relax_normal_3", 100),
    ("loc_park_loiter_relax_normal_4", 100),
    ("loc_park_loiter_relax_normal_5", 100),
    ("loc_park_loiter_relax_normal_6", 100),
    ("loc_park_loiter_relax_normal_7", 100),
    ])

label loc_park_loiter_relax_normal_1:
    pcm "This is nice..."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_2:
    pcm "Uff, such lovely weather."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_3:
    "I sit there just watching people pass."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_4:
    pcm "I wonder what all these people are like. Everyone just going about their lives."
    if player.has_perk(perk_numb, notif=True):
        pcm "Probably all cunts..."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_5:
    "I spend most of my time relaxing and watching some birds fighting over scraps of food."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_6:
    $ player.face_annoyed()
    pc "Ah damn, I didn't check before sitting down and now my arse is wet."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_normal_7:
    $ player.face_angry()
    pc "Go away birds!"
    pcm "Damn things are pretty aggressive now there isn't as much food."
    jump loc_park_loiter_relax_end





label loc_park_loiter_relax_desire:
    jump expression WeightedChoice([
    ("loc_park_loiter_relax_desire_1", 100),
    ("loc_park_loiter_relax_desire_2", 100),
    ("loc_park_loiter_relax_desire_3", 100),
    ("loc_park_loiter_relax_desire_4", 100),
    ("loc_park_loiter_relax_desire_5", 100),
    ("loc_park_loiter_relax_desire_6", 100),
    ])

label loc_park_loiter_relax_desire_1:
    "I relax and watch a couple sitting on a nearby bench."
    $ player.face_shy()
    pcm "Wow, they can't keep their faces apart for a moment."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_desire_2:
    "I sit and look at a nice looking guy stretching before going for a run. He looks at me and smiles before starting his run."
    $ player.face_shy()
    pcm "Oops, he noticed me looking."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_desire_3:
    "I sit there just watching people pass."
    pcm "Would. Would. Wouldn't. Would. Ugh no chance!"
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_desire_4:
    "I relax and just look at the some of the guys jogging around the park."
    pcm "Mmmm."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_desire_5:
    "I relax and just look at the joggers running around the park."
    pcm "Ugh, I'm turning into a pervert. I should probably have a cold shower or something."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_desire_6:
    "I relax watching a couple caressing each other on the grass."
    $ player.face_shy()
    pc "..."
    jump loc_park_loiter_relax_end





label loc_park_loiter_relax_allure:
    jump expression WeightedChoice([
    ("loc_park_loiter_relax_allure_1", 100),
    ("loc_park_loiter_relax_allure_2", 100),
    ("loc_park_loiter_relax_allure_3", 100),
    ("loc_park_loiter_relax_allure_4", If(not player.sold, 100, 0)),
    ("loc_park_loiter_relax_allure_5", 100),
    ("loc_park_loiter_relax_allure_6", 100),
    ("loc_park_loiter_relax_allure_7", 100),
    ])

label loc_park_loiter_relax_allure_1:
    "While I am relaxing, a guy comes over and sits next to me even though there is plenty of space to sit elsewhere."
    $ player.face_worried()
    pc "..."
    "Eventually, I decide to go and sit somewhere else."
    $ player.face_annoyed()
    pcm "Damn weirdo."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_2:
    "While relaxing, I notice an old guy sitting on a bench staring at me."
    $ player.face_worried()
    pc "Is he... Rubbing himself? Ugh."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_3:
    "I notice a group of urchins sitting nearby constantly glancing over at me."
    $ player.face_shy()
    pcm "Heh."
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_4:
    stranger "Hey sexy girl. How much for you and me in the bushes?"
    $ player.face_annoyed()
    pc "Whaaa! No chance. Not with you!"
    stranger "Damn bitch, since when did whores turn down money?"
    $ player.face_angry()
    pc "The fuck makes you think I'm a whore? Piss off, you pig!"
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_5:
    "I notice a guy laying on the grass looking at me."
    $ player.face_shy()
    pcm "Hehe."
    $ player.face_sus()
    pcm "Hold on..."
    pcm "Ugh, yes he is. He's wanking while looking at me. Damn pervert!"
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_6:
    "A guy rushes up to me and quickly grabs at my clothes."
    $ c.bottom = 0
    $ c.outfit = 0
    $ player.face_shock()
    pc "Whaaa what the fuck!"
    pc "..."
    if player.has_perk(perk_exhibitionist):
        $ player.face_shy()
        "I pretend to fumble with my clothes and give a good showing to the gawkers."
        pc "C'mon, ahh. Sorry sorry."
        "I pretend to be humiliated but in fact I find this really exciting."
        $ pc_dress()
        pc "Finally."
        $ player.face_annoyed()
        pc "Shoo! Show's over!"
        $ player.add_mood(10)
        $ player.add_conf(2)
        $ player.add_desire_random(20)
    else:
        $ pc_dress()
        $ player.face_angry()
        pc "What kind of creep rushes up to someone and pulls their clothes down?"
        pc "Damn, some right weirdos out in the world."
        $ player.add_mood(-5)
    jump loc_park_loiter_relax_end

label loc_park_loiter_relax_allure_7:
    "While I am sitting down relaxing, some guy comes and sits directly next to me so our hips are touching."
    $ player.face_worried()
    pc "Errm, do you mind?"
    stranger "Mind what?"
    pc "Not sitting so close to me."
    stranger "I like it here."
    if player.has_perk([perk_slut, perk_sucu, perk_bimbo], notif=True):
        pc "Right..."
        $ player.grope()
        pc "Yeah, thought as much..."
        $ player.grope()
        pcm "This guy stinks..."
        $ player.grope_end()
    $ player.face_angry()
    pc "Ugh. Freak!"
    "I get up and find somewhere else to sit."
    jump loc_park_loiter_relax_end





label loc_park_loiter_walk_end:
    $ player.face_normal()
    $ loiter()
    $ renpy.scene()
    with dissolve
    $ dialouge = renpy.random.choice([
    "After my walk, I head back to where I started.",
    "After my walk, I head back towards the entrance.",
    "I head back towards the entrance after my walk.",
    "I head back to where I started after my walk."
    ])
    "[dialouge]"
    jump travel_arrival

label loc_park_loiter_relax_end:
    $ player.face_normal()
    $ loiter()
    $ renpy.scene()
    with dissolve
    $ dialouge = renpy.random.choice([
    "I get up and carry on with my day.",
    "I decide to get up and get back to my day.",
    "I get up and go about my business",
    "I decide to get up and carry on with my day"
    ])
    "[dialouge]"
    jump travel_arrival
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
