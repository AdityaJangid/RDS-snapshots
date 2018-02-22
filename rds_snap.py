import boto3
import datetime
from datetime import timedelta

now = str(datetime.datetime.now()).split()[0]
client = boto3.client('rds')

db_instances = ["snap"]
db_clusters = ["clusters"]

## snapshot of RDS instance
def create_instance_snapshot(instance, instance_snapshot_identifier):
    db_snapshot_response = client.create_db_snapshot(
              DBSnapshotIdentifier=instance_snapshot_identifier,
              DBInstanceIdentifier=instance
              )

## delete previous snapshots

def del_instnace_snapshot(instance, instance_snapshot_identifier):
    snapshots = client.describe_db_snapshots(DBInstanceIdentifier=instance, SnapshotType='manual')['DBSnapshots']
    for snapshot in snapshots:
        print(snapshot['DBSnapshotIdentifier'])
        if(snapshot['DBSnapshotIdentifier'] != instance_snapshot_identifier or snapshot['DBSnapshotIdentifier'] != '%s-%s' % (instance,(datetime.datetime.now() - timedelta(days=1)).strftime("%y-%m-%d") )):
            response = client.delete_db_snapshot( DBSnapshotIdentifier=snapshot['DBSnapshotIdentifier'])

### snapshot of cluster
def create_cluster_snapshot():
    cluster_snapshot_response = client.create_db_cluster_snapshot(
                  DBClusterSnapshotIdentifier=cluster_snapshot_identifier,
                  DBClusterIdentifier=cluster
                  )

def main():
    for instance in db_instances:
        #  instance_snapshot_identifier = '%s-'+ now % (instance)
        instance_snapshot_identifier = '{0}-'.format(instance)+ now
        #  create_instance_snapshot(instance, instance_snapshot_identifier)
        del_instnace_snapshot(instance, instance_snapshot_identifier)

    #  for cluster in db_clusters:
    #      #  cluster_snapshot_identifier = '%s-'+ now % (cluster)
    #      instance_snapshot_identifier = '{0}-'.format(cluster)+ now
    #      create_cluster_snapshot(cluster, cluster_snapshot_identifier)
    #

if __name__ == "__main__":
    main()
