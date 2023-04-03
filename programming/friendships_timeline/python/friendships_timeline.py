def friendships_timeline(friends_added, friends_removed):
    # sort the lists by date just in case they are not.
    friends_added = sorted(friends_added, key=lambda x: x['date'])
    friends_removed = sorted(friends_removed, key=lambda x: x['date'])

    timeline = []
    for v in friends_removed:
        added_entries = [
            entry for entry in friends_added if set(entry['users']) == set(v['users']) and entry['date'] < v['date']
        ]  # dates are in YYYY-MM-DD format, allows for string comparison

        timeline.append({
            'users': sorted(v['users']),
            'start_date': added_entries[len(added_entries) - 1]['date'],
            'end_date': v['date']
        })

    return timeline
