# Complaint Reply Tool

**Live demo:** https://complaint-reply-tool.onrender.com

A simple web tool that turns a customer complaint into a polite, professional reply draft in seconds.

## What it does

Small businesses in Kampala (shops, courier services, Airbnbs, restaurants) get complaints on WhatsApp and often spend around 20 minutes writing a careful reply. This tool reduces that to three steps:

1. Paste the customer's complaint into the text box.
2. Click **Generate Reply**.
3. Get a draft reply on the same page, ready to copy into WhatsApp.

Every reply is written to:

- Be polite and acknowledge the customer's specific issue.
- Offer one clear next step.
- Avoid blaming the customer, staff, or anyone else.
- Avoid promising refunds, replacements, or exact times.

**Who it is for:** any business that handles customer complaints by message.

## Important note

This tool writes a **draft**. The business owner should read and edit the reply before sending it, especially for serious complaints (health issues, threats, or large amounts of money).

## How I tested it

I tested the live site with three different complaints, checking every reply against a six-point checklist: polite, acknowledges the specific issue, no blame, no promises, one clear next step, and short enough for WhatsApp.

| # | Business type | Complaint tested | Result |
|---|---|---|---|
| 1 | Restaurant | Food arrived cold and one hour late, third time | Pass |
| 2 | Courier | Parcel arrived crushed with a cracked phone screen | Pass |
| 3 | Airbnb | Room not clean and no wifi, guest wants money back | Pass |

AI replies vary slightly each time, so I ran each complaint more than once and refined the instructions given to the AI until replies were consistently within the rules.

## Pricing for a branded version

A branded version is this same tool customised for one business.

**What is included:**

- The business's name, colours, and logo on the page.
- Reply instructions written around the business's own tone and policies (for example, a courier's tracking process).
- Deployment on a live address, with the API key stored securely.
- Testing with the business's own real complaints.
- A short handover so the owner knows how to use it.

| | Price (UGX) |
|---|---|
| **One-time setup** | **350,000** |
| **Monthly (optional but recommended)** | **60,000** |

The monthly fee covers always-on hosting, AI usage, monitoring, and small updates to the reply instructions. First-year cost for a client who takes both: UGX 1,070,000 (350,000 + 12 x 60,000).

**Not included (priced separately):** connecting the tool directly to WhatsApp so replies send automatically, multiple users or logins, saving complaint history, or high-volume use.

### Why this price: the research

Research done on 7 November 2026. Prices change, and most figures below are prices businesses advertise, not confirmed amounts customers actually paid. USD figures are converted at roughly UGX 3,700 per US dollar, so check the current rate.

**1. The value to the customer**

My teacher's brief puts a typical complaint reply at about 20 minutes of writing. A business with 10 complaints a week spends about 14 hours a month on replies. If the owner still spends about 5 minutes reading and editing each draft, the saving is roughly 11 hours a month. This is an illustration, not a guarantee, because results depend on the business.

**2. What similar services cost in Uganda**

| Comparison | Advertised price | Notes |
|---|---|---|
| Basic business website | UGX 600,000 - 900,000 | Kampala web design agency pricing, 2026 |
| Custom WhatsApp chatbot for small businesses | UGX 500,000 - 3,000,000 | Wider scope than this tool |
| AI sales agent on WhatsApp (Kampala agency) | Setup from about UGX 1,000,000 | Much wider scope |
| Chatbot widget subscription | From UGX 349,000 per month | Ugandan provider, includes lead capture and integrations |
| Customer support software | UGX 40,000 per month (1 agent) to UGX 250,000 per month (3 agents, WhatsApp) | 2025 listing |
| Overseas WhatsApp AI assistants | About USD 15 - 75 per month | Subscription products |
| Agency custom chatbots | USD 3,000 - 18,000 | Much larger projects, not comparable to this tool |

This tool does one narrow job: it has no WhatsApp connection, no login, and no memory. So I priced it below the custom chatbot range and below a basic website, while keeping the monthly fee at the low end of subscription products.

**3. What it costs me to run, per client**

| Cost | Estimate per month | Source and assumptions |
|---|---|---|
| Hosting (always-on) | About USD 7 (about UGX 26,000) | Render's Starter web service. The free plan sleeps after 15 minutes without visitors and takes about a minute to wake up, which is fine for a demo but not for a business using it daily. |
| AI usage | About UGX 3,000 - 10,000 for 300 replies | My estimate, not measured. Assumes about 500 input and 200 output tokens per reply, at published rates of about USD 1.50 input and USD 9 output per million tokens for Gemini 3.5 Flash. Cheaper models cost less. |
| **Total** | **About UGX 30,000 - 36,000** | |

The AI usage cost is very small. The real running cost is hosting, which is why the monthly fee must cover at least that. At UGX 60,000, I keep roughly UGX 24,000 per month for monitoring and small updates.

**4. How I set the numbers**

- **Setup, UGX 350,000:** roughly half the low end of a basic website package, because the scope is much smaller. It covers a few hours of branding, prompt tailoring, deployment, and testing.
- **Monthly, UGX 60,000:** covers my costs (about UGX 36,000) plus time for support. It is far below chatbot widget subscriptions and close to the lower end of customer support software.
- Both numbers are a starting point. I will adjust them after speaking with real business owners about what they would pay.

## Built with

- Python and Flask (backend)
- HTML, CSS, and JavaScript (frontend)
- Google Gemini API (reply generation)
- Hosted on Render

## How it is secured

- The API key is stored as a protected environment variable on the server and is never in the code or the GitHub repository.
- The app runs on a production server (Gunicorn), with debug mode off.
- **For paying clients:** complaints contain customer information. Google states that content sent on the free Gemini tier may be used to improve its products, while paid-tier content is not. A client version should use a paid API key.

## Run it locally

1. Clone this repo and create a virtual environment.
2. Run `pip install -r requirements.txt`.
3. Create a `.env` file containing `GEMINI_API_KEY=your_key`.
4. Run `python app.py` and open http://127.0.0.1:5000.

## Limitations

- Replies are AI-generated drafts and vary between runs.
- Tested in English. Other languages, including Luganda, have not been verified.
- The live demo runs on a free hosting plan, so the first visit after a quiet period may take about a minute to load.
- The demo is public, and each reply uses my API quota. A client version would add access protection and usage limits.

## Research sources (checked 7 November 2026)

- Kico Web Design, "Best Website Designers in Uganda (2026)" (website package prices; vendor-published)
- Mctaba, "Building a WhatsApp Chatbot for Ugandan Businesses" (custom WhatsApp chatbot range)
- Desishub, "Why Every Kampala SME Needs an AI-Powered Chatbot (2026)" (setup from UGX 1M)
- Virtual Receptionist Uganda (chatbot widget subscription)
- Nucamp, "Top 10 AI Tools Every Customer Service Professional in Uganda Should Know" (support software prices)
- Information Village Limited, "How much does an AI chatbot cost in Uganda? (2026 guide)" (agency price ranges and running costs)
- HustleFlow (overseas WhatsApp AI assistant subscription prices)
- Render documentation (docs.render.com/free) and Render pricing summaries (free plan spin-down, Starter instance price)
- Gemini API pricing, from Google (ai.google.dev/pricing) and third-party summaries (per-token rates, free vs paid data handling)