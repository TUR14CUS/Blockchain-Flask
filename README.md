# Blockchain Implementation with Flask

This repository contains a simple blockchain implementation using Flask, where each block is represented as a class. This blockchain allows mining new blocks, retrieving the entire chain, and checking the validity of the blockchain.

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
python your_script_name.py
```

Replace `your_script_name.py` with the name of the script where your Flask application is defined.

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

## Contributing

Feel free to contribute to this blockchain implementation by opening issues or creating pull requests. Your feedback and suggestions are highly appreciated.

## License

This project is licensed under the [MIT License](LICENSE).