## create a virtualenv
```bash
python3 -m venv scoreboard_env
```

## install the required packages
```bash

pip install -r requirements.txt
```
## create database file
make an empty file named scoreboard.db

## initiate database
```bash

python initiate.py 
```

## Running the app

```bash
export FLASK_APP=main
```

Start the server 
```bash
flask run
```

Open the GraphQL dashboard at http://localhost:5000/graphql 


## create player
```bash
mutation newPlayer {
  createPlayer(address:"Vancouver", age:27, score:1) {
    success
    errors
    player {
      id
      address
      age
	  score
    }
  }
}
```

## get list of players
```bash

query fetchAllPlayers {
  players {
    success
    errors
    players {
      address
      age
	  score
      id
    }
  }
}
```

# delete player
```bash

mutation {
  deletePlayer(playerId: "1") {
    success
    errors
  }
}
```

#update score
```bash

mutation updateScore {
  updateScore(playerId: "1", action: "plus") {
    success
    errors
  }
}
```