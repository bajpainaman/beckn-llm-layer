from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_openai import ChatOpenAI

class RouteQuery(BaseModel):
    datasource: str = Field(
        ..., description="Given a user question choose to route it to web search or a vectorstore."
    )

class GradeDocuments(BaseModel):
    binary_score: str = Field(
        description="Documents are relevant to the question, 'yes' or 'no'"
    )

class GradeHallucinations(BaseModel):
    binary_score: str = Field(
        description="Answer is grounded in the facts, 'yes' or 'no'"
    )

class GradeAnswer(BaseModel):
    binary_score: str = Field(
        description="Answer addresses the question, 'yes' or 'no'"
    )

def get_llms():
    llm = ChatOpenAI(model="gpt-3.5-turbo-0125", temperature=0)
    structured_llm_router = llm.with_structured_output(RouteQuery)
    structured_llm_grader = llm.with_structured_output(GradeDocuments)
    structured_llm_hallucination_grader = llm.with_structured_output(GradeHallucinations)
    structured_llm_answer_grader = llm.with_structured_output(GradeAnswer)
    return llm, structured_llm_router, structured_llm_grader, structured_llm_hallucination_grader, structured_llm_answer_grader
