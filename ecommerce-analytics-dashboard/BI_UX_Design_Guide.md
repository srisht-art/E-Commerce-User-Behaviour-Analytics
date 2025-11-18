# E-commerce Analytics Dashboard: BI, UX Design & Microcopy Guide

## Part 1: BI Dashboard Design (Senior BI Consultant Perspective)

### 1. Key KPIs (5-7 Metrics for Top Section)

| KPI | Calculation | Tooltip Explanation |
|-----|-------------|---------------------|
| **Total Revenue** | `SUM(Revenue)` | Total money earned from all completed purchases in the selected period. |
| **Conversion Rate** | `(Total Purchases / Total Sessions) × 100` | Percentage of website visitors who completed a purchase. |
| **Cart Abandonment Rate** | `((Add to Cart - Purchase) / Add to Cart) × 100` | Percentage of users who added items to cart but didn't complete the purchase. |
| **Average Order Value (AOV)** | `Total Revenue / Total Orders` | Average amount spent by a customer per order. |
| **Revenue per User (RPU)** | `Total Revenue / Unique Users` | Average amount each unique customer spent during the period. |
| **Returning Customer Rate** | `(Returning Customers / Total Customers) × 100` | Percentage of customers who made more than one purchase. |
| **Session-to-Purchase Time** | `AVG(Time from Session Start to Purchase)` | Average time it takes for a user to complete a purchase after starting a session. |

### 2. Best Charts/Visuals (3-4 Core Visualizations)

#### Chart 1: **Funnel Chart - User Journey**
- **What it shows:** Homepage → Product View → Add to Cart → Checkout → Payment Success
- **Why it's useful:** Instantly identifies where users drop off in the conversion process
- **Insight:** Highlights the biggest bottleneck (e.g., "60% drop at checkout stage")

#### Chart 2: **Line Chart - Revenue Trend Over Time**
- **What it shows:** Daily/Weekly/Monthly revenue with trend line
- **Why it's useful:** Shows growth patterns, seasonality, and identifies peak sales periods
- **Insight:** "Revenue increased 25% in Q4" or "Weekends show 40% higher sales"

#### Chart 3: **Stacked Bar Chart - Revenue by Product Category**
- **What it shows:** Total revenue broken down by product categories (stacked or grouped)
- **Why it's useful:** Identifies top-performing categories and revenue distribution
- **Insight:** "Electronics contribute 45% of total revenue" or "Fashion category growing fastest"

#### Chart 4: **Heatmap - User Activity by Day & Hour**
- **What it shows:** Color-coded grid showing peak activity times (darker = more activity)
- **Why it's useful:** Helps schedule promotions, customer support, and understand user behavior patterns
- **Insight:** "Peak shopping hours: 7-9 PM on weekdays, 2-4 PM on weekends"

### 3. Dashboard Layout (Single Page)

```
┌─────────────────────────────────────────────────────────────────┐
│  TOP SECTION: KPIs (7 cards in a row)                         │
│  [Revenue] [Conversion] [Cart Abandon] [AOV] [RPU] [Returning] │
│  [Session Time]                                                 │
├─────────────────────────────────────────────────────────────────┤
│  LEFT PANEL (50%)          │  RIGHT PANEL (50%)               │
│                              │                                  │
│  FUNNEL CHART                │  REVENUE BY CATEGORY            │
│  (User Journey)              │  (Stacked Bar Chart)            │
│                              │                                  │
│  [Visualization]             │  [Visualization]                 │
│                              │                                  │
│  Key Insight:                │  Top 3 Categories:                │
│  "Checkout has highest       │  1. Electronics - $45K           │
│   drop-off (60%)"            │  2. Fashion - $32K              │
│                              │  3. Home & Living - $18K        │
├─────────────────────────────────────────────────────────────────┤
│  BOTTOM SECTION (Full Width)                                   │
│                                                                 │
│  REVENUE TREND LINE CHART                                      │
│  [Monthly/Weekly Revenue Over Time]                            │
│                                                                 │
│  ACTIVITY HEATMAP (Optional - if space allows)                 │
│  [Day × Hour Activity Grid]                                    │
└─────────────────────────────────────────────────────────────────┘
```

**Design Principles:**
- **Top:** KPIs in cards with trend indicators (↑↓ arrows, % change)
- **Left:** Funnel chart (most critical for identifying issues)
- **Right:** Category breakdown (business performance)
- **Bottom:** Time series (trends and patterns)
- **Color Scheme:** Green for positive metrics, Orange for warnings, Red for critical issues

---

## Part 2: UX Flow Improvements (Senior UX Designer Perspective)

