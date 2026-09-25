import pandas as pd
import requests

url = "https://himalayas.app/jobs/api"

# First, let's make a quick initial request just to check the total count
response = requests.get(url, params={"limit": 1})
if response.status_code == 200:
  initial_data = response.json()
  total_available = initial_data.get("totalCount", "Unknown")
  print(f"🔥 Total jobs available on the platform: {total_available}")
else:
  print("Could not retrieve total count.")

# Now, start collecting jobs using pagination
all_jobs = []
cursor = None
max_pages = 5  # You can increase this number if you want to download more pages
current_page = 1

print(
    f"\nStarting to fetch jobs with pagination (target: {max_pages}"
    " pages)..."
)

while current_page <= max_pages:
  params = {"limit": 20}
  if cursor:
    params["cursor"] = cursor

  response = requests.get(url, params=params)

  if response.status_code == 200:
    data = response.json()
    jobs_list = data.get("jobs", [])

    if not jobs_list:
      break

    all_jobs.extend(jobs_list)
    print(
        f"Page {current_page}: Fetched {len(jobs_list)} jobs (Total collected:"
        f" {len(all_jobs)})"
    )

    cursor = data.get("nextCursor")
    if not cursor:
      print("Reached the end of the feed.")
      break

    current_page += 1
  else:
    print(f"Error: {response.status_code}")
    break

# Process and save to Excel
if all_jobs:
  parsed_data = []
  for job in all_jobs:
    parsed_data.append({
        "Title": job.get("title"),
        "Company": job.get("companyName"),
        "Location": job.get("locationRestrictions", "Worldwide"),
        "Link": job.get("applicationLink"),
    })

  df = pd.DataFrame(parsed_data)
  df.to_excel("job_aggregator_output.xlsx", index=False)
  print(
      f"\nSuccess! Saved {len(parsed_data)} jobs to 'himalayas_all_jobs.xlsx'."
  )
else:
  print("No jobs found.")