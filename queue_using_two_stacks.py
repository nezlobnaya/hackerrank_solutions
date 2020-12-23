
in_stack, out_stack  = [], []

def enqueue(item):
    in_stack.append(item)


def dequeue():
    if len(out_stack) == 0:

            # Move items from in_stack to out_stack, reversing order
        while len(in_stack) > 0:
            newest_in_stack_item = in_stack.pop()
            out_stack.append(newest_in_stack_item)

            # If out_stack is still empty, raise an error
            if len(out_stack) == 0:
                raise IndexError("Can't dequeue from empty queue!")

    return out_stack.pop()

n = int(input())
for _ in range(n):
    data = list(input().split())
    
    if data[0]=='3':
        if not out_stack:
            print(in_stack[0])
        else:
            print(out_stack[-1])

    elif data[0]=='2':
           dequeue()   
           continue
        
    else:
        enqueue(data[1])
        