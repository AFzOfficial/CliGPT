import openai, os, time, platform

openai.api_key = '' # SET YOUR API KEY


messages = []


def Typing(text):
    for char in text:
        time.sleep(0.020)
        print(char, end='', flush=True)



def app():
    os.system('cls' if platform.system() == 'Windows' else 'clear')
    while True:
        promt = input('\n>>> ')

        messages.append({"role": "user", "content": f"{promt}"})

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            response = response.choices[0].message["content"]

            messages.append({"role": "system", "content": f"{response}"})

            print('\n\nGPT : ', end=' ')

            Typing(response)

            print('\n')

        except Exception as e:
            print(f'\nGPT : {e}\n')




app()