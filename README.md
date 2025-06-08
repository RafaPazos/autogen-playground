# autogen Python Playground

## Overview

**autogen** is a Python-based playground for experimenting with Microsoft's agentic platform, which enables the creation, orchestration, and management of autonomous AI agents. The platform provides tools and frameworks for building agents that can reason, plan, and collaborate to accomplish complex tasks. This repository offers a hands-on environment to prototype, test, and extend agentic workflows using Python, making it easier to explore advanced AI capabilities and integrate them into real-world applications.

Those exercises are based on the [autogen documentation](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/installation.html)

## Installation

To get started with this project, follow these steps:

1. create an environment:

```
// Create a virtual environment named 'agentic'
python -m venv .agentic

// On Windows, activate the environment
.agentic\Scripts\activate

// On macOS/Linux, activate the environment
source .agentic/bin/activate
```

2. Install the required dependencies:

```
   pip install -r requirements.txt
```

### Telemetry

Telemetry is an important aspect of monitoring and improving the performance of AI agents. This project includes built-in support for collecting and analyzing telemetry data to gain insights into agent behavior and performance. 

We use the open telemetry library to instrument the code and capture relevant metrics, traces, and logs. This allows us to track the execution of agents, identify bottlenecks, and optimize their performance over time.

here you can read how to install the open telemetry collector [docu](https://opentelemetry.io/docs/collector/installation/)

and here how to configure your open telemetry [provider](https://microsoft.github.io/autogen/stable/user-guide/core-user-guide/framework/telemetry.html)

## Usage

To run the application, execute the following command:

Exercise number 1:
```
python src/agent_chat_quick/main.py
```

Exercise number 2:
```
python src/agent_chat_tutorial/main.py
```

Exercise number 3:
```
python src/agent_team/main.py
```

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.