import os
import json
import chromadb
from chromadb.utils import embedding_functions

# Create / connect to local ChromaDB database
def get_chroma_client():
    return chromadb.PersistentClient(path="./chroma_db")

def setup_and_populate_db():
    """
    Creates the ChromaDB collection and loads sports facts
    from data/sports_facts.json.
    """

    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    json_file_path = os.path.join("data", "sports_facts.json")

    # Check if data file exists
    if not os.path.exists(json_file_path):
        print(f"Error: Raw fact data file not found at {json_file_path}")
        return collection

    # Load and parse facts
    with open(json_file_path, "r") as f:
        facts_list = json.load(f)

    documents = []
    metadata_list = []
    ids = []

    for idx, item in enumerate(facts_list):
        documents.append(item["fact"])
        metadata_list.append({"sport": item["sport"]})
        ids.append(f"fact_{idx}")

    # Bulk add vectors to collection
    collection.add(
        documents=documents,
        metadatas=metadata_list,
        ids=ids
    )

    print(f"Successfully vectorized and stored {len(documents)} facts.")
    return collection

def query_historic_facts(sport: str, n_results: int = 3):
    """
    Retrieve relevant sports facts from ChromaDB.
    """

    client = get_chroma_client()

    embedding_fn = embedding_functions.DefaultEmbeddingFunction()

    collection = client.get_or_create_collection(
        name="sports_history",
        embedding_function=embedding_fn
    )

    results = collection.query(
        query_texts=[sport],
        n_results=n_results
    )

    if results["documents"]:
        return results["documents"][0]

    return []