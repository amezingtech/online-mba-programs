# Microsoft Store — Submission Kit (ready to upload)

Everything except the Partner Center clicks is done. Live app:
**https://amezingtech.github.io/online-mba-programs/**

## ✅ Already prepared (in `store-package/`, NOT committed to the public repo)

| Item | File |
|---|---|
| **Store package** (upload this) | `store-package/Online MBA Programs.zip` → contains `Online MBA Programs.msixbundle` |
| Sideload/test build | same zip → `Online MBA Programs.sideload.msix` + `install.ps1` |
| Legacy Windows build | `Online MBA Programs.classic.appxbundle` (only if Partner Center asks) |
| Screenshots (1440×2000, 6 screens) | `store-package/screenshots/01…06.png` |

**Package identity (verified inside the .msixbundle):**
- Name: `com.amezingtech.onlinembaprograms`
- Publisher: `CN=33A0F994-6DF4-4058-9B1C-9C108074FC34` ← your existing Amezing Tech Satara Partner Center identity
- Display name: `Online MBA Programs` · Publisher display: `Amezing Tech Satara` · Version `1.0.1.0`

## 👉 Your steps in Partner Center (~15 minutes)

1. **https://partner.microsoft.com/dashboard** → sign in with the account used for
   Watch Cartoon Online (Amezing Tech Satara).
2. **Apps and Games → New product → New app** → reserve the name:
   **`Online MBA Programs`**
   (if taken: `Online MBA Programs 2026` — then tell me and I'll regenerate the
   package with the new name; takes 2 minutes).
3. **Start submission** → **Packages** → upload
   `store-package/Online MBA Programs.zip/Online MBA Programs.msixbundle`.
   It should pass validation with no warnings (identity matches your publisher).
4. **Store listing** — copy-paste from below. Upload the 6 screenshots.
5. **App categories**: Primary `Education`, Secondary `Business`.
   Age ratings: questionnaire, no restricted content → 3+.
6. **Submit for certification** — PWAs of this type typically pass in **1–3 business days**.

## Store listing copy (paste-ready)

**Description (short search term field — 30 keywords max):**
`online mba, mba online, online mba fees, online degree, online bba, online mca, distance mba, mba admission, dy patil online mba, online mba india`

**Description:**
```
Online MBA 2026 — the complete guide to DPU Pune's online degree programs.

Get every detail of all 8 UGC-entitled, NAAC A++ online programs from Dr. D. Y. Patil Vidyapeeth, Pune — Centre for Online Learning:

• Online MBA — ₹1,89,400 total, 18 specializations, 102 credits, no entrance exam
• Online MCA — ₹1,40,000, AI-ML / Blockchain / FinTech tracks
• Online M.Com — ₹1,30,000, ideal with CA/CS prep
• Online BBA — ₹1,45,400, start after 12th
• Online BCA — ₹1,25,000, job-ready IT degree
• Online B.Com — ₹75,000, India's best-value commerce degree
• 6-month certificates in Digital Marketing & Hospital Management — ₹28,000

EVERY PROGRAM INCLUDES: semester-wise fee tables, full syllabus, eligibility,
career outcomes and FAQs — plus the complete Online MBA guide: fees comparison
vs Jain, Amity, Manipal, LPU & Symbiosis; is an online MBA valid in India;
online vs regular vs distance MBA; and which specialization has the best scope.

ADMISSION MADE SIMPLE: 5-step process, interactive document checklist,
eligibility quick-check for every program, and free counseling on WhatsApp from
authorised DPU-COL academic advisors — +91 77096 45632.

Features:
• All 8 programs with full details — fees, syllabus, specializations, careers
• 18 MBA specializations with career roles for each
• Fee comparison table — DPU vs India's top online MBA universities
• Online MBA validity, worth-it analysis & specialization scope guide
• Interactive document checklist for admission
• EMI & scholarship information
• Direct WhatsApp counseling — free, official channel
• Works offline after first load

An Amezing Tech Academic Advisors (Satara) initiative — official counseling
partner for DPU-COL. Admission, delivery and examinations are solely managed
by the university. Fees as per current prospectus; confirm at admission.
```

**What's new in this version:** `Initial release — Online MBA 2026 programs guide.`

**Search terms field:** `online mba, online mba fees, online mba india, mba online, online degree, dy patil online, online bba, online mca, online bcom, distance mba`

**Category:** Education (primary) · Business (secondary)

**Privacy policy URL:** `https://amezingtech.github.io/online-mba-programs/privacy-policy.html`
**Website:** `https://onlinembadegreeprograms.org`
**Support contact:** phone `+91 77096 45632` · email your advisor address

## Why you never repackage
Store-installed PWAs load live from the website — updates go out by pushing to
GitHub (`git add -A && git commit -m "update" && git push`), no new Store submission needed.

## After certification
Send me the Store link — I'll add it to the app footer, the README and the website.
