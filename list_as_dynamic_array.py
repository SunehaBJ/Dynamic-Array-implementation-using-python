"""
Implementation on Dynamic Array in python
i.e, in-built List of python behaves as Dynamic Array
Author : Suneha Banu J
E-mail : suneha.hsd@gmail.com
LinkedIn : https://www.linkedin.com/in/suneha-banu-j-650b50bb/
Date : 10/02/2024
"""

import sys
import ctypes

class MyList:
    def __int__(self):
        self.size = 1
        self.n = 0
        self.A = self.__make_array(self.size)

    def __len__(self):
        return self.n

    def __str__(self):
        result =  ''
        for i in range(self.n):
            result = result + self.A[i] + ','
        return '['+ result[:-1] +']'

    def __getitem__(self,index):
        if 0 <= index < self.n:
            return A[index]
        else:
            return 'Index Error - Index is out of range'

    def append(self, item):
        if self.n == self.size:
            #resize : new array of double seize and copy the old array to new
            self.__resize(self.size*2)
        else:
            self.A[self.n] = item
            self.n = self.n + 1

    def pop(self):
        if self.n == 0:
            return 'Empty List'
        print(self.A[self.n-1])
        self.n = self.n - 1

    def clear(self):
        self.n = 0
        self.size = 1

    def find(self,item):
        for i in range(self.n):
            if self.A[i] == item:
                return i
        return 'valueError - not in list'

    def insert(self,pos, item):
        if 0 <= pos < self.n:
            if self.size == self.n:
                self.__resize(self.size*2)
            for i in range(self.n, pos, -1):
                self.A[i] = self.A[i-1]
            self.A[pos] = item
            self.n = self.n + 1
        else:
            return 'IndexError'

    def remove(self, item):
        pos = self.find(item)
        if type(pos) == int:
            #delete
            self.__delitem__(pos)
        else:
            return pos

    def __delitem__(self, pos):
        if 0 <= pos < self.n:
            for i in range(pos, self.n-1):
                self.A[i] = self.A[i+1]
        self.n = self.n - 1

    def __resize(self,new_capacity):
        #create a new array with new capacity
        B = self.__make_array(new_capacity)
        self.size = new_capacity
        #copy the content of A to new B
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B

    def __make_array(self, capacity):
        #cretaes a C type array(static, refrential) with size capacity
        return (capacity*ctypes.py_object)()

L = MyList()

