import pandas as pd
from datetime import datetime

class AlertSystem:

    def __init__(self, conn):
        self.conn = conn

    def check_job_drop_spike_alert(self):

        query = """
        SELECT DATE(ingestion_timestamp) as dat, COUNT(*) as job_count
        FROM jobs
        GROUP BY DATE(ingestion_timestamp)
        ORDER BY DATE(ingestion_timestamp)
        """
        df = pd.read_sql(query, self.conn)

        if len(df) < 2:
            print("Insufficient data for checking alert")
            return

        prev_jobs = df.iloc[-2]["job_count"]
        curr_jobs = df.iloc[-1]["job_count"]

        prev_date = df.iloc[-2]["dat"]
        curr_date = df.iloc[-1]["dat"]

        if prev_jobs > 0:

            drop = (prev_jobs - curr_jobs) / prev_jobs
            spike = (curr_jobs - prev_jobs) / prev_jobs

            # DROP ALERT
            if drop >= 0.3:
                msg = f"Job DROP alert: {prev_date} -> {curr_date} ({drop*100:.1f}% drop)"

                # check duplicate using pandas
                check_df = pd.read_sql(
                    f"SELECT * FROM alerts WHERE alert_msg = '{msg}'",
                    self.conn
                )

                if check_df.empty:
                    print("ALERT:", msg)
                    self.conn.execute(
                        "INSERT INTO alerts (alert_msg, alert_time, alert_type) VALUES (?, ?, ?)",
                        (msg, datetime.now(),"DROP")
                    )
                else:
                    print("Duplicate alert skipped")

            # SPIKE ALERT
            if spike >= 0.6:
                msg = f"Job SPIKE alert: {prev_date} -> {curr_date} ({spike*100:.1f}% increase)"

                check_df = pd.read_sql(
                    f"SELECT * FROM alerts WHERE alert_msg = '{msg}'",
                    self.conn
                )

                if check_df.empty:
                    print("ALERT:", msg)
                    self.conn.execute(
                        "INSERT INTO alerts (alert_msg, alert_time, alert_type) VALUES (?, ?,?)",
                        (msg, datetime.now(),"SPIKE")
                    )
                else:
                    print("Duplicate alert skipped")

        self.conn.commit()