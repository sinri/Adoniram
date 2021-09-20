from adoniram.task.BaseTaskHandler import BaseTaskHandler


class TaskHandlerForP1(BaseTaskHandler):
    def _load_task_detail(self):
        self.is_positive = self.get_task_reference() > 0
        # self.is_negative=self.get_task_reference()<0

    def handle(self):
        if self.is_positive:
            self.set_task_handle_result(True)
            self.set_task_handle_feedback('POSITIVE')
        else:
            self.set_task_handle_result(False)
            self.set_task_handle_feedback('NOT_POSITIVE')
