from db_orm import init_db, get_events, get_plases, get_plases_events, add_event, delete_event, update_event, reserv_ticket, return_ticket, get_tickets
from db_orm import get_num_tickets, update_plase,  add_plase, delete_plase, add_in_events_plases 
from db_orm import search_events, search_plases, search_events_all, search_plases_all

def print_menu():
    print("\nЧто вы хотите сделать? (выберите нужную команду) ")
    print("0. Выход")
    print("1. Посмотреть список мероприятий")
    print("2. Посмотреть список мест")
    print("3. Посмотреть список мест и мероприятий")
    print("4. Изменить список мероприятий")
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
    
    init_db()
    print("Таблицы созданы")
    
    # отлов ошибки на дозаписывание новых строк при повторном запуске, получше варианта не придумала
    # try:
    #     db_orm.content_db()
    # except Exception as e:
    #     print(f"Что-то пошло не так! {e}")

    while True:
        print_menu()
        cmd = int(input("Введите номер команды: "))

        if cmd == 0:
            print("\nСпасибо за пользование сервисом! До свидания!")
            break
        
        elif cmd == 1:  # Показать список мероприятий
            print("\nСписок мероприятий: ")
            events = get_events()
            for event in events:
                print(f"ID {event.id} - {event.title}, {event.date}.")

        elif cmd == 2:  # Показать список мест
            print("\nСписок мест: ")
            plases = get_plases()
            for plase in plases:
                print(f"ID {plase.id} - {plase.name}.")
        
        elif cmd == 3:  # Показать список мест и мероприятий
            print("\nСписок: ")
            plases_ev = get_plases_events()
            for plase in plases_ev:
                print(f"{plase[1]} (id {plase[2]}) - {plase[3]}, {plase[4]}.")
        
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
                    add_event(title, date)
                    add_in_events_plases(title)  # добавление в EventPlase (Plase = None)
                    print("Мероприятие добавлено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
                
                    
            elif cmd3 == 2:
                print("\nВы выбрали удаление мероприятия")
                id = input("Введите ID удаляемого мероприятия: ")
                try:
                    delete_event(id)
                    print("Мероприятие удалено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            elif cmd3 == 3:
                print("\nВы выбрали обновление мероприятия")
                id = input("Введите ID обновляемого мероприятия: ")
                title = input("Введите новое название мероприятия: ")
                date = input("Введите новую дату мероприятия: ")
                try:
                    update_event(title, date, id)
                    print("Информация о мероприятии обновлена.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            else:
                print("Вы ввели несуществующею команду. Попробуйте еще раз!")
            

        elif cmd == 5:  # Изменить список меcт
            print("\nЧто вы хотите сделать? (выберите нужную команду)")
            print("1. добавить место.")
            print("2. удалить место.")
            cmd3 = int(input("Введите команду "))
            if cmd3 == 1:
                print("\nВы выбрали добавление места")
                plase_name = input("Введите название места: ")
                try:
                    add_plase(plase_name)
                    print("Место добавлено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            elif cmd3 == 2:
                print("\nВы выбрали удаление места")
                id = input("Введите ID удаляемого места: ")
                try:
                    delete_plase(id)
                    print("Место удалено.")
                except Exception as e:
                    print(f"Что-то пошло не так! {e}")
            else:
                print("Вы ввели несуществующею команду. Попробуйте еще раз!")

        elif cmd == 6: # Изменить место проведения мероприятия
            print("\nВы выбрали обновление мероприятия")
            event_id = input("\nВведите ID мероприятия, место проведения которого хотите поменять: ")
            plase_id = input("Введите ID места проведения мероприятия: ")
            try:
                update_plase(plase_id, event_id)
                print("Информация о месте проведения мероприятия обновлена.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 7:  # Поиск объектов по названию
            query = input("\nЧто вы ищете (введите название): ")
            events = search_events_all(query)
            plases = search_plases_all(query)
            print(f"Найдено мероприятий по запросу '{query}':")
            for event in events:
                print(f"ID {event.id} - {event.title}.")
            print(f"Найдено меcт по запросу '{query}':")
            for plase in plases:
                print(f"ID {plase.id} - {plase.name}.")
        #     query = input("\nЧто вы ищете (введите название): ")
        #     with db_orm.connect_db() as conn, conn.cursor() as cur:
        #         cur.execute(f"SELECT * FROM events WHERE title = '{query}';")
        #         events = cur.fetchall()
        #     print(f"Найдено мероприятий по запросу:")
        #     for event in events:
        #         print(f"ID {event[0]} - {event[1]}.")
        #     with db_orm.connect_db() as conn, conn.cursor() as cur:
        #         cur.execute(f"SELECT * FROM plases WHERE name = '{query}';")
        #         plases = cur.fetchall()
        #     print(f"Найдено меcт по запросу:")
        #     for plase in plases:
        #         print(f"ID {plase[0]} - {plase[1]}.")
        
        elif cmd == 8:  # Поиск объектов по части названия
            query = input("\nЧто вы ищете (введите название/часть названия): ")
            events = search_events(query)
            plases = search_plases(query)
            print(f"Найдено мероприятий по запросу '{query}':")
            for event in events:
                print(f"ID {event.id} - {event.title}.")
            print(f"Найдено меcт по запросу '{query}':")
            for plase in plases:
                print(f"ID {plase.id} - {plase.name}.")
        
        # • Функционал для бронирования и отмены билетов"""
        elif cmd == 9:  # бронирование билетов
            print("\nВы выбрали бронирование билетов")
            event_id = input("Введите ID мероприятия, куда хотите забронировать билет: ")
            buyer = input("Введите ваше имя для покупки билета: ") 
            try:
                reserv_ticket(buyer, event_id)
                print("Билет успешно прибретен.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 10:  # возврат билетов
            print("\nВы выбрали возврат билетов")
            id = input("Введите ID билета: ")
            try:
                return_ticket(id)
                print("Билет успешно анулирован.")
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 11:  # Вывод информации о числе забронированных билетов по ID мероприятия
            print("\nВывод информации о числе забронированных билетов на мероприятие")
            id = input("Введите ID мероприятия: ")
            try:
                event_tickets = get_num_tickets(id)
                num_tickets = event_tickets["num_tickets"]
                event = event_tickets["event"]   
                for ev in event:
                    print(f"На мероприятие: '{ev.title}'  забронировано билетов: {num_tickets}")                   
            except Exception as e:
                print(f"Что-то пошло не так! {e}")
        
        elif cmd == 12:  # Вывод информации о числе забронированных билетов на мероприятие
            print("\nВывод информации о числе забронированных билетов на мероприятие")
            try:
                tickets_info = get_tickets()
                
                for t in tickets_info:
                    print(f'Уникальный номер билета: {t[0]}; Покупатель - {t[1]}; Название: {t[2]}, {t[3]}.')

            except Exception as e:
                print(f"Что-то пошло не так! {e}")

        else:
            print("Вы ввели несуществующею команду. Попробуйте еще раз!")
    

app()