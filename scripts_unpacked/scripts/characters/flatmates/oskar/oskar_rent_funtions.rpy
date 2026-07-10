init python:
    def rent_tick():
        if t.wkday == "Sunday" and not (loc_kitchen.locked or dis_residential.locked or dis(dis_haven)):
            if len(rent_ledger) < t.week:
                rent_raise()
                rent_ledger.append(rent_amount)

    def rent_convert_ledger():
        global rent_ledger
        if not type(rent_ledger) == list:
            new_ledger = []
            for k in sorted(rent_ledger):
                new_ledger.append(rent_ledger[k])
            rent_ledger = new_ledger

    def rent_total_owed(): 
        if oskar.dead:
            return 0
        return sum(rent_ledger)

    def rent_debt_owed(): 
        if oskar.dead:
            return 0
        return sum(rent_ledger[0:-1])

    def rent_month_owed(): 
        if oskar.dead or len(rent_ledger) == 0:
            return 0
        return rent_ledger[-1]

    def rent_weeks_skipped(): 
        if oskar.dead:
            return 0 
        return sum(1 for amount in rent_ledger if amount > 0)

    def rent_pay(amount, cash=True, notif=True):
        remainder = amount
        for key, week_rent in enumerate(rent_ledger):
            if remainder <= 0:
                
                break
            
            payment = min(week_rent, remainder)
            
            rent_ledger[key] -= payment
            remainder -= payment
        
        if amount and notif:
            show_notif_popup("£" + str(amount) + " of rent paid")
        if cash:
            player.spend(amount, notif=False)  

    def rent_workoff(amount):
        
        pay_amount = amount
        remainder = 0
        if rent_total_owed() < amount:
            remainder = amount - rent_total_owed()
            pay_amount = rent_total_owed()
        rent_pay(pay_amount, cash=False)
        if remainder:
            player.add_money(remainder)
        return remainder

    def rent_punish():
        if rent_weeks_skipped() > 2:
            return True
        else:
            return False

    def rent_kick():
        if rent_weeks_skipped() > 5:
            return True
        else:
            return False

    def rent_raise():
        global rent_amount, rent_raise_counter
        rent_raise_counter += 1
        if rent_raise_counter > 2 and rent_amount < 1000:
            rent_amount += 200
            rent_raise_counter = 0
            add_to_list(quest_rent.list, "rent_raised")

default rent_amount = 400
default rent_raise_counter = 0

default rent_ledger = []
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
