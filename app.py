import os
import gradio as gr
from google import genai
import config

client = genai.Client(
    vertexai=True,
    project=config.GCP_PROJECT_ID,
)

def predict(user_prompt):
    response = client.models.generate_content(
        model=config.MODEL_NAME,
        contents=user_prompt
    )
    return response.text

# Створюємо інтерфейс
demo = gr.Interface(
    fn=predict,                 # Функція, яку викликає Gradio
    inputs="text",              # Поле введення (текст)
    outputs="text",             # Поле виведення (текст)
    title="Gemini Vertex AI",   # Заголовок
    description="`Введіть запит до Gemini через Google Cloud Vertex AI"
)

if __name__ == "__main__":
    port = int(os.getenv("PORT", 7860))
    demo.launch(
        server_name="0.0.0.0",
        server_port=port,
        theme=gr.themes.Soft()
    )
