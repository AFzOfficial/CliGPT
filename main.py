import openai, os, time, platform

openai.api_key = '' # set your API key

# store messages in memmory
messages = []



def type_animation(text):
    '''
    this function for typing animation in CLI
    input: str
    output: char
    '''

    for char in text:
        time.sleep(0.020)
        print(char, end='', flush=True)



def send_request(prompt):
    '''
    send requests to openai API
    input: user prompt
    output: system response
    '''
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    response = response.choices[0].message["content"]

    return response





def main():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    while True:
        prompt = input('\n>>> ')

        messages.append({"role": "user", "content": f"{prompt}"})

        try:
            response = send_request(prompt)

            messages.append({"role": "system", "content": f"{response}"})

            print('\n\nCHAT GPT : ', end=' ')

            type_animation(response)

            print('\n')

        except Exception as e:
            print(f'\nCHAT GPT : {e}\n')




            
main()
