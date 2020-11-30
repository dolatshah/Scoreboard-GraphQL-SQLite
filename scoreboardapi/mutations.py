from datetime import datetime

from ariadne import convert_kwargs_to_snake_case

from scoreboardapi import db
from scoreboardapi.models import Player


@convert_kwargs_to_snake_case
def resolve_create_player(obj, info, address, age,score):
    try:
        # address, age and score is required
        player = Player(
            address=address, age=int(age),score=int(score)
        )
        db.session.add(player)
        db.session.commit()
        payload = {
            "success": True,
            "player": player.to_dict()
        }
    except ValueError:  # invalid input
        payload = {
            "success": False,
            "errors": [f"invalid input"]
        }

    return payload




@convert_kwargs_to_snake_case
def resolve_delete_player(obj, info, player_id):
    try:
        player = Player.query.get(player_id)
        db.session.delete(player)
        db.session.commit()
        payload = {"success": True}

    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Player matching id {player_id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def resolve_update_score(obj, info, player_id, action):
    try:
        # only acceptable actions are plus and minus
        player = Player.query.get(player_id)
        if action == 'plus':
            player.score += 1
        if action == 'minus':
            player.score -= 1

        db.session.add(player)
        db.session.commit()
        payload = {
            "success": True,
            "player": player.to_dict()
        }

    except ValueError:  # action format errors
        payload = {
            "success": False,
            "errors": [f"action format errors"]
        }
    except AttributeError:  # player not found
        payload = {
            "success": False,
            "errors": [f"Player matching id {player_id} not found"]
        }
    return payload
