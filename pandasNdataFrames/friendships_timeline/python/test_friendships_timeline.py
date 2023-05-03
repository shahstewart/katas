import pandas as pd
import pytest
from friendships_timeline import friendships_timeline

added = pd.DataFrame([
    {'users': [1, 2], 'date': '2022-01-01'},
    {'users': [4, 5], 'date': '2022-01-04'},
    {'users': [2, 3], 'date': '2022-01-08'},
    {'users': [3, 6], 'date': '2022-01-12'},
    {'users': [2, 1], 'date': '2022-01-16'},
    {'users': [2, 6], 'date': '2022-01-18'},
    {'users': [6, 3], 'date': '2022-01-22'},
    {'users': [4, 6], 'date': '2022-01-26'},
    {'users': [5, 6], 'date': '2022-01-30'}
])

removed = pd.DataFrame([
    {'users': [2, 1], 'date': '2022-01-12'},
    {'users': [6, 3], 'date': '2022-01-18'},
    {'users': [4, 5], 'date': '2022-01-20'},
    {'users': [1, 2], 'date': '2022-01-22'}
])

def test_friendships_timeline():
    res = friendships_timeline(added, removed)
    assert len(res) == 4
    assert len(res) == len(removed)
    assert res[0]['users'] == removed.iloc[0]['users']
    for v in res:
        assert v['start_date'] < v['end_date']
