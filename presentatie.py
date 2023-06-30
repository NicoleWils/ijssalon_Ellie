def presenteer(d={},totaal=0):
    for item in d:
        print(item,":",d[item]," euro")
    print(35*"=")
    print(f"totaal : {totaal} euro")
# mijn_dict={"vis":10,"vlees":25,"overig":15}
# presenteer(mijn_dict,50)