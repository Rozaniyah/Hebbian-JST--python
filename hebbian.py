#Membuat inputan banyak data dan X
n = int(input("Input banyak data = " ))
xn = int(input("Input banyak X = "))

#inisialisasi bobot, bias, dan dw (Menginisialisasi nilai bobot,bias, dw nol, dimana bobot mengikuti banyak X sehingga menggunakan perulangan)
w = []
dw = []
for i in range(xn):
    w.append(0)
    dw.append(0)
b = 0

#tahapan inputan (Menginputkan X dan T)
x = []
t = []
for i in range(n):
    x.append([])
    for j in range(xn):
        x[i].append(int(input("Input X"+str(j+1)+" Data ke-"+str(i+1)+" = ")))
    t.append(int(input("Input T data ke-"+str(i+1)+" =")))
    
#tahapan learning (pengakurasian data, jika telah mencapai jumlah data "akurasi = banyak data", maka iterasi akan berhenti)
a = 0 #digunakan agar dapat masuk ke perulangan
ep = 1
print()
while a < n: 
    a = 0
    print("Epoch ke-", ep)
    #Untuk mengambil tampilan atas
    for i in range(xn):
        print ("X"+str(i+1), end = "\t")
    print("T", end = "\t")
    #Menginisialisasi bobot baru dengan Delta bobot dan Delta Bias
    for i in range(xn):
        print("DW"+str(i+1), end = "\t")
    print("DB", end = "\t")
    for i in range(xn):
        print("W"+str(i+1), end = "\t")
    print("B", end = "\t")
    print()
    
    #tahapan perubahan bobot 
    for i in range(n):
        for j in range(xn):
            dw[j] = x[i][j]*t[i] #Mencari dw dimana dw*t
        db = t[i] #delta bias sama dengan T dalam indeks i
        for j in range(xn):
            w[j] = w[j]+dw[j] #set bobot menjadi lama baru
        b = b + db  
        #tampilan 
        for j in range(xn):
            print(x[i][j], end ="\t")
        print(t[i], end = "\t")
        for j in range(xn):
            print(dw[j], end = "\t")
        print(db, end = "\t")
        for j in range (xn):
            print(w[j], end = "\t")
        print(b, end = "\t")
        print()  
        
        
    #Menampilkan bobot baru
    print()
    for i in range(xn):
        print("W"+str(i+1)+ "=", w[i])
    print("B = ", b)
    print()
    
    #tahapan hitung fungsi sumary
    for i in range(xn):
        print("X"+str(i+1), end = "\t")
    print("T", end = "\t")
    print("F(x,w)", end = "\t")
    print("Out", end = "\t")
    print("Akurasi")
    for i in range(n):
        for j in range(xn):
            print(x[i][j], end = "\t")
        print(t[i], end = "\t")
        fx = 0 #untuk permulaan nilai x yang kemudian digunakan untuk menambahkan bobot baru mengikuti banyak X yang ada
        for j in range(xn):
            fx = fx+(w[j]*x[i][j])
        fx = fx +b 
        print(fx, end = "\t")
        if (fx >= 0): #Mencari output target dengan output bipolar
            out = 1
        else:
            out = -1
        print(out, end = "\t")
        if out == t[i]: #Output sama dengan target, maka akurasinya true atau 1
            a += 1 #a++
            print("1")
        else:
            print("0")
    ep += 1 #menandakan pada epoch ke- berapa

    
#algoritma testing
print()
for i in range(xn):
     print("W"+str(i+1)+" =", w[i])
print("B = ", b) #Menampilkan akurasi bobot yang paling benar atau sudah fix
print()


tx = [] 
for i in range(xn):
    tx.append(int(input("Input X"+str(i+1)+" ="))) #input x tanpa target, karena target telah memenuhi

#fungsi sumary algoritma testing
fx = 0
for i in range(xn):
    fx = fx+(w[i]*tx[i])
fx = fx+b

print("Hasil Agoritma Learning")
print("FX = ", fx)
if (fx >= 0): #mengambil output yang ada di learning sebelumnya
    out = 1
else:
    out = -1
print("Output = ", out)


