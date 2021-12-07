s = 'AAAAACCCCCAAAAACCCCCCAAAAATTTGGGCCCCTTTGGG'
s2 = 'AAAAAAAAAAAAAAAAA'
s3 = "AAAAACCCCCAAAAAGCCCCCCAAAAACCCCCAAAAAGGGTTT"
def fun(str_in):
    if len(str_in) < 0 or len(str_in) > 1 * 10 ** 5:
        print('字符串长度不符要求')
        return
    set_out = {}
    for i in range(len(str_in)):
        if i <= len(str_in) - 10:
            part_s = str_in[i:i + 10:]
            # print(part_s)
            if part_s in str_in[i + 1:]:
                # print(part_s)
                set_out.setdefault(part_s)
    list_out = list(set_out)
    return list_out

print(fun(s3))
