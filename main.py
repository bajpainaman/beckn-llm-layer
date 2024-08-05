
from environment import set_environment
from index import build_index
from graph import build_graph
from pprint import pprint

def main():
    set_environment()

    urls = [
        "https://lilianweng.github.io/posts/2023-06-23-agent/",
        "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
        "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
    ]

    retriever = build_index(urls)
    app = build_graph()

    inputs = {"question": "What player are the Bears expected to draft first in the 2024 NFL draft?"}
    for output in app.stream(inputs):
        for key, value in output.items():
            pprint(f"Node '{key}':")
            pprint("\n---\n")

    pprint(value["generation"])

if __name__ == "__main__":
    main()
