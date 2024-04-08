class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(sandwiches[0] in students):
            if sandwiches[0] == students[0]:
                tempo = sandwiches[0]
                sandwiches = sandwiches[1:]
                sandwiches.append(tempo)
                students = students[1:]

            else:
                tempo = students[0]
                students = students[1:]
                students.append(tempo)
        return len(students)
