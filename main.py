from scoreboardapi import app, db


from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from scoreboardapi.mutations import resolve_create_player,  \
    resolve_delete_player, resolve_update_score
from scoreboardapi.queries import resolve_players, resolve_player

query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("players", resolve_players)
query.set_field("player", resolve_player)

mutation.set_field("createPlayer", resolve_create_player)
mutation.set_field("deletePlayer", resolve_delete_player)
mutation.set_field("updateScore", resolve_update_score)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers
)


# access to the main dashboard
@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200

# run queries
@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
