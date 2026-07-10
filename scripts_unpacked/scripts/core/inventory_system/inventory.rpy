init python:

    class Item(store.object):
        def __init__(self, name, desc, class_name, use_notif=None, value=100, type="item", icon=None, act=None, stackable=False,
            skirt=False, clevage=False, belly=False, ass=False, thong=False, slutty=False, nips=False, braless=False, bra_nolift=False, pantsless=False, pokenips=False, hair="", fringe=True, outfit=[],
            perverted=False, sexual=False, gagged=False, covers_bottom=False, covers_top=False, exposed_nips=False, exposed_vag=False, exposed_ass=False,
            locked=False, locked_always=False
            ):
            self.name = name
            self.desc = desc
            self.class_name = class_name
            self.use_notif = use_notif
            self._icon = icon
            self._act = act
            self.value = value               
            self.type = type 
            self._stackable = stackable 
            self.used = 0 
            self._last_used = 0 
            self.locked = locked 
            self.locked_always = locked_always 
            
            
            
            
            self.clothes = False 
            self.clothes_tab = ""
            self.clothes_number = 0
            
            self._outfit = outfit 
            
            self.hat_hair = hair
            self.hat_fringe = fringe   
            
            self.skirt = skirt 
            self.clevage = clevage 
            self.belly = belly 
            self.ass = ass 
            self.braless = braless 
            self.bra_nolift = bra_nolift 
            self.pantsless = pantsless 
            self.thong = thong 
            self.slutty = slutty 
            self.pokenips = pokenips 
            self.covers_bottom = covers_bottom 
            self.covers_top = covers_top 
            self.sexual = sexual 
            self.perverted = perverted 
            self.gagged = gagged
            
            
            
            
            
            
            self.exposed_nips = exposed_nips
            self.exposed_vag = exposed_vag
            self.exposed_ass = exposed_ass
            
            
            
            
            self.clothes_check()
            self.clothes_add_to_list()
            self.item_add_to_list()
            self.clothes_outfit_setter()  
        
        @property
        def act(self):
            if not self._act:
                action = self.class_name + "_action"
                if not renpy.has_label(action):
                    action = "item_none_action"
            else:
                action = self._act
            if self.clothes:
                return clothes_set(self.clothes_tab, self.clothes_number)
            else:
                return [Hide("inventory_screen"), Show("travel_screen"), Hide("wardrobe_text"), SetVariable("item_inv_call", True), Jump(action)]
        @property
        def icon(self):
            if self._icon:
                return self._icon
            else:
                return self.class_name
        
        @property
        def stackable(self):
            if self.type in ["consumable", "junk"]:
                return True
            elif self._stackable:
                return True
            else:
                return False
        
        @property
        def outfit(self):
            return self._outfit
        
        @property
        def last_used(self):
            if self._last_used:
                return t.hours_total - self._last_used
            else:
                return 0
        
        def clothes_outfit_setter(self):
            if self.clothes and not self._outfit:
                if not self.type in ["outfit", "top", "bottom"]:
                    self._outfit = ["school", "daily", "party", "sport", "home"]
                else:
                    self._outfit = ["daily", "party", "home"]
        
        def clothes_check(self):
            if any(substring in self.class_name for substring in clothes_list):
                self.clothes = True
                self.clothes_tab = "".join([i for i in self.class_name if not i.isdigit()]).replace("item", '').replace("_", "")
                self.clothes_number = int(''.join(filter(str.isdigit, self.class_name)))
            
            else:
                return False
        def clothes_add_to_list(self):
            if self.clothes:
                add_to_list(item_clothes_list, self)
        
        def item_add_to_list(self):
            if not (self.clothes or self.type == "mission"):
                add_to_list(item_list, self)

    class Inventory(store.object):
        def __init__(self, name="", money=0):
            self.name = name  
            self.money = money            
            self.inv = []  
            self.shop_list = []
            self.sort_by = self.sort_name
            self.sort_order = True 
            self.grid_view = True
            
            self.open = True 
            self.discount = 1 
            self.percent = None 
            self.list = []
            self.dict = {}
        
        
        def add_to_shop_list(self):
            global shop_list
            add_to_list(shop_list, self)
        
        def buy(self, item):            
            
            self.take(item)  
        
        def stock(self, percent=100):
            if not hasattr(self, 'percent'): 
                self.percent=None
            if not self.percent:
                self.percent = percent
            self.empty(junk=False)
            for i in self.shop_list:
                if not isinstance(i, list):
                    i = [i, 1]
                if not i[0].locked:
                    for q in range(i[1]):
                        if numgen(1, 100) <= self.percent:
                            self.take(i[0], 1)
            
            if self.shop_list and not self.inv:
                
                self.stock()
            self.add_to_shop_list()  
        
        def add_to_stock(self, item, amount, percent=100):
            add_to_list(self.shop_list, [[item, amount]])
            self.stock(percent)
        
        def does_stock(self, item):
            
            for sublist in self.shop_list:
                if not isinstance(sublist, list):
                    
                    sublist = [sublist]
                if item in sublist:
                    return True
            else:
                return False
        
        
        def check(self, item):
            if self.qty(item):
                for i in self.inv:
                    if i[0] == item:        
                        return self.inv.index(i) 
        
        def check_type(self, what_type):
            global tab_top
            tab_top_new = re.sub('[0-9]', '', tab_top)
            type_list = []
            for item in self.inv:
                
                if item[0].type == what_type and (tab_top_new in item[0].outfit or "shop" in tab_top):
                    if item[0].clothes:
                        if item[0].clothes_number != 0:  
                            return True
                    else:
                        return True
                elif item[0].type == what_type and self == inv:
                    return True
        
        
        def check_recipe(self, item): 
            checklist = list()
            for i in item.recipe:
                if self.qty(i[0]) >= i[1]:
                    checklist.append(True)
            if len(checklist) == len(item.recipe):
                return True
            else:
                return False        
        
        def craft(self, item):
            for line in item.recipe:
                self.drop(line[0], line[1])
            self.take(item)  
            message = "Crafted a %s!" % (item.name)
            renpy.show_screen("inventory_popup", message=message)   
        
        def deposit(self, amount):
            self.money -= amount   
        
        def use(self, item, qty=1, notif=True, notif_message=None):
            if self.qty(item):
                item.used += 1
                item._last_used = t.hours_total
                if notif and self == inv and item.use_notif:
                    message = item.use_notif
                    show_notif_popup(message)
                elif notif_message:
                    show_notif_popup(notif_message)
                item_location = self.check(item)
                if self.inv[item_location][1] > qty:
                    self.inv[item_location][1] -= qty
                else:
                    del self.inv[item_location] 
        
        def drop(self, item, qty=1, notif=False, notif_message=None):
            if not isinstance(item, list):
                item = [item]
            for i in list(item):
                if self.qty(i):
                    item_location = self.check(i)
                    if self.inv[item_location][1] > qty:
                        self.inv[item_location][1] -= qty
                    else:
                        del self.inv[item_location]  
                    if self is wardrobe and i.clothes and i.type in clothes_wardrobe_list:
                        for q in clothes_tab_all_list:
                            if getattr(globals()[q], i.type) == i.clothes_number:
                                setattr(globals()[q], i.type, 0)
                    if notif:
                        if notif_message == None:
                            notif_message = "Lost " + i.name
                        show_notif_popup(notif_message)
        
        def drop_clothes(self, slot, tab=None, notif=True, notif_message=None):
            
            global tab_top
            if tab == None:
                tab = tab_top
            tab = get_outfit_class(tab)
            
            if not isinstance(slot, list):
                slot = [slot]
            
            for i in slot:
                self.drop(globals()["item_" + i + "_" + str(getattr(tab, i))], notif=notif, notif_message=notif_message)
        
        def qty(self, item):
            for i in self.inv:
                if i[0] == item:
                    if i[1] and not i[0].stackable:
                        return 1
                    else:
                        return i[1] 
            else:
                return 0
        
        
        def give(self, item, who, qty=1):
            self.drop(item, qty)
            who.take(item, qty)
        
        def sell_junk(self, item, what_inv):
            if item.type == "junk" or item == item_cigs:
                player.add_money((item.value * self.qty(item)))
                what_inv.take(item, self.qty(item))
                self.drop(item, self.qty(item))
            else:
                player.add_money(((int(item.value * 0.7))))
                what_inv.take(item, 1)
                self.drop(item, 1)
        
        
        def sort_name(self):
            self.inv.sort(key=lambda i: i[0].name, reverse=self.sort_order)
        
        def sort_qty(self):
            self.inv.sort(key=lambda i: i[1], reverse=self.sort_order)
        
        def sort_value(self):
            self.inv.sort(key=lambda i: i[0].value, reverse=self.sort_order)
        
        def sort_clothes(self):
            self.inv.sort(key=lambda i: i[0].clothes_number, reverse=False)
        
        def take(self, item, qty=1, notif=True, all_notif=False, dress=False):
            if not qty:
                return
            if self.qty(item):
                item_location = self.check(item)            
                self.inv[item_location][1] += qty                  
            else:
                self.inv.append([item,qty])  
            if item.locked and self == wardrobe:
                
                item.locked = False
            if (notif and self == inv) or all_notif:
                message = "Got " + If(qty > 1, str(qty), "") + " " + item.name
                show_notif_popup(message)
            if dress and self == wardrobe:
                
                setattr(globals()[tab_top], str(item.type), int(re.sub("[^0-9]","",item.class_name)))
                setattr(c, str(item.type), int(re.sub("[^0-9]","",item.class_name)))
                return "Dress"
        
        def empty(self, junk=True):
            for item in self.inv[:]:
                if item[0].type == "junk":
                    if junk:
                        self.drop(item[0], item[1])
                    continue
                else:
                    self.drop(item[0], item[1])
        
        def withdraw(self, amount):
            self.money += amount
        
        def value(self, discount=0):
            amount = 0
            if not self.inv:
                return 0
            for item in self.inv:
                subtotal = item[0].value * item[1]
                amount += subtotal * (1 - discount / 100)
            
            return int(amount)
        
        def value_junk(self): 
            amount = 0
            if not self.inv:
                return 0
            for item in self.inv:
                if item[0].type == "junk":
                    amount += item[0].value * item[1]
            return amount
        
        def add_inv_to_value(self, value=10):
            items = []
            for i in item_list:
                if not i.type == "mission":
                    items.append(i)
            for i in item_clothes_list:
                if not wardrobe.qty(i) and not (i.locked or i.locked_always):
                    items.append(i)
            while self.value() < value:
                self.take(random(items))

    def inv_value(what_inv, discount=0):
        amount = 0
        for item in what_inv.inv:
            amount += (item[0].value * item[1])-((item[0].value * item[1])*discount/100)
        return amount

    def inv_return(what_inv):
        amount = 0
        for item in buy_inv.inv[:]:
            what_inv.take(item[0], item[1])
            buy_inv.drop(item[0], item[1])

    def inv_buy(discount):
        player.remove_money(inv_value(buy_inv, discount)) 
        for item in buy_inv.inv[:]:
            if item[0].clothes:
                wardrobe.take(item[0], item[1])
            else:
                inv.take(item[0], item[1])
            buy_inv.drop(item[0], item[1])

    def inv_transfer(inv_from, inv_to):
        for item in inv_from.inv[:]:
            inv_to.take(item[0], item[1], notif=False)
            inv_from.drop(item[0], item[1])

    def inv_transfer_to_player(inv_from, notif=True):
        for item in inv_from.inv[:]:
            if item[0].clothes:
                wardrobe.take(item[0], item[1], all_notif=notif)
            else:
                inv.take(item[0], item[1], notif=notif)
            inv_from.drop(item[0], item[1], notif=False)

    def inv_remove_items(what_inv, what_list):
        for item in what_inv.inv[:]:
            if item[0] in what_list:
                inv_from.drop(item[0], item[1])






