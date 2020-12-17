## Introduction
This is a solution to the 15th puzzle of the advent of code 2020.

The code is available at [github](https://github.com/MatiasStorm/AdventOfCode_2020)

## Solution

### Part 1

As allways part one is somewhat straight forward.
```python
def read_fields():
    fields = {}
    with open("fields.txt", "r") as f:
        for l in f.readlines():
            l = l.strip()
            field = l[0:l.index(":")]
            min1 = int(l[l.index(":") + 2: len(l)].split(" or ")[0].split("-")[0])
            max1 = int(l[l.index(":") + 2: len(l)].split(" or ")[0].split("-")[1])
            min2 = int(l[l.index(":") + 2: len(l)].split(" or ")[1].split("-")[0])
            max2 = int(l[l.index(":") + 2: len(l)].split(" or ")[1].split("-")[1])
            fields[field] = [i for i in range(min1, max1+1)] + [i for i in range(min2, max2+1)] # Create array of all possible values
    return fields

def read_nearby_tickets():
    tickets = []
    with open("nearby_tickets.txt", "r") as f:
        for l in f.readlines():
            tickets.append([int(i) for i in l.strip().split(",")])
    return tickets

def get_tickets_errorrate(tickets, fields):
    errors = 0
    for ticket in tickets:
        for val in ticket:
            found = False
            for f in fields:
                if val in fields[f]:
                    found = True
            if not found:
                errors += val
    return errors

fields = read_fields()
tickets = read_nearby_tickets()
print("Part 1:", get_tickets_errorrate(tickets, fields))
```
We read the fields and their ranges, and all the tickets. 
Then we check every value in every ticket and see if it matches a field range.

### Part 2
Part two was a bit more involved.

The basic idea is to start with the first position of every ticket, 
find the fields all tickets matches. If only one field is found that field 
cannot be on any other position, thus we can remove it from the search.

Here is the code:
```python
def remove_invalid_tickets(tickets, fields):
    for ticket in tickets.copy():
        for val in ticket:
            found = False
            for f in fields:
                if val in fields[f]:
                    found = True
            if not found:
                tickets.remove(ticket)
    return tickets

def get_depature_product(tickets, fields):
    your_ticket = [127,109,139,113,67,137,71,97,53,103,163,167,131,83,157,101,107,79,73,89]
    positions = [list(fields.keys()) for i in range(len(tickets[0]))]
    departure_fields = [i for i in fields if "departure" in i]
    product = 1
    while len([field for fields in positions for field in fields]) != len(tickets[0]): # Check if all positions are found
        for i in range(len(tickets[0])): # Loop through the possible field positions.
            for t in tickets: # Loop through all the tickets
                for field in positions[i].copy():
                    if t[i] not in fields[field]:
                        positions[i].remove(field) # Remove fields that dont match this tickets position
                
                if len( positions[i] ) == 1: # Only on possible field
                    field = positions[i][0]
                    
                    if field in departure_fields: # Calculate the product
                        product *= your_ticket[i]
                        departure_fields.remove(field)
                        
                    for j in range(len(positions)): # Remove found field from all other positions
                        if field in positions[j] and j != i:
                            positions[j].remove(field)
                    break # Don't need to look no further
    return product
    
    
fields = read_fields()
tickets = remove_invalid_tickets(read_nearby_tickets(), fields)
print("Part 2:", get_depature_product(tickets, fields))
```
I have tried to document the code with comments as well as I could, hope it is understandable.

Thanks for reading!
