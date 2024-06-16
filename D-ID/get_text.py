from openai import OpenAI
import os
import sys
import time
from typing import List, Optional
import argparse



class PDFAssistant:
    """
    A class to interact with the OpenAI API to create an assistant for answering questions based on a PDF file.

    Attributes:
        client (OpenAI): Client for interacting with OpenAI API.
        assistant_id (Optional[str]): ID of the created assistant. None until an assistant is created.
    """

    def __init__(self) -> None:
        """
        Initializes the PDFAssistant with the API key from environment variables.
        """
        self.client = OpenAI(api_key='sk-proj-hChtu2v4Jo3XsHV27RxAT3BlbkFJyXhC1oDAsddecDd5eHiu')
        self.assistant_id: Optional[str] = None

    def upload_file(self, filename: str) -> None:
        """
        Uploads a file to the OpenAI API and creates an assistant related to that file.

        Args:
            filename (str): The path to the file to be uploaded.
        """
        file = self.client.files.create(
            file=open(filename, 'rb'),
            purpose="assistants"
        )

        assistant = self.client.beta.assistants.create(
            name="PDF Helper",
            instructions="You are my assistant who can answer by using the information of given pdf",
            model="gpt-4-1106-preview",
            tools=[{"type": "retrieval"}],
            file_ids=[file.id]
        )
        self.assistant_id = assistant.id

    def get_answers(self, question: str) -> List[str]:
        """
        Asks a question to the assistant and retrieves the answers.

        Args:
            question (str): The question to be asked to the assistant.

        Returns:
            List[str]: A list of answers from the assistant.

        Raises:
            ValueError: If the assistant has not been created yet.
        """
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
    parser = argparse.ArgumentParser(description="Creating txt file.")
     
    parser.add_argument('--pdf', type=str, help='pdf file directory')
    args = parser.parse_args()

    client = PDFAssistant()
    client.upload_file(args.pdf)
    # client.upload_file("/mnt/disk1/ivymm02/information/steve_jobs_info.pdf")

    question_template = "Write a one-minute-long speech for {} by using the pdf that contains my information. Don't include any description of nonverbal communication. Don't use text-to-speech challenging words. Don't use e-mail format or letter format. You don't need to include every information that I gave you. The speech must be less than 200 words."
    tone = input("Tell me the purpose of your speech (ex. online date, job interview, ...): ")
    question = question_template.format(tone)

    answers = client.get_answers(question)
    file_path = "/mnt/disk1/ivymm02/gpt_answer_steve_jobs.txt"
    for answer in answers:
        print(answer)
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(answer)