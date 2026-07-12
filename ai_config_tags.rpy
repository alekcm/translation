# ai_config_tags.rpy - КОНФИГ ТЕГОВ КОМФОРТА
# Этот файл можно править самому, он не перезаписывается при обновлении основного мода
# Добавляй свои темы сюда. Фильтр в основном моде будет учитывать только те теги что ты разрешил.

init python:
    # Уровень комфорта: 0 = запретить, 1 = только намёки/мягко/согласие, 2 = разрешить полностью
    # Если фильтра LLM нет - он всё равно не сгенерит запрещенное, но наш фильтр не даст показать ивент с запрещенным тегом

    AI_COMFORT_TAGS = [
        # Базовые - уже есть в TheFixer лоре
        {"id": "femininity", "name": "Феминизация / Sissification", "desc": "Тренировка быть девушкой, походка, одежда", "level": 2, "always": True},
        {"id": "crossdressing", "name": "Кроссдрессинг", "desc": "Переодевание в женское", "level": 2, "always": True},
        {"id": "humiliation", "name": "Унижение", "desc": "Словесное унижение", "level": 3},
        {"id": "gender_bender_humiliation", "name": "Унижение из-за смены пола", "desc": "Унижение из-за смены пола", "level": 3},

        # Социальные
        {"id": "blackmail", "name": "Шантаж", "desc": "Шантаж фотками", "level": 3},
        {"id": "genderbender_blackmail", "name": "Шантаж о смене пола", "desc": "Шантаж секретом что был мужиком", "level": 1},
        {"id": "exhibitionism", "name": "Эксгибиционизм", "desc": "Показывать тело на людях", "level": 3},
        {"id": "voyeurism", "name": "Вуайеризм", "desc": "Подглядывание", "level": 1},
        {"id": "bullying", "name": "Буллинг / Травля", "desc": "Школа, Wolf Pack и т.д.", "level": 3},

        # Секс-работа
        {"id": "prostitution", "name": "Проституция", "desc": "Продажа тела за деньги", "level": 2},
        {"id": "freeuse", "name": "Free Use / Общественное пользование", "desc": "Используют без спроса в определенных зонах", "level": 3},
        {"id": "slavery", "name": "Рабство / Владение", "desc": "Клеймо, ошейник, принадлежность Институту/персонажу", "level": 3},

        # Согласие
        {"id": "dubcon", "name": "Сомнительное согласие / Пьяная", "desc": "Пьяная, накачанная, не до конца понимает", "level": 3},
        {"id": "noncon", "name": "Non-con / Изнасилование", "desc": "Полностью несогласный секс", "level": 3},
        {"id": "violence", "name": "Насилие", "desc": "Избиение, физическое насилие не сексуальное", "level": 3},

        # Вещества
        {"id": "alcohol", "name": "Алкоголь", "desc": "Пьянки в пабе", "level": 2},
        {"id": "drugs_light", "name": "Легкие наркотики / Травка", "desc": "Травка, таблетки Lebo из игры", "level": 2},
        {"id": "drugs_hard", "name": "Тяжелые наркотики", "desc": "Хард", "level": 3},

        # Кинки
        {"id": "bdsm_light", "name": "BDSM Лайт", "desc": "Связывание, шлепки, повязка", "level": 2},
        {"id": "bdsm_bondage", "name": "BDSM Бондаж", "desc": "Жесткий бондаж", "level": 2},
        {"id": "bdsm_hard", "name": "BDSM Хард", "desc": "Пытки, иглы", "level": 3},
        {"id": "gag", "name": "Кляп / Gag", "desc": "Кляп во рту", "level": 3},
        {"id": "chastity", "name": "Пояс верности", "desc": "Пояс верности, клетка", "level": 0},
        {"id": "pregnancy", "name": "Беременность / Breeding", "desc": "Риск беременности, желание забеременеть", "level": 2},
        {"id": "breeding", "name": "Разведение / Оплодотворение", "desc": "Целенаправленное оплодотворение", "level": 3},
        {"id": "incest", "name": "Инцест (сестра Эмили)", "desc": "Сестра Emile есть в лоре", "level": 2},
        {"id": "cheating", "name": "Измена / NTR", "desc": "Измена, NTR", "level": 0},

        # Экстрим - по умолчанию запрещены, можешь включить если хочешь
        {"id": "urination", "name": "Мочеиспускание (бытовое)", "desc": "Просто сходить в туалет: сидеть, стоять, вытираться. Не сексуально.", "level": 0},
        {"id": "menstruation_mundane", "name": "Месячные (бытовое)", "desc": "Тампоны, прокладки, судороги, пятна на трусах — без секса", "level": 0},
        {"id": "menstruation_sex", "name": "Секс во время месячных", "desc": "Кровь во время секса, period sex", "level": 0},
        {"id": "blood", "name": "Кровь", "desc": "Кровь, порезы", "level": 2},
        {"id": "scat", "name": "Scat", "desc": "Фекалии", "level": 0},
        {"id": "watersports", "name": "Watersports", "desc": "Золотой дождь", "level": 0},
        {"id": "mindcontrol", "name": "Контроль разума / Гипноз", "desc": "Промывка мозгов", "level": 2},
        {"id": "body_mod_pirs", "name": "Пирсинг", "desc": "Пирсинг", "level": 2},
        {"id": "body_mod_tatoo", "name": "Тату", "desc": "Тату", "level": 2},
        {"id": "body_mod_silicone", "name": "Силикон", "desc": "Силикон", "level": 0},

        # Добавь свои ниже - просто скопируй строку и поменяй id/name
        # {"id": "my_tag", "name": "Мой тег", "desc": "Описание", "level": 2},
    ]

    # Словарь для быстрого доступа
    AI_COMFORT_DICT = {t['id']: t for t in AI_COMFORT_TAGS}

    AI_HARD_BLOCKED_THEMES = [
        u"none",
    ]

    def ai_get_forbidden_themes_text():
        """Собирает единый список запретов: хард-лист + теги с level==0.
        Отдаётся LLM как раздел [FORBIDDEN THEMES] промпта."""
        lines = []
        # 1) хард-лист
        for t in AI_HARD_BLOCKED_THEMES:
            try:
                lines.append(u"- " + unicode(t))
            except Exception:
                lines.append(u"- " + str(t))
        # 2) теги, которые игрок явно отключил в AI_COMFORT_TAGS (level==0)
        try:
            for tag in AI_COMFORT_TAGS:
                if tag.get('level', 2) == 0:
                    name = tag.get('name') or tag.get('id') or u"?"
                    desc = tag.get('desc') or u""
                    try:
                        line = u"- " + unicode(name)
                        if desc:
                            line += u" — " + unicode(desc)
                        line += u" (disabled by player)"
                        lines.append(line)
                    except Exception:
                        lines.append(u"- " + str(name) + u" (disabled by player)")
        except Exception:
            pass
        return u"\n".join(lines) if lines else u"(none configured)"

    def ai_is_tag_allowed(tag_id):
        # Проверяет разрешен ли тег
        t = AI_COMFORT_DICT.get(tag_id)
        if not t:
            return True  # неизвестный тег разрешаем по умолчанию
        return t['level'] > 0

    def ai_get_allowed_tags():
        return [t['id'] for t in AI_COMFORT_TAGS if t['level'] > 0]

    def ai_get_forbidden_tags():
        return [t['id'] for t in AI_COMFORT_TAGS if t['level'] == 0]

    # Для дебага - список всех id
    # print("Comfort tags loaded: %s" % AI_COMFORT_TAGS)

    def ai_event_has_hard_blocked_content(event):
        """Неотключаемый safety-filter. По умолчанию ничего не блокирует.
        Можно расширить под свои hard-ban слова/теги."""
        try:
            if not event:
                return False
            # Пример: раскомментируй и дополни при необходимости
            # blob = (unicode(event.get('title','')) + ' ' + unicode(event.get('description',''))).lower()
            # for bad in []:
            #     if bad and bad in blob:
            #         return True
            return False
        except Exception:
            return False


