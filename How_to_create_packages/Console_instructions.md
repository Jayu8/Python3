>>cd ~\How_to_create_packages 
(no need to go inside mypackage)

>>python

Package:
>>import mypackage.demo
>>mypackage.demo.demoprint() (we get output)
OR
>>import mypackage.demo as de
>>de.demoprint()
OR
>> from mypackage.demo import demoprint()
>> demoprint()

Subpackage:
>>import mypackage.subpackage.subdemo
>>mypackage.subpackage.subdemo.subdemoprint()
OR
>>import mypackage.subpackage.subdemo as sd
>>sd.subdemoprint()
OR
>> from mypackage.subpackage.subdemo  import subdemoprint()
>> subdemoprint()

Ref : https://www.youtube.com/watch?v=qmsTqQbcBNM 
