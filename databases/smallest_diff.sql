-- setup
-- table scores
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


/* Question: Find the players with the smallest difference in scores.

If more than one pair of players have the same score diff, then pick the
first player that is the lowest in the alphabetical order and second player
that is the highest in the alphabetical order.
*/

-- Solution
select
    s.player as player_one,
    s2.player as player_two,
    abs(s.score - s2.score) as score_diff
from scores as s
cross join scores as s2
where s.player != s2.player
order by score_diff, s.player, s2.player DESC
limit 1;
