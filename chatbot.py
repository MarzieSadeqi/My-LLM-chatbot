import openai
import time
import config

# Set your OpenAI API key using the new client interface
client = openai.OpenAI(api_key=config.OPENAI_API_KEY)

# Initial system prompt
SYSTEM_PROMPT = "You are a helpful assistant."

# Chat history
conversation_history = [
    {"role": "system", "content": SYSTEM_PROMPT}
]

def chat_with_gpt(user_input):
    conversation_history.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=conversation_history,
            temperature=0.7
        )
        reply = response.choices[0].message.content.strip()
        conversation_history.append({"role": "assistant", "content": reply})
        return reply
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    print("Welcome to the Mini Chatbot! (Type 'exit' to quit)")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        reply = chat_with_gpt(user_input)
        print(f"Bot: {reply}")
        time.sleep(0.5)
