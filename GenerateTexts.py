import openai

def get_facts(topic):

    openai.api_key = "[[Insert openai api key]]"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt="Create three tik-tok like plain text for curious facts about "+topic+" separated by enters without text before or after",
        temperature=0.5,
        max_tokens=150,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    facts = response['choices'][0]['text'].strip().split('\n')
    return facts
