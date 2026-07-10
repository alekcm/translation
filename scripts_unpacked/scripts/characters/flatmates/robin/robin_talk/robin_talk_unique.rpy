



label robin_talk_soccerboys_ask:
    $ add_to_list(robin.list, "soccerboys_ask_know")
    robin.name "You ever go to the pitch at the school? Wondering if the boys there are safe to play with."
    if not loc_school_field.visited:
        pc "Actually not been there. What boys?"
        robin.name "There are some boys who play football at the school. Seen them a few times."
        pc "Interested in them?"
        robin.name "Interested in playing football. It's fun but don't want to end up with some weirdos."
        pc "Well, not been there. Tell me how it goes if you do."
    elif drake.has_met:
        pc "Yeah. I was checking the place out and they invited me to play. They seem alright."
        robin.name "Yeah? Might have to check it out and join."
        pc "The more the merrier."
    else:
        pc "Been to the field but don't remember the boys there."
        robin.name "No? They were there when I was checking the place out and was tempted to join them."
        pc "Oh? Interested in getting a boyfriend?"
        robin.name "Interested in playing football. It's fun but don't want to end up with some weirdos."
        pc "Well, Tell me how it goes if you do join them."
    jump robin_talk_end

label robin_talk_soccerboys_tell:
    $ add_to_list(robin.list, "soccerboys_ask_tell")
    robin.name "So I had a chat with the boys at the field and played a few games with them."
    if not drake.has_met:
        pc "Ah yeah?"
        robin.name "They seem alright. Might hang with them after school instead of just staying locked up in here all evening."
        pc "Yeah, good to get out there and enjoy, even if it is a bit shitty."
        robin.name "Yeah, going a bit crazy cooped up in here all day."
    else:
        pc "Ah yeah? They seem decent enough."
        robin.name "Seemed like it to me as well."
        if nate.love > 10:
            pc "Watch out for [nate.name] though. Pervert through and through."
            robin.name "Yeah, he made that pretty clear right away. Harmless though isn't he?"
            pc "Yeah, though no doubt he will jump you if you offer."
            robin.name "Pfft. Could say that about off of 'em."
            pc "True..."
        else:
            pc "Might see you out there at some point and can play together."
            robin.name "Hope so."
    jump robin_talk_end

label robin_talk_soccerboys_meet:
    show robin happy at right1 with dissolve
    $ add_to_list(robin.list, "soccerboys_ask_tell")
    pc "Ah hey [robin.name]."
    robin.name "[name]! Joining us?"
    pc "Yeah. Good to see you here."
    robin.name "Come on. We gotta beat the boys here. Can't let these cunts show us up."
    nate.name "Less chat more play!"
    hide robin with dissolve
    jump school_field_soccer_play_start

label robin_talk_beachvball_ask:
    $ add_to_list(robin.list, "beachvball_ask_know")
    robin.name "Ever been to the beach?"
    if "prologue_event" in emile.dict and emile.dict["prologue_event"] >= 2:
        pc "Yeah, went there with [emile.name]. Why?"
    elif loc_beach_hangout.visited:
        pc "Yeah, I checked it out. Why?"
    else:
        pc "No, not been there. Why?"
    robin.name "I heard some people play volleyball there. Was thinking of going."
    pc "Well, pretty sure people would be happy to see you there. Bikini and all."
    robin.name "That's why I still haven't gone. Probably perverts everywhere looking to stare at our arses."
    pc "So, like everywhere else then?"
    show robin happy
    robin.name "Ha. Fuck... Yeah, no change there."
    jump robin_talk_end

label robin_talk_beachvball_tell:
    $ add_to_list(robin.list, "beachvball_ask_tell")
    robin.name "So ended up heading to the beach and checking the place out."
    pc "Oh? How many times someone grab your arse."
    robin.name "Not much more than usual. Seems like at least some decent people there as well. Played a few matches with them."
    pc "Sounds nice. Maybe I should join with you."
    robin.name "Would be nicer with you there yeah. And can go home together to avoid the bus creeps."
    jump robin_talk_end





