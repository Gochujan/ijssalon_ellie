def presenteer(mijn_dict, totaal):
    for sleutel, waarde in mijn_dict.items():
        print(f"{sleutel}: {waarde}")
    print("=" * 25)
    print(f"totaal : {totaal}")