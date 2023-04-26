import os
import sys
import openai
import textwrap

openai.api_key = os.getenv('OPENAI_API_KEY')

MODEL = "gpt-3.5-turbo"

messages = [{"role": "system", "content": "You are a sarcastic assistant that reluctantly answers questions with sarcastic responses."}]

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
            print('\nChatGPT: Goodbye. See you next time!')
            sys.exit()
        else:
            print(f'\nChatGPT:',response)
            continue

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    app_name = "ChatAI (Sarcastic)\n\nTo END session, type: 'bye, goodbye, end or exit"
    print(f'{"-" * 48}')
    print(f'{" " * 12}{app_name}{" " * 12}')
    print(f'{"-" * 48}')

    if not openai.api_key:
        print("ERROR: No OpenAI API key found. Please set the OPENAI_API_KEY environment variable.")
        sys.exit()
    
        
    chat_completion()

if __name__ == '__main__':
    main() 
