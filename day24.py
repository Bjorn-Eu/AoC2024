
def get_value(name,variables):
    value = 0
    index = 0
    var = name+f"{index:02}"
    while var in variables.keys():
        print(variables[var],end='')
        value += variables[var]*(2**index)
        index +=1
        var = name+f"{index:02}"
    print('')
    print('The value is of ',name,' is ',value)
    return value




f = open('samples/sample24.txt')
data = (f.read()).split('\n\n')
initial_var = data[0].split('\n')
operations = data[1].split('\n')




variables = {}

for var in initial_var:
    name = var[0:3]
    val = (int)(var[5])
    variables[name] = val


x_val = get_value('x',variables)
y_val = get_value('y',variables)
target_z = x_val + y_val
operations_set = set(operations)

#process instructions
while operations_set:
    to_remove = set()
    for operation in operations_set:
        operands = operation.split()
        var1 = operands[0]
        var2 = operands[2]

        operator = operands[1]

        output = operands[4]
        if var1 in variables.keys() and var2 in variables.keys():
            input1 = variables[operands[0]]
            input2 = variables[operands[2]]
            value = None
            if operator == 'AND':
                value = input1 & input2
            elif operator == 'OR':
                value = input1 | input2
            elif operator == 'XOR':
                value = input1 ^ input2
            variables[output] = value
            to_remove.add(operation)
    operations_set -= to_remove



value = 0
index = 0
var = 'z'+f"{index:02}"
while var in variables.keys():
    print(variables[var],end='')
    value += variables[var]*(2**index)
    index +=1
    var = 'z'+f"{index:02}"

print('')
print('The value is',value)
print('The target value is:',target_z)
print(x_val & y_val)