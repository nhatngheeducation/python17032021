lst = [1, 2, 3, 1, 4, 2, 1, 3]
tap_hop = set(lst)
print(tap_hop)
for pt in tap_hop:
    print(pt)

tap_hop_new = {1.2, "Nhat Nghe", 2, 1.2}
print(tap_hop_new)

# Them 1 phan tu
tap_hop_new.add(2003)
print(tap_hop_new) # {1.2, 2, 2003, "Nhat Nghe"}
# Update gia tri
tap_hop_new.update({1,3,5,7})
print(tap_hop_new)
tap_hop_new.remove(2)
print(tap_hop_new)