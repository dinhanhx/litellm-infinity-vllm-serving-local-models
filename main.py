from cohere import ClientV2 as Cohere
from openai import OpenAI

text = "Hello there!"
list_texts = ["Hello there!", "How are you?", "How do you do?"]

base_url = "http://localhost:8793"
# OpenAI
openai_client = OpenAI(api_key="empty", base_url=base_url)
embeddings = openai_client.embeddings.create(
    input=list_texts, model="jina-embeddings-v3"
).data
print(len(embeddings), len(embeddings[0].embedding))

completion = openai_client.chat.completions.create(
    model="Llama-3.2-1B-Instruct",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
    ],
)
print(completion.choices[0].message.content)

# Cohere
cohere_client = Cohere(api_key="empty", base_url=base_url)
rerank_results = cohere_client.rerank(
    query=text,
    documents=list_texts,
    model="jinaai/jina-reranker-v2-base-multilingual",
    return_documents=False,
)
print(len(rerank_results.results))
