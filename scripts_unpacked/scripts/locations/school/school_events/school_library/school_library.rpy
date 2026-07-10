label school_library_study:
    "I grab a book from the shelf, get comfortable and read it for a while."
    $ working(60)
    $ player.add_int()
    pcm "Hmmmm..."
    "I decide I am done for now and put the book back."
    jump travel

label school_library_relax:
    "I sit down and grab one of the magazines to browse through."
    $ loiter()
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
