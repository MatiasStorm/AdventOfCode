def read_rules(file_name):
    rules = {}
    with open(file_name, "r") as f:
        for l in f.readlines():
            l = l.strip()
            rule_no = l.split(":")[0]
            rules[rule_no] = [n for n in l.split(" ")[1:] if n != "|"]
    return rules

def read_messages(file_name):
    with open(file_name, "r") as f:
        return [l.strip() for l in f.readlines()]

def get_message(rules, rule):
    messages = []
    sub_rules = rules[rule]
    if sub_rules[0] in "ab":
        return sub_rules
    elif len(sub_rules) == 1:
        return get_message(rules, sub_rules)
    elif len(sub_rules) == 2:
        messages.append(get_message(rules, sub_rules[0]) + get_message(rules, sub_rules[1]))
    else:
        m1 = get_message(rules, sub_rules[0]) + get_message(rules, sub_rules[1])
        m2 = get_message(rules, sub_rules[2]) + get_message(rules, sub_rules[3])
        messages += [ m1, m2 ]
    return messages


# def get_valid_messages(rules):
#     messages = []
#     for r in rules:
#         message = ""
#         sub_rules = rules[r]
#         if sub_rules in "ab":
#             return sub_rules
#         elif len(sub_rules) == 2:
#             message += get_message(rules, sub_rules[0]) + get_message(rules,sub_rules[1])
#         else:


if __name__ == "__main__":
    test = {"0" : ["4", "1", "5"], "1": [["2", "3"], ["3", "2"]], }
    rules = read_rules("rules.txt")
    messages = read_messages("messages.txt")
    print(get_message(rules, "0"))
