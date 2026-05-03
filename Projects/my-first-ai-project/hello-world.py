from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import sys
import logging


# configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
logging.getLogger("openai").setLevel(logging.DEBUG)
logging.getLogger("httpx").setLevel(logging.DEBUG)

class OpenAIFoundry:
       def __init__(self) :
           pass

       def hello_world(self):
                '''function to call AzureOpenAI endpoint'''
                endpoint_url, api_key, deployment_name = self._load_environment_config();
                print(f"Endpint {endpoint_url}")
                print(f"api_key {api_key}")
                print(f"deployment_name {deployment_name}")
                client = OpenAI(
                base_url = endpoint_url,
                api_key = api_key
                )
                #print(f"client: {client}")
                
                completetion = client.chat.completions.create (
                      model = deployment_name,
                      messages = [ 
                            {
                                "role": "user",
                                "content": "Why the colour of the blood is red"
                            }
                        ]
                )
                print(completetion);

       def _load_environment_config(self):
                load_dotenv();
                endpoint_url = os.getenv('ENDPOINT_URL')
                api_key = os.getenv('API_KEY')
                deployment_name = os.getenv('DEPLOYMENT_NAME')
                return endpoint_url, api_key, deployment_name;

if __name__ == "__main__":
    logging.info('********Starting the conversation with AzureOpenAI*********')

    # Initialize AzureOpenAI
    try:
        openai_client = OpenAIFoundry()
        openai_client.hello_world()
    except Exception as e:
        logging.error(f'Exception has occurred while initializing OpenAI {e}')
        sys.exit(1)
