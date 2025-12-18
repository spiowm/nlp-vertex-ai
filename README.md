# 📝 Text Transformer

AI-powered text style transformation application using Google Vertex AI and Gemini.

## Features

- Transform text into different writing styles:
  - **Formal** - Professional and business-like tone
  - **Casual** - Conversational and relaxed style
  - **Simple** - Easy to understand, even for children
  - **Poetic** - Metaphorical and artistic expression

- Clean output without AI introductions or explanations
- Modern Gradio interface with examples
- Single LLM call architecture

## Prerequisites

- Python 3.13+
- Google Cloud Project with Vertex AI enabled
- Valid GCP credentials

## Installation

```bash
uv sync
```


## Configuration

Create a `.env` file in the project root:

```env
GCP_PROJECT_ID=your-project-id
MODEL_NAME=gemini-2.5-flash-lite
PORT=7860
```

## Running the Application

### Local Development

```bash
python app.py
```

The application will be available at `http://localhost:7860`

### Docker

```bash
docker-compose up --build
```

## Project Structure

```
.
├── app.py              # Main application
├── config.py           # Configuration loader
├── Dockerfile          # Container definition
├── docker-compose.yml  # Docker orchestration
├── pyproject.toml      # Python dependencies
└── .env               # Environment variables
```

## Usage

1. Enter your text in the input field
2. Select the desired style from the dropdown
3. Click "✨ Трансформувати" button
4. Get the transformed text instantly

## License

MIT

