init python:
    class Time(object):
        def __init__(self, begin=0, end=24, hourlength=60, weeklength=7, month_start="Summer"):
            self._begin = begin * hourlength
            self._hours = end - begin
            self._hourlength = hourlength
            self._weeklength = weeklength
            self._minutes = 0
            self._daym = 0
            self._monthlengthday = 4 
            self._monthlength = 28 - 0
            self._daynames = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
            self._monthnames = self.month_order(month_start)
            self._daycheck = 1
            self._hourcheck = 1
            self._pregnantday = 0
            self._timeofday = ""
        
        def month_order(self, month_start):
            
            
            months = ["Summer", "Autumn", "Winter", "Spring"]
            
            return (months[months.index(month_start):] + months[:months.index(month_start)])
        
        @property
        def daycheck(self):
            return self._daycheck
        
        @property
        def hourcheck(self):
            return self._hourcheck
        
        @property
        def minute(self):
            return self._minutes % self._hourlength
        
        @property
        def minutes_total(self):
            return self._minutes
        
        @property
        def hour(self):
            return self._minutes / self._hourlength % self._hours + self._begin
        
        @property
        def hours_total(self):
            return self._minutes / self._hourlength
        
        @property
        def day(self):
            return self._minutes / self._hourlength / self._hours + 1
        
        @property
        def pregnantday(self):
            return self._pregnantday
        
        @property
        def wkday(self):
            return self._daynames[int(self._minutes / self._hourlength / self._hours % self._weeklength)]
        
        @property
        def week(self):
            return self._minutes / self._hourlength / self._hours / self._weeklength + 1
        
        @property
        def month(self):
            return self._monthnames[int(self._minutes / self._hourlength / self._hours / self._monthlength % self._monthlengthday)]
        
        @property
        def timeofday(self):
            return self._timeofday
        
        @minute.setter
        def minute(self, minutes=0):
            
            self._minutes += minutes
            game_tick()
            self.timeofday_check()
            self.minute_trigger(minutes)
            if self._minutes < 0:
                self._minutes = 0
            if self.day != self._daycheck:
                self.day_trigger()
            if self.hour != self._hourcheck:
                self.hour_trigger()
        
        @hour.setter
        def hour(self, hours=0):
            game_tick()
            self.timeofday_check()
            self.minute = hours * self._hourlength
            player.inhib_degrade(hours * 60)
            
            if self.day != self._daycheck:
                self.day_trigger()
            if self.hour != self._hourcheck:
                self.hour_trigger()
        
        @day.setter
        def day(self, days=0):
            game_tick()
            self.timeofday_check()
            self.hour = days * self._hours
            player.inhib_degrade(days * 24 * 60)
            if self.day != self._daycheck:
                new_day()
                player.deg_perk(days=True)
                player.preg_day() 
                self._daycheck = self.day
        
        @property
        def daym(self):
            return self._minutes / self._hourlength / self._hours % self._monthlength + 1
        
        @daym.setter
        def daym(self, daysm=0):
            self.hour = daysm * self._hours
        
        def minute_trigger(self, minutes):
            player.inhib_degrade(minutes)
            player.deg_perk(mins=minutes)
            dance_min_tick() 
            npc_active_routine_minute()
            item_cigs_smoke_auto()
            neighbour_routine(minutes)
        
        def hour_trigger(self):
            global global_random_hour_number, global_random_noon_number
            player.deg_perk()
            player.cum_degrade()
            player.add_mood_queue()
            player.add_comfort_chance(timer=True) 
            bruise.heal_ass()
            npc_drunk()
            npc_active_routine_hour()
            npc_desire_raise()
            blood.clean()
            perk_commando_queue()
            perk_lactating_tick()
            global_random_hour_number = numgen(0,10)
            diary_filler_entry_func()
            men_location_degrade()
            for i in npc_all:
                i.hour_number = numgen(0,10) 
            if self.hour == 12:
                npc_active_routine_day_middle()
                global_random_noon_number = numgen(0,10)
                for i in npc_all:
                    i.noon_number = numgen(0,10)
            if self.hour == 5:
                weather_set() 
            self._hourcheck = self.hour
        
        def day_trigger(self):
            new_day()
            player.deg_perk(days=True)
            player.preg_day() 
            for i in npc_all:
                i.hour_number = numgen(0,10)
            self._daycheck = self.day
        
        def timeofday_check(self):
            if self.month == "Summer":
                day = irange(6,20)
            elif self.month == "Winter":
                day = irange(9,17)
            else:
                day = irange(7,19)
            
            if self.hour in day:
                self._timeofday = "day"
            elif self.hour in (min(day) - 1, max(day) + 1):
                self._timeofday = "dawn"
            else:
                self._timeofday = "night"
            return day
        
        def time(self, hour, mins):
            if not isinstance(hour,list):
                hour = [hour]
            if not isinstance(min,list):
                mins = [mins]
            if self.hour in hour and self.minute in mins:
                return True
            else:
                return False
        
        def hour_from_to(self, hour_from, hour_to):
            if hour_from > hour_to:
                if self.hour >= hour_from or self.hour <= hour_to:
                    return True
            else:
                if self.hour in irange(hour_from, hour_to):
                    return True
            return False
        
        def time_from_to(self, time_from, time_to):
            current_time = str(self.hour).zfill(2) + "." + str(self.minute).zfill(2)
            time_from = str(time_from).split('.')[0].zfill(2) + "." + str(time_from).split('.')[1].ljust(2, '0')
            time_to = str(time_to).split('.')[0].zfill(2) + "." + str(time_to).split('.')[1].ljust(2, '0')
            
            
            if time_to < time_from:
                return current_time >= time_from or current_time <= time_to 
            return time_from <= current_time <= time_to
        
        def pass_time(self, days, start_day=True):
            
            self.day = days
            self.hour = numgen(4,20)
            if start_day:
                while not self.timeofday == "day":
                    self.hour = numgen(1,3)
            if player.tired < 25:
                player.add_tired(numgen(20,50))
            player.face_normal()
            player.hands_reset()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
