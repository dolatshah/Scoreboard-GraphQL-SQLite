from ariadne import convert_kwargs_to_snake_case

from .models import Player


def resolve_players(obj, info):
    try:
        players = [player.to_dict() for player in Player.query.all()]
        payload = {
            "success": True,
            "players": players
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def resolve_player(obj, info, player_id):
    try:
        player = Player.query.get(player_id)
        payload = {
            "success": True,
            "player": player.to_dict()
        }

    except AttributeError:  # player not found
        payload = {
            "success": False,
            "errors": [f"Player matching id {player_id} not found"]
        }

    return payload
