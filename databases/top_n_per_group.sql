-- Setup
-- The players table
DROP TABLE IF EXISTS public.players;

CREATE TABLE IF NOT EXISTS public.players
(
    id serial primary key,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    total_goals integer NOT NULL,
    club_id integer NOT NULL
);

insert into players (first_name, last_name, total_goals, club_id)
values
('Jack', 'Spears', 333, 1),
('Samantha', 'Spears', 223, 2),
('Anne', 'Matte', 167, 3),
('Dick', 'Donaldson', 120, 3),
('Jill', 'Black', 33, 2),
('James', 'Green', 240, 2),
('Jock', 'Sespic', 27, 2),
('Gerard', 'Runner', 130, 2),
('Tom', 'Booths', 90, 1),
('Bill', 'Brady', 133, 1);

-- The clubs table
DROP TABLE IF EXISTS public.clubs;

CREATE TABLE IF NOT EXISTS public.clubs
(
    id serial primary key,
    club_name varchar(30) NOT NULL
);

insert into clubs (club_name)
values
('Avocado Orchards'),
('Melaluka Farms'),
('Cane Cooks'),
('Cypress Sprinters');


/* Question: Select top n number of values per group
   Given the scores and the club table, pick top 3 scorers for each club.
   Return the results in the order of club ascending, score descending.
 */

-- Solution
select full_name, club_name, total_goals
from (
    select
        c.club_name,
        concat_ws(' ', p.first_name, p.last_name) as full_name,
        p.total_goals,
        row_number() over (partition by c.club_name order by c.club_name, p.total_goals desc) as rownum
    from players p
    join clubs c
    on p.club_id = c.id
     ) t
where rownum < 4;
