label haven_intel_first:

    $ add_to_list(main_quest_05.conversation_topics, "intel_first")
    pcm "Well based on what I heard, [ant.name] was here at some point. No idea if he will return though. I might be able to find out if I get more info."
    $ log.activate("mq_05_info", notify=True)
    jump travel

label haven_intel_mid:

    $ add_to_list(main_quest_05.conversation_topics, "intel_mid")
    pcm "Doesn't sound like [ant.name] will be returning, at least not any time soon. I need to find out where he might be now."
    jump travel

label haven_intel_done:

    $ add_to_list(main_quest_05.conversation_topics, "intel_done")
    pcm "If I piece together everything I have heard here, it paints a pretty clear picture of what happened to [ant.name]."
    pcm "Looks like I no longer need to try to find my way up to [alex.fname] [alex.sname]'s floor and can just report in to [tucker.name] with what I have."
    $ loc_haven_exterior.locked = False
    $ walk(loc_haven_lobby)
    pcm "Not caused any trouble here so should just be able to walk out and meet with [tucker.name]'s people keeping watch"
    pcm "Not sure if it would be a good idea to ever return here, so if I still have something to do I had better do it now before I leave."

    jump travel

label haven_intel_1:
    havmuff "...least he knew how to do that. It's how we got so much brew here. That Doctor couldn't fix a person but knew how to get a still going."
    pcm "They talking about [ant.name]?"
    havmuff "...why he went over to those lot. Not just booze you can learn when going to doctor school. Load of other tricks as well so they wanted him over there to cook something up."
    havmuff "Think so? Didn't seem like he would be interested in that. Came here all noble but is just shit like all the rest."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_1")

    $ working(20)

    return
    $ haven_room_join_chance()
    jump travel

label haven_intel_2:
    havmuff "...like he had been in a fire. Come in 'ere like he owns the place claiming he would know better 'cos he is a Doctor or summit."
    pcm "Doctor. What about him?"
    havmuff "...probably running away 'cos he has some disease and they wanna lock him up 'fore he spreads it."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_2")

    $ working(20)

    return
    $ haven_room_join_chance()
    jump travel

label haven_intel_3:
    havgirl "...and it just won't stop even though it's been over a year since I gave birth. Tried speaking to that Doctor that came round here and..."
    pcm "Wait what? Speaking to the doctor?"
    havwhore "Don't the guys like it? I mean with the milk constantly coming out, don't they pay to milk you or something?"
    if player.has_perk(perk_preg_want):
        pcm "Mmmm, lucky girl."
    havgirl "Fuck them! I don't wanna be milked like a cow just so they can get off to it!"
    if player.has_perk(perk_preg_want):
        pcm "Sounds like fun to me..."
    havwhore "Well if it's happening, might as well take advantage and get paid for it. What the doc say about it anyway?"
    havgirl "No fucking clue. He was telling me it's because of this and that. Words that I don't understand even a bit of so it all went in one ear and..."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_3")

    $ working(10)
    return
    $ haven_shower_join_chance()
    jump haven_shower_listen_leave

label haven_intel_4:
    havgirl "...all over the place because of that issue but couldn't find the Doctor around here. Tried asking some of the girls..."
    pcm "Wait what? Looking for the Doctor?"
    havwhore "...went to speak to some of them over by the factories. It's probably why there is some bad blood."
    havgirl "Ugh, I don't care about that. I just need the help. Not like there is much choice anyway, unless you count some of the crazies that can heal by putting milk in your pussy..."
    havwhore "Ha, does anyone fall for that?"
    pcm "What the hell?"
    havgirl "...keep trying though so must have worked at least once. Who the hell knows with some of the addict whores round here seeing fairies and elephants..."
    "I try to catch any important information about [ant.name], but eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_4")

    $ working(10)
    return
    $ haven_shower_join_chance()
    jump haven_shower_listen_leave

label haven_intel_5:
    hav "Made me laugh. The shitty Doctor was all acting as if he found something that could give him back his old life. Discovering a new condition or something he could study..."
    pcm "Did I hear them say \"Doctor\"?"
    hav "...an it was just Fae layin there after takin more than she could handle. Probably off in her own world walking like he made up a new language."
    hav "The doc was goin' on like he discovered some new plague or somethin'. Talkin' 'bout how he can study it and get his life back."
    pcm "Are they serious?"
    "They keep making fun of [ant.name] until eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_5")

    $ working(10)
    return
    $ haven_shower_join_chance()
    jump haven_shower_listen_leave

