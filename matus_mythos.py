import os
from openai import OpenAI

class MatusMythos:
    def __init__(self):
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def analyze_code_for_vulnerabilities(self, code_snippet):
        prompt = f"Analyze the following code snippet for potential security vulnerabilities and suggest improvements:\n\n```\n{code_snippet}\n```\n\nProvide a concise summary of findings and actionable recommendations."
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-4.1-mini", # Using a more advanced model for security analysis
                messages=[
                    {"role": "system", "content": "You are a world-class security researcher specialized in zero-day discovery."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during AI analysis: {e}"

    def suggest_exploit_path(self, vulnerability_description):
        prompt = f"Given the following vulnerability description, suggest a potential exploit path or method:\n\n{vulnerability_description}\n\nProvide a high-level overview of the exploit strategy."
        
        try:
            response = self.client.chat.completions.create(
                model="gemini-2.5-flash", # Using a suitable LLM for analysis
                messages=[
                    {"role": "system", "content": "You are a security expert specialized in outlining exploit strategies."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error during AI analysis: {e}"

def inject_mythos_tools(interpreter):
    mythos_instance = MatusMythos()
    interpreter.variables["mythos_analyze_code"] = mythos_instance.analyze_code_for_vulnerabilities
    interpreter.variables["mythos_suggest_exploit"] = mythos_instance.suggest_exploit_path
