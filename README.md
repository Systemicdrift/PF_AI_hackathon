# PF_AI_hackathon
A production of Von, Tal and Anthony

## About
This project springs from onboarding documentatioon that that Axcess team has stood up to onboard new members of the team. There was expressed interest from across the organization to share those docs with other teams and subsequently non-powerflex employees. This would serve to inform the public in a conversational tone rather than present a stale readme to folks.

Ask it "what is Axcess", "What is authz"... 

There is also a similar experiement for alerts, but it does not have enough data.

## Getting Started

pip3 install pipenv

python3 -m venv venv

pip3 install -r requirements.txt

python3 app/gpt.py

python3 app/alerts.py

## ChatGPT
At it's core, the Open AI chatgpt3 engine was used to create the underlying models and the Completion class to field requests. We consulted the documentation more than actually using chatgpt to build these models. We found that a lot of the answers chatgpt would give about itself were completely wrong. 

## Obtaining Data
The more data you have the better the model responds. We grabbed text from the onboarding docs and converted it to json using chatgpt. This is how we obtained data in the format that's accepted.

We started by giving it a body of text and instructing it generate questions based on the given text.
![Screen Shot![Screen Shot 2023-03-15 at 8 07 49 PM](https://user-images.githubusercontent.com/96091647/225483709-39d1fe81-084f-4f0b-82ae-903ef75e04b2.png)

Here's one of the responses
![Screen Shot 2023-03-15 at 8 07 49 PM](https://user-images.githubusercontent.com/96091647/225483808-86536e55-8b02-49c7-a6e0-90e5133375f9.png)

## Python
Python was an easy choice for this project as the base tools are written in python and there is good support.

## Evolution
1. Build your first jsonl file, filled with prompts/completions.
2. Run the file through the fine-tuner: openai tools fine_tunes.prepare_data -f ./alerts.jsonl
3. Create the model: openai api fine_tunes.create -t ./alerts_prepared.jsonl -m davinci
4. Follow it's progress: openai api fine_tunes.follow -i ft-XIDtEA4HxOHW4PStoRZtNEHI

## Value Proposition
1. Surfacing documenation has long been a difficult task, this could provide a curated view into Powerflex's inner workings.
2. Surfacing other tid bits of information has long been sought after as well, such as how do we handle alerting. The use case for this particular tool was to provide actions for specific types of alerts. Unfortunately the way the data was imported was not suitable for chatgpt's model.
3. We can use this model to share information, and ultimately sell our products and services. EG: A chat bot that allows users to ask about products and curates a solution based on thier needs, without a sales person breathing down their backs.





