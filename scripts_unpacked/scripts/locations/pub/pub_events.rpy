label loc_pub_visit:
    pcm "Hmm, I expected this place to look a lot worse..."
    if t.time_from_to(18.00, 02.00):
        pcm "Lot more busy than I expected it would be."
    else:
        pcm "I could probably ask about work here."
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
