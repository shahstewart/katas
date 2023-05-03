import pandas as pd

def friendships_timeline(friends_added: pd.DataFrame, friends_removed: pd.DataFrame):
    friends_added = friends_added.sort_values(by='date')
    friends_removed = friends_removed.sort_values(by='date')
    friends_added['users'] = friends_added.users.apply(lambda x: {*x})  # convert the list to set to allow comparison

    timeline = []
    for i, r in friends_removed.iterrows():
        sts = friends_added[friends_added.users.apply(lambda x: x == {*r.users})].query('date <= @r.date')
        timeline.append({
            'users': r.users,
            'start_date': sts.iloc[0].date,
            'end_date': r.date})

    return timeline
