from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_core.messages import AnyMessage
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langgraph.checkpoint.memory import InMemorySaver
from agent.my_prompt import prompt

class State(TypedDict):
    """
    Represents the state of the agent.
    """
    messages: Annotated[list[AnyMessage], add_messages]


def chatbot(state: State) -> str:
    """
    Contacts LLM to get a response based on the current state.
    Args:
        state (State): The current state of the agent.
    Returns:
        state (State): The updated state with the response.
    """
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