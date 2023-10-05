# Pokémon Service

A simple service that provides details about Pokémon and offers some light-hearted Pokémon-related humor.

## Features

- Retrieve Pokémon skills.
- Get a random miscellaneous joke related to Pokémon.

## Prerequisites

- Python 3.x
- Flask
- Requests

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/aadriantech/api-pokemon-joke.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pokemon-service
   ```

3. Install the required packages: (this project uses docker also)
   ```bash
   pip install -r requirements.txt
   ```

## Usage vanilla python

1. Start the Flask server:
   ```bash
   python main.py
   ```

## Usage Docker container
1. Start the docker container:
   ```bash
   docker-compose up --build
   ```

2. Open your browser or API tool (like Postman):
   - To get Pokémon skills and joke:
     ```
     http://localhost:5000/poke-joke/speak?pokemon=pikachu
     ```

   - To get a Pokémon species information:
     ```
     http://localhost:5000/poke-joke/species?pokemon=bulbasaur
     ```

## Unit Testing

1. Run the test:
   ```bash
   pytest
   ```

## API Endpoints

- `/poke-joke/species?pokemon={name}`: Get species information for a given Pokémon.
- `/poke-joke/speak?pokemon={name}`: Get skills of the given Pokémon and for it to say a joke.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss the proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.