import openai
import gradio
messages = role": "system", "content": "You are a psychologist"}1
def CustomChatGPT(user_input):
    messages. append(("role": "user", "content": user_input})
     response = openai.ChatCompletion. create
        model = "gpt-3.5-turbo",
        messages = messages
    ChatGPT_reply = response ["choices"] [0] ["message"1 ["content"]
    messages. append(("role": "assistant", "content": ChatGPT_reply})
     return ChatGPT_reply
demo = gradio.Interface(fn=CustomChatGPT, inputs DE "text", outputs - "text", title - "Your Title")
demo. launch()

