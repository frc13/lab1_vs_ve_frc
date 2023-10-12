s = 0  # Cəmi yadda saxlamaq üçün 0-a bərabər təyin edirik
n = 1  # Ardıcıllığın ilk elementi
e = 0.01  # E dəqiqliyi

while True:
    t = 1 / n  # Ardıcıllığın tək elementini hesablayırıq
    s = s + t  # Ardıcıllığın bu elementini cəmə əlavə edirik
    n = n + 1  # Növbəti elementə keçirik

    # Əgər cəm e dəqiqliyə çatdısa, döngüdən çıxırıq
    if t < e:
        break

print("Sonsuz ardclln cəmi:", s)
