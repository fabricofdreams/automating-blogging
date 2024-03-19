# Blog Automation Crew

## Overview

The Blog Post Automation App streamlines the process of generating and managing blog content by automating the retrieval and organization of web search results and titles. It supports content in both English and Spanish, providing a user-friendly interface to input topics, view search results, and read content drafts directly within the app.

## Features

- **Automated Searches**: Based on the input topic, the app performs web searches, collecting relevant titles and content.

- **Content Preview**: Users can preview the search results and read content drafts in English and Spanish.

- **Data Organization**: Search results and drafts are organized into CSV and Markdown files, respectively, for easy access and further processing.

- **Data Organization**: Search results and drafts are organized into CSV and Markdown files, respectively, for easy access and further processing.

- **Downloadable Results**: The app provides functionality to download the search results and drafts directly from the interface.

## Getting Started

To use this project, you'll need to set up a Python environment and install the required dependencies listed in the `pyproject.toml` file by poetry. Additionally, ensure you have access to the necessary APIs and services for the language models and tools used in the project.

### Installation

Clone the repository and install the dependencies using pip:

```bash
git clone https://github.com/your_username/your_project.git
cd your_project
poetry install
poetry shell
```

### Configuration

Before running the code, make sure to set up your environment variables by creating a `.env` file in the project directory and specifying any necessary credentials or API keys required by the language models and tools.

```plaintext
# .env file
API_KEY=your_api_key
```

## Run the Application

Start the app by running:

```
   streamlit run app.py
```

## Modules

The core functionality of the project is encapsulated in the `crewai` module, specifically in the `Crew` class, which orchestrates the activities of various agents and tasks. The `Crew` class takes agents, tasks, and a process type as input to execute the desired automation.

### Agents

- **BloggingAutomationAgents**: Contains agents responsible for managing different aspects of blog post creation, such as blogging management, web research, title creation, post creation, and translation.

### Tasks

- **BlogPostAutomationTasks**: Defines tasks related to managing the creation of blog posts, including managing blog post creation, web search, title creation, post writing, and post translation.

## Usage

### Start the App

Open the app in your web browser

### Define the blog post topic

```
post_topic = "Video generation with AI."
```

## View Results

Use the chat input to enter a topci your're interested in.

## Download Files and Copy Paste

Use the download buttons to save the tables to your local machine and copy and paste the drafts.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features you'd like to see implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Fernando Robledo - @frobledo - fernando.robledoruiz@gmail.com

Project Link: [https://github.com/yourusername/blog-post-automation-app](https://github.com/yourusername/blog-post-automation-app)
