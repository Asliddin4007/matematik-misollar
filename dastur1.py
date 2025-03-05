import random

print("📌 Eslatma: login = admin, parol = parol")
login = "admin"
parol = "parol"
sna = 1  # Urinishlar soni

ishoralar = ["*", "/", "+", "-"]
sanagich = 1
xatolar = 0
togrilar = 0

# 🔒 LOGIN KIRITISH
while True:
    login_t = input("🔑 Login: ")
    parol_t = input("🔐 Parol: ")
    
    if login == login_t and parol == parol_t:
        print("✅ Siz tizimga kirdingiz! ")
        break
    else:
        print("📛❗ Login yoki parol xato")
        sna += 1
        if sna == 2:
            print("⚠️ 2-urinish qildi")
        elif sna == 3:
            print("⚠️ 3-urinish qildi")
        elif sna == 4:
            print("⛔ Sizda urinishlar soni tugadi!")
            parol = input("🆕 Yangi parol kiriting (yodda tuting): ")
            sna = 1  # Urinishlarni qayta boshlash

# 📌 SINFI ANIQLASH
while True:
    try:
        aniqlash = int(input("📚 Nechanchi sinfsiz: "))
        if 1 <= aniqlash <= 4:
            m = 9
            break
        elif 5 <= aniqlash <= 8:
            m = 99
            break
        elif 9 <= aniqlash <= 11:
            m = 999
            break
        else:
            print("🚫 Bunday sinf yo‘q! Boshqattan kiriting.")
    except ValueError:
        print("⚠️ Iltimos, faqat son kiriting!")

# 🔢 MATEMATIKA MISOLLARI
while True:
    a = random.randint(1, m)
    b = random.randint(1, m)
    ishora = random.choice(ishoralar)

    # Nolga bo‘lishdan qochish
    if ishora == "/" and b == 0:
        continue  

    # To‘g‘ri javobni hisoblash
    if ishora == "+":
        togri_javob = a + b
    elif ishora == "-":
        togri_javob = a - b
    elif ishora == "*":
        togri_javob = a * b
    elif ishora == "/":
        togri_javob = round(a / b, 2)  # 2 xonali kasr qismi bilan

    # 📝 Foydalanuvchidan javob olish
    javob = input(f"{sanagich}) {a} {ishora} {b} = ")
    sanagich += 1

    # 🛑 Agar foydalanuvchi `stop` yozsa, dastur tugaydi
    if javob.lower() == "stop":
        umumiy = togrilar + xatolar
        if umumiy > 0:
            foyiz = round((togrilar / umumiy) * 100, 2)
            print(f"\n📊 Dastur tugadi.\n✅ To‘g‘ri javoblar: {togrilar} ({foyiz}%)\n❌ Xato javoblar: {xatolar}")
        else:
            print(f"\n📊 Dastur tugadi.\n✅ To‘g‘ri javoblar: {togrilar}\n❌ Xato javoblar: {xatolar}")

        # 💬 Hayrlashish
        while True:
            hayr = input("👋 Hayr deb yozing: ").lower()
            if hayr == "hayr":
                print("👋 Hayr! Dasturdan chiqildi.")
                break
        break

    # 🎯 Foydalanuvchining javobini tekshirish
    else:
        try:
            if float(javob) == togri_javob:
                print("✅ To‘g‘ri!")
                togrilar += 1
            else:
                print(f"❌ Xato! To‘g‘ri javob: {togri_javob}")
                xatolar += 1
        except ValueError:
            print("⚠️ Iltimos, son kiriting yoki 'stop' yozib chiqib keting.")
