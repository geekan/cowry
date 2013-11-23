
Title: C陷阱与缺陷 - 笔记
Email: ether.wcl@gmail.com
------------------

1. 难以简单debug出的错误  
注意运算符两旁要空格, 否则会造成歧义.  
`y = x/*p /* p points at the divisor */;`
在老版本的C代码中, 下面这句等同于 `a-=1`
`a=-1;`


































