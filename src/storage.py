from models import Task, Tracker
import json


def save_data_in_db(tracker: Tracker, filename: str = "tasks.json"):

    with open(filename, 'w', encoding="utf-8") as f:
        data = {}

        i = 0
        for t in tracker.get_tasks():
            t: Task

            data[i] = [t.title, t.level, t.completed]
            i += 1

        json.dump(data, f, indent=2)


def download_data_from_db(tracker: Tracker,filename: str = "tasks.json"):

    with open(filename, 'r', encoding="utf-8") as f:

        data = json.load(f)
        for i in data.keys():
            if i == "0":
                Task._next_id = 0
            else:
                title = data[i][0]
                level = data[i][1]
                completed = data[i][2]

                task = Task(title, level, completed)

                tracker.add_task(task)














