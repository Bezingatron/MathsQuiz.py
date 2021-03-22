import questions

class Question:
    def __init__(self, objective):
        # Initiates relevant question object and determines the question and correct answer
        if objective == "1N1":
            self.question = questions.Objective1N1()
        elif objective == "2N1":
            self.question = questions.Objective2N1()
        elif objective == "3N1":
            self.question = questions.Objective3N1()
        elif objective == "4N1":
            self.question = questions.Objective4N1()
        elif objective == "5N1":
            self.question = questions.Objective5N1()
        elif objective == "1N2a":
            self.question = questions.Objective1N2a()
        elif objective == "1N2b":
            self.question = questions.Objective1N2b()
        elif objective == "1N2c":
            self.question = questions.Objective1N2c()
        elif objective == "2N2a":
            self.question = questions.Objective2N2a()
        elif objective == "2N2b":
            self.question = questions.Objective2N2b()
        elif objective == "3N2a":
            self.question = questions.Objective3N2a()
        elif objective == "3N2b":
            self.question = questions.Objective3N2b()
        elif objective == "4N2a":
            self.question = questions.Objective4N2a()
        elif objective == "4N2b":
            self.question = questions.Objective4N2b()
        elif objective == "5N2":
            self.question = questions.Objective5N2()
        elif objective == "6N2":
            self.question = questions.Objective6N2()
        elif objective == "2N3":
            self.question = questions.Objective2N3()
        elif objective == "3N3":
            self.question = questions.Objective3N3()
        elif objective == "4N3a":
            self.question = questions.Objective4N3a()
        elif objective == "4N3b":
            self.question = questions.Objective4N3b()
        elif objective == "5N3a":
            self.question = questions.Objective5N3a()
        elif objective == "5N3b":
            self.question = questions.Objective5N3b()
        elif objective == "6N3":
            self.question = questions.Objective6N3()
        elif objective == "1N4":
            self.question = questions.Objective1N4()
        elif objective == "2N4":
            self.question = questions.Objective2N4()
        elif objective == "3N4":
            self.question = questions.Objective3N4()
        elif objective == "4N4a":
            self.question = questions.Objective4N4a()
        elif objective == "4N4b":
            self.question = questions.Objective4N4b()
        elif objective == "5N4":
            self.question = questions.Objective5N4()
        elif objective == "6N4":
            self.question = questions.Objective6N4()
        elif objective == "4N5":
            self.question = questions.Objective4N5()
        elif objective == "5N5":
            self.question = questions.Objective5N5()
        elif objective == "6N5":
            self.question = questions.Objective6N5()
        elif objective == "2N6":
            self.question = questions.Objective2N6()
        elif objective == "3N6":
            self.question = questions.Objective3N6()
        elif objective == "4N6":
            self.question = questions.Objective4N6()
        elif objective == "5N6":
            self.question = questions.Objective5N6()
        elif objective == "6N6":
            self.question = questions.Objective6N6()
        elif objective == "1C1":
            self.question = questions.Objective1C1()
        elif objective == "2C1":
            self.question = questions.Objective2C1()
        elif objective == "3C1":
            self.question = questions.Objective3C1()
        elif objective == "5C1":
            self.question = questions.Objective5C1()
        elif objective == "1C2a":
            self.question = questions.Objective1C2a()
        elif objective == "1C2b":
            self.question = questions.Objective1C2b()
        elif objective == "2C2a":
            self.question = questions.Objective2C2a()
        elif objective == "2C2b":
            self.question = questions.Objective2C2b()
        elif objective == "3C2":
            self.question = questions.Objective3C2()
        elif objective == "4C2":
            self.question = questions.Objective4C2()
        elif objective == "5C2":
            self.question = questions.Objective5C2()
        elif objective == "2C3":
            self.question = questions.Objective2C3()
        elif objective == "3C3":
            self.question = questions.Objective3C3()
        elif objective == "4C3":
            self.question = questions.Objective4C3()
        elif objective == "5C3":
            self.question = questions.Objective5C3()
        elif objective == "6C3":
            self.question = questions.Objective6C3()
        elif objective == "1C4":
            self.question = questions.Objective1C4()
        elif objective == "2C4":
            self.question = questions.Objective2C4()
        elif objective == "3C4":
            self.question = questions.Objective3C4()
        elif objective == "4C4":
            self.question = questions.Objective4C4()
        elif objective == "5C4":
            self.question = questions.Objective5C4()
        elif objective == "6C4":
            self.question = questions.Objective6C4()
        elif objective == "5C5a":
            self.question = questions.Objective5C5a()
        elif objective == "5C5b":
            self.question = questions.Objective5C5b()
        elif objective == "5C5c":
            self.question = questions.Objective5C5c()
        elif objective == "5C5d":
            self.question = questions.Objective5C5d()
        elif objective == "6C5":
            self.question = questions.Objective6C5()
        elif objective == "2C6":
            self.question = questions.Objective2C6()
        elif objective == "3C6":
            self.question = questions.Objective3C6()
        elif objective == "4C6a":
            self.question = questions.Objective4C6a()
        elif objective == "4C6b":
            self.question = questions.Objective4C6b()
        elif objective == "4C6c":
            self.question = questions.Objective4C6c()
        elif objective == "5C6a":
            self.question = questions.Objective5C6a()
        elif objective == "5C6b":
            self.question = questions.Objective5C6b()
        elif objective == "6C6":
            self.question = questions.Objective6C6()
        elif objective == "2C7":
            self.question = questions.Objective2C7()
        elif objective == "3C7":
            self.question = questions.Objective3C7()
        elif objective == "4C7":
            self.question = questions.Objective4C7()
        elif objective == "5C7a":
            self.question = questions.Objective5C7a()
        elif objective == "5C7b":
            self.question = questions.Objective5C7b()
        elif objective == "6C7a":
            self.question = questions.Objective6C7a()
        elif objective == "6C7b":
            self.question = questions.Objective6C7b()
        elif objective == "6C7c":
            self.question = questions.Objective6C7c()
        elif objective == "1C8":
            self.question = questions.Objective1C8()
        elif objective == "2C8":
            self.question = questions.Objective2C8()
        elif objective == "3C8":
            self.question = questions.Objective3C8()
        elif objective == "4C8":
            self.question = questions.Objective4C8()
        elif objective == "5C8a":
            self.question = questions.Objective5C8a()
        elif objective == "5C8b":
            self.question = questions.Objective5C8b()
        elif objective == "5C8c":
            self.question = questions.Objective5C8c()
        elif objective == "6C8":
            self.question = questions.Objective6C8()
        elif objective == "2C9a":
            self.question = questions.Objective2C9a()
        elif objective == "2C9b":
            self.question = questions.Objective2C9b()
        elif objective == "6C9":
            self.question = questions.Objective6C9()
        elif objective == "1F1a":
            self.question = questions.Objective1F1a()
        elif objective == "1F1b":
            self.question = questions.Objective1F1b()
        elif objective == "2F1a":
            self.question = questions.Objective2F1a()
        elif objective == "2F1b":
            self.question = questions.Objective2F1b()
        elif objective == "3F1a":
            self.question = questions.Objective3F1a()
        elif objective == "3F1b":
            self.question = questions.Objective3F1b()
        elif objective == "3F1c":
            self.question = questions.Objective3F1c()
        elif objective == "4F1":
            self.question = questions.Objective4F1()
        elif objective == "2F2":
            self.question = questions.Objective2F2()
        elif objective == "3F2":
            self.question = questions.Objective3F2()
        elif objective == "4F2":
            self.question = questions.Objective4F2()
        elif objective == "5F2a":
            self.question = questions.Objective5F2a()
        elif objective == "5F2b":
            self.question = questions.Objective5F2b()
        elif objective == "6F2":
            self.question = questions.Objective6F2()
        elif objective == "3F3":
            self.question = questions.Objective3F3()
        elif objective == "5F3":
            self.question = questions.Objective5F3()
        elif objective == "6F3":
            self.question = questions.Objective6F3()
        elif objective == "3F4":
            self.question = questions.Objective3F4()
        elif objective == "4F4":
            self.question = questions.Objective4F4()
        elif objective == "5F4":
            self.question = questions.Objective5F4()
        elif objective == "6F4":
            self.question = questions.Objective6F4()
        elif objective == "5F5":
            self.question = questions.Objective5F5()
        elif objective == "6F5a":
            self.question = questions.Objective6F5a()
        elif objective == "6F5b":
            self.question = questions.Objective6F5b()
        elif objective == "4F6a":
            self.question = questions.Objective4F6a()
        elif objective == "4F6b":
            self.question = questions.Objective4F6b()
        elif objective == "5F6a":
            self.question = questions.Objective5F6a()
        elif objective == "5F6b":
            self.question = questions.Objective5F6b()
        elif objective == "6F6":
            self.question = questions.Objective6F6()
        elif objective == "4F7":
            self.question = questions.Objective4F7()
        elif objective == "5F7":
            self.question = questions.Objective5F7()
        elif objective == "4F8":
            self.question = questions.Objective4F8()
        elif objective == "5F8":
            self.question = questions.Objective5F8()
        elif objective == "4F9":
            self.question = questions.Objective4F9()
        elif objective == "6F9a":
            self.question = questions.Objective6F9a()
        elif objective == "6F9b":
            self.question = questions.Objective6F9b()
        elif objective == "6F9c":
            self.question = questions.Objective6F9c()
        elif objective == "3F10":
            self.question = questions.Objective3F10()
        elif objective == "4F10a":
            self.question = questions.Objective4F10a()
        elif objective == "4F10b":
            self.question = questions.Objective4F10b()
        elif objective == "5F10":
            self.question = questions.Objective5F10()
        elif objective == "6F10":
            self.question = questions.Objective6F10()
        elif objective == "5F11":
            self.question = questions.Objective5F11()
        elif objective == "6F11":
            self.question = questions.Objective5F11()
        elif objective == "5F12":
            self.question = questions.Objective5F12()
        elif objective == "6R1":
            self.question = questions.Objective6R1()
        elif objective == "6R2":
            self.question = questions.Objective6R2()
        elif objective == "6R3":
            self.question = questions.Objective6R3()
        elif objective == "6R4":
            self.question = questions.Objective6R4()
        elif objective == "6A1":
            self.question = questions.Objective6A1()
        elif objective == "6A2":
            self.question = questions.Objective6A2()
        elif objective == "6A3":
            self.question = questions.Objective6A3()
        elif objective == "6A4":
            self.question = questions.Objective6A4()
        elif objective == "6A5":
            self.question = questions.Objective6A5()
        elif objective == "1M1":
            self.question = questions.Objective1M1()
        elif objective == "2M1":
            self.question = questions.Objective2M1()
        elif objective == "3M1a":
            self.question = questions.Objective3M1a()
        elif objective == "3M1b":
            self.question = questions.Objective3M1b()
        elif objective == "3M1c":
            self.question = questions.Objective3M1c()
        elif objective == "4M1":
            self.question = questions.Objective4M1()
        elif objective == "1M2":
            self.question = questions.Objective1M2()
        elif objective == "2M2":
            self.question = questions.Objective2M2()
        elif objective == "3M2a":
            self.question = questions.Objective3M2a()
        elif objective == "3M2b":
            self.question = questions.Objective3M2b()
        elif objective == "3M2c":
            self.question = questions.Objective3M2c()
        elif objective == "4M2":
            self.question = questions.Objective4M2()
        elif objective == "1M3":
            self.question = questions.Objective1M3()
        elif objective == "2M3a":
            self.question = questions.Objective2M3a()
        elif objective == "2M3b":
            self.question = questions.Objective2M3b()
        elif objective == "1M4a":
            self.question = questions.Objective1M4a()
        elif objective == "1M4b":
            self.question = questions.Objective1M4b()
        elif objective == "1M4c":
            self.question = questions.Objective1M4c()
        elif objective == "2M4a":
            self.question = questions.Objective2M4a()
        elif objective == "2M4b":
            self.question = questions.Objective2M4b()
        elif objective == "2M4c":
            self.question = questions.Objective2M4c()
        elif objective == "3M4a":
            self.question = questions.Objective3M4a()
        elif objective == "3M4b":
            self.question = questions.Objective3M4b()
        elif objective == "3M4c":
            self.question = questions.Objective3M4c()
        elif objective == "3M4d":
            self.question = questions.Objective3M4d()
        elif objective == "3M4e":
            self.question = questions.Objective3M4e()
        elif objective == "3M4f":
            self.question = questions.Objective3M4f()
        elif objective == "4M4a":
            self.question = questions.Objective4M4a()
        elif objective == "4M4b":
            self.question = questions.Objective4M4b()
        elif objective == "4M4c":
            self.question = questions.Objective4M4c()
        elif objective == "5M4":
            self.question = questions.Objective5M4()
        elif objective == "4M5":
            self.question = questions.Objective4M5()
        elif objective == "5M5":
            self.question = questions.Objective5M5()
        elif objective == "6M5":
            self.question = questions.Objective6M5()
        elif objective == "5M6":
            self.question = questions.Objective5M6()
        elif objective == "6M6":
            self.question = questions.Objective6M6()
        elif objective == "3M7":
            self.question = questions.Objective3M7()
        elif objective == "4M7a":
            self.question = questions.Objective4M7a()
        elif objective == "4M7b":
            self.question = questions.Objective4M7b()
        elif objective == "5M7a":
            self.question = questions.Objective5M7a()
        elif objective == "5M7b":
            self.question = questions.Objective5M7b()
        elif objective == "6M7a":
            self.question = questions.Objective6M7a()
        elif objective == "6M7b":
            self.question = questions.Objective6M7b()
        elif objective == "6M7c":
            self.question = questions.Objective6M7c()
        elif objective == "5M8":
            self.question = questions.Objective5M8()
        elif objective == "6M8a":
            self.question = questions.Objective6M8a()
        elif objective == "6M8b":
            self.question = questions.Objective6M8b()
        elif objective == "2M9":
            self.question = questions.Objective2M9()
        elif objective == "3M9a":
            self.question = questions.Objective3M9a()
        elif objective == "3M9b":
            self.question = questions.Objective3M9b()
        elif objective == "3M9c":
            self.question = questions.Objective3M9c()
        elif objective == "3M9d":
            self.question = questions.Objective3M9d()
        elif objective == "4M9":
            self.question = questions.Objective4M9()
        elif objective == "5M9a":
            self.question = questions.Objective5M9a()
        elif objective == "5M9b":
            self.question = questions.Objective5M9b()
        elif objective == "5M9c":
            self.question = questions.Objective5M9c()
        elif objective == "5M9d":
            self.question = questions.Objective5M9d()
        elif objective == "6M9":
            self.question = questions.Objective6M9()
        elif objective == "1G1a":
            self.question = questions.Objective1G1a()
        elif objective == "1G1b":
            self.question = questions.Objective1G1b()
        elif objective == "2G1a":
            self.question = questions.Objective2G1a()
        elif objective == "2G1b":
            self.question = questions.Objective2G1b()
        elif objective == "2G2a":
            self.question = questions.Objective2G2a()
        elif objective == "2G2b":
            self.question = questions.Objective2G2b()
        elif objective == "3G2":
            self.question = questions.Objective3G2()
        elif objective == "4G2a":
            self.question = questions.Objective4G2a()
        elif objective == "4G2b":
            self.question = questions.Objective4G2b()
        elif objective == "4G2c":
            self.question = questions.Objective4G2c()
        elif objective == "5G2a":
            self.question = questions.Objective5G2a()
        elif objective == "5G2b":
            self.question = questions.Objective5G2b()
        elif objective == "6G2a":
            self.question = questions.Objective6G2a()
        elif objective == "6G2b":
            self.question = questions.Objective6G2b()
        elif objective == "2G3":
            self.question = questions.Objective2G3()
        elif objective == "3G3a":
            self.question = questions.Objective3G3a()
        elif objective == "3G3b":
            self.question = questions.Objective3G3b()
        elif objective == "5G3":
            self.question = questions.Objective5G3()
        elif objective == "6G3a":
            self.question = questions.Objective6G3a()
        elif objective == "6G3b":
            self.question = questions.Objective6G3b()
        elif objective == "3G4a":
            self.question = questions.Objective3G4a()
        elif objective == "3G4b":
            self.question = questions.Objective3G4b()
        elif objective == "4G4":
            self.question = questions.Objective4G4()
        elif objective == "5G4a":
            self.question = questions.Objective5G4a()
        elif objective == "5G4b":
            self.question = questions.Objective5G4b()
        elif objective == "5G4c":
            self.question = questions.Objective5G4c()
        elif objective == "6G4a":
            self.question = questions.Objective6G4a()
        elif objective == "6G4b":
            self.question = questions.Objective6G4b()
        elif objective == "6G5":
            self.question = questions.Objective6G5()
        elif objective == "2P1":
            self.question = questions.Objective2P1()
        elif objective == "1P2":
            self.question = questions.Objective1P2()
        elif objective == "2P2":
            self.question = questions.Objective2P2()
        elif objective == "4P2":
            self.question = questions.Objective4P2()
        elif objective == "5P2":
            self.question = questions.Objective5P2()
        elif objective == "6P2":
            self.question = questions.Objective6P2()
        elif objective == "4P3a":
            self.question = questions.Objective4P3a()
        elif objective == "4P3b":
            self.question = questions.Objective4P3b()
        elif objective == "6P3":
            self.question = questions.Objective6P3()
        elif objective == "2S1":
            self.question = questions.Objective2S1()
        elif objective == "3S1":
            self.question = questions.Objective3S1()
        elif objective == "4S1":
            self.question = questions.Objective4S1()
        elif objective == "5S1":
            self.question = questions.Objective5S1()
        elif objective == "6S1":
            self.question = questions.Objective6S1()
        elif objective == "2S2a":
            self.question = questions.Objective2S2a()
        elif objective == "2S2b":
            self.question = questions.Objective2S2b()
        elif objective == "3S2":
            self.question = questions.Objective3S2()
        elif objective == "4S2":
            self.question = questions.Objective4S2()
        elif objective == "5S2":
            self.question = questions.Objective5S2()
        elif objective == "6S3":
            self.question = questions.Objective6S3()

    def correct_answer(self):
        return str(self.question.correct_answer).lower()

    def question_text(self):
        return self.question.question_text
