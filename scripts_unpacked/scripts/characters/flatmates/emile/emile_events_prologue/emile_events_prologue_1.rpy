label emile_prologue_event_1:
    emile.name "So now we have all that out of the way, you want to go take a walk around the neighbourhood?"
    emile.name "Be good to stretch your legs and will get you used to the area a bit."
    pc "Err..."
    menu:
        "Sure, let's take a walk":
            pc "Okay, sounds good."
            jump emile_prologue_event_1_go_out
        "No, think I would prefer to go alone":

            emile.name "You sure? I won't be around for long so won't really get another chance."
            menu:
                "Actually, yeah let's go out":
                    jump emile_prologue_event_1_go_out
                "Yeah I'm sure.":
                    emile.name "Ok, but don't wander around too late and be home before dark."
                    pc "Right. Okay."
                    jump travel

label emile_prologue_event_1_go_out:
    $ emile.dict["prologue_event"] += 1
    if "home" in tab_top:
        pc "Let me change first though."
        $ pc_dress_event("daily", loc_bedroom)
        show emile at right1
        $ walk(loc_kitchen)
        pc "Ready."
    show emile at right1
    $ walk(loc_stairwell)
    emile.name "You poked your head outside yet?"
    if loc_residential.visited:
        pc "A bit, not too much though."
    else:
        pc "No, not since yesterday."
    $ walk(loc_residential)
    emile.name "Well, as you can see, a lot has changed..."
    pc "Yeah... Well, no actually. Area is a bit run down but could find places like that everywhere before."
    emile.name "Mmm, but before those areas were the shitholes. You actually live in quite a nice area here."
    pc "What? Really? Windows are all boarded up, can see ramshackle houses around and the road can barely support cars."
    emile.name "Yeah... About that..."
    emile.name "Other than the city bus, you won't see too many cars on the road any more. No easy supply of petrol so cars are limited to those who can get fuel."
    pc "Err... Okay... How does the bus run?"
    emile.name "It's a hybrid and gets all the workers around, so they try to maintain it as best they can. Still, they stink and are full of cretins."
    pc "Right, and all the other stuff?"
    emile.name "It's people fixing up their own places. Have to make do with whatever you can get your hands on and there are no window shops around so it's usually wood."
    pc "Basically... No services work any more?"
    emile.name "Some do, most don't."
    pc "..."
    $ walk(loc_park)
    pc "So..."
    pc "What am I expected to do here?"
    emile.name "Dunno. Sounded like [tucker.name] wanted to speak to you about that."
    pc "He could have told me then."
    emile.name "Yeah... I think he didn't want to while I was around."
    pc "You?"
    emile.name "Just a guess."
    pc "Well, ok. But that doesn't answer the question. Am I just supposed to go to school, get a job and pretend like none of this happened?"
    emile.name "Err, I guess?"
    pc "You guess?"
    emile.name "Well, what else is there?"
    pc "Dunno... Something..."
    emile.name "We came here to escape the riots and would have been dead if we didn't manage that."
    pc "Err..."
    emile.name "Well, dead for good."
    emile.name "A few seasons might have passed since then, but nothing has changed."
    emile.name "We live here now and for the most part, we are safe. No one looking to kill us because they think we are hoarding food, no gangs roaming the streets..."
    pc "Okay."
    emile.name "Okay?"
    if player.has_perk(perk_male):
        pc "Yeah, you are right. This is what we came here for. Ignoring my lack of a cock, we got what we wanted. Safe and far away from the burning big cities."
    else:
        pc "Yeah, you are right. This is what we came here for. Ignoring the fact I ended up wrapped round a lamp post and died, we got what we wanted. Safe and far away from the burning big cities."
    pc "School doesn't put money in my pocket though, what should I do about that?"
    emile.name "Well, it's not really a school so it's not mandatory you turn up to it."
    pc "It's not? Why do I have a school uniform then?"
    emile.name "Most people are in shitty situations like you are and can barely afford clothes. There was a warehouse full of uniforms so they give 'em out so the place doesn't look like a homeless refuge."
    pc "Ah. Wait, isn't that the same reason as before?"
    emile.name "Hah, pretty much. The place is just to put a bunch of young people like you who ended up fucked harder than most by all this. Lets you all adjust together."
    pc "Ahh young people \"like me\"... I'm gonna be the oldest person there."
    emile.name "Yeah, but no one else knows that."
    pc "So basically, get a job, go hang out with the local kids and try not to starve."
    emile.name "Or get kicked out. You have to pay rent."
    pc "Fuck!"
    emile.name "Rent is paid up for a week so you are good for now. But no doubt the landlord will be paying you a visit at some point."
    pc "Only 2 weeks. Those cheap bastards."
    emile.name "Yeah, how dare they spend 6 months bringing you back to life, give you a brand new body, a place to live in a nice area and not give you a million dollars."






















    pc "..."
    pc "What about you? How have you been holding up through all this?"
    if emile.days_pregnant > (global_pregnancy_length * 0.3):
        pc "Does the bun in the oven mean you ended up getting married or something?"
        emile.name "No..."
        pc "Oh? You minx!"
        emile.name "There is no birth control any more..."
        pc "What? None?"
        emile.name "It's stuff you will find out at the academy, but pretty much. All illegal now."
        if player.has_perk(perk_male):
            emile.name "You are new to being a girl so listen to me when I say this. Be careful."
            pc "I..."
            emile.name "Can get knocked up. Yes. Probably anyway. I assume the body can."
            emile.name "So don't be so quick to try out your shiny new body or you will end up like this in no time at all."
        else:
            pc "Fuck..."
            emile.name "Yeah..."
        emile.name "I hear there is a black market for this kind of stuff, but nothing I could find."
        pc "There usually is..."
        pc "You getting on okay otherwise?"
    emile.name "Managed to get my own place in an area a bit nicer than this. Costs more of course but means I am not squashed in like sardines."
    pc "Oh, so you have a job?"
    emile.name "Yeah, working in an office type place. Pay is shit but it's stable work so hopefully won't turn up one day and be fired out the blue."
    pc "Ah yeah. That's good."
    $ loiter(180, emile)
    "We walk around the park for a few hours catching up. [emile.name] seems mostly reluctant to talk a lot about what she got up to while I was in hospital."
    "But it's still nice to hang out with her and catch up. We talk a lot about my past life."
    "I don't really want to tell her, but most of what she talks about, I have no memory of. I mostly just listen and pretend where I can that I do remember."
    $ walk(loc_residential)
    "We have been out for quite a while so we grab something from a food stand and start to head home while eating it."
    pc "So no restaurants any more?"
    $ player.eat()
    emile.name "Not really. You have the Diner where truckers eat but that's about it. Most places shut down or were looted during the chaos."
    emile.name "Hard for a restaurant to survive while people are literally starving in the streets."
    $ walk(loc_stairwell)
    pc "I guess..."
    emile.name "Tomorrow, if you want, we can go hang out somewhere else."
    pc "Err, sure. Where?"
    emile.name "Dunno, I'll think of that tomorrow. Probably get the bus somewhere further out."
    pc "Okay."
    hide emile with dissolve
    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
