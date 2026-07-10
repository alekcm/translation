label sport_blocker_pregnant:
    $ player.face_sad()
    $ dialouge = renpy.random.choice([
    "(I can't really be exercising while pregnant.",
    "(I think right now all I am capable of is waddling around so probably best not to try.",
    "(I'm not going to manage any of that with this fat belly.",
    "(I'm not going anywhere with this fat belly of mine.",
    "(If I really want to do some exercise while pregnant then I should head to the pool instead. It's about all I will be able to manage with a belly this size.",
    "(Fat with child and trying to do that? No chance.",
    ])
    pc "[dialouge]"
    $ player.face_normal()
    jump travel

label sport_blocker_pregnant_mild:
    $ dialouge = renpy.random.choice([
    "(If I keep thing light then I should be okay with this belly.",
    "(May only be capable of waddling, but it is better than nothing.",
    "(A little bit of exercise won't harm the baby.",
    ])
    pc "[dialouge]"
    return

label sport_blocker_rain:
    $ player.face_sad()
    $ dialouge = renpy.random.choice([
    "(Don't really want to be exercising in the pissing rain.",
    "(It's pissing down, I'll get sick if I exercise in it.",
    "(I'll end up soaked to the bone if I stay out under this weather.",
    "(No chance, I'll probably slip and end up face first in the mud if I go exercising in this weather.",
    "(Out in this weather? No chance.",
    ])
    pc "[dialouge]"
    $ player.face_normal()
    jump travel

label sport_blocker_snow:
    $ player.face_sad()
    $ dialouge = renpy.random.choice([
    "(Don't really want to be exercising in this snow.",
    "(It's freezing cold, I'll get sick if I exercise in it.",
    "(I'll end up frozen to death if I stay out under this weather.",
    "(No chance, I'll probably slip and end up face first in the snow if I go exercising in this weather.",
    "(Out in this weather? No chance.",
    ])
    pc "[dialouge]"
    $ player.face_normal()
    jump travel

label sport_blocker_drunk:
    $ player.face_sad()
    $ dialouge = renpy.random.choice([
    "(Ugh, had a bit too much to drink to be doing that.",
    "(Will end up puking if I do that.",
    ])
    pc "[dialouge]"
    $ player.face_normal()
    jump travel

label sport_blocker_tired:
    $ player.face_sad()
    $ dialouge = renpy.random.choice(sport_blocker_tired)
    pc "[dialouge]"
    $ player.face_normal()
    jump travel

label sport_blocker_mood:
    $ player.face_sad()
    $ dialouge = renpy.random.choice([
    "(I'm not in the mood exercising. I'd rather just go home and watch TV.",
    "(I don't feel like exercising right now. Would prefer to do something to lift my mood.",
    "(Ugh no. Exercising now will just upset me even more than I am already.",
    "(I'm not in the mood for exercising right now.",
    "(No, just no. I am not in the mood for exercising right now.",
    ])
    pc "[dialouge]"
    $ player.face_normal()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
