> This workshop is for LLM generating MKT content

## Getting Started
1. To start the workshop, follow these steps:
```bash
# install miniconda
    ## mac
    brew install miniconda
    ## other systems
    [miniconda installer](https://docs.conda.io/en/latest/miniconda.html)
# Create a new conda environment with Python 3.10
conda create -n py310 python=3.10

# Activate the conda environment
conda activate py310

# Clone the repository to your local machine
git clone  ...

# Navigate to the project directory
cd smart-marketing-llm-workshop

# Install dependencies from requirements.txt
pip install -r requirements.txt
```

2. After installing, you can launch the application simply by running:

```bash
streamlit run app.py
```