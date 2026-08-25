
<img width="1414" height="809" alt="Screenshot 2026-08-25 at 6 05 56 AM" src="https://github.com/user-attachments/assets/78a1de6d-2825-4a7a-93b0-c0e039a27d18" />
<img width="1059" height="741" alt="Screenshot 2026-08-25 at 6 06 52 AM" src="https://github.com/user-attachments/assets/ee620049-3188-428b-803d-d139dd65a46c" />
<img width="1433" height="809" alt="Screenshot 2026-08-25 at 6 06 30 AM" src="https://github.com/user-attachments/assets/7d11c3aa-c37e-4494-afb6-b82bb35f46e7" />
<img width="1432" height="811" alt="Screenshot 2026-08-25 at 6 06 16 AM" src="https://github.com/user-attachments/assets/81e340ee-c573-4967-8115-78334727cc90" />
# 🏦 Vision Bank Financial Analytics & Business Intelligence Dashboard

[![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.0+-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Supabase](https://img.shields.io/badge/Supabase-Cloud-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)](https://supabase.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge)](LICENSE)

A high-performance, enterprise-grade financial analytics and business intelligence platform built to translate massive relational database ledgers into real-time operational insights. Powered by **Python**, **Streamlit**, **Plotly Express**, and hosted on **Supabase PostgreSQL**, Vision Bank Analytics provides banking executives, risk managers, and branch supervisors with dynamic risk profiling, customer segmentation, liquidity tracking, and branch throughput metrics.

---

## 📑 Table of Contents
1. [Executive Summary](#-executive-summary)
2. [Business Problems & Key Questions Solved](#-business-problems--key-questions-solved)
3. [System Architecture & Data Flow](#-system-architecture--data-flow)
4. [Relational Database Schema & Data Models](#-relational-database-schema--data-models)
5. [Dashboard Modules & Features](#-dashboard-modules--features)
6. [Technology Stack & Dependency Matrix](#-technology-stack--dependency-matrix)
7. [Prerequisites & System Requirements](#-prerequisites--system-requirements)
8. [Local Setup & Installation (Zsh Guide)](#-local-setup--installation-zsh-guide)
9. [Environment Configuration & Security](#-environment-configuration--security)
10. [Analytical Methods & Performance Optimization](#-analytical-methods--performance-optimization)
11. [Cloud Deployment Strategy (Streamlit Cloud)](#-cloud-deployment-strategy-streamlit-cloud)
12. [Future Roadmap & Modular Expansion](#-future-roadmap--modular-expansion)
13. [Author & Contact](#-author--contact)

---

## 🚀 Executive Summary

Modern retail and commercial banking operations generate millions of transactional records daily. Traditional reporting mechanisms—such as static spreadsheet exports or slow batch processing—fail to give decision-makers real-time visibility into liquidity, account defaults, or regional revenue shifts. 

**Vision Bank Analytics** solves this operational bottleneck by serving as a high-throughput visual intelligence wrapper over a relational database. Developed as a recruitment practical assessment, this production-ready application demonstrates how cloud database infrastructure (**Supabase PostgreSQL**) can be seamlessly connected to a reactive Python frontend (**Streamlit**) to provide low-latency analytical data exploration.

### Key Value Drivers:
* **Zero Latency Querying:** Uses optimized SQL views and server-side aggregation combined with local Python vectorized operations to render dashboards in sub-second timeframes.
* **Granular Risk Detection:** Automatically highlights high-risk credit accounts, loan default exposures, and overdue balance concentrations across customer segments.
* **360° Customer & Branch Insights:** Enables cross-table correlation between customer demographics, account tiers, transaction types, and geographic branch performance.

---

## 💡 Business Problems & Key Questions Solved

Vision Bank Analytics directly addresses critical operational and financial questions faced by executive leadership and banking risk officers:

### 1. Executive Leadership & Financial Health
* **Question:** *What is our overall financial velocity across total deposits, active loan capital, net fees generated, and net transaction volume?*
* **Solution:** The **Executive Summary** tab dynamically calculates high-level financial KPIs, calculating month-over-month (MoM) growth metrics across all active banking channels.

### 2. Credit Risk & Compliance Operations
* **Question:** *Which account tiers present the highest exposure to credit default, and where are overdue balances concentrated?*
* **Solution:** The **Risk & Credit Management** engine categorizes accounts by risk ratings, credit scores, and overdue debt levels, enabling compliance officers to mitigate default risks proactively.

### 3. Customer Lifecycle & Portfolio Segmentation
* **Question:** *How are account balances and revenue contributions distributed across Customer Tiers (e.g., Retail, Preferred, Private Banking) and Account Types (Savings, Checking, Investment)?*
* **Solution:** The **Customer Analytics** module breaks down capital distribution across demographics, highlighting top-tier high-net-worth customer segments and retention risks.

### 4. Regional Branch Performance & Operations
* **Question:** *Which branch locations drive the highest transaction throughput versus which locations are underperforming relative to overhead?*
* **Solution:** The **Branch Performance** tab compares transactional volume, total customer registrations, and total revenue per regional branch with interactive sorting and drill-down metrics.

### 5. Transaction Auditing & Fraud Pattern Isolation
* **Question:** *Are there unusual spikes in transfer velocities, high-frequency withdrawals, or fee revenues during specific operational windows?*
* **Solution:** The **Transaction Ledger Explorer** provides time-series trend analysis and granular record filtering by transaction type (Deposit, Withdrawal, Transfer, Wire, Fee).

---

## 🏗 System Architecture & Data Flow

The architecture follows a modular decoupled design, separating data persistence (Cloud PostgreSQL), connection pooling, data transformation (Pandas/NumPy), and presentation (Streamlit/Plotly).

```
+-----------------------------------------------------------------------+
|                            USER INTERFACE                             |
|              Streamlit Reactive Web App (Interactive Dashboard)       |
+-----------------------------------^-----------------------------------+
                                    |
                          Rendered Visualizations
                            (Plotly Express)
                                    |
+-----------------------------------v-----------------------------------+
|                        ANALYTICAL & PROCESSING LAYER                  |
|  - Streamlit Caching Engine (@st.cache_data)                          |
|  - Pandas Vectorized Transformations & Data Wrangling                 |
|  - Dynamic Filtering & Aggregation Pipelines                          |
+-----------------------------------^-----------------------------------+
                                    |
                             SQL Queries (ORMs)
                                    |
+-----------------------------------v-----------------------------------+
|                     DATA ACCESS & CONNECTION POOL                       |
|  - SQLAlchemy / Psycopg2 Database Drivers                             |
|  - SSL Encrypted Transport Layer                                      |
+-----------------------------------^-----------------------------------+
                                    |
                           Database Connection Pool
                                    |
+-----------------------------------v-----------------------------------+
|                          CLOUD DATABASE BACKEND                       |
|                   Supabase Managed PostgreSQL Instance                |
|  [customers] <---> [accounts] <---> [transactions] <---> [branches]   |
+-----------------------------------------------------------------------+
```

### Data Flow Execution Sequence:
1. **User Interaction:** The user adjusts dashboard controls (e.g., selects a date range, branch filter, or risk threshold).
2. **Query Dispatch / Cache Lookup:** Streamlit evaluates whether the query parameters match cached in-memory DataFrames (`@st.cache_data`).
3. **Database Execution:** If uncached, SQLAlchemy dispatches optimized SQL aggregation queries to the Supabase PostgreSQL instance over a connection pool.
4. **Vectorized Transformation:** Data returned from PostgreSQL is transformed in memory using Pandas and NumPy for complex KPI calculations.
5. **Chart Rendering:** Plotly Express generates interactive graphics (heatmaps, time-series line charts, bar graphs) which are rendered natively in the browser.

---

## 🗄 Relational Database Schema & Data Models

The underlying PostgreSQL database relies on a clean, normalized relational model designed for fast join operations and analytical query indexing.

```
       +-------------------+              +-------------------+
       |     branches      |              |     customers     |
       +-------------------+              +-------------------+
       | PK branch_id      |<-------------| PK customer_id    |
       |    branch_name    |              | FK branch_id      |
       |    city           |              |    first_name     |
       |    region         |              |    last_name      |
       |    manager_name   |              |    email          |
       +-------------------+              |    credit_score   |
                                          |    customer_tier  |
                                          |    created_at     |
                                          +---------+---------+
                                                    |
                                                    | 1:N
                                                    v
       +-------------------+              +-------------------+
       |   transactions    |              |     accounts      |
       +-------------------+              +-------------------+
       | PK transaction_id |              | PK account_id     |
       | FK account_id     |------------->| FK customer_id    |
       |    amount         |              |    account_type   |
       |    type           |              |    balance        |
       |    timestamp      |              |    overdue_amount |
       |    status         |              |    status         |
       +-------------------+              +-------------------+
```

### Data Table Definitions:

#### 1. `branches` Table
* `branch_id` (INT, Primary Key): Unique branch identifier.
* `branch_name` (VARCHAR): Name of the operational branch location.
* `city` (VARCHAR): Operating city.
* `region` (VARCHAR): Geographical territory/region.
* `manager_name` (VARCHAR): Branch operational supervisor.

#### 2. `customers` Table
* `customer_id` (INT, Primary Key): Unique customer identifier.
* `branch_id` (INT, Foreign Key -> `branches.branch_id`): Home branch assigned to customer.
* `first_name`, `last_name` (VARCHAR): Customer contact details.
* `email` (VARCHAR): Email address.
* `credit_score` (INT): Customer credit score (300-850 range).
* `customer_tier` (VARCHAR): Retail, Preferred, or Private Banking classification.
* `created_at` (TIMESTAMP): Customer onboarding date.

#### 3. `accounts` Table
* `account_id` (INT, Primary Key): Unique banking account number.
* `customer_id` (INT, Foreign Key -> `customers.customer_id`): Account holder reference.
* `account_type` (VARCHAR): Savings, Checking, Money Market, or Investment.
* `balance` (NUMERIC): Current liquid account balance.
* `overdue_amount` (NUMERIC): Outstanding overdue credit/loan balance.
* `status` (VARCHAR): Active, Dormant, Suspended, Closed.

#### 4. `transactions` Table
* `transaction_id` (INT, Primary Key): Ledger transaction tracking code.
* `account_id` (INT, Foreign Key -> `accounts.account_id`): Associated account.
* `amount` (NUMERIC): Monied value of transaction.
* `type` (VARCHAR): Deposit, Withdrawal, Transfer, Wire, Fee.
* `timestamp` (TIMESTAMP): Execution date and time.
* `status` (VARCHAR): Completed, Pending, Failed.

---

## ✨ Dashboard Modules & Features

Vision Bank Analytics features five dedicated tabs designed for structured exploration:

### Module 1: Executive Dashboard Overview
* **KPI Metrics Scorecard:** Visual callouts for Total System Deposits, Net Transaction Volume, Total Overdue Debt, and Active Account Count.
* **Monthly Volume Trajectory:** Interactive dual-axis chart comparing deposit growth against transaction outflow trends over time.

### Module 2: Risk & Default Analytics
* **Credit Risk Distribution Matrix:** Categorizes customer accounts into Risk Bands (Low, Medium, High, Default-Imminent) based on credit scores and account status.
* **Overdue Loan Exposure:** Interactive table listing accounts with delinquent payments, sorted by exposure size and branch location.

### Module 3: Customer Portfolio & Segmentation
* **Tiered Asset Distribution:** Donut charts illustrating total liquidity owned by Retail vs. Preferred vs. Private Banking tiers.
* **Customer Demographic Drill-Down:** Filterable data matrix showing customer longevity, average account balances, and cross-product adoption.

### Module 4: Regional Branch Analytics
* **Branch Comparison Heatmap:** Matrix plotting branch locations against metrics such as total accounts managed, total deposits collected, and gross fees.
* **Geographical Distribution:** Visual breakdown of account holdings across major operational territories.

### Module 5: Transaction Ledger & Data Exporter
* **Real-time Ledger Search:** Search and filter individual transactions by transaction ID, account ID, date range, or transaction category.
* **CSV/Excel Export Integration:** Allows analysts to download filtered analytical datasets directly for offline reporting.

---

## 🛠 Technology Stack & Dependency Matrix

| Category | Technology | Purpose / Role |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core application logic and data pipelines |
| **Web Framework** | Streamlit | Frontend UI generation and state management |
| **Database Platform**| Supabase | Cloud-managed PostgreSQL hosting |
| **Database Drivers** | SQLAlchemy, Psycopg2-binary | Connection management & SQL ORM query dispatch |
| **Data Processing** | Pandas, NumPy | In-memory data manipulation, aggregation, & vectorization |
| **Data Visualization**| Plotly Express, Chart Studio | Interactive charting, time-series, and heatmaps |
| **Environment Tools**| Python-dotenv | Local environment variable isolation |

---

## 📋 Prerequisites & System Requirements

Before attempting local setup, verify that your workstation environment satisfies the following requirements:

* **Operating System:** macOS (macOS Sonoma or later recommended), Linux, or Windows (WSL2)
* **Python Runtime:** Python `3.10.x` or `3.11.x`
* **Package Manager:** `pip` (updated to latest version)
* **Shell Environment:** **Zsh** terminal (default on macOS)
* **Database Instance:** Active Supabase project with database credentials (or local PostgreSQL 15+ instance)

---

## 💻 Local Setup & Installation (Zsh Guide)

Follow these exact shell commands in your **Zsh** terminal to configure and execute the application locally.

### Step 1: Clone the GitHub Repository
```zsh
git clone [https://github.com/your-username/vision-bank-analytics.git](https://github.com/your-username/vision-bank-analytics.git)
cd vision-bank-analytics
```

### Step 2: Set Up Python Virtual Environment
Create and activate an isolated Python virtual environment:
```zsh
# Create virtual environment named 'venv'
python3 -m venv venv

# Activate virtual environment in Zsh
source venv/bin/activate
```

*(Verify active environment: `which python` should point to `.../vision-bank-analytics/venv/bin/python`)*

### Step 3: Upgrade Package Manager & Install Dependencies
```zsh
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Local Environment Credentials
```zsh
cp .env.example .env
```
Open the `.env` file in your preferred code editor (e.g., VS Code) and update the placeholder connection parameters with your actual Supabase credentials.

### Step 5: Execute the Dashboard
```zsh
streamlit run app.py
```
The Streamlit local development server will start and automatically launch the application in your browser at `http://localhost:8501`.

---

## 🔑 Environment Configuration & Security

To maintain security compliance, connection credentials must never be hardcoded or committed to version control.

### Local `.env` File Format:
Create a `.env` file in the root directory:

```env
# Supabase PostgreSQL Configuration
SUPABASE_DB_HOST=db.xxxxxxxxxxxxxxxxxxxx.supabase.co
SUPABASE_DB_PORT=5432
SUPABASE_DB_NAME=postgres
SUPABASE_DB_USER=postgres
SUPABASE_DB_PASSWORD=your_ultra_secure_password_here

# Constructed Database Connection String
DATABASE_URL=postgresql://postgres:your_ultra_secure_password_here@db.xxxxxxxxxxxxxxxxxxxx.supabase.co:5432/postgres
```

### `.gitignore` Enforcement:
Ensure your `.gitignore` includes the following rules to prevent security leaks:
```gitignore
# Local Environment Files
.env
.env.local
venv/
__pycache__/
.streamlit/secrets.toml
```

---

## ⚡ Analytical Methods & Performance Optimization

To deliver high performance over cloud PostgreSQL database connections, Vision Bank Analytics incorporates several software optimization strategies:

### 1. Intelligent Data Caching (`@st.cache_data`)
Query results are wrapped inside Streamlit's `@st.cache_data(ttl=600)` decorator. This ensures that frequent dashboard navigation reuses cached Pandas DataFrames for up to 10 minutes, drastically reducing database load and connection costs.

```python
@st.cache_data(ttl=600)
def fetch_transaction_data():
    query = '''
    SELECT t.transaction_id, t.account_id, t.amount, t.type, t.timestamp, a.account_type, c.branch_id
    FROM transactions t
    JOIN accounts a ON t.account_id = a.account_id
    JOIN customers c ON a.customer_id = c.customer_id;
    '''
    return pd.read_sql(query, engine)
```

### 2. Connection Pooling
Database connections are maintained via SQLAlchemy's connection pool engine (`pool_size=10`, `max_overflow=20`), preventing connection overhead on every query.

### 3. Vectorized Pandas Calculations
Financial metrics (such as MoM growth rates, weighted average credit scores, and delinquent loan ratios) are computed using vectorized NumPy and Pandas operations rather than slow Python loops.

---

## ☁️ Cloud Deployment Strategy (Streamlit Cloud)

Vision Bank Analytics is optimized for zero-downtime deployment on **Streamlit Community Cloud**.

### Step-by-Step Cloud Deployment:

1. Push your updated code repository to GitHub (ensuring `.env` is ignored).
2. Log in to Streamlit Community Cloud with your GitHub account.
3. Click **New App**, select your `vision-bank-analytics` repository, and set the main file path to `app.py`.
4. Open **Advanced Settings > Secrets** and paste your database credentials in TOML format:

```toml
[postgres]
host = "db.xxxxxxxxxxxxxxxxxxxx.supabase.co"
port = 5432
dbname = "postgres"
user = "postgres"
password = "your_ultra_secure_password_here"
```

5. Click **Deploy**. Streamlit Cloud will install dependencies from `requirements.txt` and instantiate the app.

---

## 🗺 Future Roadmap & Modular Expansion

* **Predictive Credit Default Modeling:** Integrating scikit-learn machine learning models to score credit default probabilities dynamically based on historical repayment trends.
* **LedgerGuard Intelligence Engine Hook:** Connecting backend ledger validation algorithms to enforce strict double-entry balance auditing.
* **Automated Fraud Alert System:** Webhook integrations sending automated notifications (Twilio/SendGrid) when anomalous transaction spikes or suspicious wire transfers are flagged.
* **Automated PDF Executive Report Generation:** One-click PDF report export feature summarizing quarterly branch performance for executive board presentations.

---

## 👤 Author & Contact

**Anthony Nii Addo Nartey**  
*Data Analyst & Software Developer*  

* **Email:** anthonynartey481@icloud.com  
* **Tech Stack:** Python | SQL | PostgreSQL | Supabase | Streamlit | Plotly | DuckDB | Zsh
