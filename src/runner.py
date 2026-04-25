import sqlite3
import pipeline
import analysis
import pandas as pd

print("\n====RUNNING SYSTEM ====")

conn=sqlite3.connect("data/jobss.db")
print("\n===Running Pipeline ===")
pipeline.run_pipeline(conn)

print("\n--Checking Alerts--")
from alertt import AlertSystem
ale=AlertSystem(conn)
ale.check_job_drop_spike_alert()
query="""
select * from alerts
"""
df=pd.read_sql(query,conn)
df.to_csv("alerts_table.csv",index=False)
print("alerts csv updated succesfully")


print("\n--Running Analysis--")
analysis.run_all_analysis(conn)

print("\n--Exporting data for power bi--")


query="""
select * from jobs
"""
df=pd.read_sql(query,conn)
df.to_csv("jobs_data.csv",index=False)
print("csv updated succesfully")

conn.close()
print("System running complete")

