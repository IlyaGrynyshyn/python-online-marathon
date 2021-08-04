class Testpaper:
    def __init__(self, subject, markscheme, pass_mark):
        self.subject = subject
        self.markscheme = markscheme
        self.pass_mark = pass_mark


class Student:
    tests_taken = "No tests taken"

    def __init__(self):
        self.tests_taken = Student.tests_taken

    def take_test(self, Testpaper, answer):
        self.answer = answer
        count = 0
        for i in range(len(self.answer)):
            if self.answer[i] == Testpaper.markscheme[i]:
                count += 1
        if count:
            self.pass_answer = str(round(count / len(Testpaper.markscheme) * 100)) + '%'
        else:
            self.pass_answer = '0%'
        if self.pass_answer < Testpaper.pass_mark:
            self.result = 'Failed!'
        else:
            self.result = 'Passed!'
        if self.tests_taken == "No tests taken":
            self.tests_taken = {}
        self.tests_taken[Testpaper.subject] = f"{self.result} ({self.pass_answer})"


paper1 = Testpaper("Maths", ["1A", "2C", "3D", "4A", "5A"], "60%")
paper2 = Testpaper("Chemistry", ["1C", "2C", "3D", "4A"], "75%")
paper3 = Testpaper("Computing", ["1D", "2C", "3C", "4B", "5D", "6C", "7A"], "75%")

student1 = Student()
student2 = Student()
student1.take_test(paper1, ["1A", "2D", "3D", "4A", "5A"])
print(student1.tests_taken)
