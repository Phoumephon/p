print("========////ສະບາຍດີ ຍິນດີຕ້ອນຮັບສູ່ຮ້ານຊື້ຂາຍເງີນ///========")
print("")
print("====///ຍິນດີຕ້ອນຮັບສູ່ຮ້ານ ແລກ ປ່ຽນ ເງີນຕາ///===")
print("====///ເປີດໄຫ້ບໍລິການ 8:30 ຫາ 5:30///=====")
print("---------///ສະຖານທີ່ ບ້ານໂນນພະເນົາ///------ ")
print("---------///ເມືອງໄຊເສດຖາ///------")
print("---------////ນະຄອນລຫວງວຽງຈັນ///------")
print("")
choose = input("ຕ້ອງການຊື້ຂາຍ[ຊື້/ຂາຍ]=")
if choose == "ຊື້":
    print("===>ປະເພດເງີນແຕ່ລະປະເທດທີ່ຕ້ອງການຊື້<===")
    print("1.ອາເມຣິກາ")
    print("2.ຈີນ")
    print("3.ຫວຽດນາມ")
    print("4.ເກົາຫຼີ")
    print("5.ໄທ")
    print("6.ມຽນມາ")
    print("7.ສິງກະໂປ")
    print("8.ອອກຈາກໂປຣແກຣມ")
while True:
    a = int(input("ເລືອກຈຳນວນເງີນຂອງທ່ານທີ່ຕ້ອງການຈະຊື້="))
    if a == 1:
        print("1 USD ເທົ່າ ", 15000, "2 USD ເທົ່າ", 30000, "3 USD ເທົ່າ", 45000)
        print("ອາເມກາ")
    elif a == 2:
        print("1 CNY ເທົ່າ",20000,"20 CNY ເທົ່າ",30000,"30 CNY ເທົ່າ",50000)
        print("ຈີນ")
    elif a == 3:
        print("5 VND ເທົ່າ",15000,"10 VND",300000,"20 VND ເທົ່າ" ,550000)
        print("ຫວຽດນາມ")
    elif a == 4:
        print ("15 KRW ເທົ່າ",200000,"30 KRW",400000,"60 KRW ເທົ່າ" ,600000)
        print("ເກົາຫຼີ")
    elif a == 5:
        print("20 THB ເທົ່າ",250000,"35 THB",500000,"65 TH3B ເທົ່າ" ,650000)
        print("ໄທ")
    elif a == 6:
        print("25 KS ເທົ່າ",350000,"40 KS ",650000,"65 KS ເທົ່າ" ,750000)
        print("ມຽນມາ")
    elif a == 7:
        print("25 SGD ເທົ່າ",450000,"40 SGD ",750000,"65 SGD ເທົ່າ" ,850000)
        print("ສິງກະໂປ")