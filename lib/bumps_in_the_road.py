# splits the road string and then counts the bumps
def long_journey(road):
    sections = list(road)
    bumps = sections.count("n")
    return "Woohoo!" if bumps <= 15 else "Car Dead"

# just counts the bumps in the road string directly because you can
def shorter_journey(road):
    bumps = road.count("n")
    return "Woohoo!" if bumps <= 15 else "Car Dead"

# concise
def journey(road):
    return "Woohoo!" if road.count("n") <= 15 else "Car Dead"
