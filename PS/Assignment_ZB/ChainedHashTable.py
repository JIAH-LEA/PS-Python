## 난이도: *****
# HashTable 클래스는 문자열을 key로 입력받는 해쉬 테이블 자료구조를 구현한 것이다.
# HashTable을 상속하여 해쉬 충돌이 발생해도 정상적으로 동작하는 ChainedHashTable을 완성하시오.
# 아스키코드 변환 함수: ord()


def hash_func(key):
    return ord(key[0]) % 10

class HashTable:
    def __init__(self):
        self.table = [None]*10

    def set(self, key, value):
        self.table[hash_func(key)] = value

    def get(self, key):
        return self.table[hash_func(key)]

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None

class ChainedHashTable(HashTable):
    def __init__(self):
        super().__init__()
    
    def set(self, key, value):
        item = self.hash_func(key)
        if self.table[item] is None:
            self.table[item] = Node(key, value)
        else:
            existed = self.table[item]
            while existed.next is not None:
                if existed.key == key:
                    existed.data = value
                return node = node.next
            node.next = Node(key, value)
            
    def get(self, key):
        item = self.hash_func(key)
        if self.table[item] is None:
            return None
        else:
            existed = self.table[item]            
            while existed.next is not None:
                if existed.key == key:
                    return existed.data
                existed = existed.next
            if existed.key == key:
                return existed.data
            else:
                return None # 그 키가 끝까지 존재하지 않음 

    

# Test code

ht = ChainedHashTable()
ht.set('hello', 1)
ht.set('hello2', 2)
ht.set('hello3', 3)
ht.set('hello4', 4)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
print()

ht.set('hello2', 5)

print(ht.get('hello'), end=' ')
print(ht.get('hello2'), end=' ')
print(ht.get('hello3'), end=' ')
print(ht.get('hello4'), end=' ')
