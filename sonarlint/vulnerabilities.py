def xxe_vulnerability():
    from lxml import etree
    parser = etree.XMLParser()
    etree.parse('resources/xxe.xml', parser)


def db_connect_no_password():
    import mysql
    mysql.connector.connect(host='localhost', user='sonarsource', password='')
    return "postgresql://user:@domain.com"


def robust_cypher_algo():
    from Cryptodome.Cipher import DES
    key = b'-8B key-'
    DES.new(key, DES.MODE_OFB)


def jwt_process_without_verify(token):
    import jwt
    jwt.process_jwt(token)


def predictable_salt(password):
    import hashlib
    salt = "string_literal"
    hashlib.pbkdf2_hmac('sha256', password, salt, 100000)
