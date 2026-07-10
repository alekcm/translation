






































label flatmate1_test_kitchen:
    "THis is a test to confirm that the flatmate thing is working"
    "This is morning breakfast, it will improve your relationship with both flatmates."
    $ t.minute = 25
    jump kitchen_screen
label flatmate1_test_kitchen1:
    "THis is a test to confirm that the flatmate thing is working"
    "This is evening food, it will improve your relationship with flatmate 1. flatmate 2 isnt here."
    "He might demand that you make him food since you are a woman or something like that. He might also demand you put on an apron and nothing else"
    $ t.minute = 25
    jump kitchen_screen

label flatmate1_test_common_evening_mon:
    "He is just chilling with a beer and watching whatever crap is on tv and recovering a bit from his heavy weekend."
    "If your relationship is not developed, there is less chance of him doing something to you"
    "If your relationship is more developed, he might ask you to blow him or ride him while he watches tv."
    $ t.hour = 1
    jump common_screen
label flatmate1_test_common_evening_wed:
    "Today is either monday or wednesday and your flatmate is watching some sports on TV and drinking a beer."
    "You dont care about sports and he knows it, but you can sit and watch with him anyway. You dont understand a damn thing but it doesnt seem to matter."
    "Depending on your relationship, he might demand stupid things from you like wearing a cheer costume and cheering his team on"
    $ t.hour = 1
    jump common_screen
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
