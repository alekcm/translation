init python:
    def beach_clothes():
        if any(clothes in ["swim", "temp_outfit", "work"] for clothes in tab_top):
            return True
        else:
            return False

label loc_lake_pier_loiter:
    $ walk(loc_pier)
    jump loc_pier_relax
label loc_lake_gym_loiter:
    $ walk(loc_beach_gym)
    jump loc_vball_relax
label loc_lake_beach_loiter:
    $ walk(loc_beach_hangout)
    jump loc_beach_relax
label loc_lake_fire_loiter:
    $ walk(loc_beach_fire)
    jump loc_fire_relax

label dis_lake_loiter_tombola:
    $ rand_choice = WeightedChoice([
    ("loc_lake_pier_loiter", If (can_loiter(loc_pier) and people_beach(), 50, 0)),
    ("loc_lake_beach_loiter", If (can_loiter(loc_beach_hangout) and not t.timeofday == "night" and weather_var <= 2 and beach_clothes(), 50, 0)),
    ("loc_lake_gym_loiter", If (can_loiter(loc_beach_gym) and people_beach_girls_vball() and t.hour_from_to(7,17) and beach_clothes(), 50, 0)),
    ("loc_lake_fire_loiter", If (can_loiter(loc_beach_fire) and people_beach_firepit() and beach_clothes(), 50, 0)),
    ])
    jump expression rand_choice
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
