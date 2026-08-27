# Databricks notebook source
# MAGIC %run "/Workspace/optum/connectors"
# MAGIC

# COMMAND ----------

# MAGIC %run "/Workspace/optum/generic"

# COMMAND ----------

hos_df = read_bronze_csv("Hospital")

# COMMAND ----------

df_row_columns(hos_df)

# COMMAND ----------

check_missing_values(hos_df,hos_df.columns)

# COMMAND ----------

check_string_as_nan(hos_df)

# COMMAND ----------

check_duplicates(hos_df,hos_df.columns)

# COMMAND ----------

hos_df = hos_df.replace("NaN",None)

# COMMAND ----------

display(hos_df)  #action

# COMMAND ----------

#actual transformations
hos_df = hos_df.fillna({'state':"UT"})
hos_df = hos_df.replace("New Delhi", "Delhi")

# COMMAND ----------

display(hos_df)

# COMMAND ----------

write2silver(hos_df,"Hospital_S.csv")