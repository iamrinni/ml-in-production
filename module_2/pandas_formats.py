import pandas as pd
import numpy as np
import time
import argparse

# Create a synthetic dataset with 5,000 rows
n_rows = 5000
df = pd.DataFrame({
    'id': np.arange(n_rows),
    'value': np.random.rand(n_rows),
    'category': np.random.choice(['A', 'B', 'C', 'D'], size=n_rows)
})


# Function to benchmark saving and loading for various formats
def benchmark_format(format_name, save_func, load_func, *args, **kwargs):
    print(f"Benchmarking {format_name} format...")

    # Benchmark saving
    start_time = time.time()
    save_func(*args, **kwargs)
    save_time = time.time() - start_time
    print(f"  Save time (seconds): {save_time:.4f}")

    # Benchmark loading
    start_time = time.time()
    load_func(*args, **kwargs)
    load_time = time.time() - start_time
    print(f"  Load time (seconds): {load_time:.4f}")


# Benchmark CSV
def save_csv(filename):
    df.to_csv(filename, index=False)


def load_csv(filename):
    return pd.read_csv(filename)


# Benchmark Parquet
def save_parquet(filename):
    df.to_parquet(filename, index=False)


def load_parquet(filename):
    return pd.read_parquet(filename)


# Benchmark Feather
def save_feather(filename):
    df.to_feather(filename)


def load_feather(filename):
    return pd.read_feather(filename)


# Master function for benchmarking
def run_benchmarks(output_dir):
    # Files for saving
    csv_file = f'{output_dir}/benchmark.csv'
    parquet_file = f'{output_dir}/benchmark.parquet'
    feather_file = f'{output_dir}/benchmark.feather'

    # Run benchmarks
    benchmark_format('CSV', save_csv, load_csv, csv_file)
    benchmark_format('Parquet', save_parquet, load_parquet, parquet_file)
    benchmark_format('Feather', save_feather, load_feather, feather_file)


# Main function to parse arguments
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Benchmark Pandas formats (CSV, Parquet, Feather)")
    parser.add_argument('--output-dir', type=str, required=True, help="Directory where files will be saved")
    args = parser.parse_args()

    # Run benchmarks with the provided output directory
    run_benchmarks(args.output_dir)


if __name__ == "__main__":
    main()
