from flask.views import MethodView
from flask import jsonify

class PokeJokeController(MethodView):

    # def get(self):
    #     return jsonify({"data": ["Apple", "Banana", "Cherry"]})

    # def something(self):
    #     return jsonify({"info": "This is something else!"})
    
    def get(self, action=None):  # Ensure this accepts the "action" parameter
        if action == "something":
            return self.something()
        
        return jsonify({"jokes": ["Apple", "Banana", "Cherry"]})

    def something(self):
        return jsonify({"info": "This is something else!"})
            