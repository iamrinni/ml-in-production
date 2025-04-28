import time
import numpy as np
import pandas as pd
import lancedb
import typer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

app = typer.Typer()

# Create synthetic dataset with 5,000 rows and some random features
def generate_data(n_samples=300, n_features=10):
    data = np.random.rand(n_samples, n_features)  # Random numerical data
    df = pd.DataFrame(data, columns=[f"feature_{i}" for i in range(n_features)])
    return df


# Transform dataset into vectors (standardize and reduce dimensionality)
def transform_to_vectors(df):
    # Step 1: Standardize the dataset
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)

    # Step 2: Reduce dimensionality (optional, for example using PCA)
    pca = PCA(n_components=8)  # Reduce to 5 principal components
    vectors = pca.fit_transform(scaled_data)

    return vectors


# Ingest vectors into LanceDB
@app.command()
def create_new_vector_db(
    table_name: str = "my-rag-app-3", number_of_documents: int = 1000, uri=".lancedb"
):
    dataset = generate_data()
    embeddings = transform_to_vectors(dataset)

    data = [
        {
            "id": idx,
            "vector": embeddings[idx]
        }
        for idx in range(len(dataset))
    ]

    db = lancedb.connect(uri)
    lance_table = db.create_table(table_name, data=data)
    lance_table.create_index()

    return embeddings

@app.command()
def query_existing_vector_db(
    query: str = "What was ARR last year?",
    table_name: str = "my-rag-app-3",
    top_n: int = 1,
    uri=".lancedb",
):
    query_embedding = query
    db = lancedb.connect(uri)
    tbl = db.open_table(table_name)

    results = tbl.search(query_embedding).limit(top_n).to_list()
    typer.echo("Search result:")
    for result in results:
        typer.echo("RESULT")
        typer.echo(result)

    return results


# Main function to demonstrate the entire process
def main():
    # Step 1,2, 3: Create data, transform to vectors, ingest
    vectors = create_new_vector_db()

    # Step 4: Query LanceDB for similar vectors (nearest neighbors)
    query_idx = 0  # Example: Query the first row of the dataset
    query_vector = vectors[query_idx]
    results = query_existing_vector_db(query=query_vector, top_n=5)

    # Output results
    print(f"Querying vector at index {query_idx}")
    print(f"Similar vectors (indices and distances): {results}")


if __name__ == "__main__":
    main()
