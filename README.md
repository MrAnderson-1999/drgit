# drgit
## Documentation automation for everyone

Welcome to the drgit repository! This project aims to provide automated documentation generation for your codebase. In this README, we'll explain the purpose of the key files within this repository, namely `gpt.py` and `template.json`, and how they contribute to the project's functionality.

### Documentation Comments Generator

The `gpt.py` file serves as the core of the Documentation Comments Generator. It leverages OpenAI's GPT-3 model to generate informative comments for your code. Here's a breakdown of its main components:

Main keywords: GPT-3, Documentation Generator, code comments, gpt.py
Main topic name: Automated Code Documentation Generation

1. `api_key`: This variable stores your OpenAI API key, which is required for making requests to the GPT-3 model.

2. `get_text()`: This function reads the content of the `template.json` file, which is crucial for providing context to the GPT-3 model. It reads the file and returns its content as text.

3. `send_req()`: This function sends a request to the GPT-3 model, using the content from `template.json` as a prompt. It specifies parameters like the model to use and the maximum number of tokens for the response. The response from the model is then returned.

### `template.json`

The `template.json` file is essential for providing context to the GPT-3 model. It contains the structure and context for generating code comments. Here's what you need to know:

Main keywords: template.json, context, code comments, GPT-3
Main topic name: Contextual Code Comment Generation

- `"main request"`: This key specifies the primary purpose of the code comments generated. It helps the GPT-3 model understand the desired format and content.

- `"file"`: This section includes information about the file to be commented on, such as its internal path, the format for explained comments, and reformatting rules. The `"file_content"` field is where the actual code to be documented should be placed.

- `"context"`: This section allows you to provide additional context or a project description to guide the comment generation process.

### Features

- Automated generation of code comments for improved code documentation.
- Integration with the powerful GPT-3 model for context-aware comments.

### Requirements

- Python 3.x
- OpenAI API Key

### Installation

1. Clone this repository to your local machine.

```
git clone https://github.com/yourusername/drgit.git
```
Set up your OpenAI API Key as an environment variable.
```
export OPENAI_API_KEY=your-api-key
```
Install the required dependencies.
```
pip install requests
```
 ### Usage
To use the Documentation Comments Generator, follow these steps:

Ensure that you have set up your OpenAI API Key as an environment variable.

Place the code you want to generate comments for in the template.json file under "file_content".

Run the gpt.py script to generate comments.

### Example

The following is an example of the output of the script:
```
python gpt.py
```

### License

This project is licensed under the MIT License - see the LICENSE file for details.

### Contributing

We welcome contributions! If you'd like to contribute to this project, please follow our contribution guidelines.

Thank you for using drgit! We hope this README helps you understand how to utilize the gpt.py and template.json files for automated code documentation generation.
