import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate

load_dotenv(".env", override=True)
url = os.getenv("LMS_BASE_URL")
key = os.getenv("LMS_TOKEN")

os.system("clear")

llm = ChatOpenAI(
    model="gemma-4-e4b-it-qat",
    base_url=url,
    api_key=key,
    default_headers={"authorization": "Bearer " + key},
)

# messages = [
#     SystemMessage(content="You're a helpful programming assistant"),
#     HumanMessage(
#         content="Write a Python function to calculate factorial. only give raw code that i can paste in a file, no reasoning or extra text strictly, not event code markers."
#     ),
# ]

# output = llm.invoke(messages)
# print(output.content)

template = ChatPromptTemplate.from_messages(
    [
        {"role": "system", "content": "You are a english to spanish translator"},
        {"role": "human", "content": "translate this text please: {text_to_translate}"},
    ]
)

text = input("Enter some text to translate to spanish: ")
chain = template | llm
output = chain.invoke(template.format_messages(text_to_translate="" + text))
print(output.content)
