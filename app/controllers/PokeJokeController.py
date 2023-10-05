from flask.views import MethodView
from flask import jsonify, request
import sys, requests

class PokeJokeController(MethodView):
    
    """ 
    -------------------------------------------------
    Controller function mapping
    Uses switch cases dictionary to route action names
    -------------------------------------------------
    """
    def get(self, action=None):  # Ensure this accepts the "action" parameter
        
        # print(pokemon_name)
        # sys.exit(1)
        
        # Map actions to their respective functions
        switch = {
            "speak": self.speak,
            "species": self.species        
        }
                
        # Retrieve the function based on the provided action
        func = switch.get(action, self.default_case)

        # Call and return the result of the function
        return func()
    
    """ 
    -------------------------------------------------
    Return bad request if action not found
    Return: JSON
    -------------------------------------------------
    """
    def default_case(self):
        return jsonify({"info": "Bad request"}, 400)
        
    """
    -------------------------------------------------
    Provides all the information for a given pokemon name
    Params: string:pokemon
    Return: JSON
    -------------------------------------------------
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
    -------------------------------------------------
    Provides all the information for a given pokemon name
    Params: string:pokemon
    Return: JSON
    -------------------------------------------------
    """
    def species(self):
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
    -------------------------------------------------
    Provides all the skills for a pokemon
    Params: string:pokemon
    Return: array
    -------------------------------------------------
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
    -------------------------------------------------
    Retrieve a joke from the Joke API
    Params: none
    Return: string
    -------------------------------------------------
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
