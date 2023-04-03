## Timelines of Friendships on Social Media

### Description
There are two lists of dictionaries representing friendship beginnings and endings: 
friends_added and friends_removed. Each dictionary contains the user ids and the date
of the friendship beginning /ending.

Here are short examples of how the lists look like:
```python
friends_added = [
    {'users': [1, 2], 'date': '2020-01-01'},
    {'users': [3, 2], 'date': '2020-01-02'},
    {'users': [2, 1], 'date': '2020-02-02'},
    {'users': [4, 1], 'date': '2020-02-02'}]

friends_removed = [
    {'users': [2, 1], 'date': '2020-01-03'},
    {'users': [2, 3], 'date': '2020-01-05'},
    {'users': [1, 2], 'date': '2020-02-05'}]
```

<br><br>
### Task
Write a function friendship_timelines to generate an output that lists the pairs of friends 
with their corresponding dates of the friendship beginning and ending. There can be multiple 
instances over time when two people became friends and unfriended. Only output values when a 
corresponding friendship was removed.

The output should have the following format:
```python
friendships = [{
    'users': [1, 2],
    'start_date': '2020-01-01',
    'end_date': '2020-01-03'
  },
  {
    'users': [1, 2],
    'start_date': '2020-02-02',
    'end_date': '2020-02-05'
  },
  {
    'users': [2, 3],
    'start_date': '2020-01-02',
    'end_date': '2020-01-05'
  },
]
```

<br><br>
### Solutions
A python solution that uses looping over the list is given here.  
A solution using pandas dataframes can be found in the `pandasNdataFrames/friendships_timeline` folder.

<br><br>
### Tests

**Python:**   
Using _pytest_.  
Run `py.test` from `katas/programming/temporal_overlap_probability/python`

<br><br>
