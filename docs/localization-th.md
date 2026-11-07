# PhotoCraft ภาษาไทย / Thai localization

รุ่นปรับแต่งนี้เพิ่มภาษาไทยให้ PhotoCraft โดยแยกจาก FilmCraft และคงระบบแก้ไขภาพของต้นฉบับไว้ ใช้เมนู **PhotoCraft › Language › ไทย** เพื่อเลือกภาษาไทย หรือกำหนด `interface.language` เป็น `th` รองรับรหัสภูมิภาค `th-TH` และ `th_TH.UTF-8` ด้วย

## ต้นฉบับและเครดิต

- PhotoCraft: https://github.com/storytold/photocraft
- ฐานต้นฉบับ: `efb7ebd0c0dab1fc108ee4642aa47c22694271a8` (0.21.0)
- โค้ดและคำแปลใหม่: MIT OR Apache-2.0 ตามสัญญาอนุญาตของโครงการ
- คำแปลร่วมบางส่วนมาจากงานภาษาไทยใน FilmCraft และ craft-i18n ซึ่งอยู่ภายใต้ MIT OR Apache-2.0
- นี่เป็นรุ่นปรับแต่งภาษาไทย ไม่ใช่รุ่นทางการหรือรุ่นที่ได้รับการรับรองจากผู้สร้างต้นฉบับ

## วิธีทำงาน

PhotoCraft เป็นโปรแกรมแก้ไขภาพแบบเนทีฟ เขียนด้วย Rust และแสดงผลด้วย egui/wgpu เมนู เครื่องมือ และระบบควบคุมอัตโนมัติเรียกใช้คำสั่งจากเอนจินเดียวกัน การแปลนี้เปลี่ยนข้อความแสดงผลโดยไม่เปลี่ยนรหัสคำสั่ง รูปแบบไฟล์ หรือการคำนวณสี

คำแปลเก็บใน `crates/ui-egui/src/i18n/th.tsv` โดยแต่ละบรรทัดมีบริบท ข้อความต้นฉบับ และคำแปล คีย์ `@id` ใช้สำหรับคำสั่งที่ต้องแยกความหมาย ส่วน `@plural` ใช้คำไทยรูปเดียวสำหรับทุกจำนวน ระบบบีบอัดตารางคำแปลลงในแอปขณะสร้าง จึงไม่ต้องเชื่อมต่ออินเทอร์เน็ตเพื่อแสดงภาษาไทย

รุ่นติดตั้งใช้ชุด craft-fonts ตามพินของต้นฉบับ (`b076417b5880bd4154bd22f00695b1d28c6bea83`) รวม Noto Sans Thai และแนบสัญญาอนุญาต OFL ระบบยังรองรับฟอนต์สำรองของ macOS ด้วย ไม่มีการคัดลอกไฟล์ฟอนต์เข้ามาใน repository นี้

คำแปลเริ่มจากข้อความร่วมและร่างที่ช่วยแปลด้วยโมเดลภาษาในเครื่อง จากนั้นปรับคำศัพท์เฉพาะและตรวจตัวแปร ตัวเลข และรูปพหูพจน์ ชื่อผลิตภัณฑ์ รูปแบบไฟล์ ปุ่มลัด และคำย่อทางเทคนิคบางรายการคงภาษาเดิม ข้อความวินิจฉัยบางส่วนจากเอนจิน ระบบปฏิบัติการ หรือไลบรารีภายนอกอาจยังเป็นภาษาอังกฤษ

## ตรวจสอบและแก้ไข

```sh
export CRAFT_FONTS_DIR="$PWD/../craft-fonts"
export CRAFT_FONTS_REQUIRED=1
python3 scripts/thai/validate.py
cargo test --locked -p photocraft-ui-egui
cargo clippy -p photocraft-ui-egui --all-targets -- -D warnings
cargo xtask layers
cargo xtask wasm
```

ตัวตรวจ Python เปรียบเทียบความครอบคลุมกับคีย์ทั้งหมดในตารางภาษาอื่น และตรวจตัวแปร `{name}` ตัวเลข เครื่องหมาย `…` และรูปพหูพจน์ การทดสอบ Rust ตรวจการเลือกภาษาไทยและการสลับภาษาขณะเปิดเอกสาร

## English

This independently modified build adds Thai to PhotoCraft, a native Rust image editor based on [storytold/photocraft](https://github.com/storytold/photocraft), revision `efb7ebd0c0dab1fc108ee4642aa47c22694271a8` (0.21.0). It is separate from the FilmCraft localization and is not an official upstream release.

Select **PhotoCraft › Language › ไทย** in the macOS menu bar, or set `interface.language` to `th`. Regional Thai locale identifiers also resolve to Thai. Translations are embedded at build time and work offline. Command identifiers, document formats and image-processing behavior remain upstream's implementation.

The catalog combines shared MIT/Apache-licensed Thai strings with locally machine-assisted translations and terminology corrections. Automated checks cover reference-catalog coverage, placeholders, numeric values, ellipses and Thai plural forms. Technical names and some engine diagnostics or external system errors may remain in English. The packaged build embeds upstream craft-fonts at revision `b076417b5880bd4154bd22f00695b1d28c6bea83`, including Noto Sans Thai, and includes OFL license notices. macOS system fallback remains available. Font files are kept in the separate craft-fonts checkout, not this repository.

Retain the upstream license, NOTICE and asset attribution when redistributing. Locally ad-hoc-signed builds are not Apple-notarized releases.

## ความครอบคลุม / Coverage

ตารางภาษาไทยมี **4,726 รายการ** ครอบคลุมคีย์อ้างอิงทั้งหมด และตัวสแกนซอร์สรายงาน **2,361/2,361 (100%)** ไม่พบคีย์ไทยที่ขาด เพิ่มคำแปล 99 รายการจากรุ่นก่อนหน้า การนับนี้ไม่รวมข้อความที่ไม่ผ่านระบบแปลของแอปจากระบบปฏิบัติการหรือไลบรารีภายนอก

The catalog contains **4,726 entries** and covers **2,361/2,361 source-derived keys (100%)**. It adds 99 translations over the previous Thai release. This measures the app's localization catalog, not every OS or third-party diagnostic. See [current validation](validation-0.21.0-th.1.json).

## สร้างแอป / Build the app

```sh
export CRAFT_FONTS_DIR="$PWD/../craft-fonts"
export CRAFT_FONTS_REQUIRED=1
cargo build --release --locked -p photocraft -p photocraft-cli --features heif
bash scripts/thai/package-local.sh
```

DMG อยู่ใน `dist/thai/` เปิดไฟล์แล้วลาก PhotoCraft ไปยัง Applications รุ่นที่สร้างในเครื่องใช้ลายเซ็น ad-hoc และยังไม่ผ่าน Apple notarization รองรับสถาปัตยกรรมของเครื่องที่ใช้สร้างเท่านั้น

The DMG is written to `dist/thai/`. Open it and drag PhotoCraft to Applications. This local build is ad-hoc signed, not Apple-notarized, and supports only the architecture it was built for.

ผลตรวจและข้อจำกัดของชุดทดสอบ / Test results and remaining failures: [validation-th.md](validation-th.md).

## อัปเกรด 7 พฤศจิกายน 2026

รวมซอร์สต้นฉบับรุ่นใหม่และคงชุดแปลภาษาไทย ดูสถานะการตรวจและการแพ็กเกจใน [บันทึกอัปเกรด](thai-upgrade-20261107.md) ก่อนใช้ตัวเลขทดสอบรุ่นเก่าอ้างอิงรุ่นนี้
