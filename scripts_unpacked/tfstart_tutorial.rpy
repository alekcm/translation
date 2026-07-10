label tfstart_tutorial:

    scene bg outside hospital
    with dissolve

    "sister Emily [sname] will talk some fluff then ask your new name"
    "this is a test to see if the name input worked [fname] [sname]. Okay [name]"
    "she will explain that she and male friend have been staying in the city for X months while you recovered from the procedure"
    "the hospital has given them a stipend and they have been working and getting to know the town"
    "its a decent place to live, and for plot reasons they havent left. no need to go into detail about it. they live here now"
    "The town is nice but has it's bad parts, and should be careful at night time"

    "she then tells you that you are going shopping together, can't have you walking around with a hospital gown all day"

    "first stop is the clothing shop, here you will pick from a list of preset choices. the choices will determine some of your starting stats"

    "next you are off to the underware shop. same deal here"

    "next to the sports shop where you get yourself some gym clothes and swimwear. again same deal. limited choices and they effect your stats"

    "finally some makeup and other essentials and off to your flat"

    "testing a pause"

    window hide
    $ renpy.pause(hard=True)

    "something to tell the pause to go away"

    jump shared_dorm_bedroom
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
