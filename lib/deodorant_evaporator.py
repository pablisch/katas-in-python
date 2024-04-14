def deodorant_evaporation_threshold_1(content, loss_rate, threshold):
    min_content = content * threshold / 100
    days = 0
    while content > min_content:
        content -= (content * loss_rate / 100)
        days += 1
    return days

def deodorant_evaporation_threshold(content, loss_rate, threshold):
    days = 0
    percent = 100
    while percent > threshold:
        percent -= (percent * loss_rate / 100)
        days += 1
    return days