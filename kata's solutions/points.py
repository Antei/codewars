def points(games):
	result = 0
	for match in games:
		x, y = map(int, match.split(':'))
		if x > y:
			result += 3
		elif x == y:
			result += 1
	return result


games = ['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']

print(points(games))  # 30

# Rules for counting points for each match:

# if x > y: 3 points
# if x < y: 0 point
# if x = y: 1 point