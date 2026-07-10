# ai_config_locations.rpy - КОНФИГ ЛОКАЦИЙ И ТЕМ
# Тут список всех локаций TheFixer и какие теги в них разрешены
# Можешь править сам, файл не перезаписывается основным модом

init python:
    # ПОЛНЫЙ СПИСОК ЛОКАЦИЙ ИЗ ТВОЕЙ ИГРЫ (собрал из definitions.rpy + filelist + tree.txt)
    # Для дебага - используй это чтобы знать где что может происходить
    AI_ALL_LOCATIONS = [
        # --- HOME (приват, нет камер) ---
        "bedroom", "bathroom", "common", "hallway", "kitchen",
        "bedroom_robin", "common_robin",

        # --- RESIDENTIAL ---
        "residential_area", "residential_area_kiosk", "busstop_residential_area",
        "residential_area_alley", "bushes",

        # --- COMMERCIAL ---
        "commercial_area", "commercial_area_mall", "busstop_commercial_area",
        "commercial_area_mall_fitting", "commercial_area_mall_shop_funwear", "commercial_area_mall_shop_meow",

        # --- SCHOOL EXTERIOR ---
        "school_exterior", "busstop_school_exterior",

        # --- SCHOOL INTERIOR ---
        "school_classroom", "school_hallway", "school_cafe", "school_gym", "school_field", "school_field_back",
        "school_locker_girl", "school_locker_boy", "school_toilet", "school_toilet_boy", "school_toilet_girl",
        "school_locker_old", "school_sewroom",

        # --- HIGHWAY ---
        "highway_local", "highway_local_motel", "busstop_highway_local", "truckstop", "motel", "motel_pinkroom", "motel_shower",

        # --- TRAINSTATION / REVEL ---
        "revel", "trainstation_local_exterior", "trainstation_local_platform", "busstop_trainstation_exterior",
        "trainstation_local_pub", "trainstation_local_pub_toilet_girls", "trainstation_local_pub_toilet_boys",
        "partyhouse", "partyhouse_balcony", "partyhouse_hall", "partyhouse_kitchen", "partyhouse_main", "partyhouse_stage",

        # --- MARKET / PARK ---
        "park_local", "park_local_community_centre", "park_local_market", "filler",

        # --- HOSPITAL / INSTITUTE ---
        "hospital_exterior", "hospital_reception", "hospital_ward", "institute_office",

        # --- BUS STOPS ---
        "busstop_residential_area", "busstop_commercial_area", "busstop_school_exterior", "busstop_revel",
        "busstop_lake_entrance", "busstop_highway_local", "busstop_checkpoint", "busstop_industrial_area",
        "busstop_truckstop", "busstop_park_local",

        # --- HAVEN (секта) ---
        "haven_exterior", "haven_hallway_1f", "haven_hallway_2f", "haven_hallway_3f", "haven_lobby",
        "haven_landing", "haven_bedroom", "haven_bed", "haven_shower", "haven_shower_stall",
        "haven_room1", "haven_room2", "haven_room3", "haven_lounge", "haven_storage", "haven_utilities",
        "haven_office", "haven_guardroom",

        # --- MINOR ---
        "alley", "bushes",
        "industrial_area", "checkpoint", "lake_entrance", "lake_boardwalk", "lake_firepit", "lake_gym", "beach", "lake_water",

        # --- SPECIAL ---
        "stairwell", "bus_interior", "revel_backstreet", "commercial_area_mall_fitting"
    ]

    # Уникальный список (убрать дубли)
    AI_ALL_LOCATIONS = sorted(list(set(AI_ALL_LOCATIONS)))

    # ТЕМЫ ПО ЛОКАЦИЯМ - какие теги где могут появляться
    # Если пусто - разрешены все из AI_COMFORT_TAGS где level>0
    # Формат: "location_name": ["tag_id", "tag_id", ...] или ["*"] = все разрешенные
    # Можешь ставить ["!tag"] чтобы запретить конкретный тег в этой локации
    AI_LOCATION_THEMES = {
        # Дома приватно - только феминность, без насилия/шантажа
        "bedroom": ["femininity","crossdressing","humiliation","pregnancy","bdsm_light","chastity"],
        "bathroom": ["femininity","crossdressing","humiliation"],
        "common": ["femininity","crossdressing","bullying"],
        "hallway": ["femininity","bullying"],
        "kitchen": ["femininity"],

        # Школа - буллинг, Wolf Pack, exhibitionism
        "school_exterior": ["*"],  # все разрешенные
        "school_classroom": ["bullying","humiliation","femininity","crossdressing"],
        "school_hallway": ["bullying","exhibitionism","humiliation","femininity"],
        "school_gym": ["femininity","exhibitionism","bullying","body_mod"],
        "school_locker_girl": ["exhibitionism","voyeurism","humiliation","femininity","crossdressing"],
        "school_locker_boy": ["bullying","violence","blackmail"],  # опасно идти в мужскую раздевалку
        "school_toilet": ["exhibitionism","voyeurism","bullying"],
        "school_toilet_girl": ["exhibitionism","voyeurism"],
        "school_toilet_boy": ["bullying","violence"],

        # Коммерческая зона - проституция, freeuse, магазины
        "commercial_area": ["*"],
        "commercial_area_mall": ["prostitution","freeuse","exhibitionism","femininity","humiliation","crossdressing"],
        "commercial_area_mall_fitting": ["exhibitionism","voyeurism","femininity","humiliation"],

        # Парк / пляж / озеро - эксгибиционизм, вуайеризм, свободное использование
        "park_local": ["exhibitionism","voyeurism","freeuse","femininity","bullying"],
        "park_local_market": ["prostitution","freeuse","drugs_light"],
        "lake_entrance": ["exhibitionism","voyeurism","freeuse","femininity"],
        "beach": ["exhibitionism","voyeurism","freeuse","femininity","pregnancy","body_mod"],
        "lake_water": ["exhibitionism","voyeurism"],

        # Хайвэй / мотель / дальнобойщики - жестче темы
        "highway_local": ["prostitution","freeuse","slavery","violence","drugs_light","drugs_hard","blackmail","bullying"],
        "highway_local_motel": ["prostitution","freeuse","slavery","bdsm_light","gag","pregnancy"],
        "truckstop": ["prostitution","freeuse","slavery","violence","drugs_light"],
        "motel": ["prostitution","freeuse","slavery","bdsm_light","breeding"],

        # Патихаус / Revel / бар - алкоголь, наркота, freeuse
        "revel": ["alcohol","drugs_light","prostitution","freeuse","exhibitionism","bullying","blackmail"],
        "partyhouse": ["alcohol","drugs_light","freeuse","exhibitionism","prostitution","humiliation","bdsm_light","gag"],
        "trainstation_local_pub": ["alcohol","prostitution","freeuse","violence","blackmail"],

        # Haven - секта, рабы, контроль разума
        "haven_exterior": ["bullying","mindcontrol","slavery","humiliation"],
        "haven_bedroom": ["slavery","mindcontrol","humiliation","bdsm_light","gag","chastity","pregnancy","breeding"],
        "haven_shower": ["exhibitionism","voyeurism","humiliation","slavery"],
        "haven_lounge": ["mindcontrol","humiliation","slavery","bullying"],

        # Институт / больница - контроль, бодимод
        "hospital_exterior": ["mindcontrol","body_mod"],
        "hospital_ward": ["mindcontrol","body_mod","humiliation"],
        "institute_office": ["mindcontrol","blackmail","body_mod"],

        # Автобус - можно все но мягко
        "bus_interior": ["exhibitionism","voyeurism","humiliation","groping"],

        # По умолчанию для неизвестных локаций - все разрешенные из комфорта
        # "*": ["*"] # не нужно, если локации нет в словаре - разрешены все allowed tags
    }

    # Функция проверки разрешена ли тема в локации
    def ai_is_theme_allowed_in_location(theme_id, location_name):
        # Сначала проверяем глобальный комфорт
        from ai_config_tags import AI_COMFORT_DICT
        tag = AI_COMFORT_DICT.get(theme_id)
        if not tag or tag['level'] == 0:
            return False

        # Потом проверяем локацию
        loc_themes = AI_LOCATION_THEMES.get(location_name)
        if loc_themes is None:
            # Локации нет в конфиге - разрешаем все что разрешено глобально
            return True

        # Если ["*"] - разрешены все глобально разрешенные
        if "*" in loc_themes:
            return True

        # Если есть запрет "!tag"
        if ("!"+theme_id) in loc_themes:
            return False

        # Если тема явно в списке разрешенных для локации
        if theme_id in loc_themes:
            return True

        # Если список не пуст и темы там нет - запрещаем (строгий режим)
        # Если хочешь мягкий режим - верни True по умолчанию
        # Сейчас строгий: если локация указана, разрешены только её теги
        return False

    def ai_get_allowed_themes_for_location(location_name):
        # Возвращает список тегов разрешенных в этой локации с учетом комфорта
        try:
            from ai_config_tags import AI_COMFORT_DICT
            allowed_global = [tid for tid, t in AI_COMFORT_DICT.items() if t['level']>0]

            loc_themes = AI_LOCATION_THEMES.get(location_name)
            if loc_themes is None:
                return allowed_global

            if "*" in loc_themes:
                return allowed_global

            # Фильтруем - только те что и в локации и глобально разрешены
            result = []
            for tid in loc_themes:
                if tid.startswith("!"):
                    continue
                if tid in allowed_global:
                    result.append(tid)
            return result
        except:
            return []

    # Дебаг - вывести все локации с темами
    # for loc in AI_ALL_LOCATIONS:
    #     print(loc, "->", ai_get_allowed_themes_for_location(loc))
