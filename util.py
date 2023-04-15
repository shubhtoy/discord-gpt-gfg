import openai

API_KEY = "YOUR-OPEN-AI-API-KEY"

openai.api_key = API_KEY


def getResponse(prompt):
    global conversation
    conversation.append({"role": "user", "content": prompt})
    conversation = chatGPTResponse(conversation)

    return conversation[-1]["content"].strip()


# Function that generates the response from ChatGPT
def chatGPTResponse(conversation):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=conversation
        )
    except openai.error.APIConnectionError:
        return None

    conversation.append(
        {
            "role": response.choices[0].message.role,
            "content": response.choices[0].message.content,
        }
    )
    return conversation


def initializeConversation():
    global conversation
    conversation = []
    conversation.append({"role": "system", "content": "How may I help you?"})
    conversation = chatGPTResponse(conversation)


# Below code is just for testing purpose

if __name__ == "__main__":
    choice = 1
    initializeConversation()
    while choice != 0:
        prompt = input("Enter your prompt: ")
        response = getResponse(prompt)
        print(response)
        choice = int(input())
