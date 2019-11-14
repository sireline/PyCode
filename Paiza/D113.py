h, m = [int(n) for n in input().split(":")]
print(f"{h-8}:{m}" if h >= 8 else f"{h+16}:{m}")
