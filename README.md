# Redis-like Database Implementation

This project implements a Redis-like database with basic functionalities such as setting, getting, and deleting key-value pairs, as well as managing data structures like lists and sets.

## Project Structure

```
redis_like_db/
├── src/
│   ├── __init__.py
│   ├── server.py
│   ├── protocol.py
│   ├── database.py
│   ├── command_handler.py
│   └── types/
│       └── __init__.py
├── requirements.txt
└── README.md
```

## Features

- **Key-Value Store**: Store and retrieve values associated with keys.
- **Data Structures**: Support for lists and sets.
- **Protocol Handling**: Implements a communication protocol for client-server interaction.
- **Command Processing**: Efficiently routes commands to the appropriate handlers.

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd redis_like_db
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the server:
   ```
   python src/server.py
   ```

## Usage Examples

- Set a key-value pair:
  ```
  SET mykey "Hello"
  ```

- Get a value by key:
  ```
  GET mykey
  ```

- Delete a key:
  ```
  DEL mykey
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.