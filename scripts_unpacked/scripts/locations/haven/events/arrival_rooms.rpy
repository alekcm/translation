label haven_room_arrival_join:
    jump haven_room_arrival_join_boys

label haven_room_arrival_join_bedroom:
    if haven_time_safe():
        jump haven_room_arrival_join_girls
    elif haven_time_danger():
        jump haven_room_arrival_join_boys
    else:
        $ rand_choice = WeightedChoice([
        ("haven_room_arrival_join_girls", 1),
        ("haven_room_arrival_join_boys", 1),
        ])
        jump expression rand_choice

label haven_room_arrival_join_shower:
    if haven_time_safe():
        jump haven_room_arrival_join_girls
    elif haven_time_danger():
        jump haven_room_arrival_join_boys
    else:
        $ rand_choice = WeightedChoice([
        ("haven_room_arrival_join_girls", 1),
        ("haven_room_arrival_join_boys", 1),
        ])
        jump expression rand_choice

label haven_room_arrival_join_girls:
    if player.check_speech(3) and not numgen(0,8):
        jump expression "haven_intel_" + str(numgen(15,16))

    $ dialouge = WeightedChoice([
    ("...woke up to the grunting and it is right in front of my face. I was just about to shout at him to get the fuck away, but the second I opened my mouth...", 1),
    ("...he's gonna get down on his knee and give you a ring or summit? Best you can hope for is he wants more than one kid and you can be slow in giving them to him so he keeps you round...", 1),
    ("...over in the pub. Money is worse but at least there, nothing is expected of you and you can just keep your legs closed and serve the beer to the...", 1),
    ("...stupid of me. Came back drunk after drinking with a punter an come back here staggering all over the place. I know it didn't happen out there cos I didn't lay with the guy but I still woke up with my...", 1),
    ("...fightin' over who goes off with one of the mongers since he tips well if you let him do what he wants. Harmless, so no chance of you waking up with your insides missing or something. So of course they waanna go off with...", 1),
    ("...layin' 'ere like I was dying of the Plague or somethin'. An he's like \"You gonna be using the ben for much longer?\" Fuckin hell fella, can't you see I'm only gettin' out of here today as a corpse...", 1),
    ])
    havgirl "[dialouge]"
    jump travel

label haven_room_arrival_join_boys:
    if player.check_speech(3) and not numgen(0,8):
        jump expression "haven_intel_" + str(numgen(17, 20))

    $ dialouge = WeightedChoice([
    ("...and he came up as if he owned the place. He goes \"Thats mine\". So I stood up and was ready for a ruck but you should have seen the size of him...", 1),
    ("...hidin' behind some bins waiting for them to go, but some dog was barking at me so had to do a runner. Next time I see that damn mutt I am gonna cook....", 1),
    ("...running away and jumped over some fence. But there was no floor over the fence but a bug hole leading to the basement level. Fucked up my foot on the way...", 1),
    ("...selling the brew to everyone and lording it over us. Man thinks he's gonna take over this place in the future with all that...", 1),
    ("...not a chance. You seen their girls with the dead eyes? Looking at you like you aren't even sure there is someone behind them. Dunno what goes on over there, but to turn someone like that...", 1),
    ("...drunk as a skunk staggering all over the place. And he bumps into the doorframe, which rattles the wall, knocking everything off the shelves in the entire room. Was chaos for a while until they realised...", 1),
    ("...pissing out the window down onto the courtyard. He couldn't believe what was going on and went to rush up the stairs. But 'cos his boots were wet he slips on the concrete and cracks his head...", 1),
    ])
    hav "[dialouge]"
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
