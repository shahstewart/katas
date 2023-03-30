# Smallest difference in scores
This kata involves getting the smallest difference between values of a column.  

We have a player's score table as follows:  

### Players table
| Column | Type    |
|--------|---------|
| id     | int     |
| player | varchar |
| score  | int     |

<br><br>

## Question
The task is to find a pair of players with the minimum difference between their scores. If more than one player
combination has the same minimum score difference, select the first player name that is lowest in the alphabetical 
order and the second player name that is the highest in the alphabetical order.

### Expected output
| Column     | Type |
|------------| ---- |
| player_one | varchar |
| player_two | varchar |
| score_diff | int |  

<br><br>

## Setup
```postgresql
DROP TABLE IF EXISTS public.scores;

CREATE TABLE IF NOT EXISTS public.scores
(
    id serial primary key,
    player varchar(50) NOT NULL,
    score integer NOT NULL
);

insert into scores (player, score)
values
('Jack Spears', 80),
('Samantha Spears', 83),
('Anne Matte', 60),
('Dick Donaldson', 76),
('Jill Black', 88),
('James Green', 75),
('Jock Sespaniak', 64),
('Gerard Runner', 58),
('Tom Booths', 90),
('Bill Brady', 69),
('Walter Brady', 70),
('Julia Arnold', 74);
```
<br><br>

## Solution
```postgresql
select
    s.player as player_one,
    s2.player as player_two,
    abs(s.score - s2.score) as score_diff
from scores as s
cross join scores as s2
where s.player != s2.player
order by score_diff, s.player, s2.player DESC
limit 1;
```
<br>

## Tags
self join, cross join, multiple order by, abs()

