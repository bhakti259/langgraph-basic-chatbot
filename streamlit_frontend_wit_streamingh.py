import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = '1'

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
        