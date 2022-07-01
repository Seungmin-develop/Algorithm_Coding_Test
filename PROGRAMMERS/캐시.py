def solution(cacheSize, cities):
    answer = 0
    
    cache = []
    
    if cacheSize == 0:
        answer = len(cities) * 5
        return answer
    
    for idx, city in enumerate(cities):
        city = city.lower()
        
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                del cache[0]
                cache.append(city)
            answer += 5
    
    return answer