label robin_talk_pregnant_discover:
    $ add_to_list(robin.list, "seen_pregnant_" + str(robin.preg))
    if not robin.love >= 50:

        jump robin_talk_subject
    if robin.preg == 1:
        pc "Oh? Pregnant? How'd you manage that?"
    else:
        pc "Pregnant again? Who's the lucky man?"
    robin.name "It's obvious now is it?"
    pc "Yeah... No hiding that anymore."
    if any(x == robin.pregnant_who for x in [drake, nate, dan]):
        robin.name "[robin.pregnant_who.name] gave this to me. Maybe I shouldn't have been so eager to join in the fun with you."
        pc "Or should have been more careful."
        if player.pregnancy > 2:
            robin.name "Yeah, don't think you are one to talk."
            pc "Hah, probably not."
        else:
            robin.name "Maybe, though I guess is bound to happen when you are entertaining three guys."
            pc "Mmm, probably."
    elif robin.pregnant_who == oskar:
        robin.name "Pretty sure I got this while paying the rent off."
        pc "Oh? Maybe you should start charging him rent for his baby living inside you."
        robin.name "Haha. I wish."
    elif robin.pregnant_who == robinman:
        robin.name "This? Pretty sure it happened when we were out having fun together."
        pc "Ah. Yeah I guess when you go about being a slut, this is going to happen."
        robin.name "Yeah."
    elif robin.pregnant_who == busgroper:
        robin.name "Err..."
        pc "..."
        robin.name "A man on the bus..."
        pc "Oh wow! Err..."
        pc "Congrats?"
        robin.name "Haha, yeah right..."
    elif robin.pregnant_who == lover:
        robin.name "Err, not sure. I think it was one of the guys from the beach."
        pc "Oh? Sounds like fun."
        robin.name "Was at the time."
        pc "Haha."
    elif any(x == robin.pregnant_who for x in [punter, highpayer]):
        robin.name "Err..."
        robin.name "It was someone who offered to pay..."
        pc "Ah."
        robin.name "Yeah..."
        pc "Got more than he paid for then."
        robin.name "Yeah, should have got more money off him if I knew I would end up like this."
    elif robin.pregnant_who == rapist:
        robin.name "Err, wasn't by choice..."
        pc "Ah, shit. Sorry."
        robin.name "Yeah..."
    else:
        robin.name "Not sure actually."
        pc "Oh?"
        robin.name "Yeah..."
    jump robin_talk_end





label robin_talk_scav_intro:
    $ robin.dict["robin_talk_scav_chain"] = t.day
    pc "I ended up checking out the junk yard way out the end of town."
    robin.name "That near the checkpoint? I've been told to stay away from that area."
    pc "Oh? Never heard to stay away. The highway is where everyone tells me to avoid."
    robin.name "Might have been the highway... Can't remember."
    pc "Anyway, bumped into a girl there that was talking about making some money."
    robin.name "Bending over?"
    pc "Sort of. But not with things in your arse. Collecting junk from the street and selling it on."
    robin.name "Ah! I used to do that as a kid. Collect bottles and tins and sell them to the recycler."
    pc "Well, pretty much the same thing actually. Sell things like that off to the junk yard. Money without people trying to stick things in you."
    robin.name "Hmm... Might have to give that a go. You met her at the checkpoint?"
    pc "No, she runs the junk yard that's near the checkpoint with her brother."
    robin.name "I'll probably have a look."
    jump robin_talk_end

label robin_talk_scav_return:
    $ robin.dict["robin_talk_scav_chain"] = t.day
    $ add_to_list(robin.list, "is_scavver")
    robin.name "I went to that junk yard you told me about."
    pc "Ah yeah?"
    robin.name "Decided it could be worth just collecting some of the junk."
    pc "Better job than most I guess."
    robin.name "Was also speaking to [sandy.name] about it at the lake."
    if not sandy.has_met:
        pc "Don't think I know her."
        robin.name "Ah. Well she works a kiosk at the lake and makes jewellery. Wants to also buy stuff you find on the beach."
    else:
        pc "Ah yeah, she wants shells and things like that."
        robin.name "Yeah."
    if shop_needle.open:
        pc "Girls at school also buy up any cloth or fabric stuff you can dig up."
        robin.name "Oh? Will have to keep an eye out for that then."
    jump robin_talk_end

