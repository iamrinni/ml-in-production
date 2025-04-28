# ml-in-production
ML in Production course home works

### Pandas formats comparison

```
python -m pandas_formats --output-dir /Users/irinaevdokimova/PycharmProjects/ml-in-production/module_2/data
```
Output example:

```
Benchmarking CSV format...
  Save time (seconds): 0.0155
  Load time (seconds): 0.0043
Benchmarking Parquet format...
  Save time (seconds): 0.3891
  Load time (seconds): 0.6293
Benchmarking Feather format...
  Save time (seconds): 0.0472
  Load time (seconds): 0.0016
```

### Inference comparison

```
python -m pandas_inference
```

Output example:
```
Single process inference time: 0.0089 seconds
Multiple processes (n=4) inference time: 2.2019 seconds
Speedup from using 4 processes: 0.00x

```