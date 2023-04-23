import openai
from django.http import JsonResponse

def home_page(request):
    prompt = request.GET.get('prompt', '')
    response = get_chat_gpt_response(prompt)
    return JsonResponse({'response': response})

def get_chat_gpt_response(prompt):
    openai.api_key = "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"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        # n=1,
        # stop=".",
        temperature=0.7,
    )
    return response.choices[0].text.strip()
