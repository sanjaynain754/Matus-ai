"""
AutoAgent - AI-Powered Autonomous Task Agent
Controlled by Datya | Optional OpenAI integration
"""

import os

try:
    from openai import OpenAI
    HAS_OPENAI = True
except ImportError:
    HAS_OPENAI = False


class AutoAgent:
    """Autonomous AI agent for complex task execution"""

    def __init__(self):
        self.client = None
        if HAS_OPENAI:
            api_key = os.environ.get("OPENAI_API_KEY")
            if api_key:
                try:
                    self.client = OpenAI(api_key=api_key)
                except Exception:
                    pass

    def auto_task(self, task_description):
        """Run an autonomous AI-powered task"""
        if self.client is None:
            return ("Auto task requires OpenAI API key.\n"
                    "Set OPENAI_API_KEY environment variable to enable AI features.\n"
                    "You can still use all other Datya tools without AI.")

        prompt = f"""You are Datya, the AI agent of Matus AI (Admin: Sanjay).
Task: {task_description}

Provide a step-by-step solution as a numbered list.
Keep it concise and actionable."""

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are Datya, an AI agent controlling security and system tools."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI task error: {str(e)}"

    def auto_analyze(self, text):
        """AI-powered text analysis"""
        if self.client is None:
            return "OpenAI not available for analysis."

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Analyze the following text and provide key insights, risks, and recommendations."},
                    {"role": "user", "content": str(text)}
                ],
                max_tokens=800,
                temperature=0.5
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Analysis error: {str(e)}"

    def auto_generate_code(self, description, language="python"):
        """AI-powered code generation"""
        if self.client is None:
            return "OpenAI not available for code generation."

        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"Generate clean {language} code based on the description. Only output code."},
                    {"role": "user", "content": str(description)}
                ],
                max_tokens=1500,
                temperature=0.3
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Code generation error: {str(e)}"

    def get_tools(self):
        """Return all tools as a dict"""
        tools = {
            'auto_task': self.auto_task,
        }
        if self.client is not None:
            tools['auto_analyze'] = self.auto_analyze
            tools['auto_generate_code'] = self.auto_generate_code
        return tools
