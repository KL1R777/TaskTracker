import time


from models import Task, Tracker
from storage import download_data_from_db


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        print(f"Программа завершена. Время работы: {time.time() - start}")
        return res
    return wrapper


@timer
def main():
    is_running = True
    try:
        while is_running:
            print("=== ТРЕКЕР ЗАДАЧ ===")
            print("1. Добавить задачу")
            print("2. Показать все задачи")
            print("3. Показать задачи по статусу")
            print("4. Отметить задачу выполненной")
            print("5. Удалить задачу")
            print("6. Импортировать задачи")
            print("7. Выйти")
            ans = input("Выбор: ")


            if ans == "1":
                title = input("Название задачи: ")

                level = input("Сложность задачи (low, medium, hard): ")
                if level.lower() in ("low", "medium", "hard"):
                    task = Task(title,level.lower())
                    tracker.add_task(task)
                    print("Задача успешно добавлена")
                else:
                    print("Сложность задачи должна быть в диапазоне (low, medium, hard)!")



            elif ans == "2":
                tracker.check_tasks()

            elif ans == "3":
                try:
                    comp = input("Введите True или False: ")
                    if comp.lower() == "true":
                        tracker.find_task_by_completed(True)
                    if comp.lower() == "false":
                        tracker.find_task_by_completed(False)


                except ValueError:
                    print("Выберите True или False !")



            elif ans == "4":
                try:
                    id = int(input("Введите номер задачи: "))
                    task = tracker.find_task(id)
                    if isinstance(task, Task):
                        if task.completed == False:
                            task.completed = True
                            print("Задача отмечена как выполненой")
                        else:
                            print("Задача уже выполнена")

                    else:
                        print("Такой задачи нету")
                except ValueError:
                    print("Вы ввели нечисловые данные")

            elif ans == "5":
                try:
                    id = int(input("Введите номер задачи: "))
                    task = tracker.delete_task(id)
                    if isinstance(task, Task):
                        print("Задача удалена")

                    else:
                        print("Такой задачи нету")
                except ValueError:
                    print("Вы ввели нечисловые данные")
            elif ans == "6":
                # Можно не создавать файл там есть файл по умолчанию
                download_data_from_db(tracker)
                print("Задачи добавлены успешно")
            elif ans == "7":
                from storage import save_data_in_db
                print("До свидание")
                save_data_in_db(tracker)
                is_running = False

            else:
                print("Введите число от 1 до 7")




    except ValueError:
        print("Вы ввели нечисловые данные")
    except KeyboardInterrupt:
        print("Выход из программы")


if __name__ == "__main__":
    tracker = Tracker()
    tracker.start_auto_save(0.0000000000000001)
    main()