label haven_intel_6:
    hav "...a chance in hell. That quack Doctor will probably want to chop it off or something. Rather go drink milk from the loonies before I go ask..."
    pcm "\"Quack Doctor\"?"
    hav "what he had that kid who ate the bird that got run over do for his stomach. Never seen someone's insides come out their mouth. That nut didn't even seem shocked and reacted as if he knew it would happen."
    "They go on for a while sharing horror stories about [ant.name] until eventually the conversation trails off onto other topics."
    $ haven_gained_intel("intel_6")

    $ working(10)
    return
    $ haven_shower_join_chance()
    jump haven_shower_listen_leave

label haven_intel_7:
    havgirl "...taking that stuff the weird doc told you to?"
    show haven_sleep conf
    pcm "Wait what? Weird doc?"
    havwhore "Yeah, not like I have any options."
    show haven_sleep peek
    havgirl "But something \"he\" told you to do? That fucking weirdo could be telling you any random shit to take."
    pcm "A doctor in this place can only be [ant.name]. No one else would come to this shithole."
    havwhore "...a better doctor and I'll be happy to see him, til then I am stuck doing what he told me to."
    pcm "Gave medical advice to her?"
    "I listen to the rest of their conversation until it trails off."
    $ haven_gained_intel("intel_7")

    $ working(10)
    return

label haven_intel_8:
    havwhore "...would I trust him? Calls himself a doctor but has some nasty stuff on his arms and body. Shouldn't he fix himself first?"
    show haven_sleep conf
    pcm "Doctor? Nasty stuff on his body. Could this be his patches?"
    havgirl "...you manage to find someone else willing to look at the whores in this place then tell me. Til then you don't have much choice."
    show haven_sleep peek
    havwhore "Fuck..."
    "I listen to the rest of their conversation until it trails off."
    $ haven_gained_intel("intel_8")

    $ working(20)
    return

label haven_intel_9:
    hav "What is that you have there? Hope that shit the doctor had wasn't contagious or something."
    pcm "Doctor? They talking about [ant.name]?"
    hav "Na, I fell over and got the skin scraped off. This ain't the same as that weird stuff patchy man had."
    pcm "Yes, sounds like they are talking about him."
    "I listen to their conversation. While muffled through the wall I manage to pick up most of the key details. But it isn't long before the topic moves on and there is no more of real interest."
    $ haven_gained_intel("intel_9")

    jump haven_room1_listen_end

label haven_intel_10:
    hav "...I know. I tried looking for that doctor guy to take a look at it."
    pcm "Doctor guy? Are they talking about [ant.name]?"
    "I listen to their conversation about weird infections they managed to get. There is some info about [ant.name] but mostly it is about their nasty bits."
    $ haven_gained_intel("intel_10")

    jump haven_room1_listen_end

label haven_intel_11:
    havmuff "...He told me to rub it on myself after the showers. Not like we got many doctors around 'ere so 'course I'd listen to him."
    pcm "Doctor? [ant.name]?"
    havmuff "But it still doesn't go away. I tried to track him down..."
    "I listen to the conversation about the whores nasty infections and try to pick up what I can about [ant.name]. Eventually the conversation changes topic and they carry on with uninteresting things."
    $ haven_gained_intel("intel_11")

    jump haven_room1_listen_end

