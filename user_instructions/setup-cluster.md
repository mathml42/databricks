# Set up a Databricks Cluster

For any workload in Databricks, you'll need a cluster. You can create a cluster (menu item: Create > Cluster) through the UI.

## Through the UI

1. Choose `Compute` in the left navigation:
![databricks-create-cluster-menu-selection](./assets/databricks-create-cluster-menu-selection.png)

2. Create a cluster with the following parameters (:bulb: there may be a pre-existing cluster policy with these exact parameters):
![databricks-create-cluster.png](./assets/databricks-create-cluster.png)

If you want to share a cluster with a colleague, you can create a shared-environment.
![databricks-select-cluster-shared.png](./assets/databricks-select-cluster-shared.png)

In a `no isolation shared` environment, everybody in the team can execute notebooks on your cluster. This helps a lot when working together in smaller groups on the same notebook.

3. Confirm by clicking the `Create Cluster` button at the bottom of the page.