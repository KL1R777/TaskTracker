# level - сложность
# dealine - в секундах измеряется срок выполнения
# title - название задачи
# prosrochka - задача не выполнена в срок
import time
from threading import Thread
class Task:
    _next_id = 0  # ID каждой задачи

    def __init__(self, title: str, level: str, completed: bool = False) -> None:
        Task._next_id += 1
        self.id = Task._next_id
        self.title = title
        self.level = level
        self.completed = completed



# Список тасков




class Tracker:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__tasks = []

        return cls._instance

    def start_auto_save(self, interval=30):
        self.auto_save_running = True

        def save_loop():
            from storage import save_data_in_db
            while self.auto_save_running:
                time.sleep(interval)
                save_data_in_db(self)

        thread = Thread(target=save_loop, daemon=True)
        thread.start()

    def stop_auto_save(self):
        self.auto_save_running = False



    def get_tasks(self):
        return self.__tasks.copy()
    def add_task(self, task: Task):
            self.__tasks.append(task)

            return task

    def find_task_by_completed(self, completed: bool):
        for i in self.get_tasks():

                if i.completed == completed:
                    print(f"Задача {i.id}. {i.title}: Сложность - {i.level}; Выполнена - {i.completed}")


    def find_task(self, id: int) -> Task | str: # Бинарный поиск (быстрее из-за упорядоченого id)
        l, r = 0, len(self.__tasks) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.__tasks[mid].id == id:
                return self.__tasks[mid]


            if self.__tasks[mid].id > id:
                r = mid - 1
            else:
                l = mid + 1

        return f"Задача с ID {id} не найдена"


    def update_task(self, id:int, title:str | None =None, level:str | None =None,completed:bool | None=None,):
        l, r = 0, len(self.__tasks) - 1
        while l <= r:
            mid = (l + r) // 2

            if self.__tasks[mid].id == id:
                self.__tasks[mid].completed = completed if completed else self.__tasks[mid].completed
                self.__tasks[mid].title = title if title else self.__tasks[mid].title
                self.__tasks[mid].level = level if level else self.__tasks[mid].level

                return self.__tasks[mid]
            if self.__tasks[mid].id > id:
                r = mid - 1
            else:
                l = mid + 1

        return f"Задача с ID {id} не найдена"
    def delete_task(self, id):

        l, r = 0, len(self.__tasks) - 1

        while l <= r:
            mid = (l + r) // 2

            if self.__tasks[mid].id == id:
                task = self.__tasks[mid]
                self.__tasks.remove(self.__tasks[mid])
                return task
            if self.__tasks[mid].id > id:
                r = mid - 1
            else:
                l = mid + 1

        return f"Задача с ID {id} не найдена"


    def check_tasks(self):

        if self.__tasks:
            for i in self.__tasks:
                print(f"Задача {i.id}. {i.title}: Сложность - {i.level}; Выполнена - {i.completed}")

        else:
             print("Задач пока нету в трекере")







