# master node setup
locust -f locustfile.py --worker --master-host=192.168.56.1

app.run(host='host-ipv4')