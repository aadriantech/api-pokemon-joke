from flask.views import MethodView
from flask import jsonify, request
import sys, requests

class PokeJokeController(MethodView):
    
    """ 
    Controller function mapping
    -------------------------------------------------
    Uses switch cases dictionary to route action names
    """
    def get(self, action=None):
        try:
            # Map actions to their respective functions
            switch = {
                "speak": self.speak,
                "species": self.species        
            }

            # Retrieve the function based on the provided action
            func = switch.get(action, self.default_case)

            # Call and return the result of the function
            return func()

        except Exception as e:
            # Handle or log the error
            print(f"Error occurred: {e}")
            return {"error": "An unexpected error occurred"}

    
    """ 
    Return bad request if action not found
    -------------------------------------------------
    Return: JSON
    """
    def default_case(self):
        return jsonify({"info": "Bad request"}, 400)
        
    """
    Provides all the information for a given pokemon name
    -------------------------------------------------
    Params: string:pokemon
    Return: JSON
    """
    def speak(self):        
        pokemon_name = request.args.get('pokemon')        
        
        skills = self.fetch_pokemon_skills(pokemon_name)
        joke = self.fetch_joke()
        
        if skills and joke:
            result = {
                "pokemon_name": pokemon_name,
                "skills": skills,
                "joke": joke
            }
            return jsonify(result), 200
        else:
            return jsonify({"error": "Error fetching data."}), 500            


    """
    Provides all the information for a given pokemon name
    -------------------------------------------------
    Params: string:pokemon
    Return: JSON
    """
    def species(self):
        pokemon_name = request.args.get('pokemon')
        
        species = self.fetch_pokemon_species(pokemon_name)        

        if species:
            result = {                
                "data": species,       
            }
            return jsonify(result), 200
        else:
            return jsonify({"error": "Error fetching data."}), 500
    
    """
    Provides all the skills for a pokemon
    -------------------------------------------------
    Params: string:pokemon
    Return: array
    """
    def fetch_pokemon_skills(self, pokemon_name):
        
        POKEAPI_ENDPOINT = "https://pokeapi.co/api/v2/pokemon/{}"        
        response = requests.get(POKEAPI_ENDPOINT.format(pokemon_name))
        
        if response.status_code != 200:
            return None
        
        pokemon_data = response.json()
        
        # return skills only
        return [move["move"]["name"] for move in pokemon_data["moves"]]        

    """
    Retrieve a joke from the Joke API
    -------------------------------------------------
    Params: none
    Return: string
    """
    def fetch_joke(self):
        
        JOKEAPI_ENDPOINT = "https://v2.jokeapi.dev/joke/Miscellaneous"
        response = requests.get(JOKEAPI_ENDPOINT)
        
        if response.status_code != 200:
            return None
        
        joke_data = response.json()
        
        if joke_data["type"] == "single":
            return joke_data["joke"]
        
        else:
            return f"{joke_data['setup']} {joke_data['delivery']}"

    """
    Retrieve pokemon species data
    -------------------------------------------------
    Params: none
    Return: string
    """
    def fetch_pokemon_species(self, pokemon_name):
        POKEAPI_ENDPOINT = "https://pokeapi.co/api/v2/pokemon-species/{}"
        response = requests.get(POKEAPI_ENDPOINT.format(pokemon_name))
        
        if response.status_code != 200:
            return None
        
        species_data = response.json()
        
        # Extract species name
        species_name = species_data.get('name', None)
        
        # Extract English flavor texts
        flavor_text_entries = species_data.get('flavor_text_entries', [])
        english_flavor_texts = [entry['flavor_text'] for entry in flavor_text_entries if entry['language']['name'] == 'en']
        
        # Combining the species name with the first English flavor text description
        # You can adjust this logic based on how you want to use the multiple flavor texts (if available).
        description = english_flavor_texts[0] if english_flavor_texts else None
        
        return {
            "name": species_name,
            "description": description
        }