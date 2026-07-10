




label school_geography_picker:
    if school_geography == 0:
        jump school_geography0
    $ rand_choice = WeightedChoice([
    ("school_geography1", 1),
    ("school_geography2", 1),
    ("school_geography3", 1),
    ("school_geography4", 1),
    ("school_geography5", 1),
    ("school_geography6", 1),
    
    

    ])
    jump expression rand_choice

label school_geography0:
    geog "Good morning. In this class I will be going over most of the important areas in and around [town]."
    geog "[town] is barely a shadow of it's former glory. It used to be one of the larger cities in the country, but much has changed since the Plague."
    geog "The city it's self has shrunk considerably behind the walls and checkpoint and is less than one quarter of it's original size."
    geog "A lot of people born here will be aware, but [town] was never it's original name. The name [town] came about after the walls went up and most of the city was left behind them."
    geog "Since then, much has changed. Places have fell into disrepair, been repurposed for other uses, been lost behind the walls and even the burning means that the city of old is no more."
    geog "So we will be going over what does remain, what is new and many of the other changes that have happened all over [town]."
    $ school_geography += 1
    jump school_class_lesson_end

label school_geography1:
    geog "Like it was before the Plague, much of the cities nightlife and entertainment is centred around Revel street."
    geog "There you can find places to drink and have a good time along with some shopping."
    geog "It does of course mean you have a lot of drunks around at night time along with other unsavoury characters. So be careful."
    geog "It is not advisable to be around there alone late at night. While security does maintain a decent presence in the area, it is better to be safe than sorry."
    geog "Since security is around, if you find yourself in trouble, get to one of the main walkways where it is well lit. If you can do that, you should be able to attract their attention."
    geog "If they will do something about it though is another question. But it may get someone harassing you to leave."
    jump school_class_lesson_end

label school_geography2:
    geog "[town] still has some shopping opportunities centred around the shopping area and market. While what you want to buy might be limited, it is usually the first place to go."
    geog "Some things such as electronics and other technology are quite difficult to find, but clothes, sports gear and other more daily essentials can be found there."
    geog "The market also has its fair share of books, local foods and second hand goods. A lot of people go there to sell or barter, so it's a good idea to check it out regularly."
    geog "It is also where you might find some of the less common items you might want to get your hands on that are no longer manufactured."
    geog "Things such as toothbrushes, toiletries and female sanitary items, magazines, jewellery and most other things you might want to try to get hold of."
    geog "Sellers will also try to get hold of items for you if you ask them to. Assuming there is money in it for them."
    jump school_class_lesson_end

label school_geography3:
    geog "The lake is one of the few areas around [town] that is not walled. The lake it's self as well as the rough forest terrain surrounding it makes it a natural barrier."
    geog "This does mean though that any one with a boat can bypass it. This means at night there might be things going on that you do not want to get involved with."
    geog "During the day though it can be lovely there. The water is cleaner than it ever was thanks to less waste being produced, so you can swim in it no problem."
    geog "Been a while since I was there, but I hear people set up a volleyball net on the sand and there are vendors selling food and beer."
    geog "Don't wander too deep into the forest though. It's a good way to slip and break your neck or find yourself alone with people you would rather not be with."
    jump school_class_lesson_end

label school_geography4:
    geog "Some of you might have already seen it, but there is a busy checkpoint on the other side of [town] where supply convoys and other deliveries come through."
    geog "There is nothing for anyone here to do there so it's advisable you don't go poking around the area. But it is where the main security offices moved to."
    geog "Since the police station was burned down, the checkpoint became the new home to [town]'s security forces."
    geog "Most of their duties is maintaining the checkpoint, but you can report crimes there. Whether they listen or care is another matter entirely."
    jump school_class_lesson_end

label school_geography5:
    geog "Not far from the checkpoint you have the truck stop. A considerably larger area than it sounds since it is where most of the vehicles from the convoys stay."
    geog "Many of the drivers are not from [town] so they will stay in one of the motels scattered around the place. There are also places to eat and other facilities anyone here for a short stay will need."
    geog "But unless you have a reason to be there, it is best to stay away. Pretty much anyone who is not a trucker is assumed to be a whore or providing other types of services."
    geog "So unless you are providing such services, keep away."
    jump school_class_lesson_end

label school_geography6:
    geog "One of the nicer places around [town] is the major park. It is not too far from the lake and much of the forest near the lake envelops the park as well."
    geog "It can make it just as nice a place to hang out as the lake is. It still has paved paths running through the park but also more secluded forest areas and open grass."
    geog "You can see a lot of people relaxing on the benches, playing on the grass or getting up to no good in the wooded areas."
    geog "Generally it is a safe area, but like with the lake, don't go too deep into the forest and don't stick around too late at night."
    jump school_class_lesson_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
