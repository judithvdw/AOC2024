def do_instruction(instruction, pointer, combo, registers, output):
    A, B, C = registers
    operands = {0: 0, 1: 1, 2: 2, 3: 3, 4: A, 5: B, 6: C, 7: None}
    match instruction:
        case 0:  # adv
            A = A // 2 ** operands[combo]
        case 1:  # bxl
            B = B ^ combo
        case 2:  # bst
            B = operands[combo] % 8
        case 3:
            if A == 0:
                pass
            else:
                pointer = combo
        case 4:
            B = B ^ C
        case 5:
            output.append(operands[combo] % 8)
        case 6:
            B = A // 2 ** operands[combo]
        case 7:
            C = A // 2 ** operands[combo]

    return (A, B, C), pointer, output


# big test
registers = (729, 0, 0)
raw_instructions = "0,1,5,4,3,0"

pointer = 0
instructions = tuple(map(int, raw_instructions.split(',')))
output = []

while pointer < len(instructions) - 1:
    registers, new_pointer, output = do_instruction(instructions[pointer], pointer, instructions[pointer + 1],
                                                    registers, output)
    if new_pointer == pointer:
        pointer += 2
    else:
        pointer = new_pointer

print(",".join(map(str, output)))
