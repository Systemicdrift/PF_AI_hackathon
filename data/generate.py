import json
import nltk
import openai


# receivers = [
#     "sites",
#     "evse",
#     # "solar",
#     # "storage",
# ]

# statuses = ["Firing", "Resolved"]
# sites_alerts = ["Site not reporting", "Site "]

# evse_alerts = ["EVSE Faulty", "EVSE Above pilot threshold", "EVSE Not Reporting"]

# solar_alerts = []
# storage_alerts = []

# customers = {"0001":"Kwik E Mart", "0002": "Moe's Tavern", "0003": "Lard Lad Donuts", "0004": "Krusty Burger", "0005": "Leftorium"}
# sites = ["01", "02", "03", "04", "05"]
# groups = ["01", "02"]
# stations = ["01","02","03","04","05","06","07","08","09","10"]

openai.api_key = "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"

# Define function to generate response from ChatGPT
def generate_response(prompt, model, max_tokens=60):
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = response.choices[0].text.strip()

    return message

def preprocess_alerts(alerts):
    # Convert alerts from JSON to Python dictionary
    alerts_dict = alerts #json.loads(alerts)

    # Extract relevant information from alerts
    alert_texts = []
    for alert in alerts_dict['alerts']:
        alert_text = alert['annotations']['summary']
        alert_texts.append(alert_text)

    # Tokenize alert text
    tokenized_alerts = []
    for alert_text in alert_texts:
        tokens = nltk.word_tokenize(alert_text)
        tokenized_alerts.append(tokens)

    # Convert tokens to lowercase
    lowercase_alerts = []
    for tokens in tokenized_alerts:
        lowercase_tokens = [token.lower() for token in tokens]
        lowercase_alerts.append(lowercase_tokens)

    # Concatenate tokens into text strings
    formatted_alerts = []
    for tokens in lowercase_alerts:
        text = ' '.join(tokens)
        formatted_alerts.append(text)

    return formatted_alerts

if __name__ == "__main__":
    file_path = "./sample.json" # replace with the path to your file
    print(file_path)
    with open(file_path, "r") as f:
        data = json.load(f)

        formatted_alerts = preprocess_alerts(data)
        print(formatted_alerts)

        prompt = "I have received the following alerts:\n"
        for alert in formatted_alerts:
            prompt += "- " + alert + "\n"
        prompt += "What actions should I take?"

        # Generate response from ChatGPT
        model = "davinci"  # replace with your preferred ChatGPT model
        response = generate_response(prompt, model)
        print(response)

