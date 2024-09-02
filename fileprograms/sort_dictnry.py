placements={"jango":2,"bitdata":7,"java":6,"aspnet":9,"testing":4}
def get_value(key):
    return placements.get(key)
srt=sorted(placements,key=get_value,reverse=True)
print(srt)
def get_va(key):
    return w