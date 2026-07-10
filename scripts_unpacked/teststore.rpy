label teststore:

    "this is a test store"
    "we will now return you to the main street"
    jump highstreet



label test_bars:
    scene bg_bedroom
    "Add desire 10"
    $ player.desire += 10
    "Some text to delay things"
    "more text"
    "Add will 10"
    $ player.will += 10
    "add corruption 50"
    $ player.corrupt += 50
    "Some text to delay things"
    "more text"
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
