---
marp: true
title: FizzBuzz
theme: gaia
style: @import url('https://unpkg.com/tailwindcss@^2/dist/utilities.min.css');
---
1. 自我介绍
2. 什么是FizzBuzz
3. 知识点
    1. 编程技术

    2. 课堂练习
    2. 编程思维

5. 总结

---

## 自我介绍

姓名： 梁明浩
爱好：

---

## 什么是FizzBuzz

* 从1数到100
* 是三的倍数就喊“Fizz！”
* 是五的倍数就喊“Buzz！”
* 是十五的倍数就喊“FizzBuzz！”

---

## 知识点

用```for```循环输出1到100

```python
for i in range(1,101):
    print(i)
```

```
1
2
3
...
...
97
98
99
100
```

---
## 知识点
判断n的倍数：取余数运算 ```%```
<div class="grid grid-cols-2 gap-4">
<div>

```python
print(1%3)   ### 1
print(2%3)   ### 2
print(3%3)   ### 0
print(4%3)   ### 1
print(5%3)   ### 2
print(6%3)   ### 0
```

</div>

<div>

```python
print(1%3==0) ### False
print(2%3==0) ### False
print(3%3==0) ### True
print(4%3==0) ### False
print(5%3==0) ### False
print(6%3==0) ### True
```
</div>

---
## 知识点 
```if-elif-else``` 条件判断
<div class="grid grid-cols-2 gap-4">

<div>


90 ~ 100分： &nbsp;A
80 ~  90分：&emsp;B
70 ~  80分：&emsp;C
60 ~  70分：&emsp;D
60以下：&emsp;不及格

</div>

<div>

```python
if 90 <= 分数 < 100:
    print("A") 
elif 80 <= 分数:
    print("B")
elif 70 <= 分数: 
    print("C")
elif 60 <= 分数:
    print("D")
else:
    print("不及格")

```
</div>
</div>

---
## 代码实例

<div class="grid grid-cols-2 gap-4">
<div>

```python
for i in range(1,16):
    if i % 3  == 0:
        print("Fizz")
    if i % 5  == 0:
        print("Buzz")
    if i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i)
```

发现错误了吗？
该如何修改代码？
</div>
<div>

```
1
2
Fizz
3
4
Buzz
5
Fizz
6
7
8
Fizz
9
Buzz
10
11
Fizz
12
13
14
Fizz
Buzz
FizzBuzz
```
</div>

---
##  代码实例

<div class="grid grid-cols-2 gap-4">
<div>

```python
for i in range(1,16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3  == 0:
        print("Fizz")
    elif i % 5  == 0:
        print("Buzz")
    else:
        print(i)

```
</div>
<div>

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```
</div>

---
##  代码实例 (优化)

<div class="grid grid-cols-2 gap-4">
<div>

```python
for i in range(1,16):
    output = ""
    if i % 3  == 0:
        output = "Fizz"
    if i % 5  == 0:
        output += "Buzz"
    
    print(output or i)

```
</div>
<div>

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
```
</div>

---
##  代码实例 (对比)

<div class="grid grid-cols-2 gap-4">
<div>

```python
for i in range(1,16):
    output = ""
    if i % 3  == 0:
        output = "Fizz"
    if i % 5  == 0:
        output += "Buzz"
    print(output or i)
```
</div>
<div>

```python
for i in range(1,16):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3  == 0:
        print("Fizz")
    elif i % 5  == 0:
        print("Buzz")
    else:
        print(i)
```
</div>

---
##  代码实例 (进一步优化)

<div class="grid grid-cols-2 gap-4">
<div>

```python
for i in range(1,16):
    output = "fizz" if i % 3 == 0 else ""
    output += "buzz" if i % 5 == 0 else ""
    print(output or i)
```
</div>
<div>

```python
for i in range(1,16):
    print( ("fizz" * (i % 3 == 0) + "buzz"*(i % 5 == 0)) or i)
```
</div>
