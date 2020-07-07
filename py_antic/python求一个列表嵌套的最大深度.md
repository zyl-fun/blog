### python求一个列表嵌套的最大深度

```python
list_test = [1,[222,222,222,33,[67,[66,[33333,[7777777,[7777777777]]]],777]]]
print(list_test)


def depth_count(lists,x=0):
    if not lists or not isinstance(lists,list):
        return x
    l = depth_count(lists[0],x + 1)
    r = depth_count(lists[1:],x)

    return max(l,r)

if __name__ == '__main__':
    print(depth_count(list_test))
```

