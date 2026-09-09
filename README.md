# genpark-cholesky-decomposition-spd-solver-skill

[![GitHub stars](https://img.shields.io/github/stars/alphaparkinc/genpark-cholesky-decomposition-spd-solver-skill?style=social)](https://github.com/alphaparkinc/genpark-cholesky-decomposition-spd-solver-skill/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-0%20external-brightgreen.svg)](#)
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20Compatible-orange.svg)](#)

> Autonomous Agent Cholesky Decomposition LL^T Solver for Symmetric Positive-Definite Covariance Matrices

Part of the **GenPark Autonomous Numerical Linear Algebra & Matrix Decompositions Architecture**.

## Architecture Overview

```mermaid
graph TD
    A[Symmetric Positive-Definite Covariance Matrix A] --> B[Iterate Row i from 0 to N-1]
    B --> C[Diagonal Elements L_ii = sqrt A_ii - sum L_ik^2]
    C --> D[Off-Diagonal Elements L_ij = 1/L_jj * A_ij - sum L_ik L_jk]
    D --> E[Construct Lower Triangular Matrix L]
    E --> F[Exact Factorization A = L * L^T in Half FLOPs of LU]
    F --> G[Multivariate Gaussian Random Sampling & Kalman Noise Transforms]
```

## Features

- **Pure Python Standard Library**: Zero external dependencies (no NumPy or SciPy required).
- **Production-Grade Design**: Type annotations, partial pivoting, Gram-Schmidt stabilization.
- **MCP Server Ready**: Built-in stdio Model Context Protocol (MCP) server for Claude / Cursor / Agent tool calling.
- **Benchmark Validated**: 100% verified test coverage in isolated sandbox environments.

## Quickstart

```bash
git clone https://github.com/alphaparkinc/genpark-cholesky-decomposition-spd-solver-skill.git
cd genpark-cholesky-decomposition-spd-solver-skill
python example_usage.py
```

## Model Context Protocol (MCP) Usage

```bash
python mcp_server.py
```

## License

MIT License. Designed for autonomous agentic workflows.
