# Online MBA & Degrees — DPU Pune (Programs App)

Information-complete companion app for **onlinembadegreeprograms.org** — all 8
DPU-COL online programs with full details, plus a deep Online MBA guide.
Main keyword: **online mba**.

Every CTA funnels to WhatsApp **+91 77096 45632** with contextual pre-filled text
(generic, per-program, per-specialization, document-checklist status, lead form).

## What's inside (content sourced from the live site)

| Tab | Content |
|---|---|
| **Home** | Hero (Online MBA 2026), stats, 8 reasons to choose DPU-COL, popular programs, spec teaser |
| **Programs** | All 8 programs + compare-at-a-glance fee table |
| **Guide** | Online MBA fees comparison (DPU vs Jain/Amity/Manipal/LPU/Symbiosis/CU/NMIMS), UGC validity, Online vs Regular vs Distance, worth-it analysis, specialization scope ranking, all 18 specializations, MBA FAQs |
| **Admission** | 5-step process, interactive document checklist, eligibility table, fee payment & EMI info |
| **Contact** | Lead form → WhatsApp message, 3 phone numbers, Instagram, website links |

Each program detail view: overview + objectives, fundamentals table, semester-wise
fee table, specializations (MBA/MCA), full semester syllabus, career roles, FAQs,
Apply CTA, related programs.

- Programs: MBA ₹1,89,400 · MCA ₹1,40,000 · M.Com ₹1,30,000 · BBA ₹1,45,400 ·
  BCA ₹1,25,000 · B.Com ₹75,000 · 2 certificates ₹28,000
- Includes JSON-LD `EducationalOccupationalProgram` schema for the Online MBA

## Files
| File | Purpose |
|---|---|
| `index.html` | Complete app — no build step |
| `manifest.webmanifest` | PWA installability |
| `sw.js` | Offline caching |
| `privacy-policy.html` | Store-submission requirement |
| `icons/` | App icons (shared with the older lead-gen app) |

## Run locally
Double-click `index.html`, or:
```bash
python -m http.server 8090   # open http://localhost:8090
```

## Deploy (GitHub Pages)
Same flow as the older app:
```bash
git init && git add -A && git commit -m "Online MBA programs app"
# create repo e.g. amezingtech/online-mba-programs, then:
git remote add origin https://github.com/amezingtech/online-mba-programs.git
git push -u origin main   # enable Pages → deploy from branch
```
Live URL will be `https://amezingtech.github.io/online-mba-programs/`.

## Publish as Android app (PWABuilder — free)
1. Open https://www.pwabuilder.com, enter the deployed URL.
2. Download the **Android package (AAB)**.
3. Upload to Google Play Console ($25 one-time) with the listing below.

## Play Store listing draft (keyword: online mba)
- **App title:** `Online MBA - Programs & Fees` (alternatives: `Online MBA: DPU Degrees 2026`)
- **Short description:** `Online MBA fees, 18 specializations & all DPU Pune online degrees — BBA, MCA, B.Com. Free counseling on WhatsApp.`
- **Long description keywords to include naturally:** online mba, online mba fees, online mba india, mba online, online degree, online bba, online mca, dy patil online
- **Category:** Education · **Rating:** Everyone

## Editing
- WhatsApp number: `WA_NUM` in `index.html` (one place).
- All program data lives in the `PROGRAMS` object — fees, syllabus, FAQs, jobs.
- MBA specialization career lines: `SPEC_CAREERS`.
- Footer keeps the honest partner framing — preserve it when editing.
