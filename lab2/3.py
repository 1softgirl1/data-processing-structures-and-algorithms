def del_all_e(s, e):
    if s == '':
        return ''
    if s[0] == e:
        return del_all_e(s[1:], e)
    else:
        return s[0]+ del_all_e(s[1:], e)


print(del_all_e('мама мыла раму', 'а'))
