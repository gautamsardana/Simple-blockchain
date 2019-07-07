import hashlib

class blockchain:
    def __init__(self, sender, receiver, amount):
        self.sender=sender
        self.receiver=receiver
        self.amount=amount
        self.sender_arr, self.receiver_arr, self.amount_arr, self.hash_arr = [], [], [], []

    def view(self):
        print("sender\treceiver\tamount")
        for x in range(len(self.amount_arr)):
            print(str(self.sender_arr[x])+"\t\t\t"+str(self.receiver_arr[x])+"\t\t\t"+str(self.amount_arr[x]))

    def gather(self):
        self.one,self.two,self.three,self.four,self.five=1000,1000,1000,1000,1000
        print("\nEnter the sender, receiver and the amount separated by a space\n")
        self.sender,self.receiver,self.amount=map(int,input().split())
        self.sender_arr.append(self.sender)
        self.receiver_arr.append(self.receiver)
        self.amount_arr.append(str(self.amount))

    def new(self,hash_arr):
        self.hash_arr=hash_arr
        return(hash_arr)

bc=blockchain(0,0,0)
count=0
hash_arr = []

while (1):
    print("\nEnter what you want to do\n1) Transaction 2) View Transactions 3) Enter new block 0) Exit\n")
    n=input()
    if n=="1":
        bc.gather()

    elif n=="2":
        bc.view()

    elif n=="3":

        if count==0:
            total = "".join(bc.amount_arr)
            print("The sum of all transactions are: " + total)
            hashvalue = hashlib.sha512(total.encode()).hexdigest()
            print("Hash value of the transactions are: " + str(hashvalue))

            for x in range(100000):
                if hashlib.sha512(str(int(total) + x).encode()).hexdigest()[:3] == "aaa":
                    print("The seal or the proof of work of the transactions is: " + str(x))
                    hash_arr.append(hashlib.sha512(str(int(total) + x).encode()).hexdigest())
                    break

            print(bc.new(hash_arr))
            count+=1
            print(count)
            bc.__init__(0,0,0)
            print("-------------End of blockchain " + str(count) + "-----------")

        else:
            total = "".join(bc.amount_arr)
            print("The sum of all transactions are: " + total)
            hashvalue = hashlib.sha512(total.encode()).hexdigest()
            print("Hash value of the transactions are: " + str(hashvalue))
            prev_hash=hash_arr[-1]
            print("Hash value of the previous block was "+ prev_hash)

            for x in range(100000):
                if hashlib.sha512(str(int(total) + x + int(prev_hash,16)).encode()).hexdigest()[:3] == "aaa":
                    print("The seal or the proof of work of the transactions is: " + str(x))
                    hash_arr.append(hashlib.sha512(str(int(total) + x).encode()).hexdigest())
                    break

            print(bc.new(hash_arr))
            count += 1
            print("-------------End of blockchain "+ str(count)+"-----------")
            bc.__init__(0, 0, 0)

    else:
        exit()
