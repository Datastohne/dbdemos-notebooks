# Databricks notebook source
# MAGIC %md 
# MAGIC ## Demo bundle configuration
# MAGIC Please ignore / do not delete, only used to prep and bundle the demo

# COMMAND ----------

{
  "name": "lakehouse-fsi-fraud",
  "category": "lakehouse",
  "title": "Retail Banking - Fraud Detection",
  "custom_schema_supported": True,
  "default_catalog": "main",
  "default_schema": "dbdemos_fsi_fraud_detection",
  "description": "Build your Banking platform and detect Fraud in real-time. End 2 End demo, with Model Serving & realtime fraud inference A/B testing.",
  "fullDescription": "The Databricks Lakehouse Platform is an open architecture that combines the best elements of data lakes and data warehouses. In this demo, we'll show you how to build a Real-time Fraud detection system for banking transactionn, delivering data and insights that would typically take months of effort on legacy platforms. <br/><br/>This demo covers the end to end lakehouse platform: <ul><li>Ingest data from external systems (EPR/Salesforce...) and then transform it using Delta Live Tables (DLT), a declarative ETL framework for building reliable, maintainable, and testable data processing pipelines. </li><li>Secure your ingested data to ensure governance and security on top of PII data</li><li>Leverage Databricks DBSQL and the warehouse endpoints to build dashboards to analyze the ingested data and understand the existing Fraud</li><li>Build a Machine Learning model with Databricks AutoML to flag transactions at risk</li><li>Leverage Databricks Model Serving to deploy a REST API serving real-time inferences in milliseconds with model A/B testing.</li><li>Orchestrate all these steps with Databricks Workflow</li></ul>",
  "usecase": "Lakehouse Platform",
  "products": ["Delta Live Tables", "Databricks SQL", "MLFLow", "Auto ML", "Unity Catalog"],
  "related_links": [
      {"title": "View all Product demos", "url": "<TBD: LINK TO A FILTER WITH ALL DBDEMOS CONTENT>"}, 
      {"title": "Databricks for Financial Services", "url": "https://www.databricks.com/solutions/industries/financial-services"}],
  "recommended_items": ["lakehouse-iot-platform", "lakehouse-fsi-credit", "lakehouse-retail-c360"],
  "demo_assets": [
      {"title": "Delta Live Table pipeline", "url": "https://www.dbdemos.ai/assets/img/dbdemos/lakehouse-fsi-fraud-dlt-0.png"},
      {"title": "Databricks SQL Dashboard: Credit Decisioning", "url": "https://www.dbdemos.ai/assets/img/dbdemos/lakehouse-fsi-fraud-dashboard-0.png"}],     
  "bundle": True,
  "tags": [{"dlt": "Delta Live Table"},  {"ds": "Data Science"}, {"uc": "Unity Catalog"}, {"dbsql": "BI/DW/DBSQL"}],
  "notebooks": [
    {
      "path": "_resources/00-setup", 
      "pre_run": False, 
      "publish_on_website": False, 
      "add_cluster_setup_cell": False,
      "title":  "Prep data", 
      "description": "Helpers & setup."
    },
    {
      "path": "_resources/01-load-data", 
      "pre_run": False, 
      "publish_on_website": False, 
      "add_cluster_setup_cell": False,
      "title":  "Prep data", 
      "description": "Prep data for demo."
    },
    {
      "path": "config", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Demo setup", 
      "description": "Setup schema and database name."
    },
    {
      "path": "00-FSI-fraud-detection-introduction-lakehouse", 
      "pre_run": False,
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Lakehouse - Fraud introduction", 
      "description": "Start here to explore the Lakehouse."
    },
    {
      "path": "01-Data-ingestion/01.1-DLT-fraud-detection-SQL", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Ingest data with Delta Live Table", 
      "description": "SQL DLT pipeline to ingest data & build clean tables."
    },
    {
      "path": "02-Data-governance/02-UC-data-governance-ACL-fsi-fraud", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Governance with Unity Catalog", 
      "description": "Secure your tables, lineage, auditlog..."
    },
    {
      "path": "03-BI-data-warehousing/03-BI-Datawarehousing-fraud", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Datawarehousing & BI / Dashboarding", 
      "description": "Run interactive queries on top of your data"
    },
    {
      "path": "04-Data-Science-ML/04.1-AutoML-FSI-fraud", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Build Fraud prediction model (AutoML)", 
      "description": "Leverage Databricks AutoML to create a Fraud model in a few clicks"
    },
    {
      "path": "04-Data-Science-ML/04.2-automl-generated-notebook-fraud",
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Explore Fraud Prediction generated model", 
      "description": "Explore the best Fraud model generated by AutoML and deploy it in production.",
      "parameters": {"shap_enabled": "true"}
    },
    {
      "path": "04-Data-Science-ML/04.3-Model-serving-realtime-inference-fraud", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Infer Fraud in realtime - serverless API", 
      "description": "Once your model is deployed, run low latency inferences."
    },
    {
      "path": "04-Data-Science-ML/04.4-Upgrade-to-imbalance-and-xgboost-model-fraud", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Upgrade our model to XGboost", 
      "description": "Improve AutoML model to handle imbalanced data."
    },
    {
      "path": "04-Data-Science-ML/04.5-AB-testing-model-serving-fraud", 
      "pre_run": True, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": True,
      "title":  "Roll-out our new model with A/B testing.", 
      "description": "Deploy the new model comparing its performance with the previous one."
    },
    {
      "path": "05-Workflow-orchestration/05-Workflow-orchestration-fsi-fraud", 
      "pre_run": False, 
      "publish_on_website": True, 
      "add_cluster_setup_cell": False,
      "title":  "Orchestrate churn prevention with Workflow", 
      "description": "Orchestrate all tasks in a job and schedule your data/model refresh"
    }
  ],
  "init_job": {
    "settings": {
        "name": "dbdemos_lakehouse_fsi_fraud_init_{{CURRENT_USER_NAME}}",
        "email_notifications": {
            "no_alert_for_skipped_runs": False
        },
        "timeout_seconds": 0,
        "max_concurrent_runs": 1,
        "tasks": [
            {
                "task_key": "init_data",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/_resources/01-load-data",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {}
            },
            {
                "task_key": "start_dlt_pipeline",
                "pipeline_task": {
                    "pipeline_id": "{{DYNAMIC_DLT_ID_dlt-fsi-fraud}}",
                    "full_refresh": false
                },
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                    {
                        "task_key": "init_data"
                    }
                ]
            },
            {
                "task_key": "create_feature_and_automl_run",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.1-AutoML-FSI-fraud",
                    "source": "WORKSPACE"
                },
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "start_dlt_pipeline"
                      }
                  ]
            },
            {
                "task_key": "register_model",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.2-automl-generated-notebook-fraud",
                    "source": "WORKSPACE"
                },
                "base_parameters": {"shap_enabled": "false"},
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "create_feature_and_automl_run"
                      }
                  ]
            },
            {
                "task_key": "create_model_serving_endpoint",
                "notebook_task": {
                    "notebook_path": "{{DEMO_FOLDER}}/04-Data-Science-ML/04.3-Model-serving-realtime-inference-fraud",
                    "source": "WORKSPACE"
                },
                "base_parameters": {"shap_enabled": "false"},
                "job_cluster_key": "Shared_job_cluster",
                "timeout_seconds": 0,
                "email_notifications": {},
                "depends_on": [
                      {
                          "task_key": "register_model"
                      }
                  ]
            }
        ],
        "job_clusters": [
            {
                "job_cluster_key": "Shared_job_cluster",
                "new_cluster": {
                    "spark_version": "15.3.x-cpu-ml-scala2.12",
                    "spark_conf": {
                        "spark.master": "local[*, 4]",
                        "spark.databricks.cluster.profile": "singleNode"
                    },
                    "custom_tags": {
                        "ResourceClass": "SingleNode"
                    },
                    "spark_env_vars": {
                        "PYSPARK_PYTHON": "/databricks/python3/bin/python3"
                    },
                    "enable_elastic_disk": True,
                    "data_security_mode": "SINGLE_USER",
                    "runtime_engine": "STANDARD",
                    "num_workers": 0
                }
            }
        ],
        "format": "MULTI_TASK"
    }
  },
  "cluster": {
      "spark_conf": {
        "spark.master": "local[*]",
        "spark.databricks.cluster.profile": "singleNode"
    },
    "custom_tags": {
        "ResourceClass": "SingleNode"
    },
    "spark_version": "15.3.x-cpu-ml-scala2.12",
    "single_user_name": "{{CURRENT_USER}}",
    "data_security_mode": "SINGLE_USER",
    "num_workers": 0
  }, 
  "pipelines": [
    {
      "id": "dlt-fsi-fraud",
      "run_after_creation": False,
      "definition": {
        "clusters": [
            {
                "label": "default",
                "autoscale": {
                    "min_workers": 1,
                    "max_workers": 2,
                    "mode": "LEGACY"
                }
            }
        ],
        "development": True,
        "continuous": False,
        "channel": "PREVIEW",
        "edition": "ADVANCED",
        "photon": True,
        "libraries": [
            {
                "notebook": {
                    "path": "{{DEMO_FOLDER}}/01-Data-ingestion/01.1-DLT-fraud-detection-SQL"
                }
            }
        ],
        "name": "dbdemos_fraud_{{CATALOG}}_{{SCHEMA}}",
        "catalog": "{{CATALOG}}",
        "target": "{{SCHEMA}}"
      }
    }
  ],
  "dashboards": [{"name": "[dbdemos] FSI Credit Decisioning Analysis",       "id": "credit-decisioning"}]
}
