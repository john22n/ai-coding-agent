import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import call_function, available_functions
from prompts import system_prompt

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []

    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    if not args:
        print("AI code assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "how do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)]),]

    try:
        for i in range(20):
            text = generate_content(client, messages, verbose)
            if verbose:
                print("iteration", i + 1, "text:", repr(text))
            if text:
                print("final response")
                print(text)
                break
        else:
            print("reached max iterations without final response")

    except Exception as e:
        print("error:", e)

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
            ),
    )

    for candidate in response.candidates:
        messages.append(candidate.content)

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        part = function_call_result.parts[0]

        if not part.function_response:
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {part.function_response.response}")

        function_responses.append(part)

        messages.append(types.Content(role="user", parts=[part]))


    if not function_responses:
        raise Exception("no function responses generated, exiting.")


if __name__ == "__main__":
    main()
