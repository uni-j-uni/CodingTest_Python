def solution(name, yearning, photo):
    list = dict(zip(name, yearning))

    return [sum(list.get(person, 0) for person in p) for p in photo]