import os
from openai import OpenAI

class MatusAuto:
    def __init__(self, interpreter):
        self.interpreter = interpreter
        self.client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

    def autonomous_task(self, task_description, max_attempts=5):
        print(f"Starting autonomous task: {task_description}")
        attempts = 0
        success = False
        last_error = ""

        while attempts < max_attempts and not success:
            attempts += 1
            print(f"Attempt {attempts} of {max_attempts}...")
            
            # Use AI to generate code for the task
            prompt = f"""
            You are an autonomous agent using the Matus programming language.
            The user wants to achieve this task: {task_description}
            
            Last error (if any): {last_error}
            
            Provide ONLY the Matus code to achieve this task. 
            Matus supports:
            - print(msg)
            - var = value
            - if condition: (with 4-space indentation)
            - for var in list: (with 4-space indentation)
            - func name(params): (with 4-space indentation)
            - get_ip(domain), scan_ports(target, ports), run_cmd(cmd)
            - read_file(path), write_file(path, content)
            - admin_sys_info(), admin_list_procs(), admin_kill_proc(pid)
            
            Respond with ONLY the code block, no explanations.
            """
            
            try:
                response = self.client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=[{"role": "user", "content": prompt}]
                )
                generated_code = response.choices[0].message.content.strip()
                if "```" in generated_code:
                    generated_code = generated_code.split("```")[1]
                    if generated_code.startswith("matus"):
                        generated_code = generated_code[5:]
                    elif generated_code.startswith("python"):
                        generated_code = generated_code[6:]
                
                print(f"Executing generated code:\n{generated_code}")
                
                # Capture output and check for success
                try:
                    self.interpreter.execute(generated_code)
                    print("Execution finished. Verifying success...")
                    
                    # AI verification
                    verify_prompt = f"Did the following execution successfully achieve the task '{task_description}'? Respond with 'YES' or 'NO'.\n\nCode:\n{generated_code}"
                    verify_response = self.client.chat.completions.create(
                        model="gpt-4.1-mini",
                        messages=[{"role": "user", "content": verify_prompt}]
                    )
                    if "YES" in verify_response.choices[0].message.content.upper():
                        success = True
                        print("Task completed successfully!")
                    else:
                        last_error = "AI verification failed. Task might not be fully achieved."
                except Exception as e:
                    last_error = str(e)
                    print(f"Execution error: {last_error}")
            
            except Exception as e:
                last_error = f"AI Generation error: {e}"
                print(last_error)

        if not success:
            print(f"Failed to complete task after {max_attempts} attempts.")
        return success

def inject_auto_tools(interpreter):
    auto = MatusAuto(interpreter)
    interpreter.variables['auto_task'] = auto.autonomous_task
