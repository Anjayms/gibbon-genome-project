from gibbon1 import Gibbon_pheno
nleo_Geno = ["Aa", "8B2b", "Dd", "eE", "ff", "Gg", "7H5h", "JJ", "Kk", "Pp", "qq", "5R3r", "Tt", "4Y"]
wauyb_Geno = ["aa", "5B5b", "Dd", "eE", "Ff", "Gg", "5H7h", "Jj", "KK", "Pp", "QQ", "6R2r", "Tt", "2Y2y"]
sotiu_Geno = ["Aa", "3B7b", "Dd", "EE", "Ff", "Gg", "7H5h", "Jj", "KK", "Pp", "Qq", "3R5r", "tt", "3Yy"]
una_Geno = ["AA", "6B4b", "DD", "ee", "Ff", "Gg", "5H7h", "Jj", "kk", "pp", "qq", "5R3r", "Tt", "Y3y"]
kilao_Geno = ["Aa", "5B5b", "DD", "EE", "Ff", "Gg", "6H6h", "Jj", "Kk", "pp", "Qq", "2R6r", "tt", "2Y2y"]
Rouob_Geno = ["Aa", "6B4b", "dd", "EE", "ff", "Gg", "7H5h", "Jj", "Kk", "Pp", "QQ", "5R3r", "tt", "3Yy"]
Gyteu_Geno = ["AA", "2B8b", "Dd", "EE", "FF", "Gg", "9H3h", "JJ", "KK", "Pp", "Qq", "2R6r", "Tt", "4y"]
Jinya_Geno = ["Aa", "4B6b", "Dd", "EE", "Ff", "Gg", "6H6h", "JJ", "KK", "pp", "QQ", "2R6r", "Tt", "3Yy"]
Juluo_geno = ["Aa", "6B4b", "dd", "EE", "ff", "GG", "7H5h", "Jj", "kk", "Pp", "Qq", "3R5r", "Tt", "3Yy"]
Vuab_Geno = ["aa", "7B3b", "dd", "EE", "Ff", "GG", "5H7h", "Jj", "KK", "Pp", "Qq", "3R5r", "Tt" "3Yy"]



Nleo_Pheno = Gibbon_pheno("Nleo", 1, 0.0, "Dead", "Dead", "dead" "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", nleo_Geno)
Wauyb_Pheno = Gibbon_pheno("Wauyb", 1, 0.0, "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", wauyb_Geno) 
Sotiu_Pheno = Gibbon_pheno("Sotiu", 1, 7.3, False, "usually", "cursorial", 40.5, 56, "e", 1.6, "screams", "drops", sotiu_Geno)
Una_Pheno = Gibbon_pheno("Una", 1, 0.0, "Dead", "Dead", "Dead" "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", "Dead", una_Geno)
Kilao_Pheno = Gibbon_pheno("Kilao", 2, 23.6, False, "usually", "cursorial", 78, 80, "a", 1.6, "hoots", "swings", kilao_Geno)
Rouob_Pheno = Gibbon_pheno("Rouob", 2, 8.5, True, "usually", "cursorial", 40.5, 32, "e", 1.6, "hoots", "swings", Rouob_Geno)
Gyteu_Pheno = Gibbon_pheno("Gyteu", 2, 2.3, False, "always", "ambush", 0, 0, "z", 0.2, "screams", "drops", Gyteu_Geno)
Jinya_Pheno = Gibbon_pheno("Jinya", 2, 21.1, False, "usually", "ambush", 39, 48, "b", 1.6, "hoots", "drops", Jinya_Geno)
Juluo_Pheno = Gibbon_pheno("Juluo", 3, 6.4, True, "usually", "cursorial", 40.5, 37, "e", 1.6, "screams", "drops", Juluo_geno)
Vuab_Pheno = Gibbon_pheno("Juluo", 3, 6.0, False, "usually", "cursorial", 37.5, 29, "e", 1.6, "screams", "drops", Vuab_Geno)


dead = []
for i in [Nleo_Pheno, Wauyb_Pheno, Sotiu_Pheno, Una_Pheno, Kilao_Pheno, Rouob_Pheno, Gyteu_Pheno, Jinya_Pheno, Juluo_Pheno, Vuab_Pheno]:
    if i.fitness > 9:
        dead.append(i)


if len(dead) == 2:
    for i in dead:
        for j in dead:
            if i.name != j.name and i.name > j.name:
                for num in range(len(i.geno)):
                    if i.geno[num] == j.geno[num]:
                        print(i.name, j.name, j.geno[num])

elif len(dead) == 3:
    for i in dead:
        for j in dead:
            for a in dead:
                if i.name != j.name and j.name != a.name and j.name > i.name and i.name > a.name:
                    for num in range(len(i.geno)):
                        if i.geno[num] == j.geno[num] and i.geno[num] == a.geno[num]:
                            print(j.name, i.name, a.name, j.geno[num])

elif len(dead) == 4:
    for i in dead:
        for j in dead:
            for a in dead:
                for b in dead:
                    if i.name != j.name and j.name != a.name and a.name != b.name and i.name > j.name and j.name > a.name and a.name > b.name:
                        for num in range(len(i.geno)):
                            if i.geno[num] == j.geno[num] and i.geno[num] == a.geno[num] and a.geno[num] == b.geno[num]:
                                print(j.name, i.name, a.name, b.name, j.geno[num])

elif len(dead) == 5:
    for i in dead:
        for j in dead:
            for a in dead:
                for b in dead:
                    for h in dead:
                        if i.name != j.name and j.name != a.name and a.name != b.name and b.name != h in dead and i.name > j.name and j.name > a.name and a.name > b.name and b.name > h.name:
                            for num in range(len(i.geno)):
                                if i.geno[num] == j.geno[num] and i.geno[num] == a.geno[num] and a.geno[num] == b.geno[num] and b.geno[num] == h.geno[num]:
                                    print(j.name, i.name, a.name, b.name, h.name, j.geno[num])