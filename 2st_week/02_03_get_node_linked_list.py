class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node = Node(3)


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    # LinkedList 의 가장 끝에 있는 노드에 새로운 노드를 연결해줘
    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    # linked_list 에서 저장한 head를 따라가서 현재 있는 노드들을 전부 출력시켜주는 함수
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 입력받은 인덱스의 속해있는 node 구하기
    def get_node(self, value):
        cur = self.head
        cur_index = 0
        while cur is not None:
            if value != cur_index:
                cur = cur.next
                cur_index += 1
            else:
                return cur.data

linked_list = LinkedList(5)
linked_list.append(12)
# 이렇게 되면 5 -> 12 형태로 노드를 연결한 겁니다!
linked_list.append(8)
# 이렇게 되면 5 -> 12 -> 8 형태로 노드를 연결한 겁니다!

# linked_list.print_all()

# 1번 인덱스의 요소 프린트
print(linked_list.get_node(1))