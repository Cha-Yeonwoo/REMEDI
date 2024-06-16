from openai import OpenAI
import os
import sys
import time
from typing import List, Optional


class PDFAssistant:

    def __init__(self) -> None:

        self.client = OpenAI(api_key='sk-proj-7z0CTIw1tvlU6C5xHlBrT3BlbkFJo8KpLl8ZA8tCJDb23go7')
        self.assistant_id: Optional[str] = None

    def upload_file(self, filename: str) -> None:

        file = self.client.files.create(
            file=open(filename, 'rb'),
            purpose="assistants"
        )

    

        # assistant = self.client.beta.assistants.create(
        #     name="PDF Helper",
        #     instructions="You are my assistant who can answer questions from the given pdf",
        #     model="gpt-4-1106-preview",
        #     tools=[{"type": "retrieval"}].
        #     file_ids=[file.id]
        # )
        # assistant = self.client.beta.assistants.create(
        #     name="PDF Helper",
        #     instructions="You are my assistant who can answer questions from the given pdf",
        #     model="gpt-4-1106-preview",
        #     tools=[{
        #         "type": "retrieval",
        #         "file_ids": [file.id]
        #     }]
        # )
        assistant = self.client.Assistant.create(
            name="PDF Helper",
            instructions="You are my assistant who can answer questions from the given pdf",
            model="gpt-4-1106-preview",
            tools=[{
                "type": "file_search",
                "file_ids": [file.id]
            }]
        )

        self.assistant_id = assistant.id

    def get_answers(self, question: str) -> List[str]:

        if self.assistant_id is None:
            raise ValueError("Assistant not created. Please upload a file first.")

        thread = self.client.beta.threads.create()

        self.client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )

        run = self.client.beta.threads.runs.create(
            thread_id=thread.id,
            assistant_id=self.assistant_id
        )

        while True:
            run_status = self.client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)
            time.sleep(10)
            if run_status.status == 'completed':
                messages = self.client.beta.threads.messages.list(thread_id=thread.id)
                break
            else:
                time.sleep(2)

        return [message.content[0].text.value for message in messages.data if message.role == "assistant"]


if __name__ == "__main__":
    client = PDFAssistant()
    client.upload_file('/mnt/disk1/ivymm02/D-ID/hello.pdf')

    while True:
        question_template = "Can you write a self introduction script in {} situation?"
        tone = input("상황을 입력하세요 (예 : online date, office interview): ")
        question = question_template.format(tone)
        if question.lower() in ['exit', 'quit']:
            break

        answers = client.get_answers(question)
        for answer in answers:
            print(answer)