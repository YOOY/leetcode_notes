def findingUsersActiveMinutes(logs, k):
    ans = [0] * k
    users = {}
    for user, minutes in logs:
        u = users.get(user, set())
        u.add(minutes)
        users[user] = u
    for v in users.values():
        ans[len(v)-1] += 1
        
    return ans

print(findingUsersActiveMinutes([[0,5],[1,2],[0,2],[0,5],[1,3]], 5))