from typing import List

from sdclientapi import API
from sqlalchemy.orm.session import Session

from securedrop_client.api_jobs.base import ApiJob


class SeenJob(ApiJob):
    def __init__(self, files: List[str], messages: List[str], replies: List[str]) -> None:
        super().__init__()
        self.files = files
        self.messages = messages
        self.replies = replies

    def call_api(self, api_client: API, session: Session) -> str:
        """
        Override ApiJob.

        Mark files, messages, and replies as seen
        """
        api_client.seen(self.files, self.messages, self.replies)
