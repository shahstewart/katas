# Top three players

This kata basically involves accessing top n values in a column per group.

We have a **players** table that gets updated every year, with the new lifetime total
of goals for the players after the latest season.

### Players table
| Column      | Type    |
|-------------|---------|
| id          | int     |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int     |
 | club_id     | int     |  


We also have the **clubs** table as:  

| Column      | Type |
|-------------| ---- |
| id | int |
| name   | varchar |

<br>  

## Question
Given the above two tables, write a query to retrieve 3 top scorers from each club.
If a club has fewer than 3 players, retrieve 2 or 1 top player as per the case. Return
players full name, club name and lifetime total of goals.

**Assume:** at least one player per club and the firstname-lastname combination to
represent a unique player (no 2 player have the same firstname-lastname combination).  

### Expected output
| Column      | Type |
|-------------| ---- |
| full_name   | varchar |
| club_name   | varchar |
| total_goals | int |  


<br> 

## Setup
The players table
```postgresql
DROP TABLE IF EXISTS public.players;

CREATE TABLE IF NOT EXISTS public.players
(
    id serial primary key,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    total_goals integer NOT NULL,
    club_id integer NOT NULL
);

insert into players values
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
```

The clubs table 
```postgresql
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
```
<br><br>

## Solution
```postgresql
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
```
<br>

## Tags
window function, over(), partition by, row_number(), subquery, concat_ws()