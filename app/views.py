from django.shortcuts import render
from openai import OpenAI
from django.conf import settings
import requests
import prompts




print(f'#############')

openai_client = OpenAI(

    api_key=settings.OPENAI_API_KEY
)
rag_endpoint = settings.RAG_ENDPOINT
rag_api_key = settings.RAG_API_KEY

headers = {
    'Authorization': f'Api-Key {rag_api_key}'
    }

system_prompt = prompts.SP
assistant_prompt = prompts.AP
knowledge_base = prompts.KB



def rag_agent(query):

    data = {
      
    'kb_id': '6828c12a-4d29-49d7-afba-86deddb775e4',
    'query': '{}'.format(query),
    'strict_knowledge_prompt': 'I want you to act as a support agent. Your name is "DocWing". You will provide me with answers from the given info. If the answer is not included, say exactly "Hmm, I am not sure." and stop after that. Refuse to answer any question not about the info. Never break character.',
    'tmp': '0.7',
    'max_tokens': '500',
}
    res = requests.post(rag_endpoint, headers=headers, data=data)
    # print the response "response"
    response = res.json().get('response')
    print(f'#### response: {response}')
    return response


def relevance_agent(query, rag_response):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": "You will evaluate the provided data. check if the services recommended align with the users medical query, respond only with yes or no"}, {"role": "user", "content": query}],
        max_tokens=150,
        temperature=0.7,)
    
    relevance = response.choices[0].message.content
    print(f'#### relevance: {relevance}')
    return relevance
    

def generate_response(query):

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": system_prompt},{"role": 'assistant', 'content': assistant_prompt}, {"role": "user", "content": query}],
        max_tokens=150,
        temperature=0.7,)
    return response.choices[0].message.content

def generate_symptoms_response(query):

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": 'based on a query provided, ask for more details about thei query'},{"role": 'assistant', 'content': "do not give medical advicec"}, {"role": "user", "content": query}],
        max_tokens=150,
        temperature=0.7,)
    return response.choices[0].message.content



def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(f'#### query: {query}')
        rag = rag_agent(query)
        relevance = relevance_agent(query)
        if relevance == 'yes':
            res = generate_response(query)
        else:
            res = generate_symptoms_response(query)

    return res

