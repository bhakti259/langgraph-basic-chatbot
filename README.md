# LangGraph Basic Chatbot

A conversational AI chatbot built with **LangGraph**, featuring a **Streamlit** web interface, multi-thread support, and **SQLite-based** conversation history management.

## Features

✨ **Core Features:**
- 🤖 AI-powered conversation using OpenAI's GPT models
- 💬 Multi-threaded chat support (separate conversations)
- 💾 Persistent conversation history with SQLite database
- 🎯 Clean and intuitive Streamlit UI
- 🔄 Real-time streaming responses
- 📱 Responsive web interface

## Tech Stack

- **Backend:** LangGraph, LangChain, OpenAI API
- **Frontend:** Streamlit
- **Database:** SQLite with LangGraph checkpoints
- **Language:** Python 3.10+ (3.11–3.12 recommended)

## Installation

### Prerequisites
- Python 3.10+ (3.11–3.12 recommended; Python 3.14 may show Pydantic v1 warnings)
- OpenAI API key
- Git

### Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/bhakti259/langgraph-basic-chatbot.git
cd langgraph-basic-chatbot
```

2. **Create and activate a virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create a `.env` file in the project root:**
```bash
OPENAI_API_KEY=your_api_key_here
```

Get your OpenAI API key from: https://platform.openai.com/api-keys

5. **Run the application:**
```bash
python -m streamlit run streamlit_frontend_db.py
```

The app will open at `http://localhost:8501`

## Project Structure

```
langgraph-basic-chatbot/
├── langgraph_db_backend.py          # LangGraph chatbot logic with SQLite
├── streamlit_frontend_db.py         # Streamlit web interface
├── streamlit_frontend_threading.py  # Threading-based frontend (alternative)
├── streamlit_frontend_wit_streamingh.py # Streaming-based frontend (alternative)
├── langgraph_chatbot.db             # SQLite database (auto-created)
├── .env                             # Environment variables (create locally)
├── .gitignore                       # Git ignore rules
├── requirements.txt                 # Python dependencies
└── README.md                        # This file
```

## Usage

### Basic Workflow

1. **Start a New Chat:** Click "New Chat" button in the sidebar
2. **Send a Message:** Type your message and press Enter
3. **View History:** All conversations are saved and appear in the sidebar
4. **Switch Conversations:** Click any thread ID in the sidebar to load previous chats
5. **Refresh Browser:** Your chat history persists even after refresh

### Database

- Conversation history is automatically saved to `langgraph_chatbot.db`
- SQLite checkpoint storage ensures thread-safe operations
- Delete the `.db` file to reset all conversations

## Configuration

### Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-...your-key-here...

# Optional: LangSmith tracing for monitoring and debugging
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_API_KEY=your-langsmith-api-key
LANGCHAIN_PROJECT=your-project-name
```

**Required:**
- `OPENAI_API_KEY`: Your OpenAI API key

**Optional:**
- `LANGCHAIN_TRACING_V2`: Enable LangSmith tracing (set to `true` to enable)
- `LANGCHAIN_ENDPOINT`: LangSmith API endpoint
- `LANGCHAIN_API_KEY`: LangSmith API key (from https://smith.langchain.com)
- `LANGCHAIN_PROJECT`: Project name for organizing traces in LangSmith

### Optional Configuration

Edit `langgraph_db_backend.py` to customize:
- LLM model (default: `gpt-4`)
- Temperature and other OpenAI parameters
- Database filename

## API Usage

### Backend Functions

#### `get_all_threads()`
Returns a list of all conversation thread IDs from the database.

```python
from langgraph_db_backend import get_all_threads
threads = get_all_threads()
```

#### `chatbot.invoke()`
Send a message and get a response.

```python
from langgraph_db_backend import chatbot
from langchain_core.messages import HumanMessage

config = {'configurable': {'thread_id': 'your-thread-id'}}
response = chatbot.invoke(
    {'messages': [HumanMessage(content='Hello!')]},
    config=config
)
```

## Troubleshooting

### Issue: `streamlit: command not found`
**Solution:** Activate your virtual environment first
```bash
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### Issue: `ModuleNotFoundError: No module named 'langgraph'`
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Pydantic v1 warning on Python 3.14
**Symptom:** `Core Pydantic V1 functionality isn't compatible with Python 3.14 or greater.`

**Solution:** Use Python 3.11 or 3.12 for best compatibility with LangChain/LangGraph.

### Issue: OpenAI API errors
**Solution:** Check your API key:
- Verify `OPENAI_API_KEY` is set correctly in `.env`
- Check you have sufficient API credits
- Ensure the key hasn't expired

### Issue: Database locked
**Solution:** Stop the app and delete `langgraph_chatbot.db`, then restart

## Development

### Installing Additional Dependencies
```bash
pip install package-name
pip freeze > requirements.txt  # Update requirements
```

### Running Tests
```python
python langgraph_db_backend.py  # Check if backend initializes correctly
```

## Future Enhancements

- [ ] Add conversation naming feature
- [ ] Implement user authentication
- [ ] Add multiple AI models support
- [ ] Export conversations to PDF/JSON
- [ ] Add conversation search functionality
- [ ] Rate limiting and usage tracking
- [ ] Docker containerization

## Contributing

Feel free to fork, create a branch, and submit pull requests!

## License

MIT License - see LICENSE file for details

## Support

For issues or questions:
- Open an issue on [GitHub](https://github.com/bhakti259/langgraph-basic-chatbot/issues)
- Check existing issues for solutions

## Credits

- Built with [LangGraph](https://github.com/langchain-ai/langgraph)
- UI powered by [Streamlit](https://streamlit.io)
- LLM by [OpenAI](https://openai.com)

---

**Last Updated:** February 10, 2026
