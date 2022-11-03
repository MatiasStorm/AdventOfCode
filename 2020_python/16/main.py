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
        for i in range(len(tickets[0])):
            for t in tickets:
                for field in positions[i].copy(): # Remove fields that dont match this tickets position
                    if t[i] not in fields[field]:
                        positions[i].remove(field)
                if len( positions[i] ) == 1:
                    field = positions[i][0]
                    if field in departure_fields: # Calculate the product
                        product *= your_ticket[i]
                        departure_fields.remove(field)
                    for j in range(len(positions)): # Remove found field from all other positions
                        if field in positions[j] and j != i:
                            positions[j].remove(field)
                    break
    return product

if __name__ == "__main__":
    fields = read_fields()
    tickets = read_nearby_tickets()
    print("Part 1:", get_tickets_errorrate(tickets, fields))
    print("Part 2:", get_depature_product(remove_invalid_tickets(tickets, fields), fields))
