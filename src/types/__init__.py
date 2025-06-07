class DataType:
    STRING = 'string'
    LIST = 'list'
    SET = 'set'
    HASH = 'hash'
    ZSET = 'zset'

class Status:
    OK = 'OK'
    ERROR = 'ERROR'

class Command:
    SET = 'SET'
    GET = 'GET'
    DEL = 'DEL'
    LPUSH = 'LPUSH'
    RPUSH = 'RPUSH'
    LPOP = 'LPOP'
    SADD = 'SADD'
    HSET = 'HSET'
    ZADD = 'ZADD'