define inv_tab_left = "consumable"

screen inventory_tableft_button(text_title, text_desc, tab, what_inv=inv, force_show=False):
    if what_inv.check_type(tab) or force_show:
        frame padding (0,0) xysize (82,80) background None:
            add "button_wardrobe_tab_bg"
            add "button_inv_tab_" + tab:
                if inv_tab_left != tab:
                    matrixcolor TintMatrix(wardrobe_colour_selected)

            imagebutton auto "button_wardrobe_tab_frame_%s":
                hovered Show("wardrobe_text", text_title=text_title, text_desc=text_desc),
                unhovered Hide("wardrobe_text"),
                action [SetVariable ("inv_tab_left", tab)]

screen inventory_button(item):
    frame padding (3,3) xysize (126, 80) background None:
        add item[0].icon pos (1,1)
        if item[1] > 1 and item[0].stackable:
            text "[item[1]]" anchor (0.0,1.0) align (0.05,1.0) size 18
        imagebutton auto "button_items_frame_%s":
            action item[0].act
            hovered Show("wardrobe_text", text_title=item[0].name, text_desc=item[0].desc)

            unhovered Hide("wardrobe_text")

screen inventory_buy_button(item, what_inv, discount, show_locked):

    frame padding (3,3) xysize (126, 80) background None:
        $ price = ((item[0].value)-(item[0].value*discount/100))
        if ((inv.qty(item[0]) or buy_inv.qty(item[0])) and not item[0].stackable) or ((wardrobe.qty(item[0]) or buy_inv.qty(item[0])) and item[0].clothes):
            add item[0].icon pos (1,1) matrixcolor SaturationMatrix(0)
            add "button_items_owned"
        else:
            add item[0].icon pos (1,1)
            text "[item[1]]" anchor (0.0,1.0) align (0.05,1.0) size 18
            text "£[price]" anchor (1.0,1.0) align (0.95,1.0) size 18


            imagebutton:
                idle "button_items_frame_idle"
                hover "button_items_frame_hover"
                action [
                    Function(what_inv.drop, item[0]), 
                    Function(buy_inv.take, item[0]), 
                    Show("wardrobe_text", text_title=item[0].name, text_desc=item[0].desc)
                    ]

