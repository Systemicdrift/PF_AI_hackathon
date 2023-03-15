import openai

fine_tuned_model = "curie:ft-personal-2023-03-15-17-51-00"
openai.api_key = "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"


def chatGptConversation(conversation):
    response = openai.Completion.create(
        model=fine_tuned_model, prompt=conversation)

    print(response)


chatGptConversation("what is authz?")
