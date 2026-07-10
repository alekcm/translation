# ai_config_spicy.rpy - МЕХАНИКА SPICY / NSFW УРОВНЯ
# Чтобы квесты не были только "чудесный день, примерь наряд", а иногда spicy
# Реализация: кубик + нарастающий шанс

init python:
    # Текущий уровень spicy - чем больше, тем выше шанс spicy квеста
    # После каждого спокойного квеста +20, после spicy - сброс -30..-50

    # Настройки
    AI_SPICY_BASE_CHANCE = 20  # базовый шанс spicy в %
    AI_SPICY_INCREMENT = 20    # на сколько растет после каждого calm квеста
    AI_SPICY_DECREMENT = 40    # на сколько падает после spicy квеста
    AI_SPICY_MAX = 80          # максимальный шанс

    # Можно еще сделать зависимость от феминности, коррапта, времени дня, локации
    # Например ночью шанс spicy выше, в школе ниже и т.д.

    def ai_get_spicy_chance():
        try:
            base = getattr(store, 'ai_spicy_meter', AI_SPICY_BASE_CHANCE)
            # Модификаторы
            # Ночь +20%
            hour = getattr(store.t, 'hour', 12) if hasattr(store, 't') else 12
            if hour in (20,21,22,23,0,1,2,3,4,5):
                base += 15
            # Высокая феминность +10%
            fem = getattr(store, 'ai_fem', 25)
            if fem > 60:
                base += 10
            # Высокий коррапт +15%
            try:
                corrupt = getattr(store.player, 'corrupt', 0) if hasattr(store, 'player') else 0
                if corrupt > 30:
                    base += 15
            except:
                pass
            # Локация
            loc = "home"
            try:
                if hasattr(store, 'loc_to') and store.loc_to:
                    loc = str(store.loc_to[0])
            except:
                pass
            if any(x in loc for x in ["pub","haven","highway","motel","partyhouse","beach"]):
                base += 20
            elif any(x in loc for x in ["school","hospital"]):
                base -= 10

            return max(0, min(AI_SPICY_MAX, base))
        except:
            return AI_SPICY_BASE_CHANCE

    def ai_roll_spicy():
        # Кидает кубик, решает будет ли spicy квест
        import random as py_random
        chance = ai_get_spicy_chance()
        roll = py_random.randint(0, 100)
        is_spicy = roll < chance
        # Обновляем метр
        try:
            current = getattr(store, 'ai_spicy_meter', AI_SPICY_BASE_CHANCE)
            if is_spicy:
                # Spicy сработал - понижаем
                new_val = max(0, current - AI_SPICY_DECREMENT)
                store.ai_spicy_meter = new_val
                print("SPICY triggered! Chance was %s%%, roll %s. Meter %s -> %s" % (chance, roll, current, new_val))
            else:
                # Calm - повышаем
                new_val = min(AI_SPICY_MAX, current + AI_SPICY_INCREMENT)
                store.ai_spicy_meter = new_val
                print("Calm quest. Chance was %s%%, roll %s. Meter %s -> %s" % (chance, roll, current, new_val))
        except Exception as e:
            print("spicy meter err %s" % e)
        return is_spicy, chance, roll

    def ai_get_spicy_level():
        # Возвращает уровень spicy 0-10 для промпта
        # 0 = совсем ваниль, 10 = максимально spicy NSFW
        try:
            chance = ai_get_spicy_chance()
            # Конвертим шанс в уровень 0-10
            level = int(chance / 10)
            return max(0, min(10, level))
        except:
            return 2

# Переменные
default ai_spicy_meter = 20  # стартовый шанс spicy
default ai_spicy_last_was_spicy = False
default ai_total_quests = 0
default ai_total_spicy_quests = 0

# Для дебага - показать текущий шанс
init python:
    def ai_spicy_debug():
        chance = ai_get_spicy_chance()
        meter = getattr(store, 'ai_spicy_meter', 0)
        return "Spicy meter: %s%%, chance: %s%%, total: %s, spicy: %s" % (meter, chance, getattr(store,'ai_total_quests',0), getattr(store,'ai_total_spicy_quests',0))
