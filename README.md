# Scalable UDP Server for Low-Latency Humidity Data Transmission

An advanced, open‐source project that implements a UDP server to serve live humidity and temperature data from a connected sensor

## Table of Contents

- [Features](#features)
- [Repository Structure](#repository-structure)
- [Architecture Overview](#architecture-overview)
- [Setup and Installation](#setup-and-installation)
  - [Hardware Setup](#hardware-setup)
  - [Software Setup](#software-setup)
  - [Docker Deployment](#docker-deployment)
  - [CI/CD Workflows](#cicd-workflows)
- [Usage](#usage)
- [Testing](#testing)
- [Contribution Guidelines](#contribution-guidelines)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Real-Time Sensor Data Acquisition:** Reads live temperature and humidity data from a DHT sensor.  
- **Simulation Mode:** Option to simulate sensor readings for development and testing purposes.  
- **Low-Latency UDP Server:** Serves sensor data over UDP in near real-time with an emphasis on fast response times.  
- **Advanced Logging and Error Handling:** Comprehensive logs (both to console and file) and robust error/retry mechanisms.  
- **Modular Architecture:** Additional utility modules, services for analytics, notifications, caching, and metrics collection.  
- **Containerized Deployment:** Fully dockerized solution with a Dockerfile and docker-compose for easy deployment and scalability.  
- **CI/CD Integration:** Automated testing, linting, and deployment pipelines using GitHub Actions.  
- **Extensible Codebase:** Structured to allow for easy expansion and integration with additional services and features.

---

## Repository Structure

```
Scalable-UDP-Server-Humidity/
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
├── Dockerfile                    # Docker build configuration
├── docker-compose.yml            # Docker Compose deployment file
├── README.md                     # Project overview and instructions
├── requirements.txt              # Python dependencies
├── config.py                     # Centralized configuration settings
├── docs/
│   ├── architecture.md           # System architecture description
│   ├── design_decisions.md       # Rationale behind design decisions
│   └── changelog.md              # Project change log
├── scripts/
│   ├── setup.sh                  # Environment setup script
│   ├── run_tests.sh              # Script to execute unit tests
│   └── deploy.sh                 # Deployment automation script
├── ci/
│   ├── .github/
│   │   └── workflows/
│   │       ├── python-app.yml    # CI workflow for testing and linting
│   │       └── deploy.yml        # Deployment workflow
│   └── lint.yml                  # Linting configuration
├── src/
│   ├── sensor_reader.py          # Sensor module for reading (or simulating) data
│   ├── udp_server.py             # UDP server implementation with multithreading
│   ├── utils/                    # Utility modules for logging, formatting, etc.
│   │   ├── logger.py             # Custom logger configuration
│   │   ├── decorators.py         # Function decorators (e.g., retry, timeit)
│   │   ├── exceptions.py         # Custom exception definitions
│   │   └── data_formatter.py     # Helper functions to format sensor data
│   └── services/                 # Supplementary services for analytics and metrics
│       ├── analytics.py          # Data analytics service
│       ├── notification.py       # Notification service (stub)
│       ├── caching.py            # In-memory caching mechanisms
│       └── metrics.py            # Metrics collection and reporting
├── tests/                        # Unit and integration tests
│   ├── test_sensor_reader.py
│   ├── test_udp_server.py
│   └── test_utils.py
└── examples/                     # Example client and sample data files
    ├── sample_client.py          # Sample UDP client script
    └── sample_data.json          # Example JSON data output
```

---

## Architecture Overview

The repository is organized into several layers to ensure clear separation of concerns:

- **Sensor Module:**  
  Handles reading data from a physical sensor using the Adafruit_DHT library or simulates readings if a sensor is unavailable.

- **UDP Server:**  
  A multithreaded server that listens for UDP client requests and responds with JSON-formatted sensor data.

- **Utility Modules:**  
  Custom logging configurations, decorators, exception handling, and data formatting functions that support maintainability and debugging.

- **Service Layer:**  
  Provides additional functionality (analytics, notifications, caching, metrics) and acts as a foundation for further feature integrations.

- **CI/CD and Containerization:**  
  Uses GitHub Actions for automated testing, linting, and deployments. Containerization via Docker ensures consistency across various deployment environments.

---

## Setup and Installation

### Hardware Setup

- **Sensor Connection:**  
  Connect your DHT sensor (e.g., DHT22) to your hardware (such as a Raspberry Pi) using the GPIO pin defined in `config.py`.

### Software Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/Scalable-UDP-Server-Humidity.git
   cd Scalable-UDP-Server-Humidity
   ```

2. **Create and Activate a Virtual Environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Variables:**  
   Create or update the `.env` file with appropriate values (an example file is included in the repository).

### Docker Deployment

1. **Build and Run with Docker Compose:**

   ```bash
   docker-compose up --build
   ```

   This command builds the container image, starts the UDP server, and maps the UDP port as configured in `.env`.

### CI/CD Workflows

- **Testing and Linting:**  
  The repository includes GitHub Actions workflows located in `ci/.github/workflows/python-app.yml` and `ci/lint.yml` which run tests and lint checks on every push and pull request.

- **Automated Deployment:**  
  See `ci/.github/workflows/deploy.yml` for details on deployment pipelines.

---

## Usage

### Running the UDP Server Locally

To run the server directly on your local machine:

```bash
python src/udp_server.py
```

The server listens on the IP and UDP port specified in `config.py` and responds with live sensor data.

### Interacting with the Server

Refer to the example client located in `examples/sample_client.py` to test the server:

```bash
python examples/sample_client.py
```

The client sends a UDP packet and prints the sensor data received as a JSON response.

---

## Testing

The project includes comprehensive unit and integration tests:

- **Run All Tests:**

  ```bash
  bash scripts/run_tests.sh
  ```

- **Test Coverage:**  
  The tests are located in the `tests/` directory and cover sensor readings, UDP server responses, and utility functions.

---

## Contribution Guidelines

Contributions are welcome and encouraged! To contribute:

1. **Fork the Repository:**  
   Create a personal fork of the project on GitHub.

2. **Create a Feature Branch:**  
   Use a descriptive branch name (e.g., `feature/add-enhanced-logging`).

3. **Implement Your Changes:**  
   Follow the established coding style and include tests for your changes.

4. **Submit a Pull Request:**  
   Provide a clear description of your changes and reference any related issues.

For detailed contribution guidelines, please refer to the `CONTRIBUTING.md` file or contact the maintainers.

---

## License

This project is distributed under the [MIT License](LICENSE). Please see the LICENSE file for more details.

---

## Contact

For any inquiries, bug reports, or feature requests, please open an issue on [GitHub Issues](https://github.com/AkhilRai28/Scalable-UDP-Server-Humidity/issues).

---

Enjoy using and contributing to this open-source project! Your support helps us improve and expand the capabilities of this IoT solution.
