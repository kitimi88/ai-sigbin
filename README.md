# AI-SIGBIN

## About
This project demonstrates how pre-programmed chatbot behaviors can be showcased by utilizing the [GPT3.5 Turbo model](https://platform.openai.com/docs/models/gpt-3-5) and [Chat Completions](https://platform.openai.com/docs/guides/chat), as described in the official [OpenAI Cookbook](https://github.com/openai/openai-cookbook).

Furthermore, this project is designed to run seamlessly using Python or Anaconda, with consideration given to VS Code's [Python Interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py).

While this project is coded in Python, the underlying principles can be applied to other programming languages as well.

---
## What's inside


- [Helpful assistant](./examples_py/helpful.py) - *A friendly and helpful assistant.*

- [Sarcastic Bot](./examples_py/sarcastic.py) - *A sarcastic assistant that reluctantly answers questions with sarcastic responses.*

- [Noypi](./examples_py/noypi.py) - *A Friendly assistant from the Philippines that answers question in Filipino.*

- [Translator](./examples_py/translator.py) - *A friendly and helpful translator.*

These four packages have distinct functions and behaviors that can be executed using basic Python/CLI or Anaconda with Jupyter Notebook. See [examples_py](./examples_py/) and [examples_ipynb](./examples_ipynb/).


---
## Usage
### **Requirements**
The following must be installed in your machine:

- [Python 3.10.8](https://www.python.org/downloads/) or later

- [Git](https://git-scm.com/)

- [Anaconda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) (Optional)

### **Clone**
You may clone the entire repository by running the following command:

```
git clone https://github.com/kitimi88/ai-sigbin.git
```
---
### **Basic Installation**


1. Setup virtual environment and activate virtual environment.
```
py -m venv .venv
```
```
.venv\scripts\activate.ps1 
```
2. Upgrade PIP
```
py -m pip install --upgrade pip
```
3. Install dependencies
```
py -m pip install --upgrade -r requirements.txt
```

### **Jupyter Notebook / Anaconda**

Anaconda must be installed in your local machine. See [documentation](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) for initial setup. Once installed you may also follow some tips bellow:


- Confirm installation, run anaconda cmd prompt with the following command:
```
conda info
```

- Create environment with Python version. Replace ENV with your desired name.
```
conda create -n ENVNAME python=3.10
```
- Update all packages
```
conda update --all
```


### Install or upgrade OpenAI libraries
```
pip install openai
```

```
pip install --upgrade openai
```

---
## Contribution

### *Pending contribution guide.*
---
## License
This project is licensed under the [MIT License](./LICENSE).
