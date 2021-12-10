def score_corrupted(line):
    score = {")":3, "]": 57, "}":1197, ">":25137}
    reduced_line = line.replace("()", "").replace("[]","").replace("{}","").replace("<>","")
    if len(reduced_line) == len(line):
        closing_brackets = reduced_line.replace("(", "").replace("[","").replace("{","").replace("<","")
        if len(closing_brackets)>0:
            return score[closing_brackets[0]]
        else:
            return 0
    return score_corrupted(reduced_line)

def score_incomplete(line):
    score = {"(":1, "[": 2, "{":3, "<":4}
    reduced_line = line.replace("()", "").replace("[]","").replace("{}","").replace("<>","")
    if len(reduced_line) == len(line):
        closing_brackets = reduced_line.replace("(", "").replace("[","").replace("{","").replace("<","")
        if len(closing_brackets)>0:
            return 0
        else:
            return sum([5**(i)*score[x] for i,x in enumerate(list(reduced_line))])
    return score_incomplete(reduced_line)


with open('input.txt') as f:
        data = f.read().splitlines()

print("PART 1:")
print(sum([score_corrupted(x) for x in data]))

incomplete_scores = [score_incomplete(x) for x in data if score_incomplete(x) != 0]
incomplete_scores.sort()

print("PART 2:")
print(incomplete_scores[int(len(incomplete_scores)/2)])