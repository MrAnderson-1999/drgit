from ast import main
import requests, logging, os

api_key = os.environ.get("OPENAI_API_KEY")


def get_text():
    # Specify the path to the file you want to read
    file_path = 'Untitled-1.json'

    # Open the file in read mode ('r')
    try:
        with open(file_path, 'r') as file:
            # Read the entire content of the file into a variable
            file_content = file.read()
            # Now, 'file_content' contains the content of the file
            return file_content
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        

def send_req():
    url = "https://api.openai.com/v1/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(api_key)
    }

    payload = {
        "model": "text-davinci-003",
        "prompt": "{}".format(get_text()),
        # "temperature": 0,
        "max_tokens": 700
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        logging.debug(f"Error: {response.json()}")
        print(f"Error: {response.json()}")
    else:
        return response.json()["choices"][0]["text"]
    

print(send_req())