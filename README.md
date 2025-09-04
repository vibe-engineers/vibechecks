<p align="center">
  <img width=300 src="https://raw.githubusercontent.com/vibe-engineers/vibechecks/main/assets/vibechecks.png" />
  <h1 align="center">VibeChecks</h1>
</p>

<p align="center">
  <a href="https://github.com/vibe-engineers/vibechecks/actions/workflows/ci-cd-pipeline.yml"> <img src="https://github.com/vibe-engineers/vibechecks/actions/workflows/ci-cd-pipeline.yml/badge.svg" /> </a>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Technologies](#technologies)
* [Team](#team)
* [Contributing](#contributing)
* [Others](#others)

### Introduction
**VibeChecks** is a lightweight python package that allows users to use natural language (LLMs) as part of their code logic. For example, **VibeChecks** can be used to check if/loop statements as well as provide responses for functions that are described but not implemented. It supports OpenAI and Google Gemini client currently and a simple example illustrating how it can be used can be seen below:
```python
from google import genai
from vibechecks import VibeCheck

# initialize client
client = genai.Client(api_key=GEMINI_API_KEY)

# wrap it in VibeCheck
vc = VibeCheck(client, model="gemini-2.0-flash-lite")

# the example below asks user for a dog breed and checks if it is valid
user_input = input("Enter a dog breed:")
if vc(f"{user_input} is a valid dog breed"):
    print(f"{user_input} is a valid dog breed!")
else:
    print(f"{user_input} is not a valid dog breed!")
```

**VibeChecks** is published on [**pypi**](https://pypi.org/project/vibechecks/) and can be easily installed with:
```bash
python3 -m pip install vibechecks
```
Details on the usage of the package and available APIs can be found on the [**wiki page**](https://github.com/vibe-engineers/vibechecks/wiki).

### Features
- **Natural Language Conditions**: Use natural language to check for conditions, making your code more readable and intuitive.
- **Multi-provider Support**: Seamlessly switch between different LLM providers. VibeChecks currently supports OpenAI and Google Gemini.
- **Extensible**: The modular design allows for easy extension to other LLM providers in the future.
- **Custom Exceptions**: Provides custom exceptions for better error handling and debugging.

### Technologies
Technologies used by VibeChecks are as below:
##### Done with:

<p align="center">
  <img height="150" width="150" src="https://logos-download.com/wp-content/uploads/2016/10/Python_logo_icon.png"/>
</p>
<p align="center">
Python
</p>

##### Project Repository
```
https://github.com/vibe-engineers/vibechecks
```

### Team
* [Kong Le-Yi](https://github.com/konglyyy)
* [Tan Jin](https://github.com/tjtanjin)

### Contributing
If you are looking to contribute to the project, you may find the [**Developer Guide**](https://github.com/vibe-engineers/vibechecks/blob/main/docs/DeveloperGuide.md) useful.

In general, the forking workflow is encouraged and you may open a pull request with clear descriptions on the changes and what they are intended to do (enhancement, bug fixes etc). Alternatively, you may simply raise bugs or suggestions by opening an [**issue**](https://github.com/vibe-engineers/vibechecks/issues) or raising it up on [**discord**](https://discord.gg/dBW35GBCPZ).

Note: Templates have been created for pull requests and issues to guide you in the process.

### Others
For any questions regarding the implementation of the project, you may also reach out on [**discord**](https://discord.gg/dBW35GBCPZ).

