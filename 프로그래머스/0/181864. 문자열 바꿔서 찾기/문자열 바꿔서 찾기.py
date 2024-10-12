def solution(myString, pat):
    myString = myString.replace("A", "D").replace("B", "C")
    pat = pat.replace("A", "C").replace("B", "D")
    
    return int(pat in myString)