# infrastructure/llm.py
from abc import ABC, abstractmethod
from typing import Dict
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)

class LLMHelper:
    def __init__(self):
        self.system_prompt = """
        You are an expert at summarizing text into concise bullet-point lists.
        """

        
    def get_sample_prompt(self) -> dict[str, dict[str, str]]:
        prompts = {
            "system": {
                "role": "system",
                "content": ""
            },
            "user": {
                "role": "user",
                "content": ""
            }
        }
        return prompts
    

    def get_prompt(self, system_content, user_content) -> list[dict[str, str]]:
        prompts = self.get_sample_prompt()
        prompts["system"]["content"] = system_content
        prompts["user"]["content"] = user_content

        return [
        prompts["system"],
        prompts["user"]
        ]

    def get_user_prompt(self, text: str) -> str:
        user_prompt = f"""
            Please summarize the following text into a concise bullet-point list suitable for inclusion in a brochure about the company.
            Text:
            {text}
            Provide the summary in the following JSON format:
            {{
                "summary": [
                    "First bullet point",
                    "Second bullet point",
                    "Third bullet point"
                ]
                }}
            """
        return user_prompt
    
    def prepare_prompt(self, text: str) -> list[dict[str, str]]:
        prompts = self.get_prompt(self.system_prompt, self.get_user_prompt(text))
        return prompts
    

    def get_gpt_response(self, prompt, model) -> str:
        openai = OpenAI()
        response = openai.chat.completions.create(
            model=model,
            messages=prompt
        )
        result = response.choices[0].message.content
        return result
    
    def parse_summary(self, text: str, model: str) -> str:
        prompt = self.prepare_prompt(text)
        response = self.get_gpt_response(prompt, model)
        return response


class BaseLLM(ABC):
    @abstractmethod
    def summarize(self, text:str) -> str: ...

    @abstractmethod
    def classify(self, subject:str, body:str) -> Dict[str,str]: ...

    @abstractmethod
    def suggest_reply(self, thread:str) -> str: ...

class OpenAILLM(BaseLLM):
    def __init__(self, model:str): 
        super().__init__()
        self.llm_helper = LLMHelper()
        self.model = model


    def summarize(self, text:str)->str: 
        return self.llm_helper.parse_summary(text, self.model)

    def classify(self, subject:str, body:str)->Dict[str,str]:
        # ...
        return {"category":"Bug","priority":"medium"}
    
    def suggest_reply(self, thread:str)->str:
        # ...
        return "Proposed reply..."

class OllamaLLM(BaseLLM):
    def __init__(self, model:str): self.model = model
    # implement similarly for local models

def llm_factory(provider:str, model:str) -> BaseLLM:
    if provider == "openai": return OpenAILLM(model)
    if provider == "ollama": return OllamaLLM(model)
    raise ValueError("Unknown LLM provider")