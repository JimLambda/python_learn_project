import rediscluster


if __name__ == '__main__':
    nodes = [{'host': '192.168.1.8', 'port': '7000'},
             {'host': '192.168.1.8', 'port': '7001'},
             {'host': '192.168.1.8', 'port': '7002'},
             {'host': '192.168.1.8', 'port': '7003'},
             {'host': '192.168.1.8', 'port': '7004'},
             {'host': '192.168.1.8', 'port': '7005'}]

    try:
        rc = rediscluster.RedisCluster(startup_nodes=nodes)

        result = rc.get('name')
        print(result)
    except Exception as e:
        print(e)
