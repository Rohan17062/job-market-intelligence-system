import pandas as pd
def job_title_analysis(conn):
    print("\n--- Job Title Analysis ---")

    query1 = """
    SELECT job_title, COUNT(*) as job_count
    FROM jobs
    GROUP BY job_title
    ORDER BY job_count DESC
    LIMIT 3
    """
    df1 = pd.read_sql(query1, conn)


    print("\nTop 3 Overall Job Roles:")
    for i in range(len(df1)):
        print(f"{i+1}. {df1.iloc[i]['job_title']} ({df1.iloc[i]['job_count']} jobs)")

    query2 = """
    SELECT job_title, COUNT(*) as job_count
    FROM jobs
    WHERE DATE(ingestion_timestamp) = (
        SELECT MAX(DATE(ingestion_timestamp)) FROM jobs
    )
    GROUP BY job_title
    ORDER BY job_count DESC
    LIMIT 3
    """
    df2 = pd.read_sql(query2, conn)
   

    print("\nTop 3 Recent Job Roles:")
    for i in range(len(df2)):
        print(f"{i+1}. {df2.iloc[i]['job_title']} ({df2.iloc[i]['job_count']} jobs)")

    overall_top=df1.iloc[0]['job_title']
    recent_top=df2.iloc[0]['job_title']

    if overall_top == recent_top:
        print(f"\nInsight: {recent_top} continues to dominate hiring both overall and recently.")
    else:
        print(f"\nInsight: Shift observed from {overall_top} (overall) to {recent_top} (recent).")


def experience_level_analysis(conn):

    print("\n--- Experience Level Analysis ---")

    
    query1 = """
    SELECT experience_level, COUNT(*) as job_count
    FROM jobs
    GROUP BY experience_level
    ORDER BY job_count DESC
    """
    df1 = pd.read_sql(query1, conn)
    

    print("\nOverall Experience Distribution:")
    for i in range(len(df1)):
        print(f"{df1.iloc[i]['experience_level']}: {df1.iloc[i]['job_count']} jobs")

    # 🔹 Recent
    query2 = """
    SELECT experience_level, COUNT(*) as job_count
    FROM jobs
    WHERE DATE(ingestion_timestamp) = (
        SELECT MAX(DATE(ingestion_timestamp)) FROM jobs
    )
    GROUP BY experience_level
    ORDER BY job_count DESC
    """
    df2 = pd.read_sql(query2, conn)

    print("\nRecent Experience Distribution:")
    for i in range(len(df2)):
        print(f"{df2.iloc[i]['experience_level']}: {df2.iloc[i]['job_count']} jobs")

    # Insight
    overall_top = df1.iloc[0]["experience_level"]
    recent_top = df2.iloc[0]["experience_level"]

    if overall_top == recent_top:
        print(f"\nInsight: {recent_top} level dominates both overall and recent hiring.")
    else:
        print(f"\nInsight: Shift observed from {overall_top} (overall) to {recent_top} (recent).")


def industry_analysis(conn):

    print("\n--- Industry Analysis ---")

    # Overall
    query1 = """
    SELECT industry, COUNT(*) as job_count
    FROM jobs
    GROUP BY industry
    ORDER BY job_count DESC
    LIMIT 3
    """
    df1 = pd.read_sql(query1, conn)

    print("\nTop 3 Industries Overall:")
    for i in range(len(df1)):
        print(f"{i+1}. {df1.iloc[i]['industry']} ({df1.iloc[i]['job_count']} jobs)")

    # Recent
    query2 = """
    SELECT industry, COUNT(*) as job_count
    FROM jobs
    WHERE DATE(ingestion_timestamp) = (
        SELECT MAX(DATE(ingestion_timestamp)) FROM jobs
    )
    GROUP BY industry
    ORDER BY job_count DESC
    LIMIT 3
    """
    df2 = pd.read_sql(query2, conn)

    print("\nTop 3 Industries Recent:")
    for i in range(len(df2)):
        print(f"{i+1}. {df2.iloc[i]['industry']} ({df2.iloc[i]['job_count']} jobs)")

    #  Insight
    overall_top = df1.iloc[0]["industry"]
    recent_top = df2.iloc[0]["industry"]

    if overall_top == recent_top:
        print(f"\nInsight: {recent_top} remains the leading industry in both overall and recent data.")
    else:
        print(f"\nInsight: Shift observed from {overall_top} (overall) to {recent_top} (recent).")


def company_size_analysis(conn):

    print("\n--- Company Size Analysis ---")

    # Overall
    query1 = """
    SELECT company_size, COUNT(*) as job_count
    FROM jobs
    GROUP BY company_size
    ORDER BY job_count DESC
    """
    df1 = pd.read_sql(query1, conn)

    print("\nOverall Company Size Distribution:")
    for i in range(len(df1)):
        print(f"{df1.iloc[i]['company_size']}: {df1.iloc[i]['job_count']} jobs")

    # Recent
    query2 = """
    SELECT company_size, COUNT(*) as job_count
    FROM jobs
    WHERE DATE(ingestion_timestamp) = (
        SELECT MAX(DATE(ingestion_timestamp)) FROM jobs
    )
    GROUP BY company_size
    ORDER BY job_count DESC
    """
    df2 = pd.read_sql(query2, conn)

    print("\nRecent Company Size Distribution:")
    for i in range(len(df2)):
        
        print(f"{df2.iloc[i]['company_size']}: {df2.iloc[i]['job_count']} jobs")

    # Insight
    overall_top = df1.iloc[0]["company_size"]
    recent_top = df2.iloc[0]["company_size"]

    if overall_top == recent_top:
        print(f"\nInsight: {recent_top} companies dominate hiring both overall and recently.")
    else:
        print(f"\nInsight: Shift observed from {overall_top} (overall) to {recent_top} (recent).")



