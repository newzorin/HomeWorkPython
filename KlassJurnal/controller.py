import model
import view


def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject())
    model.open_file()
    student = ""
    while True:
        journal = model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == "exit":
            break

        if student in journal:
           mark = int(view.what_marks())
           model.student_mark(student, mark)
           
        else:
            print("Ученик не найден")

    model.save_file()        

