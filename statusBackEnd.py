#!/usr/bin/python
import boto.ec2
conn = boto.ec2.connect_to_region("eu-central-1", aws_access_key_id='AKIAI111111111111111', aws_secret_access_key='keykeykey')
instance = conn.get_all_instances(instance_ids=['i-40e11111'])
print  instance[0].instances[0].state
