from django.shortcuts import render
from openai import OpenAI
from django.conf import settings
import requests



# Create your views here.



print(f'#############')

openai_client = OpenAI(

    api_key=settings.OPENAI_API_KEY
)
rag_endpoint = settings.RAG_ENDPOINT
rag_api_key = settings.RAG_API_KEY

headers = {
    'Authorization': f'Api-Key {rag_api_key}'
    }




def rag_agent(query):

    data = {
      
    'username': 'mc',
    'password': 'hiii',
    'action': 'view_file',
    'kb_id': '6828c12a-4d29-49d7-afba-86deddb775e4',
    'query': '{}'.format(query),
    'strict_knowledge_prompt': 'recommend the suitable service based on the symptoms if the services are relevant to user query, recommend the service to use, else ask more questions to understand the user query better',
    'tmp': '0.7',
    'max_tokens': '500',
}
    res = requests.post(rag_endpoint, headers=headers, data=data)
    # print the response "response"
    response = res.json().get('response')
    print(f'#### response: {response}')
    return response

    


def relevance_agent(query):
    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo", 
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
        max_tokens=150,
        temperature=0.7,)
    
    relevance = response.choices[0].message.content
    print(f'#### relevance: {relevance}')
    return relevance
    





def home(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        print(f'#### query: {query}')
        rag = rag_agent(query)
        relevance = relevance_agent(query)
        return render(request, 'home.html', {'relevance': relevance, 'rag': rag})

    return {'response': 'Hello World'}

