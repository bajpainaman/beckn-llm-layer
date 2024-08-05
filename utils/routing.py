from llms import get_llms

llm, structured_llm_router, _, _, _ = get_llms()

def route_question(state):
    question = state["question"]
    source = structured_llm_router.invoke({"question": question})
    if source.datasource == "web_search":
        return "web_search"
    elif source.datasource == "vectorstore":
        return "retrieve"

def decide_to_generate(state):
    filtered_documents = state["documents"]
    if not filtered_documents:
        return "transform_query"
    else:
        return "generate"

def grade_generation_v_documents_and_question(state):
    question = state["question"]
    documents = state["documents"]
    generation = state["generation"]

    score = hallucination_grader.invoke(
        {"documents": documents, "generation": generation}
    )
    grade = score.binary_score
    if grade == "yes":
        score = answer_grader.invoke({"question": question, "generation": generation})
        grade = score.binary_score
        if grade == "yes":
            return "useful"
        else:
            return "not useful"
    else:
        return "not supported"
