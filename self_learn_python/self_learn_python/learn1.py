# encoding=utf-8
import redis

if __name__ == '__main__':
    try:
        rs = redis.Redis(host='192.168.1.8')
        # result = rs.set('name', 'Godlike')
        # print(result)
        result = rs.get('name')
        print(result)
    except Exception as e:
        print(e)

