from app.controllers.PokeJokeController import PokeJokeController

def init_routes(app):
    poke_joke_view = PokeJokeController.as_view('poke-joke-api')
    
    app.add_url_rule('/poke-joke', defaults={'action': None}, view_func=poke_joke_view, methods=['GET'])
    app.add_url_rule('/poke-joke/<string:action>', view_func=poke_joke_view, methods=['GET'])
