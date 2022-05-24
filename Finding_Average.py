if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    valor = student_marks.get(query_name)
    value = round(sum(valor) / len(valor),2)
    print(f'{value:.2f}')
