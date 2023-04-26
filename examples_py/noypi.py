import os
import sys
import openai
import textwrap

openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = "gpt-3.5-turbo"

# messages = [{"role": "system", "content": "You are a friendly poet from the Philippines and you explain the moral values of your poem in simple terms in Filipino."}]
messages = [{"role": "system", "content": "You are a friendly assistant from the Philippines that answers question in Filipino."}]
def chat_completion():
    while True:
        prompt = input('\nYou: ')
        messages.append(
            {"role": "user", "content": prompt }
        )
        completion = openai.ChatCompletion.create(
            model = MODEL,
            max_tokens = 250,
            messages = messages
        )

        response = completion['choices'][0]['message']['content']
        response = textwrap.fill(response, width=50)

        messages.append(
            {"role": "assistant", "content": "response" }
        )
        if prompt in ["bye","exit","goodbye","end"]:
            print('\nChatGPT: Paalam. Hanggang sa susunod na pagkakataon!')
            sys.exit()
        else:
            print(f'\nChatGPT:',response)
            continue

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = "ChatAI (Filipino Poet)\n\nTo END session, type: 'bye, goodbye, end or exit"
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')

    if not openai.api_key:
        print("ERROR: No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit()
    
        
    chat_completion()

if __name__ == '__main__':
    main() 
