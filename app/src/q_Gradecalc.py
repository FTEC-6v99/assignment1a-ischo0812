# Create a function called: calculate_avg_grade
# Parameters: the function should receive 1 parameter: a list of student objects
#             Remember a list can contain duplicates, so you can expect two student objects with same ID but different grades
# Returns: the function should return a dictionary with student ID as key and student average grade as value
#
# Example:
# input: [Student('s1',20,1824,90.5), Student('s2',21,1823,80.0), Student('s1',20,1824,70.0)]
# output: { 1824: 80.25, 1823: 80.0 }
#
# If the list of students is empty, return an empty dictionary
# Make sure that you add type hints to the function paramter and return value

from app.src.q_Student import Student
from app.src.q_Utils import calculate_avg


def calculate_avg_grade(statsheets: list[StatSheet]) -> dict[int, float]:
    player_to_stats: dict[int, list[StatSheet]] = {}
    if len(StatSheet) == 0:
        raise Exception('Dictionary is empty')
    else:
        for statsheet in statsheets:
            player_id: int = statsheet.player.number
            if player_id in player_to_stats.keys():
                player_to_stats.get(player_id).append(statsheet)
            else:
                player_to_stats[player_id] = [statsheet]
                player_to_avgpts: dict[int, float] = {}
        for player_id, stats in player_to_stats.items():
            points = [x.stats.points for x in stats]
            avg_pts = calculate_avg(points)
            player_to_avgpts[player_id] = avg_pts
        return player_to_avgpts
