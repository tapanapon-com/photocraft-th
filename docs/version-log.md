# PhotoCraft TH — Version Log

## 0.21.0-th.1 — 7 November 2026

Based on the complete [upstream v0.21.0 release](https://github.com/storytold/photocraft/releases/tag/v0.21.0), commit `efb7ebd0c0dab1fc108ee4642aa47c22694271a8`.

### การเปลี่ยนแปลงจากต้นฉบับ / Upstream changes

- เพิ่มตัวเลือกบันทึกภาพรวมเอกสารขนาดเต็มลงใน `.pcraft` / Optional full-size flattened document preview: [upstream change](https://github.com/storytold/photocraft/pull/9913).
- ลดการเก็บข้อมูลไฟล์ที่เข้ารหัสซ้ำในหน่วยความจำขณะบันทึก / Avoid duplicating the encoded save buffer: [upstream change](https://github.com/storytold/photocraft/pull/8115).
- ปรับการนำเข้า PSD/PSB และ EXR ให้ทำงานเป็นช่วงที่จำกัดขนาด / Bounded-band PSD/PSB and EXR imports: [upstream change](https://github.com/storytold/photocraft/pull/5331).

The release tag was merged in full. These are selected upstream highlights, credited to their original contributors; they are not new features authored by this Thai project.

### การปรับรุ่นภาษาไทย / Thai edition changes

- เพิ่มคำแปลใหม่ 99 รายการ รวม 4,726 รายการ / Added 99 translations, 4,726 catalog entries total.
- คีย์จากซอร์สครบ 2,361/2,361 / All 2,361 source-derived keys covered.
- แก้การพิมพ์ชื่อฟอนต์เดิมแล้วกด Down ให้คงตัวเลือกที่ตรงกันก่อน / Retyping the current font keeps its exact match on the first Down key.
- เปลี่ยนช่องทางตรวจอัปเดตไปที่ repository รุ่นไทย / Update checks now use the Thai repository.
- แพ็กเกจ Mac และ Windows รวม CLI สำหรับ MCP / Mac and Windows packages include the CLI for MCP.

### ผลตรวจ / Validation

UI and integration: 5,513 passed, 23 ignored. Updater checks: 4 passed. Final localization checks: 63 passed. Clippy, formatting, dependency layers, wasm and HEIF wasm checks passed. See [source validation](validation-0.21.0-th.1.json) and [upgrade notes](thai-upgrade-20261107.md). Platform checks and artifact hashes are recorded with the release after packaging; source coverage does not imply that every upstream feature or external diagnostic has been tested or translated.

Mac packages use ad-hoc signatures and are not notarized. Windows packages are unsigned. Windows CLI/installer checks run on a native Windows CI runner; this does not claim manual testing of every Windows GUI workflow.

## 0.20.1-th.1 — previous release

4,627 Thai entries; 2,272/2,272 source keys. Historical font-selection failures and the original Mac verification are preserved in [the dated report](validation-th.md). They do not describe the current release's results.