### Data Insights Summary
Based on typical e-commerce analytics:
- **Biggest drop-off:** Checkout page (60% of users who reach checkout abandon)
- **Secondary drop-off:** Add to Cart stage (30% add items but don't proceed)
- **Device insight:** Mobile users convert 40% less than desktop users
- **Time insight:** Users who spend >5 minutes on product pages convert 3x higher

### 1. Optimal User Flow

```
HOME PAGE
    ↓
PRODUCT LISTING (with filters)
    ↓
PRODUCT DETAIL PAGE
    ↓
ADD TO CART (with mini cart preview)
    ↓
CART PAGE (review & edit)
    ↓
CHECKOUT (simplified, 1-page)
    ↓
PAYMENT (multiple options, saved cards)
    ↓
ORDER CONFIRMATION
```

**Key Principles:**
- **Reduce friction:** Fewer clicks, fewer form fields
- **Build trust:** Show security badges, return policy, reviews
- **Create urgency:** Limited stock, time-sensitive offers
- **Mobile-first:** Thumb-friendly buttons, simplified navigation

### 2. Screen-by-Screen Design

#### **HOME PAGE**

**Main Goals:**
- Show value proposition immediately
- Guide users to products they want
- Build trust and credibility

**Must-Have Elements:**
1. **Hero banner** with clear value proposition (e.g., "Free Shipping on Orders $50+")
2. **Search bar** (prominent, autocomplete enabled)
3. **Category navigation** (visual icons, max 6-8 categories)
4. **Featured products** (best sellers, new arrivals)
5. **Trust badges** (secure payment, return policy, customer reviews)

**Data-Based Improvements:**
- Show "Trending Now" based on real-time analytics
- Personalize "Recommended for You" based on user behavior
- Display "Limited Stock" badges on popular items
- Add "Recently Viewed" section for returning users

**Figma Layout Suggestion:**
- **Header:** Sticky top bar with logo (left), search (center), cart icon (right)
- **Hero Section:** Full-width banner (1920×600px on desktop, 375×300px on mobile)
- **Content:** 3-column grid for categories (desktop), 2-column (tablet), 1-column (mobile)
- **Products:** 4-column grid (desktop), 2-column (mobile) with hover effects

---

#### **PRODUCT DETAIL PAGE**

**Main Goals:**
- Show product clearly (images, details, price)
- Answer user questions (reviews, Q&A, specifications)
- Make it easy to add to cart

**Must-Have Elements:**
1. **Image gallery** (zoom, multiple angles, 360° view if possible)
2. **Product title & price** (clear, prominent)
3. **Add to Cart button** (large, visible, shows stock status)
4. **Product description** (collapsible, detailed specs)
5. **Customer reviews** (ratings, photos, verified purchases)

**Data-Based Improvements:**
- Show "X people viewing this" to create urgency
- Display "Usually ships in 2-3 days" based on inventory
- Add "Frequently bought together" recommendations
- Show "People also viewed" at bottom
- Display return policy and warranty info upfront

**Figma Layout Suggestion:**
- **Left (60%):** Image gallery with thumbnails below
- **Right (40%):** Product info, price, size/color selector, Add to Cart button (sticky on scroll)
- **Below:** Tabs for Description, Reviews, Q&A, Shipping Info
- **Mobile:** Stack vertically, sticky "Add to Cart" bar at bottom

---

#### **CART PAGE**

**Main Goals:**
- Show items clearly with easy edit/remove options
- Display total cost breakdown
- Encourage proceeding to checkout

**Must-Have Elements:**
1. **Item list** (image, name, price, quantity selector, remove button)
2. **Price summary** (subtotal, shipping, tax, total)
3. **Promo code field** (collapsible)
4. **Checkout button** (prominent, full-width on mobile)
5. **Continue shopping link** (secondary action)

**Data-Based Improvements:**
- Show "You're $X away from free shipping" (if applicable)
- Display "Save for later" option (reduces abandonment)
- Add "Recommended items" below cart
- Show estimated delivery date
- Display security badges near checkout button

**Figma Layout Suggestion:**
- **Left (70%):** Cart items list
- **Right (30%):** Order summary box (sticky on desktop)
- **Mobile:** Stack items, sticky order summary at bottom
- **Empty state:** Friendly illustration + "Start Shopping" CTA

---

#### **CHECKOUT PAGE**

**Main Goals:**
- Collect payment and shipping info quickly
- Build trust and reduce anxiety
- Complete the purchase

**Must-Have Elements:**
1. **Progress indicator** (Step 1 of 2: Shipping → Payment)
2. **Shipping address form** (auto-fill if logged in, address validation)
3. **Payment method selector** (cards, PayPal, Apple Pay, etc.)
4. **Order summary** (items, prices, total - always visible)
5. **Place Order button** (clear, secure, shows total)

**Data-Based Improvements:**
- **One-page checkout** (reduce form fields by 50%)
- **Guest checkout option** (don't force account creation)
- **Save address for next time** (checkbox)
- **Show shipping options** with estimated delivery
- **Display trust signals** (SSL badge, money-back guarantee)
- **Auto-apply best shipping** (free if available)
- **Mobile:** Use native inputs (better UX, autofill)

**Figma Layout Suggestion:**
- **Left (60%):** Form fields (shipping, then payment)
- **Right (40%):** Sticky order summary box
- **Mobile:** Single column, order summary at bottom (sticky)
- **Form fields:** Large, clear labels, inline validation
- **Buttons:** Primary (Place Order) - full width, Secondary (Back to Cart) - outlined

---

### 3. Key UX Improvements Based on Data

**For Checkout Drop-off (60%):**
- Reduce form fields from 12 to 6 (use smart defaults)
- Add "Express Checkout" with saved payment methods
- Show progress indicator ("Almost done! 2 steps left")
- Display security badges prominently
- Add "Estimated delivery: Dec 25" to create urgency

**For Add to Cart Drop-off (30%):**
- Show mini cart preview when item added (don't navigate away)
- Add "Continue Shopping" option in cart
- Display "X items in cart" badge on header
- Show "Save for later" option
- Add "Recommended items" in cart

**For Mobile Conversion (40% lower):**
- Larger touch targets (min 44×44px)
- Simplified navigation (hamburger menu)
- Sticky "Add to Cart" button on product pages
- One-column layout (no sidebars)
- Faster page load (optimize images, lazy load)

---

## Part 3: Microcopy (UX Writer Perspective)

### Tone Guidelines
- **Simple:** Use everyday words, avoid jargon
- **Human:** Write like you're talking to a friend
- **Friendly:** Warm but professional, not overly casual
- **Clear:** One idea per sentence, direct action

---

### 1. Add to Cart Button

**States:**

**Default:**
```
Add to Cart
```

**With Quantity:**
```
Add 2 to Cart
```

**Out of Stock:**
```
Out of Stock
(Notify me when available)
```

**Loading:**
```
Adding...
```

**Success (Toast/Notification):**
```
✓ Added to cart! [View Cart]
```

---

### 2. Checkout Button

**Cart Page:**
```
Proceed to Checkout
```

**Checkout Page:**
```
Place Order • $129.99
```

**With Security:**
```
Place Secure Order
```

**Loading:**
```
Processing...
```

---

### 3. Empty Cart Screen

**Headline:**
```
Your cart is empty
```

**Subheading:**
```
Looks like you haven't added anything yet.
```

**CTA Button:**
```
Start Shopping
```

**Optional Secondary:**
```
Browse Categories
```

**Illustration:** Friendly shopping bag or cart icon (not sad/empty feeling)

---

### 4. Payment Success Screen

**Headline:**
```
Order confirmed! 🎉
```

**Subheading:**
```
Thanks for your purchase. We've sent a confirmation email to you@email.com
```

**Order Details:**
```
Order #12345
Estimated delivery: Dec 25, 2024
```

**Actions:**
```
[Track Order]  [Continue Shopping]
```

**Optional:**
```
Share your purchase and get 10% off your next order
```

---

### 5. Payment Failure Screen

**Headline:**
```
Payment couldn't be processed
```

**Subheading:**
```
Don't worry, your items are still in your cart. Please try again or use a different payment method.
```

**Actions:**
```
[Try Again]  [Use Different Payment]  [Contact Support]
```

**Helpful Note:**
```
Tip: Check that your card details are correct and you have sufficient funds.
```

---

### 6. Error Messages (Short & User-Focused)

**Card Declined:**
```
Your card was declined. Please try a different card or contact your bank.
```

**Invalid Address:**
```
We couldn't verify this address. Please check and try again.
```

**Network Issue:**
```
Connection lost. Please check your internet and try again.
```

**Alternative (Even Shorter):**

**Card Declined:**
```
Card declined. Try another payment method.
```

**Invalid Address:**
```
Address not found. Please check and update.
```

**Network Issue:**
```
Connection error. Please try again.
```

---

## Summary: Quick Reference

### Dashboard KPIs Priority
1. Conversion Rate (most important)
2. Cart Abandonment Rate
3. Total Revenue
4. Average Order Value
5. Revenue per User

### UX Flow Priority Fixes
1. **Checkout:** Simplify form, add trust signals
2. **Cart:** Show mini preview, save for later
3. **Mobile:** Larger buttons, simplified layout
4. **Product Page:** Add urgency, show reviews

### Microcopy Principles
- Keep it under 10 words when possible
- Use active voice ("Add to cart" not "Item will be added")
- Show, don't tell ("Order confirmed!" not "Your order has been successfully processed")
- Be helpful, not apologetic (focus on solution, not problem)

---

**Next Steps:**
1. Implement dashboard in Power BI using these KPIs
2. Create Figma mockups following layout suggestions
3. Test microcopy with real users (A/B test different versions)
4. Monitor analytics to measure impact of changes

