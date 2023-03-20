# Player Points (Error in table update)
We have a **players** table that gets updated every year, with the new lifetime total
of goals for the player after the latest season. This year, instead of updating the goals 
total, an employee errored and did an insert.

### Players table
| Column      | Type |
|-------------| ---- |
| id          | varchar |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int |
 | club_id     | int |

Please note that the id is a varchar.
<br><br>

## Question
Write a query to get current goal total for each player.  
Assume no players have the same first-last name combination.

### Expected output
| Column      | Type |
|-------------| ---- |
| first_name  | varchar |
| last_name   | varchar |
| total_goals | int |  

<br><br>


## Solution
#### Postgresql
```postgresql
select p.first_name, p.last_name, p.total_goals
from players p
join (select max(id::int) as id, first_name, last_name
		from players
		group by first_name, last_name) as t
on e.id::int = t.id
```

