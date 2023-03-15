# PF_AI_hackathon
A production of Von, Tal and Anthony

## About
This project builds a chatgpt model that consumes Powerflex documentation to learn about PF projects in a conversational tone. Ask it "what is Axcess", "What is authz"... 

There is also a similar experiement for alerts, but it does not have enough data.

## Getting Started

pip3 install pipenv

python3 -m venv venv

pip3 install -r requirements.txt

python3 app/gpt.py

python3 app/alerts.py