label haven_intel_12:
    $ haven_gained_intel("intel_12")



    show haven_peeping talk brow_straight mouth_flat eye_back with dissolve
    pc "Before you get any funny ideas, I need to know if you have the info I want."
    havenpeeper.name "Well, let's hear it. What are you after."
    pc "I am looking for someone."
    havenpeeper.name "Ok... I need more."
    pc "Don't have much. Looking for someone who had patchy skin. Lots of pale patches all over his body."
    havenpeeper.name "Ah, the doctor?"
    show haven_peeping mouth_open brow_conf
    pc "What? You know him?"
    havenpeeper.name "Yeah."
    pc "Well, tell me what you know about him. Is he still here?"
    havenpeeper.name "Hmm, is he still here? Let me think"
    show haven_peeping grope_ass shorts_down with dissolve
    $ c.bottom = 0
    $ c.pants = 0
    havenpeeper.name "Mmmm, such a nice ass."
    pcm "Fuck, he is gonna drag this out until he gets everything he wants."
    show haven_peeping grope_tit with dissolve
    havenpeeper.name "I saw him around here for some time."
    pcm "..."
    havenpeeper.name "Patchy skin. Hair as well when it grew in. Usually kept it shaved though."
    havenpeeper.name "By the way. I love a shaved pussy. But hard to find girls around this place that can keep up the maintenance."
    havenpeeper.name "But I have taken a liking to your furry muff. And it aint often you find a girl with a plug in her arse."
    pc "Well, what about him? Where is he? What did he want?"
    havenpeeper.name "I'm just letting you know I aint a liar by telling you about him. You gotta pay the price first."
    pcm "Well, there goes any chance of getting the info early and backing out before he gets to fuck me."
    if not player.check_sex_agree(3):
        menu:
            "Back out of it now":
                pc "Sorry mate, I'm not willing to pay this price after all."
                "I hastily jump to my feet, pulling my shorts back up and rush out of the room"
                $ pc_dress()
                hide haven_peeping with dissolve
                $ walk(loc_haven_room1)
                pc "..."
                jump travel
            "Keep going":
                $ NullAction()
    pc "And what price do you want me to pay?"
    havenpeeper.name "Don't pretend like you don't know. You are a pervert whore so playing dumb doesn't work."
    pc "I am not a pervert whore."
    havenpeeper.name "Stop playing games. You are here spying on men in the shower with a giant plug up your arse and collard like a breeding bitch."
    show haven_peeping poke_out with dissolve
    $ c_top = 0
    havenpeeper.name "So let's stop pretending and have some fun. Play with my cock between your legs."
    pcm "..."
    show haven_peeping arm_mast with dissolve
    if player.has_perk(perk_preg_want) and player.check_sex_agree(3):
        show haven_peeping mouth_happy brow_straight
        pc "You gonna breed me like a bitch?"
        havenpeeper.name "You want that?"
        pc "Mmmmm."
        havenpeeper.name "Oh, more of a pervert that I thought. You want me to cum in you and give you a big fat belly?"
        pc "Oh yes!"
        havenpeeper.name "These tits in my hand full of milk. When you are being fucked like the whore bitch you are, you can have these milked like a cow?"
        if player.pregbabies > 0:
            pc "Yes, fuck me and put another baby in me."
            havenpeeper.name "Another? How many times you been knocked up?"
            if player.pregbabies == 1:
                pc "Only once. But at this rate I will be knocked up again."
            elif player.pregbabies == 2:
                pc "Twice. Maybe you will be the father of my third?"
            elif player.pregbabies == 3:
                pc "If you do a good job, yours will be the fourth."
            else:
                pc "A bunch of times. Perverts like you keep putting babies in me."
                havenpeeper.name "Fuuuuck. And you let them. Damn a dumb bitch like you is a god send to a place like this."
        else:
            pc "Yes, fuck a baby into me!"
        havenpeeper.name "Don't worry slut, I'll make sure to fill you up."
    elif player.check_sex_agree(2):
        show haven_peeping mouth_happy brow_straight
        pc "Mmmm, it's a big one. Something like that between my tiny pussy is a bit dangerous."
        if havenpeeper.vsex > 0:
            hav "Yeah, one that you already swallowed up like the little whore you are."
        else:
            hav "Considering what you have in your arse, I'm sure your pussy can manage."
        pc "You think so? I am not so sure. ♥"
        havenpeeper.name "Well let's see then shall we?"
    else:
        show haven_peeping mouth_flat brow_straight
        pc "Like this?"
        havenpeeper.name "Mmmm, I want to feel you putting my cock inside you."
    "I slide his cock against my lips with my hand, making sure it is all lubed up with my juices."
    $ player.sex_vag(havenpeeper, main_quest_05)
    show haven_peeping poke_in enjoy with dissolve
    pc "Haaaa fuck!"
    "He fucks me like an eager rabbit while groping at my tits. His groping is borderline painful but the excitement he is giving me down below makes it worth it."
    if player.has_perk(perk_preg_want):
        hav "You aren't fat yet, but these tits still need some milking."
    pc "Haaahaha... ♥ So nice!"
    havenpeeper.name "Ah that plug makes your pussy feel so tight!"
    pc "Mmmm, I can feel it. I thought I was full before but now it feels like I am about to burst."
    havenpeeper.name "Ah fuck yes, I'm gonna cum!"
    $ player.sex_cum_location_offer(
    difficulty=3, choice_inside="Keep going!", choice_pullout="Not inside.",  
    cum_want="haven_intel_12_cum_want", 
    cum_notwant="haven_intel_12_cum_notwant", 
    cum_pullout="haven_intel_12_pullout",   
    )

