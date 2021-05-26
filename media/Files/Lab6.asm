;11c+3aad - e/b
.686                  
.model flat, stdcall  
option casemap:none   

include \masm32\include\windows.inc
include \masm32\macros\macros.asm

include \masm32\include\masm32.inc
include \masm32\include\kernel32.inc

includelib \masm32\lib\masm32.lib
includelib \masm32\lib\kernel32.lib

include \masm32\include\masm32rt.inc
includelib \masm32\lib\user32.lib

include \masm32\include\msvcrt.inc
includelib \masm32\lib\msvcrt.lib

include \masm32\MasmBasic\MasmBasic.inc
func PROTO :real4, :real4, :real4, :real4, :real4
func1 PROTO :real8, :real8, :real8, :real8, :real8
func2 PROTO :real10, :real10, :real10, :real10, :real10

.data?
res real8 ?
res0 real8 ?
res1 real8 ?
res11 real8 ?
res2 real10 ?
res22 real10 ?
.data
const11 real4 11.0
const12 real4 3.0
const21 real8 11.0
const22 real8 3.0
const31 real10 11.0
const32 real10 3.0

av real4 2.0
bv real4 1.4
cv real4 1.0
dv real4 1.2
ev real4 1.0

av1 real8 2.0
bv1 real8 1.4
cv1 real8 1.0
dv1 real8 1.2
ev1 real8 1.0

av2 real10 2.0
bv2 real10 1.4
cv2 real10 1.0
dv2 real10 1.2
ev2 real10 1.0

MsgBoxCaption db "Result", 0

fmt db "Float %s",10,0
fmt1 db "Double %s",10,0
fmt2 db "Long double %s",0

.code ;11c+3aad - e/b
start:

invoke func, av, bv, cv, dv, ev
invoke func1, av1, bv1, cv1, dv1, ev1
invoke func2, av2, bv2, cv2, dv2, ev2

invoke crt_printf, addr fmt, Str$(res)
invoke crt_printf, addr fmt1, Str$(res1)
invoke crt_printf, addr fmt2, Str$(res2)

invoke MessageBox, NULL, Str$(res), offset MsgBoxCaption, MB_OK

invoke MessageBox, NULL, Str$(res1), offset MsgBoxCaption, MB_OK

invoke MessageBox, NULL, Str$(res2), offset MsgBoxCaption, MB_OK


invoke Sleep, 10000
invoke ExitProcess, NULL
;11c+3aad - e/b
func proc p1:real4, p2:real4, p3:real4, p4:real4, p5:real4
finit
fld real4 ptr [const11]
fld real4 ptr [p3]
fmul ;11c
fstp real4 ptr [res] 

finit
fld real4 ptr [p1]
fld real4 ptr [p1]
fmul ;aa
fld real4 ptr [p4]
fmul ;aad
fld real4 ptr [const12]
fmul ;3aad

fld real4 ptr [res]
fadd ;11c+3aad
fstp real4 ptr [res] 

fld real4 ptr [p5]
fld real4 ptr [p2]
fdiv ;e/b
fstp real4 ptr [res0]

fld real4 ptr [res]
fld real4 ptr [res0]
fsub ;11c+3aad - e/b
fstp real8 ptr [res]

ret
func endp


func1 proc p1:real8, p2:real8, p3:real8, p4:real8, p5:real8
finit
fld real8 ptr [const21]
fld real8 ptr [p3]
fmul ;11c
fstp real8 ptr [res1] 

finit
fld real8 ptr [p1]
fld real8 ptr [p1]
fmul ;aa
fld real8 ptr [p4]
fmul ;aad
fld real8 ptr [const22]
fmul ;3aad

fld real8 ptr [res1]
fadd ;11c+3aad
fstp real8 ptr [res1] 

fld real8 ptr [p5]
fld real8 ptr [p2]
fdiv ;e/b
fstp real8 ptr [res11]

fld real8 ptr [res1]
fld real8 ptr [res11]
fsub ;11c+3aad - e/b
fstp real8 ptr [res1]

ret
func1 endp


func2 proc p1:real10, p2:real10, p3:real10, p4:real10, p5:real10
finit
fld real10 ptr [const31]
fld real10 ptr [p3]
fmul ;11c
fstp real10 ptr [res2] 

finit
fld real10 ptr [p1]
fld real10 ptr [p1]
fmul ;aa
fld real10 ptr [p4]
fmul ;aad
fld real10 ptr [const32]
fmul ;3aad

fld real10 ptr [res2]
fadd ;11c+3aad
fstp real10 ptr [res2] 

fld real10 ptr [p5]
fld real10 ptr [p2]
fdiv ;e/b
fstp real10 ptr [res22]

fld real10 ptr [res2]
fld real10 ptr [res22]
fsub ;11c+3aad - e/b
fstp real10 ptr [res2]

ret
func2 endp

end start