screen inventory_display_button(item, what_inv, discount):
    frame padding (3,3) xysize (126, 80) background None:
        $ price = ((item[0].value)-(item[0].value*discount/100))

        add item[0].icon pos (1,1)
        text "[item[1]]" anchor (0.0,1.0) align (0.05,1.0) size 18
        text "£[price]" anchor (1.0,1.0) align (0.95,1.0) size 18
        imagebutton:
            idle "button_items_frame_idle"
            hover "button_items_frame_hover"
            action [
                Function(buy_inv.drop, item[0]), 
                Function(what_inv.take, item[0]), 
                Show("wardrobe_text", text_title=item[0].name, text_desc=item[0].desc)
                ]

screen inventory_screen_return(x=0.25, y=0.5):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":
            action [Hide("inventory_screen"), Hide("inventory_popup"), Hide("wardrobe_text"), SetVariable("inv_tab_left", "consumable"), Show("travel_screen"), Function(player.face_normal)],

screen inventory_screen(what_inv=inv):
    vbox anchor (0,0) align (0.3,0.095) spacing 3:
        frame xsize 970:
            has hbox yoffset 3
            text "MY INVENTORY" size 35 font "BRLNSB.TTF"

        frame xysize (970,837):
            has hbox
            vbox:
                use inventory_tableft_button("CONSUMABLES", "Items that are consumed when used. Food, drink, cigarettes and the like.", "consumable", force_show=True)
                use inventory_tableft_button("TOOLS", "I have collected an assortment of tools and other objects. I keep them here.", "tool")
                use inventory_tableft_button("JUNK", "Junk and scrap I have managed to collect and can probably sell on.", "junk")
                use inventory_tableft_button("MISSION ITEMS", "Things I have gathered while on a mission. Probably only useful for that specific mission.", "mission")
            hbox:
                box_wrap True
                for i in inv.inv:
                    if getattr(i[0], "type") == inv_tab_left:
                        use inventory_button(i)




    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        $ NullAction()

    use inventory_screen_return()

