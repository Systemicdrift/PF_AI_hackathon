import openai

fine_tuned_model = "davinci:ft-personal-2023-03-15-22-47-24"
openai.api_key = "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"


def chatGptConversation(conversation):
    response = openai.Completion.create(
        model=fine_tuned_model, prompt=conversation, temperature=0.1)

    print(response.choices[0].text)


if __name__ == '__main__':
    while 1:
        print("Ask me a question about Powerflex...")
        query = input()
        chatGptConversation(query)