label robin_talk_bitching_aftermath:
    pc "Next time you want to kill me, make sure you have a grave dug first. Would be a nightmare to hide the body."
    robin.name "Haha, I'll keep that in mind."
    pc "Can't believe \"death by horny bitch\" gets added to my list of close calls with death."
    robin.name "Well, you did deserve it."
    pc "Maybe..."
    $ remove_from_list(robin.list, "done_bitching")
    jump robin_talk_end

label robin_talk_nudevball_tell:
    $ add_to_list(robin.list, "nudebeachvball_ask_know")
    pc "So, you know those girls yu hang with at the beach?"
    robin.name "Yeah, what about them?"
    pc "You know what they get up to at night?"
    robin.name "Drink and probably have sex. I don't hang out there that late so no idea."
    robin.name "Why? You are welcome to join."
    pc "Ah, well I bumped into... I went at night and everyone was naked playing volleyball."
    robin.name "Really?"
    pc "Yeah, it's a fun thing they do."
    robin.name "Oh?"
    pc "Mostly girls. Maybe you want to join."
    jump robin_talk_end

label robin_talk_nudevball_tell_pc:
    $ add_to_list(robin.list, "nudebeachvball_ask_know")
    $ add_to_list(loc_beach_hangout.list, "nude_vball")
    robin.name "You ever considered joining us for volleyball at night?"
    pc "Err, not really. Why do you play at night?"
    robin.name "It's kinda fun."
    pc "Yeah, but can't see the ball properly. It's just worse than in the day."
    robin.name "We... Play naked."
    pc "Play naked...?"
    pc "Ah, doing weird naked things?"
    robin.name "It's just a bit of fun the girls have. Nothing too much else."
    pc "Right..."
    robin.name "So come at night, it will be fun."
    jump robin_talk_end

label robin_talk_kickedout_window:
    if t.hour in irange(0,5):
        pcm "It's late and she is probably asleep."
        jump travel

    "I go over to [robin.name]'s window and knock on it."
    if not robin_here(dis_home):
        pcm "Doesn't seem like she is home..."
        jump travel

    $ add_to_list(robin.list, "kickedout_window_entry")
    $ loc_bedroom_robin.locked = False
    robin.name "Oh hey, hold on. I'll open the window."
    "[robin.name] opens the window and I climb in."
    $ walk(loc_bedroom_robin)
    show robin at right1 with dissolve
    pc "Hey."
    robin.name "Hey, so kicked out but still paying me a visit?"
    pc "Sure, thought I would pop by."
    robin.name "Well, you are more than welcome."
    pc "[oskar.name] would disagree."
    robin.name "Ha, fuck that cunt."
    robin.name "Although better not let him catch you here, I might end up out on my arse as well."
    pc "Yeah."
    robin.name "I'll leave the window unlocked so you can pop by."
    robin.name "Can't have you stay over the night though."
    robin.name "[oskar.name] will kick me out too."
    pc "Yeah no worries."
    jump robin_talk_end

label robin_talk_kickedout_window_locked:
    pcm "The window is locked. I guess [robin.name] isn't home."
    jump travel

label robin_talk_oskar_dead_know:
    $ add_to_list(robin.list, "oskar_dead_know")
    robin.name "Did you hear? They emptied [oskar.name]'s office."
    pc "Oh? They fire him or something?"
    robin.name "Maybe. But he owned the place so who could sack him? Heard security was there."
    pc "Oh wow. Maybe they arrested him or something?"
    robin.name "Maybe."
    robin.name "Wonder if this will effect rent?"
    if loc_kitchen.locked:
        $ loc_kitchen.locked = False
        robin.name "Oh? Maybe you can move back in."
        pc "Oh yeah that would be nice."
    jump robin_talk_end
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
