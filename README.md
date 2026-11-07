# PhotoCraft TH — โปรแกรมแต่งภาพภาษาไทยสำหรับ Mac และ Windows

[ดาวน์โหลด DMG / Download](https://github.com/tapanapon-com/photocraft-th/releases/tag/v0.21.0-th.1) · [วันละ Craft / One Per Craft](https://tapanapon.com/one-per-craft) · [English](#english)

PhotoCraft TH เป็นรุ่นปรับแต่งภาษาไทยของ [PhotoCraft โดย storytold](https://github.com/storytold/photocraft) โปรแกรมแก้ไขภาพแบบเนทีฟที่เขียนด้วย Rust ใช้ egui/wgpu สำหรับหน้าจอและการแสดงผล เหมาะสำหรับทดลองทำงานกับภาพ เลเยอร์ มาสก์ แปรง และข้อความ โดยใช้เมนูภาษาไทย

**โครงการนี้เป็นงานแปลอิสระ ไม่ใช่รุ่นทางการหรือผลิตภัณฑ์ที่ได้รับการรับรองจากผู้สร้าง PhotoCraft/ArtCraft ต้นฉบับ** โค้ดเอนจินและคุณสมบัติหลักเป็นผลงานของโครงการต้นฉบับ

## ภาพหน้าจอ

ภาพจากแอป macOS รุ่นภาษาไทย ใช้เอกสารสาธิตที่สร้างขึ้นสำหรับโครงการนี้

![พื้นที่ทำงาน PhotoCraft ภาษาไทย พร้อมเลเยอร์และข้อความไทย](docs/images/th/photocraft-th-workspace.png)

![หน้าต่างสร้างเอกสารใหม่ของ PhotoCraft ภาษาไทย](docs/images/th/photocraft-th-new-document.png)

## ทำอะไรได้บ้าง

- แก้ไขภาพด้วยเลเยอร์ มาสก์ เครื่องมือเลือก แปรง และการปรับสีตามความสามารถของ PhotoCraft ต้นฉบับ
- เพิ่มข้อความไทยด้วยฟอนต์ Noto Sans Thai ที่แนบในรุ่นติดตั้ง
- บันทึกเอกสาร `.pcraft` เพื่อกลับมาแก้ไข และส่งออกภาพ เช่น PNG
- ใช้ CLI และระบบคำสั่งอัตโนมัติของต้นฉบับ โดยรหัสคำสั่งยังคงเดิม
- เลือก **PhotoCraft › Language › ไทย** และสลับกลับภาษาอังกฤษได้

หน้าจอส่งคำสั่งไปยังเอนจินภาพเดียวกับ CLI คำแปลอยู่ใน `crates/ui-egui/src/i18n/th.tsv` และฝังในแอปตอน build จึงแสดงภาษาไทยได้โดยไม่ต้องเชื่อมต่ออินเทอร์เน็ต การแปลไม่เปลี่ยนรูปแบบไฟล์หรือวิธีคำนวณสี

## ดาวน์โหลดและติดตั้งบน Mac

รุ่น **0.21.0-th.1** สำหรับ **Apple Silicon (arm64)** เท่านั้น ขนาดประมาณ **126.6 MiB** ทดสอบบน macOS 26.3.1

1. [ดาวน์โหลด PhotoCraft TH DMG](https://github.com/tapanapon-com/photocraft-th/releases/download/v0.21.0-th.1/PhotoCraft-TH-0.21.0-th.1-macOS-arm64.dmg)
2. เปิด DMG แล้วลาก **PhotoCraft.app** ไปยัง **Applications** หากมี PhotoCraft เดิม ให้บันทึกงานและปิดแอปก่อนแทนที่
3. เปิดแอป แล้วเลือก **PhotoCraft › Language › ไทย**

รุ่นนี้เซ็นแบบ **ad-hoc** และ **ยังไม่ผ่าน Apple notarization** macOS อาจแจ้งเตือนเมื่อเปิด หากตรวจสอบแหล่งที่มาแล้ว ให้ใช้ตัวเลือก Open Anyway ใน System Settings › Privacy & Security ตามที่ macOS แสดง ไม่จำเป็นต้องปิดระบบรักษาความปลอดภัยทั้งเครื่อง

SHA-256:

```text
0162006f4c344ad80bbfb6127a2ab967c332f91b54fc83c840237c5de0c91828
```

## ดาวน์โหลดและติดตั้งบน Windows

รุ่น x64 มีทั้ง MSI และ portable ZIP:

1. เปิด [หน้า Releases](https://github.com/tapanapon-com/photocraft-th/releases/tag/v0.21.0-th.1) แล้วเลือก `photocraft-0.21.0-th.1-windows-x64.msi`
2. เปิด MSI และทำตามขั้นตอนติดตั้ง จากนั้นเปิด PhotoCraft และเลือก Language › ไทย
3. หากใช้ portable ให้แตก `photocraft-0.21.0-th.1-windows-x64-portable.zip` ทั้งโฟลเดอร์ แล้วเปิด `photocraft.exe` โดยเก็บ `portable.txt` ไว้ข้างแอป

แพ็กเกจ Windows ยังไม่เซ็นด้วยใบรับรอง ตรวจชื่อ repository และ SHA-256 ในหน้า release ก่อนเปิด CLI อยู่ในโฟลเดอร์เดียวกับแอปชื่อ `photocraft-cli.exe`

## ขอบเขตคำแปลและข้อจำกัด

ตารางภาษาไทยมี **4,726 รายการ** เครื่องมือตรวจคีย์จากโค้ดรายงาน **2,361/2,361** ทดสอบภาษาและการสลับภาษาผ่าน **63 รายการ** และ integration ผ่าน **191 รายการ** ตัวเลขความครอบคลุมไม่ได้หมายความว่าทุกข้อความของระบบปฏิบัติการเป็นภาษาไทย

คำแปลใช้ข้อความร่วมและร่างที่ช่วยแปลด้วยโมเดลภาษาในเครื่อง แล้วปรับคำศัพท์และตรวจรูปแบบ ข้อความวินิจฉัยจากเอนจิน/ไลบรารีบางส่วนยังเป็นอังกฤษ ชื่อไฟล์และเลเยอร์ของผู้ใช้ไม่ถูกแปล แก้ปัญหาการเลือกฟอนต์เดิมแล้ว ชุดทดสอบ UI และ integration ผ่านรวม **5,513 รายการ** (ข้าม 23 รายการตามต้นฉบับ) ดู [ผลตรวจรุ่นนี้](docs/validation-0.21.0-th.1.json) และ [Version Log](docs/version-log.md)

## ใช้ซอร์สจาก GitHub

Source ZIP และ `git clone` เป็นซอร์สโค้ด ต้อง build ก่อนใช้งาน หากต้องการติดตั้งทันทีให้ใช้ DMG/MSI ในหน้า Releases ดูคำสั่ง build และ MCP สำหรับ Codex/Claude ใน [คู่มือ](docs/localization-th.md)

## ต้นฉบับ สัญญาอนุญาต และการพัฒนาต่อ

- ต้นฉบับ: [storytold/photocraft](https://github.com/storytold/photocraft) รุ่น 0.21.0 ที่ commit [`efb7ebd`](https://github.com/storytold/photocraft/tree/efb7ebd0c0dab1fc108ee4642aa47c22694271a8)
- [README ต้นฉบับ](README-upstream.md), [เครดิตและทรัพยากร](ATTRIBUTION.md), [NOTICE](NOTICE), [MIT](LICENSE-MIT), [Apache-2.0](LICENSE-APACHE)
- โค้ดต้นฉบับและคำแปลใช้ MIT OR Apache-2.0; `LICENSE` ที่สร้างตอนตั้ง repository ใช้กับส่วนที่เจ้าของ repository มีสิทธิ์ให้อนุญาต ไม่แทนที่เครดิตหรือสัญญาอนุญาตต้นฉบับ
- ฟอนต์จาก [storytold/craft-fonts](https://github.com/storytold/craft-fonts) พิน `b076417b5880bd4154bd22f00695b1d28c6bea83` พร้อมใบอนุญาต OFL ในแอป; ชื่อและตราสินค้าต้นฉบับยังอยู่ภายใต้เงื่อนไขของเจ้าของ
- [คู่มือภาษาไทยและวิธี build](docs/localization-th.md)

## English

**PhotoCraft TH is an independent Thai localization of [storytold/photocraft](https://github.com/storytold/photocraft), not an official or endorsed upstream release.** The original PhotoCraft contributors created the image engine and core features. This repository adds Thai interface text, localization checks, a font-query compatibility fix, and Mac/Windows packaging.

### What it does

PhotoCraft is a native Rust image editor with an egui/wgpu interface. It supports image editing workflows involving layers, masks, selections, brushes, color adjustments and text, subject to upstream's documented limitations. Save editable `.pcraft` documents and export flat images such as PNG. The desktop UI, CLI and automation interface share the same command engine.

The Thai catalog is embedded during compilation and works offline. Command IDs, image-processing behavior and document formats retain upstream's implementation. The macOS package includes Noto Sans Thai through the upstream font bundle. Select **PhotoCraft › Language › ไทย** to use Thai, or switch back to English from the same menu.

### Available tools

<h4>🧰 68 tools</h4>
      Move · Artboard · Rectangular and Elliptical Marquee · Single Row Marquee · Single Column Marquee · Lasso · Polygonal Lasso · Magnetic Lasso · Object Selection · Quick Selection · Magic Wand · Crop · Perspective Crop · Slice · Slice Select · Frame · Eyedropper · Color Sampler · Ruler · Note · Count · Remove · Spot Healing Brush · Healing Brush · Patch · Content-Aware Move · Red Eye · Brush · Pencil · Mixer Brush · Color Replacement · Clone Stamp · Pattern Stamp · History Brush · Art History Brush · Eraser · Background Eraser · Magic Eraser · Gradient · Paint Bucket · Blur · Sharpen · Smudge · Dodge · Burn · Sponge · Pen · Freeform Pen · Curvature Pen · Add Anchor Point · Delete Anchor Point · Convert Point · Horizontal and Vertical Type · Horizontal and Vertical Type Mask · Path Selection · Direct Selection · Rectangle · Ellipse · Triangle · Polygon · Line · Custom Shape · Hand · Rotate View · Zoom

### Mac download

[Download PhotoCraft TH 0.21.0-th.1 for Apple Silicon](https://github.com/tapanapon-com/photocraft-th/releases/download/v0.21.0-th.1/PhotoCraft-TH-0.21.0-th.1-macOS-arm64.dmg) — approximately 126.6 MiB, arm64 only, tested on macOS 26.3.1. Open the DMG and drag PhotoCraft to Applications. Save your work and quit any existing PhotoCraft installation before replacing it.

The app is **ad-hoc signed and not Apple-notarized**. macOS may require an explicit Open Anyway choice under Privacy & Security after you verify the source. Do not disable system-wide security protections. The SHA-256 above and the release checksum file identify this exact download.

### Windows download

Open the [Thai release](https://github.com/tapanapon-com/photocraft-th/releases/tag/v0.21.0-th.1). Choose the Windows x64 MSI, run it and follow the installer. For portable use, extract the entire portable ZIP and run `photocraft.exe`; keep `portable.txt` beside it. Select Language › ไทย in the app. These Windows packages are unsigned; verify the repository and release checksum. The CLI is included as `photocraft-cli.exe`.

### Coverage and validation

The catalog has **4,726 entries**, covering **2,361/2,361 source-extracted keys**. **63 localization tests** and **191 integration tests** passed. This is catalog coverage, not a promise that every OS or library diagnostic is translated. Technical names and user document content retain their original text. Translations started from shared strings and a locally machine-assisted draft, followed by terminology and formatting checks.

The previous font-selection failures are fixed. The UI and integration suites passed **5,513 tests**, with 23 ignored upstream tests. See the [current validation](docs/validation-0.21.0-th.1.json) and [version log](docs/version-log.md).

### Source and credits

Based on the complete upstream v0.21.0 tag, revision `efb7ebd0c0dab1fc108ee4642aa47c22694271a8`. Mac executables were built from `a66d18014` (source/localization commit `32d45190b`); subsequent commits add packaging records, documentation and screenshots. Windows build provenance is recorded in the release validation.

Read the [upstream README](README-upstream.md), [attribution](ATTRIBUTION.md), [MIT](LICENSE-MIT) and [Apache-2.0](LICENSE-APACHE) notices. Retain original copyright and asset licenses when redistributing. The repository-initialization `LICENSE` does not replace upstream notices. Upstream branding is subject to its own terms.

For build instructions, see the [bilingual localization guide](docs/localization-th.md). Product news and downloads are collected at [One Per Craft by Tapanapon](https://tapanapon.com/one-per-craft).
