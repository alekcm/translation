# ai_config_factions.rpy - ГРУППИРОВКИ / ФРАКЦИИ
# Школа и другие части мира которые влияют на игрока и на которые влияет игрок
# Отношения влияют на события

init python:
    AI_FACTIONS = {
        # --- ШКОЛА ---
        "wolf_pack": {
            "name": "Wolf Pack",
            "desc": "Стая парней-буллей в школе, гнобят слабых. Лидер Mason.",
            "members": ["mason","soccerboys"],
            "location": ["school_field","school_hallway","school_gym"],
            "reputation": 0,  # -100 враги, +100 друзья
            "influence": "Если репутация низкая - будут домогаться в раздевалке, шантажировать. Если высокая - будут защищать, но требовать быть их сучкой.",
            "events_tags": ["bullying","blackmail","violence","humiliation","exhibitionism"]
        },
        "mean_girls": {
            "name": "Mean Girls Academy",
            "desc": "Популярные девки академии, Cass, Mira и т.д.",
            "members": ["cass","mira","saskia","frida"],
            "location": ["school_classroom","school_hallway","school_cafe"],
            "reputation": 0,
            "influence": "Высокая репа = приглашают на тусы, дают одежду. Низкая = сливают фотки, буллинг.",
            "events_tags": ["bullying","humiliation","exhibitionism","blackmail"]
        },
        "teachers": {
            "name": "Учителя",
            "desc": "Carlson, O'Neill, Abbott и т.д.",
            "members": ["carlson","oneil","abbott","headt"],
            "location": ["school_classroom","school_hallway"],
            "reputation": 0,
            "influence": "Репутация влияет на оценки, возможность прогуливать, наказания.",
            "events_tags": ["blackmail","humiliation"]
        },

        # --- ГОРОД ---
        "institute": {
            "name": "Institute",
            "desc": "Организация что спасла тебя, пересадила в тело Саманты. Dr. Tucker, Dr. Nikolas, Nurse Lilly, Dr. Brooker.",
            "members": ["tucker","nik","nurse","psy"],
            "location": ["hospital_exterior","hospital_ward","institute_office"],
            "reputation": 10,
            "influence": "Работодатель. Дает миссии Fixer, следит за феминностью. Высокая репа = больше денег, операции. Низкая = недоверие.",
            "events_tags": ["mindcontrol","body_mod","blackmail"]
        },
        "police": {
            "name": "Полиция Blaston",
            "desc": "Sgt. Betty Parson, Paige Williams",
            "members": ["betty","paige"],
            "location": ["checkpoint","industrial_area","commercial_area"],
            "reputation": 0,
            "influence": "Если репутация низкая - могут арестовать за проституцию. Высокая - крышуют.",
            "events_tags": ["blackmail","violence","prostitution"]
        },
        "haven": {
            "name": "Haven (Секта)",
            "desc": "Культ, держит девушек как рабынь. Wolfgang и т.д.",
            "members": ["haven"],
            "location": ["haven_exterior","haven_lobby","haven_bedroom"],
            "reputation": -10,
            "influence": "Секта хочет заполучить тебя как рабыню. Высокая репа (подчинение) = продвигают внутри, низкая = пытаются похитить.",
            "events_tags": ["slavery","mindcontrol","humiliation","bdsm_light","pregnancy","breeding"]
        },
        "commercial": {
            "name": "Торговцы",
            "desc": "Магазины одежды, Funwear shop girl и т.д.",
            "members": ["fun_girl","shop"],
            "location": ["commercial_area","commercial_area_mall"],
            "reputation": 0,
            "influence": "Скидки в магазинах, доступ к slutty одежде.",
            "events_tags": ["femininity","crossdressing","exhibitionism"]
        },
        "pub": {
            "name": "Пуб Revel",
            "desc": "Bob, Trixie, бармены. Место где бухают и снимают шлюх.",
            "members": ["bob","trixie"],
            "location": ["trainstation_local_pub","revel"],
            "reputation": 0,
            "influence": "Работа официанткой, чаевые, знакомства с мужиками.",
            "events_tags": ["alcohol","prostitution","freeuse","exhibitionism"]
        },
        "highway_whores": {
            "name": "Highway Whores",
            "desc": "Kitty, Rose bud, Charity, Pursy - шлюхи с трассы",
            "members": ["kitty","rose","charity","pursy"],
            "location": ["highway_local","truckstop","highway_local_motel"],
            "reputation": 0,
            "influence": "Если дружишь - учат как продавать тело, дают клиентов. Если враги - отбирают клиентов.",
            "events_tags": ["prostitution","freeuse","slavery","drugs_light"]
        },
        "dance_troupe": {
            "name": "Sweet Girls Dance",
            "desc": "Svetlana, Dani, Anabel и т.д. - танцевальная труппа",
            "members": ["svet","dani","anabel","rachel"],
            "location": ["park_local_community_centre","school_gym"],
            "reputation": 0,
            "influence": "Приглашают на шоу, дают уверенность, могут затянуть в стриптиз.",
            "events_tags": ["exhibitionism","femininity","humiliation"]
        },

        # --- ДОМ ---
        "flatmates": {
            "name": "Соседи по дому",
            "desc": "Robin, Oskar, Emile, Charlie - живешь с ними",
            "members": ["robin","oskar","emile","charlie"],
            "location": ["common","bedroom","kitchen","hallway","bathroom"],
            "reputation": 0,
            "influence": "Влияют на домашние события, могут домогаться, помогать с арендой.",
            "events_tags": ["voyeurism","exhibitionism","femininity","incest"]
        },
    }

    # Репутация игрока у фракций - хранится в сейве
    # default значения в AI_FACTIONS["reputation"] - начальные

    def ai_get_faction_rep(faction_id):
        try:
            # Пробуем взять из сохраненной переменной если есть
            var_name = "ai_faction_%s_rep" % faction_id
            if hasattr(store, var_name):
                return getattr(store, var_name)
            # Иначе из конфига
            return AI_FACTIONS.get(faction_id, {}).get('reputation', 0)
        except:
            return 0

    def ai_set_faction_rep(faction_id, value):
        try:
            var_name = "ai_faction_%s_rep" % faction_id
            # Кламп -100..100
            value = max(-100, min(100, value))
            setattr(store, var_name, value)
            # Уведомление
            renpy.notify("%s rep %+d" % (AI_FACTIONS.get(faction_id,{}).get('name',faction_id), value))
        except Exception as e:
            print("set faction rep err %s" % e)

    def ai_add_faction_rep(faction_id, delta):
        try:
            cur = ai_get_faction_rep(faction_id)
            ai_set_faction_rep(faction_id, cur + delta)
        except:
            pass

    def ai_get_factions_for_location(location_name):
        # Какие фракции активны в этой локации
        result = []
        for fid, fdata in AI_FACTIONS.items():
            if location_name in fdata.get('location',[]):
                result.append(fid)
        return result

    def ai_get_influential_factions():
        # Фракции с высокой/низкой репой что влияют на события
        high = []
        low = []
        for fid in AI_FACTIONS.keys():
            rep = ai_get_faction_rep(fid)
            if rep >= 30:
                high.append((fid, rep))
            elif rep <= -30:
                low.append((fid, rep))
        return high, low

# Для дебага - создать переменные репутации
init python:
    # Создаем дефолтные переменные для каждой фракции если нет
    for fid in AI_FACTIONS.keys():
        var_name = "ai_faction_%s_rep" % fid
        if not hasattr(store, var_name):
            try:
                # default нельзя внутри init python, но можно через setattr
                setattr(store, var_name, AI_FACTIONS[fid].get('reputation',0))
            except:
                pass
