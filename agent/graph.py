import os
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage, RemoveMessage
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langgraph.checkpoint.memory import InMemorySaver
from agent.my_prompt import prompt

class State(TypedDict):
    """
    Represents the state of the agent.
    """
    messages: Annotated[list[AnyMessage], add_messages]
    
def clean_messages(state: State) -> State:
    """
    Cleans the messages in the state except for the last one.
    Args:
        state (State): The current state of the agent.
    Returns:
        state (State): The updated state with only the last message retained.
    """
    messages = state["messages"]
    last_message = messages[-1]
    rest_messages = messages[:-1] if len(messages) > 1 else []
    
    return {"messages": [RemoveMessage(id=m.id) for m in rest_messages] + [last_message]}

def chatbot(state: State) -> str:
    """
    Contacts LLM to get a response based on the current state.
    Args:
        state (State): The current state of the agent.
    Returns:
        state (State): The updated state with the response.
    """
    params = {
        "azure_endpoint": os.getenv("AZURE_ENDPOINT"),
        "azure_deployment": os.getenv("AZURE_DEPLOYLMENT"),
        "api_version": os.getenv("MODEL_API_VERSION"),
        "api_key": os.getenv("AZURE_API_KEY"),
        "timeout": 60,
    }
    model = ChatOpenAI(
        model="gpt-4.1-mini"
    )

    chain = {"query": RunnablePassthrough()} | prompt | model
    
    messages = state["messages"]
    response = chain.invoke(messages)
    return { "messages": [response] }

builder = StateGraph(State)

builder.add_node('chatbot', chatbot)
builder.add_edge(START, 'chatbot')
builder.add_edge('chatbot', END)

checkpointer = InMemorySaver()

graph = builder.compile()