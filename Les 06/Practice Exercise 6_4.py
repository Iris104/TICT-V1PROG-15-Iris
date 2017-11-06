studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]

def gemiddelde_per_student(studentencijfers):
    gemiddelde1  = studentencijfers[0]
    leerling1_1 = gemiddelde1[0]
    leerling1_2 = gemiddelde1[1]
    leerling1_3 = gemiddelde1[2]
    gemiddelde2 = studentencijfers[1]
    leerling2_1 = gemiddelde2[0]
    leerling2_2 = gemiddelde2[1]
    leerling2_3 = gemiddelde2[2]
    gemiddelde3 = studentencijfers[2]
    leerling3_1 = gemiddelde3[0]
    leerling3_2 = gemiddelde3[1]
    leerling3_3 = gemiddelde3[2]
    gemiddelde4 = studentencijfers[3]
    leerling4_1 = gemiddelde4[0]
    leerling4_2 = gemiddelde4[1]
    leerling4_3 = gemiddelde4[2]
    gemiddeldeleerling1 = (leerling1_1 + leerling1_2 + leerling1_3)/3
    gemiddeldeleerling2 = (leerling2_1 + leerling2_2 + leerling2_3)/3
    gemiddeldeleerling3 = (leerling3_1 + leerling3_2 + leerling3_3)/3
    gemiddeldeleerling4 = (leerling4_1 + leerling4_2 + leerling4_3)/3
    antw = [gemiddeldeleerling1, gemiddeldeleerling2, gemiddeldeleerling3, gemiddeldeleerling4]
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    gemiddelde = gemiddelde_per_student(studentencijfers)
    antw = (gemiddelde[0] + gemiddelde[1] + gemiddelde[2] +gemiddelde[3]) /4
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))