def salary_analysis(conn):

    import pandas as pd

    print("\n--- Salary Analysis ---")

    # -------------------------
    # OVERALL ANALYSIS
    # -------------------------
    query = """
    SELECT job_title, salary_range_usd
    FROM jobs
    """
    df = pd.read_sql(query, conn)

    # Clean and split salary
    df = df.dropna(subset=['salary_range_usd'])
    df[['min_sal', 'max_sal']] = df['salary_range_usd'].str.split('-', expand=True)

    df['min_sal'] = pd.to_numeric(df['min_sal'], errors='coerce')
    df['max_sal'] = pd.to_numeric(df['max_sal'], errors='coerce')

    df = df.dropna(subset=['min_sal', 'max_sal'])

    df['avg_sal'] = (df['min_sal'] + df['max_sal']) / 2

    # Filter roles (>=3 occurrences)
    role_counts = df['job_title'].value_counts()
    valid_roles = role_counts[role_counts >= 3].index

    df_filtered = df[df['job_title'].isin(valid_roles)]

    df_overall = (
        df_filtered.groupby('job_title')['avg_sal']
        .mean()
        .sort_values(ascending=False)
        .head(3)
    )

    print("\nTop 3 Highest Paying Roles (Overall):")

    if not df_overall.empty:
        for i, (role, salary) in enumerate(df_overall.items()):
            print(f"{i+1}. {role} ({salary:.0f} USD avg)")
        overall_top = df_overall.index[0]
    else:
        print("No sufficient data for overall salary analysis.")
        overall_top = None

    # -------------------------
    # RECENT ANALYSIS
    # -------------------------
    query2 = """
    SELECT job_title, salary_range_usd
    FROM jobs
    WHERE DATE(ingestion_timestamp) = (
        SELECT MAX(DATE(ingestion_timestamp)) FROM jobs
    )
    """
    df2 = pd.read_sql(query2, conn)

    df2 = df2.dropna(subset=['salary_range_usd'])

    if not df2.empty:
        df2[['min_sal', 'max_sal']] = df2['salary_range_usd'].str.split('-', expand=True)

        df2['min_sal'] = pd.to_numeric(df2['min_sal'], errors='coerce')
        df2['max_sal'] = pd.to_numeric(df2['max_sal'], errors='coerce')

        df2 = df2.dropna(subset=['min_sal', 'max_sal'])

        df2['avg_sal'] = (df2['min_sal'] + df2['max_sal']) / 2

        # Filter roles (>=2 occurrences)
        role_counts2 = df2['job_title'].value_counts()
        valid_roles2 = role_counts2[role_counts2 >= 2].index

        df2_filtered = df2[df2['job_title'].isin(valid_roles2)]

        df_recent = (
            df2_filtered.groupby('job_title')['avg_sal']
            .mean()
            .sort_values(ascending=False)
            .head(3)
        )

        print("\nTop 3 Highest Paying Roles (Recent):")

        if not df_recent.empty:
            for i, (role, salary) in enumerate(df_recent.items()):
                print(f"{i+1}. {role} ({salary:.0f} USD avg)")
            recent_top = df_recent.index[0]
        else:
            print("No sufficient data for recent salary analysis.")
            recent_top = None
    else:
        print("\nNo recent data available.")
        recent_top = None

    # -------------------------
    # INSIGHT
    # -------------------------
    if overall_top and recent_top:
        print(f"\nTop paying role overall: {overall_top}")
        print(f"Top paying role recent: {recent_top}")

        if overall_top == recent_top:
            print(f"Insight: {recent_top} is highest paying in both overall and recent.")
        else:
            print(f"Insight: Shift from {overall_top} to {recent_top} in recent data.")

    elif overall_top:
        print(f"\nOnly overall data available. Top role: {overall_top}")

    elif recent_top:
        print(f"\nOnly recent data available. Top role: {recent_top}")

    else:
        print("\nNo sufficient data to generate salary insights.")
    
        
    
          
def run_all_analysis(conn):

    print("\n========== RUNNING FULL ANALYSIS ==========")

    job_title_analysis(conn)
    print("\n" + "-"*40)

    experience_level_analysis(conn)
    print("\n" + "-"*40)

    industry_analysis(conn)
    print("\n" + "-"*40)

    company_size_analysis(conn)
    print("\n" + "-"*40)

    salary_analysis(conn)

    
    
    
    
    
    




    





    




    

    
    
    
    

    
    
    