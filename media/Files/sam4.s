.include "defs.h"

.section .bss
argv:	.quad 0

.section .text
.global _start

space:		.byte ' '
newline:	.byte '\n'

_start:
/*
 * Layout of arguments on stack:
 *
 *   0(%rsp)  - argc
 *   8(%rsp)  - argv[0] - name of executable
 *   ...      - argc-1 arguments
 *   NULL
 *   ...      - envp[0] - environment
 *   NULL
 *  ...
 */
	leaq 8(%rsp), %rcx	/* rcx = rsp + 8 */
	movq %rcx, argv		/* argv = rcx */

	movq (%rcx), %rsi	/* rsi = *rcx */
	jmp strlen		/* goto strlen */

loop1: /* rcx is current argv */
	movq (%rcx), %rsi	/* rsi = *rcx */
	cmpq $0, %rsi		/* if ( rsi = NULL) */
	je end			/*    goto end */

	pushq %rsi		/* save rsi */

	/* write space */
	movq $SYS_WRITE, %rax
	movq $STDOUT, %rdi
	movq $space, %rsi
	movq $1, %rdx
	syscall

	popq %rsi		/* restore rsi */

strlen:
	movq %rsi, %rdi		/* rdi = rsi */
	cld			/* DF = 0 */
	xorb %al, %al		/* al = 0 */
	;movq $-1, %rcx		/* rcx = -1 = 0xFFFFFFFFFFFFFFFF */
	xorq %rcx, %rcx		/* rcx = 0 */
	decq %rcx		/* rcx-- */
	repnz scasb		/* repnz:  while !(ZF==1 || rcx == 0) {
				   scasb:      cmpb %al, (%rdi) ; DF==0 ? rdi++ : rdi--
				   repnz:  rcx--; } */
	xorq %rdx, %rdx		/* rdx = 0 */
	decq %rdx		/* rdx-- */
	subq %rcx, %rdx		/* rdx -= rcx */

	movq $SYS_WRITE, %rax
	movq $STDOUT, %rdi
	/* rsi = char* str */
	/* rdx = len(str) */
	syscall

	addq $8, argv		/* argv++ (pointer size = 8) */
	movq argv, %rcx		/* rcx = argv */
	jmp loop1		/* goto loop1 */

end:
	/* write newline */
	movq $SYS_WRITE, %rax
	movq $STDOUT, %rdi
	movq $newline, %rsi
	movq $1, %rdx
	syscall

	/* exit */
	movq $SYS_EXIT, %rax
	xorq %rdi, %rdi		/* rdi = 0 */
	syscall
