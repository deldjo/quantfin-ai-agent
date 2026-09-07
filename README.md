# QuantFinAI-Agent

Verifiable AI Coding Agent for Quantitative Finance - Agenthon 2026 T1

## Overview

This agent generates Python code to solve quantitative finance problems and verifies outputs against 13 financial invariants (Put-Call Parity, Delta bounds, Gamma/Vega positivity, etc.).

## Quick Start

```bash
pip install -r requirements.txt
python agent.py --task-dir /path/to/task --out /tmp/output
Docker Build & Run
bash

docker build -t quantfin-agent .
docker run --rm quantfin-agent --task-dir /input --out /output

Results

Our agent passes all 13 financial invariance tests on the Agenthon 2026 T1 exemplar task.
Metric	Result
Test Pass Rate	13/13 (100%)
Self-Correction Improvement	76.9% → 100%
Repository Structure
text

├── agent.py              # Main agent implementation
├── Dockerfile            # Container build file
├── requirements.txt      # Python dependencies
└── README.md             # This file

License

MIT License

Team GAOKUO · Agenthon 2026 · NeurIPS Competition Track
text


### 如何更新到 GitHub

1. 在仓库页面点击 `README.md` 文件
2. 点击右上角 **✏️ 铅笔图标** 进入编辑模式
3. **全选删除**原有内容，**粘贴**上面的新内容
4. 滚动到底部，点击 **"Commit changes"** 保存

这样 README 就更新好了。如果还有其他问题，随时告诉我。🚀
