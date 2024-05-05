from openai import OpenAI
from prompt import Instructions
from eval import get_most_similar
import re

NUM_RESPONSES = 3

client = OpenAI(
    api_key="sk-proj-q6ZPouc5d3SyOU4siaa6T3BlbkFJ3gh3BdU0P0t2BMYzcAf1",
)

def GPT(prompt):
    response = client.chat.completions.create(
        model = 'gpt-3.5-turbo',
        messages=[{"role": "user", "content": prompt + Instructions}]
    )
    return response.choices[0].message.content.strip()

def remove_initial_colon_number(text):
    pattern = r'^\d+:'
    cleaned_text = re.sub(pattern, '', text)
    return cleaned_text.strip()

def generateText(prompt):
    # generating three responses with same prompt
    responses = []
    for i in range(0, NUM_RESPONSES):
        responses.append(GPT(prompt))

    # most similar response to the input prompt
    best_response = get_most_similar(responses, prompt)

    # splitting the response in lines
    lines = [line for line in best_response.split('\n') if line.strip()]

    pages = [] # variable to store the text of each page
    prompts = [] # variable to store the image prompts of each page
    for i in range(2, len(lines), 2):
        pages.append(remove_initial_colon_number(" ".join(lines[i].split()[1:])))

    for i in range(3, len(lines), 2):
        prompts.append(" ".join(lines[i].split()[1:]))

    # preparing the return context
    context = {
        'title': " ".join(lines[0].split()[1:]).strip(),
        'genre': " ".join(lines[1].split()[1:]).strip(),
        'text': pages,
        'prompts': prompts
    }

    return context
