label haven_room3_wait:
    if not haven_guard_hours():
        pcm "No point in hanging around since the guard who sneaks off to smoke is not working right now."
        jump travel
    elif haven_guard_smoking():
        pcm "He is already away smoking, so no need to wait."
        jump travel
    else:
        "I hang around waiting for the guard to pass by the room to go and have a smoke."
        $ relax(10)
        if haven_guard_smoking():
            jump haven_room3_wait_yes
        pcm "... ..."
        $ relax(10)
        if haven_guard_smoking():
            jump haven_room3_wait_yes
        pcm "..."
        $ relax(10)
        if haven_guard_smoking():
            jump haven_room3_wait_yes
        pcm "He still hasn't left his post."
        jump travel


label haven_room3_wait_yes:
    pcm "He has left his post, now is my chance."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
