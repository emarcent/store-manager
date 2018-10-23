def errors(json):
    error_count = 0
    for key,value in json.items():
        if value == "":
            error_count += 1
    if error_count != 0:
        return True
    return False
