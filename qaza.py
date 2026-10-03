
nam_qaza=str(input("nam qaza ra vared konid:"))
tedad=int(input("tedad sefares ra vared konid:"))

if nam_qaza=='pitza':
    print(tedad*250000)
elif nam_qaza=='burger':
    print(tedad*180000)
elif nam_qaza=='sandevich':
    print(tedad*120000)
elif nam_qaza!='pitza' or nam_qaza!='burger' or nam_qaza!='sandevich':
    print("nam qaza eshtebah")
money=float(input("mablaq kharid ra vared konid:"))
ersal=(input("noe ersal ra vared konid (addi_sari):"))

if ersal=='addi' and money<2000000 :
    print("majmu kharid shoma:",money+50000)
elif ersal=='sari':
    print("majmu kharid shoma:",money+100000)
if money>=2000000 and ersal=='addi':
    print("majmu kharid shpma:",money)
