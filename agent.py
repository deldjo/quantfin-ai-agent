#!/usr/bin/env python3
import argparse
import sys
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type):
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if option_type == 'call':
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * np.sqrt(T) * norm.pdf(d1)
        theta = -S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) - r * K * np.exp(-r * T) * norm.cdf(d2)
    else:
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = -norm.cdf(-d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        vega = S * np.sqrt(T) * norm.pdf(d1)
        theta = -S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) + r * K * np.exp(-r * T) * norm.cdf(-d2)
    price = max(price, 0.0)
    delta = np.clip(delta, -1.0, 1.0)
    gamma = max(gamma, 0.0)
    vega = max(vega, 0.0)
    return price, delta, gamma, vega, theta

def solve_with_bs(df):
    results = []
    for _, row in df.iterrows():
        price, delta, gamma, vega, theta = black_scholes(
            S=row['S'], K=row['K'], T=row['T'],
            r=row['r'], sigma=row['sigma'], option_type=row['option_type']
        )
        results.append({
            'option_id': row['option_id'],
            'price': price,
            'delta': delta,
            'gamma': gamma,
            'vega': vega,
            'theta': theta,
        })
    return pd.DataFrame(results)

def solve(task_dir, output_dir):
    task_path = Path(task_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    input_file = task_path / "environment" / "data" / "options.parquet"
    if not input_file.exists():
        print(f"[ERROR] Input not found: {input_file}", file=sys.stderr)
        return 1
    output_file = output_path / "results.parquet"
    df = pd.read_parquet(input_file)
    result_df = solve_with_bs(df)
    result_df.to_parquet(output_file)
    print(f"[INFO] Results written to {output_file}")
    return 0

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task-dir", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    sys.exit(solve(args.task_dir, args.out))

if __name__ == "__main__":
    main()
