def solution(a:list)->list:
    # print("Befor sorting person with theri height", a)
    count_trees = 0    
    people = []
    for x in a:
        if x == -1:
            count_trees = count_trees + 1            
        else:
            people.append(x)
    
    # print("Pick up person from origin row", people)
    person_sorted_by_height = sorted(people)
    # print("After sorted:", person_sorted_by_height)
    for index, value in enumerate(a):
        if value == -1:
            person_sorted_by_height.insert(index, -1)    
    print(person_sorted_by_height)
    return person_sorted_by_height
if __name__ == "__main__":
    solution([-1, 150, 190, 170, -1, -1, 160, 180])
    solution([-1, -1, -1, -1, -1])
    solution([-1])
    solution([4, 2, 9, 11, 2, 16])
    solution([2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1])
    solution([23, 54, -1, 43, 1, -1, -1, 77, -1, -1, -1, 3])