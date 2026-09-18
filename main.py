file = "books.txt"


def nom_unshih():
    nomnuud = []

    with open(file, "r", encoding="utf-8") as f:
        for mur in f:
            if not mur.strip():
                continue

            turul, ner, une = mur.strip().split(",")
            nomnuud.append([turul, ner, une])

    return nomnuud

def buh_nom():
    nomnuud = nom_unshih()

    for i in range(len(nomnuud)):
        turul, ner, une = nomnuud[i]
        print(f"{i + 1}) {turul} - {ner} - {une}₮")


def nom_haih():
    nomnuud = nom_unshih()
    haih = input("Хайх номын нэр: ").strip().lower()

    if not haih:
        print("Нэр оруулна уу.")
        return

    oldson = False

    for turul, ner, une in nomnuud:
        if haih in ner.lower():
            print(f"{turul} - {ner} - {une}₮")
            oldson = True

    if not oldson:
        print("Ном олдсонгүй.")



def nom_nemeh():
    turluud = [
        "Уран зохиол",
        "Түүх",
        "Шинжлэх ухаан",
        "Танин мэдэхүй",
        "Сурах бичиг"
    ]

    for i in range(len(turluud)):
        print(f"{i + 1}) {turluud[i]}")

    songolt = input("Төрлийн дугаар: ").strip()

    turul = turluud[int(songolt) - 1]
    ner = input("Номын нэр: ").strip()
    une = input("Номын үнэ: ").strip()

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"\n{turul},{ner},{une}\n")

    print("Ном нэмэгдлээ!")



def nom_ustgah():
    nomnuud = nom_unshih()

    if not nomnuud:
        print("Ном байхгүй байна.")
        return

    buh_nom()
    dugaar = int(input("Устгах номын дугаар: ").strip())

    if dugaar < 1 or dugaar > len(nomnuud):
        print("Буруу дугаар.")
        return

    del nomnuud[dugaar - 1]

    with open(file, "w", encoding="utf-8") as f:
        for turul, ner, une in nomnuud:
            f.write(f"{turul},{ner},{une}\n")

    print("Ном устгагдлаа!")


while True:
    print("\n====== НОМЫН БҮРТГЭЛ ======")
    print("1. Бүх ном харах")
    print("2. Ном хайх")
    print("3. Ном нэмэх")
    print("4. Ном устгах")
    print("0. Гарах")

    songolt = input("->>>").strip()

    if songolt == "1":
        buh_nom()
    elif songolt == "2":
        nom_haih()
    elif songolt == "3":
        nom_nemeh()
    elif songolt == "4":
        nom_ustgah()
    elif songolt == "0":
        print("Баярлалаа!")
        break
    else:
        print("Буруу сонголт.")