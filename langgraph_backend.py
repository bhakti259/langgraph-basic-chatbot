from langgraph.graph import StateGraph, START, END, add_messages
from typing import TypedDict, Annotated, Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel,Field
from langchain_core.messages import SystemMessage, HumanMessage, BaseMessage
from langgraph.checkpoint.memory import MemorySaver
import operator
 

load_dotenv()

llm = ChatOpenAI()


#define state
class ChatState(TypedDict):
    messages: Annotated[list[BaseMessage], add_messages]

#define graph
graph = StateGraph(ChatState)

def chat_node(state: ChatState):
    
    #fetch user queries from state
    messages = state['messages']
    
    #send them to llm
    response = llm.invoke(messages)
    
    return {'messages': [response]}
    
#add node
graph.add_node('chat_node', chat_node)

#add edges
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

checkpointer = MemorySaver()

#compile graph
chatbot = graph.compile(checkpointer=checkpointer)