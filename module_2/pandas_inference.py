import time
import numpy as np
import pandas as pd
import multiprocessing
from sklearn.linear_model import LinearRegression
from sklearn.datasets import make_regression


# Create synthetic regression data
def generate_data(n_samples=100000, n_features=100):
    X, y = make_regression(n_samples=n_samples, n_features=n_features, noise=0.1)
    return X, y


# Inference function (simulating model prediction)
def inference(model, X):
    return model.predict(X)


# Function to perform inference using single process
def benchmark_single_process(model, X):
    start_time = time.time()
    # Run inference for all data in a single process
    predictions = inference(model, X)
    elapsed_time = time.time() - start_time
    return elapsed_time


# Function to perform inference using multiple processes
def benchmark_multiple_processes(model, X, n_processes):
    # Split data for parallel processing
    n_samples = X.shape[0]
    chunk_size = n_samples // n_processes
    chunks = [X[i:i + chunk_size] for i in range(0, n_samples, chunk_size)]

    start_time = time.time()

    # Create a pool of workers and perform inference in parallel
    with multiprocessing.Pool(processes=n_processes) as pool:
        results = pool.starmap(inference, [(model, chunk) for chunk in chunks])

    # Combine results (predictions) from all processes
    predictions = np.concatenate(results, axis=0)
    elapsed_time = time.time() - start_time
    return elapsed_time


# Main function to benchmark and report results
def main():
    # Generate synthetic data
    X, y = generate_data()

    # Train a simple model (Linear Regression)
    model = LinearRegression()
    model.fit(X, y)

    # Benchmark single process inference
    single_process_time = benchmark_single_process(model, X)
    print(f"Single process inference time: {single_process_time:.4f} seconds")

    # Benchmark multiple processes (e.g., 4 processes)
    n_processes = 4
    multi_process_time = benchmark_multiple_processes(model, X, n_processes)
    print(f"Multiple processes (n={n_processes}) inference time: {multi_process_time:.4f} seconds")

    # Report difference
    speedup = single_process_time / multi_process_time
    print(f"Speedup from using {n_processes} processes: {speedup:.2f}x")


if __name__ == "__main__":
    main()
