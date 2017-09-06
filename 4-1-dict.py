# -*- coding:utf-8 -*-
people ={
    'yep':{
        'name':u'叶鹏',
        'email':'yepeng@utry.cn'
    },
     'cm':{
         'name':u'陈萌',
         'email':'chenmeng@utry.cn'
    }
}

lables = {
    'name':u'姓名',
    'email':u'邮箱'
}

uname = raw_input("uname: ")
#if request == 'n': key = 'name'
#if request == 'e': key = 'email'

if uname in people: 
     print u"%s 对应%s是%s." % (uname, lables['name'], people[uname]['name'])
     print u"%s 对应%s是%s." % (uname, lables['email'], people[uname]['email'])

