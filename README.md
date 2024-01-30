# Blockchain Implementation with Flask

This project demonstrates a basic blockchain implementation using Flask, where each block is represented as a class. The application provides three RESTful API endpoints to mine new blocks, retrieve the entire blockchain, and check the validity of the blockchain.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
  - [1. Mine a New Block](#1-mine-a-new-block)
  - [2. Get the Full Blockchain](#2-get-the-full-blockchain)
  - [3. Check Blockchain Validity](#3-check-blockchain-validity)
- [Example Usage](#example-usage)
- [Responses](#responses)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x
- Flask (install using `pip install Flask==0.12.2`)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/TUR14CUS/blockchain-flask.git
   cd blockchain-flask
   ```

2. Install Flask:

   ```bash
   pip install Flask==0.12.2
   ```

### Running the Application

```bash
python main.py
```

The application will be running at `http://localhost:5000/`.

## API Endpoints

### 1. Mine a New Block

- **Endpoint:** `/mine_block`
- **Method:** GET
- **Description:** Mine a new block and add it to the blockchain.

### 2. Get the Full Blockchain

- **Endpoint:** `/get_chain`
- **Method:** GET
- **Description:** Retrieve the entire blockchain.

### 3. Check Blockchain Validity

- **Endpoint:** `/is_valid`
- **Method:** GET
- **Description:** Check if the current blockchain is valid.

## Example Usage

1. **Mine a New Block:**
   - Endpoint: `http://localhost:5000/mine_block`
   - Method: GET

2. **Get the Full Blockchain:**
   - Endpoint: `http://localhost:5000/get_chain`
   - Method: GET

3. **Check Blockchain Validity:**
   - Endpoint: `http://localhost:5000/is_valid`
   - Method: GET

## Responses

- **Success (200 OK):**
  ```json
  {
    "message": "All good. The Blockchain is valid."
  }
  ```

- **Success (201 Created):**
  ```json
  {
    "message": "Congratulations, you just mined a block!",
    "index": 2,
    "timestamp": "2024-01-30 12:00:00",
    "proof": 12345,
    "previous_hash": "previous_hash_value"
  }
  ```

- **Error (400 Bad Request):**
  ```json
  {
    "message": "Houston, we have a problem. The Blockchain is not valid."
  }
  ```

## Project Structure

- **main.py:** Entry point of the application.
- **blockchain.py:** Contains the blockchain logic and Flask-RESTful resource classes.
- **README.md:** Project documentation.

## Contributing

Feel free to contribute to this blockchain implementation by opening issues or creating pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).