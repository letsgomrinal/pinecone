from pinecone import Pinecone
from pinecone import ServerlessSpec
from config import *



def create_vector_store_index():
    """
    Creates Pinecone Index if doesn't exist!
    """
    pc = Pinecone(api_key=PINECONE_API_KEY)
    if not pc.has_index(name=PINECONE_INDEX_NAME):
        pc.create_index(
        name=PINECONE_INDEX_NAME,
        dimension=DIMENSIONS, # dimensionality of MiniLM
        metric=METRIC,
        spec = ServerlessSpec(
            cloud=CLOUD, 
            region=REGION
        )
    )
    # Initialize index client
    index = pc.Index(name=index_name)
    # View index stats
    return index.describe_index_stats()