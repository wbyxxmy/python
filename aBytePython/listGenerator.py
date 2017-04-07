# -*- coding: utf-8 -*-

L1 = ['Hello','World',18,'Apple',None]

L2 = [v.lower() for v in L1 if isinstance(v, str)]

print(L1)
print(L2)