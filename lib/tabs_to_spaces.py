def tabs_to_spaces(input):
    lines = input.split('\n')
    split_lines = []
    result_lines = []
    for line in lines:
        if line.startswith('\t'):
            line = line.replace('\t', '    ', 1)
        split_line = line.split('\t')
        split_lines.append(split_line)

    for line in split_lines:
        result_line = ''
        for section in line:
            result_line = f"{section}" if len(result_line) == 0 else f"{result_line}{' ' * (4 - len(result_line) % 4)}{section}"
        result_lines.append(result_line)
    
    result = '\n'.join(result_lines)
    return result

def tab_to_spaces(text):
    return text.expandtabs(4)

# tabs_to_spaces("\tabc\t123\n\t123")
# tabs_to_spaces("a\t123\n\t123")
# tabs_to_spaces("ab\t12")
# tabs_to_spaces("abc\t123\n\t123")
# tabs_to_spaces("a\tbcdef\t1\t23456\nab\tcdef\t123 456\n\tabcdef\t12\t3456\na\tbcdef\t\t12346")