screen inventory_itemshop_screen_return(what_inv, x=0.25, y=0.5):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        add "action_return" anchor (0.5,0.5) align (0.5,0.5)
        imagebutton auto "action_button_%s":

            action [Function(inv_return, what_inv), Hide("inventory_itemshop_screen"), Hide("inventory_popup"), Hide("wardrobe_text"), Return(_return)],

screen inventory_itemshop_screen_buy(discount=0, x=0.25, y=0.42):
    frame padding (0,0) align (x,y) xysize (61,61) background None:
        if player.cash >= inv_value(buy_inv, discount):
            add "action_buy" anchor (0.5,0.5) align (0.5,0.5)
            imagebutton auto "action_button_%s":
                action [Function(inv_buy, discount)],
        else:
            add "action_button_grey" anchor (0.5,0.5) align (0.5,0.5)
            add "action_buy" anchor (0.5,0.5) align (0.5,0.5)

screen inventory_itemshop_screen(what_inv, discount=0, show_locked=False):
    vbox anchor (0,0) align (0.3,0.095) spacing 3:
        frame xsize 970:
            has hbox yoffset 3
            if what_inv.name:
                text what_inv.name.upper() size 35 font "BRLNSB.TTF"
            else:
                text "SHOP INVENTORY" size 35 font "BRLNSB.TTF"
            if discount:
                $ temp_var_1 = "{:+}".format(-discount)
                text "[temp_var_1]%" size 35 font "BRLNSB.TTF" xpos 40

        frame xysize (970,410):

            has viewport
            scrollbars "vertical"
            vscrollbar_unscrollable "hide"
            draggable True
            mousewheel True
            hbox:
                box_wrap True
                for item in what_inv.inv:
                    if not (item[0].locked or item[0].locked_always) or show_locked:
                        if not item[0].type == "junk":
                            use inventory_buy_button(item, what_inv, discount, show_locked)

        frame xsize 970:
            has hbox yoffset 3
            $ price = str(inv_value(buy_inv, discount))
            if player.cash >= inv_value(buy_inv, discount):
                text "MY ITEMS £[price]" size 35 font "BRLNSB.TTF" xpos 5
            else:
                text "MY ITEMS {color=#f00}£[price]{/color}" size 35 font "BRLNSB.TTF" xpos 5

        frame xysize (970,360):
            has hbox
            box_wrap True
            for i in buy_inv.inv:
                use inventory_display_button(i, what_inv, discount)


    frame anchor (0.0,0.0) align (0.82,0.095) xysize (330,900):
        $ NullAction()


    use inventory_itemshop_screen_buy(discount)
    use inventory_itemshop_screen_return(what_inv)

