

label cass_talk_bully_chain_0:
    $ cass.dict["cass_bully_talk"] += 1
    pc "Err. You okay [cass.nname]?"
    cass.name "Err, yeah... Why?"
    pc "I saw those arseholes giving you trouble."
    cass.name "Oh?"
    cass.name "..."
    pcm "Better not push it..."
    jump cass_talk_end

label cass_talk_bully_chain_1:
    $ cass.dict["cass_bully_talk"] += 1
    pc "Have you tried talking to someone about those cunts?"
    cass.name "..."
    pc "... ..."
    jump cass_talk_end

label cass_talk_bully_chain_2:
    $ cass.dict["cass_bully_talk"] += 1
    cass.name "Not really anyone to talk to about those idiots."
    pc "No?"
    cass.name "Everyone knows what they do. It's not just me they harass."
    pc "Yeah, they were harassing me as well..."
    jump cass_talk_end



label cass_talk_bully_tombola:
    jump expression WeightedChoice([

    ("cass_talk_bully_1", 100),
    ("cass_talk_bully_2", 100),
    ("cass_talk_bully_3", 100),
    ("cass_talk_bully_4", 100),
    ])

label cass_talk_bully_1:
    pc "Hopefully one day those idiots will run into someone who will put them in the dirt."
    cass.name "I hope so."
    jump cass_talk_end

label cass_talk_bully_2:
    pc "When will those fools trip and fall into the lake or something?"
    cass.name "Yeah..."
    jump cass_talk_end

label cass_talk_bully_3:
    cass.name "I feel like not coming here sometimes."
    pc "Cos of those cunts?"
    cass.name "Yeah."
    jump cass_talk_end

label cass_talk_bully_4:
    pc "Maybe bite their dick off?"
    cass.name "Haha, yeah. Would be fun before they kill me."
    pc "Worse ways to go out."
    jump cass_talk_end



label cass_talk_bully_poison_0:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    cass.name "That... Stuff you gave me. I don't have it any more."
    pc "Stuff? Err... Oh?"
    pcm "The poison."
    pc "Good."
    cass.name "Good? You really think so?"
    pc "..."
    jump cass_talk_end

label cass_talk_bully_poison_1:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    pc "There wasn't really any other way. Can't go tell security or anything."
    cass.name "But..."
    cass.name "*Sigh*"
    cass.name "It doesn't feel right."
    jump cass_talk_end

label cass_talk_bully_poison_2:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    pc "They went out of their way to make everyone's life hell."
    cass.name "Maybe they had their own issues."
    pc "Not your problem."
    jump cass_talk_end

label cass_talk_bully_poison_3:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    cass.name "Did any one try and talk to them or find out what their problem was?"
    pc "Hard to talk to someone when they are raping you in the ass."
    cass.name "..."
    jump cass_talk_end

label cass_talk_bully_poison_4:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    cass.name "Maybe it was an over reaction. They aren't, you know, yet. I could still save them."
    pc "And you think they will thank you? Probably use it against you even more to abuse you."
    pc "They are pieces of shit who spread harm. So they deserve any they get in return."
    jump cass_talk_end

label cass_talk_bully_poison_5:
    show cass worried
    $ cass.dict["cass_poison_talk"] += 1
    pc "Frankly, who cares about those shits. Most people here would thank you for what you did."
    cass.name "..."
    pc "Life here would be better for so many people with them gone."
    jump cass_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
