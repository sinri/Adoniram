import random

from adoniram.task.BaseTaskSeeker import BaseTaskSeeker


class TaskSeekerForP1(BaseTaskSeeker):
    def seek_one_task_reference_for_processor(self):
        return random.Random().randint(-1000, 1000)
