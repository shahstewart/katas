# Single vs Multiple Comment Users
We have a **Comments** table that holds comment ids, post ids and user ids as follows:

### comments table
| Column     | Type     |
|------------|----------|
| id         | int      |
| post_id    | int      |
| user_id    | int      |
 | created_at | datetime |

<br><br>

## Question
Given the comments table, write a query to retrieve counts of users that commented only once on 
any post as *single_comment_users* and users that commented on any post more than once 
as *multi_comment_users*.

### Expected output
| Column               | Type |
|----------------------|------|
| single_comment_users | int  |
| multi_comment_users  | int  |


<br><br>

## Setup
```postgresql
DROP TABLE IF EXISTS public.comments;

CREATE TABLE IF NOT EXISTS public.comments
(
    id serial primary key,
    post_id integer NOT NULL,
    user_id integer NOT NULL,
	date_posted timestamp not null
);

insert into comments (post_id, user_id, date_posted)
values
(1, 3, '2023-3-2 10:30:30'),
(2, 2, '2023-3-2 10:33:30'),
(1, 3, '2023-3-2 10:37:30'),
(3, 1, '2023-3-2 10:37:50'),
(4, 4, '2023-3-2 10:40:30'),
(1, 3, '2023-3-2 10:44:30'),
(2, 2, '2023-3-2 10:48:30'),
(5, 4, '2023-3-2 10:49:30'),
(6, 4, '2023-3-2 10:50:30'),
(1, 3, '2023-3-2 10:51:30'),
(7, 5, '2023-3-2 10:53:30');
```

<br><br>

## Solution
```postgresql
select 
	count(distinct a.user_id) as multi_comment_users, 
	count(distinct c.user_id) - count(distinct a.user_id) as single_comment_users 
from 
	comments c,
	(select user_id from comments group by user_id, post_id having(count(*) > 1)) a;
```
<br>  

## Tags
count, count distinct, subquery, having()
