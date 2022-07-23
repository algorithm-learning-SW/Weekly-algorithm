class DLL:
    class Node:
       def __init__(self, item, prv, nxt):
           self.item=item
           self.prv=prv
           self.nxt=nxt

    def __init__(self):
        self.head=self.Node(None, None, None)
        self.tail=self.Node(None, self.head, None)
        self.head.nxt=self.tail
        self.size=0
    '''
    def insert_head(self, item):
        newNode=self.Node(item, None, None)
        newNode.nxt=self.head
        self.head.prv=newNode
        self.head=newNode
        self.size+=1

    def insert_tail(self, item):
        newNode=self.Node(item, None, None)
        self.tail.nxt=newNode
        newNode.prv=self.tail
        self.tail=newNode
        self.size+=1
    '''
    def insert_before(self, item, nd):
        newNode=DLL.Node(item, None, None)
        newNode.nxt=nd
        newNode.prv=nd.prv
        nd.prv.nxt=newNode
        nd.prv=newNode
        self.size+=1
        
    def insert_after(self, item, nd):
        newNode=DLL.Node(item, None, None)
        nd.nxt.prv=newNode
        newNode.nxt=nd.nxt
        newNode.prv=nd
        nd.nxt=newNode
        self.size+=1

    def delete(self, nd):
        if self.size==0:
            raise "empty DLL"
        nd.prv.nxt=nd.nxt
        nd.nxt.prv=nd.prv
        self.size-=1
        return nd.item

    def print_backwards(self):
        nd=self.head.nxt
        while nd!=self.tail:
            if nd.nxt!=self.tail:
                print(nd.item, '=> ', end='')
            else:
                print(nd.item)
            nd=nd.nxt

def solution(s):
    sList=list(s)
    linkedList=DLL()
    for element in sList:
        linkedList.insert_before(element, linkedList.tail)
    linkedList.print_backwards()

    node=linkedList.head.nxt
    while(True):
        linkedList.print_backwards()
        if linkedList.size==0:
            break
        if node==linkedList.tail:
            break
        if node.item==node.nxt.item:
            linkedList.delete(node.nxt)
            node=node.prv
            linkedList.delete(node.nxt)
        elif node.item==node.prv.item:
            linkedList.delete(node.prv)
            node=node.nxt
            linkedList.delete(node.prv)
            node=node.prv
        
        node=node.nxt
        
    if linkedList.size!=0:
        return 0
    else:
        return 1
print(solution("baabaa"))
print(solution("cdcd"))
print(solution("abcddcba"))
