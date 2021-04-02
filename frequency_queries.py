from collections import Counter

def freqQuery(queries):
  valueFreq = Counter()
  freqCount = Counter()
  answer = []
  
  for query in queries:
    if query[0] == 1:
      if valueFreq[query[1]] > 0:
        freqCount[valueFreq[query[1]]] -= 1
      valueFreq[query[1]] += 1
      freqCount[valueFreq[query[1]]] += 1
    elif query[0] == 2:
      if valueFreq[query[1]] > 0:
        freqCount[valueFreq[query[1]]] -= 1
        valueFreq[query[1]] -= 1
        freqCount[valueFreq[query[1]]] += 1
    else:
      if freqCount[query[1]] > 0:
        answer.append(1)
      else:
        answer.append(0)
  return answer