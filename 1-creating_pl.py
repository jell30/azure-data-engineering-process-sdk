from azure.identity import DefaultAzureCredential
from azure.mgmt.datafactory import DataFactoryManagementClient
from azure.mgmt.datafactory.models import PipelineResource, CopyActivity, DatasetReference
# Set up authentication
credential = DefaultAzureCredential()

# Create a Data Factory management client
subscription_id = '63e68764-6c1e-4010-a6bf-0c967f06188c'
resource_group_name = 'rg-data'
factory_name = 'adf-dev-intern-data'

adf_client = DataFactoryManagementClient(credential, subscription_id)
# List pipelines
pipelines = adf_client.pipelines.list_by_factory(resource_group_name, factory_name)

# Print pipeline names
print("Existing pipelines:")
for pipeline in pipelines:
    print(f"- {pipeline.name}")