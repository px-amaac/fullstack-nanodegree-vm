-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
DROP database IF EXISTS tournament;
CREATE database tournament;
\c tournament;
DROP TABLE IF EXISTS matches;
CREATE TABLE matches
(
	round			integer NOT NULL,
	player_1_id		integer NOT NULL,
	player_2_id		integer NOT NULL,
	winner_id		integer
);
DROP TABLE IF EXISTS players;
CREATE TABLE players
(
	player_id		integer PRIMARY KEY,
	name			varchar(45) NOT NULL,
	wins			integer,
	opponent_match_wins	integer
);
DROP TABLE IF EXISTS tournament;
CREATE TABLE tournament
(
	registered_players_count	integer,
	total_rounds			integer,
	rounds_played			integer,
	matches_played			integer,
	total_matches			integer
);
