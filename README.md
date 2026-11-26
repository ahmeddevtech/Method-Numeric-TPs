# Numerical Methods Lab Work (Method-Numeric-TPs)

This repository contains Python implementations of fundamental linear algebra operations and direct numerical methods for solving systems of linear equations ($Ax = b$). Each lab session (**TP** - _Travaux Pratiques_) builds upon the previous one to create a modular toolkit for matrix manipulation and linear system resolution.

## 📁 Repository Structure

- **`Functions.py`** — _(TP 1)_: Foundational matrix operations, generation, and structural tests.
- **`TP2.py`**: Solvers for triangular linear systems using forward and backward substitution (iterative and recursive).
- **`TP3.py`**: Gaussian Elimination algorithms with non-zero, partial, and total pivoting strategies.
- **`TP4.py`**: LU Decomposition (Doolittle's method) to factorize a matrix $A = L \cdot U$ and solve $Ax = b$.
- **`execution_*.txt`**: Sample console execution logs demonstrating step-by-step iterations and outputs for TP3 and TP4.

## 📚 Overview of TPs

- **TP1 — Matrix Basics (`Functions.py`):** Handles matrix creation (square, identity, diagonal, null), arithmetic (addition, multiplication, transpose), and structural checks (upper/lower triangular, diagonal, symmetric) via an interactive CLI.
- **TP2 — Triangular Solvers (`TP2.py`):** Solves triangular systems ($Lx = b$ and $Ux = b$) using both iterative and recursive implementations of forward substitution (_descente_) and backward substitution (_remontée_).
- **TP3 — Gaussian Elimination (`TP3.py`):** Reduces general linear systems to upper triangular form before solving via backward substitution, supporting standard non-zero pivoting (`triangularisation`), partial pivoting, and total pivoting.
- **TP4 — LU Decomposition (`TP4.py`):** Factorizes $A = L \cdot U$ step-by-step and solves $Ax = b$ in two phases: forward substitution for $Ly = b$ followed by backward substitution for $Ux = y$.

## 🚀 Getting Started

### Prerequisites

- **Python 3.x** (No external dependencies required; uses only the Python standard library).

### Installation & Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/ahmeddevtech/Method-Numeric-TPs.git
   cd Method-Numeric-TPs
   ```

2. Run any of the interactive CLI menus:
   - **Run TP1, TP2, TP3 or TP4:** _(Invoke `menu()` directly via Python)_
     ```bash
     python -c "import TP3; TP3.menu()"
     ```

## 📝 Example Execution Logs

You can inspect the included `.txt` files to see sample inputs and step-by-step console outputs without running the code:

- `execution_partie1.txt` — Standard Gaussian elimination on a $4 \times 4$ system.
- `execution_partie2.txt` — Gaussian elimination with partial pivoting on a $3 \times 3$ system.
- `execution_partie3.txt` — Gaussian elimination with total pivoting on a $3 \times 3$ system.
- `execution_pivotsV2.txt` — Execution of refactored pivoting functions (`v2`).
- `execution_TP4.txt` — Full $LU$ decomposition, forward descent ($Ly = b$), and backward substitution ($Ux = y$) trace.
