def tournamentWinner(competitions, results):
    teamdict = {}
    for i, arr in enumerate(competitions):
        if arr[1-results[i]] not in teamdict.keys():
            teamdict[arr[1-results[i]]] = 3
        else:
            teamdict[arr[1-results[i]]] += 3
    return max(teamdict, key=teamdict.get)


# O(n) time | O(k) space - where n is the number
HOME_TEAM_WON = 1


def tournamentWinner2(competitions, results):
    currentBestTeam = ""
    scores = {currentBestTeam: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition

        if result == HOME_TEAM_WON:
            winningTeam = homeTeam
        else:
            winningTeam = awayTeam

        updateScores(winningTeam, 3, scores)

        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam

    return currentBestTeam


def updateScores(team, points, scores):
    if team not in scores:
        scores[team] = 0

    scores[team] += points
