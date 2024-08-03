import os
from utils import extract_code_without_backticks
from openai import OpenAI
from prompts import DiamondifyPrompt


class Diamondify:
    def _init_(self, model, input, output, file):

        self.model = model
        self.input = input
        self.output = output
        self.client = OpenAI()
        self.prompts = DiamondifyPrompt
        self.file: bool = file

    def generate_clean_code(self):
        # For "file", if its true, then it will parse it as a single file
        # if "file" is false, then the input will be parsed as a directory
        file_name = "diamondified_" + self.input
        if self.file:
            print(f"---CLEANING {self.input}---")
            with open(self.input, "r") as f:
                content = str(f.read())
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": self.prompts.system},
                        {"role": "user", "content": self.prompts.user+f" {content}"}
                    ],
                    temperature=1.2,
                )

                result = "\n".join(
                    text_piece for text_piece in extract_code_without_backticks(response.choices[0].message.content))
                with open(os.path.join(self.output, file_name), "w") as fi:
                    fi.write(result)
                    print(f"---SAVED CLEANED {self.input}---")

        else:
            files_in_dir = os.listdir(self.input)
            for document in files_in_dir:
                print(f"---CLEANING {document}---")
                with open(os.path.join(self.input, document), "r") as f:
                    content = f.read()
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=[
                            {"role": "system", "content": self.prompts.system},
                            {"role": "user", "content": self.prompts.user + f" {content}"}
                        ],
                        temperature=1.2,
                    )
                    result = "\n".join(text_piece for text_piece in extract_code_without_backticks(response.choices[0].message.content))
                    with open(os.path.join(self.output, file_name), "w") as fi:
                        fi.write(result)
                        print(f"---SAVING CLEANED{document}---")

    def _call_(self):
        print("---STARTING CODE CLEANING---")
        self.generate_clean_code()
        print("---ALL CODE CLEANED---")