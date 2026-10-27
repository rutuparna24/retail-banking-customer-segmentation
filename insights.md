# Business insights (auto-generated from computed results)

> Data source: UCI Bank Marketing dataset (real, anonymised, Portuguese bank, 2008-2010).

## Insights

1. **Response differs materially by segment.** Overall term-deposit conversion is 11.7%. Among segments with at least 100 customers, 'Senior Customers' converts best at 34.1% (n=1,541) and 'Financially Stretched' lowest at 5.7% (n=4,141).
2. **Campaign history matters.** Customers whose earlier campaign outcome was 'Success' converted at 64.7% (n=1,511) versus 9.2% for first-time contacts (n=36,954).
3. **Timing is uneven.** Highest-converting months (min 100 contacts): Mar (52.0%, n=477), Dec (46.7%, n=214), Sep (46.5%, n=579). The busiest month was May with 30.4% of all contacts at 6.7% conversion - volume and conversion are not the same thing.
4. **More contact attempts go with lower conversion.** One-contact customers converted at 14.6%; customers contacted 6+ times at 5.8% (n=4,355). Correlation only: banks may call hard-to-convert customers more often.
5. **Existing loans relate to deposit take-up.** Customers with no loans converted at 18.2% versus 6.1% for customers with both a housing and personal loan (no-loan customers respond better). A propensity model using pre-call information reached ROC-AUC 0.7131 (5-fold out-of-fold); its top decile converted at 39.4%, 3.37x the overall rate.

## Recommendations (each tied to a number above)

1. **Prioritise outreach by segment and history.** Start campaigns with 'Senior Customers' and with customers who previously said yes (insights 1-2); treat 'Financially Stretched' with lower-intensity, service-led contact.
2. **Score before you call.** Use the propensity score (excludes call duration, so it is usable before dialling) to rank the list: contacting only the top 30% of customers would reach 58.8% of the actual subscribers in this data. Pilot it on a small test-and-control group before trusting it.
3. **Build a lending cross-sell pilot from the product-gap pool.** 6,579 customers hold no loan, have no default flag and a balance of at least 1,000 euros; the largest pool is 'Mass Market Core' (4,020). This data has no loan-offer responses, so the take-up rate is unknown - the pilot should measure it.

## Limits you must state

- Observational data: patterns are associations, not proof of cause.
- One Portuguese bank, 2008-2010, euro balances; not ICICI Bank / Indian customers.
- Only the term deposit has an observed outcome; no credit-card, insurance or investment data.
- Segment names and thresholds are analyst assumptions (see docs/methodology.md).
