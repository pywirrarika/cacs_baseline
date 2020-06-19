
def accuracy(data):
    correct = 0
    total = 0
    for instance in data:
        for token in instance:
            if token[1] == token[2]:
                correct += 1
            total += 1

    return correct/total
