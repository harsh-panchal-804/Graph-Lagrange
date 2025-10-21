# Graph-Lagrange: Comprehensive Calculus Extrema Analyzer

A powerful, command-line utility implemented in Python using the SymPy library for performing in-depth calculus analysis, focusing on finding and classifying local extrema for single and multivariable functions.

## Overview

This tool serves as an interactive calculus companion, enabling users to input complex functions and parameters, receive detailed analysis (critical points, Hessian matrix, inflection points, limits), and visualize the results with dynamic plotting.

## Demo Video
Watch our demo video to see Graph-Lagrange in action and learn how to use its various features:

![Demo GIF](/Demo_video/demo_gif.gif)

## Features

### Generalized Function Input
- Accepts functions defined with standard mathematical notation (e.g., `sin(x) + y**2`, `a*x**3 + c`)

### Multivariable (2D) Analysis
- **Unconstrained Extrema**: Automatically solves for critical points (\nabla f = 0$$)
- **Hessian Matrix Test**: Calculates and displays the Hessian matrix symbolically for classification (Local Maxima, Minima, Saddle Points)
- **Lagrange Multipliers**: Supports finding constrained extrema subject to an equation $$g(x, y) = 0$$

### Single Variable (1D) Analysis
- **Interactive Parameters**: Features a loop simulating interactive sliders, allowing users to dynamically update function parameters and instantly see the corresponding analysis and plot changes
- **Inflection Points & Concavity**: Reports points of inflection by solving $$f''(x) = 0$$
- **Asymptotic Behavior**: Calculates limits as $$x \to \pm \infty$$

### Dynamic Visualization
- Generates high-resolution 2D and 3D plots with dynamically calculated ranges to ensure all relevant features (extrema, inflection points) are visible
- Professional Output: Outputs results in clean, formatted console tables and uses LaTeX strings for superior display of symbolic functions

## Installation

### Prerequisites
- Python 3.x
- sympy library (installing this typically handles plotting dependencies like Matplotlib)

### Clone the Repository
```bash
git clone https://github.com/harsh-panchal-804/Graph-Lagrange.git
cd Graph-Lagrange
```


### Install Dependencies
```bash
pip install sympy
```

## Build and Run

Start the analyzer by executing the main script:
```bash
python MaximaMinimaFinal.py
```

## Usage Example

The script will first ask if you are analyzing a 2D or 1D function:

### 1. 2D (Multivariable) Mode:
```
Is your function 2D (1/0): 1
Enter the 2D function f(x, y) (e.g., x**4 + y**4 - 4*x*y + 1): x**2 + y**2
...
(Analysis output)
...
Do you want to compute constrained extrema...? (y/n): n
Do you want to plot the function?(1/0): 1
```

### 2. 1D (Interactive) Mode:
```
Is your function 2D (1/0): 0
Enter the 1D function f(x) with parameters (e.g., a*x**3 + b*x + c): a*x**2 + b*x
Enter parameter symbols separated by commas (e.g., a, b, c): a, b

# INTERACTIVE PARAMETER UPDATE
  Enter value for parameter 'a': 1
  Enter value for parameter 'b': -2
...
(Analysis and plot updates)
...
Change parameters and re-analyze? (y/n): y
```

## Project Structure
- `MaximaMinimaFinal.py` – The complete, self-contained Python script containing all analysis and plotting logic
- `README.md` – This documentation file

## License
This project is open-source. MIT License.

## Contributing
Pull requests and suggestions are welcome! Please open an issue to discuss enhancements, especially around solving complex systems of equations or improving plotting integration.