label haven_intel_12_pullout:
    if numgen():
        havenpeeper.name "Haaaaa..."
        show haven_peeping talk mouth_happy brow_straight eye_penis top_down mast with dissolve
        "He quickly pulls out and stands next to me, furiously jerking his cock."
        havenpeeper.name "Ha here it comes."
        show haven_peeping eye_closed mouth_tounge
        pc "Uuuhuuu. Gib it to me."
        show haven_peeping cum_face
        $ player.sex_cum(havenman, "face", main_quest_05)
        havenpeeper.name "Ahhhh yes! Haaaaaa..."
        "Feeling his warm cum spray over my face brings me over the edge as well and I start to cum with my fingers between my legs."
        pc "Mmmmmmm. ♥ Haaaaa. "
        show haven_peeping eye_man mouth_happy arm_wall shorts_down with dissolve
        pc "..."
        havenpeeper.name "Ahhh that was great."
    else:
        pc "Ah fuck yes. Cum all over my arse. I want to feel you spraying it on me."
        havenpeeper.name "Haa haa aaa."
        pc "Keep goooo... Nnnnng..."
        show haven_peeping grope_tit shorts_down top_down with dissolve
        $ player.sex_cum(havenman, "ass", main_quest_05)
        havenpeeper.name "Yesssss! Haaaaaaa."
        pc "Haaa ♥ Yessss."
        pc "Mmmmmmm. ♥ Haaaaa. "
        pc "..."
        havenpeeper.name "Ahhh that was great."
        show haven_peeping talk eye_back mouth_flat brow_straight
        pc "Phew..."
        "I sit for a bit trying to catch my breath while the cum on my arse trickles down to the plug in my ass."
        pc "..."
    jump haven_intel_12_continue

label haven_intel_12_cum_notwant:
    havenpeeper.name "Haaaa too late for that. Ahhhhh!"
    show haven_peeping talk brow_worried eye_back mouth_shocked
    pc "Whaa wait no..."
    $ player.sex_cum(havenman, "inside", main_quest_05)
    havenpeeper.name "Yesssss! Haaaaaaa."
    "I give up and just carry on masturbating with his cock cumming inside me."
    show haven_peeping eye_closed mouth_happy brow_straight
    pc "Haaa ♥ Yessss."
    pc "Mmmmmmm. ♥ Haaaaa. "
    pc "..."
    havenpeeper.name "Ahhh that was great."
    show haven_peeping poke_out arm_wall shorts_down with dissolve
    pc "Mmmm."
    pc "But if you got me pregnant I will come back here and stab you in the eye while you are looking through the hole."
    havenpeeper.name "Ah sorry, you asked too late. And don't say shit like that with such a smile on your face. It's creepy."
    show haven_peeping eye_back mouth_flat
    pc "..."
    pc "Whatever."
    jump haven_intel_12_continue

label haven_intel_12_cum_want:
    pc "Keep fucking! I am not ready yet. Closeeeee. ♥"
    havenpeeper.name "Haa haa aaa."
    pc "Keep goooo... Nnnnng..."
    $ player.sex_cum(havenman, "inside", main_quest_05)
    havenpeeper.name "Yesssss! Haaaaaaa."
    pc "Haaa ♥ Yessss."
    pc "Mmmmmmm. ♥ Haaaaa. "
    pc "..."
    havenpeeper.name "Ahhh that was great."
    show haven_peeping poke_out arm_wall shorts_down with dissolve
    pc "Mmmm."
    show haven_peeping talk eye_back mouth_flat brow_straight
    pc "Phew..."
    "I sit for a bit trying to catch my breath while the cock inside me slowly softens and pops out followed by his cum leaking out of me."
    pc "..."
    jump haven_intel_12_continue

label haven_intel_12_continue:
    pc "Now, you got the fucking you wanted. Tell me what I want to know. This doctor with the patchy skin."
    "I sit there waiting as he dressed up."
    show haven_peeping talk eye_man mouth_flat brow_straight catch arm_wall shorts_down top_down with dissolve
    havenpeeper.name "Ok, well..."
    "And spend the next 5 minutes or so listening to his story about [ant.name]. It is not very informative but it follows the same pattern as the other bits of info I have heard."
    havenpeeper.name "That's about everything. Anything else you will have to get off other people. You might want to spy on the girls some more though since he dealt with their... Whore issues, let's call them."
    pc "You just want to catch me here again don't you?"
    if player.has_perk(perk_preg_want):
        havenpeeper.name "Sure, I would be happy to make sure you leave this place with a baby in your belly."
    elif player.has_perk(perk_preg_notwant):
        havenpeeper.name "Of course. Any girl who's face I can cum all over is someone I want to meet again."
    else:
        havenpeeper.name "Of course. I have loved our little pervert games. Not every day some hot whore as dirty as me comes to play."
    pc "We will see ♥"
    show haven_peeping noman with dissolve
    pcm "Better get decent myself."
    $ pc_dress()
    hide haven_peeping with dissolve
    if player.cum_visible:
        pcm "Should probably wash up though. Can't walk around with people seeing cum on me."
    $ haven_gained_intel("intel_12")

    jump travel

