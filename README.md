# Counter-Strike O'yini: OOP Tushunchalarini O'rganish

Ushbu hujjatda Counter-Strike o'yinining asosiy ishlash tartibi bayon etiladi va obyektga yo'naltirilgan dasturlash (OOP) tamoyillaridan foydalanib o'yinni qanday modellashtirish mumkinligi tushuntiriladi. Asosiy e'tibor **Counter**, **Terror**, **Player** va **Weapon** obyektlariga qaratiladi. Ushbu yondashuv orqali siz ushbu obyektlar o'rtasidagi munosabatlarni va ularning o'yindagi vazifalarini tushunasiz.

---

## O'yinning Asosiy Komponentlari

### **1. Player**
**Tavsif:** Player - foydalanuvchi tomonidan boshqariladigan asosiy xarakter. Har bir playerning o'ziga xos xususiyatlari va o'yin davomida bajarishi mumkin bo'lgan harakatlari mavjud. Player ikkita jamoalardan biriga tegishli bo'ladi: Counter-Terrorists yoki Terrorists.

#### **Xususiyatlari:**
- **name**: Playerning ismi yoki identifikatori.
- **team**: Playerning qaysi jamoaga tegishli ekanligini ko'rsatadi.
- **score**: Playerning harakatlar (masalan, dushmanlarni yo'q qilish, bomba qo'yish/zararsizlantirish) orqali yig'ilgan ochkolari.
- **weapon**: Player tomonidan foydalanilayotgan qurol.

#### **Metodlari (Harakatlari):**
- **shoot(target)**: Player dushmanga qarata o'q uzadi va uning sog'lig'iga zarar yetkazadi.
- **move(location)**: Playerni xaritada yangi joyga ko'chiradi.

### **2. Counter (Counter-Terrorist)**
**Tavsif:** Counter-Terrorist (CT) - Playerning bir turi bo'lib, asosiy vazifasi Terroristlarni bomba qo'yishdan to'xtatish va agar bomba qo'yilgan bo'lsa, uni zararsizlantirishdir.

#### **Xususiyatlari:**
- **name**: Counter-Terrorist playerning ismi.
- **team**: "Counter-Terrorists" deb belgilangan.
- **score**: Counter-Terrorist player yig'ilgan ochkolar.
- **weapon**: Counter-Terrorist foydalanayotgan qurol.

#### **Metodlari (Harakatlari):**
- **shoot(target)**: Dushman playerga (odatda Terrorist) qarata o'q uzadi.
- **defuse()**: Terrorist tomonidan qo'yilgan bombani zararsizlantirish harakatini bajaradi.

#### **Maqsadi:**
- Barcha Terroristlarni yo'q qilish.
- Qo'yilgan bombani zararsizlantirish.

### **3. Terror (Terrorist)**
**Tavsif:** Terrorist - Playerning bir turi bo'lib, asosiy vazifasi bombani qo'yish va Counter-Terroristlarning uni zararsizlantirishiga yo'l qo'ymaslikdir.

#### **Xususiyatlari:**
- **name**: Terrorist playerning ismi.
- **team**: "Terrorists" deb belgilangan.
- **score**: Terrorist player yig'ilgan ochkolar.
- **weapon**: Terrorist foydalanayotgan qurol.

#### **Metodlari (Harakatlari):**
- **shoot(target)**: Dushman playerga (odatda Counter-Terrorist) qarata o'q uzadi.
- **plant()**: Bombani xaritaning belgilangan joyida qo'yadi.

#### **Maqsadi:**
- Barcha Counter-Terroristlarni yo'q qilish.
- Bombani muvaffaqiyatli qo'yib, uni portlashini ta'minlash.

### **4. Weapon**
**Tavsif:** Weapon - bu o'yinchilar jangda foydalanadigan vositani ifodalovchi obyekt. Har xil qurollarning turli atributlari va ta'sirlari mavjud.

#### **Xususiyatlari:**
- **name**: Qurolning nomi (masalan, "AK-47", "M4A1").
- **damage**: Har bir o'q bilan dushmanning sog'lig'idan olib tashlanadigan ball.
- **ammo**: Quroldagi qolgan o'q soni.

#### **Metodlari (Harakatlari):**
- **reload()**: Qurolni o'qlar bilan qayta to'ldiradi.
- **fire()**: O'q uzadi, o'q sonini kamaytiradi va dushmanga zarar yetkazadi.

---

## OOP Tushunchalari

### **1. Klasslar va Obyektlar**
- **Klass:** Bu obyektlarning tuzilishi va xatti-harakatlarini belgilovchi shablon (masalan, Counter, Terror, Weapon).
- **Obyekt:** Klassning aniq bir qiymatlarga ega nusxasi (masalan, "Ali" ismli AK-47 bilan qurollangan Terrorist).

### **2. Xususiyatlar va Metodlar**
- **Xususiyatlar:** Bu obyektlarning atributlarini belgilaydi (masalan, `name`, `team`, `weapon`).
- **Metodlar:** Bu obyektlarning bajarishi mumkin bo'lgan harakatlarni belgilaydi (masalan, `shoot()`, `plant()`).

### **3. Inkapsulyatsiya**
- Inkapsulyatsiya obyektning ma'lumotlarini (xususiyatlarini) faqat aniq metodlar orqali kirish mumkin bo'lishini ta'minlaydi. Masalan, playerning score qiymati faqat ma'lum harakatlar orqali yangilanadi.

### **4. Merosxo'rlik**
- Counter va Terror klasslari Player klassidan umumiy xususiyatlar va metodlarni meros qilib oladi. Bu kodni takrorlashni oldini oladi va tizimni boshqarishni osonlashtiradi.

### **5. Polimorfizm**
- Polimorfizm turli obyektlarning bir xil nomdagi metodlarni (masalan, `shoot()`) turli kontekstlarda turlicha ishlatishiga imkon beradi. Masalan, Counter dushmanini o'ldirish uchun, Terror esa hujum qilish uchun o'q uzadi.

### **6. Abstraktsiya**
- Abstraktsiya murakkab implementatsiyani yashirib, foydalanuvchi uchun oddiy interfeys taqdim etadi. Masalan, player `defuse()` metodini chaqiradi, lekin uning ichki logikasini bilishi shart emas.

---

## O'yin Oqimi
1. **Tayyorlanish:** Playerlar Counter-Terrorists yoki Terrorists jamoalariga ajratiladi.
2. **Harakat:** Playerlar xaritada harakatlanadi, jang qiladi (`shoot()` metodidan foydalanadi) va vazifalarni bajaradi (masalan, `plant()` yoki `defuse()`).
3. **Ochko:** Playerlar harakatlariga qarab ochkolar to'playdi, masalan, dushmanlarni yo'q qilish yoki vazifalarni bajarish orqali.
4. **G'alaba Sharti:**
   - Counter-Terrorists barcha Terroristlarni yo'q qilsa yoki bombani zararsizlantirsa g'alaba qozonadi.
   - Terrorists barcha Counter-Terroristlarni yo'q qilsa yoki bombani muvaffaqiyatli portlatsa g'alaba qozonadi.

---
