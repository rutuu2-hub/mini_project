def nom_haih():
    print("Уран зохиол")
    print("Түүх")
    print("Шинжлэх ухаан")
    print("Танин мэдэхүй")
    print("Сурах бичиг")

    haih_turul = input("Хайх номын төрөл: ").strip()
    oldson =False

    with open("book.txt", "r" , encoding="utf-8") as f:
        for m in f:
            if not m.strip():
                continue

            turul , ner ,une = m.strip().split(",")

            if haih_turul in turul:
                print(f"{ner}: {une}₮")
                oldson = True
        if haih_turul not in turul:
                print("Тийм төрөл байхгүй байна.")

nom_haih()
