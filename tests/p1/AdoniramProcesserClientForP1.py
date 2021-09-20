from adoniram.message.BaseRequestMessage import BaseRequestMessage
from adoniram.message.BaseResponseMessage import BaseResponseMessage
from adoniram.message.request.RequestMessageAsSeekTaskToHandle import RequestMessageAsSeekTaskToHandle
from adoniram.processor.AdoniramProcesserClient import AdoniramProcesserClient
from p1.TaskHandlerForP1 import TaskHandlerForP1


class AdoniramProcesserClientForP1(AdoniramProcesserClient):

    def __init__(self, host: str, port: int, name: str):
        super().__init__(host, port, name)
        self.__count = 0

    def handle_server_response_for_task_done(self, response_message: BaseResponseMessage):
        """
        parse task_reference
        :param response_message:
        :return:
        """
        task_reference = response_message.read_data(('task_reference',))

        task_handler = TaskHandlerForP1(task_reference)
        task_handler.handle()

        self.get_logger().notice(
            'TASK OVER',
            {
                'task': task_reference,
                'result': task_handler.get_task_handle_result(),
                'feedback': task_handler.get_task_handle_feedback(),
            }
        )

        self.__count += 1

    def should_processer_stop(self) -> bool:
        return self.__count > 10

    def make_request_for_seeking_next_task_from_server(self) -> BaseRequestMessage:
        """
        return a RequestMessageAsSeekTaskToHandle
        :return:
        """
        return RequestMessageAsSeekTaskToHandle().build(
            self.get_processor_name(),
            task_seeker_class='TaskSeekerForP1',
            task_seek_conditions={
                'condition_a': 'A',
            }
        )
