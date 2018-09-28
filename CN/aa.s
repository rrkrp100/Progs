	.file	"udpServer.c"
	.text
	.section	.rodata
.LC0:
	.string	"Hello from the sever side"
.LC1:
	.string	"Socket failed"
.LC2:
	.string	"Bind Failed"
.LC3:
	.string	"Client: %s\n"
.LC4:
	.string	"Msg sent "
	.text
	.globl	main
	.type	main, @function
main:
.LFB5:
	.cfi_startproc
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register 6
	pushq	%rbx
	subq	$1112, %rsp
	.cfi_offset 3, -24
	movq	%fs:40, %rax
	movq	%rax, -24(%rbp)
	xorl	%eax, %eax
	leaq	.LC0(%rip), %rax
	movq	%rax, -1096(%rbp)
	movl	$0, %edx
	movl	$2, %esi
	movl	$2, %edi
	call	socket@PLT
	movl	%eax, -1104(%rbp)
	cmpl	$0, -1104(%rbp)
	jns	.L2
	leaq	.LC1(%rip), %rdi
	call	puts@PLT
	movl	$0, %edi
	call	exit@PLT
.L2:
	leaq	-1088(%rbp), %rax
	movl	$16, %esi
	movq	%rax, %rdi
	call	bzero@PLT
	leaq	-1072(%rbp), %rax
	movl	$16, %esi
	movq	%rax, %rdi
	call	bzero@PLT
	movw	$2, -1088(%rbp)
	movl	$0, -1084(%rbp)
	movl	$8080, %edi
	call	htons@PLT
	movw	%ax, -1086(%rbp)
	leaq	-1088(%rbp), %rcx
	movl	-1104(%rbp), %eax
	movl	$16, %edx
	movq	%rcx, %rsi
	movl	%eax, %edi
	call	bind@PLT
	testl	%eax, %eax
	jns	.L3
	leaq	.LC2(%rip), %rdi
	call	puts@PLT
	movl	$0, %edi
	call	exit@PLT
.L3:
	leaq	-1108(%rbp), %rcx
	leaq	-1072(%rbp), %rdx
	leaq	-1056(%rbp), %rsi
	movl	-1104(%rbp), %eax
	movq	%rcx, %r9
	movq	%rdx, %r8
	movl	$0, %ecx
	movl	$1024, %edx
	movl	%eax, %edi
	call	recvfrom@PLT
	movl	%eax, -1100(%rbp)
	movl	-1100(%rbp), %eax
	cltq
	movb	$0, -1056(%rbp,%rax)
	leaq	-1056(%rbp), %rax
	movq	%rax, %rsi
	leaq	.LC3(%rip), %rdi
	movl	$0, %eax
	call	printf@PLT
	movl	-1108(%rbp), %eax
	movl	%eax, %ebx
	movq	-1096(%rbp), %rax
	movq	%rax, %rdi
	call	strlen@PLT
	movq	%rax, %rdi
	leaq	-1072(%rbp), %rdx
	movq	-1096(%rbp), %rsi
	movl	-1104(%rbp), %eax
	movl	%ebx, %r9d
	movq	%rdx, %r8
	movl	$0, %ecx
	movq	%rdi, %rdx
	movl	%eax, %edi
	call	sendto@PLT
	leaq	.LC4(%rip), %rdi
	call	puts@PLT
	movl	$0, %eax
	movq	-24(%rbp), %rbx
	xorq	%fs:40, %rbx
	je	.L5
	call	__stack_chk_fail@PLT
.L5:
	addq	$1112, %rsp
	popq	%rbx
	popq	%rbp
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE5:
	.size	main, .-main
	.ident	"GCC: (Ubuntu 7.3.0-16ubuntu3) 7.3.0"
	.section	.note.GNU-stack,"",@progbits
