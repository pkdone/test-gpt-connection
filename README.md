# Test GPT Connecton

A simple project that uses the OpenAI API to test that it can connect to an OpenAI or Azure-hosted GPT LLM, send a simple prompt, and receive a text completion response.


## Prerequisites

1. Ensure you have an OpenAI or Azure OpenAI GPT model accessible along with appropriate API keys / credentials.

1. Ensure you have installed Python 3 and [PIP](https://pip.pypa.io/en/stable/installation/) on your workstation.

1. In a terminal on your workstation, from the root folder of this project, run the following command to copy an example environment configuration file to a new file into the same root folder called **`.env`**, and then edit the values for the properties shown in this new **`.env`** file to reflect your specific environment settings:

    ```console
    cp 'EXAMPLE.env' '.env'
    ```

1. In the terminal, initialise the required Python environment for you to be able to execute the application correctly.

    ```console
    python3 -m pip install --user virtualenv
    python3 -m venv my-test-env
    source my-test-env/bin/activate
    python -m pip install --upgrade pip
    python -m pip install -r requirements.txt
    ```

## Execution

- From the terminal, execute the followwing command.

    ```console
    python test-gpt-conn.py
    ```
