import os

axiom = 'A'

init = {'init_0': ('A', '#S#'),
        'init_1': ('S', 'aQ'),
        'init_2': ('Q', 'bQ'),
        'init_3': ('Q', 'b+')}

apply = ['type_1_1', 'type_1_2', 'type_1_3', 'type_1_4', 'type_1_5',
         'type_2_1', 'type_2_2', 'type_2_3', 'type_2_4',
         'type_3_1', 'type_3_2', 'type_3_3',
         'type_4_1', 'type_4_2', 'type_4_3',
         'type_5_1', 'type_5_2']

rules_apply = {'type_1_1': ('b+#', 'b*#'), 'type_1_2': ('bb*', 'b*c'), 'type_1_3': ('ab*', 'a*a-'),
               'type_1_4': ('aa*', 'a*a-'), 'type_1_5': ('#a*', '#a+'),
               'type_2_1': ('-a', 'a-'), 'type_2_2': ('-b', 'b-'), 'type_2_3': ('-c', 'b'), 'type_2_4': ('-#', '#'),
               'type_3_1': ('+a', 'a+'), 'type_3_2': ('+b', 'b+'), 'type_3_3': ('+c', 'bo'),
               'type_4_1': ('oc', "'c"), 'type_4_2': ("b'", "'b"), 'type_4_3': ("a'", 'a*'),
               'type_5_1': ('a+#', 't#'), 'type_5_2': ('at', 'tt')}

derivation = []


def apply_rule(curr_str, curr_rule):
    derivation.append(curr_rule[0] + ' -> ' + curr_rule[1] + ' : ' + curr_str.replace(curr_rule[0], curr_rule[1], 1))
    return curr_str.replace(curr_rule[0], curr_rule[1], 1)


def init_rules(n):
    start = axiom
    start = apply_rule(start, init['init_0'])
    if n >= 2:
        start = apply_rule(start, init['init_1'])
        for i in range(1, n - 1):
            start = apply_rule(start, init['init_2'])
        start = apply_rule(start, init['init_3'])
        return start
    else:
        return 'n is less than 2'


def apply_rules(curr_str):
    buff_str = curr_str
    for i in range(0, 210000):
        flag = False
        for rule in apply:
            if rules_apply[rule][0] in buff_str:
                flag = True
                buff_str = apply_rule(buff_str, rules_apply[rule])
        if flag:
            continue
        else:
            break
    return buff_str


def print_derivation_in_file(num):
    init_string = init_rules(num)
    applied_string = apply_rules(init_string)
    if applied_string.startswith('#t'):
        der_file = open('derivation.txt', 'w')
        print('Prime number:', num, file=der_file)
        print('Derivation:', file=der_file)
        for j in range(1, len(derivation) + 1):
            print('{}.'.format(j), derivation[j - 1], file=der_file)
        der_file.close()
        print('Derivation is placed in file "derivation.txt"')
    else:
        print('Number {} is not prime'.format(num))


number = input('Prime number: ')
print_derivation_in_file(int(number))
