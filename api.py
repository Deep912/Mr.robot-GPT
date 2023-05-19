import openai
import config

api_key = config.Development.OPENAI_KEY

openai.api_key = api_key


def CreatingResponse(prompt):
    messages = []
    messages.append({"role": "system", "content": "You are a cyber expert."})
    
    question = {}
    question['role'] = 'user'
    question['content'] = prompt
    messages.append(question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",messages=messages) 
   
    try:
        answer = response['choices'][0]['message']['content'].replace('\n' , '<br>')
    except:
        answer = "hehe ask something else"
    return answer

