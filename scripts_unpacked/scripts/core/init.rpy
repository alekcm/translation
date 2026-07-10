
init python:

    import gc
    import copy
    import inspect
    import queue
    import math
    import re
    import random
    from collections import OrderedDict


    def class_updater(class_parent, new_variables, result=0):  
        for obj in gc.get_objects():
            if isinstance(obj, class_parent):
                if isinstance(new_variables, tuple) or isinstance(new_variables, list):
                    for i in new_variables:
                        setattr(obj,i,result)
                else:
                    setattr(obj,new_variables,result)

    def all_class_list(list, var, result):
        for i in list:
            setattr(i,var,result)

    def class_list_creator(class_parent, new_list, variable=None, result=None):
        globals()[new_list] = class_list_getter(class_parent, new_list, variable, result)

    def class_list_getter(class_parent, new_list, variable, result):
        new_list = []
        for obj in gc.get_objects():
            if isinstance(obj, class_parent):
                if not variable==None:
                    if getattr(obj, variable) == result and not obj in new_list:
                        new_list.append(obj)
                else:
                    new_list.append(obj)
        return new_list

    if renpy.variant("web"):
        config.autosave_on_choice = False

    def irange(start,end):
        return range(start, end + 1)

    def numgen(amount1=0, amount2=1):
        if amount2 <= amount1:
            amount2 = amount1 + 1
        amount = renpy.random.randint(amount1, amount2)
        return amount

    def clamp(n, minn, maxn):
        return max(min(maxn, n), minn)  

    def percent_scaler(minn, maxn, valuen, reverse=False, floatn=False):
        final = clamp(((valuen - minn) * 100) / (maxn - minn), 0, 100)
        if reverse:
            final = 100 - final
        if floatn:
            final = float(final) / 100
        return final

    def weightgen(amount1=100, amount2=100):
        choice = WeightedChoice([
        (True, amount1),
        (False, amount2)
        ])
        return choice  

    def random(what):
        return renpy.random.choice(what)

    def round_num(x, base=5):
        return int(base * round(float(x)/base))

    def if_showing(image1, layer1, image2="none", layer2="none", image3="none", layer3="none", image4="none", layer4="none", image5="none", layer5="none",image6="none", layer6="none",image7="none", layer7="none", trans=dissolve):
        
        found = False
        if renpy.showing(image1):
            renpy.show(image1 + " " + layer1)
            found = True
        if renpy.showing(image2) and not image2 == "none":
            renpy.show(image2 + " " + layer2)
            found = True
        if renpy.showing(image3) and not image3 == "none":
            renpy.show(image3 + " " + layer3)
            found = True
        if renpy.showing(image4) and not image4 == "none":
            renpy.show(image4 + " " + layer4)
            found = True
        if renpy.showing(image5) and not image5 == "none":
            renpy.show(image5 + " " + layer5)
            found = True
        if renpy.showing(image6) and not image6 == "none":
            renpy.show(image6 + " " + layer6)
            found = True
        if renpy.showing(image7) and not image7 == "none":
            renpy.show(image7 + " " + layer7)
            found = True
        if found:
            renpy.with_statement(trans)
        return found

    def layer_list(layer="master"): 
        image_list = []
        get_image_list = renpy.game.context().images.shown.copy()
        while len(get_image_list):
            item = get_image_list.pop()
            image_layer, image_name = item
            if image_layer == layer:
                image_list.append(image_name)
        return image_list

    def any_image_showing():
        
        
        if len(layer_list()):
            return True
        else:
            return False

    def image_showing(imagename, layer="master", sub_string=False): 
        
        
        
        
        
        
        full_string = "\t".join(layer_list(layer))
        if imagename in full_string:
            return True
        else:
            return False        

    def WeightedChoice(choices):
        """
        @param choices: A list of (choice, weight) tuples. Returns a random
        choice (using renpy.random as the random number generator)
        """
        totalweight = 0.0
        for choice, weight in choices:
            totalweight += weight
        randval = renpy.random.random() * totalweight
        for choice, weight in choices:
            if randval <= weight:
                return choice
            else:
                randval -= weight

    def label_callback(name, abnormal):
        store.last_label = name

    config.label_callback = label_callback


    randgen = renpy.random.random()

    def layerlist(layername):
        orderedset = []
        showingset = renpy.game.context().images.shown.copy()
        while len(showingset) > 0:
            item = showingset.pop()
            thelayer,thename = item
            if thelayer == layername:
                orderedset.append(thename)
        return orderedset
init -1:

    transform text_hov_fade:
        on show:
            alpha 0.0
            easein 0.25 alpha 1.0
    transform text_hov_fadeout:
        on show:
            alpha 1.0
            easeout 3.0 alpha 0.0
    transform icon_fadeout:
        on show:
            alpha 1.0
            easeout 1.0 alpha 0.0


    transform right1:
        xalign 0.95 yalign 1.0 xzoom 1
    transform right2:
        xalign 0.8 yalign 1.0 xzoom 1
    transform right3:
        xalign 0.65 yalign 1.0 xzoom 1
    transform right4:
        xalign 0.5 yalign 1.0 xzoom 1
    transform right5:
        xalign 0.35 yalign 1.0 xzoom 1
    transform right6:
        xalign 0.2 yalign 1.0 xzoom 1
    transform left_tutorial:
        xalign 0.18 yalign 1.0 xzoom 1
    transform left1:
        xalign 0.2 yalign 1.0 xzoom -1
    transform left2:
        xalign 0.35 yalign 1.0 xzoom -1
    transform left3:
        xalign 0.50 yalign 1.0 xzoom -1
    transform left4:
        xalign 0.65 yalign 1.0 xzoom -1

    transform rightover:
        xalign 1.2 yalign 1.0 xzoom 1
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
