from adoniram.message.BaseRequestMessage import BaseRequestMessage
from adoniram.message.BaseResponseMessage import BaseResponseMessage
from adoniram.processor.AdoniramProcesserClient import AdoniramProcesserClient


class AdoniramProcesserClientForP1(AdoniramProcesserClient):
    def handle_server_response_for_task_done(self, response_message: BaseResponseMessage):
        """
        TODO parse task_reference
        :param response_message:
        :return:
        """
        pass

    def should_processer_stop(self) -> bool:
        pass

    def make_request_for_seeking_next_task_from_server(self) -> BaseRequestMessage:
        """
        TODO return a RequestMessageAsSeekTaskToHandle
        :return:
        """
        pass
