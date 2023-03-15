import openai

fine_tuned_model = "davinci:ft-personal-2023-03-15-23-27-41"
openai.api_key = "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"

# Created fine-tune: ft-XIDtEA4HxOHW4PStoRZtNEHI

def chatGptConversation(prompt):
    response = openai.Completion.create(
        model=fine_tuned_model, prompt=prompt, temperature=0.1, max_tokens=25)

    print(response.choices[0].text)

if __name__ == "__main__":
    while(1):
        print("What is the nature of your powerflex emergency?")
        prompt = input()
        chatGptConversation(prompt)
    # chatGptConversation("how do I triage a faulty evse?")
    # chatGptConversation("how do I fix a site not reporting?")
