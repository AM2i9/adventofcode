totals = []

with open('input.txt') as f:
    content = f.read()
    elves = content.split('\n\n')

for elf in elves:
    calories = elf.split('\n')
    totals.append(sum([int(c) for c in calories if c.isdigit()]))

print(max(totals))

totals.sort(reverse=True)
print(sum(totals[:3]))
