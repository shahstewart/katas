-- Setup

-- The players table
DROP TABLE IF EXISTS public.players;

CREATE TABLE IF NOT EXISTS public.players
(
    id varchar NOT NULL, -- notice id is varchar!
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    total_goals integer NOT NULL,
    club_id integer NOT NULL,
    CONSTRAINT players_pkey PRIMARY KEY (id)
);

insert into players values
('1', 'Jack', 'Spears', 333, 1),
('2', 'Samantha', 'Spears', 223, 2),
('3', 'Anne', 'Matte', 167, 3),
('4', 'Dick', 'Donaldson', 120, 3),
('5', 'Jill', 'Black', 33, 2),
('6', 'James', 'Green', 240, 2),
('7', 'Jock', 'Sespic', 27, 2),
('8', 'Gerard', 'Runner', 130, 2),
('9', 'Tom', 'Booths', 90, 1),
('10', 'Bill', 'Brady', 133, 1);


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


/* Question : there are multiple entries for some players due to an etl error.
Get each players current goal total. */

-- Solution
select p.first_name, p.last_name, p.total_goals
from players p
join (select max(id::int) as id, first_name, last_name
		from players
		group by first_name, last_name) as t
on p.id::int = t.id
