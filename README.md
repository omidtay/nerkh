# Nerkh

A minimal currency converter for iPhone, built as an installable web app (PWA), the same way as
[world-clock](https://github.com/omidtay/world-clock). No App Store and no Xcode needed.

- Pick the currencies you care about; tap any amount and type, and every other row follows.
- Toman (and rial) use the **Tehran free market**, not the official rate. Gold coins
  (Emami, half, quarter, gram coin), 18k/24k gold per gram, mesghal and crypto in toman come from the same feed.
- Pairs that don't touch toman (EUR → USD, BTC → AED …) use global rates.
- Rates refresh on open, every 2 minutes while the app is on screen, and when you tap the status line.
  The last rates are kept, so it still works offline and says how old they are.
- Keypad has `000` for toman amounts; hold delete to clear. Edit to remove or reorder rows.
- Light and dark mode follow the phone.

## Sources

| What | Source | Updates |
| --- | --- | --- |
| Toman, rial, gold, coins, crypto in toman | [tgju.org](https://www.tgju.org) (`call2/3/4.tgju.org/ajax.json`) | every few minutes |
| Global fiat vs USD | [open.er-api.com](https://open.er-api.com) | daily |
| Global fiat, crypto, gold ounce (fallback) | [fawazahmed0/currency-api](https://github.com/fawazahmed0/exchange-api) | daily |

All three allow browser requests, so there's no backend. A currency without its own tgju quote
gets its toman price from the dollar cross rate.

## Install on iPhone

1. Open the site in **Safari**.
2. Tap **Share** → **Add to Home Screen** → **Add**.
3. Launch it from the home screen; it opens full screen like a normal app.

## Hosting

Static files only (`index.html`, `sw.js`, `manifest.webmanifest`, `icons/`), served by GitHub Pages
from `main` / root.

When you change the app, bump `CACHE` in `sw.js` so installed copies pick up the new version.
Icons are drawn by `scripts/make_icons.py`.
