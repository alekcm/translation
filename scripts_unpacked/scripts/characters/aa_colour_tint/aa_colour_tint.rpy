"Auto Highlight Ren'Py Module 2021 Daniel Westfall <SoDaRa2595@gmail.com>"
"http://twitter.com/sodara9 I'd appreciate being given credit if you do end up using it! :D Would really make my day to know I helped some people out! http://opensource.org/licenses/mit-license.php Github: https://github.com/SoDaRa/Auto-Highlight itch.io: https://wattson.itch.io/renpy-auto-highlight"




























"Setup (IMPORTANT)"


























"General Note"





"Variables"







define sprite_focus = {}






default speaking_char = None

default test_name_test = None
"Transforms"





transform sprite_highlight(sprite_name):

    function SpriteFocus(sprite_name)

init -10 python:

    import renpy.store as store
    import renpy.exports as renpy


    class Link(store.object):      
        pass


    def name_callback(event, interact=True, name=None, **kwargs):   
        global speaking_char
        if event == "begin":
            
            speaking_char = name


    class SpriteFocus(Link):
        
        
        
        def __init__(self, char_name):
            global test_name_test
            test_name_test = char_name
            if char_name in globals() and isinstance(globals()[char_name], Npc):
                self.char_name = globals()[char_name].setname.lower()
            else:
                self.char_name = char_name
        
        
        
        
        
        
        def __call__(self, trans, start_time, anim_time):
            
            def get_ease(t):
                return .5 - math.cos(math.pi * t) / 2.0
            
            global sprite_focus, speaking_char 
            char_name = self.char_name 
            
            if char_name not in sprite_focus:
                sprite_focus[char_name] = False
            anim_length = 0.2       
            bright_change = 0.2    
            sat_change = 0.0        
            zoom_change = 0.0025    
            
            
            
            
            
            y_change = 1            
            
            
            
            is_talking = speaking_char == char_name
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if isinstance(sprite_focus[char_name], (int, float)) and anim_time < sprite_focus[char_name]:
                sprite_focus[char_name] = is_talking
            
            if sprite_focus[char_name] != is_talking and isinstance(sprite_focus[char_name], bool):
                
                sprite_focus[char_name] = anim_time
                
                if renpy.is_skipping() or renpy.in_rollback():
                    sprite_focus[char_name] = is_talking
            
            
            
            
            
            
            curr_time = max(anim_time - sprite_focus[char_name],0) 
            
            
            
            curr_ease = 1.0
            
            if curr_time < anim_length and not isinstance(sprite_focus[char_name], bool):
                curr_ease = get_ease(curr_time/anim_length) 
            else:
                sprite_focus[char_name] = is_talking 
            
            
            
            
            
            
            
            
            
            if is_talking: 
                trans.matrixcolor = TintMatrix(get_weather_colour(False)) * BrightnessMatrix(curr_ease * 0.03) * SaturationMatrix(1.2)
                
                trans.zoom = min(curr_ease * zoom_change + (1.0-zoom_change), 1.0)
                trans.yoffset = y_change - curr_ease * y_change 
            else:           
                trans.matrixcolor = TintMatrix(get_weather_colour(False)) * BrightnessMatrix(curr_ease * 0) * SaturationMatrix(1)
                trans.zoom = max(1.0 - curr_ease * zoom_change, (1.0-zoom_change))
                trans.yoffset = y_change * curr_ease            
            
            
            
            return 0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
