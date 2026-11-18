# Warm Bowl / 暖碗

Website for Warm Bowl: hot dinners from local restaurants for seniors in Bayview Hill, Richmond Hill, brought by the same trusted driver.

Plain HTML and CSS. No framework and nothing to install except Python, which builds the pages.

## Pages

| File | What it is |
|---|---|
| `index.html` | Home |
| `how-it-works.html` | Sign-up, choosing dinner, delivery night, cancelling and pausing |
| `food.html` | Sample dishes, diet options, labels |
| `pricing.html` | Plans, trial week, pay it forward, billing, planned everyday prices |
| `safety.html` | Driver standards and the no-answer protocol |
| `faq.html` | Questions |
| `waitlist.html` | Waitlist form (the main goal of the site) |
| `about.html` | Founder story |
| `drive.html` | Driver recruiting with application form |
| `restaurants.html` | Restaurant partner pitch with interest form |
| `zh.html` | Chinese (Simplified) page with its own waitlist form |
| `privacy.html` | Privacy note |
| `404.html` | Not-found page |

## Editing

Don't edit the `.html` files in the main folder directly. They get overwritten.

1. Edit the page content in `_build/pages/`. The shared header and footer are in `_build/build.py`.
2. Rebuild:

   ```bash
   python _build/build.py
   ```

3. Preview locally:

   ```bash
   python -m http.server 8420
   ```

   Then open http://localhost:8420

The build also writes `sitemap.xml` and `robots.txt`. When you add a page, add it to `SITEMAP` in `_build/build.py`. If the site moves to its own domain, change `SITE_URL` there and rebuild.

Styles are in `assets/css/style.css`. The colours and fonts are at the top of that file.

House style: no em dashes or en dashes anywhere. Write time and price ranges with "to", for example "5:00 to 6:15 pm".

## Before going live

Done:
- Forms are connected to Formspree (waitlist, driver, restaurant). The endpoints are in `assets/js/config.js`.
- Contact email is `warmbowlmeals@gmail.com`. To change it, search and replace it in `_build/` and `assets/js/`, then rebuild.

Still to do:
1. **Check these against reality:**
   - Prices: $20 a meal plus HST. 2 Treats $40 a week (Tue and Thu), 3 Treats $60 (adds Sat, from fall 2027). Later plans: 5 Dinners $100, 7 Dinners $140, 5 Lunches $100.
   - Driver pay (about $20 an hour plus mileage).
   - Delivery window (5:00 to 6:15 pm), lunch window (11:30 am to 12:45 pm), and cutoffs (choose by 8 pm the night before, cancel by 2 pm).
   - Partner restaurants aren't named anywhere on purpose. Add them to `food.html` once agreements are signed.
   - The site says partners will offer a lighter list of dishes, reviewed by a dietitian where possible.
2. **Host it.** Any static host works. Netlify, Cloudflare Pages and GitHub Pages are free. Upload the whole folder. The `_build` folder and `README.md` are harmless if uploaded.
