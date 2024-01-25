variable "credentials" {
  description = "My Credentials"
  default     = "../../keys/terraform-runner.json"
}


variable "project" {
  description = "Project ID"
  default     = "dtc-de-course-411515"
}

variable "region" {
  description = "Region"
  default     = "europe-west1"
}

variable "location" {
  description = "Project Location"
  default     = "EU"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "zoomcamp_week1"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "zoomcamp_week1"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
