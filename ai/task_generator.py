import openai
from typing import List, Dict

class AITaskGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key
    
    def generate_tasks(self, project_desc: str) -> List[Dict]:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Generate specific workflow tasks from project description"},
                {"role": "user", "content": project_desc}
            ]
        )
        return self._parse_response(response.choices[0].message.content)
    
    def _parse_response(self, text: str) -> List[Dict]:
        # Implementation to parse AI response
        pass
