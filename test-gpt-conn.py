import sys
import os
from pprint import pprint
from dotenv import load_dotenv
from openai import OpenAI, AzureOpenAI


##
# Main function to test the ability connect to an OpenAI or Azure-hosted GPT LLM, send a simple
# prompt, and receive a text completion response..
##
def main():
    config = load_api_config()
    response_text = prompt_llm_get_response(config)
    print(f"\nPROMPT:\n\n{config.get('prompt')}\n")
    print("---------------")
    print(f"\nANSWER:\n\n{response_text}\n")


##
# Send the a prompt to the GPT LLM's API and return its response.
# Sets some extra parameters for using the GPT4 API if hitting an Azure hosted version of the API.
##
def prompt_llm_get_response(config):
    if config.get("api_type").lower() == AZURE_TYPE:
        client = AzureOpenAI(
            api_key=config.get("api_key"),
            api_version=config.get("api_version"),
            azure_endpoint=config.get("api_base"),
        )
    else:
        client = OpenAI(
            api_key=config.get("api_key"),
        )

    messages = [{"role": "user", "content": config.get("prompt")}]
    completion = client.chat.completions.create(
        model=config.get("api_model"),
        messages=messages,
        temperature=TEMP,
    )

    return completion.choices[0].message.content


##
# Loads API configuration from a .env file.
##
def load_api_config():
    load_dotenv()
    config = {
        "api_key": os.getenv("API_KEY", "").strip(),
        "api_model": os.getenv("API_MODEL", "").strip(),
        "api_base": os.getenv("API_BASE", "").strip(),
        "api_type": os.getenv("API_TYPE", "").strip(),
        "api_version": os.getenv("API_VERSION", "").strip(),
        "prompt": os.getenv("PROMPT", "").strip(),
    }

    if not config.get("api_key"):
        raise ValueError("No 'API_KEY' value defined in '.env' file or env var")

    if not config.get("api_model"):
        raise ValueError("No 'API_MODEL' value defined in '.env' file or env var")

    if not config.get("prompt"):
        raise ValueError("No 'PROMPT' value defined in '.env' file or env var")

    return config


# Constants
TEMP = 0.1
AZURE_TYPE = "azure"


##
# Main
##
if __name__ == "__main__":
    main()
