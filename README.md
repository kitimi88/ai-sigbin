# AI-SIGBIN

## About

Here are some examples of various ChatGPT models inspired by the official [OpenAI Cookbook](https://github.com/openai/openai-cookbook) repository. 
Based on requests, this repository has two separate folders: [Basic CLI](./prompt%20examples/) for a clean traditional prompt and [Jupyter Notebook](./examples/) for in-depth and Anaconda programming.

This project is written using Python; however, the same principles can be applied to different languages.

---
## What's inside
* **Traditional prompts**
  - [Helpful assistant](./prompt%20examples/helpful.py)
  - [Sarcastic Bot](/prompt%20examples/sarcastic.py)
  - [Filipino Poet](./prompt%20examples/filipino_poet.py)
  - [Translator](./prompt%20examples/transalator.py)

* **Jupyter Notebook**
    - [Custom inputs using chat completions](./examples/custom_gpt_turbo.ipynb)
    
    - [Basic chat completions](./examples/chat_completions.ipynb)

---
## Usage
### Clone Repository

```
git clone https://github.com/kitimi88/ai-sigbin.git
```
---
### Traditional prompt

For [traditional prompts](./prompt%20examples/), you must have at least [Python 3.10](https://www.python.org/downloads/) or higher installed in your machine. Once installed:

1. **Create a virtual environment:**
```
py -m venv .venv
```
2. **Activate your virtual enviroment:**
```
.venv\scripts\activate.ps1 
```
3. **Upgrade PIP**
```
py -m pip install --upgrade pip
```
4. **Install / Upgrade OpenAI libraries. Also outlined in the [requrements.txt](./requirements.txt).**
```
py -m pip install openai
```

```
py -m pip install --upgrade openai
```
---
### Jupyter Notebook / Anaconda

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
- OpenAI libraries must be installed in your enviroment

### Install or upgrade API
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