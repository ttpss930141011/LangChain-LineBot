""" This module is responsible for creating a new window.
"""


from typing import Dict

from src.interactor.interfaces.repositories.agent_executor_repository import AgentExecutorRepositoryInterface
from src.interactor.interfaces.logger.logger import LoggerInterface
from langchain.agents import AgentExecutor
from linebot.v3.webhooks import MessageEvent


class CreateTextMessageReplyUseCase():
    """ This class is responsible for creating a new window.
    """

    def __init__(
            self,
            repository: AgentExecutorRepositoryInterface,
            logger: LoggerInterface,
            window: Dict,

    ):
        self.repository = repository
        self.logger = logger
        self.window = window
        self.agent_executor: AgentExecutor

        if not self.window.get("window_id"):
            raise ValueError("Window id is required")
    
    def _get_agent_executor(self) -> None:
        """
        Retrieves the agent executor associated with the current window.

        :param None: This function does not take any parameters.
        :return: None
        """
        
        self.agent_executor = self.repository.get(window_id=self.window.get("window_id"))
        if self.agent_executor is None:
            self.agent_executor = self.repository.create(
                window_id=self.window.get("window_id"),
            )

    def execute(self, event: MessageEvent) -> str:
        """
        Executes the function and returns a string.

        Parameters:
            event (MessageEvent): The event object containing the message text.
            
        Returns:
            str: The response generated by the agent executor.
        """
        
        self._get_agent_executor()

        response = self.agent_executor.run(input=event.message.text)
        return response
