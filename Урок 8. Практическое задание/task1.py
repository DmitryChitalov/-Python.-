import hashlib

def substring(object):
        unique = {}
        for it in range(len(object)-1):
            for words in range(len(object)+1):
                p = "".join(object[it:words])
                h = hashlib.sha1(p.encode('utf-8')).hexdigest()
                if p != "" and p not in unique and p != object:
                    print(p)
                    unique.update({p:h})
        print(f'Итог: {len(unique)} подстрок')
        print(unique)

substring("papa")


