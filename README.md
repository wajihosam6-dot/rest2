# rest2

> **رِيـــــســـــت | REST Resort — التجربة الرقمية الاستوائية والسينمائية الفاخرة**
> منتجع واستراحة ريست الفاخرة — العمارية، الرياض.

---

## 🌟 نظرة عامة (Overview)

موقع **REST** الرقمي بتصميم سينمائي متكامل وهوية استوائية بحرية راقية، يجمع بين:
- إخراج فني مدروس بدقة (Art Direction) مستوحى من هويات المنتجعات الساحلية الفاخرة (Coastal Azure / Hawaiian Lagoon).
- خط **ثمانية (Thmanyah Font Family)** بكافة أوزانه الـ 15 (Sans, Serif Display, Serif Text) مع مد وتنسيق عربي أصيل (كشيدة راقية).
- حركات وانتقالات فيزيائية سلسة مستندة إلى مبادئ **Remotion Spring Physics**.
- رسومات نباتية تفاعلية بـ SVG (رسم النخلة والوردة الحمراء مع التمرير - Scroll Draw).
- قسم تفاعلي للمواصفات والمساحات مع استجابة كاملة لخاصية السحب والتمرير على الجوال والديسكتوب.
- توافق كامل وتجاوب تام مع كافة الشاشات وأجهزة الجوال (Mobile-First Responsiveness).

---

## 📁 هيكل المشروع (Project Structure)

```
rest2/
├── rest-landing-v5-fixed/       # المجلد الرئيسي للموقع الإلكتروني
│   ├── index.html              # الصفحة الرئيسية بتصميمها السينمائي الكامل
│   └── public/                 # الأصول الرقمية والوسائط
│       └── assets/
│           ├── brand/          # شعارات وهوية ريست الرسمية (SVG)
│           ├── fonts/thmanyah/ # خطوط ثمانية الرسمية بجميع أوزانها (WOFF2)
│           ├── real/           # صور ومقاطع الفيديو الحقيقية للمنتجع
│           ├── hero/           # وسائط الهيروسيكشن المتعددة
│           ├── pools/          # صور ومسارات المسابح
│           ├── interiors/      # صور المرافق والمجالس الداخلية
│           └── garden/         # صور المساحات الخارجية والحدائق
├── rest_logo/                  # ملفات وهوية الشعار المتجهية
├── ABOUT/                      # مستندات وتفاصيل المشروع
└── README.md                   # دليل المشروع
```

---

## 🚀 التشغيل السريع (Quick Start)

يمكنك تشغيل المشروع محلياً عبر أي خادم ويب ثابت (Static Web Server) أو فتحه مباشرة:

### 1. عبر خادم محلي (موصى به لعمل مقاطع الفيديو والخطوط بشكل مثالي):
```bash
# استخدام Python
cd rest-landing-v5-fixed
python -m http.server 8000

# أو استخدام Node.js (npx serve)
npx serve rest-landing-v5-fixed
```
ثم افتح المتصفح على: `http://localhost:8000`

### 2. الفتح المباشر:
فتح ملف `rest-landing-v5-fixed/index.html` في أي متصفح حديث (Chrome, Edge, Safari, Firefox).

---

## 🎨 الهوية البصرية والتقنيات (Tech Stack & Design)

- **Typography**: ثمانية الرسمية (Thmanyah Sans, Serif Display, Serif Text)
- **Palette**: Coastal Azure / Hawaiian Lagoon (ألوان بحرية زاهية خالية من البني الغامق)
- **Motion**: Remotion Spring Physics & Intersection Observers
- **Format**: Zero External Heavy Libraries (Ultra fast load, native modern JavaScript & CSS)
- **Assets**: Optimized WebP & WebM/MP4

