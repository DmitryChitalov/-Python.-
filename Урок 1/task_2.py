a = 5
print("%d = %s" % (a, bin(a)))#в двоичном предсталении
b = 6
print("%d = %s" % (b, bin(b)))#в двоичном предсталении

print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))#в розряде стоит ниже
print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))#в розряде стоит выше
print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
print("%d << 2 = %d (%s)" % (a, a << 2, bin(a << 2)))#при побитовом сдвиге 00 сдвингаются в определенныую сторону добаляя разряды или наооборот
print("%d >> 2 = %d (%s)" % (a, a >> 2, bin(a >> 2)))
input("Press any to exit...")