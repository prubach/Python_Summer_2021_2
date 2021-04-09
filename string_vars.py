s = 'abcdefaa'
print(len(s))
print(s.count('a'))
print(s[1:])
print(s[1:3])
print(s[:2])
print(s[-3:])

s2 = 'abc\n\rdef'
print(s2)

print(ord('a'))

s3 = 'gsgałóóżźćą'
print(s3)


s4 = 'abc\tdef\t\t\tegwg'
print(s4)

s5 = 'abc\td\ef\t\t\te\gw\\tg'
print(s5)
s6 = "agsag'agsg"
s6 = 'agsag\'agsg'
print(s6)
s7 = '    asgsgsag asggs   '

print(s7.strip())

s5_tab = s5.split('\t')
print(s5_tab)