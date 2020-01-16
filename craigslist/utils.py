

def start_urls_maker(query, min, max):
	with open("states_2.csv", "r+") as file:
		lines = (line.rstrip() for line in file)
		# lines = ''.join("%s".join(line for line in lines if line) % "Ford")
		# lines = list(line.append("Ford") for line in lines if line)
		lines = [(line.format(min, max, query)) for line in lines if line]

		return lines