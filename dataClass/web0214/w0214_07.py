# lo.e 정규표현식 형태
# search 비교
# i love you, you live, lofffe, loke, leaeful, live love, from loveless

import re

m_list = ['i love you', 'you live', 'lofffe', 'loke', 'leaeful', 'live love', 'from loveless']

p = re.compile('lo.e')
for mword in m_list:
    m = p.search(mword)
    if m:
        print("매칭 성공")
        print(m.group())
        print(m.string)
        print(m.start())
        print(m.end())
        print(m.span())
    else:
        print("매칭 실패")    

