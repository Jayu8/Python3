>>cd ~\How_to_create_packages 
(no need to go inside mypackage)

>>python

Package:
/>>/ import mypackage.demo<br>
>> mypackage.demo.demoprint()<br> (we get output)<br>
OR<br>
>>import mypackage.demo as de<br>
>>de.demoprint()<br>
OR<br>
>> from mypackage.demo import demoprint()<br>
>> demoprint()<br>

Subpackage:<br><br>
>>import mypackage.subpackage.subdemo<br>
>>mypackage.subpackage.subdemo.subdemoprint()<br>
OR<br>
>>import mypackage.subpackage.subdemo as sd<br><br>
>>sd.subdemoprint()<br>
OR<br><br><br><br>
>> from mypackage.subpackage.subdemo  import subdemoprint()<br>
>> subdemoprint()<br>

Ref : https://www.youtube.com/watch?v=qmsTqQbcBNM <br>
