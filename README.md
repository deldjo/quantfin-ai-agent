# QuantFinAI-Agent

Verifiable AI Coding Agent for Quantitative Finance - Agenthon 2026 T1

## Overview

This agent generates Python code to solve quantitative finance problems and verifies outputs against 13 financial invariants (Put-Call Parity, Delta bounds, Gamma/Vega positivity, etc.).

## Quick Start

```bash
pip install -r requirements.txt
python agent.py --task-dir /path/to/task --out /tmp/output
