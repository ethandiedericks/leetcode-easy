def finalValueAfterOperations(operations):
    output = 0
    freq = {
            "--X":0,
            "X--":0,
            "X++":0,
            "++X":0,
        }
    for operation in operations:
        freq[operation] += 1
    for key,val in freq.items():
        if val > 0:
            if '-' in key:
                output -= val
            else: output += val
    return output

print(finalValueAfterOperations(["--X","X++","X++"])) # output = 1
print(finalValueAfterOperations(["++X","++X","X++"])) # output = 3
print(finalValueAfterOperations(["X++","++X","--X","X--"])) # output = 0