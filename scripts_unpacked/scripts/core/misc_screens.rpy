




screen blackout(number=100):
    zorder 999
    add "white" matrixcolor TintMatrix("#000000") * OpacityMatrix(float(number) / 100)

screen blackout_screen:
    zorder 999
    add "black_100"

screen hooded:

    add "bg_hooded"

screen fg_water:

    add "fg_water"

screen fg_blindfold:

    add "bg_blindfold"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
