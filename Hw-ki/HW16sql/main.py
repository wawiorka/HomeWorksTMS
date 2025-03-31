"""Вариант 4 - Сервис резервирования билетов:
Функционал:
• Разработка схемы базы данных для мероприятий, мест и билетов
• Простые операции, такие как добавление/удаление/редактирование
событий/мест, вывод информации о событии/месте по названию
• Сложные операции, такие как поиск события по месту, поиск
события/курса/whatever по частичному совпадению названия
• Функционал для бронирования и отмены билетов"""

import db


def print_menu():
    print("\nЧто вы хотите сделать? (выберите нужную команду) ")
    print("0. Выход")
    print("1. Посмотреть список мероприятий")
    print("2. Посмотреть список мест")
    print("3. Посмотреть список мест и мероприятий")
    print("4. Изменить список мероприятий")
    print("41. Добавить новое мероприятие в список связей")
    print("5. Изменить список мест")    
    print("6. Изменить место проведения мероприятия")
    print("7. Поиск объектов по названию")
    print("8. Поиск объектов по части названия")
    print("9. Бронирование билетов")
    print("10. Возврат билетов")
    print("11. Вывод информации о числе забронированных билетов по ID мероприятия")
    print("12. Вывод информации всех забронированных билетах")

        
def app():
    print("Добрый день! Вы запустили Сервис Резервиравания Билетов")
    
    db.init_db()
    print("Таблицы созданы")
    
    # отлов ошибки на дозаписывание новых строк при повторном запуске, получше варианта не придумала
    try:
        db.content_db()
    except Exception as e:
        print(f"Что-то пошло не так! {e}")

    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))

        if cmd == 0:
            print("\nСпасибо за пользование сервисом! До свидания!")
            break
        
        elif cmd == 1:  # Показать список мероприятий
            print("\nСписок мероприятий: ")
            events = db.get_events()
            for event in events:
                print(f"ID {event[0]} - {event[1]}, {event[2]}.")

        elif cmd == 2:  # Показать список мест
            print("\nСписок мест: ")
            plases = db.get_plases()
            for plase in plases:
                print(f"ID {plase[0]} - {plase[1]}.")
        
        elif cmd == 3:  # Показать список мест и мероприятий
            print("\nСписок: ")
            plases_ev = db.get_plases_events()
            for plase in plases_ev:
                print(f"{plase[0]} (id {plase[1]}) - {plase[2]}, {plase[3]}.")
        
        elif cmd == 4:  # Изменить список мероприятий
            print("\nЧто вы хотите сделать? (выберите нужную команду)")
            print("1. добавить мероприятие.")
            print("2. удалить мероприятие.")
            print("3. отредактировать мероприятие.")
            cmd3 = int(input("Введите команду "))
            if cmd3 == 1:
                print("\nВы выбрали добавление мероприятия")
                title = input("Введите название мероприятия: ")
                date = input("Введите дату мероприятия: ")
                try:
                    db.add_event(title, date)
                    db.add_in_events_plases(title)
                    print("Мероприятие добавлено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            elif cmd3 == 2:
                print("\nВы выбрали удаление мероприятия")
                id = input("Введите ID удаляемого мероприятия: ")
                try:
                    db.delete_event(id)
                    print("Мероприятие удалено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            elif cmd3 == 3:
                print("\nВы выбрали обновление мероприятия")
                id = input("Введите ID обновляемого мероприятия: ")
                title = input("Введите новое название мероприятия: ")
                date = input("Введите новую дату мероприятия: ")
                try:
                    db.update_event(title, date, id)
                    print("Информация о мероприятии обновлена.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            else:
                print("Вы ввели несуществующею команду. Попробуйте еще раз!")
            
        elif cmd == 41:  # Добавить новое мероприятие в список связей
            print("\nВы выбрали добавление нового мероприятия в список связей")
            print("\nСписок мероприятий: ")
            events = db.get_events()
            for event in events:
                print(f"ID {event[0]} - {event[1]}, {event[2]}.")
            id_ev_pl = input("Введите ID мероприятия: ")
            try:
                db.add_in_events_plases(id_ev_pl)
                print("Мероприятие добавлено.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")

        elif cmd == 5:  # Изменить список меcт
            print("\nЧто вы хотите сделать? (выберите нужную команду)")
            print("1. добавить место.")
            print("2. удалить место.")
            cmd3 = int(input("Введите команду "))
            if cmd3 == 1:
                print("\nВы выбрали добавление места")
                plase_name = input("Введите название места: ")
                try:
                    db.add_plase(plase_name)
                    print("Место добавлено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            elif cmd3 == 2:
                print("\nВы выбрали удаление места")
                id = input("Введите ID удаляемого места: ")
                try:
                    db.delete_plase(id)
                    print("Место удалено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            else:
                print("Вы ввели несуществующею команду. Попробуйте еще раз!")

        elif cmd == 6: # Изменить место проведения мероприятия
            print("\nВы выбрали обновление мероприятия")
            ivent_id = input("\nВведите ID мероприятия, место проведения которого хотите поменять: ")
            plase_id = input("Введите ID места проведения мероприятия: ")
            try:
                db.update_plase(plase_id, ivent_id)
                print("Информация о месте проведения мероприятия обновлена.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 7:  # Поиск объектов по названию
            query = input("\nЧто вы ищете (введите название): ")
            with db.connect_db() as conn, conn.cursor() as cur:
                cur.execute(f"SELECT * FROM events WHERE title = '{query}';")
                events = cur.fetchall()
            print(f"Найдено мероприятий по запросу:")
            for event in events:
                print(f"ID {event[0]} - {event[1]}.")
            with db.connect_db() as conn, conn.cursor() as cur:
                cur.execute(f"SELECT * FROM plases WHERE name = '{query}';")
                plases = cur.fetchall()
            print(f"Найдено меcт по запросу:")
            for plase in plases:
                print(f"ID {plase[0]} - {plase[1]}.")
        
        elif cmd == 8:  # Поиск объектов по части названия
            query = input("\nЧто вы ищете (введите название/часть названия): ")
            events = db.search_events(query)
            plases = db.search_plases(query)
            print(f"Найдено мероприятий по запросу '{query}':")
            for event in events:
                print(f"ID {event[0]} - {event[1]}.")
            print(f"Найдено меcт по запросу '{query}':")
            for plase in plases:
                print(f"ID {plase[0]} - {plase[1]}.")
        
        # • Функционал для бронирования и отмены билетов"""
        elif cmd == 9:  # бронирование билетов
            print("\nВы выбрали бронирование билетов")
            ivent_id = input("Введите ID мероприятия, куда хотите забронировать билет: ")
            buyer = input("Введите ваше имя для покупки билета: ") 
            try:
                db.reserv_ticket(buyer, ivent_id)
                print("Билет успешно прибретен.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 10:  # возврат билетов
            print("\nВы выбрали возврат билетов")
            id = input("Введите ID билета: ")
            try:
                db.return_ticket(id)
                print("Билет успешно анулирован.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 11:  # Вывод информации о числе забронированных билетов по ID мероприятия
            print("\nВывод информации о числе забронированных билетов на мероприятие")
            id = input("Введите ID мероприятия: ")
            try:
                event_tickets = db.get_num_tickets(id)
                num_tickets = event_tickets["num_tickets"]
                event = event_tickets["event"]   
                for ev in event:
                    print(f"На мероприятие: '{ev[0]}':")                   
                for ticket in num_tickets:
                    print(f"Забронировано билетов: {ticket[0]}")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 12:  # Вывод информации о числе забронированных билетов на мероприятие
            print("\nВывод информации о числе забронированных билетов на мероприятие")
            try:
                all_tickets = db.get_tickets()
                
                for t in all_tickets:
                    print(f'Уникальный номер билета: {t[0]}; Покупатель - {t[1]}; Название: {t[2]}, {t[3]}.')
                
            except Exception as e:
                print(f"Что-то пошло не так! {e}")

        else:
            print("Вы ввели несуществующею команду. Попробуйте еще раз!")
        

app()
