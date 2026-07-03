# Slyva Crescent Hotel — Booking Performance Dashboard

An interactive, dark-themed Excel dashboard analyzing 119,209 hotel bookings across two Slyva Crescent properties (City Hotel & Resort Hotel), covering arrivals between July 2015 and August 2017 — built to uncover guest origin, revenue, length-of-stay, and cancellation patterns.

---

## 📌 Overview

Slyva Crescent needed to move beyond raw booking records to understand *who* their guests are, *how much* they spend, *how long* they stay, and — most critically — *why* over a third of bookings end in cancellation. This dashboard turns 119K+ rows of raw reservation data into a single, filterable interactive view for management, with slicers by year, hotel type, and guest status (new vs. repeat).

---

## 🎯 Business Questions & Answers

1. **Which country do most travellers come from?**
   Portugal dominates by a wide margin — followed by the UK, France, Spain, and Germany.

   | Rank | Country        | Bookings |
   |------|----------------|----------|
   | 1    | Portugal       | 48,483   |
   | 2    | United Kingdom | 12,119   |
   | 3    | France         | 10,401   |
   | 4    | Spain          | 8,560    |
   | 5    | Germany        | 7,285    |

2. **Who has the highest ADR (Average Daily Rate)? How much?**
   Daniel Walter, City Hotel — **$5,400.00** (arrival: 25 March 2016). A significant outlier versus the rest of the dataset, where rates are typically well under $400.

3. **What is the mean total ADR across all bookings?**
   **$101.83**

4. **What is the average length of stay?**
   **3.43 nights**

5. **Who booked with the most children and babies?**
   A tie at the top, each with 10 children: **Jamie Ramirez** (Resort Hotel) and **Nicholas Parker**.

6. **How does cancellation behavior differ between repeat and new guests?**
   Repeat guests cancel far less often than new guests — prior experience with the hotel correlates strongly with follow-through on bookings.

7. **What are the seasonal trends in booking volume?**
   **August** is the busiest month for arrivals, with demand tapering off toward the winter months — a clear summer peak.

8. **How does lead time affect cancellation likelihood?**
   Cancellation risk rises steadily the further in advance a booking is made — bookings made within a week of arrival rarely cancel (under 10%), while bookings made more than a year out cancel the majority of the time (over two-thirds).

---

## 🧹 Data Cleaning & Preparation

Cleaning was done in Python (pandas) before the data was loaded into Excel for dashboarding.

- Dropped irrelevant/sensitive columns: `agent`, `company`, `email`, `phone-number`, `credit_card`.
- Removed **181 invalid bookings**: 1 with a negative rate (logically impossible) and 180 listing zero total guests.
- Filled missing `children` values with **0**, on the assumption guests left the field blank rather than omitting a non-zero count.
- Labeled missing `country` values as **"Unknown"** rather than guessing, to avoid introducing bias into the country breakdown.
- Engineered new features:
  - `total_kids` = `children` + `babies`
  - `total_guests` = `adults` + `total_kids`
  - `total_nights` = `stays_in_weekend_nights` + `stays_in_week_nights`
- Exported the cleaned dataset to `CLEANED_DATA.csv` for dashboard use.

See [`hotel_cleaning.py`](hotel_cleaning.py) for the full script.

---

## 📊 Dashboard Features

- **Dark, branded theme** (Slyva Crescent green/black) for a modern, presentation-ready look
- **KPI cards:** Total Bookings (44,224 shown at default filter), Average ADR ($101.83), Average Nights Stayed (3.43), Cancellation Rate (37.0%)
- **Slicers:** Year (2015–2017), Guest Status (New vs. Repeat), Hotel Type (City vs. Resort)
- **Lead Time vs. Likelihood of Cancellation** — line chart showing cancellation risk climbing from near-0% (0–7 days) to ~70%+ (365+ days)
- **Repeat vs. New Guest Cancellation** — bar comparison confirming repeat guests cancel far less
- **Top 5 Reservations by Country** — bar chart led heavily by Portugal
- **Month Activity** — bar chart of booking volume by month, peaking in August
- **Highest ADR & Top Bookings panels** — spotlighting outlier/notable guest records

---

## 💡 Key Findings

- **Guest origin** is heavily concentrated in Portugal and nearby European markets, suggesting a largely domestic/regional guest base rather than a globally diversified one.
- **Revenue:** Average ADR is $101.83, but this is pulled upward by at least one major outlier ($5,400 booking); the median gives a more representative day-to-day picture.
- **Cancellations (37.0% overall)** are not evenly distributed — they're heavily concentrated among first-time guests and long-lead-time bookings.
- **Seasonality:** Clear summer peak in August, tapering toward a winter trough — a predictable demand curve the hotel can staff and market around.

---

## ✅ Recommendations

1. **Target high-lead-time bookings** with confirmation reminders, flexible-but-incentivized deposit terms, or pre-arrival engagement — this segment drives the bulk of cancellations.
2. **Invest in guest retention/loyalty incentives** — repeat guests are meaningfully more reliable, so converting first-timers into repeat guests has a compounding effect on lowering cancellation rates.
3. **Plan staffing and marketing around the August peak and winter trough** to balance occupancy and avoid overstaffing in slow months or strain during peak season.

---

## ⚠️ Limitations

This analysis reflects historical booking data only. It does not account for external factors — pricing changes, marketing campaigns, competitor activity — that may also influence cancellation and demand patterns.

---

## 📁 Repository Structure

```
├── README.md
├── BUSINESS_QUESTIONS.pdf
├── EXECUTIVE_SUMMARY.pdf
├── hotel_cleaning.py
├── Hotel_Booking_dashboard.xlsb
└── screenshots/
    └── dashboard-overview.png
```

---

## 🧰 Tech Stack

| Tool               | Purpose                                              |
|---------------------|-------------------------------------------------------|
| Python (pandas)     | Data cleaning, validation, feature engineering        |
| Microsoft Excel     | Dashboard design, KPI cards, slicers, charts          |

---

## 🚀 How to Use

1. Download `Hotel_Booking_dashboard.xlsb`.
2. Open in Excel (enable macros/editing if prompted).
3. Use the **Year**, **Guest Status**, and **Hotel Type** slicers to filter the dashboard.
4. Refer to `BUSINESS_QUESTIONS.pdf` and `EXECUTIVE_SUMMARY.pdf` for the full analysis writeup and recommendations.
5. See `hotel_cleaning.py` to review or reproduce the data cleaning steps on the raw dataset.

---

## 📸 Screenshot

<img width="1539" height="816" alt="Screenshot 2026-06-27 232416" src="https://github.com/user-attachments/assets/c37be2c5-d17b-4592-96d3-13134b4b768d" />


---

## 👤 Author

**Peter Obikpe (Pheonix)**
Data Analyst | IT Instructor
[Portfolio](https://peter-portfolio11.vercel.app) · [LinkedIn](https://www.linkedin.com/in/peter-obikpe) · [Email](obikpepeter808@gmail.com)
