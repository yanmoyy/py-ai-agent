import os
import sys

from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions, call_function
from prompt import system_prompt


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)
        return

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print("User prompt:", user_prompt)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content(client, messages, verbose)


def generate_content(
    client: genai.Client, messages: list[types.Content], verbose: bool
):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],
            system_instruction=system_prompt,
        ),
    )
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")

        if verbose:
            print(f"-> {function_call_result.parts[0].functionc_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting")


if __name__ == "__main__":
    main()