screen inventory_clothes_choice(choices=[]):
    hbox align (0.5,0.4):
        for i in choices:
            use wardrobe_take_choice_button(i)

screen inventory_junk_sell_choice(item, what_inv):
    frame padding (0,0) xysize (126, 80) background None:
        add item.icon pos (1,1)
        text str(inv.qty(item)) align (0.0, 0.95) size 18
        imagebutton auto "button_items_frame_%s":
            action [Hide("choice_text"), Function(inv.sell_junk, item, what_inv)]
            hovered Show("choice_text", text_desc="Sell " + str(inv.qty(item)) + " " + item.name),
            unhovered Hide("choice_text"),


screen inventory_junk_choice(what_inv, choices=[]):
    hbox align (0.5,0.4):
        for i in choices:
            if inv.qty(i):
                use inventory_junk_sell_choice(i, what_inv)
        frame padding (0,0) xysize (126, 80) background None:
            add "item_return" pos (1,1)
            imagebutton auto "button_items_frame_%s":
                action [Hide("choice_text"), Function(Return)]
                hovered Show("choice_text", text_desc="Return"),
                unhovered Hide("choice_text"),

screen inventory_gift_choice(choices=[item_beer, item_map_pill, item_abort_pill, item_joy, item_pepperspray]):
    hbox align (0.5,0.4):
        for i in choices:
            if inv.qty(i):
                use inventory_gift_give_choice(i)
        frame padding (0,0) xysize (126, 80) background None:
            add "item_return" pos (1,1)
            imagebutton auto "button_items_frame_%s":
                action [Hide("choice_text"), Function(Return)]
                hovered Show("choice_text", text_desc="Return"),
                unhovered Hide("choice_text"),

screen inventory_gift_give_choice(item):
    frame padding (0,0) xysize (126, 80) background None:
        add item.icon pos (1,1)
        imagebutton auto "button_items_frame_%s":
            action [Hide("choice_text"), Function(inv.drop, item, notif=False), Function(buy_inv.take, item, notif=False), Function(Return)]

            hovered Show("choice_text", text_desc="Give " + item.name),
            unhovered Hide("choice_text"),

screen inventory_popup(message):
    zorder 100
    frame:
        style_group "invstyle"
        has hbox
        text message
    timer 1.5 action Hide("inventory_popup")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
