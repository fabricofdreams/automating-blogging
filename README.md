# Blog Automation Crew

This project aims to automate the process of generating blog posts on a given topic using artificial intelligence (AI) agents. The system utilizes various language models and tools to assist in different stages of the blog post creation process.

## Getting Started

To use this project, you'll need to set up a Python environment and install the required dependencies listed in the `pyproject.toml` file by poetry. Additionally, ensure you have access to the necessary APIs and services for the language models and tools used in the project.

### Installation

Clone the repository and install the dependencies using pip:

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
pip install -r requirements.txt
```

### Configuration

Before running the code, make sure to set up your environment variables by creating a `.env` file in the project directory and specifying any necessary credentials or API keys required by the language models and tools.

```plaintext
# .env file
API_KEY=your_api_key
```

## Usage

The core functionality of the project is encapsulated in the `crewai` module, specifically in the `Crew` class, which orchestrates the activities of various agents and tasks. The `Crew` class takes agents, tasks, and a process type as input to execute the desired automation.

## Modules

### Agents

- **BloggingAutomationAgents**: Contains agents responsible for managing different aspects of blog post creation, such as blogging management, web research, title creation, post creation, and translation.

### Tasks

- **BlogPostAutomationTasks**: Defines tasks related to managing the creation of blog posts, including managing blog post creation, web search, title creation, post writing, and post translation.

### Define the blog post topic

```
post_topic = "Video generation with AI."
```

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features you'd like to see implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
