## About The Project

This repository is my "hands-on" knowledge base for simulation modeling. As I learn new techniques and explore different libraries, I will document my progress and share my findings through practical examples and Jupyter notebooks. The goal is to build a collection of simulations that I can reference in the future, but might also help someone else.


---

## Simulation Notebooks

Explore the simulations through the Jupyter notebooks linked below. Each notebook provides a step-by-step walkthrough of a specific model, complete with explanations, code, and visualizations.

### Quick Links

* **Economy Simulations**: [notebooks/economy](./notebooks/economy)
    * `e01_boltzmann_gibbs.ipynb` - Primitive Boltzmann-Gibbs model
* **Finance Simulations**: [notebooks/finance](./notebooks/finance)
    * `f01_behavioral_zoo.ipynb` - Psychological state of traders.



## Repository Structure

The repository is organized to separate exploratory analysis from reusable, core logic.

* `notebooks/`: Contains all Jupyter notebooks. They are organized by domain (e.g., `economy`, `finance`).
* `src/nvx_sim/`: Contains the core Python source code. This includes custom agent definitions, model classes, and data handlers that can be imported into notebooks or other scripts.



## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.12+
* [uv](https://github.com/astral-sh/uv) (a fast Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/jacobbridges/nvx-simulations.git
    cd nvx-simulations
    ```

2.  **Create and activate a virtual environment using `uv`:**
    ```sh
    # Create the virtual environment
    uv venv

    # Activate the environment (Linux/macOS)
    source .venv/bin/activate

    # Activate the environment (Windows)
    .venv\Scripts\activate
    ```

3.  **Install packages from the lockfile:**
    ```sh
    uv sync
    ```

4.  **Launch Jupyter Lab to explore the notebooks:**
    ```sh
    jupyter lab
    ```



## Technology Stack

This project primarily utilizes the following technologies and libraries:

* **Core**: Python, Jupyter Lab
* **Simulation**: Mesa, NumPy, SciPy
* **Data Handling**: Pandas
* **Visualization**: Matplotlib, Seaborn
* **Environment Management**: uv