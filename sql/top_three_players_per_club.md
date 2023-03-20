# Top three players 

We have a **players** table that gets updated every year, with the new lifetime total
of goals for the players after the latest season.

### Players table
| Column      | Type |
|-------------| ---- |
| id          | varchar |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int |
 | club_id     | int |  


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

## Solution
#### Postgresql
```postgresql
    select full_name, club_name, total_goals
    from (
        select 
            concat_ws(' ', p.first_name, p.last_name) as full_name,
            c.name as club_name,
            p.total_goals,
            row_number() over (partition by c.name order by c.name, p.total_goals desc) as rownum
        from players p 
        join clubs c
        on p.club_id = c.id        
         ) t 
    where rownum < 4
```