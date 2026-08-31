import pandas as pd

FILENAME = 'support_tickets.csv'

df = pd.read_csv(FILENAME)
# print(df.to_string())

# Find Total ticket count
print(f"Total ticket count: {df.shape[0]}")
print("-----------------")

# Count ticket by category
count_ticket_by_cat = df.groupby('category')['ticket_id'].count()
print(f"Count ticket by category: \n{count_ticket_by_cat}")
print("-----------------")

# Count ticket by priority
count_ticket_by_priority = df.groupby('priority')['ticket_id'].count()
print(f"Count ticket by priority: \n{count_ticket_by_priority}")
print("-----------------")

# Count ticket by status
count_ticket_by_status = df.groupby('status')['ticket_id'].count()
print(f"Count ticket by status: \n{count_ticket_by_status}")
print("-----------------")

# Find open tickets
opentickets_list = df.loc[df['status'] == 'Open']
print(f"Open ticket list: \n{opentickets_list}")
print(f"Open ticket list -2: \n{df[df['status'] == 'Open']}")
print("-----------------")

# Find closed tickets
closedtickets_list = df.loc[df['status'] == 'Closed']
print(f"Closed ticket list: \n{closedtickets_list}")
print(f"Closed ticket list -2: \n{df[df['status'] == 'Closed']}")
print("-----------------")

# Find resolved tickets
resolved_tickets_list = df.loc[df['status'] == 'Resolved']
print(f"Resolved ticket list: \n{resolved_tickets_list}")
print(f"Resolved ticket list -2: \n{df[df['status'] == 'Resolved']}")
print("-----------------")

# Find average resolution time
print(f"Resolution time: {df['resolution_time'].mean()}")
print("-----------------")

# Find average resolution time per category
print(
    f"Resolution time per category: \n{df.groupby('category')['resolution_time'].mean()}")
print("-----------------")

# Find tickets handled by each support agent
ticket_count = (
    df.groupby("assigned_agent")
      .size()
      .reset_index(name="total_tickets")
      .sort_values("total_tickets", ascending=False)
)
print(
    f"Find tickets handled by each support agent: \n{ticket_count}")
print("-----------------")

# Sort ticket by resolution time
sort_resolution_time = df.sort_values('resolution_time', ascending=False)
print(f"Sort ticket by resolution: \n {sort_resolution_time}")
print("-----------------")

# Find ticket taking maximum resolution time
ticket_by_max_resolution_time = df.sort_values(
    'resolution_time', ascending=False).head(5)
print(
    f"Ticket by taking maximum resolution time: \n {ticket_by_max_resolution_time}")

# Export by summary report
ticket_count.to_csv("summary.csv", index=False)
