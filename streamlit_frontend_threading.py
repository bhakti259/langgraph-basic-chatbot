import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage
import uuid


#*********************************UTILITY FUNCTIONS*************************************
#with help of UUID library generate unique thread ids for new chats
def generate_thread_id():
    return str(uuid.uuid4())    

def reset_chat():
    new_thread_id = generate_thread_id()
    st.session_state['thread_id'] = new_thread_id
    add_thread_to_list(new_thread_id)
    st.session_state['message_history'] = []
    
    
def add_thread_to_list(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation_history(thread_id):
    try:
        return chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']
    except (KeyError, AttributeError):
        return []
        
#*****************************SESSION SET UP***********************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()
    
if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []
    
#load all threads at page load    
add_thread_to_list(st.session_state['thread_id'])
    
#*********************SIDEBAR UI*********************************************
#create simple sidebar with streamlit widgets to set thread_id
with st.sidebar:
    st.title("LangGraph Chatbot")
    st.header("My conversations")
    for thread in reversed(st.session_state['chat_threads']):
        if st.button(f"Thread ID: {thread}", key=thread):
            print("Loading thread: ", thread)
            st.session_state['thread_id'] = thread
            
            messages = load_conversation_history(thread)
            temp_messages = []
            
            for msg in messages:
                if isinstance(msg, HumanMessage) or msg.type == "human":
                    role = "user"
                else:
                    role = "assistant"
                temp_messages.append({"role": role, "content": msg.content})
            
            st.session_state['message_history'] = temp_messages
            print("Loaded messages for thread ", thread, ": ", temp_messages)
        
    if st.button("New Chat"):
        reset_chat()

    
#***************************** MAIN UI _ CHAT INTERFACE***********************************

#load converation history
for message in st.session_state['message_history']:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.text(message["content"])
    else:
        with st.chat_message("assistant"):
            st.text(message["content"])
    
user_input = st.chat_input("Type your message here...")

if user_input:
    
    #first add message to history
    st.session_state['message_history'].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)
    
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
   
    
    # calling chatbot.stream inside st.write_stream to stream response
    #chatbot.stream yields message chunks and metadata
    #sending content of message chunks to st.write_stream to display them as they arrive
    
    with st.chat_message("assistant"):
        ai_message =st.write_stream(
            message_chunk.content for message_chunk, metadata in chatbot.stream(
                {'messages': [HumanMessage(content = user_input)]},
                config = CONFIG,
                stream_mode ='messages'             
            )
        )
        
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
        