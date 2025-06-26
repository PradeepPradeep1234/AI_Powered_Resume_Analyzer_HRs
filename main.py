import requests

API_KEY = "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"  # Replace with your actual key

def chat_with_deepseek(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",  # Use your domain if hosted
        "X-Title": "DeepSeek Chatbot"
    }

    payload = {
    "model": "deepseek/deepseek-chat:free",  # or deepseek/deepseek-chat-v3:free
    "messages": [
        {"role": "system", "content": "You are a helpful chatbot."},
        {"role": "user", "content": prompt}
    ]
}

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        print("Error:", response.status_code, response.text)
        return None


# Run chatbot loop
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    reply = chat_with_deepseek(user_input)
    print("Bot:", reply)
