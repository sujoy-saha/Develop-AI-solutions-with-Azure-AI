import os
from dotenv import load_dotenv

# Add OpenAI import
import openai

def main(): 
        
    try: 
    
        # Get configuration settings 
        load_dotenv()
        azure_oai_api_type = os.getenv("AZURE_OAI_API_TYPE")
        azure_oai_api_version = os.getenv("AZURE_OAI_API_VERSION")
        azure_oai_endpoint = os.getenv("AZURE_OAI_ENDPOINT")
        azure_oai_key = os.getenv("AZURE_OAI_KEY")
        azure_oai_model = os.getenv("AZURE_OAI_MODEL")              
               
        # Set OpenAI configuration settings
        openai.api_type = azure_oai_api_type
        openai.api_version = azure_oai_api_version # this may change in the future
        openai.api_base = azure_oai_endpoint
        openai.api_key = azure_oai_key

        # Send a completion call to generate an answer
        print('Sending a test completion job')
        prompt = 'Write a tagline for an ice cream shop. '
        response = openai.Completion.create(engine=azure_oai_model, prompt=prompt, max_tokens=10)
        text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
        print(prompt+text)

    except Exception as ex:
        print(ex)

if __name__ == '__main__': 
    main()