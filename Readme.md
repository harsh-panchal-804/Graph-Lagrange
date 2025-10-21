# Graph-Lagrange

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![SymPy](https://img.shields.io/badge/powered%20by-SymPy-orange.svg)](https://www.sympy.org/)

A sophisticated calculus analysis tool for exploring extrema in both single and multivariable functions.

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [Examples](#examples) • [Contributing](#contributing)

</div>

## 🎯 Overview

Graph-Lagrange is a powerful command-line utility that combines symbolic mathematics with visualization to help you analyze and understand function behavior. Whether you're studying calculus, solving optimization problems, or exploring mathematical relationships, this tool provides a comprehensive suite of analytical capabilities.

![Demo Animation](/Demo_video/demo_gif.gif)

## ✨ Features

### 📊 Single Variable Analysis
- Find critical points where $f'(x) = 0$
- Identify inflection points where $f''(x) = 0$
- Calculate limits as $x \to \pm \infty$
- Interactive parameter adjustment
- Real-time plot updates

### 🔮 Multivariable Analysis
- Locate critical points by solving $\nabla f = 0$
- Classify extrema using the Hessian matrix
- Find constrained extrema with Lagrange multipliers
- Generate 3D surface plots

### 🎨 Visualization Features
- Adaptive plotting ranges
- High-resolution 3D rendering
- Automatic feature detection
- Dynamic axis scaling

## 🚀 Installation

### Prerequisites
```bash
# Python 3.x is required
python --version  # Should be 3.x
```

### Quick Start
```bash
# Clone the repository
git clone https://github.com/harsh-panchal-804/Graph-Lagrange.git

# Navigate to project directory
cd Graph-Lagrange

# Install dependencies
pip install sympy
```

## 📖 Usage

### Launch the Analyzer
```bash
python MaximaMinimaFinal.py
```

### Mode Selection
The tool offers two analysis modes:
1. Single Variable (1D)
2. Multivariable (2D)

## 📚 Examples

### Single Variable Analysis
```python
# Input
f(x) = ax² + bx + c
Parameters: a = 1, b = -2, c = 1

# Output
Critical Points: x = 1
Classification: Minimum
f(1) = 0
```

### Multivariable Analysis
```python
# Input
f(x,y) = x² + y² - 2xy

# Output
Critical Point: (0, 0)
Classification: Saddle Point
Hessian Determinant: -4
```

### Constrained Optimization
```python
# Function
f(x,y) = x² + y²

# Constraint
g(x,y) = x + y - 1 = 0

# Solution
x = 0.5, y = 0.5
λ = 1
```

## 🔧 Advanced Features

### Hessian Analysis
The tool automatically computes and evaluates the Hessian matrix:

$H = \begin{bmatrix} 
\frac{\partial^2 f}{\partial x^2} & \frac{\partial^2 f}{\partial x \partial y} \\
\frac{\partial^2 f}{\partial x \partial y} & \frac{\partial^2 f}{\partial y^2}
\end{bmatrix}$

### Lagrange Multipliers
For constrained optimization problems, we solve:

$\nabla f = \lambda \nabla g$

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [SymPy](https://www.sympy.org/) for symbolic mathematics
- Contributors and users of this project

---
<div align="center">
Made with ❤️ by <a href="https://github.com/harsh-panchal-804">Harsh Panchal</a>
</div>
