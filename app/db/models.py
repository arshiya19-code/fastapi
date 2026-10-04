
from pydantic import BaseModel


class Answer(BaseModel):
    question_id: int
    alternative_id: int


class UserAnswer(BaseModel):
    user_id: int
    answers: list[Answer]

    def to_payload(self):
        return self.dict()
