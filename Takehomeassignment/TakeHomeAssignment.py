from functools import reduce

# Question 1

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount: float):
        amount = float(amount)

        if amount > 0:
            self.balance += amount

        return self.balance

    def withdraw(self, amount: float):
        amount = float(amount)

        if amount > 0 and self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

        return self.balance

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def apply_interest(self):
        if self.balance <= 1000:
            interest = self.balance * 0.03
        elif self.balance <= 5000:
            interest = self.balance * 0.05
        else:
            interest = self.balance * 0.07

        self.balance += interest
        return self.balance

    def __str__(self):
        return f"Savings Account - Account holder: {self.account_holder}, Balance: ${self.balance}"


class CheckingAccount(BankAccount):
    def withdraw(self, amount: float):
        amount = float(amount)
        overdraft_fee = 25.0
        overdraft_limit = -500.0

        if amount <= 0:
            return self.balance

        new_balance = self.balance - amount

        if new_balance < 0:
            new_balance -= overdraft_fee

        if new_balance >= overdraft_limit:
            self.balance = new_balance
            print(f"New balance: ${self.balance}")
        else:
            print("Overdraft limit exceeded")

        return self.balance


# Question 2

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_cycle_length(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            count = 1
            current = slow.next

            while current != slow:
                count += 1
                current = current.next

            return count

    return -1



# Question 3

def findSmallestIndex(nums, target):
    min_after = float('inf')
    answer = -1

    for i in range(len(nums) - 2, -1, -1):
        min_after = min(min_after, nums[i + 1])

        if min_after > target:
            answer = i

    return answer


# Question 4

def process_pipeline(funcs):
    def pipeline(L):
        if funcs == []:
            return L

        return list(map(lambda x: reduce(lambda value, func: func(value), funcs, x), L))

    return pipeline


# Sample Tests

if __name__ == "__main__":

    #Sample Test Q1
    print("first test case Q1: output 700")
    savings = SavingsAccount("John Doe", 500)
    savings.deposit(200)
    print(savings.get_balance())

    print("second test case Q1: output 824")
    savings2 = SavingsAccount("John Doe", 800)
    savings2.apply_interest()
    print(savings2.get_balance())

    print("third test case Q1: output 1575")
    savings3 = SavingsAccount("Jane Smith", 1500)
    savings3.apply_interest()
    print(savings3.get_balance())

    print("fourth test case Q1: output -125")
    checking = CheckingAccount("Alex Lee", 200)
    checking.withdraw(300)
    print(checking.get_balance())

    #Sample Test Q2
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node3

    print(f"Test 1 (Expected 3): {find_cycle_length(node1)}")

    # Test Case 2: List with NO cycle
    # 1 -> 2 -> 3 -> None

    no_cycle_head = ListNode(1, ListNode(2, ListNode(3)))

    print(f"Test 2 (Expected -1): {find_cycle_length(no_cycle_head)}")   

    # Test Case 3: Empty List 
    print(f"Test 3 (Expected -1): {find_cycle_length(None)}")

    #Sample Test Q3
    print("first test case Q3: output 2")
    print(findSmallestIndex([1, 2, 5, 6, 7], 4))
    print("second test case Q3: output -1")
    print(findSmallestIndex([1, 3, 5, 7], 8))
    print("third test case Q3: output -1")
    print(findSmallestIndex([1, 2, 3, 4, 5], 5))

    #Sample Test Q4
    funcs = [lambda x: x + 1, lambda x: x * 2]
    pipeline = process_pipeline(funcs)
    print(pipeline([1, 2, 3]))