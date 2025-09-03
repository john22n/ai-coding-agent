import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import system_prompt, available_tools

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = sys.argv[1]
    if len(sys.argv) > 2:
        isVerbose = sys.argv[2]
    else:
        isVerbose = None

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]
    response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_tools], system_instruction=system_prompt),
            )

    if isVerbose == "--verbose":
        print(f"User prompt: {user_prompt}")
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    print("Hello from code-agent!")
    print(response.text)

    if response.function_calls:
        print(response.function_calls[0])
        print(f"Calling function: {response.function_calls[0].name}{response.function_calls[0].args}")


if __name__ == "__main__":
    main()
