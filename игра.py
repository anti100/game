story = {
    "start": {
        "text": "Вы детектив, и вас вызвали на место преступления. Жертва найдена в своем офисе с ножом в спине. Вы видите три вещи: нож, записку и компьютер.",
        "choices": [
            {"text": "Осмотреть нож", "next": "knife"},
            {"text": "Проверить записку", "next": "note"},
            {"text": "Посмотреть на компьютер", "next": "computer"}
        ]
    },
    "knife": {
        "text": "Нож выглядит обычным, но на нем есть отпечатки пальцев. Вы решили взять его для анализа.",
        "choices": [
            {"text": "Вернуться к месту преступления", "next": "start"},
            {"text": "Поговорить с полицейским", "next": "talk_officer"}
        ]
    },
    "note": {
        "text": "Записка содержит загадочные слова: 'Он знает слишком много'. Это может быть важной уликой.",
        "choices": [
            {"text": "Вернуться к месту преступления", "next": "start"},
            {"text": "Поговорить с полицейским", "next": "talk_officer"}
        ]
    },
    "computer": {
        "text": "На компьютере открыто письмо от неизвестного отправителя. Письмо говорит о сделке, которая должна была состояться сегодня.",
        "choices": [
            {"text": "Вернуться к месту преступления", "next": "start"},
            {"text": "Поговорить с полицейским", "next": "talk_officer"}
        ]
    },
    "talk_officer": {
        "text": "Вы поговорили с полицейским. Он говорит, что есть два подозреваемых: секретарь жертвы и бизнес-партнер.",
        "choices": [
            {"text": "Допросить секретаря", "next": "interrogate_secretary"},
            {"text": "Допросить бизнес-партнера", "next": "interrogate_partner"}
        ]
    },
    "interrogate_secretary": {
        "text": "Секретарь выглядит нервной. Она говорит, что у нее был конфликт с жертвой из-за денег.",
        "choices": [
            {"text": "Спросить о деньгах", "next": "money_conflict"},
            {"text": "Поверить ей и уйти", "next": "end_game_innocent"}
        ]
    },
    "interrogate_partner": {
        "text": "Бизнес-партнер выглядит уверенно. Он говорит, что у него была хорошая связь с жертвой.",
        "choices": [
            {"text": "Спросить о сделке", "next": "deal_question"},
            {"text": "Поверить ему и уйти", "next": "end_game_innocent"}
        ]
    },
    "money_conflict": {
        "text": "Я не хотела его убивать! Он просто не хотел делиться! - кричит секретарь.",
        "choices": [
            {"text": "Обвинить секретаря", "next": "end_game_guilty_secretary"},
            {"text": "Проверить алиби секретаря", "next": "check_alibi_secretary"}
        ]
    },
    "deal_question": {
        "text": "Я ничего не знаю о сделке! Я просто работал! - говорит бизнес-партнер.",
        "choices": [
            {"text": "Обвинить бизнес-партнера", "next": "end_game_guilty_partner"},
            {"text": "Проверить алиби бизнес-партнера", "next": "check_alibi_partner"}
        ]
    },
    # Концовки
    "end_game_guilty_secretary": {
        "text": "Вы поймали меня! Я не могла больше терпеть! - признается секретарь.",
        "choices": []
    },
    "end_game_guilty_partner": {
        "text": "Это было всего лишь бизнес! - говорит партнер перед арестом.",
        "choices": []
    },
    "end_game_innocent": {
        "text": "Я ничего не сделала! - говорит она/он, и вы уходите, не найдя виновного.",
        "choices": []
    },
    # Проверка алиби
    "check_alibi_secretary": {
        "text": "У меня есть алиби! Я была в кафе в это время! - говорит секретарь.",
        "choices": [
            {"text": "Проверить ее алиби", "next": "alibi_checked_secretary"},
            {"text": "Не верить ей", "next": "end_game_guilty_secretary"}
        ]
},
"check_alibi_partner": {
    "text": "У меня есть свидетели! Я был на встрече! - говорит партнер.",
"choices": [
    {"text": "Проверить его алиби", "next": "alibi_checked_partner"},
    {"text": "Не верить ему", "next": "end_game_guilty_partner"}
]
},
# Проверка алиби
"alibi_checked_secretary": {
    "text": "Ее алиби подтвердилось! Она была в кафе! - сообщает полицейский.",
"choices": [
    {"text": "Обвинить бизнес-партнера", "next": "end_game_guilty_partner"},
    {"text": "Кто же тогда убийца? - думаете вы.", 'next': 'start'}
]
},
"alibi_checked_partner": {
    "text": "Его алиби не подтвердилось! Он не был на встрече! - сообщает полицейский.",
"choices": [
    {"text": "Обвинить бизнес партнера", 'next': 'end_game_guilty_secretary'}
        ]
}
}


def play_game(current_node):
    while True:
        # Выводим текст текущего узла
        print(story[current_node]["text"])

        # Проверяем, есть ли выборы
        choices = story[current_node]["choices"]
        if not choices:
            print("Конец игры!")
            break

        # Выводим доступные выборы
        for i, choice in enumerate(choices):
            print(f"{i + 1}. {choice['text']}")

        # Запрашиваем ввод пользователя
        user_choice = input("Выберите вариант (введите номер): ")

        # Обрабатываем выбор пользователя
        try:
            choice_index = int(user_choice) - 1
            if 0 <= choice_index < len(choices):
                current_node = choices[choice_index]["next"]
            else:
                print("Неверный выбор, попробуйте еще раз.")
        except ValueError:
            print("Пожалуйста, введите число.")


# Начало игры
play_game("start")