label haven_intel_13:
    show haven_guard1 at right1 with dissolve
    havengateguard.name "Keeping out of trouble?"
    pc "Only some of the time. How you keeping?"
    havengateguard.name "Same as."
    havengateguard.name "You know, I remember a patchy skin guy here a while ago."
    pc "Yeah?"
    havengateguard.name "Yeah, dunno much about it but I remember opening the gate for him a few times. Him and [alex.nname] had some stuff to chat about I guess."
    pc "Ah really? Not seem him recently?"
    havengateguard.name "Na, it was a while ago. But I only guard up here so he could be downstairs right now and I wouldn't know."
    pc "Ah, well thanks for telling me anyway. I'll have another look around."
    havengateguard.name "Good luck"
    hide haven_guard1 with dissolve
    $ havengateguard.dict["times_spoke"] += 1
    $ haven_gained_intel("intel_13")

    jump travel

label haven_intel_14:
    "I search around in the bed to see if there is anything worth taking."
    pcm "Not a lot here. Some bottles of what looks like... Pills I guess. But clearly not factory made. Looks more like packed plant matter than actual pills."
    pcm "Hold on..."
    pcm "A note giving instructions on what these are and how often to take them. Whoever is using these has some kind of infection or whatever. Doesn't matter."
    pcm "But whoever wrote this note is obviously giving medical advice to her. Wonder if it could be [ant.name]? I haven't seen any evidence to suggest that there are any other medical people around here."
    pcm "Anyway nothing worth taking from here."
    $ haven_gained_intel("intel_14")

    $ haven_bedroom_search_caught()
    $ working(10)
    jump travel

label haven_intel_15:
    havgirl "...so I looks over again and I was right. It was that patchy Doctor who was here for a while walking out of the..."
    pcm "Wait, she is talking about [ant.name]."
    havgirl "...he didn't notice me, or didn't even remember me. Bit hard to miss that face of his even with the scarf covering it up."
    havgirl "Thought I could earn a bit of cash off of [alex.nname] by sellin the info to him, but he already knew. Fuck thought it would be looking up..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_15")

    jump travel

label haven_intel_16:
    havgirl "...no better than the milkmen. Calls himself a Doctor but I don't remember him helping out much. Just struttin' around with the backing of..."
    pcm "Wait, she is talking about [ant.name]."
    havgirl "...probably, but you think he cares? He was able to live in this shithole like some king. Well, that was until..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_16")

    jump travel

label haven_intel_17:
    hav "...an I'm sure he just pulled some grass off his shoe, mixed it in water and tried to pass it off as medicine. Yeah right, I ain't taking that stuff you just palmed off as..."
    pcm "Medicine? They might be talking about [ant.name]."
    hav "...the old \"wait until they aren't looking and throw it over your shoulder\". He never noticed and seemed all proud that I drank his horseshit!"
    hav "I'm just there nodding as if I am listening, just waiting for him to shut up so I can..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_17")

    jump travel

label haven_intel_18:
    hav "...just messed up my leg. But for some reason the Doctor was making me drink this weird stuff. What can I say? Not like I know what it might do or..."
    pcm "Doctor? They might be talking about [ant.name]."
    hav "...did, why would I say no? But I don't remember it doing any good. So went to look for him again and tell him but I had no idea where..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_18")

    jump travel

label haven_intel_19:
    hav "...tried to sell that doctor some of the herbs I found. He just laughed at me and tried telling me how he went to this University or has that diploma..."
    pcm "Doctor? They might be talking about [ant.name]."
    hav "...give a shit. Show me what happened to those places. Show me what those names mean. He was pissed. Shouting at me about how back in the day people used to have pride or some sh..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_19")

    jump travel

label haven_intel_20:
    hav "...couldn't believe it. And that so called doctor is just standing there like \"Hmmmmm\". What the fuck? Do something ab..."
    pcm "Doctor? They might be talking about [ant.name]."
    hav "...standing there saying about how it looks like he broke his leg in this place or that place. Err, yeah anyone could tell that. His foot is pointing in the wrong directi..."
    "I listen to their conversation while trying to look like I am just hanging around. But eventually the topic changes and I move on."
    $ haven_gained_intel("intel_20")

    jump travel
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
