	.file	"test.c"
	.text
	.globl	_swap
	.def	_swap;	.scl	2;	.type	32;	.endef
_swap:
LFB6:
	.cfi_startproc          #.xxx都是写给编译器看的，忽略
	pushl	%ebp            #保存调用swap前的ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp      #将调用函数前的栈顶作为ebp
	.cfi_def_cfa_register 5
	subl	$16, %esp       #扩充函数栈，但16字节对齐
	movl	8(%ebp), %eax   #将*(ebp+8)放到eax里，即&x，也即a
	movl	(%eax), %eax    #取*eax到eax里，即获得x
	movl	%eax, -4(%ebp)  #将x放到tmp里
	movl	12(%ebp), %eax  #将b放到eax里，待用
	movl	(%eax), %edx    #取*b，放到edx里。eax要给a用
	movl	8(%ebp), %eax   #把a取出来，放到eax里
	movl	%edx, (%eax)    #把*b赋值给*a
	movl	12(%ebp), %eax  #再把b放到eax
	movl	-4(%ebp), %edx  #把tmp放到edx
	movl	%edx, (%eax)    #把tmp赋值给*b
	movl	-4(%ebp), %eax  #把tmp赋值给eax，作为返回值
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret                     #相当 mov %ebp, %esp; pop %ebp
	.cfi_endproc            #esp回到原栈顶，ebp回到swap前
LFE6:
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
LC0:
	.ascii "ret: %d\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB7:
	.cfi_startproc
	pushl	%ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	movl	%esp, %ebp
	.cfi_def_cfa_register 5
	andl	$-16, %esp
	subl	$32, %esp
	call	___main
	movl	$16, 24(%esp)
	movl	$32, 20(%esp)
	leal	20(%esp), %eax
	movl	%eax, 4(%esp)
	leal	24(%esp), %eax
	movl	%eax, (%esp)
	call	_swap
	movl	%eax, 28(%esp)
	movl	28(%esp), %eax
	movl	%eax, 4(%esp)
	movl	$LC0, (%esp)
	call	_printf
	movl	$0, %eax
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE7:
	.ident	"GCC: (GNU) 4.8.1"
	.def	_printf;	.scl	2;	.type	32;	.endef
