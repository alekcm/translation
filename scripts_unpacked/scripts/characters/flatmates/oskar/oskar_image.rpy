layeredimage oskar:
    at sprite_highlight("oskar")
    always "oskar_base" 
    if "took_poison" in oskar.dict and oskar.dict["took_poison"] > 0:
        "oskar_sick_layer"

image oskar_sick_layer:
    "oskar_sick"
    matrixcolor OpacityMatrix(If(t.day - oskar.dict["took_poison"] >= 10, 1, (t.day - oskar.dict["took_poison"]) / float(10)))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
