#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM players;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) FROM players;")
    count = c.fetchone()
    conn.close()
    return count[0]

def registerPlayer(name):
    """Adds a player to the tournament database.  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO players (name,wins,matches) VALUES ('{0}',0,0);".format(name))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT id, name, wins, matches FROM players ORDER BY wins DESC;")
    players = c.fetchall()
    conn.close()
    return players

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    increaseWinCount(winner)
    increaseMatchCount(winner, loser)
    createMatch(0,winner,loser,winner)
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """

def increaseWinCount(winnerId):
    """Increase the win count on the for the winner with given winnerId
    """
    conn = connect()
    c = conn.cursor()
    c.execute("UPDATE players SET wins = wins+1 WHERE id = '{0}';".format(winnerId))
    conn.commit()
    conn.close()

def increaseMatchCount(player1, player2):
    """Increase the match count of both players
    """
    conn = connect()
    c = conn.cursor()
    query = "UPDATE players SET matches = matches+1"
    c.execute("UPDATE players SET matches = matches + 1 WHERE id = '{0}' OR id = '{1}';".format(player1, player2))
    conn.commit()
    conn.close()

def createMatch(roundNumber, player1Id, player2Id, winnerId):
    """Create a match and add it to the matches table
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO matches (round, player_1_id, player_2_id, winner_id) VALUES ('{0}','{1}','{2}','{3}');".format(roundNumber, player1Id, player2Id, winnerId))
    conn.commit()
    conn.close()

def listMatches():
    """List all the matches in table ordered by round number.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM matches ORDER BY round DESC;")
    matches = c.fetchall()
    conn.close()
    return matches
