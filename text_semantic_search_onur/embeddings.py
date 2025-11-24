from openai import OpenAI


def generate_embeddings(texts: list[str], oai_client: OpenAI, model: str = "text-embedding-ada-002"):
    response = oai_client.embeddings.create(input = texts, model = model)
    return [e.embedding for e in response.data]
