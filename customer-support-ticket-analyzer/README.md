# Customer Support Ticket Analyzer

This project uses Python and pandas to analyze a customer-support ticket
dataset. It summarizes ticket volume, status, priority, resolution time, and
support-agent workload.

## Project Structure

```text
customer-support-ticket-analyzer/
|-- main.py
|-- support_tickets.csv
|-- summary.csv
`-- README.md
```

- `main.py` — reads the dataset, performs the analysis, and exports a summary
- `support_tickets.csv` — source dataset containing 60 tickets
- `summary.csv` — generated ticket count for each assigned agent

## Dataset Columns

| Column | Description |
|---|---|
| `ticket_id` | Unique ticket identifier |
| `customer_name` | Name of the customer |
| `category` | Type of support request |
| `priority` | Urgency of the ticket |
| `status` | Current ticket state |
| `assigned_agent` | Support agent handling the ticket |
| `resolution_time` | Resolution duration in hours |

### Categories

- Payment
- Technical
- Login
- Course
- Refund
- Account

### Priorities

- Low
- Medium
- High
- Critical

### Status Values

- Open
- In Progress
- Resolved
- Closed

`resolution_time` is empty for unresolved Open and In Progress tickets. Pandas
reads those empty fields as missing values (`NaN`) and excludes them from mean
resolution-time calculations.

## Analysis Performed

The program calculates and displays:

- Total ticket count
- Ticket count by category
- Ticket count by priority
- Ticket count by status
- Open tickets
- Closed tickets
- Resolved tickets
- Overall average resolution time
- Average resolution time by category
- Number of tickets handled by each support agent
- Tickets sorted by resolution time
- Five tickets with the longest resolution times

It demonstrates pandas operations including:

- `pd.read_csv()`
- `DataFrame.shape`
- Boolean filtering with `loc[]`
- `groupby()`
- `count()`, `size()`, and `mean()`
- `reset_index()`
- `sort_values()`
- `head()`
- `to_csv()`

## Requirements

- Python 3.8 or newer
- pandas

Install pandas with:

```bash
python -m pip install pandas
```

## Run the Project

Open a terminal in the project directory and run:

```bash
python main.py
```

The analysis is printed in the terminal, and `summary.csv` is created or
replaced with the agent workload report.

## Current Dataset Summary

- Total tickets: 60
- Total categories: 6
- Support agents: 6
- Tickets assigned to each agent: 10
- Duplicate ticket IDs: 0
