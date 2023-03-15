import json
import openai

openai.api_key = "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"

fine_tuned_model = ""

alerts_collection = {'EVSE Faulty': ['Check if Nexus box is reporting', 'Remotely restart EVSE from Nexus box', 'Send a tech out to check on the EVSE hardware'],
                    'EVSE Not Reporting': ['Check if Nexus box is reporting', 'Check if EVSE appears in Nexus site tree', 'Remotely restart EVSE from Nexus box', 'Send a tech out to check on the EVSE hardware'],
                    'Site not reporting': ['Check if this is a scheduled outage', 'Check if the Network Cradle is operational','Check Nexus box responds to SSH connections', 'Send tech to site to check on and restart the Nexus box']}

# Define function to generate response from ChatGPT
# def chatGptConversation(conversation):
#     response = openai.Completion.create(
#         model=fine_tuned_model, prompt=conversation)

#     print(response)

if __name__ == "__main__":
    keys = alerts_collection.keys()

    for key in keys:
        for action in alerts_collection[key]:
            print('{"prompt": "' + key + '", "completion": "'+ action +'"}')

    pass


# openai api fine_tunes.create -t ./alerts_prepared.jsonl -m davinci