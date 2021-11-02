## Farkle is a dice game.

a game consists of 2 or more players. each player takes a turn

1. To start, the player roles 6 dice.
2. The player must set apart at least one scoring set of dice (see notes on scoring)
3. Next, the player roles the remaining dice, hoping for another scoring set
4. If there is one or more scoring sets, repeat steps 2 & 3
5. If player runs out of dice or there are not scoring sets, then the turn ends
6. Next player is up to repeat steps 1-5

There is a traditional score you are trying to get, 10000, but any target score can be agreed upon by all players

## CLI Considerations

   - cli should prompt for a new game or load a current game (stored in a db)
   - each game should have a set number of players with names stored
   - do not trust the players to not try and cheat. they are a bunch of cheaters