def xu_ly_tinh_toan():
    def generate_number():
        import random
        return random.randint(1, 55)

    danh_sach = [generate_number(), generate_number()]
    print(danh_sach)

xu_ly_tinh_toan()
